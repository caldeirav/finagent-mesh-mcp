"""007 dual empty / yield / fallback metric aggregation."""

from __future__ import annotations

from finagent_mesh.matrix.metrics import aggregate_paper_metrics, routing_class_counts


def _rec(
    *,
    empty: bool = False,
    original_empty: bool | None = None,
    ordered2: list[str] | None = None,
    recovery_used: bool = False,
    top1: str = "10-K",
    effective: str | None = None,
    top1_correct: bool = True,
    labels1: list[str] | None = None,
    labels2: list[dict] | None = None,
) -> dict:
    o2 = ordered2 if ordered2 is not None else ([] if empty else ["c1", "c2"])
    eff = effective if effective is not None else top1
    orig = original_empty if original_empty is not None else empty
    return {
        "ranking": {
            "top1_doc_type": top1,
            "original_top1_doc_type": top1,
            "original_top1_empty": orig,
            "effective_doc_type": eff,
            "yield_recovery_used": recovery_used,
            "empty_top1_chunks": empty,
            "error": "empty_top1_chunks" if empty else None,
            "top1_correct": top1_correct,
            "stage1": {"ordered_ids": [top1, "10-Q"], "ndcg_at_5": 1.0},
            "stage2": {
                "ordered_ids": o2,
                "ndcg_at_5": 0.5 if o2 else None,
                "map_at_5": 0.4 if o2 else None,
                "mrr_at_5": 0.3 if o2 else None,
                "skipped_reason": "empty_top1_chunks" if empty else None,
            },
            "expected": {
                "stage1_labels": labels1 or [top1],
                "stage2_labels": labels2
                or ([{"id": "c1", "relevance": 1}, {"id": "c2", "relevance": 0}] if o2 else []),
            },
        }
    }


def test_dual_empty_rates_recovery_off_equal():
    records = [_rec(empty=True), _rec(empty=False), _rec(empty=True)]
    m = aggregate_paper_metrics(records)
    assert m["empty_top1_chunk_rate"] == m["empty_original_top1_rate"]
    assert abs(m["empty_top1_chunk_rate"] - 2 / 3) < 1e-9


def test_post_recovery_empty_lower_than_original():
    records = [
        _rec(empty=False, original_empty=True, recovery_used=True, effective="10-Q"),
        _rec(empty=True, original_empty=True, recovery_used=False),
        _rec(empty=False, original_empty=False),
    ]
    m = aggregate_paper_metrics(records)
    assert abs(m["empty_original_top1_rate"] - 2 / 3) < 1e-9
    assert abs(m["empty_top1_chunk_rate"] - 1 / 3) < 1e-9
    assert m["n_yield_fallback"] == 1
    assert abs(m["yield_fallback_rate"] - 1 / 3) < 1e-9
    assert m["pipeline_yield"] == 2 / 3


def test_routing_fallback_footnotes():
    records = [
        _rec(empty=False, original_empty=True, recovery_used=True, effective="10-Q"),
        _rec(empty=True, original_empty=True, recovery_used=True),
        _rec(empty=False, original_empty=False),
    ]
    rc = routing_class_counts(records)
    assert rc["n_fallback_scored"] == 1
    assert rc["n_fallback_still_empty"] == 1


def test_conditional_effective_type():
    # Original Top-1 wrong/empty, effective type is gold and scored
    records = [
        _rec(
            empty=False,
            original_empty=True,
            recovery_used=True,
            top1="10-K",
            effective="10-Q",
            top1_correct=False,
            labels1=["10-Q"],
        )
    ]
    m = aggregate_paper_metrics(records)
    # given_top1: original not in gold → excluded
    assert m["stage2_ndcg_at_5_given_top1"] is None
    # given_effective: effective in gold → included
    assert m["stage2_ndcg_at_5_given_effective_type"] == 0.5
