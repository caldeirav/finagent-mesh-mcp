"""In-process real System-1 inference backends (no lexical sidecar).

Backends:
- decision20: HuggingFace Decision-2.0 `AutoModel.system_one` (Kai / Lux)
- laya: ModernBERT-style ranking via transformers Autograd / AutoModel
- ar: Qwen instruct JSON choice generation
- clm: contrastive-lm Engine.rank when installed; else Decision-2.0 score fallback
"""

from __future__ import annotations

import json
import os
import re
import time
from functools import lru_cache
from typing import Any

from finagent_mesh.metrics.ranking import stable_rank
from finagent_mesh.runtime.progress import log


class RealInferError(RuntimeError):
    pass


def _require_torch():
    try:
        import torch  # noqa: F401
        from transformers import AutoModel  # noqa: F401
    except ImportError as exc:
        raise RealInferError(
            "Real inference requires optional deps: "
            "`uv sync --extra real` (torch, transformers>=5.17)"
        ) from exc


@lru_cache(maxsize=4)
def _load_decision20(model_id: str):
    _require_torch()
    from transformers import AutoModel

    log(f"Loading Decision-2.0 weights {model_id} (first call downloads from Hugging Face)…")
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
    log(f"Loaded Decision-2.0 {model_id}")
    return model


@lru_cache(maxsize=2)
def _load_ar(model_id: str):
    _require_torch()
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log(f"Loading AR causal LM {model_id} (first call may download)…")
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    log(f"Loaded AR {model_id}")
    return tok, model


@lru_cache(maxsize=2)
def _load_embedder(model_id: str):
    _require_torch()
    from transformers import AutoModel, AutoTokenizer

    log(f"Loading embedder {model_id} (first call may download)…")
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
    model.eval()
    log(f"Loaded embedder {model_id}")
    return tok, model


def _mean_pool(last_hidden, attention_mask):
    import torch

    mask = attention_mask.unsqueeze(-1).expand(last_hidden.size()).float()
    summed = (last_hidden * mask).sum(dim=1)
    counts = mask.sum(dim=1).clamp(min=1e-9)
    return summed / counts


