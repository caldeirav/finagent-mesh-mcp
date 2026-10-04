"""Unit tests for real-infer ranking helpers (no GPU)."""

from __future__ import annotations

import pytest

from finagent_mesh.clients.engines.real_infer import (
    RealInferError,
    _probs_from_answer,
    _score_batch_size,
    decide_anyjev,
    decide_clm,
)


def test_kai_default_score_batch_is_small() -> None:
    assert _score_batch_size("vllm-sr/Decision-2.0-Kai-0.6B") == 8
    assert _score_batch_size("vllm-sr/Decision-2.0-Lux-9B") == 16


def test_probs_from_list_scores() -> None:
    cands = [{"id": "a"}, {"id": "b"}]
    assert _probs_from_answer({"scores": [0.2, 0.8]}, cands) == {"a": 0.2, "b": 0.8}


def test_anyjev_l0_cycles_and_averages(monkeypatch: pytest.MonkeyPatch) -> None:
    from finagent_mesh.clients.engines import real_infer as ri

    orders: list[list[str]] = []

    def fake_d20(**kwargs):
        ids = [c["id"] for c in kwargs["candidates"]]
        orders.append(ids)
        ranking = [
            {"id": cid, "score": 1.0 if i == 0 else 0.0, "rank": i + 1} for i, cid in enumerate(ids)
        ]
        return {"ranking": ranking, "latency_ms": 1.0}

    monkeypatch.setattr(ri, "decide_decision20", fake_d20)
    out = decide_anyjev(
        model_id="vllm-sr/Decision-2.0-Lux-9B",
        query="q",
        candidates=[{"id": "x", "text": "X"}, {"id": "y", "text": "Y"}],
        primitive="choice",
        mode="l0",
    )
    assert orders == [["x", "y"], ["y", "x"]]
    dist = out["distribution"]
    assert dist["x"] == pytest.approx(0.5)
    assert dist["y"] == pytest.approx(0.5)
    assert out["backend"] == "anyjev_l0"


def test_clm_does_not_fall_back_to_kai(monkeypatch: pytest.MonkeyPatch) -> None:
    from finagent_mesh.clients.engines import clm_runtime

    def boom(_encoder_id: str = ""):
        raise RealInferError(clm_runtime.CLM_INSTALL_HINT)

    monkeypatch.setattr("finagent_mesh.clients.engines.clm_runtime.load_clm_engine", boom)
    with pytest.raises(RealInferError, match="Qwen3-8B"):
        decide_clm(
            model_id="Contrastive-LM/CLM-v0.1-8B",
            emb_url=None,
            query="q",
            candidates=[{"id": "c1", "text": "alpha"}],
            primitive="score",
        )
