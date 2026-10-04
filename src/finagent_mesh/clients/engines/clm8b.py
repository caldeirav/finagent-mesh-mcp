"""CLM-8B Action Cache / Score adapter."""

from __future__ import annotations

from typing import Any

from finagent_mesh.clients.engines.http_base import HttpSystemOneAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration


class Clm8bAdapter(HttpSystemOneAdapter):
    def __init__(self, cfg: EngineConfiguration) -> None:
        super().__init__(cfg)

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive not in {"score", "action_cache"}:
            raise ValueError(f"CLM-8B supports score/action_cache; got {primitive}")
        meta = dict(metadata or {})
        meta["action_cache"] = True
        return super().decide(primitive, query, candidates, meta)
