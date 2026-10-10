---
description: "Task list for Paper P0 Evidence Pack"
---

# Tasks: Paper P0 Evidence Pack

**Input**: Design documents from `/specs/004-paper-p0-evidence/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested as TDD in the feature specification. Plan/quickstart name unit checks — include as story-adjacent or Polish validation tasks (not test-first). Primary validation: each story’s Independent Test + `quickstart.md`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/finagent_mesh/`, `scripts/`, `tests/`, `artifacts/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Module stubs and CLI/docs placeholders for P0 evidence extensions

- [x] T001 Create `src/finagent_mesh/matrix/uncertainty.py` and `src/finagent_mesh/matrix/strata.py` module stubs (public function placeholders documented in module docstrings) per `plan.md`
- [x] T002 [P] Add P0 CLI flag stubs / help text notes in `scripts/run_benchmark.py` for `--synthesis-from-rankings` (behavior implemented in US4) per `contracts/evidence-cli.md`
- [x] T003 [P] Document P0 evidence commands and artifact stems in `README.md` Results / next-steps section (link `specs/004-paper-p0-evidence/quickstart.md`) without claiming unfinished metrics

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared per-example extraction + metric series helpers used by all stories — MUST complete before story work

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Add helpers in `src/finagent_mesh/matrix/metrics.py` to list per-example Stage-1/Stage-2 metric contributions (nDCG@5, MRR@5, empty/scored flags, top1_correct) from ranking payloads for a pair
- [x] T005 Implement `pipeline_yield` and secondary **pipeline-averaged** Stage-2 series in `src/finagent_mesh/matrix/metrics.py`: primary remains scored-only mean; `stage2_ndcg_at_5_pipeline` / `stage2_mrr_at_5_pipeline` average over all N with empty/unscored as **0** (distinct names per FR-002 / research.md)
- [x] T006 Implement routing class assignment (`correct_top1_scored`, `correct_top1_empty`, `wrong_top1_scored`, `wrong_top1_empty`, `missing_top1`, `other`) and count/rate maps in `src/finagent_mesh/matrix/metrics.py` per `contracts/routing-classes.md` (sum of counts = N)
- [x] T007 [P] Extend `EngineMetricsRecord` / serialization in `src/finagent_mesh/matrix/models.py` with optional fields for pipeline-averaged S2 metrics and `pipeline_yield` (nullable-safe load/save)
- [x] T008 Ensure `--analysis-from` path in `scripts/run_benchmark.py` loads inspect/ledger per-example data needed for T004–T006 without starting engines

**Checkpoint**: Foundation ready — per-example contributions, routing classes, dual S2 series, and analysis rebuild data path exist

---

## Phase 3: User Story 1 - Trustworthy ranking metrics and routing accounting (S0) (Priority: P1) 🎯 MVP

**Goal**: Analysis report shows pipeline yield, scored-only vs pipeline-averaged S2, MRR@5, and routing accounting that reconciles Top-1 recall vs empty-Top-1

**Independent Test**: `uv run python scripts/run_benchmark.py --analysis-from paper-n200-full` — report has Routing accounting table, dual S2 series, MRR@5; findings never claim empties are zeroed into **primary** S2

### Implementation for User Story 1

- [x] T009 [US1] Wire `pipeline_yield`, routing class counts/rates, and dual Stage-2 series into `build_analysis_payload` in `src/finagent_mesh/matrix/analysis.py` (JSON keys per `contracts/analysis-report-p0.md` / `data-model.md`)
- [x] T010 [US1] Extend Block B Markdown tables in `build_analysis_markdown` in `src/finagent_mesh/matrix/analysis.py` with `S2 MRR@5 (scored)`, `S2 nDCG@5 (pipeline)`, `S2 MRR@5 (pipeline)` and footnotes naming primary vs secondary series
- [x] T011 [US1] Add **Routing accounting** section to `src/finagent_mesh/matrix/analysis.py` Markdown (columns per `contracts/routing-classes.md`) plus reconciliation note when empty rate and Top-1 recall diverge
- [x] T012 [US1] Fix findings/routing narrative in `src/finagent_mesh/matrix/analysis.py` (`_build_findings`): remove/replace “empties contribute 0 to primary S2 nDCG”; cite pipeline-averaged series and class counts instead
- [x] T013 [US1] Regenerate `artifacts/benchmarks/paper-n200-full.analysis.md` and `.analysis.json` via `--analysis-from paper-n200-full` and spot-check SC-001/SC-002

**Checkpoint**: US1 MVP — trustworthy metrics and routing accounting on published full matrix

---

## Phase 4: User Story 2 - Stratified error analysis for Score bake-off (S3) (Priority: P1)

**Goal**: Strata tables and nDCG@5 win/tie/loss vs Lux Score with inspect links

**Independent Test**: Rebuilt analysis for `paper-n200-full` includes Strata + Win/tie/loss (≥10 linked samples combined); empties excluded from win/loss

### Implementation for User Story 2

- [x] T014 [P] [US2] Implement candidate-size buckets `{1–8, 9–32, 33–128, 129+}` and length quartile (or documented fixed cutpoints) helpers in `src/finagent_mesh/matrix/strata.py` per research.md
- [x] T015 [US2] Implement Block B strata aggregation (gold filing type × cand size × length) for Lux/BM25/E5/(CLM) scored examples in `src/finagent_mesh/matrix/strata.py`, returning `StratumCell` list with N and mean S2 nDCG@5
- [x] T016 [US2] Implement win/tie/loss vs `lux-lux` in `src/finagent_mesh/matrix/strata.py`: metric `stage2_ndcg_at_5`, tie if `|Δ| < 0.01`, align by `example_id` among dual-scored examples; extreme samples by `|Δ|` with inspect hrefs
- [x] T017 [US2] Render **Strata** and **Win/tie/loss vs Lux Score** sections + JSON (`strata`, `win_loss`) in `src/finagent_mesh/matrix/analysis.py` per `contracts/analysis-report-p0.md`
- [x] T018 [US2] Confirm inspect anchors used in win/loss samples resolve in `src/finagent_mesh/matrix/inspect.py` (`#pair-<pair_id>-ex-<example_id>` or documented equivalent)

