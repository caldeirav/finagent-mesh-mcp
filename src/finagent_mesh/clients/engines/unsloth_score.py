"""Unsloth FastDecisionModel Score adapter (fail-closed without checkpoint)."""

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError
from finagent_mesh.metrics.ranking import stable_rank
from finagent_mesh.unsloth.types import SCORE_CRITERIA


class UnslothScoreAdapter:
    def __init__(self, cfg: EngineConfiguration) -> None:
        self.cfg = cfg
        self.engine_id = cfg.config_id
        self.model_revision = cfg.model_revision
        self.checkpoint = (
            os.getenv("UNSLOTH_SCORE_CHECKPOINT")
            or (cfg.weights_ref or "").strip()
            or ""
        )
        self.base_model = os.getenv(
            "UNSLOTH_BASE_MODEL", "unsloth/Qwen3.8-27B-unsloth-bnb-4bit"
        )
        self.last_latency_ms: float | None = None
        self.parse_failures = 0
        self.decide_attempts = 0
        self._model = None
        self._tokenizer = None

    def _ensure_checkpoint(self) -> Path:
        if not self.checkpoint:
            raise OpenDecisionError(
                f"{self.engine_id}: UNSLOTH_SCORE_CHECKPOINT missing "
                "(fail-closed; no Lux/E5/BM25 fallback)"
            )
        path = Path(self.checkpoint)
        if not path.exists():
            raise OpenDecisionError(
                f"{self.engine_id}: checkpoint path does not exist: {path}"
            )
        return path

    def health(self) -> tuple[bool, str]:
        try:
            self._ensure_checkpoint()
        except OpenDecisionError as exc:
            return False, str(exc)
        return True, "ok"

    def _load(self):
        if self._model is not None:
            return
        self._ensure_checkpoint()
        try:
            from unsloth import FastDecisionModel  # type: ignore
        except ImportError as exc:
            raise OpenDecisionError(
                f"{self.engine_id}: Unsloth not installed (uv sync --extra unsloth)"
            ) from exc
        model, tokenizer = FastDecisionModel.from_pretrained(
            model_name=self.checkpoint or self.base_model,
            max_seq_length=2048,
            load_in_4bit=True,
        )
        FastDecisionModel.for_inference(model)
        self._model = model
        self._tokenizer = tokenizer

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if primitive not in {"score", "action_cache"}:
            raise ValueError(f"unsloth-score supports score; got {primitive}")
        self.decide_attempts += 1
        self._ensure_checkpoint()
        if not candidates:
            raise OpenDecisionError(f"{self.engine_id}: empty candidate list")

        # Allow unit tests to inject a scorer without loading Unsloth
        inject = getattr(self, "_inject_scores", None)
        started = time.perf_counter()
        if inject is not None:
            scores = inject(query, candidates, metadata)
        else:
            self._load()
            texts = [c.get("text") or "" for c in candidates]
            ids = [c["id"] for c in candidates]
            try:
                pred = self._model.predict(  # type: ignore[union-attr]
                    type="score",
                    query=query,
                    candidates=texts,
                    criteria=list(SCORE_CRITERIA),
                )
                # pred may be list of floats or graded labels
                if isinstance(pred, dict) and "scores" in pred:
                    scores = [float(x) for x in pred["scores"]]
                elif isinstance(pred, list):
                    scores = [float(x) for x in pred]
                else:
                    scores = [0.0] * len(ids)
            except Exception as exc:
                raise OpenDecisionError(
                    f"{self.engine_id}: predict failed: {exc}"
                ) from exc
            if len(scores) != len(ids):
                # Pad / truncate defensively
                scores = (scores + [0.0] * len(ids))[: len(ids)]

        ids = [c["id"] for c in candidates]
        ranked = stable_rank(ids, scores)
        ranking = [
            {"id": cid, "score": float(s), "rank": i + 1}
            for i, (cid, s, _) in enumerate(ranked)
        ]
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        return {
            "primitive": "score",
            "ranking": ranking,
            "engine": self.engine_id,
            "model_revision": self.model_revision,
            "latency_ms": self.last_latency_ms,
            "backend": "unsloth_score",
            "checkpoint": self.checkpoint,
            "n_candidates": len(candidates),
        }
