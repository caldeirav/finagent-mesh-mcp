# Tasks: Stage-2 Approach Ceilings (S8 + S2b + S7)

**Input**: Design documents from `/specs/005-s2-approach-ceilings/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included per plan.md Technical Context (unit tests for hybrids + catalog).

**Organization**: US1 S8 champions → US2 S2b shortlist-Lux → US3 S7 CE ceiling → US4 analysis hygiene → polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1…US4 map to spec user stories
- Exact file paths in descriptions

---

## Phase 1: Setup

- [x] T001 Sync engine/pair contract notes into `configs/engines.yaml` comments pointing at `specs/005-s2-approach-ceilings/contracts/matrix-pairs-p1.md`
- [x] T002 [P] Add P1 CLI examples to `scripts/run_benchmark.py` help / docstring per `contracts/p1-cli.md`
- [x] T003 [P] Document P1 env knobs (`LUX_SHORTLIST_K`, `CE_SHORTLIST_K`, `CE_WEIGHTS`) in `.env.example`

---

## Phase 2: Foundational (blocking)

- [x] T004 Extend `MatrixPair` / registry loading in `src/finagent_mesh/matrix/partners.py` to accept `role: champion` and `role: ir_ceiling` without treating them as deferred
- [x] T005 Update `sidecar_dependencies` in `src/finagent_mesh/matrix/ports.py` so `backend=lux_shortlist` (or family hybrid lux shortlist) requires `decision20-lux`
- [x] T006 [P] Register backends `lux_shortlist` and `e5_ce_shortlist` stubs in `src/finagent_mesh/clients/engines/registry.py` (raise clear error until adapters land)
- [x] T007 Remove `lux-e5-ce` from `deferred_pairs` in `configs/engines.yaml` only after engine+pair entries exist (coordinate with T014/T020); keep `lux-clm-ft` → issue #1

**Checkpoint**: Resolver can load new roles; ports know Lux shortlist dependency; #2 no longer permanently deferred in YAML once pairs added

---

## Phase 3: User Story 1 — Champion cells (S8) (Priority: P1)

**Goal**: Runnable `anyjev-l0-e5` and `anyjev-l0-bm25`; Champion analysis section.

**Independent Test**: `--pairs anyjev-l0-e5,anyjev-l0-bm25 --records 5 --skip-synthesis` completes; analysis Champion section present.

- [x] T008 [P] [US1] Add matrix pairs `anyjev-l0-e5` and `anyjev-l0-bm25` (`optional: true`, `role: champion`) in `configs/engines.yaml` per `contracts/matrix-pairs-p1.md`
- [x] T009 [P] [US1] Unit test catalog resolve includes champions with `--include-optional` or explicit `--pairs` and never marks them deferred in `tests/unit/test_partners_p1_ceilings.py`
- [x] T010 [US1] Ensure `src/finagent_mesh/matrix/ports.py` / runner starts AnyJev Stage-1 and leaves E5/BM25 in-process for champion pairs (no erroneous second GPU Score sidecar)
- [x] T011 [US1] Add Champion / compound section skeleton in `src/finagent_mesh/matrix/analysis.py` (and JSON keys) per `contracts/analysis-report-p1.md`
- [x] T012 [US1] Wire interpret/report narrative so Champion cells are not attributed as Block A Score bake-off in `src/finagent_mesh/matrix/interpret.py`

**Checkpoint**: S8 smoke path catalog-complete; analysis labels ready (metrics fill when run)

---

## Phase 4: User Story 2 — Shortlist → Lux Score (S2b) (Priority: P1)

**Goal**: `lux-lux-shortlist` with BM25 top-K then Lux Score; default K=32 via `LUX_SHORTLIST_K`.

**Independent Test**: `--pairs lux-lux-shortlist --records 5` ranks with shortlist metadata; unit tests cover tail policy.

- [x] T013 [P] [US2] Implement `LuxShortlistAdapter` in `src/finagent_mesh/clients/engines/lux_shortlist.py` (BM25 shortlist → `decision20-lux` Score; env `LUX_SHORTLIST_K` default 32; tail sentinel scores like `clm_shortlist.py`)
- [x] T014 [US2] Add engine `lux-score-shortlist-32` and pair `lux-lux-shortlist` (`optional: true`, `blocks: [B]`) in `configs/engines.yaml`
- [x] T015 [US2] Wire `create_adapter` for `backend=lux_shortlist` in `src/finagent_mesh/clients/engines/registry.py` and export in `__init__.py` if needed
- [x] T016 [P] [US2] Unit tests for shortlist truncation, empty candidates, and tail append in `tests/unit/test_lux_shortlist.py` (mock Lux HTTP)
- [x] T017 [US2] Record `shortlist_k` / `shortlist_method=bm25` in Stage-2 ranking payload or MLflow tags via adapter metadata consumed by inspect/analysis
- [x] T018 [US2] Extend P1 ceilings analysis rows for `lux-lux-shortlist` latency + shortlist_k in `src/finagent_mesh/matrix/analysis.py`

**Checkpoint**: S2b independently testable with mocked Lux + real BM25 unit path

---

## Phase 5: User Story 3 — E5 → CE ceiling (S7) (Priority: P1)

**Goal**: Runnable `lux-e5-ce`; close GitHub #2 acceptance; label IR ceiling.

**Independent Test**: `--pairs lux-e5-ce --records 5`; CE weights missing → explicit skip/error not silent E5-only under same pair id.

- [x] T019 [P] [US3] Implement `E5CeShortlistAdapter` in `src/finagent_mesh/clients/engines/e5_ce_shortlist.py` (E5 shortlist → `CrossEncoder`; env `CE_SHORTLIST_K` default 32; `CE_WEIGHTS` default `cross-encoder/ms-marco-MiniLM-L6-v2`; fail closed if CE load fails)
- [x] T020 [US3] Add engine `e5-ce-shortlist-32` and pair `lux-e5-ce` (`optional: true`, `role: ir_ceiling`) in `configs/engines.yaml`; ensure removed from `deferred_pairs`
- [x] T021 [US3] Wire `create_adapter` for `backend=e5_ce_shortlist` in `src/finagent_mesh/clients/engines/registry.py`
- [x] T022 [P] [US3] Unit tests with mocked E5/CE in `tests/unit/test_e5_ce_shortlist.py` (shortlist size, CE failure, no silent fallback to E5-only pair identity)
- [x] T023 [US3] Analysis: label `lux-e5-ce` as IR ceiling; require S2 overall + conditional Top-1 + latency vs `lux-e5`/`lux-lux` when available in `src/finagent_mesh/matrix/analysis.py`
- [x] T024 [US3] Update limitations / deferred list in `src/finagent_mesh/matrix/analysis.py` and `interpret.py`: #2 delivered; #1 remains deferred
- [x] T025 [US3] Update README deferred blurb in `README.md` so #2 is no longer “unimplemented ceiling” once code lands (keep #1)

**Checkpoint**: S7 closes #2 checklist; smoke-ready

---

## Phase 6: User Story 4 — Analysis & matrix hygiene (Priority: P2)

**Goal**: Default `--real` unchanged; P1 section complete; inspect index works.

**Independent Test**: `--list-pairs` / default resolve unchanged for required pairs; `--analysis-from` shows P1 sections.

- [x] T026 [US4] Assert default `resolve_matrix_pairs` excludes P1 optionals unless `--include-optional` or explicit `--pairs` in `tests/unit/test_partners_p1_ceilings.py`
- [x] T027 [US4] Ensure inspect HTML anchors exist for new pair ids in `src/finagent_mesh/matrix/inspect.py`
- [x] T028 [US4] Fill `analysis.json` keys `champion_pairs`, `p1_ceiling_pairs`, updated `deferred` per `contracts/analysis-report-p1.md`
- [x] T029 [US4] Align `specs/003-choice-score-paper` / README cross-links only as needed so docs do not contradict #2 status (minimal doc sync)

**Checkpoint**: Hygiene + report contract satisfied

---

## Phase 7: Polish

- [x] T030 [P] Run `uv run pytest tests/unit/test_lux_shortlist.py tests/unit/test_e5_ce_shortlist.py tests/unit/test_partners_p1_ceilings.py`
- [x] T031 Validate quickstart smoke commands in `specs/005-s2-approach-ceilings/quickstart.md` against `--list-pairs` output
- [ ] T032 Operator: N=5 smokes then N=200 `paper-p1-ceilings-n200` per quickstart; comment on issue #2 with artifact pointers when closing
- [x] T033 [P] Sync `specs/002-decision-model-bench/contracts/engines-registry.yaml` or feature contract note if required by repo convention

---

## Dependencies

```text
Phase 1 → Phase 2 → US1 (S8) → US2 (S2b) → US3 (S7) → US4 → Polish
```

- US1 can ship before hybrids exist (catalog-only champions).
- US2 depends on foundational ports + Lux sidecar dep.
- US3 depends on foundational registry; independent of US2 adapters.
- US4 after at least analysis hooks from US1–US3.

## Parallel examples

```bash
# After T007:
# Parallel: T008 + T009 (US1 catalog/tests)
# Parallel: T013 + T016 (US2 adapter + tests) once T005 done
# Parallel: T019 + T022 (US3 adapter + tests)
```

## Implementation strategy

1. **MVP**: US1 champions (fastest GPU evidence).
2. **Increment**: US2 shortlist-Lux.
3. **Ceiling**: US3 CE + close #2.
4. **Report**: US4 + polish + N=200.

**Suggested MVP scope**: T001–T012 only, then smoke S8.
