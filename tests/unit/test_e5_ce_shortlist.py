"""Unit tests for E5 → CrossEncoder shortlist adapter."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from finagent_mesh.clients.engines.e5_ce_shortlist import E5CeShortlistAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError


def _cfg() -> EngineConfiguration:
    return EngineConfiguration(
        config_id="e5-ce-shortlist-32",
        family="hybrid-ir",
        display_name="e5-ce",
        primitives=["score"],
        primary_stages=["stage2"],
        base_url="http://localhost:8703",
        backend="e5_ce_shortlist",
        model_revision="test",
        weights_ref="cross-encoder/ms-marco-MiniLM-L6-v2",
        is_heavy_gpu=False,
        is_light_edge=False,
    )


def _cands(n: int) -> list[dict[str, str]]:
    return [{"id": f"c{i}", "text": f"doc {i} about earnings"} for i in range(n)]


def test_ce_reranks_shortlist_and_appends_tail(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CE_SHORTLIST_K", "2")
    adapter = E5CeShortlistAdapter(_cfg())

    def fake_e5(
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        ranking = [
            {"id": c["id"], "score": float(100 - i), "rank": i + 1}
            for i, c in enumerate(candidates)
        ]
        return {"ranking": ranking}

    ce = MagicMock()
    ce.rank.return_value = [
        {"corpus_id": 1, "score": 9.5},
        {"corpus_id": 0, "score": 1.0},
    ]

    with patch.object(adapter._e5, "decide", side_effect=fake_e5):
        with patch(
            "finagent_mesh.clients.engines.e5_ce_shortlist._get_cross_encoder",
            return_value=ce,
        ):
            out = adapter.decide("score", "earnings", _cands(5))

    ce.rank.assert_called_once()
    assert out["backend"] == "e5_ce_shortlist"
    assert out["shortlist_method"] == "e5"
    assert out["rerank_method"] == "cross_encoder"
    assert out["n_shortlisted"] == 2
    assert len(out["ranking"]) == 5
    # CE preferred corpus_id=1 among shortlist (c0, c1) → c1 first
    assert out["ranking"][0]["id"] == "c1"


def test_ce_load_failure_is_not_silent_e5(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CE_SHORTLIST_K", "2")
    adapter = E5CeShortlistAdapter(_cfg())

    def fake_e5(
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return {
            "ranking": [
                {"id": c["id"], "score": 1.0, "rank": i + 1}
                for i, c in enumerate(candidates)
            ]
        }

    with patch.object(adapter._e5, "decide", side_effect=fake_e5):
        with patch(
            "finagent_mesh.clients.engines.e5_ce_shortlist._get_cross_encoder",
            side_effect=OpenDecisionError("Failed to load CrossEncoder"),
        ):
            with pytest.raises(OpenDecisionError, match="CrossEncoder"):
                adapter.decide("score", "q", _cands(4))


def test_empty_candidates(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CE_SHORTLIST_K", "32")
    adapter = E5CeShortlistAdapter(_cfg())
    with pytest.raises(OpenDecisionError, match="empty candidate"):
        adapter.decide("score", "q", [])
