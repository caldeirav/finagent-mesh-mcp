"""Train metadata + paper write-guard tests (no GPU / Unsloth)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from finagent_mesh.unsloth.paths import PublishedArtifactWriteError, assert_writable_artifact
from finagent_mesh.unsloth.train import assert_split_matches_paper, run_supervised_score_train


def test_refuse_paper_artifact_write(tmp_path: Path):
    with pytest.raises(PublishedArtifactWriteError):
        assert_writable_artifact(tmp_path / "paper-n200-full.json")


def test_assert_split_matches_paper():
    assert_split_matches_paper({"test_ids": ["a", "b"]}, ["b", "a"])
    with pytest.raises(ValueError):
        assert_split_matches_paper({"test_ids": ["a"]}, ["a", "b"])


def test_fab_row_to_decision_rows():
    from finagent_mesh.unsloth.train import fab_row_to_decision_rows

    rows = fab_row_to_decision_rows(
        {
            "example_id": "e1",
            "query": "What is revenue?",
            "candidates": [
                {"id": "c1", "text": "Revenue rose", "doc_type": "10-K", "relevance": 2},
                {"id": "c2", "text": "Other", "doc_type": "10-K", "relevance": 0},
            ],
            "decision": {
                "type": "score",
                "instructions": "Rank passages for answering the query.",
                "criteria": ["not relevant", "partially relevant", "highly relevant"],
            },
        }
    )
    assert len(rows) == 2
    assert rows[0]["questions"]["relevance"]["type"] == "score"
    assert rows[0]["gold"]["relevance"] == 2
    assert "Query:" in rows[0]["state"]


def test_dry_run_train_writes_meta(tmp_path: Path):
    ds = tmp_path / "ds"
    ds.mkdir()
    test_ids = [f"t{i}" for i in range(200)]
    (ds / "split_manifest.json").write_text(
        json.dumps(
            {
                "manifest_id": "m1",
                "test_ids": test_ids,
                "content_hash": "abc",
            }
        ),
        encoding="utf-8",
    )
    (ds / "train.jsonl").write_text(
        json.dumps(
            {
                "example_id": "x",
                "query": "q",
                "candidates": [{"id": "c", "text": "t", "doc_type": "10-K", "relevance": 1}],
                "decision": {"type": "score", "criteria": ["not relevant", "partially relevant", "highly relevant"]},
            }
        )
        + "\n",
        encoding="utf-8",
    )
    out = tmp_path / "ckpt"
    meta = run_supervised_score_train(
        dataset_dir=ds,
        out_dir=out,
        train_run_id="unsloth-train-score-smoke",
        dry_run=True,
        max_train_rows=10,
    )
    assert meta.status == "completed"
    assert (out / "train_run.json").exists()
    assert "paper-n200-full" not in str(out)
