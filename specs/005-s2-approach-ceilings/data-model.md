# Data Model: Stage-2 Approach Ceilings (005)

## EngineConfiguration (extensions)

| Field | Notes for P1 |
|-------|----------------|
| `config_id` | `lux-score-shortlist-32`, `e5-ce-shortlist-32` |
| `family` | `hybrid-ir` (both) |
| `backend` | `lux_shortlist` \| `e5_ce_shortlist` |
| `weights_ref` | CE: `${CE_WEIGHTS:-cross-encoder/ms-marco-MiniLM-L6-v2}`; E5 half uses existing E5 weights |
| `is_heavy_gpu` | false for in-process hybrids; Lux dependency still starts sidecar via ports |
| `shortlist_k` | Documented default 32; runtime env `LUX_SHORTLIST_K` / `CE_SHORTLIST_K` |

## MatrixPair (extensions)

| pair_id | stage1 | stage2 | blocks | optional | role | deferred |
|---------|--------|--------|--------|----------|------|----------|
| `anyjev-l0-e5` | anyjev-l0 | e5-base | [] or [champion] | true | champion | false |
| `anyjev-l0-bm25` | anyjev-l0 | bm25-stage2 | [] | true | champion | false |
| `lux-lux-shortlist` | decision20-lux | lux-score-shortlist-32 | [B] | true | optional | false |
| `lux-e5-ce` | decision20-lux | e5-ce-shortlist-32 | [B] | true | ir_ceiling | false |

`lux-e5-ce` **removed** from `deferred_pairs`. `lux-clm-ft` remains deferred (#1).

## HybridScoreResult (runtime, not persisted as new table)

Adapter `decide()` return shape unchanged: `ranking[{id,score,rank}]`, `distribution`, optional `latency_ms`, metadata tags:

- `shortlist_k`, `shortlist_method` (`bm25` \| `e5`), `rerank_method` (`lux` \| `cross_encoder`)
- `n_candidates`, `n_shortlisted`

Logged to MLflow tags / inspect synthesis-adjacent Stage-2 blobs via existing ranking payload.

## AnalysisReport (extensions)

| Section | Content |
|---------|---------|
| Champion / compound | Metrics for S8 pairs + deltas vs `anyjev-l0-lux`, `lux-e5`, `lux-bm25` |
| P1 ceilings | `lux-lux-shortlist`, `lux-e5-ce`: S2 nDCG/MRR (scored + conditional), latency, shortlist_k, CE model id |
| Limitations | #1 deferred; #2 delivered when `lux-e5-ce` measured |

## SkipRecord

Unchanged schema. Reasons: `optional_not_requested`, `missing_weights`, `engine_unhealthy`. `deferred_issue` only for remaining deferred (`lux-clm-ft`).
