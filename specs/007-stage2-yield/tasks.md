# Tasks: Stage-2 Yield Recovery (Empty Top-1 Pools)

**Input**: Design documents from `/specs/007-stage2-yield/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included — plan Testing section and quickstart Step 1 require unit coverage for fallback selection, dual metrics, analysis, and immutable path guards. Full N=200 GPU acceptance remains operator-run (not CI-gated).

**Organization**: Phases by user story (US1–US3). US1 = diagnose dual empty/yield; US2 = opt-in recovery runtime + pairs; US3 = analysis Δ vs baselines.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: US1–US3 map to spec user stories
- Exact file paths in every task

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Catalog hooks and path-guard extensions for yield artifact stems — no recovery logic yet

- [ ] T001 [P] Document `yield_recovery` pair field and example pair ids in `configs/engines.yaml` comments (or adjacent catalog note) per `contracts/matrix-pairs-yield.md` without enabling recovery on default required pairs
- [ ] T002 [P] Extend write-path allow/deny in `src/finagent_mesh/unsloth/paths.py` (and/or shared artifact guard used by matrix writes) so stems matching `yield-*` / `*-yield*` are writable while `paper-n200-full*`, `paper-p1-ceilings-n200*`, and `unsloth-score-paper-n200*` remain refused
- [ ] T003 [P] Add `.gitignore` exceptions for published yield summary artifacts under `artifacts/benchmarks/` if/when they should be tracked (mirror paper/unsloth whitelist pattern); leave large inspect JSON local-only

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: AgentState + ranking payload audit fields and helpers shared by all stories

**⚠️ CRITICAL**: No user story work until this phase completes

- [ ] T004 Extend `AgentState` (and related dump helpers) in `src/finagent_mesh/agent/state.py` with `original_top1_doc_type`, `original_top1_empty`, `effective_doc_type`, `yield_recovery_enabled`, `yield_recovery_used`, `yield_recovery_attempted_types` per `data-model.md` (nullable/defaults: recovery fields false/empty when disabled)
- [ ] T005 [P] Implement pure helper `select_effective_doc_type(...)` (ordered first-non-empty; no gold peek; full Choice exhaust) in `src/finagent_mesh/agent/nodes/stage2.py` or `src/finagent_mesh/agent/yield_recovery.py` per `contracts/yield-recovery-runtime.md`
- [ ] T006 Wire ranking payload serialization in `src/finagent_mesh/runtime/harness.py` (and `src/finagent_mesh/agent/graph.py` if needed) so audit fields always appear when recovery enabled; keep `top1_doc_type` = **original** Choice Top-1 for recall compatibility
- [ ] T007 [P] Unit tests for helper edge cases (Top-1 non-empty; Top-1 empty + rank-2 has chunks; all empty; `__all__` unchanged; missing ordered_ids → no invented order) in `tests/unit/test_yield_recovery_stage2.py`

**Checkpoint**: Foundation ready — US1–US3 can proceed (prefer P1 order)

---

## Phase 3: User Story 1 — See why the agent had no evidence (Priority: P1) 🎯 MVP

**Goal**: Dual empty/yield metrics and routing labels so operators distinguish original Top-1 empty vs post-recovery empty / Score failure

**Independent Test**: On a fixture ranking set mimicking paper N=200 classes, metrics emit `empty_original_top1_rate`, post-recovery `empty_top1_chunk_rate` / `pipeline_yield`, and analysis/routing text does not call empty pools a Stage-2 Score failure

### Tests for User Story 1

- [ ] T008 [P] [US1] Unit tests for dual empty/yield aggregation and routing footnote counts (`n_fallback_scored`, `n_fallback_still_empty`) in `tests/unit/test_yield_dual_metrics.py` per `contracts/metrics-dual-reporting.md`

### Implementation for User Story 1

- [ ] T009 [US1] Extend `src/finagent_mesh/matrix/metrics.py` to compute `empty_original_top1_rate`, post-recovery empty/yield, `n_yield_fallback` / `yield_fallback_rate` from ranking payloads (`original_top1_empty` MUST be bool; pipeline yield = fraction with non-empty Stage-2 `ordered_ids`)
- [ ] T010 [US1] Extend `src/finagent_mesh/matrix/models.py` `EngineMetricsRecord` (or equivalent) with optional fields for dual empty/yield and fallback counts without breaking existing paper analysis consumers
- [ ] T011 [US1] Ensure inspect/analysis narrative distinguishes empty-pool vs Score failure in `src/finagent_mesh/matrix/analysis.py` and/or `src/finagent_mesh/matrix/inspect.py` (empty skipped_reason / `empty_top1_chunks` labeled as routing/yield, not scorer crash)
- [ ] T012 [US1] When recovery is **off**, keep `empty_original_top1_rate` equal to today’s empty rate behavior so default pairs stay within SC-003 (±1 pp of published Lux empty on same sample when remeasured)

**Checkpoint**: Dual metrics unit tests green; default (recovery off) metrics still reconcile with existing routing accounting

---

## Phase 4: User Story 2 — Recover evidence when Top-1 type is empty (Priority: P1)

**Goal**: Opt-in ordered Choice fallback in Stage-2; catalog pairs `lux-lux-yield` and `lux-unsloth-score-yield`; new run ids only

**Independent Test**: With recovery enabled, Top-1 empty + rank-2 non-empty → Stage-2 scores rank-2 pool and sets `yield_recovery_used`; all types empty → fail closed; default pairs unchanged; path guard blocks paper/unsloth baseline stems

### Tests for User Story 2

- [ ] T013 [P] [US2] Extend `tests/unit/test_yield_recovery_stage2.py` for gated recovery on/off and first-non-empty without gold preference (gold type later in list MUST NOT win over earlier non-empty non-gold)
- [ ] T014 [P] [US2] Unit tests that yield run ids are writable and `paper-n200-full*` / `unsloth-score-paper-n200*` writes raise in `tests/unit/test_paper_artifact_immutability.py` (or new `tests/unit/test_yield_artifact_paths.py`)

### Implementation for User Story 2

- [ ] T015 [US2] Gate `run_stage2` in `src/finagent_mesh/agent/nodes/stage2.py` on `yield_recovery_enabled`: when Top-1 pool empty, call helper, set effective type / attempted list / `yield_recovery_used`; never consult gold Stage-1 labels
- [ ] T016 [US2] Plumb `yield_recovery` from pair config through `src/finagent_mesh/matrix/runner.py` / harness into agent state (pair field `yield_recovery: true` per `contracts/matrix-pairs-yield.md`)
- [ ] T017 [US2] Add optional catalog pairs `lux-lux-yield` and `lux-unsloth-score-yield` (`optional: true`, `role: yield_recovery`) in `configs/engines.yaml`
- [ ] T018 [US2] Add `--yield-recovery` (and/or pair `lux-unsloth-score-yield`) to `scripts/run_unsloth_eval.py` forcing recovery + suggesting run id prefix `yield-`; refuse overwriting `unsloth-score-paper-n200*`
- [ ] T019 [US2] Ensure frozen Stage-1 path supplies full `stage1_ordered_ids` for fallback in `src/finagent_mesh/unsloth/frozen_stage1.py` / `src/finagent_mesh/clients/engines/frozen_lux_choice.py`; if missing order, skip recovery for that example and count diagnostic
- [ ] T020 [US2] Dual conditional metrics: keep `stage2_*_given_top1` = original Top-1 ∈ gold; add `stage2_*_given_effective_type` when effective ≠ original in `src/finagent_mesh/matrix/metrics.py` per `contracts/metrics-dual-reporting.md`

**Checkpoint**: Unit tests green; smoke commands in `quickstart.md` Steps 2–4 are runnable (operator GPU)

---

## Phase 5: User Story 3 — Compare yield vs Score quality (Priority: P2)

**Goal**: Analysis “Yield recovery” section with Δ vs read-only baselines and visible fallback counts

**Independent Test**: Analysis for a recovery matrix fixture includes dual empty table, fallback counts, Δ vs `lux-lux` / `unsloth-score-paper-n200` numbers without mutating those files

### Tests for User Story 3

- [ ] T021 [P] [US3] Unit tests for Yield recovery analysis section keys and baseline Δ fields in `tests/unit/test_yield_analysis.py` per `contracts/analysis-report-yield.md`

### Implementation for User Story 3

- [ ] T022 [US3] Implement Yield recovery section in `src/finagent_mesh/matrix/analysis.py` (dual empty, post-recovery pipeline/scored, fallback counts, dual conditional labels, Δ vs read-only baselines)
- [ ] T023 [US3] Include fallback-used visibility in compact inspect or pair inspect markdown via `src/finagent_mesh/matrix/inspect.py` (original Top-1, effective type, `yield_recovery_used`)
- [ ] T024 [US3] Document operator commands and checksum regression in `README.md` (high-level 007 pointer) linking `specs/007-stage2-yield/quickstart.md`

**Checkpoint**: Analysis unit tests green; quickstart Step 5 (checksum) documented

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Acceptance documentation and cross-story consistency

- [ ] T025 [P] Align `specs/007-stage2-yield/quickstart.md` with final CLI flags/pair ids after implementation
- [ ] T026 Comment on GitHub [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10) with links to yield artifact stems once N=200 acceptance runs exist (operator)
- [ ] T027 Run `uv run pytest tests/unit/test_yield_*.py tests/unit/test_paper_artifact_immutability.py -q` and fix regressions
- [ ] T028 Verify default `run_benchmark.py --list-pairs` still marks required Block A/B without yield pairs unless `--include-optional`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **US1 (Phase 3)**: After Foundational — MVP for diagnosis metrics (can land before recovery gate is live if payloads set `original_top1_empty` even when recovery off)
- **US2 (Phase 4)**: After Foundational; benefits from US1 metrics fields but can implement runtime first then wire metrics
- **US3 (Phase 5)**: After US1 metrics + US2 payload fields exist
- **Polish (Phase 6)**: After desired stories complete

### User Story Dependencies

- **US1**: No dependency on US2 recovery being on — original empty can be computed whenever Top-1 pool emptiness is known
- **US2**: Depends on T004–T007 helpers/state
- **US3**: Depends on US1 aggregates + US2 audit fields for meaningful Δ tables

### Parallel Opportunities

- T001–T003 in parallel
- T005 and T007 after T004 types exist; T008 || T014 once contracts stable
- T013 || T014 during US2
- T021 parallel with early US3 drafting once fixture shape known

---

## Parallel Example: User Story 2

```bash
# After foundational checkpoint:
Task: "Extend tests/unit/test_yield_recovery_stage2.py for gold-blind first-non-empty"
Task: "Unit tests for yield-* writable / paper stems refused in tests/unit/test_yield_artifact_paths.py"
```

---

## Implementation Strategy

### MVP First (User Story 1)

1. Phase 1 Setup + Phase 2 Foundational  
2. Phase 3 US1 dual metrics + labeling  
3. **STOP**: Validate `test_yield_dual_metrics.py`  
4. Demo: analysis distinguishes empty-pool vs Score failure on existing ledgers if payloads backfilled

### Incremental Delivery

1. US1 → dual reporting on current runs  
2. US2 → opt-in recovery + pairs + Unsloth CLI flag  
3. US3 → Yield recovery analysis section + README pointer  
4. Operator: quickstart N=200 Lux + Unsloth acceptance  

### Suggested MVP scope

**US1 only** (diagnose) is the smallest valuable ship; **US1+US2** required to close [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10) behavior; **US3** required for architect-facing Δ tables in the same PR or follow-up.

---

## Notes

- [P] = different files, no incomplete-task dependencies  
- Do not overwrite `paper-n200-full*` or `unsloth-score-paper-n200*`  
- Recovery MUST NOT peek at gold labels when choosing effective type  
- `top1_doc_type` in payloads remains original Choice Top-1  
