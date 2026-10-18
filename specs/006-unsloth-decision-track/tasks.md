# Tasks: Unsloth Decision-Model Training Track

**Input**: Design documents from `/specs/006-unsloth-decision-track/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included — plan Testing section and SC-001 / SC-005 require automated leakage + paper-immutability / analysis unit coverage; Unsloth GPU train/eval remains smoke-documented (not CI-gated on 27B).

**Organization**: Phases by user story (US1–US4). US5 (Choice / compounds) is deferred past v1 — no implementation tasks.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: US1–US4 map to spec user stories
- Exact file paths in every task

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Optional Unsloth extra, package skeleton, artifact ignore rules — no story logic yet

- [x] T001 Create package skeleton `src/finagent_mesh/unsloth/__init__.py` (lazy-import friendly; no Unsloth import at module load)
- [x] T002 [P] Add `[project.optional-dependencies] unsloth` pins in `pyproject.toml` (isolated from `real`; document Transformers arch needs for Qwen3.8)
- [x] T003 [P] Gitignore `artifacts/unsloth/` (datasets, checkpoints, train runs) in `.gitignore` while allowing optional tracked manifests if added later
- [x] T004 [P] Add `UNSLOTH_SCORE_CHECKPOINT`, `UNSLOTH_SHORTLIST_K` (default 32), `UNSLOTH_BASE_MODEL` defaults to `configs` or `.env.example` / README env section per `contracts/unsloth-cli.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared types, paper-artifact immutability, and proof that default benchmark path never imports Unsloth

**⚠️ CRITICAL**: No user story work until this phase completes

- [x] T005 Implement write-path guard refusing stems `paper-n200-full*` and `paper-p1-ceilings-n200*` in `src/finagent_mesh/unsloth/paths.py` (FR-010)
- [x] T006 [P] Define `SplitManifest`, `ScoreTrainingRow`, `UnslothTrainRun` field schemas/types in `src/finagent_mesh/unsloth/types.py` per `data-model.md` (incl. `test_source` must be `paper-n200-full` for default; `status` enum `pending|running|completed|failed`)
- [x] T007 Add unit test that importing `finagent_mesh` / loading `scripts/run_benchmark.py` does not import `unsloth` package in `tests/unit/test_unsloth_isolation.py` (FR-003)

**Checkpoint**: Foundation ready — US1–US4 can proceed (prefer P1 order; US3 can start after T005–T007 if adapters mocked)

---

## Phase 3: User Story 1 — Leakage-safe training data (Priority: P1) 🎯 MVP

**Goal**: Export gold-type Score rows + split with `test_ids` = paper N=200 and zero train/val leakage

**Independent Test**: Run `scripts/export_unsloth_dataset.py`; `leakage_report.json` overlaps = 0; `split_manifest.json` has `n_test=200`, `test_source=paper-n200-full`

### Tests for User Story 1

- [x] T008 [P] [US1] Unit tests for paper-id holdout and zero train/val∩test in `tests/unit/test_unsloth_split.py` (SC-001)
- [x] T009 [P] [US1] Unit tests for gold-type-only candidates and Score criteria vocabulary in `tests/unit/test_unsloth_export.py`

### Implementation for User Story 1

- [x] T010 [US1] Implement split builder loading `selected_example_ids` from `artifacts/matrix_runs/paper-n200-full.json` in `src/finagent_mesh/unsloth/split.py` (`set(test)∩set(train)=∅`, `set(test)∩set(val)=∅`, `set(train)∩set(val)=∅`; `content_hash` over sorted id lists + `test_source`)
- [x] T011 [US1] Implement gold-type Score row builder in `src/finagent_mesh/unsloth/export.py` (every candidate `doc_type` ∈ `gold_doc_types`; empty pools counted not silent-success; criteria `["not relevant","partially relevant","highly relevant"]` per `contracts/training-export.md`)
- [x] T012 [US1] Implement CLI `scripts/export_unsloth_dataset.py` writing `split_manifest.json`, train/val JSONL, `leakage_report.json` (`paper_test_ids_count`, `train_overlap_count=0`, `val_overlap_count=0`, `content_hash`) under `artifacts/unsloth/datasets/`
- [x] T013 [US1] Fail closed (non-zero exit) on any paper-id leakage or write-guard violation when exporting via `scripts/export_unsloth_dataset.py`

**Checkpoint**: Export + leakage tests green without Unsloth GPU deps

---

## Phase 4: User Story 2 — Isolated Unsloth training pipeline (Priority: P1)

**Goal**: Supervised QLoRA Score train via optional extra; checkpoints under `artifacts/unsloth/`; no paper artifact mutation

**Independent Test**: Smoke `train_unsloth_score.py --max-train-rows 1000`; checkpoint + train config JSON exist; `sha256sum` of published paper JSON unchanged

