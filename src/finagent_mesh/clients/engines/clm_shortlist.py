"""BM25 shortlist then CLM Score hybrid Stage-2 adapter."""

from __future__ import annotations

import os
import time
from typing import Any

from finagent_mesh.clients.engines.bm25_score import Bm25ScoreAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration, create_adapter, load_registry
from finagent_mesh.clients.open_decision import OpenDecisionError


class ClmShortlistAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.shortlist_k = int(os.getenv("CLM_SHORTLIST_K", "32"))
        self._bm25 = Bm25ScoreAdapter(
            EngineConfiguration(
                config_id="bm25-stage2",
                family="lexical-ir",
                display_name="bm25",
                primitives=["score"],
                primary_stages=["stage2"],
                base_url="http://localhost:8701",
                backend="bm25_inprocess",
                model_revision="bm25-okapi",
                is_heavy_gpu=False,
                is_light_edge=True,
            )
        )
        self._clm = None
        self.last_latency_ms: float | None = None
        self.parse_failures = 0
        self.decide_attempts = 0

    def _clm_adapter(self):
        if self._clm is None:
            reg = load_registry()
            self._clm = create_adapter("clm-8b", reg)
        return self._clm

    def health(self) -> tuple[bool, str]:
        return self._clm_adapter().health()

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive not in {"score", "action_cache"}:
            raise ValueError(f"clm-shortlist supports score; got {primitive}")
        self.decide_attempts += 1
        if not candidates:
            raise OpenDecisionError(f"{self.engine_id}: empty candidate list")
        started = time.perf_counter()
        bm = self._bm25.decide("score", query, candidates, metadata)
        ordered = [r["id"] for r in sorted(bm["ranking"], key=lambda r: r["rank"])]
        keep = set(ordered[: self.shortlist_k])
        short = [c for c in candidates if c["id"] in keep]
        if not short:
            short = candidates[: self.shortlist_k]
        data = self._clm_adapter().decide("score", query, short, metadata)
        # Append remaining candidates at the end with low scores so ranks cover full list
        ranked_ids = {r["id"] for r in data.get("ranking") or []}
        extra = [c for c in candidates if c["id"] not in ranked_ids]
        if extra:
            ranking = list(data.get("ranking") or [])
            base = min((float(r["score"]) for r in ranking), default=0.0) - 1.0
            start_rank = len(ranking) + 1
            for i, c in enumerate(extra):
                ranking.append({"id": c["id"], "score": base - i, "rank": start_rank + i})
            data["ranking"] = ranking
        data["engine"] = self.engine_id
        data["model_revision"] = self.model_revision
        data["backend"] = "clm_shortlist"
        data["shortlist_k"] = self.shortlist_k
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        data["latency_ms"] = self.last_latency_ms
        return data
