# Feature Specification: Paper P0 Evidence Pack

**Feature Branch**: `004-paper-p0-evidence`

**Created**: 2026-10-09

**Status**: Draft

**Input**: User description: "Specify the entire P0 paper evidence plan: (S0) metric / empty-Top-1 audit with correct pipeline-yield and S2-on-scored reporting; (S3) stratified error analysis explaining E5/BM25 vs Lux Score; (S4) confidence intervals and multi-seed uncertainty protocol; (S1) Gemini synthesis pass on best pairs; (S2) run existing optional baselines lux-clm-shortlist and one-shot-ar. Integrate existing deferred issues #1/#2 as out-of-scope references only."

## Clarifications

### Session 2026-10-09 (from prior planning)

- P0 is the **evidence-hardening** slice before Stage-2 ceiling work (trained heads [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1), cross-encoder [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)), champion AnyJev×E5 cells, AnyJev L1, or Top-k type expansion.
- Motivation: absolute Stage-2 nDCG@5 ≈ 0.22–0.28 is in band with BM25/E5 on the published N=200 run; the risk is mis-reading aggregation and lacking uncertainty / answer metrics / optional baselines—not abandoning Choice→Score.

### Session 2026-10-09

- Q: Should the analysis report include a secondary Stage-2 metric that treats empty-Top-1 examples as zero (pipeline-averaged), in addition to the primary mean over scored examples? → A: Require secondary pipeline-averaged S2 (empties as 0), clearly named; primary remains scored-only
- Q: For the synthesis pass on the four best pairs, should answer generation reuse already-saved Stage-1/Stage-2 rankings from the published matrix, or re-run the full Choice→Score→synthesize pipeline? → A: Reuse saved Stage-1/2 rankings; synthesize only (plus answer score)
- Q: When counting per-example wins and losses of BM25 or E5 against Lux Score, which Stage-2 metric decides the winner? → A: Win by per-example S2 nDCG@5; |Δ| < 0.01 counts as tie
- Q: For the three-seed core-subset protocol, should each seed draw its own N=200 example sample, or should every seed re-evaluate the same fixed example ids from seed 42? → A: Independent N=200 sample per seed (different example ids allowed)
- Q: How should the analysis summarize metrics across the three independent seeds? → A: Per-seed values + mean of seed means + min–max range

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Trustworthy ranking metrics and routing accounting (S0) (Priority: P1)

A researcher opens the analysis report for a completed matrix (including `paper-n200-full`) and can tell, without reading code: (a) how many examples never reached Stage-2 passage ranking (**pipeline yield**); (b) how Stage-2 nDCG/MAP/MRR are averaged (**on scored examples**, not silently zero-filled empties, unless explicitly stated); (c) how **Top-1 type recall** relates to **empty-Top-1** (no chunk pool for the predicted type); and (d) Stage-2 quality via **MRR@5** alongside nDCG@5 so modest nDCG is not mistaken for random ranking.

**Why this priority**: The published empty-Top-1 rate (~40%) and Top-1 recall (~94%) currently look contradictory; incorrect “empties contribute 0 to nDCG” wording can make Stage-2 look artificially catastrophic and block paper drafting.

**Independent Test**: Rebuild analysis from a saved matrix run with no engines; verify new metric definitions, a routing accounting table, and corrected findings text; spot-check that empty examples without Stage-2 ranks are excluded from S2 means (or separately reported as zeros if an explicit “pipeline-averaged” series is added).

**Acceptance Scenarios**:

1. **Given** a completed matrix run, **When** the analysis report is generated, **Then** it reports for each pair: N, count/rate empty-Top-1, count/rate with a Stage-2 ranking list (**scored**), **pipeline yield** = scored/N, Stage-1 Top-1 recall, and a short reconciliation note when empty rate and Top-1 recall diverge.
2. **Given** Stage-2 aggregate metrics, **When** the researcher reads the report, **Then** primary S2 nDCG/MAP/MRR are labeled as **mean over scored examples**, and MRR@5 (overall and conditional-on-eligible-Top-1) appears next to nDCG@5 in Block B tables.
3. **Given** findings text about routing vs scoring, **When** empty-Top-1 is discussed, **Then** the report does **not** claim empties are averaged as zero into **primary** S2 nDCG; instead it shows the secondary **pipeline-averaged** series (empties as 0) under that distinct name.
4. **Given** the routing accounting section, **When** Top-1 is correct but the type-filtered chunk list is empty (or other mismatch classes exist), **Then** those classes are counted and described so “wrong type” is not the only explanation offered for empties.

