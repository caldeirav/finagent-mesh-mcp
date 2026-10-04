"""MLflow tracing helpers."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

from finagent_mesh.agent.state import AgentState


def setup_mlflow(tracking_uri: str) -> None:
    import os

    import mlflow

    os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")
    mlflow.set_tracking_uri(tracking_uri)


@contextmanager
def example_run(run_id: str, example_id: str) -> Iterator[Any]:
    import mlflow

    with mlflow.start_run(run_name=f"{run_id}:{example_id}", nested=True) as active:
        mlflow.set_tags({"run_id": run_id, "example_id": example_id})
        yield active


def log_binding(
    *,
    stage1_engine: str | None,
    stage2_engine: str | None,
    gemini_model: str | None,
) -> None:
    import mlflow

    tags = {}
    if stage1_engine:
        tags["stage1_engine"] = stage1_engine
    if stage2_engine:
        tags["stage2_engine"] = stage2_engine
    if gemini_model:
        tags["gemini_model"] = gemini_model
    if tags:
        mlflow.set_tags(tags)


def log_agent_state(
    state: AgentState,
    *,
    decision_meta: dict[str, Any] | None = None,
) -> None:
    import mlflow

    if decision_meta:
        if decision_meta.get("engine"):
            mlflow.set_tag("decision_engine", str(decision_meta["engine"]))
        if decision_meta.get("model_revision"):
            mlflow.set_tag("model_revision", str(decision_meta["model_revision"]))
        if decision_meta.get("latency_ms") is not None:
            mlflow.log_metric("decision_latency_ms", float(decision_meta["latency_ms"]))

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
