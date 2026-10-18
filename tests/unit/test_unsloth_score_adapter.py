"""Fail-closed Unsloth Score adapter tests."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.engines.unsloth_score import UnslothScoreAdapter
from finagent_mesh.clients.open_decision import OpenDecisionError


def _cfg() -> EngineConfiguration:
    return EngineConfiguration(
        config_id="unsloth-decision-score",
        family="unsloth-decision",
        display_name="unsloth",
        primitives=["score"],
        primary_stages=["stage2"],
        base_url="http://localhost:8711",
        backend="unsloth_score",
        model_revision="test",
        is_heavy_gpu=True,
        is_light_edge=False,
    )


def test_missing_checkpoint_fail_closed(monkeypatch):
    monkeypatch.delenv("UNSLOTH_SCORE_CHECKPOINT", raising=False)
    ad = UnslothScoreAdapter(_cfg())
    ok, msg = ad.health()
    assert ok is False
    assert "UNSLOTH_SCORE_CHECKPOINT" in msg
    with pytest.raises(OpenDecisionError):
        ad.decide("score", "q", [{"id": "a", "text": "t"}])


def test_score_with_injected_scorer(tmp_path: Path, monkeypatch):
    ckpt = tmp_path / "ckpt"
    ckpt.mkdir()
    (ckpt / "adapter_config.json").write_text("{}", encoding="utf-8")
    monkeypatch.setenv("UNSLOTH_SCORE_CHECKPOINT", str(ckpt))
    ad = UnslothScoreAdapter(_cfg())
    ad._inject_scores = lambda q, cands, meta: [0.1, 0.9]
    out = ad.decide(
        "score",
        "q",
        [{"id": "a", "text": "low"}, {"id": "b", "text": "high"}],
    )
    assert out["ranking"][0]["id"] == "b"
    assert out["backend"] == "unsloth_score"
