"""Compute Stage-1/Stage-2 nDCG@5, MAP@5, MRR@5."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, StageRankingResult
from finagent_mesh.metrics import ranking as rm


def run_metrics(state: AgentState) -> dict[str, Any]:
    updates: dict[str, Any] = {}
    if state.stage1 is not None:
        if not state.example.stage1_labels:
            updates["stage1"] = state.stage1.model_copy(
                update={"skipped_reason": state.stage1.skipped_reason or "missing_stage1_labels"}
            )
        elif state.stage1.ordered_ids:
            s1 = state.stage1.model_copy(
                update={
                    "ndcg_at_5": rm.ndcg_at_k(state.stage1.ordered_ids, state.example.stage1_labels, 5),
                    "map_at_5": rm.map_at_k(state.stage1.ordered_ids, state.example.stage1_labels, 5),
                    "mrr_at_5": rm.mrr_at_k(state.stage1.ordered_ids, state.example.stage1_labels, 5),
                }
            )
            updates["stage1"] = s1
    if state.stage2 is not None:
        if state.stage2.skipped_reason:
            updates["stage2"] = state.stage2
        elif not state.example.stage2_labels:
            updates["stage2"] = state.stage2.model_copy(
                update={"skipped_reason": "missing_stage2_labels"}
            )
        elif state.stage2.ordered_ids:
            s2 = state.stage2.model_copy(
                update={
                    "ndcg_at_5": rm.ndcg_at_k(state.stage2.ordered_ids, state.example.stage2_labels, 5),
                    "map_at_5": rm.map_at_k(state.stage2.ordered_ids, state.example.stage2_labels, 5),
                    "mrr_at_5": rm.mrr_at_k(state.stage2.ordered_ids, state.example.stage2_labels, 5),
                }
            )
            updates["stage2"] = s2
    return updates
