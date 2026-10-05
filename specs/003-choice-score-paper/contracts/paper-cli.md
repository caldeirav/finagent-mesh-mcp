# Contract: Paper Matrix CLI Extensions

Extends [002 matrix CLI](../../002-decision-model-bench/contracts/matrix-cli.md) via `scripts/run_benchmark.py` (primary) and `scripts/run_matrix.py` (compat).

## `run_benchmark.py` (paper defaults)

```bash
uv run python scripts/run_benchmark.py --real \
  [--run-id <id>] \
  [--records N | default 200] \
  [--seed S] \
  [--with-synthesis] \
  [--include-optional] \
  [--pairs id1,id2] \
  [--skip-synthesis] \
  [--analysis-from <run-id>] \
  [--inspect-from <run-id>]
```

### Behavior changes vs 002

| Flag / mode | Behavior |
|-------------|----------|
| `--real` without `--records` | Seeded sample `min(200, dataset_n)`; refuse mock |
| `--real` synthesis | **Off by default** (`skip_synthesis=true`) |
| `--with-synthesis` | Enable Gemini + answer scoring (fail-closed) |
| `--skip-synthesis` | Explicit ranking-only (default under `--real`) |
| Default pairs | All `optional: false` catalog pairs (Block A+B); dedupe `lux-lux` |
| `--include-optional` | Add `lux-clm-shortlist`, `one-shot-ar` |
| `--include-baseline` | Legacy; `ar-lux` is already required in Block A — flag may no-op or only affect extra baselines |
| `--pairs` | Explicit subset; still fail closed on missing engines |
| Post-run artifacts | json, csv, md (interpret), inspect html/json, **analysis md/json** |
| `--analysis-from` | Rebuild analysis only (no engines) |
| `--inspect-from` | Rebuild inspect only (existing) |
| `--list-pairs` | Show pair_id, blocks, optional, deferred |

### One-shot pair

When `one-shot-ar` is selected:

1. Do not run Stage-1 Choice.
2. Rank (or attempt to rank) chunks with AR JSON; record parse/coverage failures.
3. Set `collapsed_stages=true` in ranking_payload and pair metrics.
4. Stage-1 metrics reported as null / N/A.

### Fail-closed

- No mock rankings when `--real`.
- No silent substitution of BM25/E5/CLM/Lux.
- Missing optional weights → skip with SkipRecord, not crash of whole matrix (required pairs still fail the run if unhealthy).

### GPU policy

Sequential exclusive heavy engines; keep `decision20-lux` warm across Block A rows that share it as Stage-2; keep Lux Choice warm across Block B when Stage-1 is Lux.
