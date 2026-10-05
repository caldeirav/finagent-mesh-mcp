# Implementation Plan: Paper-Ready Choice/Score Matrix & Analysis Report

**Branch**: `003-choice-score-paper` | **Date**: 2026-10-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-choice-score-paper/spec.md` (clarified: optional Block B = shortlist dual-encoder + one-shot only; train/cross-encoder deferred as issues #1/#2; ranking-only default for N≥200; E5/GTE-class dense Stage-2).

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Rebind the FinAgentBench matrix from a CLM-partnered serving demo into a **paper ablation**: **Block A** (Stage-1 Choice varies; Lux Score fixed) and **Block B** (Stage-2 Score varies; Lux Choice fixed), plus optional shortlist-CLM and one-shot generative baselines. Extend metrics for routing vs scoring (Top-1 recall, conditional S2 nDCG, OFR, parse failures). Emit a **paper analysis report** that indexes every pair×example into existing inspect records. Default publishable runs are **ranking-only** (`--skip-synthesis`); synthesis remains opt-in. Reuse existing System-1 serving, harness, ledger, and inspect HTML—no new agent graph.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed `finagent-mesh-mcp`)

**Primary Dependencies**: Existing matrix/harness (`typer`, `httpx`, `torch`/`transformers`, Decision-2.0 / CLM / AnyJev / AR adapters); add in-process **BM25** (`rank_bm25` or equivalent) and **E5** bi-encoder (`sentence-transformers` + `intfloat/e5-base-v2`); Gemini only when synthesis opted in

**Storage**: Existing SQLite eval ledger + MLflow; matrix JSON/CSV/MD/inspect under `artifacts/benchmarks/`; new `*.analysis.md` (+ optional JSON) regenerated from saved run id

**Testing**: `pytest` unit tests for pair catalog/blocks, conditional metrics, BM25/E5 ranking adapters (mocked weights where needed), analysis report links; integration smoke with `--records 10 --skip-synthesis`

**Target Platform**: HP ZGX Nano / DGX Spark (Grace Blackwell ARM64); Podman + nvidia-container-toolkit; sequential exclusive GPU for heavy rows; BM25 CPU-only; E5 GPU or CPU

**Project Type**: Extension of existing evaluation harness + matrix CLI (not a new app)

**Performance Goals**: Paper default N≥200 seeded, ranking-only; analysis rebuild from saved run <5 minutes without engines; shared Lux Score warm across Block A where possible

**Constraints**: Constitution v1.1.0; `SYSTEMONE_MOCK=0` for official runs; fail-closed ranking/synthesis; no silent engine substitution; one-shot baseline labeled as collapsing two-stage contract; deferred train/CE not implemented

**Scale/Scope**: Required pairs ≈ Block A (5) + Block B (4) with `lux-lux` shared once → ~8 physical rows; optional +2 (`lux-clm-shortlist`, `one-shot-ar`); smoke N=10; paper N≥200

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | Unchanged MCP calculator path |
| II. Local System-1 First | PASS | Local Choice/Score/IR before optional Gemini |
| III. Local ARM64 Container Native | PASS | Existing Podman sidecars; BM25/E5 in-process or thin sidecar on ARM64 |
| IV. MCP Protocol Isolation | PASS | No new tool bypass |
| V. State Persistence & Auto-Resume | PASS | Ledger + matrix resume unchanged |
| VI. Trace Completeness | PASS | Extend ranking_payload / io_traces; MLflow engine ids |
| VII. Two-Stage Agentic Retrieval | PASS | All production pairs keep Stage 1→2; one-shot AR is an explicit **baseline** that collapses stages and MUST be labeled (exception recorded in research + contracts) |

**Post-design re-check**: PASS — contracts document one-shot as labeled baseline exception to VII; deferred CE/train stay out of scope; Complexity Tracking notes the intentional baseline exception.

## Project Structure

### Documentation (this feature)

```text
specs/003-choice-score-paper/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── matrix-pairs.yaml
│   ├── analysis-report.md
│   └── paper-cli.md
└── tasks.md             # /speckit-tasks (not this command)
```

### Source Code (repository root — extensions)

```text
configs/
└── engines.yaml                 # rewrite matrix_pairs + block engines: bm25-stage2, e5-base, clm-shortlist meta

src/finagent_mesh/
├── clients/engines/
│   ├── registry.py              # block/optional/deferred fields if needed
│   ├── bm25_score.py            # NEW in-process Stage-2 Score
│   ├── e5_score.py              # NEW E5 bi-encoder Stage-2 Score
│   ├── clm_shortlist.py         # NEW BM25 top-32 → CLM Score
│   └── ar_baseline.py           # extend: one-shot chunk ranking mode
├── matrix/
│   ├── partners.py              # block membership, dedupe lux-lux, include_optional
│   ├── models.py                # reviewer metrics fields
│   ├── metrics.py               # NEW: Top-1 recall, conditional S2, OFR helpers
│   ├── analysis.py              # NEW: paper analysis.md (+ index into inspect)
│   ├── inspect.py               # anchor ids stable for analysis links
│   ├── interpret.py             # align findings with Block A/B (no S2 bake-off on Block A)
│   └── runner.py                # default skip_synthesis for --real paper; --with-synthesis
├── scoring/
│   └── run_aggregator.py        # persist per-example flags for conditional metrics
└── runtime/harness.py           # one-shot pair path; OFR hooks for AnyJev L0

scripts/
└── run_benchmark.py             # --analysis-from; --with-synthesis; default paper N hint; --include-optional

tests/
├── unit/test_matrix_blocks.py
├── unit/test_paper_metrics.py
├── unit/test_bm25_e5_adapters.py
├── unit/test_analysis_report.py
└── integration/test_paper_matrix_smoke.py
```

**Structure Decision**: Extend the existing single-package matrix stack. Classical IR (BM25, E5) runs as **in-process Stage-2 adapters** behind the same OpenDecision Score primitive so the harness graph stays unchanged. One-shot AR is a special pair that bypasses Stage-1 type filter and is labeled `role: baseline_collapsed`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| One-shot AR collapses Stage 1+2 (Principle VII) | Paper needs a stuffing baseline to motivate typed Choice→Score | Skipping the baseline weakens the systems claim; exception is labeled and opt-in only |
