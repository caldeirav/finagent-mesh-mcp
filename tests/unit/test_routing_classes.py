from finagent_mesh.matrix.metrics import assign_routing_class, routing_class_counts


def _rec(**kwargs):
    base = {
        "top1_doc_type": "10-K",
        "top1_correct": True,
        "empty_top1_chunks": False,
        "expected": {"stage1_labels": ["10-K"]},
        "stage2": {"ordered_ids": ["c1"], "skipped_reason": None},
    }
    base.update(kwargs)
    return base


def test_routing_classes_partition() -> None:
    records = [
        {"ranking": _rec()},  # correct_scored
        {"ranking": _rec(empty_top1_chunks=True, stage2={"ordered_ids": [], "skipped_reason": "empty_top1_chunks"})},
        {"ranking": _rec(top1_correct=False)},
        {"ranking": _rec(top1_correct=False, empty_top1_chunks=True, stage2={"ordered_ids": [], "skipped_reason": "empty_top1_chunks"})},
        {"ranking": _rec(top1_doc_type=None)},
    ]
    out = routing_class_counts(records)
    assert out["n_examples"] == 5
    assert sum(out["counts"].values()) == 5
    assert out["counts"]["correct_top1_scored"] == 1
    assert out["counts"]["correct_top1_empty"] == 1
    assert out["counts"]["wrong_top1_scored"] == 1
    assert out["counts"]["wrong_top1_empty"] == 1
    assert out["counts"]["missing_top1"] == 1


def test_assign_empty_wrong() -> None:
    r = _rec(
        top1_correct=False,
        empty_top1_chunks=True,
        stage2={"ordered_ids": [], "skipped_reason": "empty_top1_chunks"},
    )
    assert assign_routing_class(r) == "wrong_top1_empty"