---

### User Story 2 - Stratified error analysis for Score bake-off (S3) (Priority: P1)

A researcher can explain **why** general-domain dense (E5) and lexical (BM25) beat Lux Score on the same Lux Choice routing: the analysis report includes strata and linked win/loss examples, not only global means.

**Why this priority**: The main Block B paper-facing surprise needs qualitative and stratified evidence before claiming System-1 Score weakness or dataset quirks.

**Independent Test**: From `paper-n200-full` (or equivalent), generate strata tables and an indexed list of example links where E5 or BM25 outrank Lux (and vice versa) on Stage-2 metrics among scored examples.

**Acceptance Scenarios**:

1. **Given** Block B pairs that share Stage-1 Choice, **When** error analysis runs, **Then** Stage-2 metrics are broken down by at least: gold filing type, bucketed candidate-list size after type filter, and bucketed query or passage length (or total chunk characters).
2. **Given** those strata, **When** the report is read, **Then** each stratum shows Lux Score vs BM25 vs E5 (and CLM if present) on the same examples, with N per cell.
3. **Given** pairwise comparisons vs Lux Score, **When** the researcher opens the report, **Then** they get a compact win/tie/loss summary among scored examples decided by per-example Stage-2 **nDCG@5** (absolute Δ < 0.01 = tie), plus links into investigation records for a fixed sample of clearest wins and losses per challenger.
4. **Given** empty-Top-1 examples, **When** strata are computed, **Then** they are excluded from scorer win/loss counts (routing failures are not attributed to Score heads) and counted only in the routing section from User Story 1.

---

### User Story 3 - Uncertainty on headline deltas (S4) (Priority: P1)

A researcher can report Block A and Block B **headline numbers with uncertainty**: bootstrap confidence intervals on the existing published sample, and a multi-seed protocol so Δ(E5 − Lux) / Δ(AnyJev − Lux) are not single-draw artifacts.

**Why this priority**: Absolute S2 levels are soft; without CIs or a second seed, reviewers will dismiss the E5>Lux and AnyJev>Lux findings.

**Independent Test**: Produce CI tables from a saved run without engines; run (or document completion of) multi-seed core-subset ranking evaluations and show seed-wise and pooled summaries in the analysis report.

**Acceptance Scenarios**:

1. **Given** a completed matrix with per-example Stage-1/Stage-2 metric contributions, **When** uncertainty analysis runs, **Then** the report includes **95% bootstrap confidence intervals** for at least: Block A Stage-1 nDCG@5 per Choice pair; Block B Stage-2 nDCG@5 and MRR@5 per Score pair; and pairwise **Δ vs Lux** for those metrics.
2. **Given** the core evidence subset (`lux-lux`, `anyjev-l0-lux`, `lux-e5`, `lux-bm25`), **When** the multi-seed protocol is executed, **Then** ranking-only runs at N≥200 use seeds **{42, 7, 123}** (or the full set if smaller), each drawing an **independent** seeded sample (example ids may differ), each with its own run id, and the analysis shows **per-seed values**, the **mean of the three seed means**, and the **min–max range** across seeds.
3. **Given** bootstrap or multi-seed outputs, **When** findings claim “E5 beats Lux Score” or “AnyJev beats Lux Choice”, **Then** the claim is accompanied by the seed-42 bootstrap CI and/or the across-seed min–max range so a reader can see whether zero is excluded.
4. **Given** GPU budget limits, **When** only bootstrap on seed 42 is available mid-iteration, **Then** the report may mark multi-seed as pending—but publishable P0 closure requires the core-subset three-seed protocol completed.