**Checkpoint**: US2 independently delivers stratified + win/loss evidence on saved run

---

## Phase 5: User Story 3 - Uncertainty on headline deltas (S4) (Priority: P1)

**Goal**: Bootstrap 95% CIs on seed 42; independent three-seed core-subset with mean-of-means and min–max

**Independent Test**: Analysis shows bootstrap CIs for Δ(E5−Lux) and Δ(AnyJev−Lux); after seeds 7/123 core runs, multi-seed table shows per-seed + mean + min–max

### Implementation for User Story 3

- [x] T019 [P] [US3] Implement example-level bootstrap (B≥1000, percentile 95% CI, `bootstrap_seed = sample_seed`) in `src/finagent_mesh/matrix/uncertainty.py` for pair metrics and Δ vs `lux-lux`
- [x] T020 [US3] Wire bootstrap intervals into analysis payload/Markdown **Uncertainty** section in `src/finagent_mesh/matrix/analysis.py` for Block A S1 nDCG@5 and Block B S2 nDCG@5 / MRR@5 (scored-only) + Δ vs Lux
- [x] T021 [US3] Add multi-seed rollup helper in `src/finagent_mesh/matrix/uncertainty.py`: load core-subset MatrixRuns for seeds `{42,7,123}`, compute per-seed, mean of seed means, min–max (no pooled multi-seed bootstrap)
- [x] T022 [US3] Document/run core-subset ranking-only commands in comments or README for `paper-n200-s7-core` / `paper-n200-s123-core` (`--pairs lux-lux,anyjev-l0-lux,lux-e5,lux-bm25`, N=200) per `contracts/evidence-cli.md`; seed 42 may reuse `paper-n200-full` rows
- [x] T023 [US3] Extend `--analysis-from` (or small helper invoked by analysis) in `scripts/run_benchmark.py` / `src/finagent_mesh/matrix/analysis.py` to accept multi-seed run ids and render multi-seed table when present; mark pending if incomplete (SC-005)

**Checkpoint**: US3 uncertainty path works offline for bootstrap; multi-seed completes when GPU runs finish

---

## Phase 6: User Story 4 - Synthesis pass on best pairs (S1) (Priority: P2)

**Goal**: Gemini synthesis + answer EM/F1 reusing saved Stage-1/2 rankings for four pairs (no Choice/Score re-inference)

**Independent Test**: Synthesis run attaches EM/F1 for `{anyjev-l0-lux, lux-lux, lux-e5, lux-bm25}` on seed 42; ranking nDCG unchanged; skips counted for empty/missing evidence

### Implementation for User Story 4

- [x] T024 [US4] Implement `--synthesis-from-rankings <matrix_run_id>` in `scripts/run_benchmark.py` per `contracts/evidence-cli.md`: select pairs `{anyjev-l0-lux, lux-lux, lux-e5, lux-bm25}`, new `--run-id` for synth artifacts
- [x] T025 [US4] Implement synthesis-reuse path in `src/finagent_mesh/runtime/harness.py` (extend `synthesis_retriable` / ranking_payload resume): load saved rankings + chunk texts from ledger/inspect; **MUST NOT** call Choice/Score engines; skip empty/missing evidence with counters
- [x] T026 [US4] Persist synthesis payloads, answer EM/F1, attempted/failed/skipped-no-evidence into ledger and pair aggregates in `src/finagent_mesh/matrix/runner.py` / harness
- [x] T027 [US4] Render **Answer metrics (synthesis reuse)** section in `src/finagent_mesh/matrix/analysis.py` stating rankings were reused; fail-closed (no extractive fake answers)
- [ ] T028 [US4] Smoke then full N=200 synthesis reuse against `paper-n200-full` per `quickstart.md` §5; confirm ranking metrics in analysis still match published matrix
  - Deferred: operator GPU/API run (`--synthesis-from-rankings`); CLI + runner path implemented in T025–T027

**Checkpoint**: US4 answer metrics attached without re-ranking

---

