# Feature Specification: Decision Model Serving & Benchmark Matrix

**Feature Branch**: `002-systemone-model-serving`

**Created**: 2026-10-04

**Status**: Draft

**Input**: User description: "Integrate model serving and benchmarking of different decision models into the agentic pipeline. Benchmark matrix evaluates five representative engine configurations: AnyJev L0 & L1 (Qwen3-8B) with adaptive cyclic shifts / temperature scaling; CLM-8B via clm-serve with Action Cache over Qwen3-8B pooling; vLLM-sr Decision-2.0 (Kai-0.6B & Lux-9B); Laya (ModernBERT 421M) via local Transformers baselines; Autoregressive LLM Baseline (Qwen3-8B-Instruct) with JSON choice output, latency, parse failures, and log-prob calibration. Agent pipeline must use fail-closed Gemini for System-2 (no extractive fallback). Benchmark script integrates with full FinAgentBench and supports small random sample runs for integration testing."

## Clarifications

### Session 2026-10-04

- Q: For a full agent pipeline run, how should Stage 1 and Stage 2 pick decision engines? → A: Per-stage binding (Stage 1 and Stage 2 may use different configurations; same-engine option allowed)
- Q: When running the multi-engine benchmark matrix on the ZGX Nano, should engines be evaluated one at a time or can several heavy GPU engines run concurrently? → A: Sequential exclusive (one heavy GPU engine configuration active per matrix row); Stage 1 and Stage 2 still run together in one end-to-end agentic process
- Q: When a matrix row tests a Stage-1-only engine (for example AnyJev), which engine should handle Stage 2 inside that same end-to-end agentic run? → A: Fixed partner (Stage-1-only rows use CLM-8B for Stage 2; Stage-2-only rows use a designated Choice engine for Stage 1)
- Q: Should the default multi-engine matrix run include Gemini System-2 answer synthesis, or only Stage 1/Stage 2 ranking metrics? → A: Full pipeline default (every matrix example includes Gemini synthesis + answer scoring)
- Q: Which Gemini model should be the default for System-2 synthesis in matrix and pipeline runs? → A: Gemini Flash default (Pro selectable per run)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Serve and Health-Check Decision Engines (Priority: P1)

A platform operator brings up each required local decision-engine configuration on the ZGX Nano station, confirms each engine is healthy and reachable for Choice and/or Score decisions, and can stop unhealthy engines without the harness silently inventing rankings.

**Why this priority**: Without real, health-checked decision services, the agent pipeline cannot evaluate System-1 models—only mocks.

**Independent Test**: Start one engine configuration, verify health and a single decision request succeed; stop the engine and verify the harness fails closed for ranking.

**Acceptance Scenarios**:

1. **Given** a supported engine configuration is started on the station, **When** the operator runs the health check, **Then** the service reports healthy and accepts a decision request for its supported primitive(s).
2. **Given** the required Stage-1 and/or Stage-2 engine for a run is unhealthy, **When** the harness processes an example, **Then** it fails closed for ranking and does not produce cloud-only Stage-1/Stage-2 rankings.
3. **Given** multiple engine configurations are defined in the matrix, **When** the operator selects one configuration for a run, **Then** only that configuration’s endpoints are used for System-1 decisions for that run.

---

### User Story 2 - Benchmark Matrix Across Five Engine Families (Priority: P1)

An evaluation operator runs the decision-model benchmark matrix that compares five representative configurations—AnyJev L0/L1, CLM-8B Action Cache, vLLM-sr Decision-2.0 (Kai and Lux variants), Laya edge baseline, and an autoregressive instruct baseline—on FinAgentBench ranking tasks, collecting quality metrics and operational signals (latency, parse failures, calibration where applicable).

**Why this priority**: Comparing engines on the same benchmark is the core research outcome of this feature.

**Independent Test**: Run the matrix (or a subset of engines) on a small random FinAgentBench sample and obtain a comparable metrics table per engine including Gemini synthesis and answer scoring by default; each example must execute Stage 1 and Stage 2 in one agentic process.

**Acceptance Scenarios**:

