# Contract: Paper Matrix CLI Extensions

Extends [002 matrix CLI](../../002-decision-model-bench/contracts/matrix-cli.md) via `scripts/run_benchmark.py` (primary) and `scripts/run_matrix.py` (compat). Full operator docs: [README.md](../../../README.md).

## Invocation

```bash
uv run python scripts/run_benchmark.py [FLAGS]
```

## Complete flag reference

| Flag | Default | Behavior |
|------|---------|----------|
| `--real` | off | Production: real HF models; refuse mock; ranking-only unless `--with-synthesis`; default sample `min(200, dataset_n)`; force-restart sidecars unless `--keep-servers`; auto-fetch FinAgentBench unless `--no-fetch-data` |
| `--records` / `-n` | see `--real` | Seeded sample of N examples |
| `--seed` / `-s` | `42` | Sampling RNG seed |
| `--run-id` | UTC timestamp `bench-…` | Matrix run id (ledger + artifact stem) |
| `--pairs` / `-p` | all required Block A/B | Comma-separated pair ids; fail closed on missing engines |
| `--engines` / `-e` | — | Legacy ablation with fixed partners; **xor** with `--pairs` |
| `--include-optional` | off | Include `lux-clm-shortlist`, `one-shot-ar` |
| `--include-baseline` | off | Legacy; Block A already includes `ar-lux` |
| `--with-synthesis` | off | Enable Gemini Flash + answer scoring |
| `--skip-synthesis` | implied by `--real` | Explicit ranking-only |
| `--gemini-model` | env / `gemini-2.5-flash` | Override System-2 model |
| `--dataset-path` | `FINAGENTBENCH_PATH` | Dataset path |
| `--out-dir` | `artifacts/benchmarks` | Report directory |
| `--min-examples` | `100` | Minimum labeled examples under `--real` |
| `--fetch-data` / `--no-fetch-data` | fetch on | Kaggle download + convert if missing |
| `--force-restart` | on with `--real` | Kill sidecars / ports 8000–8002 before run |
| `--keep-servers` | off | Reuse running sidecars (disables force-restart) |
| `--no-manage-servers` | off | Do not start/stop engines |
| `--allow-mock` | off | Debug only; **illegal** with `--real` |
| `--list-pairs` | — | Print pairs (+ deferred) and exit |
| `--list-engines` | — | Print registry engines and exit |
| `--analysis-from <id>` | — | Rebuild analysis (+ inspect) from saved matrix; no engines |
| `--inspect-from <id>` | — | Rebuild inspect only; no engines |

### Behavior changes vs 002

| Mode | Behavior |
|------|----------|
| `--real` without `--records` | Seeded `min(200, dataset_n)`; refuse mock |
| `--real` synthesis | **Off by default**; use `--with-synthesis` |
| Default pairs | All `optional: false` catalog pairs (Block A+B); dedupe `lux-lux` |
| Post-run artifacts | json, csv, md (interpret), inspect html/json, **analysis md/json** |
| Observability | Nested MLflow Runs + Traces (`finagent_example`, `systemone_*`, `gemini_synthesize`) with Stage-1/2/Gemini outcome metrics |

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
- Gemini: no extractive fabrication if API key/API fails.

### GPU policy

Sequential exclusive heavy engines; keep `decision20-lux` warm across Block A rows that share it as Stage-2; keep Lux Choice warm across Block B when Stage-1 is Lux.
