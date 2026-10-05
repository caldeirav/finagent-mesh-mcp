"""In-process BM25 Stage-2 Score adapter."""

from __future__ import annotations

import re
import time
from typing import Any

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.metrics.ranking import stable_rank


_TOKEN = re.compile(r"[a-z0-9]+", re.I)


def _tokenize(text: str) -> list[str]:
    return _TOKEN.findall((text or "").lower())


class Bm25ScoreAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
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
            raise ValueError(f"BM25 supports score; got {primitive}")
        self.decide_attempts += 1
        if not candidates:
            raise OpenDecisionError(f"{self.engine_id}: empty candidate list")
        started = time.perf_counter()
        try:
            from rank_bm25 import BM25Okapi
        except ImportError as exc:
            raise OpenDecisionError(
                "rank-bm25 is required for bm25-stage2; install with uv sync --extra real"
            ) from exc

        corpus = [_tokenize(c.get("text") or "") for c in candidates]
        if all(len(t) == 0 for t in corpus):
            # Fall back to uniform tiny scores so ranking is deterministic by id
            ids = [c["id"] for c in candidates]
            scores = [0.0] * len(ids)
        else:
            bm25 = BM25Okapi(corpus)
            q_tokens = _tokenize(query)
            scores = [float(s) for s in bm25.get_scores(q_tokens)]
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
            "backend": "bm25_inprocess",
        }
