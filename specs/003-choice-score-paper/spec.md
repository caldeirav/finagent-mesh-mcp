# Feature Specification: Paper-Ready Choice/Score Matrix & Analysis Report

**Feature Branch**: `003-choice-score-paper`

**Created**: 2026-10-05

**Status**: Draft

**Input**: User description: "Implement Block A (Stage-1 Choice ablation with fixed long-context Score) and Block B (Stage-2 Score ablation with fixed Choice) plus a comprehensive analysis report providing reviewer-needed metrics, findings/analysis, and links to every detailed record-by-record run for investigation. Position results for a research paper claiming typed Choice then Score is a meaningful architecture for financial agents."

## Clarifications

### Session 2026-10-05

- Q: Which optional Stage-2 rows should this feature implement now, versus leave for a later paper draft? → A: Shortlist dual-encoder + one-shot generative only; trained dual-encoder heads and cross-encoder deferred, tracked as [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)
- Q: For publishable runs of at least 200 seeded examples, should frontier answer synthesis run by default on the full sample, on a cheaper subset, or should ranking-only be the default? → A: Ranking-only by default; synthesis only when the operator opts in
- Q: Which dense passage scorer should the required Block B bi-encoder row use as the fixed open Choice’s Stage-2 partner? → A: General-domain dense bi-encoder (E5/GTE-class)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Isolated Stage-1 Choice ablation (Block A) (Priority: P1)

A researcher runs a comparison in which **only the filing-type chooser changes**. Every row uses the same long-context passage scorer. The table answers: which compact Choice head routes SEC filing types well enough that later passage ranking is not capped by a wrong Top-1 type.

**Why this priority**: Without a fixed Stage-2 partner, Stage-1 differences cannot be published; prior runs confounded routing with an incomplete or truncated scorer.

**Independent Test**: Execute Block A on a seeded FinAgentBench sample; confirm every required Block A pair shares the same Stage-2 scorer identity in the report, and Stage-1 ranking metrics plus Top-1 routing recall differ by pair.

**Acceptance Scenarios**:

1. **Given** Block A is selected, **When** the matrix runs, **Then** pairs include at least: strong open Choice + long-context Score, order-debiased Choice + same Score, low-latency Choice + same Score, edge Choice + same Score, and generative JSON Choice + same Score.
2. **Given** Block A completes, **When** the researcher reads Stage-1 metrics, **Then** they can compare filing-type ranking quality **without** attributing Stage-2 differences to different scorers.
3. **Given** an order-debiased Choice row, **When** results are reported, **Then** option-flip / position-bias rate is shown alongside ranking metrics.
4. **Given** the generative JSON Choice row, **When** it fails to emit a valid ranking, **Then** parse failures are counted and the example is fail-closed (no invented type ranks).

---

### User Story 2 - Isolated Stage-2 Score ablation (Block B) (Priority: P1)

A researcher runs a comparison in which **only the passage scorer changes**. Every row uses the same strong open Choice head for filing type. The table answers: how should a financial agent rank long enumerated passages after type routing—joint Score heads, dual-encoder cache, lexical floor, dense retrieval, optional shortlist-then-cache, optional cross-encoder ceiling, optional one-shot generative ranking of all chunks.

**Why this priority**: This is the paper’s central systems claim: typed two-stage retrieval vs stuffing, and System-1 Score vs classical IR.

**Independent Test**: Execute Block B on the same seeded sample as Block A; confirm every required Block B pair shares the same Stage-1 engine identity, and Stage-2 ranking metrics are reported both overall and **conditional on correct Top-1 type**.

**Acceptance Scenarios**:

1. **Given** Block B is selected, **When** the matrix runs, **Then** required rows include at least: same Choice with long-context Score, same Choice with dual-encoder cached Score, same Choice with lexical passage ranking, and same Choice with a dense bi-encoder scorer.
2. **Given** optional Block B rows are enabled, **When** they run, **Then** they include: dual-encoder on a shortlist and a one-shot generative ranker over all chunks with no separate Choice stage. Trained dual-encoder heads and bi-encoder→cross-encoder rerank are **out of scope** for this feature (tracked as follow-up issues).
3. **Given** Stage-2 nDCG@5 (or MAP/MRR), **When** gold chunks sit outside the Top-1 type, **Then** the report still shows overall scores **and** scores restricted to examples whose Top-1 type matches gold, so routing error is not blamed on the scorer.
4. **Given** a one-shot generative row, **When** it is included, **Then** it is labeled as violating the two-stage retrieval contract and is a **baseline**, not a production pair.

---

### User Story 3 - Paper analysis report with investigation links (Priority: P1)

After a matrix run, a researcher opens one **analysis report** that is usable in a paper draft: claims, metrics reviewers expect, findings, caveats, and **links from every pair to every example’s record** (expected labels vs model inputs/outputs). A reviewer can go from a table cell to the underlying example without rerunning models.

**Why this priority**: Metrics without reconstruction are not publishable; the prior inspect HTML is the investigation surface this report must index.

