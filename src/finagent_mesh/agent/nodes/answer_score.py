"""Persist answer-quality scores."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, AnswerScore
from finagent_mesh.metrics.answer import normalized_exact_match, token_f1


def run_answer_score(state: AgentState) -> dict[str, Any]:
    label = state.example.answer_label
    pred = state.synthesized_answer or ""
    if label is None or str(label).strip() == "":
        return {
            "answer_score": AnswerScore(
                prediction=pred,
                label=None,
                status="skipped_no_label",
            )
        }
    return {
        "answer_score": AnswerScore(
            prediction=pred,
            label=str(label),
            normalized_em=normalized_exact_match(pred, str(label)),
            token_f1=token_f1(pred, str(label)),
            status="scored",
        )
    }
