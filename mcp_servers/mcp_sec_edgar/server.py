"""SEC EDGAR MCP tool handlers (fixture-friendly local implementation)."""

from __future__ import annotations

from typing import Any

from finagent_mesh.agent.types import DOC_TYPES


def list_document_types(firm_id: str, as_of: str | None = None) -> dict[str, Any]:
    return {
        "document_types": list(DOC_TYPES),
        "availability": {dt: True for dt in DOC_TYPES},
        "firm_id": firm_id,
        "as_of": as_of,
    }


def fetch_filing(firm_id: str, doc_type: str, accession: str | None = None) -> dict[str, Any]:
    filing_id = accession or f"{firm_id}:{doc_type}:latest"
    return {
        "firm_id": firm_id,
        "doc_type": doc_type,
        "filing_id": filing_id,
        "content_ref": f"memory://{filing_id}",
        "metadata": {"source": "mcp-sec-edgar-local"},
    }


def extract_chunks(filing_id: str, doc_type: str | None = None) -> dict[str, Any]:
    dt = doc_type or (filing_id.split(":")[1] if ":" in filing_id else "10-K")
    # Deterministic synthetic passages + one table unit for harness smoke tests.
    chunks = [
        {
            "chunk_id": f"{filing_id}:p1",
            "text": f"{dt} overview paragraph for {filing_id}: revenue grew year over year.",
            "is_table": False,
        },
        {
            "chunk_id": f"{filing_id}:p2",
            "text": f"{dt} risk factors paragraph for {filing_id}: market and credit risk discussed.",
            "is_table": False,
        },
        {
            "chunk_id": f"{filing_id}:t1",
            "text": "| Metric | FY | Value |\n| Revenue | 2024 | 1000 |\n| Net Income | 2024 | 120 |",
            "is_table": True,
        },
    ]
    return {"filing_id": filing_id, "chunks": chunks}


def handle_tool(tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool == "list_document_types":
        return list_document_types(str(arguments["firm_id"]), arguments.get("as_of"))
    if tool == "fetch_filing":
        return fetch_filing(
            str(arguments["firm_id"]),
            str(arguments["doc_type"]),
            arguments.get("accession"),
        )
    if tool == "extract_chunks":
        return extract_chunks(str(arguments["filing_id"]), arguments.get("doc_type"))
    raise ValueError(f"Unknown tool {tool}")
