"""Ordered first-non-empty Stage-2 type selection (007 yield recovery).

MUST NOT consult gold Stage-1 labels when choosing the effective type.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


class _HasDocType(Protocol):
    doc_type: str


@dataclass(frozen=True)
class EffectiveDocTypeSelection:
    original_top1: str | None
    effective_doc_type: str | None
    original_top1_empty: bool
    yield_recovery_used: bool
    attempted_types: list[str] = field(default_factory=list)
    skipped_missing_order: bool = False


def _pool_for(chunks: list[Any], doc_type: str) -> list[Any]:
    return [c for c in chunks if getattr(c, "doc_type", None) == doc_type]


def select_effective_doc_type(
    *,
    original_top1: str | None,
    ordered_ids: list[str] | None,
    chunks: list[Any],
    recovery_enabled: bool,
    order_missing: bool = False,
) -> EffectiveDocTypeSelection:
    """Pick Stage-2 filing type: Top-1 pool, or first non-empty in Choice order.

    When ``recovery_enabled`` and Top-1 is empty, walks ``ordered_ids`` in order.
    If Choice order is missing/incomplete for recovery, skips recovery (fail closed
    on original Top-1) and sets ``skipped_missing_order``.
    """
    if not original_top1:
        return EffectiveDocTypeSelection(
            original_top1=None,
            effective_doc_type=None,
            original_top1_empty=True,
            yield_recovery_used=False,
            attempted_types=[],
            skipped_missing_order=False,
        )

    if original_top1 == "__all__":
        # One-shot collapsed baseline — recovery N/A
        return EffectiveDocTypeSelection(
            original_top1=original_top1,
            effective_doc_type=original_top1,
            original_top1_empty=False,
            yield_recovery_used=False,
            attempted_types=[],
            skipped_missing_order=False,
        )

    original_empty = len(_pool_for(chunks, original_top1)) == 0
    if not original_empty or not recovery_enabled:
        return EffectiveDocTypeSelection(
            original_top1=original_top1,
            effective_doc_type=original_top1,
            original_top1_empty=original_empty,
            yield_recovery_used=False,
            attempted_types=[],
            skipped_missing_order=False,
        )

    ids = [str(x) for x in (ordered_ids or []) if x]
    if order_missing or not ids:
        return EffectiveDocTypeSelection(
            original_top1=original_top1,
            effective_doc_type=original_top1,
            original_top1_empty=True,
            yield_recovery_used=False,
            attempted_types=[],
            skipped_missing_order=True,
        )

    attempted: list[str] = []
    for t in ids:
        attempted.append(t)
        if len(_pool_for(chunks, t)) > 0:
            return EffectiveDocTypeSelection(
                original_top1=original_top1,
                effective_doc_type=t,
                original_top1_empty=True,
                yield_recovery_used=(t != original_top1),
                attempted_types=attempted,
                skipped_missing_order=False,
            )

    return EffectiveDocTypeSelection(
        original_top1=original_top1,
        effective_doc_type=original_top1,
        original_top1_empty=True,
        yield_recovery_used=False,
        attempted_types=attempted,
        skipped_missing_order=False,
    )
