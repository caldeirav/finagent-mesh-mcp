"""Laya ModernBERT edge Choice adapter (HTTP sidecar; optional local Transformers)."""

from __future__ import annotations

import time
from typing import Any

from finagent_mesh.clients.engines.http_base import HttpSystemOneAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.metrics.ranking import stable_rank


class LayaAdapter(HttpSystemOneAdapter):
    """Prefers local Transformers when weights + package available; else HTTP sidecar."""

    def __init__(self, cfg: EngineConfiguration) -> None:
        super().__init__(cfg)
        self._local = None
        if cfg.weights_ref:
            try:
                import transformers  # noqa: F401

                self._local = "transformers"
            except ImportError:
                self._local = None

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive != "choice":
            raise ValueError(f"Laya supports choice only; got {primitive}")
        if self._local and self.cfg.weights_ref:
            return self._local_decide(query, candidates)
        meta = dict(metadata or {})
        meta["laya_mode"] = "edge"
        return super().decide(primitive, query, candidates, meta)

    def _local_decide(self, query: str, candidates: list[dict[str, str]]) -> dict[str, Any]:
        # Lightweight lexical stand-in when Transformers is present but full
        # ModernBERT weights wiring is operator-supplied (degraded CPU path).
        started = time.perf_counter()
        self.decide_attempts += 1
        q = set(query.lower().split())
        scored: list[tuple[str, float]] = []
        for c in candidates:
            text = (c.get("text") or "").lower()
            overlap = float(len(q.intersection(text.split())))
            scored.append((c["id"], overlap + 0.001 * len(text)))
        ids = [s[0] for s in scored]
        scores = [s[1] for s in scored]
        ranked = stable_rank(ids, scores)
        total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": "choice",
            "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
            "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
        }