1. **Given** FinAgentBench labels for Stage 1 and/or Stage 2, **When** a matrix run completes for an engine, **Then** the operator receives Stage ranking metrics (nDCG@5, MAP@5, MRR@5 as applicable) plus Gemini synthesis/answer-score outcomes for that engine’s examples.
2. **Given** the autoregressive instruct baseline, **When** it produces choices, **Then** the run records generation latency, JSON parse failure rate, and log-probability calibration signals.
3. **Given** AnyJev L0 vs L1, **When** both are evaluated, **Then** results are reported as distinct matrix rows (L0 adaptive cyclic shifts vs L1 temperature scaling calibrated on a held-out set of 200 examples).
4. **Given** vLLM-sr Decision-2.0, **When** Kai and Lux are evaluated, **Then** results are reported as distinct matrix rows (Kai low-latency routing vs Lux hybrid linear-attention reasoning).
5. **Given** a matrix row under evaluation, **When** examples are processed, **Then** only that row’s engine is the variable engine under test (sequential exclusive among matrix rows), the fixed partner may co-run, and Stage 1 and Stage 2 for each example still execute in one end-to-end agentic process.
6. **Given** a Stage-1-only matrix row (e.g., AnyJev), **When** an example runs, **Then** Stage 2 is served by the fixed CLM-8B partner; Stage-2 metrics for that row are attributed to the partner and Stage-1 metrics to the variable engine.

---

### User Story 3 - Wire Engines into the Agentic Pipeline (Priority: P1)

An evaluation operator runs the existing agentic FinAgentBench pipeline so that Stage 1 and Stage 2 decisions come from a selected real decision engine (not a lexical mock), while final answer synthesis uses Gemini only after local ranking completes.

**Why this priority**: Serving engines in isolation is insufficient; they must drive the production agent loop.

**Independent Test**: With mock System-1 disabled and a healthy engine selected, process a small sample end-to-end through Stage 1 → Stage 2 → (optional) Gemini synthesis and confirm traces show the selected engine’s decisions.

**Acceptance Scenarios**:

1. **Given** selected Stage-1 and Stage-2 engine bindings (same or different configurations) and mock System-1 disabled, **When** an example is processed, **Then** Stage 1 and Stage 2 rankings are produced by those bound local engines before any Gemini call.
2. **Given** ranking-complete results, **When** synthesis is enabled, **Then** System-2 uses Gemini exclusively and never falls back to extractive/local text concatenation.
3. **Given** Gemini credentials or the Gemini service are unavailable, **When** synthesis is required, **Then** the example is marked synthesis-failed/retriable (fail closed) without fabricating an answer from raw chunks.

---

### User Story 4 - Full Dataset and Random Sample Modes (Priority: P2)

An evaluation operator can run the benchmark against the full FinAgentBench set or against a small random sample of records for fast integration testing of model wiring.

**Why this priority**: Full runs are required for published comparisons; sample mode is required for safe iteration on the Nano.

**Independent Test**: Run with sample size N and verify exactly N examples (or fewer if dataset smaller) are processed; run without sample and verify full-set iteration is attempted.

**Acceptance Scenarios**:

1. **Given** a requested random sample size N, **When** the benchmark starts, **Then** it selects N examples uniformly at random (with optional fixed seed for reproducibility) and processes only those.
2. **Given** no sample limit, **When** the benchmark starts, **Then** it targets the full FinAgentBench labeled set.
3. **Given** a sample run completes, **When** the operator inspects outputs, **Then** engine identity, sample seed/size, and metrics are recorded for that run.

---

### User Story 5 - Publish Comparable Engine Reports (Priority: P3)

An evaluation operator exports a matrix report that lets them compare engines on quality and operational metrics side by side for the same dataset slice.

**Why this priority**: Comparison value depends on a clear export; ranking correctness and serving come first.

**Independent Test**: After a multi-engine sample run, export a single report containing one row (or section) per engine configuration with shared metric columns.

**Acceptance Scenarios**:

1. **Given** completed runs for two or more engines on the same sample seed, **When** the operator exports the matrix report, **Then** each engine appears with Stage-1/Stage-2 metrics, latency summaries, and synthesis/answer-score summaries.
2. **Given** an engine that does not support a given stage, **When** the report is generated, **Then** that stage is marked unsupported/skipped with reason rather than inventing scores.

### Edge Cases

