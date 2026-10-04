from finagent_mesh.matrix.interpret import build_interpretation_markdown
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRun, MatrixRowResult


def test_interpretation_contains_leaderboard_and_metrics() -> None:
    matrix = MatrixRun(
        matrix_run_id="t1",
        dataset_path="./data",
        sample_size=2,
        sample_seed=1,
        selected_example_ids=["ex-001", "ex-002"],
        config_ids=["anyjev-l0", "clm-8b"],
        status="completed",
        partner_ids={"stage1_partner_id": "anyjev-l0", "stage2_partner_id": "clm-8b"},
        synthesis_enabled=False,
        rows=[
            MatrixRowResult(
                variable_config_id="anyjev-l0",
                eval_run_id="t1:anyjev-l0",
                stage1_engine_id="anyjev-l0",
                stage2_engine_id="clm-8b",
                status="completed",
                metrics=EngineMetricsRecord(
                    n_examples=2,
                    stage1_ndcg_at_5=0.9,
                    stage2_ndcg_at_5=0.8,
                ),
            ),
            MatrixRowResult(
                variable_config_id="clm-8b",
                eval_run_id="t1:clm-8b",
                stage1_engine_id="anyjev-l0",
                stage2_engine_id="clm-8b",
                status="completed",
                metrics=EngineMetricsRecord(
                    n_examples=2,
                    stage1_ndcg_at_5=0.7,
                    stage2_ndcg_at_5=0.85,
                ),
            ),
        ],
    )
    md = build_interpretation_markdown(matrix)
    assert "Leaderboard" in md
    assert "anyjev-l0" in md
    assert "Interpretation" in md
    assert "nDCG@5" in md
