"""Autoregressive Qwen3 JSON choice / one-shot chunk ranking baseline adapter."""

from __future__ import annotations

import json
from typing import Any

from finagent_mesh.clients.engines.http_base import HttpSystemOneAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.metrics.ranking import stable_rank


class ArBaselineAdapter(HttpSystemOneAdapter):
    def __init__(self, cfg: EngineConfiguration) -> None:
        super().__init__(cfg)

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        # choice/json_choice for Stage-1 types; score for one-shot chunk ranking
        if primitive not in {"choice", "json_choice", "score"}:
            raise ValueError(f"AR baseline supports json_choice/choice/score; got {primitive}")
        meta = dict(metadata or {})
        meta["json_choice"] = True
        meta["candidate_ids"] = [c["id"] for c in candidates]
        if primitive == "score" or meta.get("one_shot_chunks"):
            meta["one_shot_chunks"] = True
            meta["rank_all_chunks"] = True
        try:
            data = super().decide("choice", query, candidates, meta)
        except OpenDecisionError:
            self.parse_failures += 1
            raise
        raw = data.get("raw_json") or data.get("generation")
        if raw is not None:
            try:
                parsed = json.loads(raw) if isinstance(raw, str) else raw
                ordered = list(parsed.get("ordered_ids") or [])
                scores = list(parsed.get("scores") or [])
                if not ordered:
                    raise ValueError("empty ordered_ids")
                # Do not invent missing ranks — only return what the model emitted
                cand_set = {c["id"] for c in candidates}
                ordered = [i for i in ordered if i in cand_set]
                if not ordered:
                    raise ValueError("no valid ordered_ids in candidate set")
                if len(scores) != len(ordered):
                    scores = [float(len(ordered) - i) for i in range(len(ordered))]
                ranked = stable_rank(ordered, [float(s) for s in scores])
                total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
                data["ranking"] = [{"id": i, "score": s, "rank": r} for i, s, r in ranked]
                data["distribution"] = {i: max(s, 0.0) / total for i, s, _ in ranked}
                data["coverage"] = len(ordered) / max(len(candidates), 1)
            except Exception as exc:  # noqa: BLE001
                self.parse_failures += 1
                raise OpenDecisionError(
                    f"AR JSON parse failure for {self.engine_id}: {exc}"
                ) from exc
        if data.get("parse_failure"):
            self.parse_failures += 1
            raise OpenDecisionError(f"AR parse_failure flagged by engine {self.engine_id}")
        data["engine"] = self.engine_id
        data["model_revision"] = self.model_revision
        return data

    @property
    def parse_failure_rate(self) -> float | None:
        if self.decide_attempts == 0:
            return None
        return self.parse_failures / self.decide_attempts
