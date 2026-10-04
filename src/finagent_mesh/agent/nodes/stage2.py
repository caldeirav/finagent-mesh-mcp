"""Stage 2 chunk ranking over Top-1 Stage-1 document type only."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, PassageChunk, StageRankingResult
from finagent_mesh.clients.open_decision import OpenDecisionClient


def run_stage2(state: AgentState, client: OpenDecisionClient) -> dict[str, Any]:
    top1 = state.top1_doc_type
    if not top1:
        return {
            "stage2": StageRankingResult(
                stage="stage2",
                ordered_ids=[],
                scores=[],
                skipped_reason="missing_top1_doc_type",
            ),
            "stage2_chunks": [],
            "error": "missing_top1_doc_type",
        }

    chunks = [c for c in state.example.chunks if c.doc_type == top1]
    if not chunks:
        return {
            "stage2": StageRankingResult(
                stage="stage2",
                ordered_ids=[],
                scores=[],
                skipped_reason="empty_top1_chunks",
            ),
            "stage2_chunks": [],
            "error": "empty_top1_chunks",
        }

    candidates = [{"id": c.chunk_id, "text": c.text} for c in chunks]
    resp = client.decide(
        "score",
        state.example.query_text,
        candidates,
        {"doc_type": top1, "firm_id": state.example.firm_id},
    )
    ranking = sorted(resp["ranking"], key=lambda r: r["rank"])
    ordered = [r["id"] for r in ranking]
    scores = [float(r["score"]) for r in ranking]
    by_id = {c.chunk_id: c for c in chunks}
    ranked_chunks: list[PassageChunk] = []
    for r in ranking:
        c = by_id[r["id"]]
        ranked_chunks.append(
            c.model_copy(update={"score": float(r["score"]), "rank": int(r["rank"])})
        )
    result = StageRankingResult(
        stage="stage2",
        ordered_ids=ordered,
        scores=scores,
        decision_distribution={k: float(v) for k, v in resp.get("distribution", {}).items()},
    )
    return {"stage2": result, "stage2_chunks": ranked_chunks, "error": None}
