# Feature Specification: FinAgentBench Hybrid Evaluation Harness

**Feature Branch**: `001-finagentbench-harness`

**Created**: 2026-10-04

**Status**: Draft

**Input**: User description: "Build a hybrid financial AI agent system evaluating the FinAgentBench benchmark dataset on an HP ZGX Nano / NVIDIA DGX Spark local AI station paired with Google Gemini API, including two-stage agentic retrieval metrics, local System-1 decision engines, cloud System-2 answer synthesis, governed filing/calculator tools, and crash-safe end-to-end harness auto-resume."

## Clarifications

### Session 2026-10-04

- Q: After Stage 1 ranks the five document types, which filings should Stage 2 rank chunks from? → A: Top-1 only (chunks from the single highest-ranked document type)
- Q: If Stage 1 and Stage 2 rankings and metrics succeed but cloud answer synthesis fails, should that example count as complete for resume purposes? → A: Ranking-complete, synthesis-retriable (commit Stage 1/2 + metrics; retry only synthesis)
- Q: Should this feature’s success criteria include scoring the quality of final synthesized answers, or only the two-stage ranking metrics? → A: Ranking plus answer accuracy (score final answers against FinAgentBench or equivalent labels)
- Q: How many top-ranked Stage-2 chunks should be passed into cloud answer synthesis by default? → A: Top-5 chunks (matches @5 metric cutoff)
- Q: After a retriable failure (local timeout or cloud synthesis error), how many automatic retries should the harness attempt before marking the example failed? → A: Up to 3 total attempts per failing stage by default; retry budget configurable via environment settings (e.g. `.env`)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Run Two-Stage FinAgentBench Ranking Evaluation (Priority: P1)

An evaluation operator loads FinAgentBench examples for S&P-500 firms and runs the mandated two-stage retrieval workflow: first rank document types among 10-K, 10-Q, 8-K, Earnings, and DEF14A; then rank paragraph-level passages (tables kept intact as single units) from the selected filings. The operator receives Stage-1 and Stage-2 ranking quality scores against expert ground-truth labels using nDCG@5, MAP@5, and MRR@5. After synthesis, the operator also receives an answer-quality score against FinAgentBench (or equivalent) answer labels.

**Why this priority**: Correct two-stage retrieval scoring plus answer scoring is the core benchmark contract; without it the harness cannot claim full FinAgentBench evaluation results.

**Independent Test**: Can be fully tested by running a small labeled subset through Stage 1 and Stage 2 only (no final answer synthesis) and verifying metric outputs match expected formulas against ground truth.

**Acceptance Scenarios**:

1. **Given** a FinAgentBench example with ground-truth document-type labels, **When** Stage 1 ranking completes, **Then** the system produces an ordered ranking over exactly the five document types and records nDCG@5, MAP@5, and MRR@5 for Stage 1.
2. **Given** the single highest-ranked document type from Stage 1 and extracted paragraph-level chunks from that type only (tables as single units), **When** Stage 2 ranking completes, **Then** the system produces an ordered chunk ranking and records nDCG@5, MAP@5, and MRR@5 for Stage 2.
3. **Given** expert ground-truth labels for both stages, **When** metrics are computed, **Then** scores are deterministic for the same rankings and labels (identical inputs yield identical metric values).
4. **Given** a synthesized final answer and an answer ground-truth label, **When** answer scoring runs, **Then** the system records an answer-quality score for that example alongside Stage-1/Stage-2 metrics.

---

### User Story 2 - Crash-Safe Full Dataset Evaluation Run (Priority: P1)

An evaluation operator starts an end-to-end FinAgentBench run over the full expert-annotated set (~26K examples). If the run is interrupted (process crash, power loss, or intentional stop), relaunching the harness resumes from the first incomplete example, skips already completed work, and does not duplicate results.

**Why this priority**: Multi-day local+cloud evaluation runs are unusable without reliable auto-resume.

**Independent Test**: Can be tested by completing N examples, forcibly stopping the harness mid-item, restarting, and confirming completed items are skipped and the interrupted item continues without duplicate ledger entries.

