"""MLflow experiment runs + GenAI / LangGraph span traces.

Keeps classic nested ``mlflow.start_run`` logging and adds MLflow Tracing
(Traces tab): LangGraph autolog + a root agent span per example, with clear
Stage-1 / Stage-2 / Gemini outcome metrics on the active run.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

from finagent_mesh.agent.state import AgentState

_AUTOLOG_ENABLED = False
DEFAULT_EXPERIMENT = "finagent-mesh"


def setup_mlflow(tracking_uri: str, *, experiment: str | None = None) -> None:
    """Configure tracking URI, experiment, and LangGraph/Gemini autolog."""
    global _AUTOLOG_ENABLED
    import mlflow

    os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")
    os.environ.setdefault("MLFLOW_DISABLE_AGENT_HINT", "1")
    mlflow.set_tracking_uri(tracking_uri)
    exp = experiment or os.getenv("MLFLOW_EXPERIMENT_NAME", DEFAULT_EXPERIMENT)
    try:
        mlflow.set_experiment(exp)
    except Exception:  # noqa: BLE001
        pass

    if not _AUTOLOG_ENABLED and os.getenv("MLFLOW_DISABLE_AUTOLOG", "0") not in {
        "1",
        "true",
        "TRUE",
    }:
        try:
            # Inline tracer keeps manual start_span children nested under LangGraph nodes.
            mlflow.langchain.autolog(
                log_traces=True, silent=True, run_tracer_inline=True
            )
        except TypeError:
            try:
                mlflow.langchain.autolog(log_traces=True, silent=True)
            except Exception:  # noqa: BLE001
                pass
        except Exception:  # noqa: BLE001
            pass
        try:
            # Native Google GenAI SDK if present; LangChain Gemini is covered by langchain.autolog
            mlflow.gemini.autolog(log_traces=True, silent=True)
        except Exception:  # noqa: BLE001
            pass
        _AUTOLOG_ENABLED = True


def flush_traces() -> None:
    import mlflow

    try:
        mlflow.flush_trace_async_logging()
    except Exception:  # noqa: BLE001
        pass


@contextmanager
def example_run(run_id: str, example_id: str) -> Iterator[Any]:
    """Nested MLflow Run (Experiments → Runs) for one example."""
    import mlflow

    with mlflow.start_run(run_name=f"{run_id}:{example_id}", nested=True) as active:
        mlflow.set_tags({"run_id": run_id, "example_id": example_id})
        yield active


@contextmanager
def example_trace(
    *,
    run_id: str,
    example_id: str,
    stage1_engine: str | None = None,
    stage2_engine: str | None = None,
    gemini_model: str | None = None,
    skip_synthesis: bool = False,
) -> Iterator[Any]:
    """Root agentic span for one example (Experiments → Traces)."""
    import mlflow
    from mlflow.entities import SpanType

    attrs = {
        "run_id": run_id,
        "example_id": example_id,
        "skip_synthesis": skip_synthesis,
    }
    if stage1_engine:
        attrs["stage1_engine"] = stage1_engine
    if stage2_engine:
        attrs["stage2_engine"] = stage2_engine
    if gemini_model:
        attrs["gemini_model"] = gemini_model

    with mlflow.start_span(
        name="finagent_example",
        span_type=SpanType.AGENT,
        attributes=attrs,
    ) as span:
        span.set_inputs({"example_id": example_id, "run_id": run_id})
        try:
            mlflow.update_current_trace(
                tags={
                    "run_id": run_id,
                    "example_id": example_id,
                    "stage1_engine": stage1_engine or "",
                    "stage2_engine": stage2_engine or "",
                    "gemini_model": gemini_model or "",
                }
            )
        except Exception:  # noqa: BLE001
            pass
        yield span


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


def _attach_span_outcomes(outcomes: dict[str, Any]) -> None:
    import mlflow

    span = mlflow.get_current_active_span()
    if span is None:
        return
    # Spans prefer JSON-safe scalars/strings
    attrs: dict[str, Any] = {}
    for k, v in outcomes.items():
        if v is None:
            continue
        if isinstance(v, (bool, int, float, str)):
            attrs[k] = v
        else:
            attrs[k] = str(v)
    if attrs:
        span.set_attributes(attrs)


def outcome_metrics(state: AgentState) -> dict[str, Any]:
    """Compute clear Stage-1 / Stage-2 / Gemini outcome metrics for one example."""
    from finagent_mesh.matrix.metrics import top1_correct

    out: dict[str, Any] = {}
    ex = state.example

    # --- Stage 1 (Choice / routing) ---
    if state.stage1 and state.stage1.ordered_ids:
        out["stage1_ran"] = 1.0
        if state.stage1.ndcg_at_5 is not None:
            out["stage1_ndcg_at_5"] = float(state.stage1.ndcg_at_5)
        if state.stage1.map_at_5 is not None:
            out["stage1_map_at_5"] = float(state.stage1.map_at_5)
        if state.stage1.mrr_at_5 is not None:
            out["stage1_mrr_at_5"] = float(state.stage1.mrr_at_5)
        correct = top1_correct(state.top1_doc_type, ex.stage1_labels)
        out["stage1_top1_correct"] = 1.0 if correct else 0.0
        out["stage1_top1"] = state.top1_doc_type or ""
    else:
        out["stage1_ran"] = 0.0
        out["stage1_top1_correct"] = 0.0

    # --- Stage 2 (Score / passage ranking) ---
    empty = state.error == "empty_top1_chunks"
    out["empty_top1_chunks"] = 1.0 if empty else 0.0
    if state.stage2 and state.stage2.ordered_ids and not state.stage2.skipped_reason:
        out["stage2_ran"] = 1.0
        if state.stage2.ndcg_at_5 is not None:
            out["stage2_ndcg_at_5"] = float(state.stage2.ndcg_at_5)
        if state.stage2.map_at_5 is not None:
            out["stage2_map_at_5"] = float(state.stage2.map_at_5)
        if state.stage2.mrr_at_5 is not None:
            out["stage2_mrr_at_5"] = float(state.stage2.mrr_at_5)
    else:
        out["stage2_ran"] = 0.0

    # --- Gemini Flash (System-2 synthesis) ---
    if state.skip_synthesis:
        out["gemini_status"] = "skipped_ranking_only"
        out["gemini_synthesis_ok"] = 0.0
    elif state.synthesized_answer is not None and str(state.synthesized_answer).strip():
        out["gemini_status"] = "ok"
        out["gemini_synthesis_ok"] = 1.0
    elif state.error in {
        "empty_top1_chunks",
        "missing_top1_doc_type",
        "no_chunks_for_synthesis",
    }:
        out["gemini_status"] = f"skipped_{state.error}"
        out["gemini_synthesis_ok"] = 0.0
    else:
        out["gemini_status"] = "missing"
        out["gemini_synthesis_ok"] = 0.0

    if state.answer_score and state.answer_score.status == "scored":
        if state.answer_score.normalized_em is not None:
            out["gemini_answer_normalized_em"] = float(state.answer_score.normalized_em)
            out["answer_normalized_em"] = float(state.answer_score.normalized_em)
        if state.answer_score.token_f1 is not None:
            out["gemini_answer_token_f1"] = float(state.answer_score.token_f1)
            out["answer_token_f1"] = float(state.answer_score.token_f1)

    if state.error:
        out["example_error"] = state.error
    return out


def log_outcome_metrics(state: AgentState) -> dict[str, Any]:
    """Log Stage-1 / Stage-2 / Gemini outcomes to the active MLflow Run + current span."""
    import mlflow

    outcomes = outcome_metrics(state)
    metrics = {
        k: float(v)
        for k, v in outcomes.items()
        if isinstance(v, (int, float)) and not isinstance(v, bool)
    }
    # bools already converted to 0/1 floats above
    if metrics:
        mlflow.log_metrics(metrics)
    status = outcomes.get("gemini_status")
    if status:
        mlflow.set_tag("gemini_status", str(status))
    if outcomes.get("stage1_top1"):
        mlflow.set_tag("stage1_top1", str(outcomes["stage1_top1"]))
    if outcomes.get("example_error"):
        mlflow.set_tag("error", str(outcomes["example_error"]))
    _attach_span_outcomes(outcomes)
    return outcomes


def log_agent_state(
    state: AgentState,
    *,
    decision_meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Legacy + enriched logging: distributions, tools, and outcome metrics."""
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
    if state.stage2:
        mlflow.log_dict(state.stage2.decision_distribution, "stage2_distribution.json")
    if state.synthesized_answer is not None:
        mlflow.log_text(state.synthesized_answer, "synthesis.txt")
    for i, rec in enumerate(state.tool_records):
        mlflow.log_dict(rec, f"tool_{i}.json")

    outcomes = log_outcome_metrics(state)

    span = mlflow.get_current_active_span()
    if span is not None:
        span.set_outputs(
            {
                "top1_doc_type": state.top1_doc_type,
                "stage1_ndcg_at_5": state.stage1.ndcg_at_5 if state.stage1 else None,
                "stage2_ndcg_at_5": state.stage2.ndcg_at_5 if state.stage2 else None,
                "gemini_synthesis_ok": bool(
                    state.synthesized_answer and str(state.synthesized_answer).strip()
                ),
                "error": state.error,
            }
        )
    return outcomes
