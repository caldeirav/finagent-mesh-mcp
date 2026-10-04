"""MLflow tracing helpers."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

from finagent_mesh.agent.state import AgentState


def setup_mlflow(tracking_uri: str) -> None:
    import os

    import mlflow

    # MLflow 3.x puts the local filesystem store in maintenance mode by default.
    os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")
    mlflow.set_tracking_uri(tracking_uri)


@contextmanager
def example_run(run_id: str, example_id: str) -> Iterator[Any]:
    import mlflow

    with mlflow.start_run(run_name=f"{run_id}:{example_id}", nested=True) as active:
        mlflow.set_tags({"run_id": run_id, "example_id": example_id})
        yield active


def log_agent_state(state: AgentState) -> None:
    import mlflow

    if state.stage1:
        mlflow.log_dict(state.stage1.decision_distribution, "stage1_distribution.json")
        if state.stage1.ndcg_at_5 is not None:
            mlflow.log_metrics(
                {
                    "stage1_ndcg_at_5": state.stage1.ndcg_at_5,
                    "stage1_map_at_5": state.stage1.map_at_5 or 0.0,
                    "stage1_mrr_at_5": state.stage1.mrr_at_5 or 0.0,
                }
            )
    if state.stage2:
        mlflow.log_dict(state.stage2.decision_distribution, "stage2_distribution.json")
        if state.stage2.ndcg_at_5 is not None:
            mlflow.log_metrics(
                {
                    "stage2_ndcg_at_5": state.stage2.ndcg_at_5,
                    "stage2_map_at_5": state.stage2.map_at_5 or 0.0,
                    "stage2_mrr_at_5": state.stage2.mrr_at_5 or 0.0,
                }
            )
    if state.synthesized_answer is not None:
        mlflow.log_text(state.synthesized_answer, "synthesis.txt")
    if state.answer_score and state.answer_score.status == "scored":
        mlflow.log_metrics(
            {
                "answer_normalized_em": float(state.answer_score.normalized_em or 0.0),
                "answer_token_f1": float(state.answer_score.token_f1 or 0.0),
            }
        )
    if state.error:
        mlflow.set_tag("error", state.error)
    for i, rec in enumerate(state.tool_records):
        mlflow.log_dict(rec, f"tool_{i}.json")
