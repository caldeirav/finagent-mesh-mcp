---
description: "Task list for decision model serving and benchmark matrix"
---

# Tasks: Decision Model Serving & Benchmark Matrix

**Input**: Design documents from `/specs/002-decision-model-bench/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested as TDD in the feature specification. Plan names contract/unit/integration checks — include those as Polish validation tasks (not test-first). Primary validation: each story’s Independent Test + `quickstart.md`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/finagent_mesh/`, `containers/`, `scripts/`, `configs/`, `tests/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Layout, registry config, env, and package scaffolding for engines/matrix

- [x] T001 Create directories `src/finagent_mesh/clients/engines/`, `src/finagent_mesh/matrix/`, `containers/laya/`, `containers/ar-qwen3-instruct/`, `configs/calibration/`, `artifacts/` per plan.md
- [x] T002 [P] Add package markers `src/finagent_mesh/clients/engines/__init__.py` and `src/finagent_mesh/matrix/__init__.py`
- [x] T003 Install engine registry at `configs/engines.yaml` from `specs/002-decision-model-bench/contracts/engines-registry.yaml` (seven `config_id`s; partners `stage2_partner_id=clm-8b`, `stage1_partner_id=anyjev-l0`; ports 8000/8001/8002)
- [x] T004 [P] Create calibration placeholder `configs/calibration/anyjev_l1_heldout.json` with schema `{ "calibration_id": "anyjev_l1_heldout", "example_ids": [], "source": "..." }` and document that L1 start requires exactly 200 IDs
- [x] T005 [P] Extend `.env.example` with `SYSTEMONE_MOCK=0` (official default), `ENGINES_REGISTRY_PATH=./configs/engines.yaml`, weight vars `ANYJEV_WEIGHTS`, `CLM8B_WEIGHTS`, `DECISION20_KAI_WEIGHTS`, `DECISION20_LUX_WEIGHTS`, `LAYA_WEIGHTS`, `AR_QWEN3_WEIGHTS` per `contracts/matrix-cli.md`
- [x] T006 [P] Declare optional GPU/edge deps in `pyproject.toml` (or extras): `transformers`, `torch` notes for Laya; keep existing harness deps

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Registry, binding types, fail-closed Gemini, mock gate, multi-engine health — MUST complete before story work

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Implement `EngineConfiguration` loader in `src/finagent_mesh/clients/engines/registry.py` from `configs/engines.yaml` with fields `config_id` (unique PK), `family`, `display_name`, `primitives`, `primary_stages`, `base_url`, `health_path` default `/healthz`, `decide_path` default `/v1/systemone`, `container_ref`, `weights_ref`, `calibration_ref` nullable, `is_heavy_gpu`, `is_light_edge`, `model_revision`
- [x] T008 [P] Implement `FixedStagePartners` helpers in `src/finagent_mesh/matrix/partners.py` with defaults Stage-2 partner `clm-8b` and Stage-1 partner `anyjev-l0` and matrix row binding rules from `data-model.md`
- [x] T009 [P] Add `PipelineBinding` / `MatrixRun` / `MatrixRowResult` / `EngineMetricsRecord` dataclasses (or Pydantic models) in `src/finagent_mesh/matrix/models.py` with status enums `pending|running|completed|failed` and metrics fields from `data-model.md`
- [x] T010 Remove extractive/offline chunk-head fallback from `src/finagent_mesh/clients/gemini.py`: missing `GOOGLE_API_KEY` or API errors MUST raise (fail closed); never fabricate answers from raw chunks
- [x] T011 Enforce official mock disable in `src/finagent_mesh/config.py` and `src/finagent_mesh/runtime/harness.py`: refuse start when `SYSTEMONE_MOCK` truthy unless `--allow-mock` (record `systemone_mock` in run config)
- [x] T012 Extend `src/finagent_mesh/runtime/health.py` to health-check arbitrary engine `base_url`+`health_path` lists (variable + partner) and fail closed on any unhealthy required engine
- [x] T013 [P] Implement seeded sampling helper in `src/finagent_mesh/matrix/sampling.py` using `random.Random(seed).sample` over example IDs; persist `sample_seed`, `sample_size`, `selected_example_ids`; if sample size > dataset size, process entire dataset and record capped
- [x] T014 Scaffold `scripts/serve_engine.sh` with `start|stop|health <config_id>` resolving registry entries (stub start OK until US1 fills real serve)
- [x] T015 Scaffold `scripts/run_matrix.py` Typer CLI with subcommands `run`, `export`, `status` per `contracts/matrix-cli.md` delegating to `src/finagent_mesh/matrix/` stubs

**Checkpoint**: Foundation ready — user story implementation can begin

---

## Phase 3: User Story 1 - Serve and Health-Check Decision Engines (Priority: P1) 🎯 MVP

**Goal**: Operable, health-checked local serving for all seven matrix engine configurations; unhealthy engines cause fail-closed ranking (no silent mock invent)

**Independent Test**: Start one engine config, verify `/healthz` + one `/v1/systemone` decision; stop engine and confirm harness fails closed for ranking

### Implementation for User Story 1

- [x] T016 [P] [US1] Replace placeholder serve path in `containers/anyjev/Containerfile` (+ entrypoint/scripts as needed) for AnyJev L0/L1 Choice on ARM64 exposing `/healthz` and `/v1/systemone`
- [x] T017 [P] [US1] Replace placeholder serve path in `containers/clm-8b/Containerfile` for CLM-8B Action Cache / Score on ARM64 (`vllm serve … --runner pooling` / clm-serve as researched)
- [x] T018 [P] [US1] Replace placeholder serve path in `containers/vllm-sr/Containerfile` supporting Decision-2.0 Kai and Lux variants via env/weights
- [x] T019 [P] [US1] Author `containers/laya/Containerfile` (or local process serve) for Laya ModernBERT 421M Choice baseline with latency recording
- [x] T020 [P] [US1] Author `containers/ar-qwen3-instruct/Containerfile` for AR Qwen3-8B-Instruct JSON-choice baseline
- [x] T021 [US1] Extend `scripts/build_containers.sh` to build all five engine families for `linux/arm64` (Podman preferred)
- [x] T022 [US1] Complete `scripts/serve_engine.sh` start/stop/health: map ports per registry; when variable is `clm-8b`, bind Stage-1 partner `anyjev-l0` to `:8000` and CLM to `:8001`
- [x] T023 [US1] Enforce AnyJev L1 calibration gate in `scripts/serve_engine.sh` and/or `src/finagent_mesh/clients/engines/anyjev.py`: refuse start if `calibration_ref` missing or `example_ids` length ≠ 200
- [x] T024 [P] [US1] Implement AnyJev adapter in `src/finagent_mesh/clients/engines/anyjev.py` translating native API → OpenAPI `choice` with `engine`/`model_revision` for `anyjev-l0` and `anyjev-l1`
- [x] T025 [P] [US1] Implement CLM-8B adapter in `src/finagent_mesh/clients/engines/clm8b.py` for primitives `score` and `action_cache` using Action Cache embeddings
- [x] T026 [P] [US1] Implement vLLM-sr adapter in `src/finagent_mesh/clients/engines/vllm_sr.py` for `decision20-kai` and `decision20-lux` Choice
- [x] T027 [P] [US1] Implement Laya adapter in `src/finagent_mesh/clients/engines/laya.py` (Transformers path; allow CPU degraded mode; always record latency)
- [x] T028 [P] [US1] Implement AR baseline adapter in `src/finagent_mesh/clients/engines/ar_baseline.py`: prompt JSON `{"ordered_ids":[...],"scores":[...]}`; on parse failure set `parse_failure=1` and fail structured Stage-1 ranking; record generation latency (+ optional logprobs)
- [x] T029 [US1] Implement adapter factory in `src/finagent_mesh/clients/engines/registry.py` (or `factory.py`) returning a decide/health client for a `config_id` speaking `contracts/systemone-adapters.md`
- [x] T030 [US1] Wire factory into `OpenDecisionClient` or stage clients so selecting a config uses that engine’s `base_url` only (no silent cross-engine bleed) in `src/finagent_mesh/clients/open_decision.py`

**Checkpoint**: Operator can start/health/decide for each config_id; unhealthy → fail closed

---

## Phase 4: User Story 3 - Wire Engines into the Agentic Pipeline (Priority: P1)

**Goal**: Per-stage Stage-1/Stage-2 engine bindings drive one LangGraph process Stage 1→2→Gemini Flash; mock off; Gemini fail-closed only

**Independent Test**: With `SYSTEMONE_MOCK=0` and healthy bindings, process a small sample end-to-end; traces show bound engine ids; no extractive synthesis

### Implementation for User Story 3

- [x] T031 [US3] Extend `scripts/run_harness.py run` with `--stage1-engine`, `--stage2-engine`, `--gemini-model` (default `gemini-2.5-flash`), `--sample-size`, `--sample-seed`, `--allow-mock` per `contracts/matrix-cli.md`
- [x] T032 [US3] Apply `PipelineBinding` in `src/finagent_mesh/runtime/harness.py`: construct distinct Stage-1 and Stage-2 clients from registry; support same-config binding for both stages
- [x] T033 [US3] Update `src/finagent_mesh/agent/graph.py` / stage nodes so Stage 1 and Stage 2 use their bound clients and record `engine` + `model_revision` + latency in MLflow traces via `src/finagent_mesh/runtime/tracing.py`
- [x] T034 [US3] Ensure synthesize path uses Gemini exclusively after ranking-complete; on Gemini errors mark `synthesis_retriable` / failed without extractive fallback in `src/finagent_mesh/runtime/harness.py` and `src/finagent_mesh/agent/nodes/synthesize.py`
- [x] T035 [US3] Pre-run health-check both bound engines; if unhealthy, fail closed for ranking (no cloud Stage-1/2 substitution) in `src/finagent_mesh/runtime/harness.py`
- [x] T036 [US3] Persist binding + `gemini_model` + `synthesis_enabled` + `systemone_mock` in evaluation run `config_json` (ledger) for auditability

**Checkpoint**: Real engines drive agentic pipeline; Flash default; fail-closed Gemini verified

---

## Phase 5: User Story 2 - Benchmark Matrix Across Five Engine Families (Priority: P1)

**Goal**: Sequential exclusive matrix over seven configs with fixed partners; each example runs Stage 1+2+Gemini in one agentic process; metrics attributed to producing engines

**Independent Test**: Run matrix subset on seeded sample ≥50 examples; comparable per-engine metrics including synthesis/answer scores; traces show Stage 1+2 together

### Implementation for User Story 2

- [x] T037 [US2] Implement sequential orchestration in `src/finagent_mesh/matrix/runner.py`: for each variable engine stop previous variable → start V → ensure partner → health → bind stages via `partners.py` → run harness pipeline → record `MatrixRowResult`
- [x] T038 [US2] Enforce sequential exclusive variable engine (at most one variable heavy GPU under test); partner MAY co-run in `src/finagent_mesh/matrix/runner.py`
- [x] T039 [US2] Attribute Stage-1 metrics to `stage1_engine_id` and Stage-2 metrics to `stage2_engine_id` (partner attribution) when aggregating in `src/finagent_mesh/matrix/runner.py` / `src/finagent_mesh/scoring/run_aggregator.py`
- [x] T040 [US2] Wire `scripts/run_matrix.py run` to refuse mock without `--allow-mock`; default engines = all seven registry ids; default synthesis on (full pipeline); `--skip-synthesis` debug-only and recorded
- [x] T041 [US2] Reuse one seeded `selected_example_ids` list across all matrix rows in a `MatrixRun` in `src/finagent_mesh/matrix/runner.py`
- [x] T042 [US2] Collect AR `parse_failure_rate` and latency percentiles into `EngineMetricsRecord` for `ar-qwen3-8b-instruct` rows
- [x] T043 [US2] Ensure AnyJev L0 vs L1 and Decision-2.0 Kai vs Lux remain distinct `variable_config_id` rows with distinct `model_revision` in matrix results
- [x] T044 [US2] Implement `scripts/run_matrix.py status --matrix-run-id` showing per-row status and partner ids

**Checkpoint**: Multi-row sample matrix completes with e2e Stage 1+2 per example and correct attribution

---

## Phase 6: User Story 4 - Full Dataset and Random Sample Modes (Priority: P2)

**Goal**: Full FinAgentBench runs and reproducible random samples for matrix and single pipeline

**Independent Test**: Sample size N + seed S → exactly N examples (or capped); omit sample → full-set iteration attempted; seed/size recorded

### Implementation for User Story 4

- [x] T045 [US4] Integrate `src/finagent_mesh/matrix/sampling.py` into `src/finagent_mesh/runtime/harness.py` so `--sample-size` / `--sample-seed` filter dataset before ledger init
- [x] T046 [US4] Persist `sample_seed`, `sample_size`, `selected_example_ids` on `MatrixRun` and pipeline run config; identical `(seed, size, dataset_version)` → identical IDs
- [x] T047 [US4] Support full-dataset mode (no sample flags) for both `scripts/run_harness.py` and `scripts/run_matrix.py` targeting the full labeled set
- [x] T048 [US4] Document sample vs full flags and reproducibility expectations in `README.md` (pointer to `specs/002-decision-model-bench/quickstart.md`)

**Checkpoint**: Sample and full modes work for harness and matrix

---

## Phase 7: User Story 5 - Publish Comparable Engine Reports (Priority: P3)

**Goal**: Export one comparative matrix report (JSON/CSV) with aligned metric columns per variable engine on a shared sample slice

**Independent Test**: After ≥2 engine rows on same seed, export single report with one section/row per engine and shared columns

### Implementation for User Story 5

- [x] T049 [US5] Implement report builder in `src/finagent_mesh/matrix/report.py` conforming to `specs/002-decision-model-bench/contracts/matrix-report.schema.json` (required fields: `matrix_run_id`, partners, `gemini_model`, `systemone_mock`, `synthesis_enabled`, `rows[]` with metrics)
- [x] T050 [US5] Implement `scripts/run_matrix.py export --matrix-run-id --out --format json|csv` writing comparative export under `artifacts/` by default
- [x] T051 [US5] For engines not participating in a stage, mark that stage unsupported/skipped with reason (null metrics + reason) rather than inventing scores in `src/finagent_mesh/matrix/report.py`
- [x] T052 [US5] Include latency p50/p95, synthesis attempt/fail counts, answer_normalized_em / answer_token_f1, and AR parse_failure_rate columns when applicable

**Checkpoint**: Operators can export side-by-side engine comparisons for a shared sample

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Plan-named validation tests, docs, and quickstart alignment

- [x] T053 [P] Add unit test `tests/unit/test_gemini_fail_closed.py` asserting missing key / API error never returns extractive fabricated answers
- [x] T054 [P] Add contract tests `tests/contract/test_engines_registry.py` (and/or `test_engines_*.py`) validating registry load + `/healthz`+`/v1/systemone` response shape against adapters/fakes
- [x] T055 [P] Add integration smoke `tests/integration/test_matrix_smoke.py` with fake engines covering sequential variable + partner binding and mock refusal
- [x] T056 [P] Update `README.md` for matrix CLI, registry, fail-closed Gemini, and feature pointer to `specs/002-decision-model-bench/`
- [x] T057 Run operator validation scenarios from `specs/002-decision-model-bench/quickstart.md` (health, fail-closed Gemini, mock refuse, seeded sample, matrix export) and fix gaps
- [x] T058 [P] Ensure MLflow traces always include engine id, model_revision, gemini model id, and decision latency for audit (FR-016) in `src/finagent_mesh/runtime/tracing.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **US1 (Phase 3)**: After Foundational — MVP serving/health
- **US3 (Phase 4)**: After Foundational; practically after US1 adapters for real e2e (can stub clients for partial verify)
- **US2 (Phase 5)**: After US1 + US3 (needs real serve + pipeline binding)
- **US4 (Phase 6)**: After Foundational sampling helper; integrate into harness/matrix (can overlap late US2)
- **US5 (Phase 7)**: After US2 row results exist
- **Polish (Phase 8)**: After desired stories complete

