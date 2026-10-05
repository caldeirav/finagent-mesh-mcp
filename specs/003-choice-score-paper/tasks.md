---
description: "Task list for paper-ready Choice/Score matrix and analysis report"
---

# Tasks: Paper-Ready Choice/Score Matrix & Analysis Report

**Input**: Design documents from `/specs/003-choice-score-paper/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested as TDD in the feature specification. Plan names unit/integration checks — include those as Polish validation tasks (not test-first). Primary validation: each story’s Independent Test + `quickstart.md`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/finagent_mesh/`, `scripts/`, `configs/`, `tests/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Catalog shape, deps, env for Block A/B + IR adapters

- [x] T001 Rewrite `matrix_pairs` in `configs/engines.yaml` to match `specs/003-choice-score-paper/contracts/matrix-pairs.yaml` (Block A `*-lux`, Block B `lux-*`, optional `lux-clm-shortlist` / `one-shot-ar`, `blocks` / `optional` / `role` fields; remove old `*-clm` cross-product defaults except required `lux-clm`)
- [x] T002 [P] Add engine entries `bm25-stage2`, `e5-base`, `clm-shortlist-32` to `configs/engines.yaml` and mirror in `specs/002-decision-model-bench/contracts/engines-registry.yaml` or feature contract sync note in README
- [x] T003 [P] Add deps to `pyproject.toml` extras (`real` or new): `rank-bm25`, `sentence-transformers`; document `E5_WEIGHTS=intfloat/e5-base-v2` and `CLM_SHORTLIST_K=32` in `.env.example`
- [x] T004 [P] Document deferred pairs `lux-clm-ft` / `lux-e5-ce` with issue URLs in `configs/engines.yaml` comments (or `deferred_pairs` key) linking [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Pair model, resolver, metrics helpers, CLI paper defaults — MUST complete before story work

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Extend `MatrixPair` in `src/finagent_mesh/matrix/partners.py` with fields `blocks: list[str]` (values `A`\|`B`), `collapsed_stages: bool = False`, `deferred: bool = False`, `deferred_issue: str | null = None` per `data-model.md`
- [x] T006 Update `pairs_from_registry` / `resolve_matrix_pairs` in `src/finagent_mesh/matrix/partners.py`: default = all `optional=false`; `--include-optional` adds optional; never auto-select `deferred=true`; dedupe physical run when `lux-lux` appears in both blocks
- [x] T007 [P] Extend `PairResult` / matrix models in `src/finagent_mesh/matrix/models.py` with reviewer fields: `stage2_*_given_top1`, `stage1_top1_recall`, `stage1_top5_recall`, `empty_top1_chunk_rate`, `option_flip_rate`, `parse_failure_rate`, latency p50/p95, `gpu_mem_high_water_mb`, `blocks`, `skip` support per `data-model.md`
- [x] T008 [P] Add `SkipRecord` handling in `src/finagent_mesh/matrix/models.py` (`pair_id`, `reason` in `optional_not_requested|deferred_issue|missing_weights|missing_calibration|…`, `issue_url` nullable)
- [x] T009 Implement paper metric helpers in `src/finagent_mesh/matrix/metrics.py`: Top-1/Top-5 type recall, empty-top1 rate, Stage-2 nDCG/MAP/MRR conditional on `top1_correct`, aggregate latency percentiles from example traces
- [x] T010 Wire `ranking_payload` routing flags in `src/finagent_mesh/runtime/harness.py` (`top1_correct`, `empty_top1_chunks`, `eligible_for_conditional_s2`) into ledger payloads for metric aggregation
- [x] T011 Change `--real` paper defaults in `scripts/run_benchmark.py`: without `--records` use `min(200, dataset_n)` seeded sample; default `skip_synthesis=True`; add `--with-synthesis` to enable Gemini; keep `--skip-synthesis` explicit
- [x] T012 Extend `--list-pairs` in `scripts/run_benchmark.py` to print `pair_id`, `blocks`, `optional`, `role`, `collapsed_stages` from registry

**Checkpoint**: Foundation ready — catalog resolves Block A/B; metrics helpers exist; paper CLI defaults ranking-only N=200

---

## Phase 3: User Story 1 - Isolated Stage-1 Choice ablation (Block A) (Priority: P1) 🎯 MVP

**Goal**: Run Block A pairs where only Choice varies and Stage-2 is always Lux Score; report S1 metrics + OFR + parse failures without confounding S2 scorers

**Independent Test**: Execute Block A on a seeded sample; every required Block A pair shares Stage-2 engine `decision20-lux`; S1 nDCG/Top-1 recall differ by pair; AnyJev L0 reports OFR; AR reports parse-failure rate

### Implementation for User Story 1

- [x] T013 [US1] Ensure Block A required pairs resolve and run via `src/finagent_mesh/matrix/runner.py`: `lux-lux`, `anyjev-l0-lux`, `kai-lux`, `laya-lux`, `ar-lux` with Stage-2 `decision20-lux`; keep Lux Score warm across Block A rows when possible
- [x] T014 [US1] Implement option-flip rate (OFR) for AnyJev L0 in `src/finagent_mesh/clients/engines/anyjev.py` and/or harness: measure fraction of examples where argmax filing type changes under reversed option order; persist `option_flip_rate` on pair metrics
- [x] T015 [US1] Ensure AR Stage-1 parse failures increment `parse_failure_rate` and fail closed (no invented type ranks) in `src/finagent_mesh/clients/engines/ar_baseline.py` and aggregator path
- [x] T016 [US1] Populate Block A pair metrics (S1 nDCG/MAP/MRR, Top-1/Top-5 recall, OFR, parse-fail, S1 latency p50/p95, shared `stage2_engine`) in `src/finagent_mesh/matrix/runner.py` using `src/finagent_mesh/matrix/metrics.py`
- [x] T017 [US1] Update `src/finagent_mesh/matrix/interpret.py` so Block A narrative never attributes Stage-2 nDCG differences to different scorers when `stage2_engine` is identical across rows

**Checkpoint**: Block A ablation runnable and interpretable as Choice-only

---

## Phase 4: User Story 2 - Isolated Stage-2 Score ablation (Block B) (Priority: P1)

**Goal**: Run Block B pairs where only Score varies (Lux Choice fixed) including BM25, E5, CLM, lux-lux; optional shortlist-CLM and one-shot AR; report overall and conditional-on-Top-1 S2 metrics

**Independent Test**: Execute Block B on same seed as Block A; required pairs share Stage-1 `decision20-lux`; S2 metrics include `*_given_top1`; optional pairs only with `--include-optional`

### Implementation for User Story 2

- [x] T018 [P] [US2] Implement in-process BM25 Stage-2 Score adapter in `src/finagent_mesh/clients/engines/bm25_score.py` (`config_id` `bm25-stage2`, `BM25Okapi` over Top-1-type chunks, no GPU, fail closed on empty candidate list)
- [x] T019 [P] [US2] Implement E5 Stage-2 Score adapter in `src/finagent_mesh/clients/engines/e5_score.py` (`config_id` `e5-base`, Hub `intfloat/e5-base-v2` via `E5_WEIGHTS`, prefixes `query: ` / `passage: `, cosine rank descending)
- [x] T020 [P] [US2] Implement shortlist hybrid adapter in `src/finagent_mesh/clients/engines/clm_shortlist.py` (`clm-shortlist-32`: BM25 top-`CLM_SHORTLIST_K` default 32 then existing CLM Score)
- [x] T021 [US2] Register BM25/E5/shortlist backends in `src/finagent_mesh/clients/engines/registry.py` (and `__init__.py`) so OpenDecision Score routes without silent substitution
- [x] T022 [US2] Extend `src/finagent_mesh/clients/engines/ar_baseline.py` for one-shot chunk ranking mode used by pair `one-shot-ar` (`collapsed_stages=true`, no Stage-1 Choice, parse/coverage failure recording, no invented remaining ranks)
- [x] T023 [US2] Special-case `one-shot-ar` in `src/finagent_mesh/runtime/harness.py` / `src/finagent_mesh/matrix/runner.py`: skip Stage-1 type filter; set `collapsed_stages=true` on ranking_payload; Stage-1 metrics null/N/A; label `role: baseline_collapsed`
- [x] T024 [US2] Ensure Block B required pairs run: `lux-lux` (shared), `lux-clm`, `lux-bm25`, `lux-e5`; optional `lux-clm-shortlist`, `one-shot-ar` only with `--include-optional` in `scripts/run_benchmark.py` + `partners.py`
- [x] T025 [US2] Aggregate Block B metrics including `stage2_*_given_top1`, `empty_top1_chunk_rate`, S2 latency p50/p95, shared `stage1_engine` (except one-shot) in `src/finagent_mesh/matrix/runner.py`
- [x] T026 [US2] Best-effort GPU memory high-water (`torch.cuda.max_memory_allocated`) into pair metrics when CUDA available in `src/finagent_mesh/matrix/runner.py` or engine adapters

**Checkpoint**: Block B Score ablation + optional shortlist/one-shot independently testable

---

## Phase 5: User Story 3 - Paper analysis report with investigation links (Priority: P1)

**Goal**: Paper-facing analysis report with Block A/B tables, reviewer metrics, findings guardrails, and links to every pair×example inspect record; rebuildable without engines

**Independent Test**: `--analysis-from <run-id>` regenerates report without starting sidecars; follow pair→example link to expected labels and S1/S2 I/O

### Implementation for User Story 3

- [x] T027 [US3] Add stable inspect HTML anchors `#pair-<pair_id>-ex-<example_id>` in `src/finagent_mesh/matrix/inspect.py` per `contracts/analysis-report.md`
- [x] T028 [US3] Implement `src/finagent_mesh/matrix/analysis.py` writing `<run-id>.analysis.md` and `<run-id>.analysis.json` with sections: run facts, research questions, Block A table, Block B table, routing-vs-scoring, latency/resources, findings, limitations (incl. deferred #1/#2), skip/deferred, artifact index
- [x] T029 [US3] Implement findings guardrails in `src/finagent_mesh/matrix/analysis.py`: assert Block A completed pairs share identical `stage2_engine`; Block B (excl. one-shot) share `stage1_engine`; never claim Block A S2 model bake-off; synthesis “not run” when disabled; label one-shot collapsed
- [x] T030 [US3] Index every pair×example (completed, failed, empty_top1) with relative `href` into inspect HTML; use `trace_missing` when ledger/inspect lacks I/O — never fabricate — in `src/finagent_mesh/matrix/analysis.py`
- [x] T031 [US3] Call analysis writer at end of matrix run in `scripts/run_benchmark.py`; add `--analysis-from <run-id>` rebuild path (no engines, manage_servers=false)
- [x] T032 [US3] Point interpret MD artifacts section at analysis + inspect paths in `src/finagent_mesh/matrix/interpret.py`

**Checkpoint**: Analysis report is paper-usable and links to inspect records

---

## Phase 6: User Story 4 - Default paper set vs optional expensive rows (Priority: P2)

**Goal**: Default `--real` runs only required Block A+B; optional rows opt-in; deferred appear as skip records with issue URLs; stable pair ids

**Independent Test**: `--list-pairs` / default resolve shows required only; `--include-optional` adds shortlist + one-shot; deferred never auto-run; SkipRecords in analysis

### Implementation for User Story 4

- [x] T033 [US4] Enforce resolver rules in `src/finagent_mesh/matrix/partners.py`: default excludes `optional=true`; `--include-optional` adds them; `deferred=true` never selected; emit `SkipRecord` for deferred with `issue_url` for analysis
- [x] T034 [US4] Add `--include-optional` flag to `scripts/run_benchmark.py` and pass through `MatrixRunner` / `resolve_matrix_pairs`
- [x] T035 [US4] On missing weights for optional IR engines, skip that pair with SkipRecord `missing_weights` without substituting another engine; required pair failures still fail the matrix run — in `src/finagent_mesh/matrix/runner.py`
- [x] T036 [US4] Ensure `lux-lux` executes once per matrix run and appears in both Block A and Block B analysis tables in `src/finagent_mesh/matrix/runner.py` + `analysis.py`

**Checkpoint**: Default paper set frozen; optional/deferred correctly gated

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Docs, tests, quickstart validation

- [x] T037 [P] Update `README.md` Default pairs table to Block A/B catalog, ranking-only `--real` default, `--with-synthesis`, `--include-optional`, analysis/inspect artifacts
- [x] T038 [P] Unit tests for block resolver + dedupe in `tests/unit/test_matrix_blocks.py`
- [x] T039 [P] Unit tests for conditional S2 / Top-1 recall helpers in `tests/unit/test_paper_metrics.py`
- [x] T040 [P] Unit tests for BM25/E5 adapters (tiny synthetic docs) in `tests/unit/test_bm25_e5_adapters.py`
- [x] T041 [P] Unit tests for analysis guardrails + anchor index in `tests/unit/test_analysis_report.py`
- [x] T042 Integration smoke `tests/integration/test_paper_matrix_smoke.py` (mock-allowed or tiny fake adapters) verifying default pair set excludes optional
- [x] T043 Run `specs/003-choice-score-paper/quickstart.md` smoke path (`--real --records 10 --skip-synthesis`) and confirm analysis + inspect artifacts
- [x] T044 [P] Sync `uv.lock` after dependency adds; verify `.gitignore` still excludes eval artifacts/secrets

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **US1 (Phase 3)**: After Foundational — MVP (Block A with existing Lux Score)
- **US2 (Phase 4)**: After Foundational — can parallelize with US1 after T012; needs T018–T021 before full Block B
- **US3 (Phase 5)**: After Foundational — ideally after US1 or US2 produce a matrix JSON; can stub with fixture run for analysis-only
- **US4 (Phase 6)**: After T006 resolver; refine after US2 optional adapters exist
- **Polish (Phase 7)**: After desired stories complete

### User Story Dependencies

- **US1 (P1)**: No dependency on US2/US3 — uses existing Lux Score
- **US2 (P1)**: Independent Score adapters; shares catalog foundation with US1
- **US3 (P1)**: Needs completed matrix artifact (from US1 and/or US2) or fixture
- **US4 (P2)**: Tightens resolver/CLI around US1/US2 catalog

### Parallel Opportunities

- T002–T004 after T001 catalog shape is clear
- T007–T008 in parallel during Foundational
- T018–T020 (BM25/E5/shortlist) in parallel during US2
- T038–T041 unit tests in parallel during Polish
- US1 and US2 can proceed in parallel once Phase 2 completes (different files)

---

## Parallel Example: User Story 2

```bash
# Adapters in parallel (different files):
Task: "Implement BM25 adapter in src/finagent_mesh/clients/engines/bm25_score.py"
Task: "Implement E5 adapter in src/finagent_mesh/clients/engines/e5_score.py"
Task: "Implement shortlist adapter in src/finagent_mesh/clients/engines/clm_shortlist.py"
```

## Parallel Example: User Story 3

```bash
# After inspect anchors exist:
Task: "Implement analysis.py report writer"
Task: "Wire --analysis-from in scripts/run_benchmark.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup — rewrite catalog to `*-lux` Block A
2. Phase 2 Foundational — resolver, metrics, ranking-only defaults
3. Phase 3 US1 — run Block A; OFR + parse-fail; interpret guardrail
4. **STOP and VALIDATE** with `--pairs` limited to Block A + `--records 10`

### Incremental Delivery

1. Setup + Foundational → catalog + CLI defaults
2. US1 Block A → Choice ablation MVP
3. US2 Block B → BM25/E5/CLM/shortlist/one-shot
4. US3 Analysis report → paper artifact + links
5. US4 Optional gating → frozen default set
6. Polish → README + tests + quickstart

### Suggested MVP scope

**US1 only** (Block A with Lux Score fixed) proves the paper’s Choice ablation claim; US2/US3 required before a full paper draft.

---

## Notes

- [P] = different files, no incomplete-task dependencies
- Do not implement trained CLM heads or cross-encoder (issues #1/#2)
- Fail closed: no mock rankings on `--real`, no silent engine substitution
- Commit after each task or logical group
- Primary validation: Independent Test per story + `quickstart.md`
