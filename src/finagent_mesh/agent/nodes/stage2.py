"""Stage 2 chunk ranking over Top-1 (or yield-recovered) document type."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, PassageChunk, StageRankingResult
from finagent_mesh.agent.yield_recovery import select_effective_doc_type
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
            "original_top1_doc_type": None,
            "original_top1_empty": True,
            "effective_doc_type": None,
            "yield_recovery_used": False,
            "yield_recovery_attempted_types": [],
        }

    ordered_ids = list(state.stage1.ordered_ids) if state.stage1 else []
    selection = select_effective_doc_type(
        original_top1=top1,
        ordered_ids=ordered_ids,
        chunks=list(state.example.chunks),
        recovery_enabled=bool(state.yield_recovery_enabled),
        order_missing=bool(state.stage1_order_missing),
    )

    audit: dict[str, Any] = {
        "original_top1_doc_type": selection.original_top1,
        "original_top1_empty": selection.original_top1_empty,
        "effective_doc_type": selection.effective_doc_type,
        "yield_recovery_used": selection.yield_recovery_used,
        "yield_recovery_attempted_types": list(selection.attempted_types),
        # top1_doc_type stays original Choice Top-1 for recall compatibility
        "top1_doc_type": top1,
    }
    if selection.skipped_missing_order:
        audit["n_recovery_skipped_missing_order"] = 1

    effective = selection.effective_doc_type or top1

    # Collapsed one-shot baseline: rank all chunks (noop-choice Top-1 = __all__)
    if effective == "__all__":
        chunks = list(state.example.chunks)
    else:
        chunks = [c for c in state.example.chunks if c.doc_type == effective]

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
            **audit,
        }

    candidates = [{"id": c.chunk_id, "text": c.text} for c in chunks]
    meta: dict[str, Any] = {"doc_type": effective, "firm_id": state.example.firm_id}
    if effective == "__all__":
        meta["one_shot_chunks"] = True
        meta["collapsed_stages"] = True
    if selection.yield_recovery_used:
        meta["yield_recovery_used"] = True
        meta["original_top1_doc_type"] = top1
    resp = client.decide(
        "score",
        state.example.query_text,
        candidates,
        meta,
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
    return {
        "stage2": result,
        "stage2_chunks": ranked_chunks,
        "error": None,
        **audit,
    }
