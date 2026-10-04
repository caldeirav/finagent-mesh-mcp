"""OpenDecisionClient for local System-1 `/v1/systemone` APIs."""

from __future__ import annotations

from typing import Any, Literal, Protocol

import httpx

from finagent_mesh.agent.types import DOC_TYPES
from finagent_mesh.metrics.ranking import stable_rank

Primitive = Literal["choice", "score", "action_cache"]


class OpenDecisionError(RuntimeError):
    pass


class StageClient(Protocol):
    engine_id: str
    model_revision: str

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]: ...


class OpenDecisionClient:
    """Routes Choice → stage1 URL/client and Score/ActionCache → stage2 URL/client."""

    def __init__(
        self,
        stage1_url: str,
        stage2_url: str,
        *,
        mock: bool = False,
        timeout: float = 60.0,
        stage1_client: StageClient | None = None,
        stage2_client: StageClient | None = None,
        stage1_engine_id: str | None = None,
        stage2_engine_id: str | None = None,
    ) -> None:
        self.stage1_url = stage1_url.rstrip("/")
        self.stage2_url = stage2_url.rstrip("/")
        self.mock = mock
        self.timeout = timeout
        self.stage1_client = stage1_client
        self.stage2_client = stage2_client
        self.stage1_engine_id = stage1_engine_id or getattr(stage1_client, "engine_id", "stage1")
        self.stage2_engine_id = stage2_engine_id or getattr(stage2_client, "engine_id", "stage2")
        self.last_response_meta: dict[str, Any] = {}

    def _base_for(self, primitive: Primitive) -> str:
        if primitive == "choice":
            return self.stage1_url
        return self.stage2_url

    def _client_for(self, primitive: Primitive) -> StageClient | None:
        if primitive == "choice":
            return self.stage1_client
        return self.stage2_client

    def decide(
        self,
        primitive: Primitive,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if self.mock:
            data = self._mock_decide(primitive, query, candidates)
            self.last_response_meta = {
                "engine": data.get("engine"),
                "model_revision": data.get("model_revision"),
                "latency_ms": data.get("latency_ms"),
            }
            return data

        bound = self._client_for(primitive)
        if bound is not None:
            data = bound.decide(primitive, query, candidates, metadata)
            self.last_response_meta = {
                "engine": data.get("engine", getattr(bound, "engine_id", None)),
                "model_revision": data.get(
                    "model_revision", getattr(bound, "model_revision", None)
                ),
                "latency_ms": data.get("latency_ms"),
            }
            return data

        payload = {
            "primitive": primitive,
            "query": query,
            "candidates": candidates,
            "metadata": metadata or {},
        }
        url = f"{self._base_for(primitive)}/v1/systemone"
        try:
            with httpx.Client(timeout=self.timeout) as client:
                resp = client.post(url, json=payload)
                resp.raise_for_status()
                data = resp.json()
        except httpx.HTTPError as exc:
            raise OpenDecisionError(f"System-1 call failed: {exc}") from exc
        if "ranking" not in data or "distribution" not in data:
            raise OpenDecisionError("System-1 response missing ranking/distribution")
        self.last_response_meta = {
            "engine": data.get("engine"),
            "model_revision": data.get("model_revision"),
            "latency_ms": data.get("latency_ms"),
        }
        return data

    def _mock_decide(
        self,
        primitive: Primitive,
        query: str,
        candidates: list[dict[str, str]],
    ) -> dict[str, Any]:
        q_tokens = set(query.lower().split())
        scored: list[tuple[str, float]] = []
        for c in candidates:
            text = (c.get("text") or "").lower()
            cid = c["id"]
            overlap = len(q_tokens.intersection(text.split())) if q_tokens else 0
            bias = 0.0
            if primitive == "choice" and cid in DOC_TYPES:
                bias = (len(DOC_TYPES) - DOC_TYPES.index(cid)) * 0.01
            scored.append((cid, float(overlap) + bias + 0.001 * len(text)))
        ids = [s[0] for s in scored]
        scores = [s[1] for s in scored]
        ranked = stable_rank(ids, scores)
        ranking = [{"id": i, "score": s, "rank": r} for i, s, r in ranked]
        total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
        distribution = {i: max(s, 0.0) / total for i, s, _ in ranked}
        return {
            "primitive": primitive,
            "ranking": ranking,
            "distribution": distribution,
            "engine": "mock",
            "model_revision": "mock-1",
        }


def bind_from_registry(
    stage1_config_id: str,
    stage2_config_id: str,
    *,
    mock: bool = False,
    registry_path: str | None = None,
) -> OpenDecisionClient:
    from pathlib import Path

    from finagent_mesh.clients.engines.registry import create_adapter, load_registry

    reg = load_registry(Path(registry_path) if registry_path else None)
    s1 = create_adapter(stage1_config_id, reg)
    s2 = create_adapter(stage2_config_id, reg)
    return OpenDecisionClient(
        reg.get(stage1_config_id).base_url,
        reg.get(stage2_config_id).base_url,
        mock=mock,
        stage1_client=s1,
        stage2_client=s2,
        stage1_engine_id=stage1_config_id,
        stage2_engine_id=stage2_config_id,
    )
