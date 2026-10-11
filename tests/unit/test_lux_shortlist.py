"""Unit tests for BM25 → Lux Score shortlist adapter."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from finagent_mesh.clients.engines.lux_shortlist import LuxShortlistAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.open_decision import OpenDecisionError


def _cfg() -> EngineConfiguration:
    return EngineConfiguration(
        config_id="lux-score-shortlist-32",
        family="hybrid-ir",
        display_name="lux-shortlist",
        primitives=["score"],
        primary_stages=["stage2"],
        base_url="http://localhost:8000",
        backend="lux_shortlist",
        model_revision="test",
        is_heavy_gpu=False,
        is_light_edge=False,
    )


def _cands(n: int) -> list[dict[str, str]]:
    return [{"id": f"c{i}", "text": f"passage about topic {i} finance revenue"} for i in range(n)]


def test_shortlist_truncates_and_appends_tail(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LUX_SHORTLIST_K", "3")
    adapter = LuxShortlistAdapter(_cfg())

    def fake_bm25(
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        # Prefer higher index so shortlist is deterministic
        ranking = [
            {"id": c["id"], "score": float(i), "rank": len(candidates) - i}
            for i, c in enumerate(candidates)
        ]
        ranking.sort(key=lambda r: r["rank"])
        return {"ranking": ranking}

    lux = MagicMock()
    lux.decide.return_value = {
        "ranking": [
            {"id": "c9", "score": 10.0, "rank": 1},
            {"id": "c8", "score": 9.0, "rank": 2},
            {"id": "c7", "score": 8.0, "rank": 3},
        ],
        "distribution": {},
    }
    lux.health.return_value = (True, "ok")

    with patch.object(adapter._bm25, "decide", side_effect=fake_bm25):
        with patch.object(adapter, "_lux_adapter", return_value=lux):
            out = adapter.decide("score", "revenue", _cands(10))

    lux.decide.assert_called_once()
    short_ids = {c["id"] for c in lux.decide.call_args.args[2]}
    assert len(short_ids) == 3
    ranks = out["ranking"]
    assert len(ranks) == 10
    assert out["shortlist_k"] == 3
    assert out["shortlist_method"] == "bm25"
    assert out["backend"] == "lux_shortlist"
    assert out["n_shortlisted"] == 3


def test_empty_candidates_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LUX_SHORTLIST_K", "32")
    adapter = LuxShortlistAdapter(_cfg())
    with pytest.raises(OpenDecisionError, match="empty candidate"):
        adapter.decide("score", "q", [])


def test_invalid_k_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LUX_SHORTLIST_K", "0")
    adapter = LuxShortlistAdapter(_cfg())
    with pytest.raises(OpenDecisionError, match="LUX_SHORTLIST_K"):
        adapter.decide("score", "q", _cands(5))
