"""Frozen Lux Choice adapter — returns Top-1 from paper-n200-full records."""

from __future__ import annotations

import time
from typing import Any

from finagent_mesh.agent.types import DOC_TYPES
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.unsloth.types import FrozenStage1Record

# Populated by run_unsloth_eval before matrix execution
_FROZEN_RECORDS: dict[str, FrozenStage1Record] = {}


def set_frozen_stage1_records(records: dict[str, FrozenStage1Record]) -> None:
    global _FROZEN_RECORDS
    _FROZEN_RECORDS = dict(records)


def clear_frozen_stage1_records() -> None:
    global _FROZEN_RECORDS
    _FROZEN_RECORDS = {}


class FrozenLuxChoiceAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.last_latency_ms: float | None = None
        self.parse_failures = 0
        self.decide_attempts = 0

    def health(self) -> tuple[bool, str]:
        if not _FROZEN_RECORDS:
            return False, "frozen Stage-1 records not loaded"
        return True, f"ok ({len(_FROZEN_RECORDS)} records)"

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive != "choice":
            raise ValueError(f"frozen-lux-choice supports choice only; got {primitive}")
        self.decide_attempts += 1
        started = time.perf_counter()
        meta = metadata or {}
        eid = str(meta.get("example_id") or "")
        if not eid:
            raise OpenDecisionError(
                f"{self.engine_id}: metadata.example_id required for frozen Choice"
            )
        rec = _FROZEN_RECORDS.get(eid)
        if rec is None:
            raise OpenDecisionError(
                f"{self.engine_id}: no frozen Stage-1 record for example_id={eid!r}"
            )
        top1 = rec.top1_doc_type
        ids = [c["id"] for c in candidates] or list(DOC_TYPES)
        if top1 and top1 not in ids:
            ids = [top1, *ids]
        ordered = list(rec.stage1_ordered_ids) if rec.stage1_ordered_ids else []
        if top1:
            ordered = [top1] + [i for i in (ordered or ids) if i != top1]
        elif not ordered:
            ordered = list(ids)
        scores = list(rec.stage1_scores)
        if len(scores) < len(ordered):
            scores = [float(len(ordered) - i) for i in range(len(ordered))]
        ranking = [
            {"id": cid, "score": float(scores[i]), "rank": i + 1}
            for i, cid in enumerate(ordered)
        ]
        total = sum(max(r["score"], 0.0) for r in ranking) or 1.0
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": "choice",
            "ranking": ranking,
            "distribution": {r["id"]: max(r["score"], 0.0) / total for r in ranking},
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
            "backend": "frozen_lux_choice",
            "frozen_stage1": True,
            "frozen_source": rec.source,
            "empty_top1": rec.empty_top1,
        }