def decide_decision20(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """Choice/score via Decision-2.0 system_one API."""
    model = _load_decision20(model_id)
    criteria = {c["id"]: (c.get("text") or c["id"])[:500] for c in candidates}
    qtype = "choice" if primitive == "choice" else "score"
    started = time.perf_counter()
    result = model.system_one(
        state=query,
        questions={
            "rank": {
                "type": qtype,
                "instructions": "Rank which candidate best answers the financial query.",
                "criteria": criteria
                if qtype == "choice"
                else list(criteria.values()),
            }
        },
    )
    latency_ms = (time.perf_counter() - started) * 1000.0
    answers = result.get("answers") or result
    ans = answers.get("rank") if isinstance(answers, dict) else None
    probs: dict[str, float] = {}
    if isinstance(ans, dict):
        probs = {
            str(k): float(v)
            for k, v in (ans.get("probabilities") or ans.get("scores") or {}).items()
        }
        # Map criterion text back to ids when score mode used text list
        if not probs and ans.get("choice") is not None:
            choice = str(ans["choice"])
            probs = {choice: 1.0}
    if not probs:
        # Fall back: use criteria keys with uniform if API shape differs
        raise RealInferError(f"Decision-2.0 returned unusable answers: {ans!r}")

    # Normalize keys to candidate ids
    id_by_text = {(c.get("text") or c["id"])[:500]: c["id"] for c in candidates}
    mapped: dict[str, float] = {}
    for k, v in probs.items():
        if k in criteria:
            mapped[k] = v
        elif k in id_by_text:
            mapped[id_by_text[k]] = v
        else:
            mapped[k] = v
    for c in candidates:
        mapped.setdefault(c["id"], 0.0)

    ids = [c["id"] for c in candidates]
    scores = [float(mapped.get(i, 0.0)) for i in ids]
    ranked = stable_rank(ids, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "latency_ms": latency_ms,
        "backend": "decision20",
        "model_id": model_id,
    }


def decide_embed_rank(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """Dense cosine ranking (Laya / embedding baselines)."""
    import torch

    tok, model = _load_embedder(model_id)
    started = time.perf_counter()
    texts = [query] + [f"{c['id']}: {c.get('text') or ''}" for c in candidates]
    enc = tok(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        out = model(**enc)
        hidden = getattr(out, "last_hidden_state", None)
        if hidden is None:
            raise RealInferError(f"Embedder {model_id} produced no last_hidden_state")
        emb = _mean_pool(hidden, enc["attention_mask"])
        emb = torch.nn.functional.normalize(emb, p=2, dim=1)
    q = emb[0]
    scores = (emb[1:] @ q).tolist()
    latency_ms = (time.perf_counter() - started) * 1000.0
    ids = [c["id"] for c in candidates]
    ranked = stable_rank(ids, [float(s) for s in scores])
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "latency_ms": latency_ms,
        "backend": "embed_rank",
        "model_id": model_id,
    }


def decide_ar_json(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """Autoregressive JSON ordered_ids baseline."""
    import torch

    tok, model = _load_ar(model_id)
    cand_blob = json.dumps(
        [{"id": c["id"], "text": (c.get("text") or "")[:300]} for c in candidates]
    )
    prompt = (
        "You rank financial retrieval candidates. Reply with ONLY JSON: "
        '{"ordered_ids":["id1","id2",...],"scores":[1.0,0.9,...]}\n'
        f"Query: {query}\nCandidates: {cand_blob}\nJSON:"
    )
    started = time.perf_counter()
    inputs = tok(prompt, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=False,
            pad_token_id=tok.eos_token_id,
        )
    text = tok.decode(out[0][inputs["input_ids"].shape[-1] :], skip_special_tokens=True)
    latency_ms = (time.perf_counter() - started) * 1000.0
    match = re.search(r"\{.*\}", text, flags=re.S)
    if not match:
        raise RealInferError(f"AR JSON parse failure; raw={text[:200]!r}")
    try:
        parsed = json.loads(match.group(0))
        ordered = list(parsed.get("ordered_ids") or [])
        scores = [float(x) for x in (parsed.get("scores") or [])]
    except Exception as exc:  # noqa: BLE001
        raise RealInferError(f"AR JSON parse failure: {exc}; raw={text[:200]!r}") from exc
    if not ordered:
        raise RealInferError("AR JSON missing ordered_ids")
    if len(scores) != len(ordered):
        scores = [float(len(ordered) - i) for i in range(len(ordered))]
    ranked = stable_rank(ordered, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "raw_json": match.group(0),
        "latency_ms": latency_ms,
        "backend": "ar_json",
        "model_id": model_id,
    }


def decide_clm(
    *,
    model_id: str,
    emb_url: str | None,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """CLM Action Cache / rank via contrastive-lm when available."""
    started = time.perf_counter()
    try:
        from clm import Engine  # type: ignore
    except ImportError:
        # Fall back to Decision-2.0 scoring with model_id if clm not installed
        return decide_decision20(
            model_id=os.getenv("CLM_FALLBACK_DECISION_MODEL", "vllm-sr/Decision-2.0-Kai-0.6B"),
            query=query,
            candidates=candidates,
            primitive="score" if primitive != "choice" else "choice",
        )

    url = emb_url or os.getenv("CLM_EMB_URL", "http://127.0.0.1:8090/v1/embeddings")
    engine = Engine(emb_url=url)
    texts = [c.get("text") or c["id"] for c in candidates]
    ranked_raw = engine.rank(query, texts)
    latency_ms = (time.perf_counter() - started) * 1000.0
    # Map back to ids by text
    by_text = {(c.get("text") or c["id"]): c["id"] for c in candidates}
    ids: list[str] = []
    scores: list[float] = []
    for item in ranked_raw:
        cand = item.get("candidate") if isinstance(item, dict) else str(item)
        score = float(item.get("prob", item.get("score", 0.0))) if isinstance(item, dict) else 0.0
        ids.append(by_text.get(cand, cand))
        scores.append(score)
    ranked = stable_rank(ids, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "latency_ms": latency_ms,
        "backend": "clm",
        "model_id": model_id,
    }


def infer_for_family(
    *,
    family: str,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
    emb_url: str | None = None,
) -> dict[str, Any]:
    if family in {"vllm-sr", "anyjev"}:
        # AnyJev L0/L1: until anyjev runtime is packaged, use Decision-2.0-compatible
        # system_one path on the configured weights (Qwen3-8B decision checkpoint).
        return decide_decision20(
            model_id=model_id, query=query, candidates=candidates, primitive=primitive
        )
    if family == "laya":
        return decide_embed_rank(
            model_id=model_id, query=query, candidates=candidates, primitive=primitive
        )
    if family == "ar-baseline":
        return decide_ar_json(
            model_id=model_id, query=query, candidates=candidates, primitive=primitive
        )
    if family == "clm":
        return decide_clm(
            model_id=model_id,
            emb_url=emb_url,
            query=query,
            candidates=candidates,
            primitive=primitive,
        )
    raise RealInferError(f"No real backend for family={family}")