---

### User Story 4 - Synthesis pass on best pairs (S1) (Priority: P2)

A researcher runs frontier answer synthesis on the **same N and seed** as the published ranking matrix for the pairs that matter most for the paper story, **reusing saved Stage-1/Stage-2 rankings** (no Stage-1/2 re-inference), and obtains answer EM/F1 alongside those fixed ranking metrics.

**Why this priority**: Ranking-only cannot support “agentic retrieval helps answers”; synthesis tests whether ~0.3 S2 nDCG still moves answer scores.

**Independent Test**: Opt-in synthesis-only evaluation on the designated pairs against saved rankings; analysis report gains an answer-metrics section with investigation links for synthesis I/O; ranking nDCG/MRR for those pairs remain unchanged from the published matrix.

**Acceptance Scenarios**:

1. **Given** saved rankings from the published sample (same dataset revision, N, seed **42**), **When** synthesis evaluation runs, **Then** it includes at least: `anyjev-l0-lux`, `lux-lux`, `lux-e5`, and `lux-bm25`, and does **not** re-run Choice or Score engines for those examples.
2. **Given** synthesis completes, **When** the analysis report is generated, **Then** answer normalized EM and token F1 appear per pair, with N attempted / failed / skipped-no-evidence, and ranking-only pairs remain labeled “not run” for answer metrics.
3. **Given** empty-Top-1 or missing Stage-2 evidence in the saved record, **When** synthesis would run, **Then** the example is skipped and counted explicitly (no fabricated extractive answers; no Stage-2 backfill).
4. **Given** synthesis cost, **When** the operator needs a cheaper path, **Then** a documented subset size may be used for smoke—but P0 acceptance for the paper table uses the full published N on the four pairs above.

---

### User Story 5 - Optional catalog baselines that Spec 003 already defined (S2) (Priority: P2)

A researcher runs the **already catalogued** optional Block B rows—shortlist dual-encoder and one-shot generative stuffing—on the same sample, and the analysis report treats them as baselines (not production System-1 pairs).

**Why this priority**: Spec 003 left these optional; without them the systems claim (typed Choice→Score vs stuffing; shortlist before cache) is incomplete. This is **not** issues #1/#2.

**Independent Test**: Opt in to optional pairs; confirm `lux-clm-shortlist` and `one-shot-ar` appear as measured rows with correct labeling; deferred #1/#2 remain skipped with issue links.

**Acceptance Scenarios**:

1. **Given** optional pairs are enabled, **When** the matrix runs on the published N/seed, **Then** `lux-clm-shortlist` and `one-shot-ar` produce Stage-2 (or collapsed) ranking metrics with investigation records.
2. **Given** `one-shot-ar`, **When** results are reported, **Then** the row is labeled as collapsing the two-stage contract (baseline), not as a Choice→Score production pair.
3. **Given** `lux-clm-shortlist`, **When** results are reported, **Then** shortlist size is printed and metrics are comparable to zero-shot `lux-clm` and to Lux/E5/BM25 on the same sample.
4. **Given** deferred pairs `lux-clm-ft` and `lux-e5-ce`, **When** the report lists skips, **Then** they remain deferred with links to [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)—**out of scope for this feature**.

---

### Edge Cases

