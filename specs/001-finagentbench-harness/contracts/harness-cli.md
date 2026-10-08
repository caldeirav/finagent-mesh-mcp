# Harness CLI & Environment Contract

Entrypoint: `scripts/run_harness.py` (invoked via `uv run python scripts/run_harness.py ...`).

## Commands

### `run`

Start or resume an evaluation run.

```bash
uv run python scripts/run_harness.py run \
  --run-id <id> \
  [--limit N] \
  [--dataset-path PATH] \
  [--synthesis-k 5] \
  [--skip-synthesis]
```

**Behavior**:
1. Acquire ledger lease for `run_id` or exit with conflict.
2. Health-check System-1 at `SYSTEMONE_STAGE1_URL` and `SYSTEMONE_STAGE2_URL`.
3. Iterate ledger: skip `completed` / `ranking_complete` (for ranking), resume `synthesis_retriable` at synthesis, process `pending` / `failed_retriable` / incomplete.
4. Emit MLflow traces; write Stage-1/2 metrics and answer scores.

### `export-metrics`

```bash
uv run python scripts/run_harness.py export-metrics --run-id <id> [--out PATH]
```

Exports aggregate nDCG@5 / MAP@5 / MRR@5 (Stage 1 & 2) and answer normalized-EM / token-F1 summaries.

### `status`

```bash
uv run python scripts/run_harness.py status --run-id <id>
```

Prints ledger state counts and lease info.

## Environment variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `FINAGENTBENCH_PATH` | _(required)_ | Dataset root |
| `EVAL_LEDGER_PATH` | `./eval_ledger.db` | SQLite ledger path |
| `SYSTEMONE_STAGE1_URL` | `http://localhost:8000` | Stage 1 Choice base URL |
| `SYSTEMONE_STAGE2_URL` | `http://localhost:8001` | Stage 2 Score base URL |
| `AGENT_GATEWAY_URL` | _(required)_ | Gateway base for MCP + mediated calls |
| `GOOGLE_API_KEY` | _(required for synthesis)_ | Google AI Studio key |
| `GEMINI_MODEL` | `gemini-2.5-flash` | System-2 model id |
| `SYNTHESIS_K` | `5` | Top-K chunks to synthesize |
| `HARNESS_MAX_ATTEMPTS` | `3` | Total attempts per failing stage |
| `MLFLOW_TRACKING_URI` | `sqlite:///mlflow.db` | MLflow tracking URI (SQLite; prefer over FileStore `./mlruns`) |
| `PODMAN_OR_DOCKER` | `podman` | Runtime preference for build script |

See also: [systemone-openapi.yaml](./systemone-openapi.yaml), [mcp-sec-edgar.json](./mcp-sec-edgar.json), [mcp-financial-calculator.json](./mcp-financial-calculator.json).
