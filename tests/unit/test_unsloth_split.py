"""Leakage-safe paper holdout split tests (SC-001)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from finagent_mesh.unsloth.split import (
    SplitLeakageError,
    assert_no_leakage,
    build_split_manifest,
    content_hash,
)


def test_assert_no_leakage_passes():
    report = assert_no_leakage(["t1", "t2"], ["a", "b"], ["c"])
    assert report["train_overlap_count"] == 0
    assert report["val_overlap_count"] == 0


def test_assert_no_leakage_fails():
    with pytest.raises(SplitLeakageError):
        assert_no_leakage(["t1"], ["t1", "a"], ["b"])


def test_build_split_manifest_paper_holdout(tmp_path: Path):
    paper = tmp_path / "paper-n200-full.json"
    test_ids = [f"ex-{i}" for i in range(200)]
    paper.write_text(
        json.dumps({"selected_example_ids": test_ids, "matrix_run_id": "paper-n200-full"}),
        encoding="utf-8",
    )
    all_ids = test_ids + [f"tr-{i}" for i in range(50)]
    manifest, report = build_split_manifest(
        all_ids, paper_matrix_path=paper, seed=42, val_fraction=0.2
    )
    assert manifest.n_test == 200
    assert manifest.test_source == "paper-n200-full"
    assert set(manifest.test_ids).isdisjoint(manifest.train_ids)
    assert set(manifest.test_ids).isdisjoint(manifest.val_ids)
    assert report["train_overlap_count"] == 0
    assert len(manifest.content_hash) == 64
    assert content_hash(
        test_ids=manifest.test_ids,
        train_ids=manifest.train_ids,
        val_ids=manifest.val_ids,
        test_source=manifest.test_source,
    ) == manifest.content_hash
