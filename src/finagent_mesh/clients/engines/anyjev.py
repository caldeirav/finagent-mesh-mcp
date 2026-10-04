"""AnyJev L0/L1 Choice adapter."""

from __future__ import annotations

from typing import Any

from finagent_mesh.clients.engines.http_base import HttpSystemOneAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration


class AnyJevAdapter(HttpSystemOneAdapter):
    """L0: adaptive cyclic shifts; L1: temperature scaling with 200-ex calibration.

    Calibration cardinality is enforced at serve start (`serve_engine.sh`), not adapter import.
    """

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
            raise ValueError(f"AnyJev supports choice only; got {primitive}")
        meta = dict(metadata or {})
        meta["anyjev_mode"] = "l1" if self.engine_id == "anyjev-l1" else "l0"
        return super().decide(primitive, query, candidates, meta)
