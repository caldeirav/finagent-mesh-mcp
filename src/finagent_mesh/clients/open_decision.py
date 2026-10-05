"""OpenDecisionClient for local System-1 `/v1/systemone` APIs."""

from __future__ import annotations

import os
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
        timeout: float | None = None,
        stage1_client: StageClient | None = None,
        stage2_client: StageClient | None = None,
        stage1_engine_id: str | None = None,
        stage2_engine_id: str | None = None,
    ) -> None:
        self.stage1_url = stage1_url.rstrip("/")
        self.stage2_url = stage2_url.rstrip("/")
        self.mock = mock
        self.timeout = timeout if timeout is not None else float(
            os.getenv("SYSTEMONE_HTTP_TIMEOUT", "900")
        )
        self.stage1_client = stage1_client
        self.stage2_client = stage2_client
        self.stage1_engine_id = stage1_engine_id or getattr(stage1_client, "engine_id", "stage1")
        self.stage2_engine_id = stage2_engine_id or getattr(stage2_client, "engine_id", "stage2")
        self.last_response_meta: dict[str, Any] = {}
        self.io_traces: list[dict[str, Any]] = []

    def reset_traces(self) -> None:
        self.io_traces = []
        self.last_response_meta = {}

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
        slim_cands = [
            {"id": c["id"], "text": (c.get("text") or "")[:400]} for c in candidates
        ]
        rec: dict[str, Any] = {
            "primitive": primitive,
            "query": query,
            "n_candidates": len(candidates),
            "candidates": slim_cands,
            "metadata": dict(metadata or {}),
        }
        try:
            import mlflow
            from mlflow.entities import SpanType

            span_cm = mlflow.start_span(
                name=f"systemone_{primitive}",
                span_type=SpanType.RETRIEVER,
                attributes={
                    "primitive": primitive,
                    "engine": (
                        self.stage1_engine_id
                        if primitive == "choice"
                        else self.stage2_engine_id
                    ),
                    "n_candidates": len(candidates),
                },
            )
        except Exception:  # noqa: BLE001
            span_cm = None

        def _run() -> dict[str, Any]:
            return self._decide_inner(primitive, query, candidates, metadata, rec)

        if span_cm is None:
            return _run()
        with span_cm as span:
            span.set_inputs(
                {
                    "primitive": primitive,
                    "query": query,
                    "n_candidates": len(candidates),
                    "candidate_ids": [c["id"] for c in candidates[:50]],
                }
            )
            try:
                data = _run()
                span.set_outputs(
                    {
                        "engine": self.last_response_meta.get("engine"),
                        "latency_ms": self.last_response_meta.get("latency_ms"),
                        "top_ids": [
                            r.get("id") for r in (data.get("ranking") or [])[:5]
                        ],
                    }
                )
                return data
            except Exception as exc:
                span.set_attributes({"error": str(exc)[:500]})
                raise

    def _decide_inner(
        self,
        primitive: Primitive,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None,
        rec: dict[str, Any],
    ) -> dict[str, Any]:
        try:
            if self.mock:
                data = self._mock_decide(primitive, query, candidates)
                self.last_response_meta = {
                    "engine": data.get("engine"),
                    "model_revision": data.get("model_revision"),
                    "latency_ms": data.get("latency_ms"),
                }
            else:
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
                else:
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
            rec.update(
                {
                    "engine": self.last_response_meta.get("engine"),
                    "model_revision": self.last_response_meta.get("model_revision"),
                    "latency_ms": self.last_response_meta.get("latency_ms"),
                    "ranking": data.get("ranking"),
                    "distribution": data.get("distribution"),
                    "backend": data.get("backend"),
                    "model_id": data.get("model_id"),
                    "error": None,
                }
            )
            self.io_traces.append(rec)
            return data
        except Exception as exc:
            rec["error"] = str(exc)
            rec["engine"] = rec.get("engine") or (
                self.stage1_engine_id if primitive == "choice" else self.stage2_engine_id
            )
            self.io_traces.append(rec)
            raise

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
    port_overrides: dict[str, int] | None = None,
) -> OpenDecisionClient:
    from pathlib import Path

    from finagent_mesh.clients.engines.registry import create_adapter, load_registry
    from finagent_mesh.matrix.ports import base_url_for_port

    reg = load_registry(Path(registry_path) if registry_path else None)
    ports = port_overrides or {}
    s1_url = (
        base_url_for_port(ports[stage1_config_id])
        if stage1_config_id in ports
        else reg.get(stage1_config_id).base_url
    )
    s2_url = (
        base_url_for_port(ports[stage2_config_id])
        if stage2_config_id in ports
        else reg.get(stage2_config_id).base_url
    )
    s1 = create_adapter(stage1_config_id, reg, base_url=s1_url)
    s2 = create_adapter(stage2_config_id, reg, base_url=s2_url)
    return OpenDecisionClient(
        s1_url,
        s2_url,
        mock=mock,
        stage1_client=s1,
        stage2_client=s2,
        stage1_engine_id=stage1_config_id,
        stage2_engine_id=stage2_config_id,
    )
