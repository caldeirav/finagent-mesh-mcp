"""Paper reviewer metrics: routing recall, conditional Stage-2, latency percentiles."""

from __future__ import annotations

from typing import Any, Literal

from finagent_mesh.metrics.ranking import map_at_k, mrr_at_k, ndcg_at_k

RoutingClass = Literal[
    "correct_top1_scored",
    "correct_top1_empty",
    "wrong_top1_scored",
    "wrong_top1_empty",
    "missing_top1",
    "other",
]

ROUTING_CLASS_IDS: tuple[str, ...] = (
    "correct_top1_scored",
    "correct_top1_empty",
    "wrong_top1_scored",
    "wrong_top1_empty",
    "missing_top1",
    "other",
)


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
        "n_scored": len(s2_ndcg),
        "pipeline_yield": len(s2_ndcg) / n if n else 0.0,
        "stage2_ndcg_at_5_pipeline": _pipeline_avg(s2_ndcg, n, empty_idxs=None, records=records, metric="ndcg"),
        "stage2_mrr_at_5_pipeline": _pipeline_avg_mrr(records),
    }


def _is_empty(ranking: dict[str, Any]) -> bool:
    s2 = ranking.get("stage2") or {}
    return bool(
        ranking.get("empty_top1_chunks")
        or ranking.get("error") == "empty_top1_chunks"
        or s2.get("skipped_reason") == "empty_top1_chunks"
    )


def _is_scored(ranking: dict[str, Any]) -> bool:
    s2 = ranking.get("stage2") or {}
    ordered2 = list(s2.get("ordered_ids") or [])
    return bool(ordered2) and not _is_empty(ranking)


def assign_routing_class(ranking: dict[str, Any]) -> RoutingClass:
    """Mutually exclusive routing outcome class for one example."""
    top1 = ranking.get("top1_doc_type")
    expected = ranking.get("expected") or {}
    labels1 = expected.get("stage1_labels") or []
    empty = _is_empty(ranking)
    scored = _is_scored(ranking)
    if not top1 or top1 == "__all__":
        if top1 == "__all__" and scored:
            return "other"
        return "missing_top1" if not top1 else "other"
    correct = ranking.get("top1_correct")
    if correct is None:
        correct = top1_correct(top1, labels1)
    if correct and scored:
        return "correct_top1_scored"
    if correct and empty:
        return "correct_top1_empty"
    if (not correct) and scored:
        return "wrong_top1_scored"
    if (not correct) and empty:
        return "wrong_top1_empty"
    return "other"


