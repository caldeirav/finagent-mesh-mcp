# Research: FinAgentBench Hybrid Evaluation Harness

**Feature**: `001-finagentbench-harness` | **Date**: 2026-10-04

## 1. Orchestration framework

**Decision**: LangGraph (`langgraph` + `langchain-core`) as the agent state machine.

**Rationale**: Constitution requires LangGraph state transitions and MLflow-traceable node boundaries. Explicit Stage 1 → Stage 2 → synthesize → score maps cleanly to typed graph nodes with durable checkpoint hooks into the ledger.

**Alternatives considered**:
- Ad-hoc Python loop — simpler, but weaker state/transition auditing and harder MLflow span alignment.
- Pure LangChain LCEL chains — less natural for multi-stage resume and branching on ranking-complete vs synthesis-retriable.

## 2. Local System-1 interface

**Decision**: Custom `OpenDecisionClient` calling TypeSafe-compatible System-1 HTTP APIs at `/v1/systemone`, fronted by AgentGateway. Default bind: Stage-1 Choice engines on `:8000`, Stage-2 Score/Action-Cache (CLM-8B) on `:8001`.

**Rationale**: Spec requires local ports 8000/8001 and Choice vs Score primitives. A thin client isolates retry, timeout, and probability-vector capture for MLflow without coupling the graph to engine internals.

**Alternatives considered**:
- Direct OpenAI-compat `/v1/chat/completions` only — insufficient for Choice/Score distributions required by FR-016.
- Embedding each engine SDK in the harness — higher coupling and ARM64 packaging risk.

## 3. Container runtime on Grace Blackwell

**Decision**: Podman preferred with `nvidia-container-toolkit`; `docker buildx` allowed as alternate build path in `scripts/build_containers.sh`, always targeting `linux/arm64`.

**Rationale**: Constitution Principle III; ZGX Nano / DGX Spark GB10 is ARM64 with 128GB unified memory. Native images avoid emulation and match NVIDIA’s GPU container toolkit path.

**Alternatives considered**:
- x86_64 images under qemu — rejected (perf + correctness risk).
- Host-process GPU servers without containers — harder reproducibility and ops parity.

## 4. Cloud System-2 synthesis

**Decision**: `langchain-google-genai` with Gemini Flash default; Pro selectable via env. Synthesis only after Stage 2; context = top-K chunks (default K=5).

**Rationale**: Matches operator stack and clarify session (Top-5). Flash default controls cost on ~26K runs; Pro available for quality sweeps.

**Alternatives considered**:
- Vertex AI-only SDK — heavier auth for Google AI Studio key workflow.
- Local-only synthesis — out of scope; brief requires Gemini path.

## 5. Gateway and MCP tooling

**Decision**: All tool calls through AgentGateway using the official Python `mcp` SDK. Servers: `mcp-sec-edgar`, `mcp-financial-calculator`.

**Rationale**: Constitution Principles I and IV. Keeps rate limits, auth, and schemas in one choke point.

**Alternatives considered**:
- Direct HTTP to EDGAR/calculators — violates MCP isolation.
- Embedding calculator in the agent process — bypasses audit boundary.

## 6. Ranking metrics

**Decision**: Implement nDCG@5, MAP@5, MRR@5 in-process against FinAgentBench stage labels; deterministic pure functions with fixed tie-break (stable sort by score desc, then candidate id asc).

**Rationale**: Spec SC-005 requires identical repeats; in-process metrics avoid external scorer drift. @5 matches synthesis K default.

**Alternatives considered**:
- External IR evaluation binaries — extra native deps on ARM64.
- Sampling-based approximate metrics — non-deterministic.

## 7. Answer-quality scoring

**Decision**: Primary scorer = **normalized exact match** (lowercase, whitespace/punctuation normalize, unicode NFKC). Secondary diagnostic = token-level F1. Persist both; treat normalized EM as the official answer-quality score for SC-009 unless FinAgentBench release notes define a stricter official rubric—then adapt while keeping EM as regression baseline.

**Rationale**: Spec deferred rubric to plan time. Normalized EM is deterministic, cheap, and auditable for financial short answers; token F1 helps analyze near-misses without making the gate flaky.

**Alternatives considered**:
- LLM-as-judge — non-deterministic, costly, conflicts with preference for measurable gates.
- Embedding cosine only — harder to explain and threshold.

## 8. Persistence ledger

**Decision**: SQLite file `eval_ledger.db` with WAL mode, single-writer lock (PID/lease row), transactional transitions: `pending → in_progress → ranking_complete → synthesis_retriable|completed|failed_*|skipped_*`.

**Rationale**: Spec FR-015/019; clarify session ranking-complete / synthesis-retriable. SQLite is local-first, atomic, and sufficient for one-station runs.

**Alternatives considered**:
- LangGraph checkpointer alone — does not encode evaluation-domain states/metrics export.
- PostgreSQL — unnecessary ops overhead for single Nano host.

## 9. Retry policy

**Decision**: Default `HARNESS_MAX_ATTEMPTS=3` (total attempts per failing stage) via `.env`; exponential backoff with jitter for cloud 429s; no cloud fallback for ranking failures.

**Rationale**: Clarify session answer B + env configurability; SC-011.

**Alternatives considered**: Unlimited retries — unbounded runs. Zero retries — brittle on transient GPU/API faults.

## 10. Observability

**Decision**: Nested MLflow Runs (per example) plus GenAI Traces: `mlflow.langchain.autolog(run_tracer_inline=True)`, root `finagent_example` agent span, System-1 `systemone_{choice|score}` retriever spans, `gemini_synthesize` LLM span. Log Stage-1/2 outcome metrics (`stage1_top1_correct`, nDCG/MAP/MRR), Gemini outcomes (`gemini_synthesis_ok`, answer EM/F1), probability vectors, tool I/O, synthesis text.

**Rationale**: Constitution Principle VI.

**Alternatives considered**: Structured logs only — weaker reconstructability for SC-007.

## 11. Dataset handling

**Decision**: Local FinAgentBench dataset path via `FINAGENTBENCH_PATH`; support `--limit` / sample mode for smoke; full 26K for production runs. Ten query categories preserved as metadata filters.

**Rationale**: Spec FR-001; data licensing remains operator-provided.

**Alternatives considered**: Streaming remote dataset each example — fragile for resume and offline station use.

## 12. Port and engine mapping

**Decision**:
- `:8000` — Stage 1 Choice path (AnyJev L0/L1 and/or vLLM-sr Decision-2.0 behind gateway)
- `:8001` — Stage 2 Score / CLM-8B Action Cache path

**Rationale**: Spec FR-006; separates load profiles (5-way choice vs many-chunk scoring).

**Alternatives considered**: Single multiplexed port — simpler networking, harder resource isolation and health semantics.
