from finagent_mesh.matrix.analysis import build_analysis_markdown, build_analysis_payload
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRowResult, MatrixRun


def _matrix() -> MatrixRun:
    return MatrixRun(
        matrix_run_id="t-run",
        dataset_path="/tmp/data",
        sample_size=2,
        sample_seed=42,
        selected_example_ids=["e1", "e2"],
        synthesis_enabled=False,
        rows=[
            MatrixRowResult(
                variable_config_id="lux-lux",
                eval_run_id="t-run:lux-lux",
                stage1_engine_id="decision20-lux",
                stage2_engine_id="decision20-lux",
                status="completed",
                blocks=["A", "B"],
                metrics=EngineMetricsRecord(
                    n_examples=2,
                    stage1_ndcg_at_5=0.9,
                    stage2_ndcg_at_5=0.4,
                    stage2_ndcg_at_5_given_top1=0.5,
                    empty_top1_chunk_rate=0.25,
                    n_empty_top1=0,
                    blocks=["A", "B"],
                ),
            ),
            MatrixRowResult(
                variable_config_id="kai-lux",
                eval_run_id="t-run:kai-lux",
                stage1_engine_id="decision20-kai",
                stage2_engine_id="decision20-lux",
                status="completed",
                blocks=["A"],
                metrics=EngineMetricsRecord(
                    n_examples=2,
                    stage1_ndcg_at_5=0.8,
                    stage2_ndcg_at_5=0.35,
                    blocks=["A"],
                ),
            ),
        ],
        skip_records=[
            {
                "pair_id": "lux-clm-ft",
                "reason": "deferred_issue",
                "issue_url": "https://github.com/caldeirav/finagent-mesh-mcp/issues/1",
            }
        ],
    )


def test_findings_guard_fixed_s2() -> None:
    m = _matrix()
    payload = build_analysis_payload(
        m,
        inspect_examples={
            "lux-lux": [{"example_id": "e1", "ledger_state": "completed"}],
            "kai-lux": [{"example_id": "e1", "ledger_state": "completed"}],
        },
    )
    text = " ".join(payload["findings"])
    assert "decision20-lux" in text
    assert "not run" in text.lower() or "ranking-only" in text.lower()
    assert any(i["href"].endswith("#pair-lux-lux") for i in payload["artifact_index"])
    assert "executive_summary" in payload
    assert payload["findings_detail"]["block_a"]
    assert payload["findings_detail"]["takeaways"]
    assert payload["pair_outcomes"]


def test_analysis_markdown_has_blocks() -> None:
    m = _matrix()
    payload = build_analysis_payload(m)
    md = build_analysis_markdown(m, payload)
    assert "## Executive summary" in md
    assert "## How to read this report" in md
    assert "## Block A" in md
    assert "## Block B" in md
    assert "### Block A findings" in md
    assert "lux-lux" in md
    assert "Δ vs Lux" in md or "vs Lux" in md
    assert "issues/1" in md
    assert "## Takeaways" in md
    assert "## Pair outcomes" in md
