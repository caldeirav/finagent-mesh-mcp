"""Shared HTTP adapter for System-1 /healthz + /v1/systemone."""

from __future__ import annotations

import os
import time
from typing import Any

import httpx

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError


def _http_timeout() -> float:
    return float(os.getenv("SYSTEMONE_HTTP_TIMEOUT", "900"))


class HttpSystemOneAdapter:
    def __init__(self, cfg: EngineConfiguration, *, timeout: float | None = None) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.timeout = timeout if timeout is not None else _http_timeout()
        self.last_latency_ms: float | None = None
        self.parse_failures = 0
        self.decide_attempts = 0

    def health(self) -> tuple[bool, str]:
        url = self.cfg.health_url()
        try:
            with httpx.Client(timeout=5.0) as client:
                resp = client.get(url)
                if resp.status_code != 200:
                    return False, f"{url} status={resp.status_code}"
                data = resp.json()
                if data.get("status") != "ok":
                    return False, f"{url} body={data}"
                return True, "ok"
        except Exception as exc:  # noqa: BLE001
            return False, f"{url} error={exc}"

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.decide_attempts += 1
        meta = dict(metadata or {})
        meta.setdefault("engine_config_id", self.engine_id)
        payload = {
            "primitive": primitive,
            "query": query,
            "candidates": candidates,
            "metadata": meta,
        }
        url = self.cfg.decide_url()
        started = time.perf_counter()
        try:
            with httpx.Client(timeout=self.timeout) as client:
                resp = client.post(url, json=payload)
                if resp.status_code >= 400:
                    detail = (resp.text or "")[:800]
                    raise OpenDecisionError(
                        f"{self.engine_id} HTTP {resp.status_code} {url}: {detail}"
                    )
                data = resp.json()
        except OpenDecisionError:
            raise
        except httpx.HTTPError as exc:
            raise OpenDecisionError(f"{self.engine_id} System-1 call failed: {exc}") from exc
        finally:
            self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        if "ranking" not in data or "distribution" not in data:
            raise OpenDecisionError(f"{self.engine_id} response missing ranking/distribution")
        data.setdefault("engine", self.engine_id)
        data.setdefault("model_revision", self.model_revision)
        data["latency_ms"] = self.last_latency_ms
        return data
