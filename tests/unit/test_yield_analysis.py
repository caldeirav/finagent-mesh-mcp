"""007 Yield recovery analysis section keys."""

from __future__ import annotations

from finagent_mesh.matrix.analysis import (
    build_yield_recovery_comparison,
    _yield_recovery_section_md,
)
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRowResult, MatrixRun


def _matrix() -> MatrixRun:
    m = EngineMetricsRecord(
        n_examples=20,
        empty_top1_chunk_rate=0.25,
        empty_original_top1_rate=0.40,
        pipeline_yield=0.75,
        stage2_ndcg_at_5=0.40,
        stage2_ndcg_at_5_pipeline=0.30,
        stage2_ndcg_at_5_given_top1=0.45,
        stage2_ndcg_at_5_given_effective_type=0.42,
        n_yield_fallback=3,
        yield_fallback_rate=0.15,
        n_fallback_scored=2,
        n_fallback_still_empty=1,
    )
    row = MatrixRowResult(
        variable_config_id="lux-lux-yield",
        eval_run_id="yield-smoke:lux-lux-yield",
        stage1_engine_id="decision20-lux",
        stage2_engine_id="decision20-lux",
        status="completed",
        metrics=m,
        role="yield_recovery",
    )
    return MatrixRun(
        matrix_run_id="yield-paper-n20-lux-smoke",
        selected_example_ids=[f"e{i}" for i in range(20)],
        sample_seed=42,
        dataset_path="data/finagentbench",
        synthesis_enabled=False,
        rows=[row],
        status="completed",
    )


def test_yield_comparison_keys():
    payload = build_yield_recovery_comparison(_matrix())
    assert payload.get("yield_recovery_enabled") is True
    assert "lux-lux-yield" in payload.get("yield_recovery_pairs", [])
    rows = payload.get("yield_recovery_rows") or []
    assert len(rows) == 1
    row = rows[0]
    for key in (
        "empty_original_top1_rate",
        "empty_top1_chunk_rate",
        "pipeline_yield",
        "n_yield_fallback",
        "stage2_ndcg_at_5_given_effective_type",
        "baseline_pair_id",
        "delta_empty_vs_baseline",
    ):
        assert key in row
    assert row["baseline_pair_id"] == "lux-lux"


def test_yield_section_markdown():
    matrix = _matrix()
    payload = build_yield_recovery_comparison(matrix)
    md = "\n".join(_yield_recovery_section_md(matrix, payload))
    assert "## Yield recovery" in md
    assert "Dual empty" in md
    assert "effective type" in md
    assert "routing / corpus" in md or "routing / yield" in md