### Tests for User Story 2

- [x] T014 [P] [US2] Unit tests for train-config persistence fields and refuse writing paper stems in `tests/unit/test_unsloth_train_meta.py` (mock Unsloth; no GPU)

### Implementation for User Story 2

- [x] T015 [US2] Implement lazy `FastDecisionModel` / `DecisionTrainer` wrappers in `src/finagent_mesh/unsloth/train.py` (default base `unsloth/Qwen3.8-27B-unsloth-bnb-4bit`; supervised only — no RL; refuse if split `test_ids` ≠ paper selected ids)
- [x] T016 [US2] Implement CLI `scripts/train_unsloth_score.py` (`--dataset-dir`, `--base-model`, `--out-dir`, `--run-id`, `--max-train-rows`) writing under `artifacts/unsloth/checkpoints/`
- [x] T017 [US2] Persist `UnslothTrainRun` metadata JSON + MLflow tags (checkpoint path, base model id, LoRA r/alpha/dropout/`max_seq_length`/`load_in_4bit`, split hash, seed, holdout metrics when calibrate runs) from `scripts/train_unsloth_score.py` / `src/finagent_mesh/unsloth/train.py`
- [x] T018 [US2] Document resume vs clean-restart behavior for interrupted runs in `scripts/train_unsloth_score.py` help / module docstring (no silent overwrite of published eval)

**Checkpoint**: Smoke train path documented; default `uv sync --extra real` still works without Unsloth

---

## Phase 5: User Story 3 — Serve trained Score engine family (Priority: P1)

**Goal**: Register fail-closed `unsloth-decision-score` System-1 Score adapter consumable by Stage-2

**Independent Test**: With checkpoint env set, score one example → ordered ids + scores; with env unset → explicit unsupported/error (no Lux/E5/BM25 substitute)

### Tests for User Story 3

- [x] T019 [P] [US3] Unit tests fail-closed missing `UNSLOTH_SCORE_CHECKPOINT` and Score output shape in `tests/unit/test_unsloth_score_adapter.py` (mock model)

### Implementation for User Story 3

- [x] T020 [US3] Implement Score adapter in `src/finagent_mesh/clients/engines/unsloth_score.py` (`FastDecisionModel.for_inference` + `predict`; fail-closed; no `decide_decision20` / CLM / AnyJev)
- [x] T021 [US3] Register `unsloth_score` (and stub hook for hybrid) backend in `src/finagent_mesh/clients/engines/registry.py`
- [x] T022 [P] [US3] Add optional engine `unsloth-decision-score` to `configs/engines.yaml` (trained-track labeling; not default required Block A/B)

**Checkpoint**: Engine listable as optional; missing weights fail closed

---

## Phase 6: User Story 4 — Comparable evaluation run (Priority: P1)

**Goal**: Dedicated `lux-unsloth-score` eval = frozen Lux Choice + BM25 k=32 → trained Score; `unsloth-*` artifacts + analysis Δ vs published baselines

**Independent Test**: `run_unsloth_eval.py` smoke N=20 (then N=200); analysis has Trained decision track + read-only Δ vs `lux-lux`, `lux-lux-shortlist`, `lux-e5`; paper files untouched

### Tests for User Story 4

- [x] T023 [P] [US4] Unit tests BM25 shortlist k=32 then Score in `tests/unit/test_bm25_unsloth_shortlist.py`
- [x] T024 [P] [US4] Unit tests frozen Stage-1 loader matches paper Top-1 fields in `tests/unit/test_unsloth_frozen_stage1.py`
- [x] T025 [P] [US4] Unit tests trained-track analysis + read-only comparison keys in `tests/unit/test_unsloth_analysis.py` (`contracts/analysis-report-unsloth.md`)

### Implementation for User Story 4

