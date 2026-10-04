"""AgentGateway-mediated MCP client (no direct tool bypass)."""

from __future__ import annotations

import time
from typing import Any

import httpx


class McpGatewayError(RuntimeError):
    pass


class McpGatewayClient:
    """Routes tool calls exclusively through AGENT_GATEWAY_URL."""

    def __init__(self, gateway_url: str | None, *, mock: bool = False) -> None:
        self.gateway_url = gateway_url.rstrip("/") if gateway_url else None
        self.mock = mock or not gateway_url

    def call_tool(
        self, server: str, tool: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        started = time.perf_counter()
        if self.mock:
            result = self._mock_call(server, tool, arguments)
            latency_ms = int((time.perf_counter() - started) * 1000)
            return {
                "tool_name": f"{server}.{tool}",
                "request_json": arguments,
                "response_summary": result,
                "status": "ok",
                "latency_ms": latency_ms,
                "result": result,
            }
        if not self.gateway_url:
            raise McpGatewayError("AGENT_GATEWAY_URL is required for non-mock tool calls")
        url = f"{self.gateway_url}/mcp/{server}/tools/{tool}"
        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, json={"arguments": arguments})
                resp.raise_for_status()
                data = resp.json()
        except httpx.HTTPError as exc:
            raise McpGatewayError(f"Gateway tool call failed: {exc}") from exc
        latency_ms = int((time.perf_counter() - started) * 1000)
        return {
            "tool_name": f"{server}.{tool}",
            "request_json": arguments,
            "response_summary": {"keys": list(data.keys()) if isinstance(data, dict) else type(data).__name__},
            "status": "ok",
            "latency_ms": latency_ms,
            "result": data,
        }

    def _mock_call(
        self, server: str, tool: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        import sys
        from pathlib import Path

        root = Path(__file__).resolve().parents[3]
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
        if server == "mcp-sec-edgar":
            from mcp_servers.mcp_sec_edgar.server import handle_tool

            return handle_tool(tool, arguments)
        if server == "mcp-financial-calculator":
            from mcp_servers.mcp_financial_calculator.server import handle_tool

            return handle_tool(tool, arguments)
        raise McpGatewayError(f"Unknown MCP server {server}")
