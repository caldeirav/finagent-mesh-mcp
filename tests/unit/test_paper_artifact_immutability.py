"""SC-005: published paper artifacts must remain immutable under Unsloth guards."""

from __future__ import annotations

from pathlib import Path

import pytest

from finagent_mesh.unsloth.paths import (
    PublishedArtifactWriteError,
    assert_unsloth_run_id,
    assert_writable_artifact,
    is_published_paper_path,
)


@pytest.mark.parametrize(
    "name",
    [
        "paper-n200-full.json",
        "paper-n200-full.analysis.md",
        "paper-p1-ceilings-n200.json",
        "paper-p1-ceilings-n200.inspect.html",
    ],
)
def test_published_stems_detected(name: str):
    assert is_published_paper_path(name) is True
    with pytest.raises(PublishedArtifactWriteError):
        assert_writable_artifact(Path("artifacts/benchmarks") / name)


def test_unsloth_paths_allowed():
    assert_writable_artifact(Path("artifacts/benchmarks/unsloth-score-smoke20.json"))
    assert_unsloth_run_id("unsloth-score-paper-n200")


def test_bad_run_id_rejected():
    with pytest.raises(ValueError):
        assert_unsloth_run_id("paper-n200-full")