- Engine process up but decision API returns malformed ranking/distribution: fail the example; do not coerce into a fake ranking.
- Autoregressive baseline emits invalid JSON: count as parse failure; do not silently accept free text as a structured choice.
- Sample size larger than dataset: process entire dataset and record that the sample was capped.
- Held-out calibration set (200 examples) unavailable for AnyJev L1: fail configuration startup with clear reason (do not silently skip calibration).
- Gemini rate limit during synthesis: preserve ranking-complete results; mark synthesis retriable; never extractive fallback.
- Concurrent matrix jobs for the same run identity: single-writer ledger/lease semantics remain enforced.
- Laya CPU-only host: allow degraded performance mode but still produce valid decision outputs and latency measurements.
- Matrix must not split Stage 1 and Stage 2 into separate offline batch jobs; both stages run in one agentic process even when engine servers are swapped between sequential matrix rows.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide operable serving for each matrix engine family: AnyJev L0, AnyJev L1, CLM-8B Action Cache, vLLM-sr Decision-2.0 Kai, vLLM-sr Decision-2.0 Lux, Laya (ModernBERT 421M), and Autoregressive Qwen3-8B-Instruct baseline.
- **FR-002**: System MUST expose health checks for each started engine configuration before benchmark or pipeline use.
- **FR-003**: System MUST integrate selected engine configurations into the agentic FinAgentBench pipeline for Stage 1 and/or Stage 2 decisions according to each engine’s supported primitives (Choice, Score/Action Cache, or JSON choice baseline).
- **FR-018**: System MUST support per-stage pipeline binding so Stage 1 and Stage 2 MAY use different engine configurations in one run; binding both stages to the same configuration MUST also be supported.
- **FR-019**: Matrix evaluation MUST be sequential exclusive for the variable engine under test (only one matrix-row engine varied at a time); the fixed Stage partner MAY run concurrently so Stage 1 and Stage 2 can complete in one agentic process.
- **FR-020**: For every benchmark or pipeline example, Stage 1 and Stage 2 MUST execute together in a single end-to-end agentic process (not as disconnected offline ranking jobs).
- **FR-021**: Matrix rows for Stage-1-only engines MUST bind Stage 2 to the fixed CLM-8B Action Cache partner; matrix rows for Stage-2-only engines MUST bind Stage 1 to a designated default Choice partner; reports MUST attribute each stage’s metrics to the engine that produced that stage.
- **FR-004**: System MUST disable lexical/mock System-1 scoring for official matrix and pipeline runs that claim real-engine results.
- **FR-005**: System MUST evaluate AnyJev L0 with adaptive cyclic shifts and AnyJev L1 with temperature scaling calibrated on a held-out set of 200 examples, reporting L0 and L1 as separate configurations.
- **FR-006**: System MUST evaluate CLM-8B using pre-computed action embeddings and Action Cache similarity scoring over the candidate space.
- **FR-007**: System MUST evaluate vLLM-sr Decision-2.0 Kai (low-latency operational routing) and Lux (hybrid linear-attention reasoning) as separate configurations.
- **FR-008**: System MUST evaluate Laya locally to establish edge CPU/GPU performance baselines with recorded latency.
- **FR-009**: System MUST evaluate the autoregressive instruct baseline by prompting for structured JSON choices and recording generation latency, parse failure rate, and log-probability calibration.
- **FR-010**: System MUST compute and persist FinAgentBench Stage-1 and Stage-2 ranking metrics (nDCG@5, MAP@5, MRR@5) per engine where the engine participates in that stage.
- **FR-011**: System MUST support full FinAgentBench dataset runs and random sample runs with configurable sample size and optional reproducibility seed.
- **FR-012**: System MUST use Gemini exclusively for System-2 final answer synthesis; extractive or local non-Gemini answer fabrication is forbidden.
- **FR-023**: Default System-2 model MUST be Gemini Flash; operators MAY select Gemini Pro (or another allowed Gemini id) per run, and the chosen model id MUST be recorded in run config and traces.
- **FR-013**: System MUST fail closed when Gemini is unavailable or errors during required synthesis (ranking progress may be preserved; no fake answers).
- **FR-014**: System MUST fail closed when required local decision engines are unhealthy (no cloud substitution for Stage 1/Stage 2 ranking).
- **FR-015**: Operators MUST be able to select which matrix configuration(s) to run and export a comparative matrix report for completed engines on a shared dataset slice.
- **FR-022**: Default matrix runs MUST execute the full agentic pipeline including fail-closed Gemini System-2 synthesis and answer scoring for each example; an explicit opt-out MAY disable synthesis for debugging only and MUST be recorded in run config.
- **FR-016**: System MUST record engine identity, model revision/config variant (e.g., L0/L1, Kai/Lux), latency, and decision distributions/scores in run traces for auditability.
- **FR-017**: Benchmark and pipeline runs MUST remain compatible with atomic resume semantics for long FinAgentBench executions.

### Key Entities

