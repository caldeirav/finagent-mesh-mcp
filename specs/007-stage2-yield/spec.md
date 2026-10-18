# Feature Specification: Stage-2 Yield Recovery (Empty Top-1 Pools)

**Feature Branch**: `007-stage2-yield`

**Created**: 2026-10-18

**Status**: Draft

**Input**: GitHub issue [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10) — improve **pipeline yield** when Stage-1 Choice selects a filing type that has **no passage candidates** in the index (“empty Top-1 pool”), without pretending Score quality alone can fix missing evidence. Follows published Score specialization (`006` / `unsloth-score-paper-n200`), where scored Stage-2 quality is strong (~0.61 nDCG) but **pipeline** quality stays capped (~0.35) by ~**37–40%** empty pools under Lux Choice on the paper N=200 slice.

**Related**: [#11](https://github.com/caldeirav/finagent-mesh-mcp/issues/11) latency ladder (separate), [#14](https://github.com/caldeirav/finagent-mesh-mcp/issues/14) multi-seed confirmation (separate), [#9](https://github.com/caldeirav/finagent-mesh-mcp/issues/9) Choice FT (separate). Closed [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5) Score v1 complete.

## Clarifications

### Session 2026-10-18 (defaults for v1)

- Q: Default recovery when Top-1 type has an empty chunk pool? → A: **Ordered Choice fallback** — try the next Stage-1 option(s) in Choice rank order until a non-empty type-filtered pool is found or options are exhausted; record which type was used and that a fallback occurred.
- Q: Does yield recovery change published paper baselines by default? → A: **No** — default matrix / published `paper-*` and `unsloth-score-paper-n200*` remain unchanged; yield recovery is opt-in via dedicated pair(s) and/or run id(s).
- Q: Primary eval sample for v1 acceptance? → A: **Same paper N=200 seed-42 holdout** as `paper-n200-full` / `unsloth-score-paper-n200` so yield Δ is comparable.

### Session 2026-10-18 (clarify)

- Q: After yield recovery, should empty rate / pipeline yield count the final evidence outcome or only the original Choice Top-1 type? → A: **Dual metrics** — keep original Top-1 empty accounting for baseline comparability, and add **post-recovery** empty/yield for the effective type used in Stage-2; success criteria for improved yield use the post-recovery figures.
- Q: When recovery uses a type that is not Choice Top-1, how should conditional Stage-2 quality be reported? → A: **Dual reporting** — keep **conditional-on-Choice-Top-1** as published today (only when original Top-1 is in gold), and add **conditional-on-effective-type** when fallback changed the type; do not silently redefine the published conditional metric.
- Q: Which Stage-2 path(s) must be evaluated with yield recovery for v1 acceptance? → A: **Both** — at least one published-style Lux Score twin (e.g. `lux-lux` or shortlist Lux with the same Score family as a published row) **and** one tuned Unsloth Score path (`lux-unsloth-score`-style: frozen Choice + BM25 shortlist + trained Score).
- Q: When Top-1 has no chunks, how far down the Choice ranking should recovery search? → A: **Exhaust the full Choice ranking** — try all remaining types in rank order until a non-empty pool is found or options are exhausted.
- Q: If several lower-ranked types have chunks, how should recovery pick among them? → A: **First non-empty in Choice rank order** — never use gold Stage-1 labels to choose the fallback; gold remains for scoring and routing accounting only.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See why the agent had no evidence (Priority: P1)

An operator or architect reviewing a failed or empty-evidence example can tell whether the agent **routed to a type with no chunks** versus **picked the wrong type**, using existing routing accounting plus clear yield labels—without reading raw ledger JSON by hand.

**Why this priority**: Without a shared diagnosis, teams over-invest in Score training when the failure is empty corpus after a plausible route.

**Independent Test**: On the published N=200 paper slice under Lux Choice (or frozen Lux), produce a routing/yield breakdown that separates empty-pool classes and matches counts already reported in paper analysis (within rounding).

**Acceptance Scenarios**:

1. **Given** a completed ranking-only matrix on the paper N=200 ids, **When** the operator opens the analysis (or a yield section), **Then** they see empty-Top-1 rate, pipeline yield, and mutually exclusive routing classes that reconcile Top-1 recall vs empties.
2. **Given** an example with empty Stage-2 candidates after Top-1 type filter, **When** inspect or analysis is viewed, **Then** the case is labeled as empty-pool (not as a Stage-2 Score failure).
3. **Given** an example with a non-empty Stage-2 list, **When** metrics are reported, **Then** scored Stage-2 quality remains distinct from pipeline-averaged quality (empties counted as 0 in pipeline).

---

### User Story 2 - Recover evidence when Top-1 type is empty (Priority: P1)

A researcher enables an **opt-in yield-recovery** path: if the Top-1 filing type has no chunks for that example, the agent tries the next Choice option(s) in rank order until a non-empty pool is found (or options run out), then runs Stage-2 scoring as usual on that recovered type’s candidates.

**Why this priority**: This is the core product fix for “routed but nothing to fetch” when a lower-ranked type still has evidence.

**Independent Test**: Run opt-in recovery on the paper N=200 holdout for **both** a Lux Score twin and a tuned Unsloth Score path; compare post-recovery empty/yield and pipeline Stage-2 metrics to the matching no-fallback baselines; confirm published baseline artifact files are unchanged.

**Acceptance Scenarios**:

1. **Given** yield recovery is disabled (default), **When** a matrix/eval runs, **Then** behavior matches today’s empty-pool accounting (no silent fallback).
2. **Given** yield recovery is enabled and Top-1 type has zero chunks but a lower-ranked Choice option has chunks, **When** the example is evaluated, **Then** Stage-2 runs on the **first** non-empty type in Choice rank order (even if a later option is in gold and this one is not), and the run records that fallback from Top-1 to that effective type occurred.
3. **Given** all Choice options yield empty pools, **When** the example is evaluated, **Then** the outcome remains empty (fail closed for evidence); no invented passages.
4. **Given** a paper holdout eval with recovery enabled, **When** artifacts are written, **Then** they use a **new** run id / pair id prefix and do **not** overwrite `paper-n200-full*`, `paper-p1-ceilings-n200*`, or `unsloth-score-paper-n200*`.

---

### User Story 3 - Compare yield vs Score quality for design decisions (Priority: P2)

An architect reading reports can see **side-by-side** scored Stage-2 quality and pipeline yield (with and without recovery) so they can decide whether to invest in corpus coverage, fallbacks, or further Score training.

**Why this priority**: Closes the interpretation gap highlighted after 006 (strong scored nDCG, weak pipeline).

**Independent Test**: Analysis for a recovery run includes a comparison table vs the published no-recovery baseline metrics on the same N=200 sample (read-only baseline numbers).

**Acceptance Scenarios**:

1. **Given** a completed recovery eval on the paper slice, **When** analysis is generated, **Then** it reports original Top-1 empty rate, post-recovery empty rate / yield, scored S2 nDCG, and post-recovery pipeline S2 nDCG for the recovery pair.
2. **Given** published baseline numbers for the same sample, **When** analysis is generated, **Then** Δ post-recovery empty / Δ pipeline S2 (and fallback counts) are shown without editing baseline files, alongside original Top-1 empty for apples-to-apples baseline comparison.
3. **Given** fallbacks occurred, **When** analysis or inspect is viewed, **Then** the count (or rate) of examples that used a non–Top-1 type is visible.

---

### Edge Cases

- Top-1 type empty but gold type is also empty in the dump → recovery may still leave empty; must not fabricate chunks.
- Fallback selects a type that is not in gold Stage-1 labels → keep Choice-Top-1 recall / conditional-on-Choice-Top-1 unchanged in meaning; also report conditional-on-effective-type for the type actually scored; never present effective-type conditional as if it were the published Top-1 conditional.
- Frozen Stage-1 distributions (006-style) with recovery → fallback uses the frozen ranked option list, not a re-inferred Choice, unless a non-frozen pair is explicitly selected.
- Synthesis / System-2 off (ranking-only) → recovery only affects evidence availability; no answer generation required for v1 acceptance.
- Resume-safe ledger → re-running the same recovery run id must not duplicate completed examples (constitution: auto-resume).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST continue to separate Stage-1 document-type Choice from Stage-2 passage ranking (constitution VII).
- **FR-002**: The system MUST report pipeline yield and empty rates as first-class outcomes alongside scored Stage-2 quality for matrix/eval analysis on the paper sample. For recovery-enabled runs, analysis MUST report **both** (a) original Choice Top-1 empty rate (comparable to published baselines) and (b) **post-recovery** empty rate / yield after optional type fallback (effective type).
- **FR-003**: By default, empty Top-1 pools MUST behave as today (no automatic type fallback) so published baselines remain reproducible.
- **FR-004**: Operators MUST be able to enable an **opt-in** yield-recovery mode that, when Top-1 type has no candidates, tries **all** subsequent Choice-ranked types in rank order and selects the **first type with a non-empty candidate pool** (or leaves empty if none). Recovery MUST NOT consult gold Stage-1 labels when choosing the fallback type.
- **FR-005**: When recovery changes the effective type, the system MUST record the original Top-1 type, the effective type used for Stage-2, and that a fallback occurred (for audit and inspect).
- **FR-006**: Recovery MUST fail closed: if no type yields candidates, the example remains empty/unscored for Stage-2; the system MUST NOT invent passages or skip the empty outcome.
- **FR-007**: Yield-recovery evaluation on the paper holdout MUST write artifacts under new run/pair identifiers and MUST NOT overwrite `paper-n200-full*`, `paper-p1-ceilings-n200*`, or `unsloth-score-paper-n200*`.
- **FR-008**: Analysis for recovery runs MUST present comparison to read-only published baseline yield / pipeline metrics on the same N=200 seed-42 sample.
- **FR-009**: Routing class accounting MUST remain reconcilable (empty vs wrong type vs scored) when recovery is enabled, with an explicit rule for “fallback used” examples.
- **FR-011**: For recovery-enabled runs, Stage-2 analysis MUST report **conditional-on-Choice-Top-1** with the same meaning as published baselines (conditioned on original Top-1 ∈ gold) **and**, when effective type ≠ Choice Top-1, a separate **conditional-on-effective-type** series; labels MUST make the distinction explicit.
- **FR-010**: Yield recovery MUST work with both live Choice engines and frozen Choice rankings (reuse ranked option lists) so 006-style frozen Stage-1 evals can opt in without re-running Choice GPU by default.
- **FR-012**: v1 acceptance MUST demonstrate recovery on **at least two** Stage-2 paths on the paper N=200 holdout: (a) a Lux Score twin comparable to a published Block B / shortlist row, and (b) a tuned Unsloth Score path comparable to `lux-unsloth-score`.

### Key Entities

- **Empty pool**: Stage-2 candidate set after type filter has size zero for the selected filing type.
- **Pipeline yield (post-recovery)**: Fraction of examples that produce a non-empty Stage-2 ranking list after optional type fallback.
- **Original Top-1 empty rate**: Fraction where the Choice Top-1 type alone has no candidates (baseline-comparable; unchanged by whether fallback later succeeds).
- **Yield recovery / type fallback**: Using a lower-ranked Choice option’s type pool when Top-1 is empty.
- **Effective type**: Filing type actually used for Stage-2 after optional recovery.
- **Baseline holdout**: Published seed-42 N=200 `selected_example_ids` from `paper-n200-full`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On the paper N=200 holdout, an opt-in recovery run reduces **post-recovery** empty rate versus the no-recovery Lux Choice empty baseline **or** documents with counts why remaining empties are corpus-limited (no chunks for any Choice option). The same report MUST still show original Top-1 empty rate for side-by-side comparison with published baselines.
- **SC-002**: On the same holdout, **post-recovery** pipeline Stage-2 quality (empties as zero after fallback) improves versus the no-recovery baseline when recovery finds non-empty pools on a non-trivial share of previously empty examples (target: recovery applies to **≥10%** of the 200 examples, or the run report explains a lower rate with class counts).
- **SC-003**: Default (recovery off) reproduces original Top-1 empty rate within **1 percentage point** of published Lux Choice empty rate on the same sample (~40.5% on `paper-n200-full`).
- **SC-004**: 100% of recovery-enabled examples that change effective type have an inspectable audit trail (original Top-1, effective type, fallback flag).
- **SC-005**: Published baseline artifact checksums for `paper-n200-full.json` (and documented companion paper artifact stems) remain unchanged after a recovery eval run.
- **SC-006**: Operators can distinguish “Score failed” from “no evidence after routing/recovery” in analysis without reading implementation code.
- **SC-007**: Acceptance artifacts include recovery results for both a Lux Score twin and a tuned Unsloth Score path on the same paper N=200 holdout (new run/pair ids only).

## Assumptions

- FinAgentBench ICAIF dump and published `paper-n200-full` matrix remain the comparison anchors.
- v1 recovery policy is **ordered Choice fallback** (not multi-type union pools, not corpus re-indexing) — corpus coverage improvements may be recommended in analysis but are out of scope as a data-engineering project in this feature.
- Ranking-only eval is sufficient for v1 acceptance; answer synthesis is out of scope (see #13 / #4).
- v1 acceptance MUST include recovery-enabled evals for **(1)** a published-style Lux Score twin and **(2)** a tuned Unsloth Score path; additional IR heads (E5/BM25) are optional extras, not required for close.
- Conditional Stage-2 metrics use dual reporting (Choice-Top-1 vs effective-type); v1 MUST not hide fallback behind inflated or redefined published conditional scores.
- Latency ladder (#11) and multi-seed (#14) are out of scope for this feature’s acceptance.
