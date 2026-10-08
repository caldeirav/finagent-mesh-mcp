# Matrix & Pipeline CLI Contract

Entrypoints (via `uv run python …`):

- **`scripts/run_benchmark.py`** — **preferred** paper Block A/B matrix (`--real`); full flags in [003 paper-cli](../../003-choice-score-paper/contracts/paper-cli.md) and [README](../../../README.md)
- `scripts/run_matrix.py` — sequential engine matrix (legacy / ablation-oriented)
- `scripts/run_harness.py` — single pipeline run (extended bindings)
- `scripts/serve_engine.sh` — start/stop/health one registry config

Extends [001 harness CLI](../../001-finagentbench-harness/contracts/harness-cli.md).

## `serve_engine.sh`

```bash
./scripts/serve_engine.sh start <config_id>
./scripts/serve_engine.sh stop <config_id>
./scripts/serve_engine.sh health <config_id>
```

**Behavior**:
1. Resolve `config_id` from `configs/engines.yaml`.
2. For `anyjev-l1`, refuse start if calibration file missing or ≠200 IDs.
3. `health` curls `{base_url}{health_path}` and exits non-zero on failure.
4. Emit engine id + model_revision on success.

## `run_harness.py run` (extensions)

```bash
uv run python scripts/run_harness.py run \
  --run-id <id> \
  --stage1-engine <config_id> \
  --stage2-engine <config_id> \
  [--sample-size N] [--sample-seed S] \
  [--gemini-model gemini-2.5-flash] \
  [--skip-synthesis] \
  [--allow-mock]
```

**Behavior**:
1. Refuse official start if `SYSTEMONE_MOCK` truthy unless `--allow-mock` (recorded in config).
2. Health-check both bound engines; fail closed if unhealthy.
3. Bind OpenDecision clients per stage; one LangGraph execution per example (Stage 1→2→Gemini).
4. Default Gemini model `gemini-2.5-flash`; no extractive fallback.
5. Seeded sample: persist `sample_seed`, `sample_size`, `selected_example_ids`.

## `run_matrix.py`

### `run`

```bash
uv run python scripts/run_matrix.py run \
  --matrix-run-id <id> \
  [--engines anyjev-l0,anyjev-l1,clm-8b,...] \
  [--sample-size 50] [--sample-seed 42] \
  [--gemini-model gemini-2.5-flash] \
  [--skip-synthesis] \
  [--allow-mock]
```

**Behavior**:
1. Default `--engines` = all seven registry configs.
2. Refuse if mock enabled without `--allow-mock`.
3. Draw sample once; reuse same example IDs for every matrix row.
4. For each variable engine V sequentially:
   - stop previous variable engine (keep partner warm when possible)
   - start V; ensure fixed partner running
   - health-check V + partner
   - bind stages per [data-model](../data-model.md) matrix rules
   - run full pipeline (synthesis on by default)
   - export row metrics; mark row completed/failed
5. At most one variable heavy engine under test at a time (SC-009).

### `export`

```bash
uv run python scripts/run_matrix.py export \
  --matrix-run-id <id> \
  [--out PATH] \
  [--format json|csv]
```

Produces comparative report per [matrix-report.schema.json](./matrix-report.schema.json).

### `status`

```bash
uv run python scripts/run_matrix.py status --matrix-run-id <id>
```

## Environment variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `SYSTEMONE_MOCK` | `0` | Must be falsy for official claims |
| `ENGINES_REGISTRY_PATH` | `./configs/engines.yaml` | Registry path |
| `GEMINI_MODEL` | `gemini-2.5-flash` | System-2 default (Flash) |
| `GOOGLE_API_KEY` | _(required for synthesis)_ | Fail closed if missing when synthesis on |
| `FINAGENTBENCH_PATH` | _(required)_ | Dataset root |
| `EVAL_LEDGER_PATH` | `./eval_ledger.db` | Ledger |
| `MLFLOW_TRACKING_URI` | `sqlite:///mlflow.db` | Runs + Traces (use `./scripts/mlflow_ui.sh`) |
| `ANYJEV_WEIGHTS` / `CLM8B_WEIGHTS` / … | _(operator)_ | Weights paths from registry |

See also: [engines-registry.yaml](./engines-registry.yaml), [systemone-adapters.md](./systemone-adapters.md).
