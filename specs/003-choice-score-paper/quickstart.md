# Quickstart: Paper Choice/Score Matrix

Operator path to validate Block A/B + MLflow + (optional) Gemini. Canonical flag docs: [paper-cli.md](./contracts/paper-cli.md) and [README.md](../../README.md).

## Prerequisites

```bash
./scripts/prepare_real_stack.sh
# .env: SYSTEMONE_MOCK=0, SYSTEMONE_BACKEND=real, HF_TOKEN=…,
#       MLFLOW_TRACKING_URI=sqlite:///mlflow.db
# GOOGLE_API_KEY only for --with-synthesis
# Kaggle creds only if FinAgentBench not already under data/finagentbench/
uv sync --extra real --group dev
```

## 1. List catalog

```bash
uv run python scripts/run_benchmark.py --list-pairs
```

**Expect**: Required Block A/B ids (`lux-lux`, `anyjev-l0-lux`, `kai-lux`, `laya-lux`, `ar-lux`, `lux-clm`, `lux-bm25`, `lux-e5`); optional `lux-clm-shortlist`, `one-shot-ar`; deferred listed separately.

## 2. Technical smoke (Gemini + MLflow) — preferred first check

Use a **new** `--run-id`. Open MLflow in another terminal:

```bash
./scripts/mlflow_ui.sh
```

```bash
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --pairs lux-lux \
  --records 5 --seed 42 \
  --run-id paper-smoke-mlflow-gemini-5
```

**Expect**:
- Artifacts under `artifacts/benchmarks/paper-smoke-mlflow-gemini-5.*`
- Non-empty Gemini synthesis when ranking succeeds
- MLflow **Runs**: `stage1_*`, `stage2_*`, `gemini_synthesis_ok`, `gemini_answer_*`
- MLflow **Traces**: `finagent_example` → LangGraph nodes → `systemone_*` → `gemini_synthesize`

## 3. Ranking-only Block A/B smoke

```bash
uv run python scripts/run_benchmark.py --real \
  --records 10 --seed 42 \
  --run-id paper-smoke-10
```

(`--real` already implies ranking-only; `--skip-synthesis` is optional/explicit.)

**Expect**:
- No Gemini calls
- `.analysis.md` + `.inspect.html`
- Block A shares Lux Score on :8001 while Choice engines swap on :8000
- Lux Stage-2 ordinal Score completes without `invalid_question`

## 4. Optional pairs smoke

```bash
uv run python scripts/run_benchmark.py --real \
  --records 5 --seed 42 \
  --include-optional \
  --pairs lux-clm-shortlist,one-shot-ar \
  --run-id paper-opt-smoke
```

**Expect**: Shortlist completes or fails closed with records; one-shot labeled collapsed; analysis SkipRecord empty for these ids when healthy.

## 5. Rebuild analysis (no engines)

```bash
bash scripts/serve_engine.sh stop-all   # optional
uv run python scripts/run_benchmark.py --analysis-from paper-smoke-10
uv run python scripts/run_benchmark.py --inspect-from paper-smoke-10
```

**Expect**: Regenerated analysis/inspect artifacts; inspect links resolve to `#pair-…-ex-…` anchors.

## 6. Paper-sized run

```bash
uv run python scripts/run_benchmark.py --real \
  --seed 42 \
  --run-id paper-n200
# default N = min(200, dataset size); ranking-only
```

With synthesis:

```bash
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --seed 42 --run-id paper-n200-synth
```

## 7. Unit checks

```bash
uv run pytest tests/unit/test_matrix_pairs.py \
  tests/unit/test_paper_metrics.py \
  tests/unit/test_analysis_report.py \
  tests/unit/test_tracing_outcomes.py -q
```

## Out of scope here

- Trained CLM heads → [issue #1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1)
- Cross-encoder ceiling → [issue #2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)