- **Engine Configuration**: A named matrix row (e.g., AnyJev-L0, AnyJev-L1, CLM-8B, Decision-2.0-Kai, Decision-2.0-Lux, Laya, AR-Qwen3-8B-Instruct) with primitives, endpoints, and calibration settings.
- **Calibration Set**: Held-out 200-example set used for AnyJev L1 temperature scaling.
- **Action Cache**: Pre-computed candidate embeddings used by CLM-8B for similarity scoring.
- **Matrix Run**: Evaluation over a dataset slice for one or more engine configurations with shared seed/sample parameters.
- **Engine Metrics Record**: Per-engine Stage-1/Stage-2 quality metrics plus latency/parse/calibration operational metrics.
- **Pipeline Binding**: Mapping from Stage 1 and Stage 2 agent steps to concrete engine configurations for a run (independent per stage; may be identical).
- **Fixed Stage Partner**: Default partner engines used when a matrix row under test does not cover both stages (Stage-2 partner = CLM-8B; Stage-1 partner = designated Choice engine).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of matrix engine configurations declared in scope have a documented start/health/decision validation path that an operator can execute on the target station.
- **SC-002**: A sample matrix run of at least 50 FinAgentBench examples produces Stage ranking metric triples for every engine that claims Stage-1 or Stage-2 support (or an explicit unsupported/skipped reason) and, under default settings, attempts Gemini synthesis for each processed example.
- **SC-003**: With mock System-1 disabled and a healthy engine selected, 0% of processed examples use mock/lexical rankings in traces.
- **SC-004**: When Gemini credentials are removed and synthesis is required, 0% of examples receive extractive/non-Gemini fabricated answers; all such examples end synthesis-failed or synthesis-retriable.
- **SC-010**: Under default configuration with credentials present, synthesis calls use Gemini Flash unless the operator overrides the model for that run.
- **SC-005**: Random sample mode with seed S and size N processes the same example IDs on repeat runs (reproducible sampling).
- **SC-006**: Autoregressive baseline runs report parse failure rate and mean generation latency for 100% of attempted examples in the sample.
- **SC-007**: Operators can export one comparative report covering ≥2 engines evaluated on the same sample seed with aligned metric columns.
- **SC-008**: A smoke integration of one real engine + Gemini fail-closed path completes a ≥20-example sample with ≥95% examples reaching a terminal ledger state.
- **SC-009**: In a matrix run over ≥2 variable engine rows, at most one variable matrix engine is under test at a time (fixed partner may co-run), and each example’s trace still contains both Stage 1 and Stage 2 within one agentic execution.

## Assumptions

- Target hardware remains HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64) unless an engine is explicitly marked edge-CPU capable (Laya).
- Base model weights for Qwen3-8B, Kai-0.6B, Lux-9B, ModernBERT 421M, and Qwen3-8B-Instruct are available to the operator (licensing/download outside repo scope).
- Serving stacks referenced by the brief are the intended runtimes: anyjev over local vLLM for AnyJev; clm-serve with vLLM pooling runner for CLM-8B; native vLLM feature-extraction endpoints for Decision-2.0; Hugging Face Transformers pipelines for Laya; instruct generation endpoint for the AR baseline.
- Stage participation defaults: Choice-oriented engines primarily Stage 1; CLM-8B Action Cache primarily Stage 2; Decision-2.0 Kai/Lux and AnyJev as configured for Choice; AR baseline Stage 1 JSON choices unless extended; operators bind stages independently per run.
- Pipeline runs use per-stage engine binding (mix-and-match allowed); same-engine for both stages remains a valid binding.
- Variable matrix engines run sequentially (one under test at a time); fixed Stage partner may co-run; Stage 1+2 remain one agentic end-to-end process per example.
- Fixed partners: Stage-1-only matrix rows use CLM-8B for Stage 2; Stage-2-only rows use a designated Choice engine for Stage 1 (named at plan time; AnyJev-L0 recommended default).
- Default matrix profile is full pipeline (Stage 1 + Stage 2 + Gemini synthesis + answer scoring); synthesis opt-out is debug-only and must be flagged in run config.
- Default Gemini model is Flash; Pro is opt-in per run.
- AnyJev L1 calibration uses a fixed held-out 200-example split from FinAgentBench (or an operator-provided calibration file with the same cardinality).
- Existing FinAgentBench harness ledger, two-stage retrieval contract (Top-1 Stage-1 → Stage 2), and AgentGateway/MCP tool path remain in force; this feature extends System-1 serving/benchmarking and System-2 fail-closed Gemini behavior.
- Constitution v1.1.0 applies (local System-1 first, ARM64 containers, MCP isolation, auto-resume, trace completeness, deterministic finance math, two-stage retrieval).
- Out of scope: training/finetuning new decision weights from scratch; non-FinAgentBench corpora; replacing Gemini with alternate System-2 providers.
