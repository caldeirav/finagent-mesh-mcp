"""OpenDecisionClient for local System-1 `/v1/systemone` APIs."""

from __future__ import annotations

from typing import Any, Literal

import httpx

from finagent_mesh.agent.types import DOC_TYPES
from finagent_mesh.metrics.ranking import stable_rank

Primitive = Literal["choice", "score", "action_cache"]


class OpenDecisionError(RuntimeError):
    pass


class OpenDecisionClient:
    def __init__(
        self,
        stage1_url: str,
        stage2_url: str,
        *,
        mock: bool = False,
        timeout: float = 60.0,
    ) -> None:
        self.stage1_url = stage1_url.rstrip("/")
        self.stage2_url = stage2_url.rstrip("/")
        self.mock = mock
        self.timeout = timeout

    def _base_for(self, primitive: Primitive) -> str:
        if primitive == "choice":
            return self.stage1_url
        return self.stage2_url

    def decide(
        self,
        primitive: Primitive,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if self.mock:
            return self._mock_decide(primitive, query, candidates)
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
        return data

    def _mock_decide(
        self,
        primitive: Primitive,
        query: str,
        candidates: list[dict[str, str]],
    ) -> dict[str, Any]:
        # Deterministic lexical overlap mock for local/dev without engines.
        q_tokens = set(query.lower().split())
        scored: list[tuple[str, float]] = []
        for c in candidates:
            text = (c.get("text") or "").lower()
            cid = c["id"]
            overlap = len(q_tokens.intersection(text.split())) if q_tokens else 0
            # Prefer known doc-type order bias for choice when ties.
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
