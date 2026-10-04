---
description: "Task list for FinAgentBench hybrid evaluation harness"
---

# Tasks: FinAgentBench Hybrid Evaluation Harness

**Input**: Design documents from `/specs/001-finagentbench-harness/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not explicitly requested as TDD in the feature specification — no dedicated test-first tasks. Validate via each story’s Independent Test and `quickstart.md` scenarios during Polish.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/finagent_mesh/`, `mcp_servers/`, `containers/`, `scripts/`, `tests/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and package layout

- [x] T001 Create directory tree per plan.md: `src/finagent_mesh/{dataset,metrics,ledger,clients,gateway,agent/nodes,scoring,runtime}/`, `mcp_servers/{mcp_sec_edgar,mcp_financial_calculator}/`, `containers/{vllm-sr,anyjev,clm-8b}/`, `scripts/`, `tests/{unit,integration,contract}/`
- [x] T002 Add package markers `src/finagent_mesh/__init__.py` and empty `__init__.py` files under each `src/finagent_mesh/*` package path
- [x] T003 Declare runtime dependencies in `pyproject.toml` via uv: `langgraph`, `langchain-core`, `langchain-google-genai`, `mcp`, `mlflow`, `httpx`, `numpy`, `pydantic`, `python-dotenv`, `typer` (or argparse), and dev deps `pytest`, `pytest-asyncio`
- [x] T004 [P] Create `.env.example` documenting `FINAGENTBENCH_PATH`, `EVAL_LEDGER_PATH`, `SYSTEMONE_STAGE1_URL`, `SYSTEMONE_STAGE2_URL`, `AGENT_GATEWAY_URL`, `GOOGLE_API_KEY`, `GEMINI_MODEL`, `SYNTHESIS_K`, `HARNESS_MAX_ATTEMPTS`, `MLFLOW_TRACKING_URI`, `PODMAN_OR_DOCKER` per `specs/001-finagentbench-harness/contracts/harness-cli.md`
- [x] T005 [P] Update `README.md` with uv setup, feature pointer to `specs/001-finagentbench-harness/`, and ZGX Nano/ARM64 notes

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared config, domain types, clients interfaces, and health primitives required by all stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement env-backed settings in `src/finagent_mesh/config.py` with defaults `SYNTHESIS_K=5`, `HARNESS_MAX_ATTEMPTS=3`, Stage1 URL `http://localhost:8000`, Stage2 URL `http://localhost:8001`, ledger path `./eval_ledger.db`
- [x] T007 [P] Define shared Pydantic/dataclass domain types in `src/finagent_mesh/agent/state.py` for `BenchmarkExample` (fields: `example_id`, `firm_id`, `query_text`, `query_category`, `stage1_labels`, `stage2_labels`, `answer_label` nullable), `DocumentTypeCandidate` (`doc_type` ∈ {10-K,10-Q,8-K,Earnings,DEF14A}, `score`, `rank`), `PassageChunk` (`chunk_id`, `doc_type`, `text`, `is_table`, `score`, `rank`), and LangGraph run state
- [x] T008 [P] Define document-type enum constant `DOC_TYPES = ("10-K","10-Q","8-K","Earnings","DEF14A")` and Top-1 Stage-2 selection helper stub in `src/finagent_mesh/agent/nodes/__init__.py` (or `src/finagent_mesh/agent/types.py` if cleaner)
- [x] T009 Implement `OpenDecisionClient` skeleton in `src/finagent_mesh/clients/open_decision.py` matching `specs/001-finagentbench-harness/contracts/systemone-openapi.yaml` (`POST /v1/systemone` with primitives `choice|score|action_cache`; return `ranking` + `distribution`)
- [x] T010 [P] Implement System-1 health check helper in `src/finagent_mesh/runtime/health.py` for `GET {base}/healthz` on Stage1 and Stage2 URLs
- [x] T011 [P] Implement AgentGateway MCP client stub in `src/finagent_mesh/gateway/mcp_gateway.py` that routes tool calls only through `AGENT_GATEWAY_URL` (no direct tool bypass)
- [x] T012 Create CLI scaffold in `scripts/run_harness.py` with subcommands `run`, `export-metrics`, `status` per `contracts/harness-cli.md`, delegating to `src/finagent_mesh/runtime/harness.py` stubs
- [x] T013 Implement FinAgentBench dataset loader in `src/finagent_mesh/dataset/finagentbench.py` supporting `FINAGENTBENCH_PATH`, full iteration, and `--limit`/sample mode; validate label doc types ⊆ `DOC_TYPES`

**Checkpoint**: Foundation ready — user story implementation can now begin

---

## Phase 3: User Story 1 - Two-Stage Ranking & Answer Scoring (Priority: P1) 🎯 MVP

**Goal**: Run Stage 1 document-type ranking and Stage 2 Top-1 chunk ranking, compute nDCG@5/MAP@5/MRR@5 for both stages, synthesize over top-5 chunks when enabled, and score answers (normalized EM + token F1)

**Independent Test**: Run a small labeled subset with `--skip-synthesis` and verify Stage-1/Stage-2 metric triples; with synthesis on, verify answer scores when labels exist

### Implementation for User Story 1

- [x] T014 [P] [US1] Implement pure ranking metrics `ndcg_at_k`, `map_at_k`, `mrr_at_k` (k=5) with stable tie-break (score desc, id asc) in `src/finagent_mesh/metrics/ranking.py`
- [x] T015 [P] [US1] Implement answer scorers normalized exact match (official) and token F1 (diagnostic) in `src/finagent_mesh/metrics/answer.py`
- [x] T016 [P] [US1] Implement Stage 1 Choice node in `src/finagent_mesh/agent/nodes/stage1.py` ranking exactly {10-K,10-Q,8-K,Earnings,DEF14A} via `OpenDecisionClient` primitive `choice`
- [x] T017 [US1] Implement Stage 2 Score/Action-Cache node in `src/finagent_mesh/agent/nodes/stage2.py` ranking chunks only from Top-1 Stage-1 `doc_type` (MUST NOT pool multiple types)
- [x] T018 [US1] Implement metrics node in `src/finagent_mesh/agent/nodes/metrics_node.py` persisting `StageRankingResult` fields `ndcg_at_5`, `map_at_5`, `mrr_at_5` for `stage1` and `stage2`
- [x] T019 [P] [US1] Implement Gemini synthesis client wrapper in `src/finagent_mesh/clients/gemini.py` using `langchain-google-genai` with `GEMINI_MODEL` default Flash
- [x] T020 [US1] Implement synthesize node in `src/finagent_mesh/agent/nodes/synthesize.py` passing top-K Stage-2 chunks with default `K=5` from config
- [x] T021 [US1] Implement answer-score node in `src/finagent_mesh/agent/nodes/answer_score.py` writing `AnswerScore` (`normalized_em`, `token_f1`, `status` ∈ {scored, skipped_no_label})
- [x] T022 [US1] Wire LangGraph graph in `src/finagent_mesh/agent/graph.py`: Stage1 → Stage2 → metrics → (optional synthesize → answer_score); support `--skip-synthesis`
- [x] T023 [US1] Implement in-memory/run-local result sink in `src/finagent_mesh/scoring/run_aggregator.py` to collect per-example Stage-1/2 metrics and answer scores for export
- [x] T024 [US1] Connect `scripts/run_harness.py run --run-id … --limit N [--skip-synthesis]` to execute the graph over the dataset loader without requiring durable resume yet
- [x] T025 [US1] Handle edge cases in graph nodes: missing stage labels → skip metrics with reason; empty Top-1 chunks → structured failure and no synthesis; missing answer label → skip answer scoring with reason

**Checkpoint**: User Story 1 fully functional for ranking+metrics (+ optional synthesis/answer score) on a limited subset

---

## Phase 4: User Story 2 - Crash-Safe Auto-Resume (Priority: P1)

**Goal**: Atomic SQLite ledger with ranking-complete / synthesis-retriable semantics so restarts skip completed work and retry synthesis only when needed

**Independent Test**: Complete N examples, kill harness mid-run, relaunch same `--run-id`, confirm no re-rank of ranking-complete/completed and synthesis-only resume

### Implementation for User Story 2

- [x] T026 [US2] Implement SQLite ledger schema and WAL mode in `src/finagent_mesh/ledger/sqlite_ledger.py` for `EvaluationRun` (`run_id` PK, `created_at`, `config_json`, `status` ∈ {running,stopped,completed,failed}, `lease_owner`, `lease_expires_at`) and `LedgerEntry` composite PK (`run_id`,`example_id`)
- [x] T027 [US2] Implement ledger state machine transitions in `src/finagent_mesh/ledger/sqlite_ledger.py`: `pending` → `in_progress` → (`skipped_invalid` | `failed_retriable` | `ranking_complete` → (`synthesis_retriable` | `completed`)); transactional `BEGIN IMMEDIATE`
- [x] T028 [US2] Persist `ranking_payload_json` at `ranking_complete` and `synthesis_payload_json` on synthesis success in `src/finagent_mesh/ledger/sqlite_ledger.py`; resume MUST NOT re-run Stage 1/2 when `ranking_complete` or `synthesis_retriable`
- [x] T029 [US2] Implement single-writer lease acquire/release/steal-on-expiry in `src/finagent_mesh/ledger/sqlite_ledger.py`; second concurrent `run` for same `run_id` exits or waits with clear conflict
- [x] T030 [US2] Implement attempt counters `attempts_stage1`, `attempts_stage2`, `attempts_synthesis` with env `HARNESS_MAX_ATTEMPTS` default 3 in `src/finagent_mesh/runtime/harness.py`
- [x] T031 [US2] Integrate ledger into `src/finagent_mesh/runtime/harness.py`: skip `completed`; resume `synthesis_retriable` at synthesis only; process `pending`/`failed_retriable`/incomplete; mark terminal states
- [x] T032 [US2] Implement `scripts/run_harness.py status --run-id` showing ledger state counts and lease info
- [x] T033 [US2] Ensure partial crash mid-commit leaves example incomplete/retriable (no half-complete success) via transactional commits in `src/finagent_mesh/ledger/sqlite_ledger.py`

**Checkpoint**: Crash/resume and synthesis-only retry work for a named run

---

## Phase 5: User Story 3 - Local Guardrails Before Cloud (Priority: P2)

**Goal**: Stage 1/2 always use local System-1; fail closed if unhealthy; Gemini only after Stage 2 for top-K chunks

**Independent Test**: With cloud disabled after Stage 2, rankings/metrics still complete; with local engines down, no cloud-only ranking

### Implementation for User Story 3

- [x] T034 [US3] Complete `OpenDecisionClient` production HTTP path in `src/finagent_mesh/clients/open_decision.py` (timeouts, error mapping, distribution capture) against `:8000` Choice and `:8001` Score/Action-Cache
- [x] T035 [US3] Enforce pre-run and per-example health gates in `src/finagent_mesh/runtime/harness.py` using `src/finagent_mesh/runtime/health.py` — fail closed; never substitute Gemini for Stage 1/2
- [x] T036 [US3] Enforce graph ordering in `src/finagent_mesh/agent/graph.py` so synthesize node cannot run before Stage 2 + metrics commit path
- [x] T037 [US3] On local ranking timeout/OOM, retry up to `HARNESS_MAX_ATTEMPTS` then `failed_retriable` without cloud fallback in `src/finagent_mesh/runtime/harness.py`
- [x] T038 [US3] On Gemini rate-limit/auth failure after ranking-complete, mark `synthesis_retriable` and preserve Stage 1/2 payloads in `src/finagent_mesh/runtime/harness.py`

**Checkpoint**: Local-before-cloud and fail-closed behavior verified

---

## Phase 6: User Story 4 - ARM64 Container Build & Serve (Priority: P2)

**Goal**: Build native Grace Blackwell ARM64 images for vLLM-sr, AnyJev, CLM-8B and serve System-1 on ports 8000/8001

**Independent Test**: Run build automation on target station; confirm `/healthz` on both ports before examples run

### Implementation for User Story 4

- [x] T039 [P] [US4] Author `containers/vllm-sr/Containerfile` (or Dockerfile) targeting `linux/arm64` with NVIDIA container runtime hooks for Decision-2.0 / Stage-1 Choice serving
- [x] T040 [P] [US4] Author `containers/anyjev/Containerfile` for AnyJev L0/L1 Stage-1 Choice serving on ARM64
- [x] T041 [P] [US4] Author `containers/clm-8b/Containerfile` for CLM-8B Stage-2 Score/Action-Cache serving on ARM64
- [x] T042 [US4] Implement `scripts/build_containers.sh` preferring Podman with `nvidia-container-toolkit`, fallback `docker buildx`, always `--platform linux/arm64`
- [x] T043 [US4] Document/start mapping in `scripts/build_containers.sh` (or companion start section) so Stage-1 engines expose `http://localhost:8000` and Stage-2 `http://localhost:8001` per FR-006
- [x] T044 [US4] Wire harness startup health wait in `src/finagent_mesh/runtime/harness.py` so evaluation does not begin until required local services are healthy (or records clear startup failure)

**Checkpoint**: Build/start path yields healthy `:8000` and `:8001` on ZGX Nano

---

## Phase 7: User Story 5 - MCP Filings & Deterministic Finance Math (Priority: P2)

**Goal**: Governed `mcp-sec-edgar` and `mcp-financial-calculator` tools via AgentGateway; tables preserved as single chunks; no model-invented numerics

**Independent Test**: Fetch/extract known filing chunks; calculator IRR/NPV/ratio cases return exact deterministic values through gateway

### Implementation for User Story 5

- [x] T045 [P] [US5] Implement `mcp_servers/mcp_sec_edgar` MCP server tools `list_document_types`, `fetch_filing`, `extract_chunks` per `specs/001-finagentbench-harness/contracts/mcp-sec-edgar.json` (tables → `is_table=true` single units)
- [x] T046 [P] [US5] Implement `mcp_servers/mcp_financial_calculator` MCP server tools `compute_irr`, `compute_npv`, `amortization_schedule`, `ratio_analysis` per `specs/001-finagentbench-harness/contracts/mcp-financial-calculator.json`
- [x] T047 [US5] Complete `src/finagent_mesh/gateway/mcp_gateway.py` to invoke both servers only via AgentGateway with schema validation, access control, and rate-limit error surfacing
- [x] T048 [US5] Implement tool nodes in `src/finagent_mesh/agent/nodes/tools.py` for filing fetch/chunk extract used by Stage 1/2 preparation and calculator calls during synthesis/tool use
- [x] T049 [US5] Record `ToolInvocationRecord` fields (`tool_name`, `request_json`, `response_summary`, `status`, `latency_ms`) into run traces/ledger side channel from `src/finagent_mesh/agent/nodes/tools.py`
- [x] T050 [US5] Enforce constitution rule in synthesize/tool path: IRR/NPV/amortization/ratio numerics accepted only from calculator tool results in `src/finagent_mesh/agent/nodes/synthesize.py` / tool policy helper

**Checkpoint**: Filing+chunk and calculator paths work exclusively through MCP/gateway

---

## Phase 8: User Story 6 - Trace Completeness (Priority: P3)

**Goal**: MLflow traces reconstruct LangGraph transitions, System-1 distributions, tool calls, rankings, metrics, synthesis, and answer scores

**Independent Test**: Smoke ≥20 examples; reconstruct Stage-1/2 orderings, tools, and answers from traces alone

### Implementation for User Story 6

- [x] T051 [US6] Configure MLflow tracking in `src/finagent_mesh/runtime/harness.py` using `MLFLOW_TRACKING_URI` and per-`run_id` parent runs
- [x] T052 [US6] Instrument LangGraph node spans in `src/finagent_mesh/agent/graph.py` (or node wrappers) for stage1, stage2, metrics, tools, synthesize, answer_score
- [x] T053 [US6] Log System-1 `distribution` / score vectors from Stage 1/2 nodes into MLflow in `src/finagent_mesh/agent/nodes/stage1.py` and `stage2.py`
- [x] T054 [US6] Log tool invocations, rankings, metric triples, synthesis text, and answer scores as MLflow metrics/artifacts from respective nodes
- [x] T055 [US6] Persist `TraceRecord` linkage (`mlflow_run_id`, span names) alongside ledger entries in `src/finagent_mesh/ledger/sqlite_ledger.py` or thin `src/finagent_mesh/runtime/tracing.py`
- [x] T056 [US6] Ensure failed examples record failure reason and resume eligibility in both ledger `last_error` and MLflow tags

**Checkpoint**: Trace auditability meets SC-007 for smoke runs

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Export UX, docs, and quickstart validation across stories

- [x] T057 Implement `export-metrics` in `scripts/run_harness.py` + `src/finagent_mesh/scoring/run_aggregator.py` emitting Stage-1/2 aggregate nDCG@5/MAP@5/MRR@5 and answer normalized-EM / token-F1 summaries
- [x] T058 [P] Add unit tests for ranking metrics and answer scoring in `tests/unit/test_ranking_metrics.py` and `tests/unit/test_answer_metrics.py` (determinism / golden vectors)
- [x] T059 [P] Add contract smoke tests validating request/response shapes against `specs/001-finagentbench-harness/contracts/systemone-openapi.yaml` and MCP JSON contracts under `tests/contract/`
- [x] T060 [P] Refresh `README.md` with quickstart link to `specs/001-finagentbench-harness/quickstart.md` and constitution-aligned run instructions
- [x] T061 Run end-to-end validation scenarios from `specs/001-finagentbench-harness/quickstart.md` (smoke rank-only, e2e 100, crash-resume, fail-closed, golden metrics) and record gaps as follow-ups
- [x] T062 Add `eval_ledger.db`, `mlruns/`, and local dataset paths to `.gitignore` if not already ignored

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; integrates with US1 graph execution (ledger wraps harness)
- **US3 (Phase 5)**: After Foundational; hardens US1 clients/ordering; ideally after US2 for fail states
- **US4 (Phase 6)**: After Foundational; can parallel US5; needed for real System-1 on hardware
- **US5 (Phase 7)**: After Foundational; can parallel US4; feeds real chunks into US1 Stage 2
- **US6 (Phase 8)**: After US1 graph exists; best after US2–US5 for full span coverage
- **Polish (Phase 9)**: After desired stories complete

### User Story Dependencies

- **US1 (P1)**: After Foundational — independently testable with mocked System-1 + fixture chunks
- **US2 (P1)**: After Foundational — independently testable with harness+ledger even if synthesis mocked
- **US3 (P2)**: After Foundational — depends on US1 graph nodes for ordering proof
- **US4 (P2)**: After Foundational — independently testable via build/health only
- **US5 (P2)**: After Foundational — independently testable via gateway tool calls
- **US6 (P3)**: After US1 (needs spans); stronger with US2/US5 integrated

### Within Each User Story

- Models/types before nodes/services
- Nodes before graph/harness wiring
- Core path before edge-case handling
- Story complete before next priority when staffing is serial

### Parallel Opportunities

- Phase 1: T004, T005 in parallel after T001–T003
- Phase 2: T007, T008, T010, T011 in parallel after T006
- US1: T014, T015, T016, T019 in parallel; then T017–T025 sequentially as needed
- US4: T039, T040, T041 in parallel
- US5: T045, T046 in parallel
- After Foundational: US4 and US5 can proceed in parallel with US1/US2 on separate owners

---

## Parallel Example: User Story 1

```bash
# Parallel metric + client stubs:
Task: "Implement ranking metrics in src/finagent_mesh/metrics/ranking.py"
Task: "Implement answer scorers in src/finagent_mesh/metrics/answer.py"
Task: "Implement Stage 1 node in src/finagent_mesh/agent/nodes/stage1.py"
Task: "Implement Gemini wrapper in src/finagent_mesh/clients/gemini.py"

# Then sequential graph wiring:
Task: "Implement Stage 2 Top-1 node in src/finagent_mesh/agent/nodes/stage2.py"
Task: "Wire LangGraph in src/finagent_mesh/agent/graph.py"
Task: "Connect scripts/run_harness.py run path"
```

## Parallel Example: User Story 4 + 5

```bash
Task: "Author containers/vllm-sr/Containerfile"
Task: "Author containers/anyjev/Containerfile"
Task: "Author containers/clm-8b/Containerfile"
Task: "Implement mcp_servers/mcp_sec_edgar per contracts/mcp-sec-edgar.json"
Task: "Implement mcp_servers/mcp_financial_calculator per contracts/mcp-financial-calculator.json"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (ranking metrics + optional synthesis/answer score on `--limit`)
4. **STOP and VALIDATE** with `--skip-synthesis` on a small labeled subset
5. Demo Stage-1/Stage-2 metric export

### Incremental Delivery

1. Setup + Foundational → foundation ready
2. US1 → ranking MVP
3. US2 → crash-safe full runs
4. US3 → local-before-cloud enforcement
5. US4 → real ARM64 engines on Nano
6. US5 → real filings + calculator tools
7. US6 → full MLflow auditability
8. Polish → quickstart sign-off

### Parallel Team Strategy

1. Team completes Setup + Foundational together
2. Then:
   - Dev A: US1 → US2 → US3
   - Dev B: US4
   - Dev C: US5 → join US1 chunk path
   - Dev A/C: US6 after graph+tools exist

---

## Notes

- [P] tasks = different files, no dependencies on incomplete sibling tasks
- [USn] maps to spec user stories 1–6
- Constitution v1.1.0 constraints are non-negotiable in all phases
- Commit after each task or logical group
- Stop at checkpoints to validate stories independently
- Exact env/CLI contracts: `specs/001-finagentbench-harness/contracts/harness-cli.md`
