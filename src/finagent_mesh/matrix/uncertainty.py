"""Bootstrap CIs and multi-seed rollups for paper P0 evidence."""

from __future__ import annotations

import random
from typing import Any


def bootstrap_ci(
    values: list[float | None],
    *,
    n_resamples: int = 1000,
    seed: int = 42,
    alpha: float = 0.05,
) -> dict[str, float | None]:
    """Percentile bootstrap CI for the mean of non-null values.

    When building pipeline-averaged series, pass zeros for missing examples
    explicitly (do not leave None).
    """
    xs = [float(v) for v in values if v is not None]
    if not xs:
        return {"point": None, "ci_low": None, "ci_high": None, "n": 0, "n_resamples": n_resamples}
    point = sum(xs) / len(xs)
    rng = random.Random(seed)
    means: list[float] = []
    n = len(xs)
    for _ in range(n_resamples):
        sample = [xs[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo_i = int((alpha / 2.0) * (n_resamples - 1))
    hi_i = int((1.0 - alpha / 2.0) * (n_resamples - 1))
    return {
        "point": point,
        "ci_low": means[lo_i],
        "ci_high": means[hi_i],
        "n": n,
        "n_resamples": n_resamples,
    }


def bootstrap_delta_ci(
    a: list[float | None],
    b: list[float | None],
    *,
    n_resamples: int = 1000,
    seed: int = 42,
    alpha: float = 0.05,
) -> dict[str, float | None]:
    """Bootstrap CI for mean(a) - mean(b) using paired indices where both present.

    For independent samples (different example sets), falls back to unpaired
    bootstrap of each mean difference of resampled means.
    """
    paired_a: list[float] = []
    paired_b: list[float] = []
    for x, y in zip(a, b, strict=False):
        if x is not None and y is not None:
            paired_a.append(float(x))
            paired_b.append(float(y))
    if paired_a and len(paired_a) == len(a) == len(b):
        diffs = [x - y for x, y in zip(paired_a, paired_b, strict=True)]
        return bootstrap_ci(diffs, n_resamples=n_resamples, seed=seed, alpha=alpha)

    xs = [float(v) for v in a if v is not None]
    ys = [float(v) for v in b if v is not None]
    if not xs or not ys:
        return {"point": None, "ci_low": None, "ci_high": None, "n": 0, "n_resamples": n_resamples}
    point = (sum(xs) / len(xs)) - (sum(ys) / len(ys))
    rng = random.Random(seed)
    deltas: list[float] = []
    for _ in range(n_resamples):
        sx = [xs[rng.randrange(len(xs))] for _ in range(len(xs))]
        sy = [ys[rng.randrange(len(ys))] for _ in range(len(ys))]
        deltas.append(sum(sx) / len(sx) - sum(sy) / len(sy))
    deltas.sort()
    lo_i = int((alpha / 2.0) * (n_resamples - 1))
    hi_i = int((1.0 - alpha / 2.0) * (n_resamples - 1))
    return {
        "point": point,
        "ci_low": deltas[lo_i],
        "ci_high": deltas[hi_i],
        "n": min(len(xs), len(ys)),
        "n_resamples": n_resamples,
    }


def metric_series(contribs: list[dict[str, Any]], key: str, *, scored_only: bool) -> list[float | None]:
    out: list[float | None] = []
    for c in contribs:
        if scored_only and not c.get("scored"):
            out.append(None)
            continue
        if scored_only:
            out.append(c.get(key))
        else:
            # pipeline: missing → 0
            v = c.get(key)
            out.append(float(v) if v is not None else 0.0)
    return out


def multi_seed_rollup(
    per_seed: dict[int, float | None],
) -> dict[str, Any]:
    """per_seed: seed → metric; returns mean_of_means + min/max."""
    vals = {s: float(v) for s, v in per_seed.items() if v is not None}
    if not vals:
        return {
            "per_seed": dict(per_seed),
            "mean_of_means": None,
            "min": None,
            "max": None,
        }
    xs = list(vals.values())
    return {
        "per_seed": {str(k): per_seed.get(k) for k in sorted(per_seed)},
        "mean_of_means": sum(xs) / len(xs),
        "min": min(xs),
        "max": max(xs),
    }