- [x] T026 [US4] Implement frozen Lux Choice loader from `paper-n200-full` inspect/ledger in `src/finagent_mesh/unsloth/frozen_stage1.py` (`FrozenStage1Record`: `top1_doc_type`, `empty_top1`, optional ordered ids/scores)
- [x] T027 [US4] Implement hybrid Stage-2 adapter in `src/finagent_mesh/clients/engines/bm25_unsloth_shortlist.py` (mirror `lux_shortlist.py`; default `UNSLOTH_SHORTLIST_K=32`; record k in metadata)
- [x] T028 [US4] Register `bm25_unsloth_shortlist` backend in `src/finagent_mesh/clients/engines/registry.py` and wire in-process deps in `src/finagent_mesh/matrix/partners.py` / `src/finagent_mesh/matrix/ports.py` as needed
- [x] T029 [US4] Add optional pair `lux-unsloth-score` (`role=trained_decision`, Stage-2 shortlist hybrid) in `configs/engines.yaml` per `contracts/matrix-pairs-unsloth.md` (MUST NOT enter default required Block A/B)
- [x] T030 [US4] Extend analysis for Trained decision track + `comparison_vs_published` in `src/finagent_mesh/matrix/analysis.py` (read-only baselines; MUST NOT rewrite published paper analysis files)
- [x] T031 [US4] Implement CLI `scripts/run_unsloth_eval.py` (`--pairs lux-unsloth-score`, `--frozen-stage1-from paper-n200-full`, `--checkpoint`, `--run-id` prefix `unsloth-`, write `artifacts/benchmarks/unsloth-*` + `artifacts/matrix_runs/unsloth-*.json` only)
- [x] T032 [US4] Enforce immutability + fail-closed missing checkpoint in `scripts/run_unsloth_eval.py` (no fallback to Lux Score / E5 under trained pair id)

**Checkpoint**: Smoke eval + analysis comparison; paper checksums unchanged

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Docs, CI regression, quickstart validation

- [x] T033 [P] Document parallel Unsloth stack (not Decision-2.0 drop-in) and train→eval commands in `README.md` (FR-011, SC-006)
- [x] T034 [P] Add CI/unit regression that published `artifacts/benchmarks/paper-n200-full.json` is unchanged by analysis-from path / write-guard in `tests/unit/test_paper_artifact_immutability.py` (SC-005)
- [x] T035 Align operator steps with `specs/006-unsloth-decision-track/quickstart.md` (export → smoke train → smoke eval → checksum)
- [x] T036 Note US5 (Choice train / AnyJev×Unsloth) as deferred in `README.md` or issue #5 comment — no code for Choice pairs in v1

---

## Phase 8: User Story 5 — Deferred (Priority: P3)

**Goal**: Out of v1 — trained Choice pairs and AnyJev×trained-Score compounds

**Independent Test**: N/A for v1 acceptance

- No tasks. Revisit after `lux-unsloth-score` lands.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** US1–US4
- **US1 (Phase 3)**: After Foundational — MVP data path
- **US2 (Phase 4)**: After US1 export artifacts exist (needs dataset dir)
- **US3 (Phase 5)**: After Foundational; can parallelize with US1/US2 if Score adapter mocked
- **US4 (Phase 6)**: After US2 checkpoint + US3 engines (needs both for real smoke); unit tests can start after Foundational
- **Polish (Phase 7)**: After US1–US4 desired scope
- **US5**: Deferred

### User Story Dependencies

- **US1**: No dependency on other stories
- **US2**: Needs US1 export outputs for real train; meta unit tests independent
- **US3**: Independent of US1/US2 for fail-closed unit tests; real inference needs US2 checkpoint
- **US4**: Needs US3 adapters + US2 checkpoint for end-to-end; frozen-stage1/analysis units independent of GPU

### Parallel Opportunities

- T002–T004 after T001
- T006 parallel with T005
- T008–T009 after T006
- T019 parallel with T014 while US1 implements
- T023–T025 after Foundational
- T033–T034 in Polish in parallel

---

## Parallel Example: User Story 1

```bash
# Tests first (expect fail until T010–T012):
Task: "Unit tests for paper-id holdout in tests/unit/test_unsloth_split.py"
Task: "Unit tests for gold-type export in tests/unit/test_unsloth_export.py"

# Then implementation:
Task: "split.py paper holdout + content_hash"
Task: "export.py gold-type Score rows"
Task: "export_unsloth_dataset.py CLI + leakage_report"
```

## Parallel Example: User Story 4

```bash
Task: "tests/unit/test_bm25_unsloth_shortlist.py"
Task: "tests/unit/test_unsloth_frozen_stage1.py"
Task: "tests/unit/test_unsloth_analysis.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational
3. Phase 3 US1 (export + leakage)
4. **STOP**: Validate Independent Test for US1

### Incremental Delivery

1. US1 → leakage-safe datasets
2. US2 → smoke QLoRA checkpoint
3. US3 → fail-closed Score engine
4. US4 → `lux-unsloth-score` paper-slice eval + Δ tables
5. Polish → README + SC-005 immutability CI

### Suggested MVP

**US1 only** (export + automated leakage) proves holdout before GPU spend. Next vertical slice: US2 smoke train → US3 adapter → US4 N=20 eval.

---

## Notes

- Default `run_benchmark.py --real` pairs MUST remain unchanged
- Production base model: `unsloth/Qwen3.8-27B-unsloth-bnb-4bit`
- Eval Stage-2: BM25 k=32 → Unsloth Score; Stage-1 frozen from `paper-n200-full`
- Commit after each task or logical group; stop at story checkpoints
