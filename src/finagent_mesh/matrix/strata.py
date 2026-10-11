"""Block B strata and win/tie/loss vs Lux Score (paper P0)."""

from __future__ import annotations

from typing import Any

TIE_EPS = 0.01


def cand_size_bucket(n: int) -> str:
    if n <= 8:
        return "1-8"
    if n <= 32:
        return "9-32"
    if n <= 128:
        return "33-128"
    return "129+"


def length_bucket(chars: int, cuts: list[int]) -> str:
    """cuts = sorted quartile cutpoints (3 values) from scored set."""
    if not cuts:
        return "all"
    a, b, c = cuts[0], cuts[1], cuts[2]
    if chars <= a:
        return f"Q1(≤{a})"
    if chars <= b:
        return f"Q2(≤{b})"
    if chars <= c:
        return f"Q3(≤{c})"
    return f"Q4(>{c})"


def quartile_cuts(values: list[int]) -> list[int]:
    if not values:
        return []
    xs = sorted(values)
    n = len(xs)

    def q(p: float) -> int:
        i = int(p * (n - 1))
        return int(xs[i])

    return [q(0.25), q(0.5), q(0.75)]


def build_strata(
    by_pair: dict[str, list[dict[str, Any]]],
    *,
    pair_ids: list[str],
) -> list[dict[str, Any]]:
    """Stratum cells for gold_type / cand_size / length axes."""
    # Length cuts from union of scored contribs across pairs
    lengths: list[int] = []
    for pid in pair_ids:
        for c in by_pair.get(pid) or []:
            if c.get("scored"):
                lengths.append(int(c.get("length_chars") or 0))
    cuts = quartile_cuts(lengths)
    cells: list[dict[str, Any]] = []

    def add_axis(axis: str, bucket_fn) -> None:
        buckets: dict[str, dict[str, list[float]]] = {}
        for pid in pair_ids:
            for c in by_pair.get(pid) or []:
                if not c.get("scored"):
                    continue
                b = bucket_fn(c)
                if b is None:
                    continue
                buckets.setdefault(b, {}).setdefault(pid, []).append(
                    float(c.get("stage2_ndcg_at_5") or 0.0)
                )
        for bucket, pid_map in sorted(buckets.items()):
            for pid, vals in pid_map.items():
                cells.append(
                    {
                        "axis": axis,
                        "bucket": bucket,
                        "pair_id": pid,
                        "n": len(vals),
                        "stage2_ndcg_at_5": sum(vals) / len(vals) if vals else None,
                    }
                )

    add_axis("gold_type", lambda c: c.get("gold_type") or "unknown")
    add_axis("cand_size", lambda c: cand_size_bucket(int(c.get("cand_size") or 0)))
    add_axis("length", lambda c: length_bucket(int(c.get("length_chars") or 0), cuts))
    return cells


def win_loss_vs_baseline(
    baseline: list[dict[str, Any]],
    challenger: list[dict[str, Any]],
    *,
    baseline_pair_id: str,
    challenger_pair_id: str,
    inspect_name: str,
    metric: str = "stage2_ndcg_at_5",
    tie_eps: float = TIE_EPS,
    n_samples: int = 5,
) -> dict[str, Any]:
    base_by = {c["example_id"]: c for c in baseline if c.get("scored") and c.get("example_id")}
    chal_by = {c["example_id"]: c for c in challenger if c.get("scored") and c.get("example_id")}
    common = sorted(set(base_by) & set(chal_by))
    wins = losses = ties = 0
    deltas: list[tuple[str, float]] = []
    for eid in common:
        bv = base_by[eid].get(metric)
        cv = chal_by[eid].get(metric)
        if bv is None or cv is None:
            continue
        d = float(cv) - float(bv)
        deltas.append((eid, d))
        if abs(d) < tie_eps:
            ties += 1
        elif d >= tie_eps:
            wins += 1
        else:
            losses += 1
    deltas_sorted = sorted(deltas, key=lambda x: abs(x[1]), reverse=True)
    sample_wins = [
        {
            "example_id": eid,
            "delta": d,
            "href": f"{inspect_name}#pair-{challenger_pair_id}-ex-{eid}",
        }
        for eid, d in deltas_sorted
        if d >= tie_eps
    ][:n_samples]
    sample_losses = [
        {
            "example_id": eid,
            "delta": d,
            "href": f"{inspect_name}#pair-{challenger_pair_id}-ex-{eid}",
        }
        for eid, d in deltas_sorted
        if d <= -tie_eps
    ][:n_samples]
    return {
        "challenger_pair_id": challenger_pair_id,
        "baseline_pair_id": baseline_pair_id,
        "metric": metric,
        "tie_epsilon": tie_eps,
        "n_compared": wins + losses + ties,
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "sample_wins": sample_wins,
        "sample_losses": sample_losses,
    }
