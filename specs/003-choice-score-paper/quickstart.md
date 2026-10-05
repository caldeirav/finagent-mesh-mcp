# Quickstart: Paper Choice/Score Matrix

Validate Block A/B matrix + analysis report without claiming a full paper run.

## Prerequisites

```bash
./scripts/prepare_real_stack.sh
# .env: SYSTEMONE_MOCK=0, SYSTEMONE_BACKEND=real, HF_TOKEN=… (Hub rate limits),
#       weights for Lux/Kai/Laya/CLM/E5/AR
# Kaggle creds only if FinAgentBench not already under data/finagentbench/
```

See [matrix-pairs contract](./contracts/matrix-pairs.yaml) and [paper CLI](./contracts/paper-cli.md).

## 1. List catalog

```bash
uv run python scripts/run_benchmark.py --list-pairs
```

**Expect**: Required Block A/B ids (`lux-lux`, `anyjev-l0-lux`, `kai-lux`, `laya-lux`, `ar-lux`, `lux-clm`, `lux-bm25`, `lux-e5`); optional `lux-clm-shortlist`, `one-shot-ar`; deferred noted or absent from runnable list.

## 2. Smoke (ranking-only)

```bash
uv run python scripts/run_benchmark.py --real \
  --records 10 --seed 42 \
  --run-id paper-smoke-10 \
  --skip-synthesis
```

**Expect**:
- No Gemini calls
- Artifacts under `artifacts/benchmarks/paper-smoke-10.*` including `.analysis.md` and `.inspect.html`
- Block A rows share Stage-2 engine `decision20-lux` (warm on :8001 while Choice engines swap on :8000)
- Block B rows (except any skipped) share Stage-1 `decision20-lux`
- Lux Stage-2 Score completes without `invalid_question` (ordinal relevance rubric, not chunk-list criteria)
- Analysis findings do not claim different S2 models on Block A

## 3. Optional pairs smoke

```bash
uv run python scripts/run_benchmark.py --real \
  --records 5 --seed 42 \
  --include-optional \
  --pairs lux-clm-shortlist,one-shot-ar \
  --run-id paper-opt-smoke \
  --skip-synthesis
```

**Expect**: Shortlist pair completes or fails closed with records; one-shot labeled collapsed; analysis SkipRecord empty for these ids.

## 4. Rebuild analysis (no engines)

```bash
bash scripts/serve_engine.sh stop-all   # optional
uv run python scripts/run_benchmark.py --analysis-from paper-smoke-10
```

**Expect**: Regenerated `.analysis.md` / `.analysis.json` in <5 minutes; inspect links resolve to `#pair-…-ex-…` anchors.

## 5. Paper-sized run (when ready)

```bash
uv run python scripts/run_benchmark.py --real \
  --seed 42 \
  --run-id paper-n200 \
  --skip-synthesis
# default N = min(200, dataset size)
```

**Expect**: Report header shows N≥200 (or full set if smaller), seed 42, synthesis not run.

## 6. Unit checks

```bash
uv run pytest tests/unit/test_matrix_blocks.py \
  tests/unit/test_paper_metrics.py \
  tests/unit/test_analysis_report.py -q
```

## Out of scope here

- Trained CLM heads → [issue #1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1)
- Cross-encoder ceiling → [issue #2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)
