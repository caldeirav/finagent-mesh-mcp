# Implementation Plan: Unsloth Decision-Model Training Track

**Branch**: `006-unsloth-decision-track` | **Date**: 2026-10-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/006-unsloth-decision-track/spec.md` (GitHub [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5)): parallel Qwen3.8 FastDecisionModel Score train + isolated `lux-unsloth-score` eval comparable to published paper matrix.

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Deliver a **parallel** Unsloth decision-Score track that never mutates published `paper-n200-full*` / `paper-p1-ceilings-n200*` artifacts: (1) export FinAgentBench Score rows with **gold-type** pools and a leakage-safe split (**test = paper 200 ids**); (2) supervised QLoRA train of **`unsloth/Qwen3.8-27B-unsloth-bnb-4bit`** via `FastDecisionModel` / `DecisionTrainer` in an isolated optional extra; (3) serve trained Score as a new engine family; (4) eval pair **`lux-unsloth-score`** = frozen Lux Choice from `paper-n200-full` + **BM25 k=32** + trained Score; (5) analysis section with read-only Δ vs `lux-lux`, `lux-lux-shortlist`, `lux-e5`. Choice training deferred past v1.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed `finagent-mesh-mcp`)

**Primary Dependencies**: Existing harness/matrix/ledger/MLflow; `rank-bm25` (already in `--extra real`); **new optional** `[project.optional-dependencies] unsloth` (or dedicated env) with Unsloth + Transformers v5 (`qwen3_5` arch); no Unsloth import on default benchmark path

**Storage**: `artifacts/unsloth/` (gitignored checkpoints + train runs); `artifacts/benchmarks/unsloth-*` eval reports; read-only use of `artifacts/matrix_runs/paper-n200-full.json` + ledger/inspect for frozen Stage-1; split manifests under `artifacts/unsloth/splits/`

**Testing**: pytest for split leakage, gold-type export, shortlist+score adapter (mocked Unsloth), frozen-Choice eval path, analysis comparison (read-only); smoke train/eval documented for ZGX Nano (not CI-gated on 27B)

**Target Platform**: HP ZGX Nano / DGX Spark (Grace Blackwell ARM64, ~128GB unified); sequential exclusive GPU; Unsloth train/serve one at a time vs Lux sidecars

**Project Type**: Parallel training + eval track beside existing matrix (new scripts + optional engine; default `--real` pairs unchanged)

**Performance Goals**: Export + leakage check &lt;5 min; smoke train ≤1k rows &lt; few hours wall on QLoRA 27B; smoke eval N=20 &lt;1 h; full paper N=200 Score-only eval within sequential GPU budget after train

**Constraints**: Constitution v1.1.0; FR-010 immutability of published paper artifacts; fail-closed missing checkpoints; supervised DecisionTrainer only (no RL v1); `SYSTEMONE_MOCK=0` for official unsloth eval

**Scale/Scope**: One v1 pair `lux-unsloth-score`; engines e.g. `unsloth-decision-score` + hybrid `bm25-unsloth-score-shortlist-32` (or single hybrid Stage-2); scripts `export_unsloth_dataset.py`, `train_unsloth_score.py`, `run_unsloth_eval.py` (names may vary)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | No calculator / LLM math changes |
| II. Local System-1 First | PASS | Trained Score is local System-1; eval ranking-only by default |
| III. Local ARM64 Container Native | PASS | Prefer Unsloth/DGX Spark native path; document Podman GPU for 27B |
| IV. MCP Protocol Isolation | PASS | No new tool bypass |
| V. State Persistence & Auto-Resume | PASS | Eval uses existing ledger; train run metadata + checkpoint resume documented |
| VI. Trace Completeness | PASS | Stage-2 Score distributions/latency in inspect; frozen S1 labeled |
| VII. Two-Stage Agentic Retrieval | PASS | Choice→Score preserved; shortlist is Stage-2 orchestration only |

**Post-design re-check**: PASS — frozen Choice + shortlist→Score mirrors existing hybrid adapters; training isolated via optional extra; Complexity Tracking empty.

## Project Structure

### Documentation (this feature)

```text
specs/006-unsloth-decision-track/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── matrix-pairs-unsloth.md
│   ├── unsloth-cli.md
│   ├── training-export.md
│   └── analysis-report-unsloth.md
└── tasks.md                    # via /speckit-tasks (not this command)
```

### Source Code (repository root — extensions)

```text
pyproject.toml                    # optional-dependencies: unsloth
.gitignore                        # artifacts/unsloth/ checkpoints
configs/engines.yaml              # unsloth-decision-score + shortlist hybrid; pair lux-unsloth-score (optional)
scripts/
├── export_unsloth_dataset.py     # NEW: FinAgentBench → Score rows + SplitManifest
├── train_unsloth_score.py        # NEW: FastDecisionModel / DecisionTrainer
└── run_unsloth_eval.py           # NEW: frozen S1 + shortlist Score; unsloth-* run ids
src/finagent_mesh/
├── unsloth/                      # NEW package (optional import)
│   ├── split.py                  # paper test ids, leakage checks
│   ├── export.py                 # gold-type Score row builder
│   ├── train.py                  # thin wrappers around Unsloth APIs
│   └── frozen_stage1.py          # load Top-1 from paper-n200-full inspect/ledger
├── clients/engines/
│   ├── unsloth_score.py          # NEW: Score adapter (fail-closed)
│   ├── bm25_unsloth_shortlist.py # NEW: BM25 k=32 → Unsloth Score (mirror lux_shortlist)
│   └── registry.py               # register backends
└── matrix/
    ├── analysis.py               # Trained decision track section + read-only Δ
    ├── partners.py / ports.py    # optional pair + in-process hybrid deps
    └── runner.py                 # reuse MatrixRunner where possible from eval script
tests/unit/
├── test_unsloth_split.py
├── test_unsloth_export.py
├── test_bm25_unsloth_shortlist.py
└── test_unsloth_analysis.py
```

**Structure Decision**: Keep Unsloth train/export under `src/finagent_mesh/unsloth/` with lazy imports; eval reuses matrix runner patterns via dedicated script so default `run_benchmark.py --real` never pulls Unsloth. Hybrid Stage-2 copies `LuxShortlistAdapter` control flow with Unsloth Score instead of Lux HTTP.

## Complexity Tracking

> No constitution violations. Empty.
