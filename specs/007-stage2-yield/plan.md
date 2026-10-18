# Implementation Plan: Stage-2 Yield Recovery (Empty Top-1 Pools)

**Branch**: `007-stage2-yield` | **Date**: 2026-10-18 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/007-stage2-yield/spec.md` (GitHub [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10)): opt-in ordered Choice type fallback when Top-1 has no chunks; dual empty/yield and dual conditional metrics; acceptance on Lux Score twin **and** tuned Unsloth Score path; never overwrite published baselines.

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Add **opt-in yield recovery** inside the two-stage agent: when Stage-1 Choice Top-1 has an empty type-filtered chunk pool, walk the **full Choice ranking** and use the **first non-empty** type for Stage-2 (no gold peek). Default matrix behavior stays unchanged. Ship optional pairs / run ids for (1) Lux Score twin and (2) `lux-unsloth-score`-style path; extend metrics and analysis with **original Top-1 empty** vs **post-recovery empty/yield**, plus **conditional-on-Choice-Top-1** vs **conditional-on-effective-type**. Fail closed if all types empty. Ledger resume and paper artifact immutability preserved.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed `finagent-mesh-mcp`)

**Primary Dependencies**: Existing LangGraph agent (`stage1` / `stage2`), harness ledger, matrix metrics/analysis/inspect, `configs/engines.yaml`, frozen Lux Choice + Unsloth eval path from 006; no new ML training deps

**Storage**: New eval artifacts under `artifacts/benchmarks/yield-*` (and/or pair-prefixed run ids); read-only baselines `paper-n200-full*`, `unsloth-score-paper-n200*`; SQLite `eval_ledger.db` unchanged schema preferred (payload JSON carries recovery fields)

**Testing**: pytest unit tests for type-fallback selection, dual metrics aggregation, analysis Δ tables, artifact path guards; smoke ranking-only N≤20 optional on GPU

**Target Platform**: ZGX Nano / DGX Spark (same as existing `--real` / Unsloth eval)

**Project Type**: Agent + matrix/eval extension (optional pairs + metrics); default `--real` pairs unchanged

**Performance Goals**: Recovery adds only cheap chunk-pool checks until first non-empty type; Stage-2 cost dominated by existing Score engines (Lux / Unsloth). Full N=200 acceptance runs within current sequential GPU budget.

**Constraints**: Constitution VII (two-stage retrieval); FR immutability of published paper/unsloth baselines; recovery off by default; no gold-informed fallback; ranking-only for v1 acceptance

**Scale/Scope**: Paper N=200 seed-42 holdout; two required acceptance paths (Lux Score twin + Unsloth Score); optional IR extras out of scope for close

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | No calculator / LLM math |
| II. Local System-1 First | PASS | Recovery stays in Choice→Score control plane; ranking-only default |
| III. Local ARM64 Container Native | PASS | No new container story; reuse existing engines |
| IV. MCP Protocol Isolation | PASS | No new tool bypass |
| V. State Persistence & Auto-Resume | PASS | Same ledger; recovery fields in ranking payload; resume skips completed |
| VI. Trace Completeness | PASS | Record original Top-1, effective type, fallback flag in ranking/inspect/MLflow tags |
| VII. Two-Stage Agentic Retrieval | PASS | Still Choice then Score; fallback only changes which type filters Stage-2 candidates |

**Post-design re-check**: PASS — recovery is Stage-2 pool selection using Stage-1 ordered ids; does not collapse stages or invent passages. Complexity Tracking empty.

## Project Structure

### Documentation (this feature)

```text
specs/007-stage2-yield/
├── plan.md              # this file
├── research.md          # Phase 0
├── data-model.md        # Phase 1
├── quickstart.md        # Phase 1
├── contracts/
│   ├── yield-recovery-runtime.md
│   ├── matrix-pairs-yield.md
│   ├── metrics-dual-reporting.md
│   └── analysis-report-yield.md
└── tasks.md             # /speckit-tasks (not this command)
```

### Source Code (repository root — extensions)

```text
configs/engines.yaml                 # optional pairs lux-lux-yield, lux-unsloth-score-yield (+ flags)
src/finagent_mesh/
├── agent/
│   ├── state.py                     # original/effective type + recovery audit fields
│   ├── nodes/stage2.py              # ordered fallback when Top-1 pool empty (gated)
│   └── graph.py                     # pass recovery flag / persist fields in ranking dump
├── runtime/harness.py               # ranking payload: recovery + dual top1 fields
├── matrix/
│   ├── metrics.py                   # original vs post-recovery empty/yield; dual conditional
│   ├── analysis.py                  # Yield recovery section + Δ vs baselines
│   ├── models.py                    # optional metric fields
│   └── partners.py / ports.py       # pair wiring if needed
├── unsloth/
│   ├── paths.py                     # allow yield-* / *-yield run ids; keep paper immutable
│   └── frozen_stage1.py             # ensure full ordered_ids available for fallback
scripts/
├── run_benchmark.py                 # --pairs lux-lux-yield (existing entry)
└── run_unsloth_eval.py              # --yield-recovery / pair lux-unsloth-score-yield
tests/unit/
├── test_yield_recovery_stage2.py
├── test_yield_dual_metrics.py
└── test_yield_analysis.py
```

**Structure Decision**: Implement recovery in `run_stage2` (single choke point for type→chunk filter) behind a run/pair flag, rather than a new LangGraph node. Metrics layer distinguishes original Top-1 emptiness (Choice Top-1 pool empty) from post-recovery emptiness (no type in ranking had chunks). Analysis mirrors 006’s “trained track” pattern with a **Yield recovery** section and read-only baseline Δ.

## Complexity Tracking

> No constitution violations requiring justification.
