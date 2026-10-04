"""Collect and export per-run metrics summaries."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from finagent_mesh.agent.state import AgentState


@dataclass
class RunAggregator:
    run_id: str
    records: list[dict[str, Any]] = field(default_factory=list)

    def add(self, state: AgentState) -> None:
        self.records.append(
            {
                "example_id": state.example.example_id,
                "stage1": state.stage1.model_dump() if state.stage1 else None,
                "stage2": state.stage2.model_dump() if state.stage2 else None,
                "answer_score": state.answer_score.model_dump() if state.answer_score else None,
                "error": state.error,
            }
        )

    def add_payload(self, example_id: str, ranking: dict[str, Any] | None, synthesis: dict[str, Any] | None) -> None:
        self.records.append(
            {
                "example_id": example_id,
                "stage1": (ranking or {}).get("stage1"),
                "stage2": (ranking or {}).get("stage2"),
                "answer_score": (synthesis or {}).get("answer_score"),
                "error": None,
            }
        )

    def summary(self) -> dict[str, Any]:
        def avg(stage: str, key: str) -> float | None:
            vals = []
            for r in self.records:
                s = r.get(stage) or {}
                v = s.get(key)
                if v is not None:
                    vals.append(float(v))
            return sum(vals) / len(vals) if vals else None

        em_vals = [
            float(r["answer_score"]["normalized_em"])
            for r in self.records
            if r.get("answer_score") and r["answer_score"].get("status") == "scored"
            and r["answer_score"].get("normalized_em") is not None
        ]
        f1_vals = [
            float(r["answer_score"]["token_f1"])
            for r in self.records
            if r.get("answer_score") and r["answer_score"].get("status") == "scored"
            and r["answer_score"].get("token_f1") is not None
        ]
        return {
            "run_id": self.run_id,
            "n_examples": len(self.records),
            "stage1": {
                "ndcg_at_5": avg("stage1", "ndcg_at_5"),
                "map_at_5": avg("stage1", "map_at_5"),
                "mrr_at_5": avg("stage1", "mrr_at_5"),
            },
            "stage2": {
                "ndcg_at_5": avg("stage2", "ndcg_at_5"),
                "map_at_5": avg("stage2", "map_at_5"),
                "mrr_at_5": avg("stage2", "mrr_at_5"),
            },
            "answer": {
                "normalized_em": sum(em_vals) / len(em_vals) if em_vals else None,
                "token_f1": sum(f1_vals) / len(f1_vals) if f1_vals else None,
                "n_scored": len(em_vals),
            },
        }

    def export(self, path: Path | None = None) -> dict[str, Any]:
        payload = {"summary": self.summary(), "records": self.records}
        if path is not None:
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload
