"""Trained-track analysis comparison tests."""

from __future__ import annotations

import json
from pathlib import Path

from finagent_mesh.matrix.analysis import (
    build_trained_comparison,
    _trained_decision_section_md,
)
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRowResult, MatrixRun


def test_trained_comparison_read_only(tmp_path: Path, monkeypatch):
    root = tmp_path
    bench = root / "artifacts" / "benchmarks"
    bench.mkdir(parents=True)
    paper = {
        "rows": [
            {
                "variable_config_id": "lux-lux",
                "metrics": {"stage2_ndcg_at_5": 0.30},
            },
            {
                "variable_config_id": "lux-lux-shortlist",
                "metrics": {"stage2_ndcg_at_5": 0.35},
            },
            {
                "variable_config_id": "lux-e5",
                "metrics": {"stage2_ndcg_at_5": 0.28},
            },
        ]
    }
    (bench / "paper-n200-full.json").write_text(json.dumps(paper), encoding="utf-8")
    before = (bench / "paper-n200-full.json").read_text(encoding="utf-8")

    matrix = MatrixRun(
        matrix_run_id="unsloth-score-smoke20",
        dataset_path="data/finagentbench",
        sample_size=20,
        sample_seed=42,
        selected_example_ids=["a"],
        config_ids=["lux-unsloth-score"],
        rows=[
            MatrixRowResult(
                variable_config_id="lux-unsloth-score",
                eval_run_id="unsloth-score-smoke20:lux-unsloth-score",
                stage1_engine_id="frozen-lux-choice",
                stage2_engine_id="bm25-unsloth-score-shortlist-32",
                status="completed",
                metrics=EngineMetricsRecord(
                    n_examples=20,
                    stage2_ndcg_at_5=0.40,
                ),
                role="trained_decision",
            )
        ],
    )
    payload = build_trained_comparison(matrix, repo_root=root)
    assert payload["trained_decision_pairs"] == ["lux-unsloth-score"]
    assert len(payload["comparison_vs_published"]) == 3
    deltas = {r["baseline_pair_id"]: r["delta"] for r in payload["comparison_vs_published"]}
    assert abs(deltas["lux-lux"] - 0.10) < 1e-9
    # Immutability
    assert (bench / "paper-n200-full.json").read_text(encoding="utf-8") == before

    md = "\n".join(_trained_decision_section_md(matrix, {}, payload))
    assert "Trained decision track (Unsloth)" in md
    assert "lux-lux-shortlist" in md
