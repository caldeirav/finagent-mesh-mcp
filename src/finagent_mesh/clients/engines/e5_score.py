"""In-process E5 bi-encoder Stage-2 Score adapter."""

from __future__ import annotations

import os
import time
from typing import Any

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.metrics.ranking import stable_rank

_MODEL = None
_MODEL_ID: str | None = None


def _get_model(model_id: str):
    global _MODEL, _MODEL_ID
    if _MODEL is not None and _MODEL_ID == model_id:
        return _MODEL
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise OpenDecisionError(
            "sentence-transformers is required for e5-base; install with uv sync --extra real"
        ) from exc
    _MODEL = SentenceTransformer(model_id)
    _MODEL_ID = model_id
    return _MODEL


class E5ScoreAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.weights = cfg.weights_ref or os.getenv("E5_WEIGHTS", "intfloat/e5-base-v2")
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
            raise ValueError(f"E5 supports score; got {primitive}")
        self.decide_attempts += 1
        if not candidates:
            raise OpenDecisionError(f"{self.engine_id}: empty candidate list")
        started = time.perf_counter()
        model = _get_model(self.weights)
        q_emb = model.encode([f"query: {query}"], normalize_embeddings=True)
        passages = [f"passage: {(c.get('text') or '')[:2000]}" for c in candidates]
        p_emb = model.encode(passages, normalize_embeddings=True, batch_size=32)
        # cosine == dot for normalized vectors
        import numpy as np

        scores = (p_emb @ q_emb[0]).astype(float).tolist()
        ids = [c["id"] for c in candidates]
        ranked = stable_rank(ids, scores)
        total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": primitive,
            "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
            "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
            "backend": "e5_inprocess",
            "model_id": self.weights,
        }
