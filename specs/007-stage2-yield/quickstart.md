# Quickstart: Stage-2 Yield Recovery (007)

ZGX Nano / DGX Spark. Does **not** replace or rewrite published `paper-n200-full` / `unsloth-score-paper-n200` artifacts.

## Prerequisites

- FinAgentBench under `data/finagentbench`
- Published baselines present: `artifacts/matrix_runs/paper-n200-full.json`, `artifacts/benchmarks/paper-n200-full.analysis.md`
- For Unsloth twin: checkpoint `artifacts/unsloth/checkpoints/score-qwen38-r16` and `uv sync --extra real --extra unsloth`
- Paper twin: `uv sync --extra real` + Lux engines as for normal `--real` matrix

## 1. Unit checks (no GPU)

```bash
uv run pytest tests/unit/test_yield_recovery_stage2.py \
  tests/unit/test_yield_dual_metrics.py \
  tests/unit/test_yield_analysis.py -q
```

Expect: first-non-empty selection, dual empty rates, analysis section keys, immutable path guards.

## 2. Smoke — Lux twin (N=20)

```bash
bash scripts/serve_engine.sh stop-all   # if needed for Lux sidecars

uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-lux-yield \
  --records 20 --seed 42 \
  --run-id yield-paper-n20-lux-smoke
```

Expect: `artifacts/benchmarks/yield-paper-n20-lux-smoke.analysis.md` with Yield recovery section; some `yield_recovery_used` if empties exist in the 20-id prefix; `paper-n200-full.json` checksum unchanged.

## 3. Full acceptance — Lux twin (N=200)

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-lux-yield \
  --records 200 --seed 42 \
  --run-id yield-paper-n200-lux
```

Expect: post-recovery empty ↓ vs published ~40.5% **or** documented corpus-limited remainder; fallback rate reported; dual conditional columns.

## 4. Full acceptance — Unsloth twin (N=200)

```bash
bash scripts/serve_engine.sh stop-all

uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score-yield \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/score-qwen38-r16 \
  --records 200 --seed 42 \
  --yield-recovery \
  --run-id yield-unsloth-score-paper-n200
```

Expect: artifacts under `yield-unsloth-score-paper-n200.*` only; Δ vs `unsloth-score-paper-n200` post-recovery yield/pipeline; no writes to `unsloth-score-paper-n200*`.

## 5. Regression: baselines untouched

```bash
sha256sum artifacts/benchmarks/paper-n200-full.json \
          artifacts/benchmarks/unsloth-score-paper-n200.json
# re-run smoke, sha256sum again — MUST match
```

## Pass criteria (v1)

- Default pairs without `yield_recovery` unchanged  
- Dual empty + dual conditional present on recovery analyses  
- Both Lux and Unsloth acceptance runs completed (or tracked blockers documented)  
- Baseline checksums unchanged  
