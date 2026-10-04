"""LangGraph orchestration: Stage1 → Stage2 → metrics → optional synthesize → answer_score."""

from __future__ import annotations

from typing import Any, TypedDict

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


def build_graph(
    decision_client: OpenDecisionClient,
    gemini_client: GeminiClient,
):
    def _to_agent(state: GraphState) -> AgentState:
        return AgentState.model_validate(state)

    def n_stage1(state: GraphState) -> dict[str, Any]:
        return stage1.run_stage1(_to_agent(state), decision_client)

    def n_stage2(state: GraphState) -> dict[str, Any]:
        return stage2.run_stage2(_to_agent(state), decision_client)

    def n_metrics(state: GraphState) -> dict[str, Any]:
        return metrics_node.run_metrics(_to_agent(state))

    def n_synthesize(state: GraphState) -> dict[str, Any]:
        return synthesize.run_synthesize(_to_agent(state), gemini_client)

    def n_answer(state: GraphState) -> dict[str, Any]:
        return answer_score_node.run_answer_score(_to_agent(state))

    def route_after_metrics(state: GraphState) -> str:
        if state.get("skip_synthesis"):
            return "end"
        if state.get("error") in {"empty_top1_chunks", "missing_top1_doc_type", "no_chunks_for_synthesis"}:
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
    result = compiled.invoke(
        {
            "example": example,
            "skip_synthesis": skip_synthesis,
            "synthesis_k": synthesis_k,
            "tool_records": [],
        }
    )
    return AgentState.model_validate(result)