- Saved matrix missing per-example metric contributions: bootstrap MUST fail clearly or fall back only with an explicit “CI unavailable” marker—never invent intervals.
- Empty-Top-1 rate and Top-1 recall diverge: report MUST surface class counts (correct-Top-1 & empty, wrong-Top-1 & empty, wrong-Top-1 & scored with zero gold in pool, etc.) rather than a single narrative.
- Gold type present in labels but no chunks of that type in the example: counted as a **data/routing anomaly**, not as Score failure.
- Multi-seed run partially complete: analysis MUST list which seeds/pairs finished; MUST NOT average incomplete seed sets as if full.
- Synthesis API failures: fail closed; count failures; do not substitute extractive answers.
- Saved ranking traces missing top-K chunk text for synthesis reuse: skip with explicit reason; do not re-fetch via Score engines in P0.
- One-shot generative cannot emit a full permutation: record parse/coverage failure; do not invent remaining ranks.
- Optional shortlist pair missing weights or shortlist config: skip with reason; do not silently run full-pool CLM under the shortlist pair id.
- Dataset smaller than 200: run all available; print actual N; CIs still required.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The analysis report MUST define and print **pipeline yield** per pair: fraction of examples with a non-empty Stage-2 ranking list.
- **FR-002**: Primary Stage-2 nDCG@5 / MAP@5 / MRR@5 MUST be means over **scored** examples. The report MUST ALSO include a secondary **pipeline-averaged** Stage-2 series (nDCG@5 and MRR@5 at minimum) that treats empty-Top-1 / unscored examples as **zero**, under a distinct name that MUST NOT replace the primary series in Block B tables.
- **FR-003**: Block B tables MUST include MRR@5 (and conditional-on-eligible-Top-1 MRR@5 when eligibility is defined) alongside nDCG@5.
- **FR-004**: The report MUST include a **routing accounting** section that reconciles Stage-1 Top-1 recall with empty-Top-1 rate via mutually exclusive outcome classes and MUST NOT assume every empty is “wrong Top-1 type” without counts.
- **FR-005**: Findings text MUST NOT state that empty-Top-1 examples contribute zero to primary Stage-2 nDCG unless that is how primary metrics are actually computed.
- **FR-006**: The system MUST produce stratified Stage-2 comparisons for Block B scorers by gold filing type, candidate-list-size buckets, and length buckets, with per-cell N.
- **FR-007**: The system MUST produce win/tie/loss counts vs Lux Score among scored examples for BM25 and E5 (and CLM when present), decided by per-example Stage-2 **nDCG@5** with absolute difference **< 0.01** counting as a tie, plus linked investigation samples for extreme wins/losses (largest positive/negative Δ nDCG@5).
- **FR-008**: The system MUST compute **95% bootstrap confidence intervals** for headline Block A Stage-1 nDCG@5, Block B Stage-2 nDCG@5 and MRR@5, and pairwise Δ vs Lux, from per-example contributions of a completed run.
- **FR-009**: The multi-seed protocol MUST evaluate the core subset `{lux-lux, anyjev-l0-lux, lux-e5, lux-bm25}` ranking-only at N≥200 (or full set) for seeds `{42, 7, 123}`, each seed drawing an **independent** sample (example ids MAY differ), and MUST surface **per-seed metrics**, the **mean of seed means**, and the **min–max range** across seeds (pooled multi-seed bootstrap is not required).
- **FR-010**: Synthesis evaluation MUST support the pairs `{anyjev-l0-lux, lux-lux, lux-e5, lux-bm25}` on the same dataset revision, N, and seed **42** as the published ranking matrix, **reusing saved Stage-1/Stage-2 rankings** (no Choice/Score re-inference), recording answer EM/F1 fail-closed, and skipping examples without usable Stage-2 evidence.
- **FR-011**: Optional catalog pairs `lux-clm-shortlist` and `one-shot-ar` MUST be runnable under the existing opt-in path and MUST appear in analysis with baseline labeling when measured.
- **FR-012**: Deferred pairs tracked by [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) MUST remain out of scope; reports continue to list them as deferred_issue skips.
- **FR-013**: All P0 analysis artifacts MUST remain regenerable from saved run ids without starting decision engines where only report math/narrative changes (S0/S3/S4 bootstrap); engine runs are required only for new seeds, synthesis, and optional pairs.
- **FR-014**: P0 MUST NOT change Block A/B identity of required pairs from Spec 003; it adds reporting, uncertainty, synthesis on a subset, and optional baselines already in the catalog.
- **FR-015**: Champion cells (e.g. AnyJev×E5), AnyJev L1, Top-k type pools, trained CLM heads, and cross-encoder ceilings are **out of scope** for this feature (follow-on P1).

### Key Entities

