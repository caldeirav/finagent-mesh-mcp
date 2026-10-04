# Implementation Plan: Decision Model Serving & Benchmark Matrix

**Branch**: `002-systemone-model-serving` | **Date**: 2026-10-04 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-decision-model-bench/spec.md` (clarified: per-stage binding, sequential variable engines + fixed partners, full-pipeline Gemini Flash default, end-to-end Stage 1+2 agentic process).

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Replace mock System-1 paths with real, health-checked decision-engine serving for a five-family benchmark matrix (AnyJev L0/L1, CLM-8B Action Cache, vLLM-sr Decision-2.0 Kai/Lux, Laya ModernBERT, AR Qwen3-8B-Instruct). Matrix rows vary one engine at a time while a fixed Stage partner co-runs so each FinAgentBench example executes Stage 1→Stage 2→Gemini Flash synthesis in one LangGraph process. Fail-closed Gemini (no extractive fallback); seeded full/sample dataset modes; comparative matrix export with per-stage metric attribution.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed; existing `finagent-mesh-mcp` package)

**Primary Dependencies**: Existing harness (`langgraph`, `langchain-google-genai`, `httpx`, `mlflow`, SQLite ledger) plus engine-specific stacks: vLLM / anyjev / clm-serve for GPU engines; `transformers` + `torch` for Laya; OpenDecisionClient adapters per engine; matrix CLI (`typer`)

**Storage**: Existing `eval_ledger.db` + MLflow; engine registry YAML/JSON; AnyJev L1 calibration artifact (200-example held-out); CLM Action Cache embedding store; matrix report JSON/CSV exports

**Testing**: `pytest` contract tests against `/healthz` + `/v1/systemone` (or engine-specific adapters); integration smokes with one real engine + partner; fail-closed Gemini unit tests; matrix orchestration tests with fake engines

**Target Platform**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, 128GB unified memory); Podman + `nvidia-container-toolkit`; Laya may run CPU/GPU edge mode

**Project Type**: Extension of existing evaluation harness + containerized model servers + matrix runner CLI

**Performance Goals**: Sequential matrix rows without OOM; reproducible sample seed; smoke ≥20 examples ≥95% terminal; sample matrix ≥50 examples with ranking + synthesis attempts; per-example Stage 1+2 in one agentic trace

**Constraints**: Constitution v1.1.0; `SYSTEMONE_MOCK=0` for official runs; no extractive System-2; fail closed on unhealthy engines / Gemini errors; Top-1 Stage-1 → Stage 2; fixed partners (Stage-2=CLM-8B, Stage-1 Choice default=AnyJev-L0); one variable matrix engine under test at a time

**Scale/Scope**: 7 matrix configurations (AnyJev-L0, AnyJev-L1, CLM-8B, Decision-2.0-Kai, Decision-2.0-Lux, Laya, AR-Qwen3-8B-Instruct); full ~26K FinAgentBench or seeded sample; full pipeline default (ranking + Gemini Flash + answer score)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | Unchanged MCP calculator path |
| II. Local System-1 First | PASS | Real local engines before Gemini; fail closed |
| III. Local ARM64 Container Native | PASS | Podman ARM64 Containerfiles/serve scripts per engine |
| IV. MCP Protocol Isolation | PASS | Tools remain via AgentGateway |
| V. State Persistence & Auto-Resume | PASS | Ledger reused for matrix/pipeline runs |
| VI. Trace Completeness | PASS | Engine id, distributions, latency, Gemini model in MLflow |
| VII. Two-Stage Agentic Retrieval | PASS | Single agentic process Stage 1→2 (Top-1) per example |

**Post-design re-check**: PASS — contracts and data model preserve gates; Complexity Tracking empty.

## Project Structure

### Documentation (this feature)

```text
specs/002-decision-model-bench/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md             # /speckit-tasks (not this command)
```

### Source Code (repository root — extensions)

```text
src/finagent_mesh/
├── clients/
│   ├── open_decision.py          # harden; remove extractive Gemini fallback in gemini.py
│   ├── gemini.py                 # fail-closed only
│   └── engines/                  # NEW adapters
│       ├── registry.py           # EngineConfiguration catalog
│       ├── anyjev.py
│       ├── clm8b.py
│       ├── vllm_sr.py
│       ├── laya.py
│       └── ar_baseline.py
├── matrix/                       # NEW
│   ├── runner.py                 # sequential matrix orchestration
│   ├── sampling.py               # seeded random sample
│   ├── partners.py               # fixed Stage-1/Stage-2 partners
│   └── report.py                 # comparative export
├── runtime/
│   ├── harness.py                # per-stage binding + mock disable
│   └── health.py                 # multi-engine health
└── agent/                        # existing graph; bind clients per stage

containers/
├── anyjev/                       # real serve (replace placeholders)
├── clm-8b/
├── vllm-sr/                      # Kai + Lux variants via compose/env
├── laya/
└── ar-qwen3-instruct/

scripts/
├── build_containers.sh           # extend for all engines
├── serve_engine.sh               # NEW: start/stop/health one config
├── run_harness.py                # add --stage1-engine --stage2-engine
└── run_matrix.py                 # NEW matrix CLI

configs/
├── engines.yaml                  # ports, primitives, partners, weights paths
└── calibration/
    └── anyjev_l1_heldout.json    # 200-example ids or path pointer

tests/
├── contract/test_engines_*.py
├── integration/test_matrix_smoke.py
└── unit/test_gemini_fail_closed.py
```

**Structure Decision**: Extend the existing single-package harness with an `engines/` adapter layer and `matrix/` orchestration rather than a second app. Containers remain per-engine under `containers/`; matrix CLI is a thin script over shared runtime.

## Complexity Tracking

> No unjustified constitution violations. Multi-engine matrix is the feature scope; sequential variable + fixed partner keeps Nano memory feasible.
