# Implementation Plan: Paper P0 Evidence Pack

**Branch**: `004-paper-p0-evidence` | **Date**: 2026-10-09 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-paper-p0-evidence/spec.md` (clarified: pipeline-averaged secondary S2; synthesis reuses rankings; win by nDCG@5 with |Δ|<0.01 tie; independent multi-seed samples; across-seed mean+min–max).

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Harden paper evidence around `paper-n200-full` without changing Spec 003’s required Block A/B pair identities. Deliver: (S0) routing accounting + pipeline yield + scored-only vs **pipeline-averaged** Stage-2 series + MRR@5 in tables; (S3) stratified Block B comparisons and nDCG@5 win/tie/loss vs Lux; (S4) bootstrap 95% CIs on seed-42 plus independent three-seed core-subset protocol with mean-of-means and min–max; (S1) Gemini synthesis **reuse** of saved rankings for four pairs; (S2) measure optional `lux-clm-shortlist` and `one-shot-ar`. Deferred [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1)/[#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) stay out of scope. Prefer analysis rebuilds from ledger/inspect; new GPU work only for seeds 7/123 core subset, optional pairs, and synthesis-only resume.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed `finagent-mesh-mcp`)

**Primary Dependencies**: Existing matrix/analysis/inspect/harness (`typer`, SQLite ledger, MLflow); stdlib/`statistics` or lightweight bootstrap (no new heavy deps); Gemini only on synthesis-reuse path

**Storage**: Existing SQLite eval ledger + matrix JSON under `artifacts/matrix_runs/` and `artifacts/benchmarks/`; extended `*.analysis.md` / `*.analysis.json`; optional multi-seed summary artifact

**Testing**: `pytest` for routing classes, pipeline-averaged math, bootstrap CI smoke, win/tie/loss rule, strata bucketing; analysis rebuild tests without engines; optional CLI smoke docs in quickstart

**Target Platform**: HP ZGX Nano / DGX Spark (Grace Blackwell ARM64); sequential exclusive GPU for new ranking rows; synthesis reuse is API-bound (Gemini), not GPU Stage-1/2

**Project Type**: Extension of existing evaluation harness + analysis CLI (not a new app)

**Performance Goals**: Analysis/CI/strata rebuild from saved run <5 minutes for N≤200 × ≤12 pairs; bootstrap ≥1000 resamples on per-example contributions; multi-seed core subset = 4 pairs × 2 new seeds (seed 42 already published)

**Constraints**: Constitution v1.1.0; fail-closed synthesis; no fabricated extractive answers; no Choice/Score re-inference on synthesis path; primary S2 remains scored-only; issues #1/#2 deferred; do not redefine required pair ids

**Scale/Scope**: Reference `paper-n200-full` (N=200, seed=42); core multi-seed pairs `{lux-lux, anyjev-l0-lux, lux-e5, lux-bm25}` × seeds `{42,7,123}`; synthesis four pairs seed 42; optional two catalog pairs seed 42

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | Unchanged MCP calculator path; answer EM/F1 from labeled spans only |
| II. Local System-1 First | PASS | Ranking rows still local System-1; Gemini only after saved System-1 rankings exist (reuse) |
| III. Local ARM64 Container Native | PASS | Existing Podman sidecars for any new ranking rows |
| IV. MCP Protocol Isolation | PASS | No new tool bypass |
| V. State Persistence & Auto-Resume | PASS | Synthesis reuse via ledger ranking payloads / `synthesis_retriable` resume pattern |
| VI. Trace Completeness | PASS | Synthesis I/O + answer scores recorded; ranking traces preserved from prior runs |
| VII. Two-Stage Agentic Retrieval | PASS | Production pairs unchanged; `one-shot-ar` remains labeled collapsed baseline (003 exception) |

**Post-design re-check**: PASS — contracts extend analysis report without collapsing stages for production pairs; synthesis reuse attaches System-2 to existing Stage-1/2 traces; Complexity Tracking empty (no new principle exceptions).

## Project Structure

### Documentation (this feature)

```text
specs/004-paper-p0-evidence/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── analysis-report-p0.md
│   ├── evidence-cli.md
│   └── routing-classes.md
└── tasks.md             # /speckit-tasks (not this command)
```

### Source Code (repository root — extensions)

```text
src/finagent_mesh/matrix/
├── metrics.py                 # pipeline yield; pipeline-averaged S2; routing class counts
├── analysis.py                # sections: routing accounting, strata, win/loss, CIs, multi-seed, answers
├── uncertainty.py             # NEW: bootstrap CIs; Δ vs Lux; multi-seed mean/min/max rollup
├── strata.py                  # NEW: bucket helpers + Block B strata + win/loss vs Lux
├── merge.py                   # existing; may help multi-run rollups
├── inspect.py                 # ensure anchors for win/loss samples
└── runner.py / partners.py    # optional: core-subset pair list helper for multi-seed

src/finagent_mesh/runtime/
└── harness.py                 # synthesis-only resume already partially present; harden CLI path

scripts/
└── run_benchmark.py           # flags: --analysis-from enhancements; synthesis-from-rankings;
                               #        --pairs + seeds for core multi-seed; --include-optional

tests/
├── unit/test_pipeline_yield_metrics.py
├── unit/test_routing_classes.py
├── unit/test_bootstrap_ci.py
├── unit/test_win_loss_ndcg.py
├── unit/test_strata_buckets.py
└── unit/test_analysis_report.py   # extend for P0 sections
```

**Structure Decision**: Keep a single-package extension. Put pure math (bootstrap, strata, routing classes) in small matrix modules callable from `analysis.py` and from `--analysis-from` rebuilds. Prefer ledger/inspect as the source of per-example contributions rather than re-deriving from aggregates alone.

## Complexity Tracking

> No constitution violations requiring justification for this feature.
