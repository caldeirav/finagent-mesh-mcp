from finagent_mesh.matrix.merge import merge_matrix_runs
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRowResult, MatrixRun


def _row(pid: str, *, s1: float | None, s2: float | None = None) -> MatrixRowResult:
    return MatrixRowResult(
        variable_config_id=pid,
        eval_run_id=f"r:{pid}",
        stage1_engine_id="a",
        stage2_engine_id="b",
        status="completed",
        metrics=EngineMetricsRecord(n_examples=2, stage1_ndcg_at_5=s1, stage2_ndcg_at_5=s2),
    )


def test_merge_prefers_measured_over_null() -> None:
    primary = MatrixRun(
        matrix_run_id="p",
        dataset_path="/d",
        selected_example_ids=["e1"],
        rows=[_row("lux-lux", s1=0.8, s2=0.2), _row("kai-lux", s1=None)],
    )
    retry = MatrixRun(
        matrix_run_id="r",
        dataset_path="/d",
        selected_example_ids=["e1"],
        rows=[_row("kai-lux", s1=0.7, s2=0.15)],
    )
    merged = merge_matrix_runs(primary, retry, matrix_run_id="full")
    assert merged.matrix_run_id == "full"
    by_id = {r.variable_config_id: r for r in merged.rows}
    assert by_id["lux-lux"].metrics.stage1_ndcg_at_5 == 0.8
    assert by_id["kai-lux"].metrics.stage1_ndcg_at_5 == 0.7
    assert by_id["kai-lux"].eval_run_id == "r:kai-lux"


def test_merge_does_not_clobber_measured_with_null() -> None:
    primary = MatrixRun(
        matrix_run_id="p",
        dataset_path="/d",
        rows=[_row("lux-lux", s1=0.8)],
    )
    retry = MatrixRun(
        matrix_run_id="r",
        dataset_path="/d",
        rows=[_row("lux-lux", s1=None)],
    )
    merged = merge_matrix_runs(primary, retry, matrix_run_id="full")
    assert merged.rows[0].metrics.stage1_ndcg_at_5 == 0.8