### User Story Dependencies

- **US1 (P1)**: No dependency on other stories — MVP
- **US3 (P1)**: Independent with stub/fake engines; production path needs US1
- **US2 (P1)**: Depends on US1 (serve) + US3 (pipeline bind) for full acceptance
- **US4 (P2)**: Uses sampling from Phase 2; completes harness/matrix UX
- **US5 (P3)**: Depends on completed matrix rows from US2

### Parallel Opportunities

- Phase 1: T002–T006 in parallel after T001
- Phase 2: T008, T009, T013 in parallel; T010/T011 sequential with harness touchpoints carefully
- US1: T016–T020 Containerfiles in parallel; T024–T028 adapters in parallel after registry exists
- US5 + Polish test files marked [P] in parallel

---

## Parallel Example: User Story 1

```bash
# Containerfiles in parallel:
Task: "Replace placeholder serve path in containers/anyjev/Containerfile"
Task: "Replace placeholder serve path in containers/clm-8b/Containerfile"
Task: "Replace placeholder serve path in containers/vllm-sr/Containerfile"
Task: "Author containers/laya/Containerfile"
Task: "Author containers/ar-qwen3-instruct/Containerfile"

# Adapters in parallel after registry/factory skeleton:
Task: "Implement AnyJev adapter in src/finagent_mesh/clients/engines/anyjev.py"
Task: "Implement CLM-8B adapter in src/finagent_mesh/clients/engines/clm8b.py"
Task: "Implement vLLM-sr adapter in src/finagent_mesh/clients/engines/vllm_sr.py"
Task: "Implement Laya adapter in src/finagent_mesh/clients/engines/laya.py"
Task: "Implement AR baseline adapter in src/finagent_mesh/clients/engines/ar_baseline.py"
```

