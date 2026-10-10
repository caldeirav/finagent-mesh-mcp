from finagent_mesh.matrix.metrics import (
    aggregate_paper_metrics,
    contributions_from_inspect_examples,
    pipeline_means_from_contributions,
)


def test_pipeline_mean_zeros_empties() -> None:
    examples = [
        {
            "example_id": "a",
            "error": None,
            "stage1": {"top1": "10-K", "top1_in_gold": True, "gold": ["10-K"], "ndcg_at_5": 1.0},
            "stage2": {"ndcg_at_5": 0.5, "mrr_at_5": 1.0, "n_scored": 3, "rows": [{"chunk_id": "c1", "text": "x"}]},
            "expected": {"stage1_labels": ["10-K"]},
        },
        {
            "example_id": "b",
            "error": "empty_top1_chunks",
            "stage1": {"top1": "10-Q", "top1_in_gold": False, "gold": ["10-K"]},
            "stage2": {"skipped_reason": "empty_top1_chunks", "n_scored": 0, "rows": []},
            "expected": {"stage1_labels": ["10-K"]},
        },
    ]
    contribs = contributions_from_inspect_examples(examples)
    pipe = pipeline_means_from_contributions(contribs)
    assert pipe["n_scored"] == 1
    assert pipe["pipeline_yield"] == 0.5
    assert pipe["stage2_ndcg_at_5_pipeline"] == 0.25  # (0.5 + 0) / 2


def test_aggregate_includes_pipeline_fields() -> None:
    records = [
        {
            "ranking": {
                "top1_doc_type": "10-K",
                "top1_correct": True,
                "expected": {"stage1_labels": ["10-K"], "stage2_labels": ["c1"]},
                "stage1": {"ordered_ids": ["10-K"], "ndcg_at_5": 1.0},
                "stage2": {"ordered_ids": ["c1"], "ndcg_at_5": 1.0, "mrr_at_5": 1.0},
            }
        },
        {
            "ranking": {
                "top1_doc_type": "8-K",
                "top1_correct": False,
                "empty_top1_chunks": True,
                "error": "empty_top1_chunks",
                "expected": {"stage1_labels": ["10-K"], "stage2_labels": ["c1"]},
                "stage1": {"ordered_ids": ["8-K"], "ndcg_at_5": 0.0},
                "stage2": {"ordered_ids": [], "skipped_reason": "empty_top1_chunks"},
            }
        },
    ]
    agg = aggregate_paper_metrics(records)
    assert agg["n_scored"] == 1
    assert agg["pipeline_yield"] == 0.5
    assert agg["stage2_ndcg_at_5"] == 1.0  # scored-only
    assert agg["stage2_ndcg_at_5_pipeline"] == 0.5
