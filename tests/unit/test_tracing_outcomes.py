"""Unit tests for Stage-1 / Stage-2 / Gemini outcome metrics."""

from finagent_mesh.agent.state import (
    AgentState,
    AnswerScore,
    BenchmarkExample,
    StageRankingResult,
)
from finagent_mesh.runtime.tracing import outcome_metrics


def _example(**kwargs) -> BenchmarkExample:
    base = dict(
        example_id="ex-1",
        firm_id="f1",
        query_text="What is revenue?",
        stage1_labels=["10-K"],
        stage2_labels=[{"id": "c1", "relevance": 1}],
        answer_label="42",
    )
    base.update(kwargs)
    return BenchmarkExample(**base)


def test_outcome_metrics_stage1_and_stage2() -> None:
    state = AgentState(
        example=_example(),
        top1_doc_type="10-K",
        stage1=StageRankingResult(
            stage="stage1",
            ordered_ids=["10-K", "10-Q"],
            scores=[0.9, 0.1],
            ndcg_at_5=1.0,
            map_at_5=1.0,
            mrr_at_5=1.0,
        ),
        stage2=StageRankingResult(
            stage="stage2",
            ordered_ids=["c1", "c2"],
            scores=[0.8, 0.2],
            ndcg_at_5=0.8,
            map_at_5=0.7,
            mrr_at_5=1.0,
        ),
        skip_synthesis=True,
    )
    m = outcome_metrics(state)
    assert m["stage1_ran"] == 1.0
    assert m["stage1_top1_correct"] == 1.0
    assert m["stage1_top1"] == "10-K"
    assert m["stage1_ndcg_at_5"] == 1.0
    assert m["stage2_ran"] == 1.0
    assert m["stage2_ndcg_at_5"] == 0.8
    assert m["empty_top1_chunks"] == 0.0
    assert m["gemini_status"] == "skipped_ranking_only"
    assert m["gemini_synthesis_ok"] == 0.0


def test_outcome_metrics_wrong_top1() -> None:
    state = AgentState(
        example=_example(),
        top1_doc_type="8-K",
        stage1=StageRankingResult(
            stage="stage1",
            ordered_ids=["8-K", "10-K"],
            scores=[0.6, 0.4],
            ndcg_at_5=0.5,
        ),
        stage2=StageRankingResult(
            stage="stage2",
            ordered_ids=["c9"],
            scores=[0.1],
            ndcg_at_5=0.0,
        ),
        skip_synthesis=True,
    )
    m = outcome_metrics(state)
    assert m["stage1_top1_correct"] == 0.0
    assert m["stage2_ran"] == 1.0


def test_outcome_metrics_gemini_ok() -> None:
    state = AgentState(
        example=_example(),
        top1_doc_type="10-K",
        stage1=StageRankingResult(
            stage="stage1", ordered_ids=["10-K"], scores=[1.0], ndcg_at_5=1.0
        ),
        stage2=StageRankingResult(
            stage="stage2", ordered_ids=["c1"], scores=[1.0], ndcg_at_5=1.0
        ),
        skip_synthesis=False,
        synthesized_answer="Revenue was 42.",
        answer_score=AnswerScore(
            prediction="Revenue was 42.",
            label="42",
            normalized_em=1.0,
            token_f1=0.5,
            status="scored",
        ),
    )
    m = outcome_metrics(state)
    assert m["gemini_status"] == "ok"
    assert m["gemini_synthesis_ok"] == 1.0
    assert m["gemini_answer_normalized_em"] == 1.0
    assert m["gemini_answer_token_f1"] == 0.5
    assert m["answer_normalized_em"] == 1.0


def test_outcome_metrics_gemini_skipped_empty_chunks() -> None:
    state = AgentState(
        example=_example(),
        top1_doc_type="10-K",
        stage1=StageRankingResult(
            stage="stage1", ordered_ids=["10-K"], scores=[1.0]
        ),
        stage2=None,
        skip_synthesis=False,
        error="empty_top1_chunks",
    )
    m = outcome_metrics(state)
    assert m["empty_top1_chunks"] == 1.0
    assert m["stage2_ran"] == 0.0
    assert m["gemini_status"] == "skipped_empty_top1_chunks"
    assert m["gemini_synthesis_ok"] == 0.0
    assert m["example_error"] == "empty_top1_chunks"


def test_outcome_metrics_stage2_skipped_reason() -> None:
    state = AgentState(
        example=_example(),
        top1_doc_type="10-K",
        stage1=StageRankingResult(
            stage="stage1", ordered_ids=["10-K"], scores=[1.0]
        ),
        stage2=StageRankingResult(
            stage="stage2",
            ordered_ids=[],
            scores=[],
            skipped_reason="empty_top1_chunks",
        ),
        skip_synthesis=True,
    )
    m = outcome_metrics(state)
    assert m["stage2_ran"] == 0.0