**Acceptance Scenarios**:

1. **Given** a run with some examples marked complete in the persistence ledger, **When** the harness is relaunched with the same run identity, **Then** it continues from the first incomplete example and does not re-execute completed ones.
2. **Given** a crash during processing of example K, **When** the harness restarts, **Then** example K is treated as incomplete (or safely retriable) and no completed example’s results are overwritten with duplicates.
3. **Given** Stage 1/2 rankings and metrics already committed for example K but synthesis failed, **When** the harness resumes, **Then** it retries only synthesis for K and does not re-run Stage 1 or Stage 2 ranking.
4. **Given** a finished full run, **When** the operator inspects the ledger, **Then** every dataset example has exactly one terminal completion record for that run (ranking-complete with optional synthesis outcome).

---

### User Story 3 - Local Guardrailed Path Before Cloud Synthesis (Priority: P2)

An evaluation operator runs examples such that on-station local decision services perform Stage 1 (document-type choice) and Stage 2 (chunk scoring/ranking) before any cloud frontier model is used. Final answer synthesis over the top-ranked chunks uses the configured cloud reasoning model only after local ranking stages complete.

**Why this priority**: Separates expensive/cloud reasoning from local ranking control and keeps policy-sensitive ranking on-premises.

**Independent Test**: Can be tested by processing examples with cloud credentials disabled after Stage 2 and verifying Stage 1/2 rankings and metrics still complete; then enabling cloud synthesis and verifying answers are produced only from top-ranked chunks.

**Acceptance Scenarios**:

1. **Given** healthy local decision services, **When** an example is processed, **Then** Stage 1 and Stage 2 rankings are produced by the local fast path before any cloud synthesis call.
2. **Given** Stage 2 ranking results, **When** final answer synthesis runs, **Then** the cloud model receives the question plus the top-5 ranked chunks by default (or an operator-overridden K) and returns a synthesized answer.
3. **Given** local decision services are unhealthy, **When** the harness attempts an example, **Then** it fails closed for that example (records failure, does not silently skip to cloud-only ranking).

---

### User Story 4 - Build and Serve Local Decision Engines (Priority: P2)

A platform operator builds native ARM64 container images for the local decision engines on the ZGX Nano / DGX Spark station with GPU acceleration support and serves local decision APIs on the designated local endpoints used by the harness.

**Why this priority**: Local ranking depends on reproducible, hardware-native decision services on Grace Blackwell ARM64.

**Independent Test**: Can be tested by running the container build automation on the target station, starting the engines, and confirming health endpoints respond on the expected local ports before any benchmark examples run.

**Acceptance Scenarios**:

1. **Given** a ZGX Nano / DGX Spark host with GPU container support, **When** the operator runs the container build automation, **Then** images for the required local decision engines are produced for native ARM64.
2. **Given** built images, **When** the operator starts the local decision services, **Then** System-1 APIs are reachable at the two configured local endpoints on ports 8000 and 8001.
3. **Given** services are starting, **When** the harness performs health checks, **Then** evaluation does not begin until required local services report healthy (or the run records a clear startup failure).

---

### User Story 5 - Tool-Mediated Filing Access and Deterministic Finance Math (Priority: P2)

During evaluation, the agent retrieves SEC filing content and document-type metadata, extracts paragraph-level chunks, and performs any IRR, NPV, amortization, or ratio calculations only through governed tool interfaces—not by inventing numbers in free-form model text.

**Why this priority**: Filing access and numeric correctness are required for faithful financial agent behavior and benchmark integrity.

**Independent Test**: Can be tested by invoking filing retrieval/chunk extraction on a known ticker/filing and by running calculator tool cases (IRR/NPV/ratios) with known inputs and verifying exact numeric outputs.

**Acceptance Scenarios**:

