"""LangGraph orchestration: Stage1 → Stage2 → metrics → optional synthesize → answer_score."""

from __future__ import annotations

from typing import Any, TypedDict

import mlflow
from langgraph.graph import END, StateGraph

from finagent_mesh.agent.nodes import answer_score as answer_score_node
from finagent_mesh.agent.nodes import metrics_node, stage1, stage2, synthesize
from finagent_mesh.agent.state import AgentState, BenchmarkExample
from finagent_mesh.clients.gemini import GeminiClient
from finagent_mesh.clients.open_decision import OpenDecisionClient


class GraphState(TypedDict, total=False):
    example: BenchmarkExample
    skip_synthesis: bool
    synthesis_k: int
    top1_doc_type: str | None
    stage1: Any
    stage2: Any
    stage2_chunks: list
    synthesized_answer: str | None
    answer_score: Any
    error: str | None
    tool_records: list


def _annotate_span(description: str, **attrs: Any) -> None:
    span = mlflow.get_current_active_span()
    if span is None:
        return
    span.set_attribute("description", description)
    if attrs:
        span.set_attributes({k: v for k, v in attrs.items() if v is not None})


def build_graph(
    decision_client: OpenDecisionClient,
    gemini_client: GeminiClient,
):
    def _to_agent(state: GraphState) -> AgentState:
        return AgentState.model_validate(state)

    def n_stage1(state: GraphState) -> dict[str, Any]:
        """Stage-1 Choice: rank SEC filing types for the query."""
        _annotate_span(
            n_stage1.__doc__ or "stage1",
            stage="stage1",
            primitive="choice",
        )
        return stage1.run_stage1(_to_agent(state), decision_client)

    def n_stage2(state: GraphState) -> dict[str, Any]:
        """Stage-2 Score: rank passage chunks inside the Top-1 filing type."""
        _annotate_span(
            n_stage2.__doc__ or "stage2",
            stage="stage2",
            primitive="score",
            top1_doc_type=state.get("top1_doc_type"),
        )
        return stage2.run_stage2(_to_agent(state), decision_client)

    def n_metrics(state: GraphState) -> dict[str, Any]:
        """Compute Stage-1/2 nDCG@5, MAP@5, MRR@5 against FinAgentBench labels."""
        _annotate_span(n_metrics.__doc__ or "metrics", stage="metrics")
        return metrics_node.run_metrics(_to_agent(state))

    def n_synthesize(state: GraphState) -> dict[str, Any]:
        """Gemini Flash System-2: answer from top-K retrieved chunks (fail-closed)."""
        _annotate_span(
            n_synthesize.__doc__ or "synthesize",
            stage="synthesize",
            gemini_model=getattr(gemini_client, "model", None),
        )
        return synthesize.run_synthesize(_to_agent(state), gemini_client)

    def n_answer(state: GraphState) -> dict[str, Any]:
        """Score Gemini answer vs label (normalized EM + token F1)."""
        _annotate_span(n_answer.__doc__ or "answer_score", stage="answer_score")
        return answer_score_node.run_answer_score(_to_agent(state))

    def route_after_metrics(state: GraphState) -> str:
        if state.get("skip_synthesis"):
            return "end"
        if state.get("error") in {
            "empty_top1_chunks",
            "missing_top1_doc_type",
            "no_chunks_for_synthesis",
        }:
            return "end"
        return "synthesize"

    g: StateGraph = StateGraph(GraphState)
    g.add_node("stage1", n_stage1)
    g.add_node("stage2", n_stage2)
    g.add_node("metrics", n_metrics)
    g.add_node("synthesize", n_synthesize)
    g.add_node("answer_score", n_answer)
    g.set_entry_point("stage1")
    g.add_edge("stage1", "stage2")
    g.add_edge("stage2", "metrics")
    g.add_conditional_edges(
        "metrics",
        route_after_metrics,
        {"synthesize": "synthesize", "end": END},
    )
    g.add_edge("synthesize", "answer_score")
    g.add_edge("answer_score", END)
    return g.compile()


def run_example(
    compiled,
    example: BenchmarkExample,
    *,
    skip_synthesis: bool,
    synthesis_k: int,
) -> AgentState:
    """Invoke the LangGraph pipeline for one FinAgentBench example.

    Call under ``tracing.example_trace`` so LangGraph autolog spans nest under
    the agent root span (MLflow Traces tab).
    """
    span = mlflow.get_current_active_span()
    if span is not None:
        span.set_inputs(
            {
                "example_id": example.example_id,
                "firm_id": example.firm_id,
                "query_text": example.query_text,
                "skip_synthesis": skip_synthesis,
                "synthesis_k": synthesis_k,
                "n_chunks": len(example.chunks),
            }
        )
    result = compiled.invoke(
        {
            "example": example,
            "skip_synthesis": skip_synthesis,
            "synthesis_k": synthesis_k,
            "tool_records": [],
        }
    )
    state = AgentState.model_validate(result)
    if span is not None:
        span.set_outputs(
            {
                "top1_doc_type": state.top1_doc_type,
                "stage1_ndcg_at_5": state.stage1.ndcg_at_5 if state.stage1 else None,
                "stage2_ndcg_at_5": state.stage2.ndcg_at_5 if state.stage2 else None,
                "has_synthesis": bool(state.synthesized_answer),
                "error": state.error,
            }
        )
    return state
