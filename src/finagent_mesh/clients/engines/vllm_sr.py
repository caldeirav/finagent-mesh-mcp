"""vLLM-sr Decision-2.0 Kai / Lux Choice adapter."""

from __future__ import annotations

from typing import Any

from finagent_mesh.clients.engines.http_base import HttpSystemOneAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration


class VllmSrAdapter(HttpSystemOneAdapter):
    def __init__(self, cfg: EngineConfiguration) -> None:
        super().__init__(cfg)

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive != "choice":
            raise ValueError(f"vLLM-sr Decision-2.0 supports choice only; got {primitive}")
        meta = dict(metadata or {})
        meta["decision20_variant"] = "lux" if "lux" in self.engine_id else "kai"
        return super().decide(primitive, query, candidates, meta)
