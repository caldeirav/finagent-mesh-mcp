"""007 path guards: yield writable; paper/unsloth baselines refused."""

from __future__ import annotations

from pathlib import Path

import pytest

from finagent_mesh.unsloth.paths import (
    PublishedArtifactWriteError,
    assert_unsloth_run_id,
    assert_writable_artifact,
    assert_yield_run_id,
    is_immutable_eval_path,
    is_yield_artifact_stem,
)


@pytest.mark.parametrize(
    "name",
    [
        "paper-n200-full.json",
        "paper-p1-ceilings-n200.analysis.md",
        "unsloth-score-paper-n200.json",
        "unsloth-score-paper-n200.analysis.md",
    ],
)
def test_immutable_baselines_refused(name: str):
    assert is_immutable_eval_path(name) is True
    with pytest.raises(PublishedArtifactWriteError):
        assert_writable_artifact(Path("artifacts/benchmarks") / name)


@pytest.mark.parametrize(
    "name",
    [
        "yield-paper-n200-lux.json",
        "yield-unsloth-score-paper-n200.analysis.md",
        "lux-lux-yield-smoke20.json",
    ],
)
def test_yield_stems_writable(name: str):
    assert is_yield_artifact_stem(name) is True
    assert_writable_artifact(Path("artifacts/benchmarks") / name)


def test_yield_run_id_ok():
    assert_yield_run_id("yield-unsloth-score-paper-n200")


def test_yield_run_id_rejects_non_prefix():
    with pytest.raises(ValueError):
        assert_yield_run_id("unsloth-score-paper-n200")


def test_unsloth_run_id_still_rejects_published():
    with pytest.raises(PublishedArtifactWriteError):
        assert_unsloth_run_id("unsloth-score-paper-n200")


def test_existing_paper_immutability_compat():
    """Keep prior test_paper_artifact_immutability expectations."""
    from finagent_mesh.unsloth.paths import is_published_paper_path

    assert is_published_paper_path("paper-n200-full.json")
    assert_writable_artifact(Path("artifacts/benchmarks/unsloth-score-smoke20.json"))