- **Pipeline yield**: Per-pair fraction of examples that produce a Stage-2 ranking list.
- **Routing outcome class**: Mutually exclusive accounting bucket combining Top-1 correctness and empty vs scored Stage-2.
- **Scored-example metric**: Aggregate computed only on examples with Stage-2 ranks (primary).
- **Pipeline-averaged metric**: Aggregate over all N examples where empty/unscored Stage-2 contributes 0 (secondary; distinct name).
- **Stratum cell**: Metric slice keyed by filing type / size / length bucket with N.
- **Win/loss record**: Per-example comparison of two scorers by S2 nDCG@5 (tie if |Δ| < 0.01) with link to investigation.
- **Bootstrap interval**: Resample-based 95% CI on a pair metric or Δ vs Lux.
- **Seeded replicate**: Full or core-subset matrix run at a fixed seed with its own run id.
- **Synthesis outcome**: Answer EM/F1 and failure/skip reasons for an example under Gemini System-2.
- **Optional baseline row**: Catalog pair marked optional/baseline (shortlist CLM; one-shot AR).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A researcher can explain empty-Top-1 vs Top-1 recall using report class counts alone in under five minutes, without reading harness source.
- **SC-002**: Block B primary tables show MRR@5 next to nDCG@5 for every measured Score pair, and a distinctly named secondary pipeline-averaged S2 series (empties as 0) appears alongside; findings never claim empties are zero-averaged into the **primary** series.
- **SC-003**: Stratified tables and at least ten linked win/loss investigation examples (combined across challengers, ranked by \|Δ\| nDCG@5) are present for the published N=200 Lux Choice Block B comparison.
- **SC-004**: Headline Δ(E5 − Lux Score) and Δ(AnyJev − Lux Choice) on seed 42 include 95% bootstrap CIs in the analysis report.
- **SC-005**: Core-subset ranking metrics exist for all three independent seeds {42, 7, 123}, with mean-of-seed-means and min–max range reported (or explicitly marked incomplete preventing P0 closure).
- **SC-006**: Answer EM/F1 tables exist for the four synthesis pairs on seed 42 at the published N (rankings reused from the published matrix), or synthesis failures/skips are quantified with zero fabricated answers and no Stage-1/2 re-inference.
- **SC-007**: `lux-clm-shortlist` and `one-shot-ar` appear as measured or explicitly skipped-with-reason on the published sample; #1/#2 remain deferred with issue links.
- **SC-008**: An operator can regenerate S0/S3/S4-from-saved-run report sections for `paper-n200-full` without starting GPU engines.

## Assumptions

- Published reference run remains `paper-n200-full` (N=200, seed=42, ranking-only, 8/8 required pairs measured); P0 extends evidence around it rather than replacing the matrix catalog.
- Primary Stage-2 aggregates in the current harness already average over examples with Stage-2 ranks (empties omitted); P0 keeps that as primary, corrects narrative, adds yield/accounting, and **requires** a secondary pipeline-averaged series (empties as 0).
- Core multi-seed subset is limited to four pairs to bound GPU time; full eight-pair three-seed matrix is nice-to-have, not required for P0 closure.
- Multi-seed uses **independent** N=200 draws per seed (not frozen seed-42 ids), matching the harness’s seeded sampler.
- Across-seed summary is mean of seed means + min–max range (not pooled bootstrap across seeds).
- Bootstrap uses per-example metric contributions with a fixed resample count suitable for stable 95% CIs (implementation choice left to planning; default expectation ≥1000 resamples).
- Synthesis uses the existing fail-closed Gemini path and the same top-K evidence policy as Spec 003, applied to **saved** top-ranked chunks from the published matrix (reuse path).
- Shortlist size for `lux-clm-shortlist` remains the catalog default (32 unless already configured otherwise).
- Issues [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) stay deferred; this feature only references them in skip/limitations text.
- Secrets and large inspect dumps stay local; lightweight analysis artifacts may be published under `artifacts/benchmarks/` as today.
- Users are researchers preparing a systems/IR paper on financial agentic retrieval, not end-user traders.
