"""Deterministic IR ranking metrics at @k."""

from __future__ import annotations

import math
from typing import Iterable, Sequence


def stable_rank(
    ids: Sequence[str], scores: Sequence[float]
) -> list[tuple[str, float, int]]:
    """Stable sort: score desc, then id asc. Returns (id, score, 1-based rank)."""
    paired = list(zip(ids, scores, strict=True))
    paired.sort(key=lambda x: (-x[1], x[0]))
    return [(i, s, r + 1) for r, (i, s) in enumerate(paired)]


def _relevance_map(labels: Iterable[str] | Iterable[dict]) -> dict[str, float]:
    """Build id -> graded relevance. Accepts list[str] or list[{id, relevance}]."""
    rel: dict[str, float] = {}
    for item in labels:
        if isinstance(item, str):
            rel[item] = max(rel.get(item, 0.0), 1.0)
        elif isinstance(item, dict):
            cid = str(item.get("chunk_id") or item.get("id") or item.get("doc_type"))
            grade = float(item.get("relevance", item.get("label", 1.0)))
            rel[cid] = max(rel.get(cid, 0.0), grade)
    return rel


def dcg_at_k(relevances: Sequence[float], k: int) -> float:
    total = 0.0
    for i, rel in enumerate(relevances[:k]):
        total += (2**rel - 1) / math.log2(i + 2)
    return total


def ndcg_at_k(
    ordered_ids: Sequence[str],
    labels: Iterable[str] | Iterable[dict],
    k: int = 5,
) -> float:
    rel_map = _relevance_map(labels)
    gains = [rel_map.get(i, 0.0) for i in ordered_ids]
    dcg = dcg_at_k(gains, k)
    ideal = sorted(rel_map.values(), reverse=True)
    idcg = dcg_at_k(ideal, k)
    if idcg == 0.0:
        return 0.0
    return dcg / idcg


def map_at_k(
    ordered_ids: Sequence[str],
    labels: Iterable[str] | Iterable[dict],
    k: int = 5,
) -> float:
    rel_map = _relevance_map(labels)
    relevant = {i for i, g in rel_map.items() if g > 0}
    if not relevant:
        return 0.0
    hits = 0
    precision_sum = 0.0
    for idx, cid in enumerate(ordered_ids[:k], start=1):
        if cid in relevant:
            hits += 1
            precision_sum += hits / idx
    return precision_sum / min(len(relevant), k)


def mrr_at_k(
    ordered_ids: Sequence[str],
    labels: Iterable[str] | Iterable[dict],
    k: int = 5,
) -> float:
    rel_map = _relevance_map(labels)
    relevant = {i for i, g in rel_map.items() if g > 0}
    for idx, cid in enumerate(ordered_ids[:k], start=1):
        if cid in relevant:
            return 1.0 / idx
    return 0.0
