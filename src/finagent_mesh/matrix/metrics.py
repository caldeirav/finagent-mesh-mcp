"""Paper reviewer metrics: routing recall, conditional Stage-2, latency percentiles."""

from __future__ import annotations

from typing import Any

from finagent_mesh.metrics.ranking import map_at_k, mrr_at_k, ndcg_at_k


def _gold_type_ids(labels: list[Any]) -> set[str]:
    out: set[str] = set()
    for item in labels or []:
        if isinstance(item, str):
            out.add(item)
        elif isinstance(item, dict):
            cid = item.get("doc_type") or item.get("id") or item.get("chunk_id")
            if cid:
                out.add(str(cid))
    return out


def top1_correct(top1: str | None, stage1_labels: list[Any]) -> bool:
    if not top1:
        return False
    gold = _gold_type_ids(stage1_labels)
    return top1 in gold if gold else False


def topk_recall(ordered_ids: list[str], stage1_labels: list[Any], k: int) -> float | None:
    gold = _gold_type_ids(stage1_labels)
    if not gold:
        return None
    hit = any(i in gold for i in ordered_ids[:k])
    return 1.0 if hit else 0.0


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    xs = sorted(values)
    if len(xs) == 1:
        return xs[0]
    rank = (p / 100.0) * (len(xs) - 1)
    lo = int(rank)
    hi = min(lo + 1, len(xs) - 1)
    frac = rank - lo
    return xs[lo] * (1 - frac) + xs[hi] * frac


def aggregate_paper_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate per-example ranking payloads into reviewer metrics.

    Each record should include ranking payload fields plus optional latency lists.
    """
    n = len(records)
    if n == 0:
        return {"n_examples": 0}

    s1_ndcg: list[float] = []
    s1_map: list[float] = []
    s1_mrr: list[float] = []
    s2_ndcg: list[float] = []
    s2_map: list[float] = []
    s2_mrr: list[float] = []
    s2_ndcg_cond: list[float] = []
    s2_map_cond: list[float] = []
    s2_mrr_cond: list[float] = []
    top1_hits: list[float] = []
    top5_hits: list[float] = []
    empty_top1 = 0
    ofr_flags: list[float] = []
    parse_flags: list[float] = []
    lat_s1: list[float] = []
    lat_s2: list[float] = []

    for rec in records:
        ranking = rec.get("ranking") or rec
        expected = ranking.get("expected") or {}
        s1 = ranking.get("stage1") or {}
        s2 = ranking.get("stage2") or {}
        top1 = ranking.get("top1_doc_type")
        labels1 = expected.get("stage1_labels") or []
        labels2 = expected.get("stage2_labels") or []
        ordered1 = list(s1.get("ordered_ids") or [])
        ordered2 = list(s2.get("ordered_ids") or [])

        empty = bool(
            ranking.get("empty_top1_chunks")
            or ranking.get("error") == "empty_top1_chunks"
            or s2.get("skipped_reason") == "empty_top1_chunks"
        )
        if empty:
            empty_top1 += 1

        correct = ranking.get("top1_correct")
        if correct is None:
            correct = top1_correct(top1, labels1)
        eligible = ranking.get("eligible_for_conditional_s2")
        if eligible is None:
            eligible = bool(correct) and not empty

        if ordered1:
            t1 = topk_recall(ordered1, labels1, 1)
            t5 = topk_recall(ordered1, labels1, 5)
            if t1 is not None:
                top1_hits.append(t1)
            if t5 is not None:
                top5_hits.append(t5)
            if s1.get("ndcg_at_5") is not None:
                s1_ndcg.append(float(s1["ndcg_at_5"]))
            elif labels1:
                s1_ndcg.append(ndcg_at_k(ordered1, labels1, 5))
            if s1.get("map_at_5") is not None:
                s1_map.append(float(s1["map_at_5"]))
            elif labels1:
                s1_map.append(map_at_k(ordered1, labels1, 5))
            if s1.get("mrr_at_5") is not None:
                s1_mrr.append(float(s1["mrr_at_5"]))
            elif labels1:
                s1_mrr.append(mrr_at_k(ordered1, labels1, 5))

        if ordered2 and labels2:
            n2 = float(s2["ndcg_at_5"]) if s2.get("ndcg_at_5") is not None else ndcg_at_k(ordered2, labels2, 5)
            m2 = float(s2["map_at_5"]) if s2.get("map_at_5") is not None else map_at_k(ordered2, labels2, 5)
            r2 = float(s2["mrr_at_5"]) if s2.get("mrr_at_5") is not None else mrr_at_k(ordered2, labels2, 5)
            s2_ndcg.append(n2)
            s2_map.append(m2)
            s2_mrr.append(r2)
            if eligible:
                s2_ndcg_cond.append(n2)
                s2_map_cond.append(m2)
                s2_mrr_cond.append(r2)

        if ranking.get("option_flipped") is not None:
            ofr_flags.append(1.0 if ranking.get("option_flipped") else 0.0)
        if ranking.get("parse_failure") is not None:
            parse_flags.append(1.0 if ranking.get("parse_failure") else 0.0)
        elif ranking.get("error") and "parse" in str(ranking.get("error")).lower():
            parse_flags.append(1.0)

        for tr in ranking.get("io_traces") or []:
            lat = tr.get("latency_ms")
            if lat is None:
                continue
            if tr.get("primitive") == "choice":
                lat_s1.append(float(lat))
            elif tr.get("primitive") in {"score", "action_cache"}:
                lat_s2.append(float(lat))

    def _avg(xs: list[float]) -> float | None:
        return sum(xs) / len(xs) if xs else None

    return {
        "n_examples": n,
        "stage1_ndcg_at_5": _avg(s1_ndcg),
        "stage1_map_at_5": _avg(s1_map),
        "stage1_mrr_at_5": _avg(s1_mrr),
        "stage2_ndcg_at_5": _avg(s2_ndcg),
        "stage2_map_at_5": _avg(s2_map),
        "stage2_mrr_at_5": _avg(s2_mrr),
        "stage2_ndcg_at_5_given_top1": _avg(s2_ndcg_cond),
        "stage2_map_at_5_given_top1": _avg(s2_map_cond),
        "stage2_mrr_at_5_given_top1": _avg(s2_mrr_cond),
        "stage1_top1_recall": _avg(top1_hits),
        "stage1_top5_recall": _avg(top5_hits),
        "empty_top1_chunk_rate": empty_top1 / n,
        "option_flip_rate": _avg(ofr_flags),
        "parse_failure_rate": _avg(parse_flags),
        "latency_stage1_p50_ms": percentile(lat_s1, 50),
        "latency_stage1_p95_ms": percentile(lat_s1, 95),
        "latency_stage2_p50_ms": percentile(lat_s2, 50),
        "latency_stage2_p95_ms": percentile(lat_s2, 95),
        "n_empty_top1": empty_top1,
    }
