# Feature Specification: Stage-2 Approach Ceilings (S8 + S2b + S7)

**Feature Branch**: `005-s2-approach-ceilings`

**Created**: 2026-10-11

**Status**: Draft

**Input**: User description: "Spec Kit 005-s2-approach-ceilings with only S8 + S2b + S7: champion cells AnyJev×E5/BM25; shortlist-then-Lux-Score hybrid; dense bi-encoder → cross-encoder Stage-2 ceiling (close GitHub #2). Short-timeline P1 MVP on ZGX Nano / DGX Spark. Out of scope: S5 AnyJev L1, S6/CLM-ft (#1), S9 Top-k types, Unsloth decision track (#5), LLM-as-judge (#4)."

## Clarifications

### Session 2026-10-11 (locked for short timeline)

- **In scope only**: S8 (champion AnyJev×IR), S2b (shortlist→Lux Score), S7 (dense→CE ceiling / issue [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)).
- **Out of scope**: S5 (AnyJev L1), S6 / [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) (trained CLM heads), S9 (Top-k type expansion), [#4](https://github.com/caldeirav/finagent-mesh-mcp/issues/4) (LLM judge), [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5) (Unsloth FastDecisionModel track).
- Motivation: raise Stage-2 / end-to-end evidence after P0 without training jobs; answer whether better routing×IR compounds, whether ordinal Lux Score improves on a shortlist, and whether ~0.28 S2 nDCG is a soft IR ceiling.
- Defaults locked below under Assumptions (no open clarification markers).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Champion router × IR scorer cells (S8) (Priority: P1)

A researcher runs **compound** pairs that fix the best open Choice router with the best classical IR scorers—**AnyJev L0 × E5** and **AnyJev L0 × BM25**—on the same published sample size and seed as the paper matrix, and sees Stage-1 and Stage-2 metrics in a dedicated **Champion / compound** analysis section (not mixed into pure Block A/B attribution rules).

**Why this priority**: The orthogonal matrix never measures best-router × best-scorer; this is the strongest short-timeline systems figure and needs almost no new ranking machinery.

**Independent Test**: Opt in to the two champion pairs; complete ranking-only evaluation; confirm analysis shows them separately from Block A (Choice-only) and Block B (Lux-Choice Score bake-off); investigation records exist like other pairs.

**Acceptance Scenarios**:

1. **Given** the matrix catalog, **When** an operator lists or selects pairs, **Then** `anyjev-l0-e5` and `anyjev-l0-bm25` are available as optional (or explicitly selectable) pairs with stable ids.
2. **Given** a ranking-only run on the published N and seed (default N≥200, seed 42), **When** those pairs complete, **Then** Stage-1 metrics are attributable to AnyJev L0 and Stage-2 metrics to E5 or BM25 respectively, with overall and conditional-on-correct-Top-1 Stage-2 series consistent with P0 reporting.
3. **Given** analysis generation, **When** the report is opened, **Then** a **Champion / compound** section compares these cells to `anyjev-l0-lux`, `lux-e5`, and `lux-bm25` without claiming Block A Stage-2 deltas are a Score bake-off.
4. **Given** missing E5 weights or BM25 dependency, **When** a champion pair cannot run, **Then** it is skipped with an explicit reason (no silent engine substitution).

---

### User Story 2 - Shortlist then Lux Score (S2b) (Priority: P1)

A researcher runs an optional Block B-style pair that **shortlists** Top-1-type passages (lexical shortlist, same spirit as existing shortlist-CLM) then applies **Lux ordinal Score** only on that shortlist, and can compare Stage-2 quality and latency to full-pool `lux-lux` on the same sample.

**Why this priority**: Tests whether long candidate lists hurt ordinal Score—the main hypothesized fix for middling Lux S2—without training or a new model family.

**Independent Test**: Enable the shortlist-Lux pair; run ranking-only; compare S2 nDCG/MRR and Stage-2 latency to `lux-lux`; shortlist size appears in the report.

**Acceptance Scenarios**:

1. **Given** the catalog, **When** optional / selected pairs include shortlist-Lux, **Then** a stable pair id (default `lux-lux-shortlist`) appears with Stage-1 = Lux Choice and Stage-2 = shortlist-then-Lux-Score.
2. **Given** a completed run, **When** Stage-2 executes, **Then** Lux Score is applied only to the shortlisted passages (default shortlist size **32**), remaining candidates are ordered after the shortlist without inventing Lux scores for the full pool as if they were scored.
3. **Given** analysis, **When** Block B / optional Score rows are shown, **Then** `lux-lux-shortlist` is comparable to `lux-lux`, `lux-e5`, and `lux-bm25` on the same N/seed, with shortlist size and Stage-2 latency p50/p95 printed.
4. **Given** empty Top-1 chunk pool, **When** shortlist-Lux would run, **Then** behavior matches existing fail-closed empty-Top-1 handling (no fabricated ranks).

---

### User Story 3 - Dense shortlist → cross-encoder ceiling (S7) (Priority: P1)

A researcher runs the optional IR **ceiling** row: Lux Choice → dense bi-encoder shortlist → **cross-encoder** rerank of the shortlist, previously deferred as issue [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2), and sees whether Stage-2 nDCG/MRR (overall and conditional-on-correct-Top-1) exceed E5-alone and Lux Score, with latency contrasted.

**Why this priority**: Answers “is ~0.28 S2 nDCG a soft ceiling?”; closes #2; still no training job if a pretrained cross-encoder is used.

**Independent Test**: Promote `lux-e5-ce` from deferred to runnable optional; complete ranking-only on published N/seed; analysis labels the row as baseline/ceiling; latency vs `lux-e5` and `lux-lux` present; #2 acceptance bullets satisfied.

**Acceptance Scenarios**:

1. **Given** the catalog, **When** deferred pairs are resolved after this feature, **Then** `lux-e5-ce` is no longer a `deferred_issue` skip and is runnable under opt-in / explicit `--pairs`.
2. **Given** Stage-2 for `lux-e5-ce`, **When** scoring runs, **Then** candidates under the Top-1 type are shortlisted by E5 (or the documented dense shortlist), then reranked by a pretrained cross-encoder on that shortlist; the pair is labeled **IR ceiling / baseline**, not a production System-1 Score head.
3. **Given** completed metrics, **When** the analysis report is generated, **Then** Stage-2 overall and conditional-on-correct-Top-1 metrics appear, plus Stage-2 latency p50/p95 vs at least `lux-e5` and `lux-lux`.
4. **Given** missing cross-encoder weights or dependency, **When** the pair cannot run, **Then** skip with explicit reason; do not silently fall back to E5-only under the `lux-e5-ce` pair id.
5. **Given** issue [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2), **When** this feature’s acceptance is met, **Then** the issue’s acceptance checklist items are satisfied so the issue can be closed.

---

### User Story 4 - Analysis and matrix hygiene for P1 ceilings (Priority: P2)

A researcher regenerates the paper analysis report and sees a clear **P1 ceilings** section covering champion cells, shortlist-Lux, and CE ceiling; default required Block A/B pairs are unchanged; deferred #1 remains deferred; limitations no longer claim #2 is unimplemented once S7 ships.

**Why this priority**: Prevents mis-reading compound cells as orthogonal Block A/B and keeps the default paper matrix frozen.

**Independent Test**: Generate analysis from a run that includes the new pairs (or skip records); verify section structure and default `--real` pair set unchanged.

**Acceptance Scenarios**:

1. **Given** default `--real` without optional/P1 flags, **When** pairs resolve, **Then** the required Spec 003 Block A/B set is unchanged (no forced champion/CE/shortlist-Lux).
2. **Given** P1 pairs measured or skipped, **When** analysis runs, **Then** the report includes a P1 / ceilings section and updates limitations: #2 removed from “deferred unimplemented” when `lux-e5-ce` is measured; #1 remains deferred with link.
3. **Given** investigation HTML, **When** a P1 pair example is opened, **Then** expected labels vs model I/O are available like other pairs.

---

### Edge Cases

- Champion pair selected but AnyJev or E5/BM25 unhealthy: fail closed at health check; do not substitute Lux Choice or Lux Score silently.
- Shortlist size larger than candidate pool: score the full pool; do not pad with synthetic chunks.
- Shortlist size ≤ 0 or misconfigured: fail or skip with explicit config error; do not run unbounded Lux Score under the shortlist pair id.
- Cross-encoder returns partial scores: fail closed for that example (retriable) or skip with reason—never invent remaining ranks.
- Empty-Top-1: all three P1 Stage-2 paths follow existing empty-pool accounting (P0 yield / scored-only primary metrics).
- Operator requests only one of S8/S2b/S7: each story remains independently runnable via pair selection.
- GPU memory pressure: sequential exclusive heavy engines; CE/E5 in-process must not require a second Decision-2.0 sidecar concurrently with Lux Choice beyond existing port policy.
- Dataset smaller than 200: run all available; print actual N.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The catalog MUST add runnable pairs `anyjev-l0-e5` and `anyjev-l0-bm25` (S8) with Stage-1 AnyJev L0 and Stage-2 E5 / BM25 respectively.
- **FR-002**: Champion pairs MUST be opt-in (not part of the default required Block A/B set) and MUST appear in analysis under a **Champion / compound** section distinct from pure Block A and Block B tables.
- **FR-003**: The catalog MUST add runnable pair `lux-lux-shortlist` (S2b): Stage-1 Lux Choice, Stage-2 BM25 (or equivalent lexical) shortlist then Lux ordinal Score.
- **FR-004**: Shortlist size for S2b MUST default to **32** and MUST be configurable; the configured size MUST be recorded in run metadata and the analysis report.
- **FR-005**: S2b MUST NOT present full-pool Lux Score under the `lux-lux-shortlist` pair id; unscored tail passages MUST NOT be treated as Lux-scored for metric honesty (tail ordering policy MUST be documented in plan).
- **FR-006**: Pair `lux-e5-ce` MUST be promoted from deferred to runnable optional (S7), implementing Lux Choice → E5 shortlist → pretrained cross-encoder rerank, and MUST be labeled as IR ceiling/baseline in reports.
- **FR-007**: S7 MUST report Stage-2 metrics overall and conditional on correct Top-1 type, plus Stage-2 latency p50/p95 versus `lux-e5` and `lux-lux` when those rows exist in the same or referenced run.
- **FR-008**: Missing weights, calibration, or dependencies for any P1 pair MUST yield an explicit skip/failure reason with no silent engine substitution.
- **FR-009**: Ranking MUST remain fail-closed (no mock rankings for official runs); sequential exclusive GPU policy for heavy sidecars MUST be preserved.
- **FR-010**: Default required paper pairs from Spec 003 MUST remain unchanged; P1 pairs run only via `--include-optional` and/or explicit `--pairs` (or equivalent documented flags).
- **FR-011**: Analysis/report MUST include a P1 ceilings section covering S8, S2b, and S7 when any are measured; limitations MUST keep [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) deferred and MUST NOT list [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) as unimplemented once S7 is delivered.
- **FR-012**: Investigation records for P1 pairs MUST index into existing inspect HTML like other matrix pairs.
- **FR-013**: This feature MUST NOT implement AnyJev L1 enablement, CLM head training, Top-k type expansion, Unsloth decision training, or LLM-as-judge evaluation.
- **FR-014**: Closing criteria for [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) (stable pair id, ceiling labeling, sequential GPU, Stage-2 overall + conditional, latency vs bi-encoder and Lux Score, investigation/analysis index) MUST be met by S7 delivery.

### Key Entities

- **Champion pair**: Non-orthogonal Choice×Score cell combining best router with classical IR scorer (`anyjev-l0-e5`, `anyjev-l0-bm25`).
- **Shortlist-Lux pair**: Hybrid Stage-2 that lexical-shortlists then applies Lux Score (`lux-lux-shortlist`).
- **CE ceiling pair**: Dense shortlist then cross-encoder rerank (`lux-e5-ce`), labeled baseline/ceiling.
- **Shortlist size**: Configured K for hybrid Stage-2 (default 32).
- **P1 ceilings section**: Analysis report block summarizing S8/S2b/S7 results and comparisons.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On the published sample protocol (N≥200, seed 42, ranking-only), `anyjev-l0-e5` and `anyjev-l0-bm25` produce completed Stage-1/Stage-2 metrics (or explicit skip reasons) and appear in a Champion section distinguishable from Block A/B.
- **SC-002**: `lux-lux-shortlist` completes on the same protocol with shortlist size recorded; Stage-2 metrics and latency are comparable side-by-side with `lux-lux` in the analysis report.
- **SC-003**: `lux-e5-ce` is runnable (no longer deferred-only); Stage-2 overall + conditional-on-Top-1 and latency vs `lux-e5` / `lux-lux` appear; issue #2 acceptance items are satisfied.
- **SC-004**: Default required `--real` pair set is identical to Spec 003 required pairs (no accidental expansion).
- **SC-005**: An operator can run S8, S2b, and S7 independently via pair selection within a two-week local calendar budget on a single sequential-GPU workstation (smoke N=5 plus full N≥200 for each included pair).
- **SC-006**: Analysis limitations correctly state #1 still deferred and #2 delivered (or measured) after this feature.

## Assumptions

- Target hardware is ZGX Nano / DGX Spark with sequential exclusive heavy System-1 sidecars; E5 and cross-encoder may run in-process like today’s E5 adapter.
- Published reference sample remains N=200, seed=42, ranking-only, aligned with `paper-n200-full` / P0 evidence.
- S8 shortlist method for champions: none—full Top-1-type pool scored by E5 or BM25 (existing adapters).
- S2b shortlist method: **BM25** top-K then Lux Score (mirrors `lux-clm-shortlist`); default K=32.
- S7 shortlist method: **E5** top-K then pretrained cross-encoder; default K matches S2b (32) unless plan documents a CE-specific default; CE model is a small pretrained reranker suitable for ARM64/Spark (exact id chosen at plan time).
- Tail policy for hybrid scorers: shortlist receives model scores; non-shortlisted ids are appended with sentinel low scores so rank lists cover the candidate set without claiming full-pool model scores (same spirit as existing CLM shortlist adapter).
- Issue [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) stays open/deferred; [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) is in scope to close; [#4](https://github.com/caldeirav/finagent-mesh-mcp/issues/4) and [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5) are unrelated follow-ons.
- P0 metric definitions (scored-only primary S2, pipeline yield, conditional Top-1) remain authoritative; this feature does not redefine them.
- Users are researchers preparing a systems/IR paper on financial agentic retrieval.
