"""MCP tool nodes for filings and calculator."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.state import AgentState, PassageChunk
from finagent_mesh.gateway.mcp_gateway import McpGatewayClient


def fetch_and_extract_chunks(
    state: AgentState, gateway: McpGatewayClient, doc_type: str
) -> dict[str, Any]:
    """Optionally enrich example chunks via mcp-sec-edgar when empty."""
    if state.example.chunks:
        return {"example": state.example, "tool_records": state.tool_records}
    firm_id = state.example.firm_id
    fetch_rec = gateway.call_tool(
        "mcp-sec-edgar", "fetch_filing", {"firm_id": firm_id, "doc_type": doc_type}
    )
    filing_id = fetch_rec["result"].get("filing_id", f"{firm_id}:{doc_type}")
    extract_rec = gateway.call_tool(
        "mcp-sec-edgar", "extract_chunks", {"filing_id": filing_id, "doc_type": doc_type}
    )
    chunks = [
        PassageChunk(
            chunk_id=c["chunk_id"],
            doc_type=doc_type,
            text=c["text"],
            is_table=bool(c.get("is_table", False)),
        )
        for c in extract_rec["result"].get("chunks", [])
    ]
    example = state.example.model_copy(update={"chunks": chunks})
    records = list(state.tool_records) + [fetch_rec, extract_rec]
    return {"example": example, "tool_records": records}


def calculator_call(
    gateway: McpGatewayClient, tool: str, arguments: dict[str, Any]
) -> dict[str, Any]:
    """Deterministic finance math — sole numeric source."""
    return gateway.call_tool("mcp-financial-calculator", tool, arguments)
