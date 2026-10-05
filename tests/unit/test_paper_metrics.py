from finagent_mesh.matrix.metrics import aggregate_paper_metrics, top1_correct, topk_recall


def test_top1_correct() -> None:
    assert top1_correct("10-K", ["10-K", "10-Q"]) is True
    assert top1_correct("8-K", ["10-K"]) is False
    assert top1_correct(None, ["10-K"]) is False


def test_topk_recall() -> None:
    assert topk_recall(["10-Q", "10-K"], ["10-K"], 1) == 0.0
    assert topk_recall(["10-Q", "10-K"], ["10-K"], 2) == 1.0


def test_aggregate_conditional_s2() -> None:
    recs = [
        {
            "ranking": {
                "top1_doc_type": "10-K",
                "top1_correct": True,
                "empty_top1_chunks": False,
                "eligible_for_conditional_s2": True,
                "expected": {
                    "stage1_labels": ["10-K"],
                    "stage2_labels": ["c1"],
                },
                "stage1": {
                    "ordered_ids": ["10-K", "10-Q"],
                    "ndcg_at_5": 1.0,
                    "map_at_5": 1.0,
                    "mrr_at_5": 1.0,
                },
                "stage2": {
                    "ordered_ids": ["c1", "c2"],
                    "ndcg_at_5": 0.8,
                    "map_at_5": 0.8,
                    "mrr_at_5": 1.0,
                },
                "io_traces": [{"primitive": "choice", "latency_ms": 10.0}],
            }
        },
        {
            "ranking": {
                "top1_doc_type": "8-K",
                "top1_correct": False,
                "empty_top1_chunks": False,
                "eligible_for_conditional_s2": False,
                "expected": {
                    "stage1_labels": ["10-K"],
                    "stage2_labels": ["c9"],
                },
                "stage1": {
                    "ordered_ids": ["8-K", "10-K"],
                    "ndcg_at_5": 0.5,
                    "map_at_5": 0.5,
                    "mrr_at_5": 0.5,
                },
                "stage2": {
                    "ordered_ids": ["c3"],
                    "ndcg_at_5": 0.0,
                    "map_at_5": 0.0,
                    "mrr_at_5": 0.0,
                },
            }
        },
    ]
    m = aggregate_paper_metrics(recs)
    assert m["n_examples"] == 2
    assert m["stage1_top1_recall"] == 0.5
    assert m["stage2_ndcg_at_5"] == 0.4
    assert m["stage2_ndcg_at_5_given_top1"] == 0.8
