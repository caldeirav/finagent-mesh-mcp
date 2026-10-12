"""Gold-type Score export tests."""

from __future__ import annotations

import pytest

from finagent_mesh.agent.state import BenchmarkExample, PassageChunk
from finagent_mesh.unsloth.export import build_score_row, export_score_rows
from finagent_mesh.unsloth.types import SCORE_CRITERIA


def _ex(**kwargs) -> BenchmarkExample:
    base = dict(
        example_id="e1",
        firm_id="F",
        query_text="What is revenue?",
        query_category="numeric",
        stage1_labels=[{"id": "10-K", "doc_type": "10-K", "relevance": 1.0}],
        stage2_labels=[
            {"chunk_id": "c1", "relevance": 2},
            {"chunk_id": "c2", "relevance": 0},
        ],
        answer_label=None,
        chunks=[
            PassageChunk(chunk_id="c1", doc_type="10-K", text="rev up"),
            PassageChunk(chunk_id="c2", doc_type="10-K", text="other"),
            PassageChunk(chunk_id="c3", doc_type="8-K", text="noise"),
        ],
    )
    base.update(kwargs)
    return BenchmarkExample(**base)


def test_gold_type_filters_candidates():
    row = build_score_row(_ex())
    assert row is not None
    ids = {c["id"] for c in row.candidates}
    assert ids == {"c1", "c2"}
    assert "c3" not in ids
    assert row.score_criteria == list(SCORE_CRITERIA)
    assert row.labels["c1"] == 2


def test_empty_gold_pool_returns_none():
    row = build_score_row(
        _ex(
            stage1_labels=[{"id": "DEF14A", "doc_type": "DEF14A", "relevance": 1.0}],
        )
    )
    assert row is None


def test_export_stats_and_allowed_ids():
    rows, stats = export_score_rows([_ex(), _ex(example_id="e2")], allowed_ids={"e1"})
    assert stats["n_exported"] == 1
    assert stats["n_skipped_id"] == 1
    assert rows[0]["decision"]["type"] == "score"


def test_reject_non_gold_candidate_on_validate():
    from finagent_mesh.unsloth.types import ScoreTrainingRow

    bad = ScoreTrainingRow(
        example_id="e",
        query="q",
        candidates=[{"id": "x", "text": "t", "doc_type": "8-K", "relevance": 0}],
        gold_doc_types=["10-K"],
    )
    with pytest.raises(ValueError):
        bad.validate()
