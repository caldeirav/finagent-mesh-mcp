# Quickstart: Unsloth Score track (006)

ZGX Nano / DGX Spark. Does **not** replace `run_benchmark.py --real` paper matrix.

## Prerequisites

- FinAgentBench under `data/finagentbench`
- Published `artifacts/matrix_runs/paper-n200-full.json` (+ inspect/ledger for frozen Lux Top-1)
- Paper matrix BM25/E5: `uv sync --extra real`
- Unsloth fine-tune (entire stack via uv): `uv sync --extra real --extra unsloth`
  (or `bash scripts/install_unsloth_zgx.sh --with-real`). Declared in
  `pyproject.toml` `[project.optional-dependencies].unsloth`; uv overrides skip
  `xformers` and keep `transformers>=5.18`.
- GPU free of Lux sidecars during 27B train (`bash scripts/serve_engine.sh stop-all`)

## 1. Export + leakage check

```bash
uv run python scripts/export_unsloth_dataset.py \
  --dataset-path data/finagentbench \
  --paper-matrix artifacts/matrix_runs/paper-n200-full.json \
  --out-dir artifacts/unsloth/datasets/fab-paper-test-v1
```

Expect: `split_manifest.json` with `n_test=200`, `leakage_report.json` overlaps = 0.

## 2. Smoke train

```bash
uv run --extra unsloth python scripts/train_unsloth_score.py \
  --dataset-dir artifacts/unsloth/datasets/fab-paper-test-v1 \
  --max-train-rows 1000 \
  --base-model unsloth/Qwen3.8-27B-unsloth-bnb-4bit \
  --out-dir artifacts/unsloth/checkpoints/score-qwen38-smoke \
  --run-id unsloth-train-score-smoke
```

Expect: checkpoint dir + train config JSON; no writes under `artifacts/benchmarks/paper-*`.

## 3. Smoke eval (N=20)

```bash
uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/score-qwen38-smoke \
  --records 20 --seed 42 \
  --run-id unsloth-score-smoke20
```

Expect: `artifacts/benchmarks/unsloth-score-smoke20.analysis.md` with Trained decision track section and Δ vs published baselines.

## 4. Full paper-slice eval (N=200)

```bash
uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/<prod> \
  --records 200 --seed 42 \
  --run-id unsloth-score-paper-n200
```

## 5. Regression: paper artifacts untouched

```bash
sha256sum artifacts/benchmarks/paper-n200-full.json
# re-run export/train/eval smoke, then sha256sum again — MUST match
uv run python scripts/run_benchmark.py --analysis-from paper-n200-full
```

## Pass criteria

- Leakage test green
- Smoke train produces loadable checkpoint
- Smoke eval emits harness S2 metrics + comparison table
- Paper artifact checksums unchanged