**Independent Test**: Build the analysis report from an existing completed matrix run (no re-inference); open it and follow a pair → example link to expected labels and Stage-1/Stage-2 (and synthesis, if present) I/O.

**Acceptance Scenarios**:

1. **Given** a completed matrix run, **When** the analysis report is generated, **Then** it includes Block A and Block B tables (or notes which pairs were skipped), reviewer metrics listed in FR-010, a findings section that does not treat a shared Stage-2 partner as a Stage-2 model bake-off, and an artifact index.
2. **Given** the analysis report, **When** the researcher clicks (or follows) an example identifier, **Then** they reach the detailed record for that pair and example, including expected filing types / chunk ids, predicted ranks, and captured decision I/O.
3. **Given** examples with empty Top-1 type chunks or ranking failures, **When** the report is generated, **Then** those cases appear in an error/pre-filter section with the same investigation links—not only successful nDCG rows.
4. **Given** the researcher rebuilds the report from a saved run id, **When** no engines are started, **Then** metrics and links still generate from stored traces and labels.

---

### User Story 4 - Default paper set vs optional expensive rows (Priority: P2)

An evaluation operator can run a **default paper matrix** that is large enough to support claims without requiring every optional IR or training row, and can add optional rows without changing Block A/B identity of required pairs.

**Why this priority**: Full Block B (fine-tune, cross-encoder, one-shot) may be GPU-days; the paper still needs a frozen default.

**Independent Test**: List pairs: default set matches required Block A + required Block B; optional pairs are absent unless explicitly included.

**Acceptance Scenarios**:

1. **Given** a default real matrix run, **When** pairs are resolved, **Then** required Block A and required Block B rows run, overlapping `lux`+long-context Score appears once, and optional rows are skipped.
2. **Given** the operator opts in to optional pairs, **When** the run proceeds, **Then** optional rows are added without renaming required pair identities.

---

### Edge Cases

