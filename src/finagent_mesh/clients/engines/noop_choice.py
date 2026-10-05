"""No-op Choice adapter for collapsed-stage (one-shot) pairs."""

from __future__ import annotations

import time
from typing import Any

from finagent_mesh.agent.types import DOC_TYPES
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.metrics.ranking import stable_rank


class NoopChoiceAdapter:
    """Returns a sentinel Top-1 that Stage-2 interprets as 'rank all chunks'."""

    SENTINEL = "__all__"

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
        if primitive != "choice":
            raise ValueError(f"noop-choice supports choice only; got {primitive}")
        self.decide_attempts += 1
        started = time.perf_counter()
        ids = [c["id"] for c in candidates] or list(DOC_TYPES)
        # Put sentinel first so Top-1 is __all__; keep remaining types after
        if self.SENTINEL not in ids:
            ordered_ids = [self.SENTINEL, *[i for i in ids if i != self.SENTINEL]]
        else:
            ordered_ids = [self.SENTINEL] + [i for i in ids if i != self.SENTINEL]
        scores = [float(len(ordered_ids) - i) for i in range(len(ordered_ids))]
        ranked = stable_rank(ordered_ids, scores)
        # Force sentinel at rank 1 regardless of stable_rank id tie-breaks
        ranking = [{"id": self.SENTINEL, "score": 1e9, "rank": 1}]
        for i, (cid, s, _) in enumerate(ranked):
            if cid == self.SENTINEL:
                continue
            ranking.append({"id": cid, "score": float(s), "rank": len(ranking) + 1})
        total = sum(max(r["score"], 0.0) for r in ranking) or 1.0
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": "choice",
            "ranking": ranking,
            "distribution": {r["id"]: max(r["score"], 0.0) / total for r in ranking},
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
            "backend": "noop_inprocess",
            "collapsed_stages": True,
        }