def routing_class_counts(records: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(records)
    counts = {cid: 0 for cid in ROUTING_CLASS_IDS}
    for rec in records:
        ranking = rec.get("ranking") or rec
        cid = assign_routing_class(ranking)
        counts[cid] = counts.get(cid, 0) + 1
    rates = {k: (v / n if n else 0.0) for k, v in counts.items()}
    n_scored = counts["correct_top1_scored"] + counts["wrong_top1_scored"]
    return {
        "n_examples": n,
        "counts": counts,
        "rates": rates,
        "n_scored": n_scored,
        "pipeline_yield": n_scored / n if n else 0.0,
    }


def _example_s2_metrics(ranking: dict[str, Any]) -> tuple[float | None, float | None]:
    expected = ranking.get("expected") or {}
    s2 = ranking.get("stage2") or {}
    labels2 = expected.get("stage2_labels") or []
    ordered2 = list(s2.get("ordered_ids") or [])
    if not ordered2 or not labels2 or _is_empty(ranking):
        return None, None
    n2 = float(s2["ndcg_at_5"]) if s2.get("ndcg_at_5") is not None else ndcg_at_k(ordered2, labels2, 5)
    r2 = float(s2["mrr_at_5"]) if s2.get("mrr_at_5") is not None else mrr_at_k(ordered2, labels2, 5)
    return n2, r2


def _pipeline_avg(
    scored_values: list[float],
    n: int,
    *,
    empty_idxs: Any,
    records: list[dict[str, Any]],
    metric: str,
) -> float | None:
    del scored_values, empty_idxs, metric
    if n == 0:
        return None
    total = 0.0
    for rec in records:
        ranking = rec.get("ranking") or rec
        n2, _ = _example_s2_metrics(ranking)
        total += float(n2 or 0.0)
    return total / n


def _pipeline_avg_mrr(records: list[dict[str, Any]]) -> float | None:
    n = len(records)
    if n == 0:
        return None
    total = 0.0
    for rec in records:
        ranking = rec.get("ranking") or rec
        _, r2 = _example_s2_metrics(ranking)
        total += float(r2 or 0.0)
    return total / n


def per_example_contributions(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """One contribution dict per example for bootstrap / strata / win-loss."""
    out: list[dict[str, Any]] = []
    for rec in records:
        ranking = rec.get("ranking") or rec
        expected = ranking.get("expected") or {}
        s1 = ranking.get("stage1") or {}
        labels1 = expected.get("stage1_labels") or []
        ordered1 = list(s1.get("ordered_ids") or [])
        top1 = ranking.get("top1_doc_type")
        correct = ranking.get("top1_correct")
        if correct is None:
            correct = top1_correct(top1, labels1)
        empty = _is_empty(ranking)
        scored = _is_scored(ranking)
        s1_ndcg = None
        if ordered1 and labels1:
            s1_ndcg = (
                float(s1["ndcg_at_5"])
                if s1.get("ndcg_at_5") is not None
                else ndcg_at_k(ordered1, labels1, 5)
            )
        s2_ndcg, s2_mrr = _example_s2_metrics(ranking)
        # Gold filing type: first gold type id if present
        gold_types = sorted(_gold_type_ids(labels1))
        gold_type = gold_types[0] if gold_types else None
        cand_n = len(list((ranking.get("stage2") or {}).get("ordered_ids") or []))
        # Length proxy: sum of chunk text lengths when present on ranking
        length_chars = 0
        for ch in ranking.get("stage2_chunks") or []:
            length_chars += len(str(ch.get("text") or ""))
        if not length_chars:
            for row in (ranking.get("stage2") or {}).get("rows") or []:
                length_chars += len(str(row.get("text") or ""))
        out.append(
            {
                "example_id": str(
                    ranking.get("example_id")
                    or expected.get("example_id")
                    or rec.get("example_id")
                    or ""
                ),
                "routing_class": assign_routing_class(ranking),
                "top1_correct": bool(correct),
                "empty_top1": empty,
                "scored": scored,
                "stage1_ndcg_at_5": s1_ndcg,
                "stage2_ndcg_at_5": s2_ndcg,
                "stage2_mrr_at_5": s2_mrr,
                "gold_type": gold_type,
                "cand_size": cand_n,
                "length_chars": length_chars,
            }
        )
    return out


def contributions_from_inspect_examples(
    examples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Build contribution records from inspect HTML/JSON example dicts.

    Prefer stored per-example nDCG/MRR when present (avoid recomputing from truncated rows).
    """
    out: list[dict[str, Any]] = []
    for ex in examples:
        s1 = ex.get("stage1") or {}
        s2 = ex.get("stage2") or {}
        expected = ex.get("expected") or {}
        empty = (
            ex.get("error") == "empty_top1_chunks"
            or s2.get("skipped_reason") == "empty_top1_chunks"
        )
        n_scored = int(s2.get("n_scored") or 0)
        row_ids = [r.get("chunk_id") for r in (s2.get("rows") or []) if r.get("chunk_id")]
        scored = (not empty) and (n_scored > 0 or bool(row_ids) or s2.get("ndcg_at_5") is not None)
        if empty:
            scored = False
        top1 = s1.get("top1")
        correct = s1.get("top1_in_gold")
        if correct is None:
            correct = top1_correct(top1, expected.get("stage1_labels") or list(s1.get("gold") or []))
        # Routing class via a minimal ranking dict
        ranking = {
            "top1_doc_type": top1,
            "top1_correct": correct,
            "empty_top1_chunks": empty,
            "error": ex.get("error"),
            "expected": {
                "stage1_labels": expected.get("stage1_labels") or list(s1.get("gold") or []),
            },
            "stage2": {
                "ordered_ids": row_ids or ([f"__s{i}" for i in range(n_scored)] if scored else []),
                "skipped_reason": s2.get("skipped_reason"),
            },
        }
        gold_types = sorted(_gold_type_ids(ranking["expected"]["stage1_labels"]))
        length_chars = sum(len(str(r.get("text") or "")) for r in (s2.get("rows") or []))
        out.append(
            {
                "example_id": str(ex.get("example_id") or ""),
                "routing_class": assign_routing_class(ranking),
                "top1_correct": bool(correct),
                "empty_top1": empty,
                "scored": scored,
                "stage1_ndcg_at_5": (
                    float(s1["ndcg_at_5"]) if s1.get("ndcg_at_5") is not None else None
                ),
                "stage2_ndcg_at_5": (
                    float(s2["ndcg_at_5"]) if scored and s2.get("ndcg_at_5") is not None else None
                ),
                "stage2_mrr_at_5": (
                    float(s2["mrr_at_5"]) if scored and s2.get("mrr_at_5") is not None else None
                ),
                "gold_type": gold_types[0] if gold_types else None,
                "cand_size": n_scored or len(row_ids),
                "length_chars": length_chars,
            }
        )
    return out


def pipeline_means_from_contributions(contribs: list[dict[str, Any]]) -> dict[str, float | None]:
    n = len(contribs)
    if n == 0:
        return {
            "pipeline_yield": 0.0,
            "n_scored": 0,
            "stage2_ndcg_at_5_pipeline": None,
            "stage2_mrr_at_5_pipeline": None,
        }
    n_scored = sum(1 for c in contribs if c.get("scored"))
    ndcg_sum = sum(float(c["stage2_ndcg_at_5"] or 0.0) for c in contribs)
    mrr_sum = sum(float(c["stage2_mrr_at_5"] or 0.0) for c in contribs)
    return {
        "pipeline_yield": n_scored / n,
        "n_scored": n_scored,
        "stage2_ndcg_at_5_pipeline": ndcg_sum / n,
        "stage2_mrr_at_5_pipeline": mrr_sum / n,
    }


def routing_classes_from_contributions(contribs: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(contribs)
    counts = {cid: 0 for cid in ROUTING_CLASS_IDS}
    for c in contribs:
        cid = str(c.get("routing_class") or "other")
        if cid not in counts:
            cid = "other"
        counts[cid] += 1
    rates = {k: (v / n if n else 0.0) for k, v in counts.items()}
    n_scored = counts["correct_top1_scored"] + counts["wrong_top1_scored"]
    return {
        "n_examples": n,
        "counts": counts,
        "rates": rates,
        "n_scored": n_scored,
        "pipeline_yield": n_scored / n if n else 0.0,
    }
