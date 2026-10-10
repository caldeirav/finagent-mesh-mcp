# Quickstart: Paper P0 Evidence Pack

**Feature**: `004-paper-p0-evidence` | Validate after implementation (not a full paper GPU guide).

## Prerequisites

- Branch `004-paper-p0-evidence` with Spec 003 matrix stack already on `main`
- Local artifacts: `artifacts/matrix_runs/paper-n200-full.json` and ledger entries for its pairs (or regenerate inspect via `--inspect-from`)
- `.env` with `HF_TOKEN` for any new ranking rows; `GOOGLE_API_KEY` only for synthesis reuse
- `uv sync --extra real --group dev`

## 1. Rebuild analysis without engines (S0 / S3 / bootstrap)

```bash
uv run python scripts/run_benchmark.py --analysis-from paper-n200-full
```

**Expect**:
- `artifacts/benchmarks/paper-n200-full.analysis.md` includes **Routing accounting**, **pipeline yield**, dual S2 series (scored + pipeline), **MRR@5**, **Strata**, **Win/tie/loss**, **Uncertainty** (bootstrap CIs)
- Findings do **not** say empties are zeroed into the primary S2 series
- Exit 0; no GPU sidecars started

## 2. Unit checks (offline)

```bash
uv run pytest tests/unit/test_routing_classes.py \
  tests/unit/test_pipeline_yield_metrics.py \
  tests/unit/test_bootstrap_ci.py \
  tests/unit/test_win_loss_ndcg.py \
  tests/unit/test_strata_buckets.py \
  tests/unit/test_analysis_report.py -q
```

**Expect**: All pass; win rule uses ε=0.01 on nDCG@5.

## 3. Optional baselines smoke (S2) — small N first

```bash
uv run python scripts/run_benchmark.py --real --include-optional \
  --pairs lux-clm-shortlist,one-shot-ar \
  --records 5 --seed 42 --run-id paper-p0-opt-smoke5
```

**Expect**: Both pairs measured or skipped with explicit reason; analysis labels `one-shot-ar` as collapsed baseline; #1/#2 still deferred.

Paper acceptance uses N=200 seed=42 (see [evidence-cli.md](./contracts/evidence-cli.md)).

## 4. Multi-seed core subset (S4) — after smoke

```bash
uv run python scripts/run_benchmark.py --real \
  --pairs lux-lux,anyjev-l0-lux,lux-e5,lux-bm25 \
  --records 200 --seed 7 --run-id paper-n200-s7-core
# similarly seed 123 → paper-n200-s123-core
```

**Expect**: Independent example ids vs seed 42; rollup shows per-seed, mean-of-means, min–max for headline metrics.

## 5. Synthesis reuse (S1)

```bash
# Exact flag per evidence-cli.md once implemented
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --synthesis-from-rankings paper-n200-full \
  --pairs anyjev-l0-lux,lux-lux,lux-e5,lux-bm25 \
  --run-id paper-n200-full-synth
```

**Expect**:
- No Choice/Score sidecar load for examples that already have rankings (or documented equivalent)
- EM/F1 table for four pairs; skips counted for empty/missing evidence
- Ranking nDCG in analysis still matches published `paper-n200-full` for those pairs

## Pass / fail summary

| Gate | Pass condition |
|------|----------------|
| SC-001/002 | Routing table + dual S2 series + MRR visible |
| SC-003 | ≥10 win/loss inspect links on N=200 Block B |
| SC-004 | Bootstrap CIs for Δ(E5−Lux) and Δ(AnyJev−Lux) |
| SC-005 | Seeds 42/7/123 core subset + mean/min/max |
| SC-006 | Synthesis EM/F1 or quantified failures; rankings reused |
| SC-007 | Optional pairs measured or skipped-with-reason |
| SC-008 | `--analysis-from` without engines |

## References

- [spec.md](./spec.md) · [plan.md](./plan.md) · [research.md](./research.md) · [data-model.md](./data-model.md)
- Contracts: [analysis-report-p0.md](./contracts/analysis-report-p0.md), [evidence-cli.md](./contracts/evidence-cli.md), [routing-classes.md](./contracts/routing-classes.md)