1. **Given** a firm and needed document type, **When** filing retrieval is requested through the governed tool path, **Then** the system returns filing content/metadata suitable for Stage 1/2.
2. **Given** a filing selected for Stage 2, **When** chunk extraction runs, **Then** paragraph-level passages are returned and tabular regions are preserved as single chunk units.
3. **Given** a financial calculation request (IRR, NPV, amortization, or ratio analysis), **When** the agent needs a numeric result, **Then** the result comes from the deterministic calculator tool and is recorded as a tool outcome.

---

### User Story 6 - Full-Run Observability for Audit and Debugging (Priority: P3)

An evaluation operator inspects a completed or in-progress run and can reconstruct each example’s state transitions, local decision scores/distributions, tool executions, ranking outputs, metrics, and final answers from the run’s trace record.

**Why this priority**: Research credibility and debugging depend on complete traces, but ranking correctness and resume are higher priority.

**Independent Test**: Can be tested by running a handful of examples and verifying each has a reconstructible trace covering ranking stages, tool calls, and synthesis.

**Acceptance Scenarios**:

1. **Given** a processed example, **When** the operator opens the run’s trace record, **Then** Stage 1 ranking, Stage 2 ranking, tool calls, and final synthesis (if any) are all present.
2. **Given** a local ranking decision, **When** the trace is inspected, **Then** the decision probability distribution (or equivalent score vector) is recorded.
3. **Given** a failed example, **When** the operator reviews traces and the ledger, **Then** failure reason and resume eligibility are clear.

### Edge Cases

- Dataset example missing Stage-1 or Stage-2 ground-truth labels: record as skipped/invalid with reason; do not fabricate metrics.
- Dataset example missing answer ground-truth label: still compute Stage-1/Stage-2 metrics when possible; skip answer scoring with explicit reason.
- Empty chunk set after extraction for the Top-1 Stage-1 document type: fail the example with a structured error; do not call cloud synthesis.
- Local decision service timeout or resource exhaustion during ranking: retry automatically up to the configured attempt budget (default 3 total attempts for that stage); if still failing, mark failed/retriable for later resume; do not fall back to cloud for ranking.
- Cloud synthesis rate limit or auth failure: commit Stage 1/2 results and metrics as ranking-complete; retry synthesis up to the configured attempt budget (default 3 total attempts); if still failing, mark synthesis-retriable; on resume retry synthesis only (do not re-rank).
- Duplicate harness launches for the same run identity: only one active writer may advance the ledger; the other exits or waits with a clear conflict message.
- Partial ledger write interrupted mid-commit: resume logic treats the example as incomplete and retries safely (no silently “half-complete” success).
- Very large tables or filings: tables remain single units; extraction failures are logged per example without aborting the entire run.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST load and iterate FinAgentBench expert-annotated examples covering S&P-500 firms (full ~26K set supported; optional subset/sample mode allowed for smoke tests).
- **FR-002**: System MUST perform Stage 1 Document-Type Level Ranking over exactly the set {10-K, 10-Q, 8-K, Earnings, DEF14A} for each applicable example.
- **FR-003**: System MUST perform Stage 2 Chunk-Level Ranking over paragraph-level passages extracted only from the single highest-ranked document type from Stage 1 (Top-1), preserving tabular data as single chunk units.
- **FR-004**: System MUST compute and persist nDCG@5, MAP@5, and MRR@5 for Stage 1 and for Stage 2 against ground-truth labels.
- **FR-005**: System MUST complete Stage 1 and Stage 2 using on-station local decision services before any cloud frontier synthesis call.
- **FR-006**: System MUST serve local decision APIs at `http://localhost:8000` and `http://localhost:8001` for harness consumption.
- **FR-007**: System MUST provide build automation that produces native Grace Blackwell ARM64 container images for the required local decision engines with GPU container acceleration support.
- **FR-008**: System MUST treat Stage 1 as an explicit document-type choice decision on the local path (not merged into chunk ranking).
- **FR-009**: System MUST treat Stage 2 as an explicit chunk ranking/scoring decision on the local path over candidate passages from the Top-1 Stage-1 document type only.
- **FR-010**: System MUST perform final answer synthesis only after Stage 2, using the operator-configured cloud reasoning model, over the top-K Stage-2 chunks with default K=5 (operator-overridable).
- **FR-020**: System MUST score each successfully synthesized final answer against FinAgentBench (or equivalent) answer ground-truth labels and persist the answer-quality score with the example results; examples lacking answer labels MUST be marked skipped for answer scoring without blocking Stage-1/Stage-2 metrics.
- **FR-011**: System MUST retrieve filings, document-type metadata, and chunk extractions exclusively through the governed SEC filings tool path via the access gateway.
- **FR-012**: System MUST perform IRR, NPV, amortization, and ratio analysis exclusively through the governed deterministic calculator tool path; free-form model text MUST NOT be accepted as the source of those numeric results.
- **FR-013**: System MUST route all tool calls through the access gateway with schema-validated tool requests, access control, and rate limiting.
- **FR-014**: Harness MUST orchestrate service startup, health checks, gateway access, evaluation loop, metric computation, and run logging for an end-to-end evaluation.
- **FR-015**: System MUST maintain an atomic persistence ledger for evaluation progress such that restart resumes from the last uncompleted example without duplicating completed work.
- **FR-019**: System MUST treat successful Stage 1/2 ranking plus metrics as a durable ranking-complete checkpoint; if cloud synthesis fails afterward, resume MUST retry synthesis only and MUST NOT re-execute Stage 1 or Stage 2 for that example.
- **FR-021**: System MUST automatically retry retriable stage failures up to a configured total-attempt budget per failing stage (default 3), read from operator environment configuration without code changes; after exhaustion, the example MUST be marked failed or synthesis-retriable as applicable without unbounded looping.
- **FR-016**: System MUST record every agent state transition, local decision distribution/scores, tool execution, ranking output, metric values, and synthesis outcome in the run’s trace store for auditability.
- **FR-017**: Operators MUST be able to start, stop, and resume a named evaluation run and export Stage-1/Stage-2 metrics summaries for the run.
- **FR-018**: System MUST fail closed when required local decision services are unhealthy rather than silently substituting cloud models for ranking stages.

