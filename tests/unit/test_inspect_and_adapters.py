"""Adapter and inspect-report unit tests."""

from __future__ import annotations

import pytest

from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.clients.engines.vllm_sr import VllmSrAdapter
from finagent_mesh.clients.open_decision import OpenDecisionClient
from finagent_mesh.matrix.inspect import _gold_s1, _gold_s2_map, render_inspect_html


def test_decision20_adapter_allows_score(monkeypatch: pytest.MonkeyPatch) -> None:
    cfg = EngineConfiguration(
        config_id="decision20-lux",
        family="vllm-sr",
        display_name="Lux",
        primitives=["choice", "score"],
        primary_stages=["stage1", "stage2"],
        base_url="http://localhost:8000",
    )

    def fake(self, primitive, query, candidates, metadata=None):
        return {"ranking": [{"id": "a", "score": 1.0, "rank": 1}], "distribution": {"a": 1.0}}

    monkeypatch.setattr(
        "finagent_mesh.clients.engines.http_base.HttpSystemOneAdapter.decide", fake
    )
    adapter = VllmSrAdapter(cfg)
    out = adapter.decide("score", "q", [{"id": "a", "text": "t"}])
    assert out["ranking"][0]["id"] == "a"
    with pytest.raises(ValueError, match="choice and score"):
        adapter.decide("action_cache", "q", [{"id": "a", "text": "t"}])


def test_mock_client_records_io_traces() -> None:
    client = OpenDecisionClient("http://s1", "http://s2", mock=True)
    client.reset_traces()
    client.decide("choice", "which filing?", [{"id": "10-K", "text": "10-K"}])
    assert len(client.io_traces) == 1
    assert client.io_traces[0]["primitive"] == "choice"
    assert client.io_traces[0]["error"] is None
    assert client.io_traces[0]["ranking"]


def test_inspect_html_links_pairs() -> None:
    html = render_inspect_html(
        {
            "matrix_run_id": "smoke-test",
            "pairs": [
                {
                    "pair_id": "lux-clm",
                    "eval_run_id": "smoke-test:lux-clm",
                    "stage1_engine_id": "decision20-lux",
                    "stage2_engine_id": "clm-8b",
                    "row_status": "completed",
                    "metrics": {"stage1_ndcg_at_5": 0.97, "stage2_ndcg_at_5": 0.08},
                    "n_completed": 8,
                    "n_failed_retriable": 2,
                    "examples": [
                        {
                            "example_id": "dev:q1",
                            "ledger_state": "completed",
                            "error": None,
                            "expected": {"query_text": "What is revenue?", "stage1_labels": ["10-K"]},
                            "stage1": {
                                "engine": "decision20-lux",
                                "top1": "10-K",
                                "top1_in_gold": True,
                                "gold": ["10-K"],
                                "ordered_ids": ["10-K", "10-Q"],
                                "scores": [1.0, 0.1],
                                "ndcg_at_5": 1.0,
                            },
                            "stage2": {"engine": "clm-8b", "rows": [], "ndcg_at_5": 0.2},
                            "io_traces": [],
                            "synthesis": None,
                        }
                    ],
                }
            ],
        }
    )
    assert "lux-clm" in html
    assert "What is revenue?" in html
    assert "decision20-lux" in html


def test_gold_label_parsers() -> None:
    assert _gold_s1(["10-K", {"id": "10-Q"}]) == ["10-K", "10-Q"]
    assert _gold_s2_map([{"id": "c1", "relevance": 2}])["c1"] == 2.0
