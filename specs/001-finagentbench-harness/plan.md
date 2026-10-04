# Implementation Plan: FinAgentBench Hybrid Evaluation Harness

**Branch**: `001-finagentbench-harness` | **Date**: 2026-10-04 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-finagentbench-harness/spec.md` plus operator tech-stack constraints (ZGX Nano / DGX Spark, Podman, LangGraph, Gemini via `langchain-google-genai`, `OpenDecisionClient` → `/v1/systemone`, AgentGateway + MCP, MLflow, SQLite `eval_ledger.db`).

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Build a crash-safe FinAgentBench evaluation harness on HP ZGX Nano / NVIDIA DGX Spark that runs FinAgentBench’s two-stage agentic retrieval (Stage 1 document-type ranking over {10-K, 10-Q, 8-K, Earnings, DEF14A}, Stage 2 chunk ranking over Top-1 type passages), scores both stages with nDCG@5 / MAP@5 / MRR@5, synthesizes answers with Gemini over top-5 chunks, scores answer quality against labels, and resumes via an atomic SQLite ledger. Local System-1 engines (AnyJev, vLLM-sr, CLM-8B) serve Choice/Score primitives through AgentGateway; SEC filings and deterministic finance math go through MCP tools only; LangGraph orchestrates the loop with MLflow traces.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed; `requires-python = ">=3.12,<3.13"`)

**Primary Dependencies**: `langgraph`, `langchain-core`, `langchain-google-genai`, `mcp` (Python SDK), AgentGateway client/proxy integration, `mlflow`, `httpx`/`openai`-compatible HTTP for System-1, SQLite (stdlib), ranking metrics (`numpy` or pure Python), Podman + `nvidia-container-toolkit` for local engines

**Storage**: SQLite ledger `eval_ledger.db` (atomic resume); FinAgentBench dataset files on local disk; MLflow tracking store (local file or configured URI)

**Testing**: `pytest` (+ `pytest-asyncio` as needed); unit tests for metrics/ledger; contract tests for System-1 and MCP schemas; integration smoke against mocked local/cloud endpoints; ARM64 GPU path validated on target hardware

**Target Platform**: HP ZGX Nano / NVIDIA DGX Spark — NVIDIA GB10 Grace Blackwell, 128GB unified memory, ARM64 Linux; local APIs at `http://localhost:8000` and `http://localhost:8001`

**Project Type**: Single Python application / evaluation harness (CLI entrypoints + MCP server packages + container build scripts)

**Performance Goals**: Support full ~26K-example runs with durable resume; smoke ≥100 examples with ≥95% terminal ledger states; golden ≥50-example metric determinism; default synthesis K=5; default 3 attempts per failing stage

**Constraints**: Constitution v1.1.0 (deterministic MCP math, local System-1 before Gemini, ARM64 Podman GPU containers, MCP via AgentGateway, auto-resume, MLflow traces, explicit two-stage retrieval); Top-1 Stage-1 → Stage-2; ranking-complete / synthesis-retriable; fail closed if local ranking unhealthy; no cloud-only ranking fallback

**Scale/Scope**: ~26K FinAgentBench examples, 10 query categories, S&P-500 filings; 5 document types; paragraph+table chunks; dual local decision ports; two MCP servers; one orchestrated harness

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | IRR/NPV/amortization/ratios only via `mcp-financial-calculator` |
| II. Local System-1 First | PASS | Stage 1/2 via local `/v1/systemone` before Gemini synthesis |
| III. Local ARM64 Container Native | PASS | `scripts/build_containers.sh` → Podman + nvidia-container-toolkit, Grace Blackwell ARM64 |
| IV. MCP Protocol Isolation | PASS | All tools via AgentGateway + MCP schemas |
| V. State Persistence & Auto-Resume | PASS | SQLite `eval_ledger.db` with ranking-complete / synthesis-retriable |
| VI. Trace Completeness | PASS | MLflow traces for LangGraph transitions, distributions, tools |
| VII. Two-Stage Agentic Retrieval | PASS | Explicit Stage 1 then Stage 2 (Top-1 type) nodes |

**Post-design re-check**: PASS — data model, contracts, and quickstart preserve all seven gates; Complexity Tracking empty (no unjustified violations).

## Project Structure

### Documentation (this feature)

```text
specs/001-finagentbench-harness/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
src/finagent_mesh/
├── __init__.py
├── config.py                 # env/.env settings (retry budget, K, ports, model ids)
├── dataset/
│   └── finagentbench.py      # loader + subset sampling
├── metrics/
│   ├── ranking.py            # nDCG@5, MAP@5, MRR@5
│   └── answer.py             # answer-quality scoring
├── ledger/
│   └── sqlite_ledger.py      # eval_ledger.db atomic ops + locking
├── clients/
│   ├── open_decision.py      # OpenDecisionClient → /v1/systemone
│   └── gemini.py             # langchain-google-genai wrapper
├── gateway/
│   └── mcp_gateway.py        # AgentGateway-mediated MCP client
├── agent/
│   ├── state.py              # LangGraph state schema
│   ├── graph.py              # two-stage + synthesize + score graph
│   └── nodes/                # stage1, stage2, tools, synthesize, metrics
├── scoring/
│   └── run_aggregator.py     # export Stage-1/2 + answer summaries
└── runtime/
    ├── health.py             # localhost:8000/8001 health checks
    └── harness.py            # used by scripts/run_harness.py

mcp_servers/
├── mcp_sec_edgar/            # filings, doc-type metadata, chunk extract
└── mcp_financial_calculator/ # IRR, NPV, amortization, ratios

containers/
├── vllm-sr/
├── anyjev/
└── clm-8b/

scripts/
├── build_containers.sh
└── run_harness.py

tests/
├── unit/
├── integration/
└── contract/

.env.example
```

**Structure Decision**: Single Python package under `src/finagent_mesh/` with sibling `mcp_servers/`, `containers/`, and `scripts/`. Matches the repo’s uv application layout and keeps MCP servers deployable as separate processes behind AgentGateway without a multi-app monorepo.

## Complexity Tracking

> No constitution violations requiring justification. Dual-system + MCP + containers are mandated by Constitution v1.1.0, not optional complexity.