### Key Entities

- **Benchmark Example**: A FinAgentBench item with question/context identifiers, firm reference, Stage-1/Stage-2 ground-truth labels, optional answer ground-truth label, and evaluation status within a run.
- **Answer Score**: Per-example answer-quality result comparing the synthesized final answer to the answer ground-truth label.
- **Document Type Candidate**: One of 10-K, 10-Q, 8-K, Earnings, DEF14A; participates in Stage 1 ranking.
- **Passage Chunk**: A paragraph-level unit (or preserved table unit) extracted from a filing; participates in Stage 2 ranking.
- **Stage Ranking Result**: Ordered list of candidates/chunks with scores plus computed nDCG@5, MAP@5, and MRR@5 for that stage.
- **Evaluation Run**: Named execution over a dataset slice or full set, including configuration and aggregate metrics.
- **Ledger Entry**: Atomic per-example progress record (pending, in-progress, ranking-complete, synthesis-retriable, completed, failed/retriable, skipped) tied to a run.
- **Tool Invocation Record**: Governed call to filing or calculator tools with inputs, outputs, and status.
- **Trace Record**: Append-only audit of state transitions, decision distributions, tool calls, and outputs for an example.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of evaluated examples with valid labels produce both Stage-1 and Stage-2 metric triples (nDCG@5, MAP@5, MRR@5), or a structured skip/failure reason if labels or content are missing.
- **SC-009**: 100% of examples with a successful synthesis and a valid answer ground-truth label receive a persisted answer-quality score; examples missing answer labels are skipped for answer scoring with an explicit reason and still retain Stage-1/Stage-2 metrics when available.
- **SC-010**: In default configuration, synthesis for each example uses exactly the top-5 Stage-2 chunks unless the operator sets a different K for that run.
- **SC-011**: Under default configuration, a injected retriable failure recovers within 3 total attempts for that stage or else reaches a non-looping failed/synthesis-retriable terminal state; changing the environment retry setting changes the observed attempt budget accordingly.
- **SC-002**: After an intentional crash mid-run, a restarted harness completes the remaining unfinished examples with zero re-processing of already completed or ranking-complete examples for that run (verified via ledger audit); synthesis-only failures resume without re-ranking.
- **SC-003**: In a controlled fault test where local ranking services are down, 0% of examples produce cloud-only Stage-1 or Stage-2 rankings (fail closed).
- **SC-004**: On a target ZGX Nano / DGX Spark host, operators can go from source checkout to healthy local decision endpoints on ports 8000 and 8001 using the provided build/start automation without manual architecture rework.
- **SC-005**: For a fixed golden subset of at least 50 labeled examples, repeated ranking and metric computation yields identical Stage-1 and Stage-2 metric values.
- **SC-006**: 100% of financial numeric operations observed in sampled traces for IRR, NPV, amortization, and ratios are attributable to the deterministic calculator tool path (zero model-invented numerics accepted as results).
- **SC-007**: Operators can reconstruct, from traces alone, the Stage-1 ordering, Stage-2 ordering, tool calls, and final answer (if any) for every successfully completed example in a smoke run of at least 20 examples.
- **SC-008**: A smoke evaluation of at least 100 examples completes end-to-end (retrieve → Stage 1 → Stage 2 → optional synthesis → metrics → ledger complete) with at least 95% of examples reaching a terminal ledger state (completed, skipped-invalid, or failed-with-reason)—not stuck in-progress.

