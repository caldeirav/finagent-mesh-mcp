"""In-process real System-1 inference backends (no lexical sidecar).

Backends:
- decision20: HuggingFace Decision-2.0 `AutoModel.system_one` (Kai / Lux)
  Choice = listwise id→text; Score = ordinal 2–10 levels (pointwise over passages)
- laya: ModernBERT-style ranking via transformers Autograd / AutoModel
- ar: Qwen instruct JSON choice generation
- clm: contrastive-lm Engine.rank when installed (no Decision-2.0 Score fallback)
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


def _torch_device():
    import torch

    raw = (os.getenv("SYSTEMONE_DEVICE") or "auto").strip().lower()
    if raw in {"", "auto"}:
        if torch.cuda.is_available():
            return torch.device("cuda")
        return torch.device("cpu")
    return torch.device(raw)


def _torch_dtype(device):
    import torch

    if device.type == "cuda":
        return torch.bfloat16
    return torch.float32


def _place_model(model, *, label: str, cast_dtype: bool = True):
    """Move weights to CUDA/CPU. Decision-2.0 forbids dtype casts."""
    import torch

    device = _torch_device()
    dtype = _torch_dtype(device)
    if cast_dtype:
        try:
            model = model.to(device=device, dtype=dtype)
        except TypeError:
            log(f"{label}: runtime forbids dtype cast; moving to {device} only")
            model = model.to(device=device)
    else:
        log(f"{label}: moving to {device} (Decision-2.0 reloads natively; can take several minutes)…")
        model = model.to(device=device)
    model.eval()
    extra = ""
    if device.type == "cuda":
        extra = f" ({torch.cuda.get_device_name(device)})"
    log(f"{label} on {device}{extra}")
    return model, device


@lru_cache(maxsize=4)
def _load_decision20(model_id: str):
    _require_torch()
    from transformers import AutoModel

    log(f"Loading Decision-2.0 weights {model_id} (first call downloads from Hugging Face)…")
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
    model, device = _place_model(model, label=f"Decision-2.0 {model_id}", cast_dtype=False)
    return model, device


@lru_cache(maxsize=2)
def _load_ar(model_id: str):
    _require_torch()
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log(f"Loading AR causal LM {model_id} (first call may download)…")
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    model, device = _place_model(model, label=f"AR {model_id}")
    return tok, model, device


@lru_cache(maxsize=2)
def _load_embedder(model_id: str):
    _require_torch()
    from transformers import AutoModel, AutoTokenizer

    log(f"Loading embedder {model_id} (first call may download)…")
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
    model, device = _place_model(model, label=f"embedder {model_id}")
    return tok, model, device


def _mean_pool(last_hidden, attention_mask):
    import torch

    mask = attention_mask.unsqueeze(-1).expand(last_hidden.size()).float()
    summed = (last_hidden * mask).sum(dim=1)
    counts = mask.sum(dim=1).clamp(min=1e-9)
    return summed / counts


def _criterion_chars() -> int:
    raw = os.getenv("SYSTEMONE_CRITERION_CHARS", "240")
    try:
        return max(32, int(raw))
    except ValueError:
        return 240


# Decision-2.0 Score is an ordinal scale (exactly 2–10 level descriptions),
# not a list of passages. FinAgentBench Stage-2 uses pointwise Score: shared
# query state + one Score question per passage (passage text in instructions).
RELEVANCE_SCORE_CRITERIA: list[str] = [
    "Irrelevant to the query",
    "Marginally related but does not answer the query",
    "Partially answers the query",
    "Directly and fully answers the query",
]


def _score_batch_size(model_id: str) -> int:
    raw = os.getenv("SYSTEMONE_SCORE_BATCH", "").strip()
    if raw:
        try:
            return max(1, int(raw))
        except ValueError:
            pass
    lowered = model_id.lower()
    if "kai" in lowered or "0.6b" in lowered:
        return 4
    # Ordinal Score packs passage text into each question; keep batches small.
    return 4


def _probs_from_answer(ans: Any, candidates: list[dict[str, str]]) -> dict[str, float]:
    probs: dict[str, float] = {}
    if not isinstance(ans, dict):
        return probs
    if ans.get("error"):
        return probs
    raw_probs = ans.get("probabilities") or ans.get("scores") or ans.get("values")
    if isinstance(raw_probs, dict):
        probs = {str(k): float(v) for k, v in raw_probs.items()}
    elif isinstance(raw_probs, list) and raw_probs:
        for cand, val in zip(candidates, raw_probs):
            try:
                probs[cand["id"]] = float(val)
            except (TypeError, ValueError):
                continue
    if not probs and ans.get("choice") is not None:
        probs = {str(ans["choice"]): 1.0}
    return probs


def _ranking_payload(
    *,
    primitive: str,
    ids: list[str],
    scores: list[float],
    latency_ms: float,
    backend: str,
    model_id: str,
) -> dict[str, Any]:
    ranked = stable_rank(ids, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "latency_ms": latency_ms,
        "backend": backend,
        "model_id": model_id,
    }


def _system_one_choice_rank(
    model: Any,
    *,
    query: str,
    candidates: list[dict[str, str]],
    model_id: str,
) -> dict[str, Any]:
    """Listwise Choice: criteria is id → text (2–255 options)."""
    if len(candidates) < 2:
        raise RealInferError(
            f"Decision-2.0 Choice needs ≥2 candidates; got {len(candidates)}"
        )
    limit = _criterion_chars()
    criteria = {c["id"]: (c.get("text") or c["id"])[:limit] for c in candidates}
    started = time.perf_counter()
    result = model.system_one(
        state=query[:4000],
        questions={
            "rank": {
                "type": "choice",
                "instructions": "Rank which candidate best answers the financial query.",
                "criteria": criteria,
            }
        },
    )
    latency_ms = (time.perf_counter() - started) * 1000.0
    if isinstance(result, dict) and result.get("max_length_exceeded"):
        raise RealInferError(
            f"Decision-2.0 max_length_exceeded n_cand={len(candidates)} "
            f"chars={limit}; lower SYSTEMONE_SCORE_BATCH / SYSTEMONE_CRITERION_CHARS"
        )
    answers = result.get("answers") if isinstance(result, dict) else None
    if answers is None:
        answers = result
    ans = answers.get("rank") if isinstance(answers, dict) else None
    if isinstance(ans, dict) and ans.get("error"):
        raise RealInferError(f"Decision-2.0 Choice error: {ans.get('error')}")
    probs = _probs_from_answer(ans, candidates)
    if not probs:
        raise RealInferError(f"Decision-2.0 returned unusable Choice answers: {ans!r}")

    id_by_text = {(c.get("text") or c["id"])[:limit]: c["id"] for c in candidates}
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
    return _ranking_payload(
        primitive="choice",
        ids=ids,
        scores=[float(mapped.get(i, 0.0)) for i in ids],
        latency_ms=latency_ms,
        backend="decision20",
        model_id=model_id,
    )


def _system_one_ordinal_score_batch(
    model: Any,
    *,
    query: str,
    candidates: list[dict[str, str]],
) -> tuple[dict[str, float], float]:
    """Pointwise ordinal Score: 2–10 levels; one question per passage."""
    if not candidates:
        return {}, 0.0
    limit = _criterion_chars()
    questions: dict[str, dict[str, Any]] = {}
    for c in candidates:
        cid = str(c["id"])
        passage = (c.get("text") or cid)[:limit]
        questions[cid] = {
            "type": "score",
            "instructions": (
                "Rate how well the following passage answers the financial query.\n\n"
                f"Passage:\n{passage}"
            ),
            "criteria": list(RELEVANCE_SCORE_CRITERIA),
        }
    started = time.perf_counter()
    result = model.system_one(state=query[:4000], questions=questions)
    latency_ms = (time.perf_counter() - started) * 1000.0
    if isinstance(result, dict) and result.get("max_length_exceeded"):
        raise RealInferError(
            f"Decision-2.0 max_length_exceeded n_cand={len(candidates)} "
            f"chars={limit}; lower SYSTEMONE_SCORE_BATCH / SYSTEMONE_CRITERION_CHARS"
        )
    answers = result.get("answers") if isinstance(result, dict) else None
    if not isinstance(answers, dict):
        raise RealInferError(f"Decision-2.0 Score returned no answers: {result!r}")
    scores: dict[str, float] = {}
    errors: list[str] = []
    for c in candidates:
        cid = str(c["id"])
        ans = answers.get(cid)
        if not isinstance(ans, dict):
            errors.append(f"{cid}: missing")
            scores[cid] = 0.0
            continue
        if ans.get("error"):
            errors.append(f"{cid}: {ans.get('error')}")
            scores[cid] = 0.0
            continue
        raw = ans.get("score")
        try:
            scores[cid] = float(raw)
        except (TypeError, ValueError):
            errors.append(f"{cid}: bad score {raw!r}")
            scores[cid] = 0.0
    if errors and all(v == 0.0 for v in scores.values()):
        raise RealInferError(
            "Decision-2.0 Score failed for all candidates: " + "; ".join(errors[:5])
        )
    return scores, latency_ms


# Back-compat alias used by older tests / callers
def _system_one_rank(
    model: Any,
    *,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
    model_id: str,
) -> dict[str, Any]:
    if primitive == "choice":
        return _system_one_choice_rank(
            model, query=query, candidates=candidates, model_id=model_id
        )
    scores, latency_ms = _system_one_ordinal_score_batch(
        model, query=query, candidates=candidates
    )
    ids = [c["id"] for c in candidates]
    return _ranking_payload(
        primitive="score",
        ids=ids,
        scores=[float(scores.get(i, 0.0)) for i in ids],
        latency_ms=latency_ms,
        backend="decision20_ordinal_score",
        model_id=model_id,
    )


def decide_decision20(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """Choice/score via Decision-2.0 system_one API.

    - Choice: listwise id→text criteria (filing types / small option sets).
    - Score: native ordinal Score (2–10 levels) applied pointwise to passages.
      Passing chunk texts as Score criteria causes ``invalid_question``.
    """
    model, _device = _load_decision20(model_id)
    if primitive == "choice":
        batch = _score_batch_size(model_id)
        if len(candidates) <= batch:
            return _system_one_choice_rank(
                model, query=query, candidates=candidates, model_id=model_id
            )
        log(
            f"Decision-2.0 {model_id}: Choice-ranking {len(candidates)} candidates "
            f"in batches of {batch}"
        )
        merged: dict[str, float] = {}
        latency_ms = 0.0
        for i in range(0, len(candidates), batch):
            part = _system_one_choice_rank(
                model,
                query=query,
                candidates=candidates[i : i + batch],
                model_id=model_id,
            )
            latency_ms += float(part.get("latency_ms") or 0.0)
            for row in part["ranking"]:
                merged[str(row["id"])] = float(row["score"])
        ids = [c["id"] for c in candidates]
        return _ranking_payload(
            primitive="choice",
            ids=ids,
            scores=[merged.get(i, 0.0) for i in ids],
            latency_ms=latency_ms,
            backend="decision20_batched",
            model_id=model_id,
        )

    batch = _score_batch_size(model_id)
    if len(candidates) > batch:
        log(
            f"Decision-2.0 {model_id}: ordinal Score on {len(candidates)} passages "
            f"in batches of {batch} (truncated to {_criterion_chars()} chars)"
        )
    merged_scores: dict[str, float] = {}
    latency_ms = 0.0
    for i in range(0, len(candidates), batch):
        part_scores, part_ms = _system_one_ordinal_score_batch(
            model,
            query=query,
            candidates=candidates[i : i + batch],
        )
        latency_ms += part_ms
        merged_scores.update(part_scores)
    ids = [c["id"] for c in candidates]
    return _ranking_payload(
        primitive="score",
        ids=ids,
        scores=[float(merged_scores.get(i, 0.0)) for i in ids],
        latency_ms=latency_ms,
        backend="decision20_ordinal_score"
        if len(candidates) <= batch
        else "decision20_ordinal_score_batched",
        model_id=model_id,
    )


def decide_embed_rank(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
) -> dict[str, Any]:
    """Dense cosine ranking (Laya / embedding baselines)."""
    import torch

    tok, model, device = _load_embedder(model_id)
    started = time.perf_counter()
    texts = [query] + [f"{c['id']}: {c.get('text') or ''}" for c in candidates]
    enc = tok(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
    enc = {k: v.to(device) for k, v in enc.items()}
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

    tok, model, device = _load_ar(model_id)
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
    inputs = {k: v.to(device) for k, v in inputs.items()}
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


def decide_anyjev(
    *,
    model_id: str,
    query: str,
    candidates: list[dict[str, str]],
    primitive: str,
    mode: str = "l0",
) -> dict[str, Any]:
    """AnyJev L0: cyclic option permutations + mean scores on the configured backbone.

    The registry backbone is Decision-2.0 Lux until a packaged AnyJev runtime exists.
    That is the L0 algorithm on those weights — not a silent swap to Kai.
    """
    if primitive != "choice":
        raise RealInferError(
            "AnyJev L0/L1 is a Stage-1 Choice engine; it does not score Stage-2 chunks"
        )
    n = len(candidates)
    if n == 0:
        raise RealInferError("AnyJev Choice requires candidates")
    acc = {c["id"]: 0.0 for c in candidates}
    latency_ms = 0.0
    log(f"AnyJev {mode}: {n} cyclic permutations on backbone {model_id}")
    for shift in range(n):
        rotated = candidates[shift:] + candidates[:shift]
        part = decide_decision20(
            model_id=model_id,
            query=query,
            candidates=rotated,
            primitive="choice",
        )
        latency_ms += float(part.get("latency_ms") or 0.0)
        for row in part["ranking"]:
            acc[str(row["id"])] += float(row["score"])
    ids = [c["id"] for c in candidates]
    scores = [acc[i] / float(n) for i in ids]
    ranked = stable_rank(ids, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": primitive,
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "latency_ms": latency_ms,
        "backend": f"anyjev_{mode}",
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
    """CLM Action Cache / rank: Qwen3-8B encoder + Contrastive-LM heads."""
    from finagent_mesh.clients.engines.clm_runtime import (
        CLM_ENCODER_DEFAULT,
        CLM_INSTALL_HINT,
        load_clm_engine,
    )

    started = time.perf_counter()
    try:
        if emb_url:
            os.environ["CLM_EMB_URL"] = emb_url
        encoder_id = os.getenv("CLM_ENCODER_ID", CLM_ENCODER_DEFAULT)
        engine = load_clm_engine(encoder_id)
    except ImportError as exc:
        raise RealInferError(CLM_INSTALL_HINT) from exc
    texts = [(c.get("text") or c["id"])[:4000] for c in candidates]
    ranked_raw = engine.rank(
        query,
        texts,
        instructions="Rank which passage best answers the financial query.",
    )
    latency_ms = (time.perf_counter() - started) * 1000.0
    by_text: dict[str, list[str]] = {}
    for c, text in zip(candidates, texts):
        by_text.setdefault(text, []).append(c["id"])
    ids: list[str] = []
    scores: list[float] = []
    for item in ranked_raw:
        cand = item.get("candidate") if isinstance(item, dict) else str(item)
        score = float(item.get("prob", item.get("score", 0.0))) if isinstance(item, dict) else 0.0
        bucket = by_text.get(cand) or [str(cand)]
        ids.append(bucket.pop(0) if bucket else str(cand))
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
        "encoder_id": os.getenv("CLM_ENCODER_ID", CLM_ENCODER_DEFAULT),
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
    if family == "vllm-sr":
        return decide_decision20(
            model_id=model_id, query=query, candidates=candidates, primitive=primitive
        )
    if family == "anyjev":
        engine_id = (os.getenv("SYSTEMONE_ENGINE_ID") or "").lower()
        mode = "l1" if "l1" in engine_id else "l0"
        return decide_anyjev(
            model_id=model_id,
            query=query,
            candidates=candidates,
            primitive=primitive,
            mode=mode,
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
