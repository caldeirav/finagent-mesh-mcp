# Research: Stage-2 Approach Ceilings (005)

## R1 — Champion cells vs orthogonal matrix

**Decision**: Add `anyjev-l0-e5` and `anyjev-l0-bm25` as `optional: true` with `role: champion` (or `compound`). Report in a dedicated Champion section; do not put them in Block A or Block B tables that assume a single fixed partner.

**Rationale**: Spec 003 orthogonal design confounds compound gains. Champions answer the systems question after P0 showed AnyJev best Choice and E5/BM25 best Score.

**Alternatives considered**: Full factorial Choice×Score (rejected: GPU cost); only document hypothetical compounds (rejected: no evidence).

## R2 — S2b shortlist method

**Decision**: BM25 top-`LUX_SHORTLIST_K` (default 32) then Lux Score via existing Decision-2.0 Lux Stage-2 HTTP adapter. Engine id `lux-score-shortlist-32`; pair `lux-lux-shortlist`.

**Rationale**: Mirrors proven `clm_shortlist` / `lux-clm-shortlist`; isolates “shortlist helps ordinal Score” without introducing E5 into the Lux hybrid (E5 shortlist would confound with dense retrieval).

**Alternatives considered**: E5→Lux shortlist (deferred); k=16/64 (default 32 for parity with CLM shortlist).

**Tail policy**: Same as CLM shortlist—append non-shortlisted candidates with sentinel low scores so the rank list covers the pool; metrics consumers treat ordering honestly (document in adapter docstring).

## R3 — S7 cross-encoder choice

**Decision**: In-process `sentence_transformers.CrossEncoder` with pretrained `cross-encoder/ms-marco-MiniLM-L6-v2` (override via `CE_WEIGHTS` / engine `weights_ref`). Pipeline: E5 rank Top-1-type chunks → take top-K (default 32) → CE rerank shortlist → append tail. Engine `e5-ce-shortlist-32`; pair `lux-e5-ce` removed from `deferred_pairs`.

**Rationale**: Small CE is ARM/Spark-friendly; already depend on sentence-transformers for E5; closes #2 without training. MiniLM-L6 is a standard IR ceiling baseline.

**Alternatives considered**: Larger CE (ms-marco-MiniLM-L12 / bge-reranker) — optional later via env; train CE with Unsloth (out of scope; see #5); BM25→CE without E5 (weaker narrative vs current E5 leader).

## R4 — Ports / sidecars

**Decision**: Extend `sidecar_dependencies` so `lux-score-shortlist` backends require `decision20-lux` on Stage-2 port. `e5-ce-shortlist` is fully in-process (no extra GPU sidecar) but Stage-1 still needs Lux Choice sidecar for `lux-e5-ce` and AnyJev for champions.

**Rationale**: Matches `clm_shortlist` → `clm-8b` dependency pattern.

## R5 — Analysis labeling

**Decision**: Analysis gains (1) Champion / compound table for S8 pairs vs reference `anyjev-l0-lux`, `lux-e5`, `lux-bm25`; (2) P1 ceilings subsection for `lux-lux-shortlist` and `lux-e5-ce` with latency; (3) limitations: remove #2 from deferred-unimplemented; keep #1.

**Rationale**: Spec FR-002 / FR-011; prevents Block A/B mis-attribution.

## R6 — Explicit non-goals (reaffirmed)

**Decision**: Do not implement AnyJev L1, CLM-ft (#1), Top-k types, Unsloth FastDecisionModel (#5), or LLM judge (#4) in this feature.

**Rationale**: Short-timeline Nano delivery; prior feasibility assessment.
