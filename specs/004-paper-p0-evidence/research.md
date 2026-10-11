# Research: Paper P0 Evidence Pack

**Feature**: `004-paper-p0-evidence` | **Date**: 2026-10-09

## 1. Primary vs pipeline-averaged Stage-2

**Decision**: Keep **primary** S2 nDCG/MAP/MRR as mean over examples with a non-empty Stage-2 ranking list (**scored-only**). Add required secondary series **`stage2_*_pipeline`** (nDCG@5 and MRR@5 minimum): average over all N examples, contributing **0** when empty-Top-1 / no ranks.

**Rationale**: Clarification A; matches current aggregator behavior for primary; gives an end-to-end “agent yield” number without poisoning scorer comparisons.

**Alternatives considered**: Only scored-only (rejected: clarification requires secondary); replace primary with pipeline-averaged (rejected: misstates scorer quality).

## 2. Routing accounting classes

**Decision**: Mutually exclusive per-example classes for each pair:

| Class id | Definition |
|----------|------------|
| `correct_top1_scored` | Top-1 type correct AND non-empty type-filtered chunk list AND Stage-2 ranks present |
| `correct_top1_empty` | Top-1 type correct AND empty type-filtered chunk list |
| `wrong_top1_scored` | Top-1 type incorrect AND Stage-2 ranks present (wrong-type pool) |
| `wrong_top1_empty` | Top-1 type incorrect AND empty type-filtered chunk list |
| `missing_top1` | No Top-1 type predicted |
| `other` | Residual (parse/ledger anomalies) |

**Pipeline yield** = (`correct_top1_scored` + `wrong_top1_scored`) / N.  
Report class counts/rates beside Top-1 recall and empty-Top-1 rate; narrative MUST use these counts (not “empty ⇒ wrong type”).

**Rationale**: Explains ~94% Top-1 recall vs ~40% empty on `paper-n200-full`.

**Alternatives considered**: Binary empty vs not (rejected: cannot reconcile recall); gold-in-pool checks only (still needed inside `wrong_top1_scored` for optional notes, but not required as separate class for P0 tables).

## 3. Bootstrap CIs

**Decision**: Nonparametric bootstrap over **examples** (resample with replacement of per-example metric contributions), B≥1000, report percentile 95% CI for pair metrics and for Δ(pair − lux-lux) on Stage-1 nDCG@5 (Block A) and Stage-2 nDCG@5 / MRR@5 (Block B, primary scored-only). Fixed RNG seed for reproducibility (e.g. `bootstrap_seed = sample_seed`).

**Rationale**: Spec FR-008; example-level resampling matches IR reporting practice for mean nDCG.

**Alternatives considered**: Analytic SE (rejected: skewed metrics); pair-of-pairs only without CI (rejected by spec).

## 4. Multi-seed protocol

**Decision**: Independent N=200 draws for seeds `{42, 7, 123}` on core pairs `{lux-lux, anyjev-l0-lux, lux-e5, lux-bm25}`, ranking-only. Seed 42 may reuse `paper-n200-full` rows for those pairs. Across-seed summary: per-seed value, mean of seed means, min–max. No pooled multi-seed bootstrap.

**Rationale**: Clarifications on independent samples and mean+range.

**Alternatives considered**: Frozen example ids (rejected); full 8-pair × 3 seeds (deferred for GPU cost).

## 5. Win/tie/loss vs Lux Score

**Decision**: Among examples scored by **both** Lux Score (`lux-lux`) and challenger (`lux-bm25` / `lux-e5` / `lux-clm` when present), compare per-example Stage-2 nDCG@5. Win if challenger − Lux ≥ 0.01; loss if Lux − challenger ≥ 0.01; else tie. Extreme samples: top-k by |Δ| with inspect links. Align examples by `example_id` within the same sample/seed.

**Rationale**: Clarification A; Block B shares Lux Choice so example ids align on seed-42 published sample.

**Alternatives considered**: MRR-based wins (rejected); require both nDCG and MRR (rejected).

## 6. Strata buckets

**Decision**:

- **Gold filing type**: Top-1 gold Stage-1 label (or primary gold type if multi-label—use harness’s existing top gold type convention).
- **Candidate list size** after type filter (for Lux Choice pairs): buckets `{1–8, 9–32, 33–128, 129+}` (empty excluded from strata).
- **Length**: total characters of Stage-2 candidate texts, buckets by quartiles computed on the scored set for that seed (or fixed cutpoints documented in analysis JSON).

Report mean S2 nDCG@5 per scorer per cell with N.

**Rationale**: Spec FR-006; quartile length adapts to dump scale.

**Alternatives considered**: Fixed length cutpoints only (ok as fallback if quartile ties); query-length only (weaker for long filings).

## 7. Synthesis ranking reuse

**Decision**: Do **not** re-run Choice/Score. For pairs `{anyjev-l0-lux, lux-lux, lux-e5, lux-bm25}` on seed 42 / published sample, load ranking payloads (and chunk texts) from ledger/inspect for the corresponding eval_run_ids (including merged `paper-n200-full` sources), set examples to synthesis-eligible state, call Gemini with existing top-K policy, score answers, persist synthesis payloads. Skip empty-Top-1 / missing chunk text with explicit counters.

**Rationale**: Clarification A; harness already has `synthesis_retriable` + ranking_payload resume patterns.

**Alternatives considered**: Full pipeline re-run (rejected); synthesis-only new run_id that orphans ranking metrics (rejected—must attach to published rankings).

## 8. Optional baselines

**Decision**: Run `--include-optional` (or explicit `--pairs lux-clm-shortlist,one-shot-ar`) on same N=200 seed=42 ranking-only; merge into analysis alongside required rows; label `one-shot-ar` as collapsed baseline; print shortlist K for `lux-clm-shortlist`. Keep #1/#2 deferred.

**Rationale**: Spec US5 / FR-011–012; catalog already defines pairs.

**Alternatives considered**: Defer optionals to P1 (rejected: in P0 scope).

## 9. Artifact layout

**Decision**: Continue writing under `artifacts/benchmarks/`; primary published analysis stem remains regenerable for `paper-n200-full`. Multi-seed: separate matrix run ids per seed (e.g. `paper-n200-s7-core`, `paper-n200-s123-core`) plus a rollup section or small `*.multiseed.json` referenced from analysis. Synthesis may use a sibling run id (e.g. `paper-n200-full-synth`) that references ranking source run ids in metadata.

**Rationale**: Matches existing artifact conventions; avoids rewriting history of `paper-n200-full` ranking metrics.

**Alternatives considered**: Overwrite `paper-n200-full` in place with synthesis (riskier for ranking immutability).
