"""007 yield recovery: first-non-empty selection and gates."""

from __future__ import annotations

from types import SimpleNamespace

from finagent_mesh.agent.yield_recovery import select_effective_doc_type


def _chunks(*types: str):
    return [SimpleNamespace(doc_type=t, chunk_id=f"{t}-{i}") for i, t in enumerate(types)]


def test_top1_nonempty_no_fallback():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q", "8-K"],
        chunks=_chunks("10-K", "10-Q"),
        recovery_enabled=True,
    )
    assert sel.original_top1_empty is False
    assert sel.effective_doc_type == "10-K"
    assert sel.yield_recovery_used is False
    assert sel.attempted_types == []


def test_top1_empty_rank2_has_chunks():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q", "8-K"],
        chunks=_chunks("10-Q", "8-K"),
        recovery_enabled=True,
    )
    assert sel.original_top1_empty is True
    assert sel.effective_doc_type == "10-Q"
    assert sel.yield_recovery_used is True
    assert sel.attempted_types == ["10-K", "10-Q"]


def test_all_empty_fail_closed():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q", "8-K"],
        chunks=_chunks(),
        recovery_enabled=True,
    )
    assert sel.original_top1_empty is True
    assert sel.effective_doc_type == "10-K"
    assert sel.yield_recovery_used is False
    assert sel.attempted_types == ["10-K", "10-Q", "8-K"]


def test_all_sentinel_unchanged():
    sel = select_effective_doc_type(
        original_top1="__all__",
        ordered_ids=["__all__"],
        chunks=_chunks("10-K"),
        recovery_enabled=True,
    )
    assert sel.effective_doc_type == "__all__"
    assert sel.yield_recovery_used is False
    assert sel.original_top1_empty is False


def test_missing_ordered_ids_skips_recovery():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=[],
        chunks=_chunks("10-Q"),
        recovery_enabled=True,
    )
    assert sel.skipped_missing_order is True
    assert sel.yield_recovery_used is False
    assert sel.effective_doc_type == "10-K"


def test_recovery_disabled_keeps_empty_top1():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q"],
        chunks=_chunks("10-Q"),
        recovery_enabled=False,
    )
    assert sel.original_top1_empty is True
    assert sel.effective_doc_type == "10-K"
    assert sel.yield_recovery_used is False


def test_gold_later_does_not_win_over_earlier_nongold():
    """Gold type later in Choice order must not beat earlier non-empty non-gold."""
    gold = "8-K"
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q", gold],
        chunks=_chunks("10-Q", gold),
        recovery_enabled=True,
    )
    assert sel.effective_doc_type == "10-Q"
    assert sel.effective_doc_type != gold
    assert sel.yield_recovery_used is True


def test_order_missing_flag_skips():
    sel = select_effective_doc_type(
        original_top1="10-K",
        ordered_ids=["10-K", "10-Q"],
        chunks=_chunks("10-Q"),
        recovery_enabled=True,
        order_missing=True,
    )
    assert sel.skipped_missing_order is True
    assert sel.yield_recovery_used is False
