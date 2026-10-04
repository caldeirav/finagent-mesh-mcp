"""Cloud synthesis over top-K Stage-2 chunks."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState
from finagent_mesh.clients.gemini import GeminiClient


def run_synthesize(state: AgentState, client: GeminiClient) -> dict[str, Any]:
    if state.error == "empty_top1_chunks":
        return {"synthesized_answer": None, "error": state.error}
    chunks = state.stage2_chunks[: state.synthesis_k]
    if not chunks:
        return {"synthesized_answer": None, "error": "no_chunks_for_synthesis"}
    answer = client.synthesize(
        state.example.query_text,
        [(c.chunk_id, c.text) for c in chunks],
    )
    return {"synthesized_answer": answer, "error": None}
