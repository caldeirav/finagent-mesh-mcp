# Contract: Yield-recovery matrix pairs

## Required for v1 acceptance (optional catalog)

| pair_id | Stage-1 | Stage-2 | yield_recovery | Notes |
|---------|---------|---------|----------------|-------|
| `lux-lux-yield` | Lux Choice (live) **or** documented frozen equivalent | Lux Score | true | Twin of `lux-lux` |
| `lux-unsloth-score-yield` | frozen Lux Choice | BM25 k=32 → Unsloth Score | true | Twin of `lux-unsloth-score` |

Both MUST run on paper N=200 seed-42 `selected_example_ids`.

## Catalog rules

- `optional: true` — not in default `--real` required set  
- `role: yield_recovery` (or equivalent) for analysis filtering  
- MUST NOT appear in published `paper-n200-full` regeneration without a new run id  

## Suggested run ids

| Path | Example run id |
|------|----------------|
| Lux twin | `yield-paper-n200-lux` |
| Unsloth twin | `yield-unsloth-score-paper-n200` |

Artifact writes: `artifacts/benchmarks/<run_id>.*`, `artifacts/matrix_runs/<run_id>.json` only under allowed stems (`yield-*` / `*-yield*`).

## Explicitly optional (not required to close #10)

- `lux-e5-yield`, `lux-bm25-yield`, `lux-lux-shortlist-yield`