---

## Parallel Example: User Story 3

```bash
Task: "Extend scripts/run_harness.py with --stage1-engine/--stage2-engine flags"
Task: "Remove extractive fallback already done in Phase 2 — verify synthesize node fail-closed path"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL)
3. Complete Phase 3: US1 serve/health/adapters for at least `anyjev-l0` + `clm-8b`
4. **STOP and VALIDATE** Independent Test + quickstart §3
5. Then US3 smoke e2e before full matrix

### Incremental Delivery

1. Setup + Foundational → registry, fail-closed Gemini, mock gate
2. US1 → real engines health/decide
3. US3 → per-stage pipeline binding + Flash
4. US2 → sequential matrix
5. US4 → sample/full modes hardened
6. US5 → comparative export
7. Polish → tests + quickstart validation

### Parallel Team Strategy

1. Team completes Setup + Foundational together
2. Then:
   - Dev A: US1 containers/serve
   - Dev B: US1 adapters + US3 harness binding
   - Dev C: US2 matrix runner stubs against fakes → swap real engines when US1 ready
3. US4/US5 after matrix path stabilizes

---

## Notes

- [P] = different files, no incomplete-task dependencies
- Fixed partners: Stage-2 = `clm-8b`, Stage-1 = `anyjev-l0`
- Official runs: `SYSTEMONE_MOCK=0`; no extractive System-2
- Constitution VII: Stage 1+2 always one agentic process per example
- Commit after each task or logical group; stop at checkpoints to validate
