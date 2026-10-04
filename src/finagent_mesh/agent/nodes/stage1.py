"""Stage 1 document-type Choice ranking."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, StageRankingResult
from finagent_mesh.agent.types import DOC_TYPES
from finagent_mesh.clients.open_decision import OpenDecisionClient


def run_stage1(state: AgentState, client: OpenDecisionClient) -> dict[str, Any]:
    example = state.example
    if not example.stage1_labels and not example.query_text:
        result = StageRankingResult(
            stage="stage1",
            ordered_ids=[],
            scores=[],
            skipped_reason="missing_stage1_labels_or_query",
        )
        return {"stage1": result, "error": None}

    candidates = [{"id": dt, "text": f"Document type {dt} for firm {example.firm_id}"} for dt in DOC_TYPES]
    resp = client.decide("choice", example.query_text, candidates, {"firm_id": example.firm_id})
    ranking = sorted(resp["ranking"], key=lambda r: r["rank"])
    ordered = [r["id"] for r in ranking]
    scores = [float(r["score"]) for r in ranking]
    top1 = ordered[0] if ordered else None
    result = StageRankingResult(
        stage="stage1",
        ordered_ids=ordered,
        scores=scores,
        decision_distribution={k: float(v) for k, v in resp.get("distribution", {}).items()},
    )
    return {"stage1": result, "top1_doc_type": top1, "error": None}
