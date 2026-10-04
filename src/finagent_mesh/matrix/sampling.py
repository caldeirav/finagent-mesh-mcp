"""Seeded FinAgentBench example sampling."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class SampleSelection:
    sample_seed: int | None
    sample_size: int | None
    selected_example_ids: list[str]
    capped: bool


def select_example_ids(
    example_ids: list[str],
    *,
    sample_size: int | None,
    sample_seed: int | None,
) -> SampleSelection:
    """Select example IDs; reproducible for (seed, size, id order). Caps to dataset size."""
    ids = list(example_ids)
    if sample_size is None:
        return SampleSelection(
            sample_seed=sample_seed,
            sample_size=None,
            selected_example_ids=ids,
            capped=False,
        )
    if sample_size <= 0:
        raise ValueError("sample_size must be positive when provided")
    capped = sample_size > len(ids)
    n = min(sample_size, len(ids))
    if sample_seed is None:
        chosen = ids[:n] if capped else random.sample(ids, n)
    else:
        rng = random.Random(sample_seed)
        chosen = rng.sample(ids, n)
    return SampleSelection(
        sample_seed=sample_seed,
        sample_size=sample_size,
        selected_example_ids=chosen,
        capped=capped,
    )