## Assumptions

- FinAgentBench data (or a licensed/accessible copy of the ~26K expert-annotated S&P-500 examples) is available to the evaluation host; distribution and licensing are outside this feature’s build scope but required at runtime.
- Target hardware is HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64) with NVIDIA Container Toolkit available; non-ARM CI may validate non-GPU unit logic only.
- Local decision engines in scope are vLLM-sr, AnyJev (L0/L1), and CLM-8B; Stage 1 uses Choice-style decisions (AnyJev and/or vLLM-sr Decision-2.0), Stage 2 uses CLM-8B Action Cache and/or Score-style ranking, as configured per run.
- Stage 2 always uses Top-1 Stage-1 document type only; it MUST NOT pool chunks across multiple document types for ranking or Stage-2 metrics.
- Default synthesis context is the top-5 Stage-2 chunks (K=5), aligned with the @5 ranking metric cutoff; operators may override K per run.
- Default automatic retry budget is 3 total attempts per failing stage; operators may override via environment configuration (e.g. `.env`) without code changes.
- Container build automation lives at `scripts/build_containers.sh` and supports Podman (preferred) or docker buildx, still targeting native ARM64 with GPU toolkit support.
- End-to-end orchestration entrypoint is `scripts/run_harness.py`; persistence ledger is `eval_ledger.db` (atomic resume store).
- Cloud synthesis uses Gemini 2.5/3 Pro or Flash via Google AI Studio API key; default synthesis model is Gemini Flash unless overridden per run.
- Governed tools are `mcp-sec-edgar` (filings, document-type metadata, chunk extraction) and `mcp-financial-calculator` (IRR, NPV, amortization, ratios), always via AgentGateway using MCP schemas.
- Orchestration uses an explicit agent state machine with MLflow agentic tracing for run auditability (project constitution mandate).
- “Full run” means the entire FinAgentBench labeled set; subset/sample modes exist for development and CI smoke tests.
- Answer-quality scoring is in scope for v1 whenever answer ground-truth labels are present; exact scoring rubric (exact match, normalized match, or graded semantic score) is chosen at plan time from FinAgentBench’s published evaluation definition.
- Out of scope: training or finetuning local decision models; public multi-tenant SaaS UI; non-FinAgentBench benchmarks.
- Constitution v1.1.0 principles apply and supersede conflicting shortcuts (deterministic finance math, local System-1 first, ARM64 containers, MCP isolation, auto-resume, trace completeness, two-stage retrieval).
