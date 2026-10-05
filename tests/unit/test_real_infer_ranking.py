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
    assert _score_batch_size("vllm-sr/Decision-2.0-Kai-0.6B") == 4
    assert _score_batch_size("vllm-sr/Decision-2.0-Lux-9B") == 4


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


def test_ordinal_score_uses_fixed_rubric(monkeypatch: pytest.MonkeyPatch) -> None:
    from finagent_mesh.clients.engines import real_infer as ri

    seen: list[dict] = []

    class FakeModel:
        def system_one(self, *, state, questions):
            seen.append(questions)
            return {
                "answers": {
                    cid: {"type": "score", "score": float(i), "probabilities": {}}
                    for i, cid in enumerate(questions)
                }
            }

    monkeypatch.setattr(ri, "_load_decision20", lambda _mid: (FakeModel(), "cpu"))
    out = ri.decide_decision20(
        model_id="vllm-sr/Decision-2.0-Lux-9B",
        query="revenue growth",
        candidates=[
            {"id": "c0", "text": "unrelated"},
            {"id": "c1", "text": "revenue grew 12%"},
        ],
        primitive="score",
    )
    assert len(seen) == 1
    q = seen[0]
    assert set(q) == {"c0", "c1"}
    for body in q.values():
        assert body["type"] == "score"
        assert body["criteria"] == ri.RELEVANCE_SCORE_CRITERIA
        assert 2 <= len(body["criteria"]) <= 10
    assert out["ranking"][0]["id"] == "c1"
    assert out["backend"].startswith("decision20_ordinal_score")


def test_choice_still_uses_id_text_criteria(monkeypatch: pytest.MonkeyPatch) -> None:
    from finagent_mesh.clients.engines import real_infer as ri

    seen: list[dict] = []

    class FakeModel:
        def system_one(self, *, state, questions):
            seen.append(questions)
            return {
                "answers": {
                    "rank": {
                        "type": "choice",
                        "choice": "10-K",
                        "probabilities": {"10-K": 0.7, "10-Q": 0.3},
                    }
                }
            }

    monkeypatch.setattr(ri, "_load_decision20", lambda _mid: (FakeModel(), "cpu"))
    out = ri.decide_decision20(
        model_id="vllm-sr/Decision-2.0-Lux-9B",
        query="annual report",
        candidates=[
            {"id": "10-K", "text": "Annual report"},
            {"id": "10-Q", "text": "Quarterly report"},
        ],
        primitive="choice",
    )
    assert seen[0]["rank"]["type"] == "choice"
    assert isinstance(seen[0]["rank"]["criteria"], dict)
    assert out["ranking"][0]["id"] == "10-K"


def test_choice_five_filing_types_not_batched(monkeypatch: pytest.MonkeyPatch) -> None:
    """Regression: Score batch size 4 must not split Stage-1 K=5 Choice."""
    from finagent_mesh.clients.engines import real_infer as ri

    calls: list[int] = []

    class FakeModel:
        def system_one(self, *, state, questions):
            crit = questions["rank"]["criteria"]
            calls.append(len(crit))
            probs = {k: 1.0 / len(crit) for k in crit}
            return {
                "answers": {
                    "rank": {
                        "type": "choice",
                        "choice": next(iter(crit)),
                        "probabilities": probs,
                    }
                }
            }

    monkeypatch.setattr(ri, "_load_decision20", lambda _mid: (FakeModel(), "cpu"))
    cands = [{"id": t, "text": t} for t in ("10-K", "10-Q", "8-K", "DEF14A", "Earnings")]
    out = ri.decide_decision20(
        model_id="vllm-sr/Decision-2.0-Lux-9B",
        query="annual report",
        candidates=cands,
        primitive="choice",
    )
    assert calls == [5]
    assert len(out["ranking"]) == 5


def test_strip_think_and_extract_first_json() -> None:
    from finagent_mesh.clients.engines.real_infer import (
        _extract_first_json_object,
        _strip_think_blocks,
    )

    raw = (
        "<think>\nreasoning here\n</think>\n"
        '{"ordered_ids":["10-K","10-Q"],"scores":[0.9,0.1]}\n'
        "The JSON above shows Earnings is best."
    )
    cleaned = _strip_think_blocks(raw)
    assert "<think>" not in cleaned.lower()
    obj = _extract_first_json_object(cleaned)
    assert obj is not None
    assert '"ordered_ids"' in obj
    assert "The JSON above" not in obj


def test_decide_ar_json_uses_thinking_off(monkeypatch: pytest.MonkeyPatch) -> None:
    from finagent_mesh.clients.engines import real_infer as ri

    seen: dict = {}

    class FakeTok:
        def apply_chat_template(self, messages, **kwargs):
            seen["kwargs"] = kwargs
            seen["messages"] = messages
            return "PROMPT"

        def __call__(self, prompt, return_tensors="pt"):
            import torch

            return {"input_ids": torch.tensor([[1, 2, 3]])}

        @property
        def eos_token_id(self):
            return 0

        def decode(self, ids, skip_special_tokens=True):
            return (
                '{"ordered_ids":["10-K","10-Q","8-K","DEF14A","Earnings"],'
                '"scores":[1,0.8,0.6,0.4,0.2]}\nMore prose'
            )

    class FakeModel:
        def generate(self, **kwargs):
            import torch

            # prompt length 3 + generated
            return torch.tensor([[1, 2, 3, 9, 9, 9]])

    monkeypatch.setattr(ri, "_load_ar", lambda _mid: (FakeTok(), FakeModel(), "cpu"))
    out = ri.decide_ar_json(
        model_id="Qwen/Qwen3-8B",
        query="q",
        candidates=[{"id": t, "text": t} for t in ("10-K", "10-Q", "8-K", "DEF14A", "Earnings")],
        primitive="choice",
    )
    assert seen["kwargs"].get("enable_thinking") is False
    assert out["ranking"][0]["id"] == "10-K"
    assert out["backend"] == "ar_json"
