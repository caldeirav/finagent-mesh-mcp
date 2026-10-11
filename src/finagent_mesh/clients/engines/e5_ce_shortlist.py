"""E5 bi-encoder shortlist then CrossEncoder rerank (IR ceiling Stage-2)."""

from __future__ import annotations

import os
import time
from typing import Any

from finagent_mesh.clients.engines.e5_score import E5ScoreAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.metrics.ranking import stable_rank

_CE_MODEL = None
_CE_MODEL_ID: str | None = None


def _get_cross_encoder(model_id: str):
    """Load CrossEncoder; fail closed (no silent E5-only under this engine id)."""
    global _CE_MODEL, _CE_MODEL_ID
    if _CE_MODEL is not None and _CE_MODEL_ID == model_id:
        return _CE_MODEL
    try:
        from sentence_transformers import CrossEncoder
    except ImportError as exc:
        raise OpenDecisionError(
            "sentence-transformers is required for e5-ce-shortlist; "
            "install with uv sync --extra real"
        ) from exc
    from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth

    token = ensure_hf_hub_auth()
    try:
        # Context7 / sbert: CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
        kwargs: dict[str, Any] = {}
        if token:
            kwargs["token"] = token
        _CE_MODEL = CrossEncoder(model_id, **kwargs)
    except TypeError:
        # Older sentence-transformers may not accept token=
        try:
            _CE_MODEL = CrossEncoder(model_id)
        except Exception as exc:  # noqa: BLE001
            raise OpenDecisionError(
                f"Failed to load CrossEncoder weights {model_id!r}: {exc}"
            ) from exc
    except Exception as exc:  # noqa: BLE001
        raise OpenDecisionError(
            f"Failed to load CrossEncoder weights {model_id!r}: {exc}"
        ) from exc
    _CE_MODEL_ID = model_id
    return _CE_MODEL


class E5CeShortlistAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.shortlist_k = int(os.getenv("CE_SHORTLIST_K", "32"))
        self.ce_weights = cfg.weights_ref or os.getenv(
            "CE_WEIGHTS", "cross-encoder/ms-marco-MiniLM-L6-v2"
        )
        self.e5_weights = os.getenv("E5_WEIGHTS", "intfloat/e5-base-v2")
        self._e5 = E5ScoreAdapter(
            EngineConfiguration(
                config_id="e5-base",
                family="dense-ir",
                display_name="e5",
                primitives=["score"],
                primary_stages=["stage2"],
                base_url="http://localhost:8702",
                backend="e5_inprocess",
                model_revision="e5-base-v2",
                weights_ref=self.e5_weights,
                is_heavy_gpu=False,
                is_light_edge=False,
            )
        )
        self.last_latency_ms: float | None = None
        self.parse_failures = 0
        self.decide_attempts = 0

    def health(self) -> tuple[bool, str]:
        return True, "ok"

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive not in {"score", "action_cache"}:
            raise ValueError(f"e5-ce-shortlist supports score; got {primitive}")
        self.decide_attempts += 1
        if not candidates:
            raise OpenDecisionError(f"{self.engine_id}: empty candidate list")
        if self.shortlist_k <= 0:
            raise OpenDecisionError(
                f"{self.engine_id}: CE_SHORTLIST_K must be > 0 (got {self.shortlist_k})"
            )
        started = time.perf_counter()
        e5 = self._e5.decide("score", query, candidates, metadata)
        ordered = [r["id"] for r in sorted(e5["ranking"], key=lambda r: r["rank"])]
        keep_ids = ordered[: self.shortlist_k]
        by_id = {c["id"]: c for c in candidates}
        short = [by_id[i] for i in keep_ids if i in by_id]
        if not short:
            short = candidates[: self.shortlist_k]

        # Fail closed: CE load/predict errors must not fall back to E5-only ranks
        # under the lux-e5-ce / e5-ce-shortlist identity.
        ce = _get_cross_encoder(self.ce_weights)
        passages = [(c.get("text") or "")[:2000] for c in short]
        try:
            ranks = ce.rank(query, passages)
        except Exception as exc:  # noqa: BLE001
            raise OpenDecisionError(
                f"{self.engine_id}: CrossEncoder.rank failed ({self.ce_weights}): {exc}"
            ) from exc

        short_ids = [c["id"] for c in short]
        ce_scores: dict[str, float] = {}
        for row in ranks:
            corpus_id = int(row["corpus_id"])
            if 0 <= corpus_id < len(short_ids):
                ce_scores[short_ids[corpus_id]] = float(row["score"])
        if len(ce_scores) != len(short_ids):
            # Some CE versions return partial; score missing via predict pairs
            missing = [c for c in short if c["id"] not in ce_scores]
            if missing:
                try:
                    pair_scores = ce.predict(
                        [(query, (c.get("text") or "")[:2000]) for c in missing]
                    )
                except Exception as exc:  # noqa: BLE001
                    raise OpenDecisionError(
                        f"{self.engine_id}: CrossEncoder.predict failed: {exc}"
                    ) from exc
                for c, s in zip(missing, pair_scores):
                    ce_scores[c["id"]] = float(s)

        ids = list(ce_scores.keys())
        scores = [ce_scores[i] for i in ids]
        ranked = stable_rank(ids, scores)
        ranking = [{"id": i, "score": s, "rank": r} for i, s, r in ranked]
        ranked_ids = {r["id"] for r in ranking}
        extra = [c for c in candidates if c["id"] not in ranked_ids]
        if extra:
            base = min((float(r["score"]) for r in ranking), default=0.0) - 1.0
            start_rank = len(ranking) + 1
            for i, c in enumerate(extra):
                ranking.append({"id": c["id"], "score": base - i, "rank": start_rank + i})

        total = sum(max(float(r["score"]), 0.0) for r in ranking) or 1.0
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": primitive,
            "ranking": ranking,
            "distribution": {
                r["id"]: max(float(r["score"]), 0.0) / total for r in ranking
            },
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
            "backend": "e5_ce_shortlist",
            "shortlist_k": self.shortlist_k,
            "shortlist_method": "e5",
            "rerank_method": "cross_encoder",
            "ce_model_id": self.ce_weights,
            "e5_model_id": self.e5_weights,
            "n_candidates": len(candidates),
            "n_shortlisted": len(short),
        }