## Phase 7: User Story 5 - Optional catalog baselines (S2) (Priority: P2)

**Goal**: Measure `lux-clm-shortlist` and `one-shot-ar` on published N/seed; keep #1/#2 deferred

**Independent Test**: Optional pairs measured or skipped-with-reason on seed 42; analysis labels one-shot as collapsed baseline; deferred issues still linked

### Implementation for User Story 5

- [x] T029 [US5] Verify/fix optional pair execution path in `src/finagent_mesh/matrix/partners.py` + `scripts/run_benchmark.py` for `--include-optional --pairs lux-clm-shortlist,one-shot-ar` (shortlist K printed; one-shot `collapsed_stages` / baseline role)
- [ ] T030 [US5] Run ranking-only optional matrix on N=200 seed=42 (`paper-n200-optional` or merge into analysis view) using existing engines in `configs/engines.yaml`; merge via `src/finagent_mesh/matrix/merge.py` if needed
  - Deferred: optional operator GPU run; engine configs already present
- [x] T031 [US5] Ensure analysis **Optional baselines** + **Skipped/deferred** sections in `src/finagent_mesh/matrix/analysis.py` show measured optionals and deferred `lux-clm-ft` / `lux-e5-ce` with [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) / [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)

**Checkpoint**: US5 closes Spec 003 optional gaps without implementing #1/#2

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Tests, docs, quickstart validation across stories

- [x] T032 [P] Add unit tests for routing classes + pipeline-averaged math in `tests/unit/test_routing_classes.py` and `tests/unit/test_pipeline_yield_metrics.py`
- [x] T033 [P] Add unit tests for bootstrap CI and win/tie/loss (ε=0.01) in `tests/unit/test_bootstrap_ci.py` and `tests/unit/test_win_loss_ndcg.py`
- [x] T034 [P] Add unit tests for strata buckets in `tests/unit/test_strata_buckets.py`; extend `tests/unit/test_analysis_report.py` for P0 sections/guardrails
- [x] T035 Update `README.md` Results / next steps to point at regenerated P0 analysis artifacts and document multi-seed + synthesis-reuse commands from `contracts/evidence-cli.md`
- [x] T036 Run `specs/004-paper-p0-evidence/quickstart.md` validation gates SC-001–SC-008; commit published lightweight analysis artifacts under `artifacts/benchmarks/` if policy matches Spec 003 gitignore exceptions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational — can parallel US1 after T008; practically after US1 analysis wiring for less merge conflict on `analysis.py`
- **US3 (Phase 5)**: After Foundational (needs T004 contributions); analysis section can follow US1
- **US4 (Phase 6)**: After Foundational; independent of US2/US3 GPU-wise; analysis section can follow US1
- **US5 (Phase 7)**: After Foundational; independent ranking run; analysis after US1
- **Polish (Phase 8)**: After desired stories complete

### User Story Dependencies

| Story | Priority | Depends on | Notes |
|-------|----------|------------|-------|
| US1 (S0) | P1 | Phase 2 | MVP; no other stories |
| US2 (S3) | P1 | Phase 2 (+ prefer US1 for `analysis.py`) | Offline on saved run |
| US3 (S4) | P1 | Phase 2 (+ prefer US1) | Bootstrap offline; seeds 7/123 need GPU |
| US4 (S1) | P2 | Phase 2 | Synthesis reuse; Gemini |
| US5 (S2) | P2 | Phase 2 | Optional catalog pairs; GPU |

### Parallel Opportunities

- T002 ∥ T003 (Setup)
- T007 ∥ T004–T006 once models shape agreed
- After Phase 2: US2 strata module (T014–T016) ∥ US3 bootstrap module (T019) ∥ US4 harness design
- T032 ∥ T033 ∥ T034 (Polish tests)

### Parallel Example: After Foundational

```bash
# Developer A — US1 analysis wiring
Task: T009–T013 in src/finagent_mesh/matrix/analysis.py + metrics

# Developer B — US2 strata math
Task: T014–T016 in src/finagent_mesh/matrix/strata.py

# Developer C — US3 uncertainty math
Task: T019–T021 in src/finagent_mesh/matrix/uncertainty.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1–2  
2. Complete Phase 3 (US1)  
3. **STOP**: `--analysis-from paper-n200-full` validates routing + dual S2 series  
4. Demo trustworthy metrics before spending GPU on seeds/synthesis  

### Incremental Delivery

1. US1 → published analysis narrative fixed  
2. US2 → strata + win/loss  
3. US3 bootstrap → then GPU seeds 7/123  
4. US5 optional pairs (can parallel US4)  
5. US4 synthesis reuse  
6. Polish + quickstart SC-001–SC-008  

### Suggested MVP scope

**US1 (S0) only** — unblocks paper drafting confidence about absolute S2 levels and empty vs Top-1.

---

## Notes

- [P] = different files, no incomplete-task dependencies  
- Do not implement GitHub [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) / [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) in this feature  
- Prefer regenerating analysis over mutating historical ranking nDCG in `paper-n200-full`  
- Commit after each task or logical group; stop at checkpoints to validate Independently  