- Dataset smaller than the requested sample: run all available examples, report actual N, do not silently pad.
- Gold type never appears in the example’s chunks: Stage-1 can still rank types; Stage-2 conditional metrics exclude or separately flag these examples.
- Stage-2 list length 0 after Top-1 filter: count as pre-filter failure; investigation record still written.
- Optional pair missing weights, calibration file, or held-out training split: skip that pair with an explicit skip reason in the report; do not substitute a different engine.
- One-shot generative baseline cannot emit a full permutation of chunks: record parse/coverage failure; do not invent remaining ranks.
- Order-debiased Choice unavailable: skip that Block A row with reason; do not silently drop OFR from the paper metric list for rows that did run.
- Synthesis disabled: ranking and analysis report still complete; answer EM/F1 section shows “not run.”
- Rebuilding analysis after ledger rotation: fail clearly if traces for a pair/example are missing rather than fabricating I/O.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The evaluation catalog MUST define **Block A** as Stage-1 Choice variants with a **single shared long-context Score** partner, covering: strongest open Choice, order-debiased Choice on the same backbone, low-latency Choice, edge Choice, and generative JSON Choice.
- **FR-002**: The evaluation catalog MUST define **Block B** as Stage-2 Score variants with a **single shared open Choice** partner, covering required rows: long-context Score, dual-encoder cached Score, lexical Score, and a **general-domain dense bi-encoder** Score (E5/GTE-class).
- **FR-003**: Optional Block B rows in this feature MUST be first-class catalog entries (not ad-hoc scripts) for: (1) dual-encoder on a shortlist, and (2) one-shot generative ranking of all chunks. Trained dual-encoder heads and dense-then-cross-encoder MUST NOT be implemented here; they MUST remain tracked as open follow-up issues ([#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1), [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)) and listed as skipped/deferred in the analysis report when referenced.
- **FR-004**: Default real evaluation MUST run all **required** Block A and Block B pairs and MUST NOT run optional pairs unless the operator opts in.
- **FR-005**: Pair identity MUST remain stable across reports (same pair id means same Stage-1 and Stage-2 roles); the long-context same-engine pair MAY appear in both blocks as one physical run.
- **FR-006**: Stage-1 and Stage-2 for each example MUST execute in one end-to-end agentic process except the explicit one-shot generative **baseline**, which MUST be labeled as collapsing stages.
- **FR-007**: Heavy engines MUST run **sequentially exclusive** across matrix rows (one heavy GPU configuration active per row); a shared Stage-2 partner MAY stay warm across Block A rows that use it.
- **FR-008**: Ranking MUST fail closed: no mock rankings, no silent engine substitution, no extractive answer fabrication when synthesis is required.
- **FR-009**: Fine-tuning of dual-encoder heads is **deferred** (follow-up issue). When later implemented, training MUST use a held-out split disjoint from the reported test sample and MUST be labeled as such; this feature MUST NOT claim trained-head Stage-2 results.
- **FR-010**: For each pair the system MUST record: Stage-1 nDCG@5, MAP@5, MRR@5; Stage-2 nDCG@5, MAP@5, MRR@5; Stage-1 Top-1 (and Top-5) type recall; pre-filter / empty-Top-1-chunk rate; Stage-2 metrics **conditional on correct Top-1 type**; latency p50 and p95 per stage; GPU memory high-water if available; option-flip rate for order-debiased Choice; parse-failure rate for generative rows; answer EM/F1 when synthesis ran.
- **FR-011**: The analysis report MUST include: research questions, Block A table, Block B table, routing-vs-scoring decomposition, latency/resource table, findings that a non-expert researcher can paste toward a paper, limitations/threats to validity, and an index linking every pair × example to its detailed investigation record.
- **FR-012**: Detailed records MUST show expected filing-type and chunk labels versus model inputs/outputs for Stage 1, Stage 2, and synthesis when present, including failed and empty-filter examples.
- **FR-013**: Operators MUST be able to generate or regenerate the analysis report and investigation index from a saved run identifier without re-running models.
- **FR-014**: Publishable runs MUST use a seeded sample of at least **200** examples unless the operator explicitly requests a smoke size; the report MUST print N, seed, and dataset revision. Default publishable runs MUST be **ranking-only** (no frontier answer synthesis). Synthesis and answer EM/F1 MUST run only when the operator explicitly opts in; when synthesis did not run, the analysis report MUST state answer metrics as “not run.”
- **FR-015**: AnyJev L1 (temperature calibration on ~200 held-out ids) MUST remain optional until calibration artifacts exist; it is not required for Block A in this feature.
- **FR-016**: Hosted closed decision APIs MUST remain out of scope; comparisons are against FinAgentBench labels and open/local rows only.

### Key Entities

- **Evaluation pair**: Named Stage-1 × Stage-2 (or one-shot baseline) assignment with block membership (A, B, optional) and a human rationale suitable for a paper table caption.
- **Matrix run**: Seeded execution over N examples producing per-pair aggregates and per-example traces.
- **Routing outcome**: Top-1/Top-5 predicted filing type vs gold; whether Stage-2 saw any chunks.
- **Scoring outcome**: Predicted chunk ranking vs gold chunk ids, overall and conditional on routing.
- **Investigation record**: Per pair × example payload of expected labels, truncated passage texts, decision I/O, errors.
- **Analysis report**: Narrative + tables + findings + hyperlinks (or path index) into investigation records.
- **Skip record**: Optional pair not run, with reason (missing calibration, weights, opt-in flag).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A researcher can produce Block A and Block B result tables in which **exactly one stage** is the experimental factor, verified by the report listing a shared partner identity per block.
- **SC-002**: A reviewer given only the analysis report can recover, for every evaluated example, expected labels and that example’s decision I/O in **under two minutes** via published links or paths (no extra model calls).
- **SC-003**: Default paper-sized runs process **≥ 200** seeded examples (or the full set if smaller), state N and seed on the first page of the report, and complete without calling frontier synthesis unless opted in.
- **SC-004**: At least **90%** of completed examples in a successful pair have an investigation record; every failed/pre-filter example in that pair is listed with an error reason and a record or an explicit “trace missing” marker.
- **SC-005**: Findings text never attributes Stage-2 ranking differences across Block A rows to different scorers when the scorer was held fixed (spot-check: Block A Stage-2 partner names are identical).
- **SC-006**: An operator can rebuild the analysis report from a saved run in **under 5 minutes** of wall time without starting decision engines.
- **SC-007**: Optional rows, when skipped, appear as skipped with reasons so a paper draft cannot silently omit a listed baseline.

## Assumptions

- Existing real-engine serving, fail-closed Gemini, sequential exclusive GPU, and per-example inspect records remain the substrate; this feature **rebinds the catalog** and **elevates analysis**, not a new agent graph.
- The shared Block A Stage-2 partner is the strongest open **long-context Score** already used in production (Lux-class), not the dual-encoder.
- The shared Block B Stage-1 partner is the strongest open **Choice** (Lux-class).
- Lexical Stage-2 means ranking chunk text with a classical term-matching method against the query (BM25-class), not a mock System-1 sidecar.
- Dense Stage-2 for the required Block B row is a **general-domain** passage bi-encoder (E5/GTE-class), not a finance-tuned or dual-encoder-backbone-only embedder.
- Dual-encoder cached Score is the existing Contrastive-LM / Action Cache path (2k context unless shortlisted).
- Shortlist size default of 32 for the in-scope shortlist dual-encoder optional row.
- One-shot generative ranking is an in-scope **baseline** (not a System-1 production pair). Cross-encoder rerank is a deferred **ceiling** (follow-up issue), not implemented in this feature.
- Smoke small-N runs remain available; they are not publishable.
- Default paper-sized runs skip frontier synthesis; operators opt in when they want EM/F1.
- Calibration for order-debiased L1 stays skipped until the held-out file is complete.
- Secrets and raw eval artifacts stay uncommitted; reports may live under the existing artifacts directory.
- Users of the report are researchers drafting a systems/IR paper on financial agentic retrieval, not end-user traders.
