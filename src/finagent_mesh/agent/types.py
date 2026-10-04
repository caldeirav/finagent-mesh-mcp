"""Shared document-type constants and helpers."""

from __future__ import annotations

from typing import Sequence

DOC_TYPES: tuple[str, ...] = ("10-K", "10-Q", "8-K", "Earnings", "DEF14A")
DOC_TYPE_SET = frozenset(DOC_TYPES)


def validate_doc_types(values: Sequence[str]) -> list[str]:
    invalid = [v for v in values if v not in DOC_TYPE_SET]
    if invalid:
        raise ValueError(f"Invalid document types: {invalid}; allowed={list(DOC_TYPES)}")
    return list(values)


def top1_doc_type(ordered_ids: Sequence[str]) -> str | None:
    """Return the Top-1 Stage-1 document type, or None if empty."""
    if not ordered_ids:
        return None
    return ordered_ids[0]
