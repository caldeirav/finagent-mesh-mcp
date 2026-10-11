# Paper analysis — paper-p1-ceilings-n200

## Executive summary

- **Best Choice router (Block A):** `anyjev-l0-lux` with Stage-1 nDCG@5 = 0.8625 (Top-1 filing-type recall 95.1%).
- **Best passage scorer (Block B, overall S2 nDCG@5):** `lux-lux-shortlist` = 0.3517 (conditional-on-Top-1 0.3735).
- **Routing ceiling:** ~40.5% of examples under Lux Choice yield empty Stage-2 candidate sets — passage scoring cannot recover those misses.
- **Coverage:** 8/8 matrix pairs have measurable ranking metrics on N=200 (seed=42).

## How to read this report

1. **Block A** varies the Stage-1 **Choice** router; Stage-2 Score stays Lux. Higher S1 nDCG@5 / Top-1 recall = better filing-type routing.
2. **Block B** varies the Stage-2 **Score** (or dense/lexical) head; Stage-1 Choice stays Lux. Compare overall S2 nDCG@5 (full pipeline) and **S2 nDCG@5|Top-1** (scorer only, when Top-1 type was correct).
3. **`empty_top1_chunks`** means no type-filtered Stage-2 candidates (see Routing accounting — not always wrong Top-1). Primary S2 metrics are **scored-only**; **pipeline-averaged** treats empties as 0.

## Run facts

- **N**: 200
- **Seed**: 42
- **Dataset**: `data/finagentbench`
- **Synthesis**: not run (ranking-only)
- **Status**: completed

## Research questions

1. Which Choice head routes SEC filing types well (Block A)?
2. How should agents score long passages after type routing (Block B)?
3. Does typed Choice→Score beat one-shot stuffing (optional baseline)?

## Block A — Stage-1 Choice (Lux Score fixed)

| Pair | S1 engine | S1 nDCG@5 | Δ vs Lux | Top-1 recall | OFR | Parse fail | S1 p50 ms |
|---|---|---|---|---|---|---|---|
| anyjev-l0-lux | anyjev-l0 | 0.8625 | +0.0212 | 0.9509 | 0.0900 | 0.0000 | 791.0231 |
| lux-lux | decision20-lux | 0.8413 | +0.0000 | 0.9387 | — | 0.0000 | 169.2432 |

### Block A findings

- Ranked by Stage-1 nDCG@5 (filing-type ranking quality). Lux Choice baseline (`lux-lux`) is 0.8413.
- 1. **`anyjev-l0-lux`** (`anyjev-l0`) — nDCG@5 0.8625 (+0.0212 vs Lux), Top-1 recall 95.1%, S1 p50 791.0231 ms, option-flip rate 9.0%.
- 2. **`lux-lux`** (`decision20-lux`) — nDCG@5 0.8413 (+0.0000 vs Lux), Top-1 recall 93.9%, S1 p50 169.2432 ms.
- AnyJev L0 reports order sensitivity: OFR = 9.0% (fraction of examples whose top Choice flips when options are permuted).

## Champion / compound (S8)

These cells combine **best Choice** (AnyJev L0) with **classical IR Score** (E5 / BM25). They are **not** orthogonal Block A/B rows — do not read Stage-2 deltas as a Lux Score bake-off.

| Pair | S1 nDCG@5 | Top-1 recall | Empty | Yield | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | Δ S2 vs same IR (Lux Choice) | Δ S2 vs anyjev-l0-lux |
|---|---|---|---|---|---|---|---|---|---|---|
| anyjev-l0-e5 | 0.8625 | 0.9509 | 0.3600 | 0.6000 | 0.2868 | 0.5060 | 0.3153 | 0.1721 | +0.0044 | +0.0568 |
| anyjev-l0-bm25 | 0.8625 | 0.9509 | 0.3600 | 0.6000 | 0.2740 | 0.4635 | 0.2927 | 0.1644 | +0.0091 | +0.0440 |

## Block B — Stage-2 Score (Lux Choice fixed)

| Pair | S2 engine | S2 nDCG (scored) | S2 MRR (scored) | Δ nDCG vs Lux | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | Empty Top-1 | S2 p50 ms |
|---|---|---|---|---|---|---|---|---|
| lux-lux-shortlist | lux-score-shortlist-32 | 0.3517 | 0.5824 | +0.1306 | 0.3735 | 0.1952 | 0.4050 | 3419.2340 |
| lux-e5-ce | e5-ce-shortlist-32 | 0.2496 | 0.4464 | +0.0284 | 0.2692 | 0.1385 | 0.4050 | 896.6003 |
| lux-bm25 | bm25-stage2 | 0.2648 | 0.4375 | +0.0437 | 0.2829 | 0.1470 | 0.4050 | 10.2259 |
| lux-e5 | e5-base | 0.2825 | 0.4959 | +0.0613 | 0.3127 | 0.1568 | 0.4050 | 861.5197 |
| lux-lux | decision20-lux | 0.2212 | 0.4053 | +0.0000 | 0.2326 | 0.1227 | 0.4050 | 14075.4844 |

### Block B findings

- Ranked by overall Stage-2 nDCG@5 (full pipeline after Lux Choice). Lux Score baseline (`lux-lux`) is 0.2212 (conditional 0.2326).
- 1. **`lux-lux-shortlist`** (`lux-score-shortlist-32`) — S2 nDCG@5 0.3517 (+0.1306 vs Lux), S2|Top-1 0.3735, empty-Top-1 40.5%, S2 p50 3419.2340 ms.
- 2. **`lux-e5`** (`e5-base`) — S2 nDCG@5 0.2825 (+0.0613 vs Lux), S2|Top-1 0.3127, empty-Top-1 40.5%, S2 p50 861.5197 ms.
- 3. **`lux-bm25`** (`bm25-stage2`) — S2 nDCG@5 0.2648 (+0.0437 vs Lux), S2|Top-1 0.2829, empty-Top-1 40.5%, S2 p50 10.2259 ms.
- 4. **`lux-e5-ce`** (`e5-ce-shortlist-32`) — S2 nDCG@5 0.2496 (+0.0284 vs Lux), S2|Top-1 0.2692, empty-Top-1 40.5%, S2 p50 896.6003 ms.
- 5. **`lux-lux`** (`decision20-lux`) — S2 nDCG@5 0.2212 (+0.0000 vs Lux), S2|Top-1 0.2326, empty-Top-1 40.5%, S2 p50 14075.4844 ms.
- E5 (general-domain dense) and/or BM25 beat Lux Score on overall passage nDCG here — surprising for a finance-specialized ordinal Score head; confirm on full FinAgentBench and with finance-tuned dense/CE ceilings.

## P1 ceilings (S2b shortlist-Lux + S7 CE)

`lux-lux-shortlist`: BM25 top-K then Lux Score. `lux-e5-ce`: E5 shortlist then **pretrained CrossEncoder** (IR ceiling / baseline — not a production System-1 Score head).

| Pair | Role | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\|Top-1 | Δ vs lux-lux | Δ vs lux-e5 | S2 p50 ms | S2 p95 ms |
|---|---|---|---|---|---|---|---|---|
| lux-lux-shortlist | optional | 0.3517 | 0.5824 | 0.3735 | +0.1306 | +0.0693 | 3419.2340 | 3639.0994 |
| lux-e5-ce | IR ceiling | 0.2496 | 0.4464 | 0.2692 | +0.0284 | -0.0329 | 896.6003 | 2300.6152 |

## Routing accounting

Mutually exclusive classes reconcile Top-1 recall vs empty-Top-1. **Pipeline yield** = fraction of examples with a Stage-2 ranking list. Primary Stage-2 nDCG/MRR are **scored-only** means; **pipeline-averaged** treats empty/unscored as 0.

| Pair | N | Top-1 recall | Empty rate | Yield | correct_scored | correct_empty | wrong_scored | wrong_empty | missing/other |
|---|---|---|---|---|---|---|---|---|---|
| anyjev-l0-e5 | 200 | 0.9509 | 0.3600 | 0.6400 | 95 | 60 | 33 | 12 | 0 |
| anyjev-l0-bm25 | 200 | 0.9509 | 0.3600 | 0.6400 | 95 | 60 | 33 | 12 | 0 |
| lux-lux-shortlist | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| lux-e5-ce | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| anyjev-l0-lux | 200 | 0.9509 | 0.3600 | 0.6400 | 95 | 60 | 33 | 12 | 0 |
| lux-bm25 | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| lux-e5 | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| lux-lux | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 66 | 33 | 15 | 0 |

## Stage-2 metric series (scored vs pipeline)

| Pair | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | S2 MRR (pipeline) |
|---|---|---|---|---|---|
| anyjev-l0-e5 | 0.2868 | 0.5060 | 0.3153 | 0.1721 | 0.3036 |
| anyjev-l0-bm25 | 0.2740 | 0.4635 | 0.2927 | 0.1644 | 0.2781 |
| lux-lux-shortlist | 0.3517 | 0.5824 | 0.3735 | 0.1952 | 0.3233 |
| lux-e5-ce | 0.2496 | 0.4464 | 0.2692 | 0.1385 | 0.2477 |
| anyjev-l0-lux | 0.2300 | 0.4274 | 0.2427 | 0.1380 | 0.2564 |
| lux-bm25 | 0.2648 | 0.4375 | 0.2829 | 0.1470 | 0.2428 |
| lux-e5 | 0.2825 | 0.4959 | 0.3127 | 0.1568 | 0.2752 |
| lux-lux | 0.2212 | 0.4053 | 0.2326 | 0.1227 | 0.2249 |

_Footnote: **scored** = mean over examples with a Stage-2 ranking list; **pipeline** = mean over all N with empty/unscored as 0._

## Strata (Block B)

### By gold_type

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| 10-K | lux-lux | 72 | 0.2446 |
| 10-K | lux-bm25 | 72 | 0.2802 |
| 10-K | lux-e5 | 72 | 0.3258 |
| 10-Q | lux-lux | 10 | 0.2016 |
| 10-Q | lux-bm25 | 10 | 0.2866 |
| 10-Q | lux-e5 | 10 | 0.2156 |
| DEF14A | lux-lux | 2 | 0.1871 |
| DEF14A | lux-bm25 | 2 | 0.3614 |
| DEF14A | lux-e5 | 2 | 0.3331 |
| Earnings | lux-lux | 2 | 0.0000 |
| Earnings | lux-bm25 | 2 | 0.2853 |
| Earnings | lux-e5 | 2 | 0.3066 |
| unknown | lux-lux | 33 | 0.1378 |
| unknown | lux-bm25 | 33 | 0.1536 |
| unknown | lux-e5 | 33 | 0.1353 |

### By cand_size

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| 1-8 | lux-lux | 1 | 1.0000 |
| 1-8 | lux-bm25 | 1 | 0.4307 |
| 1-8 | lux-e5 | 1 | 0.4307 |
| 129+ | lux-lux | 60 | 0.1925 |
| 129+ | lux-bm25 | 60 | 0.1983 |
| 129+ | lux-e5 | 60 | 0.2450 |
| 33-128 | lux-lux | 51 | 0.2023 |
| 33-128 | lux-bm25 | 51 | 0.2811 |
| 33-128 | lux-e5 | 51 | 0.2788 |
| 9-32 | lux-lux | 7 | 0.2401 |
| 9-32 | lux-bm25 | 7 | 0.3908 |
| 9-32 | lux-e5 | 7 | 0.2862 |

### By length

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| Q1(≤3052) | lux-lux | 83 | 0.1810 |
| Q1(≤3052) | lux-bm25 | 2 | 0.2153 |
| Q1(≤3052) | lux-e5 | 5 | 0.2088 |
| Q2(≤5701) | lux-lux | 14 | 0.2839 |
| Q2(≤5701) | lux-bm25 | 40 | 0.1909 |
| Q2(≤5701) | lux-e5 | 35 | 0.2330 |
| Q3(≤6000) | lux-lux | 22 | 0.2523 |
| Q3(≤6000) | lux-bm25 | 77 | 0.2771 |
| Q3(≤6000) | lux-e5 | 79 | 0.2804 |


## Win/tie/loss vs Lux Score

Decided by per-example Stage-2 **nDCG@5**; `|Δ| < 0.01` counts as tie.

| Challenger | N compared | Wins | Ties | Losses |
|---|---|---|---|---|
| lux-e5 | 111 | 51 | 26 | 34 |
| lux-bm25 | 111 | 51 | 23 | 37 |

### Samples — `lux-e5`

**Wins:**
- `dev:q25119b32a2f9` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q25119b32a2f9))
- `dev:q84038a74fd59` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q84038a74fd59))
- `dev:qa602975e3d19` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:qa602975e3d19))
- `dev:q7c284aabbba4` Δ=0.9521 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q7c284aabbba4))
- `dev:q4d8ac905167b` Δ=0.9026 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q4d8ac905167b))

**Losses:**
- `dev:qe1811f4fd3dc` Δ=-1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:qe1811f4fd3dc))
- `dev:q8ba6a388d681` Δ=-0.8319 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q8ba6a388d681))
- `dev:q31f6fd1f392c` Δ=-0.7817 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:q31f6fd1f392c))
- `dev:qa5c748248a5b` Δ=-0.6716 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:qa5c748248a5b))
- `dev:qdec70f55027f` Δ=-0.5934 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ex-dev:qdec70f55027f))

### Samples — `lux-bm25`

**Wins:**
- `dev:q25119b32a2f9` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:q25119b32a2f9))
- `dev:q84038a74fd59` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:q84038a74fd59))
- `dev:q9dd3907388e3` Δ=1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:q9dd3907388e3))
- `dev:q4d8ac905167b` Δ=0.8304 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:q4d8ac905167b))
- `dev:q9a5cfe35fecd` Δ=0.7557 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:q9a5cfe35fecd))

**Losses:**
- `dev:qe1811f4fd3dc` Δ=-1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:qe1811f4fd3dc))
- `dev:qf8cbcec9fec6` Δ=-1.0000 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:qf8cbcec9fec6))
- `dev:qdec70f55027f` Δ=-0.7727 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:qdec70f55027f))
- `dev:qa5c748248a5b` Δ=-0.7429 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:qa5c748248a5b))
- `dev:chunk-only:qb7d1dfae8271` Δ=-0.6992 ([inspect](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25-ex-dev:chunk-only:qb7d1dfae8271))


## Uncertainty (bootstrap 95% CI)

| Id | Metric | Point | CI low | CI high | N |
|---|---|---|---|---|---|
| delta:anyjev-l0-e5-vs-lux-lux | stage1_ndcg_at_5 | 0.0162 | -0.0144 | 0.0487 | 163 |
| delta:anyjev-l0-e5-vs-lux-lux | stage2_ndcg_at_5 | 0.0657 | -0.0026 | 0.1361 | 111 |
| delta:anyjev-l0-bm25-vs-lux-lux | stage1_ndcg_at_5 | 0.0162 | -0.0144 | 0.0487 | 163 |
| delta:anyjev-l0-bm25-vs-lux-lux | stage2_ndcg_at_5 | 0.0528 | -0.0154 | 0.1266 | 111 |
| delta:lux-lux-shortlist-vs-lux-lux | stage1_ndcg_at_5 | -0.0050 | -0.0362 | 0.0267 | 163 |
| delta:lux-lux-shortlist-vs-lux-lux | stage2_ndcg_at_5 | 0.1306 | 0.0487 | 0.2066 | 111 |
| delta:lux-e5-ce-vs-lux-lux | stage1_ndcg_at_5 | -0.0050 | -0.0362 | 0.0267 | 163 |
| delta:lux-e5-ce-vs-lux-lux | stage2_ndcg_at_5 | 0.0284 | -0.0484 | 0.1024 | 111 |
| anyjev-l0-lux | stage1_ndcg_at_5 | 0.8625 | 0.8403 | 0.8849 | 163 |
| anyjev-l0-lux | stage2_ndcg_at_5_scored | 0.2300 | 0.1828 | 0.2823 | 120 |
| anyjev-l0-lux | stage2_mrr_at_5_scored | 0.4274 | 0.3489 | 0.5086 | 120 |
| delta:anyjev-l0-lux-vs-lux-lux | stage1_ndcg_at_5 | 0.0162 | -0.0144 | 0.0487 | 163 |
| delta:anyjev-l0-lux-vs-lux-lux | stage2_ndcg_at_5 | 0.0088 | -0.0624 | 0.0844 | 111 |
| lux-bm25 | stage1_ndcg_at_5 | 0.8413 | 0.8191 | 0.8631 | 163 |
| lux-bm25 | stage2_ndcg_at_5_scored | 0.2648 | 0.2190 | 0.3139 | 111 |
| lux-bm25 | stage2_mrr_at_5_scored | 0.4375 | 0.3667 | 0.5171 | 111 |
| delta:lux-bm25-vs-lux-lux | stage1_ndcg_at_5 | -0.0050 | -0.0362 | 0.0267 | 163 |
| delta:lux-bm25-vs-lux-lux | stage2_ndcg_at_5 | 0.0437 | -0.0336 | 0.1136 | 111 |
| lux-e5 | stage1_ndcg_at_5 | 0.8413 | 0.8191 | 0.8631 | 163 |
| lux-e5 | stage2_ndcg_at_5_scored | 0.2825 | 0.2312 | 0.3338 | 111 |
| lux-e5 | stage2_mrr_at_5_scored | 0.4959 | 0.4240 | 0.5742 | 111 |
| delta:lux-e5-vs-lux-lux | stage1_ndcg_at_5 | -0.0050 | -0.0362 | 0.0267 | 163 |
| delta:lux-e5-vs-lux-lux | stage2_ndcg_at_5 | 0.0613 | -0.0158 | 0.1316 | 111 |
| lux-lux | stage1_ndcg_at_5 | 0.8463 | 0.8216 | 0.8698 | 163 |
| lux-lux | stage2_ndcg_at_5_scored | 0.2212 | 0.1712 | 0.2786 | 111 |
| lux-lux | stage2_mrr_at_5_scored | 0.4053 | 0.3245 | 0.4958 | 111 |

## Multi-seed summary

Independent N draws per seed; across-seed = mean of seed means + min–max.

| Pair | Metric | Per-seed | Mean | Min | Max |
|---|---|---|---|---|---|
| lux-lux | stage1_ndcg_at_5 | `{'7': 0.8419909717877244, '42': 0.8413316040194614, '123': 0.8525207389460415}` | 0.8453 | 0.8413 | 0.8525 |
| lux-lux | stage2_ndcg_at_5 | `{'7': 0.20763463005510788, '42': 0.22117061292825135, '123': 0.19735149287851278}` | 0.2087 | 0.1974 | 0.2212 |
| anyjev-l0-lux | stage1_ndcg_at_5 | `{'7': 0.8584140447053069, '42': 0.8624832020116757, '123': 0.8667149873181825}` | 0.8625 | 0.8584 | 0.8667 |
| anyjev-l0-lux | stage2_ndcg_at_5 | `{'7': 0.22379343443990715, '42': 0.23000079268681078, '123': 0.19697593703055066}` | 0.2169 | 0.1970 | 0.2300 |
| lux-e5 | stage1_ndcg_at_5 | `{'7': 0.8419909717877244, '42': 0.8413316040194614, '123': 0.8525207389460415}` | 0.8453 | 0.8413 | 0.8525 |
| lux-e5 | stage2_ndcg_at_5 | `{'7': 0.27082406553176913, '42': 0.2824856232460483, '123': 0.2407089740673051}` | 0.2647 | 0.2407 | 0.2825 |
| lux-bm25 | stage1_ndcg_at_5 | `{'7': 0.8419909717877244, '42': 0.8413316040194614, '123': 0.8525207389460415}` | 0.8453 | 0.8413 | 0.8525 |
| lux-bm25 | stage2_ndcg_at_5 | `{'7': 0.27595784043046784, '42': 0.26484947885216487, '123': 0.19730975987049912}` | 0.2460 | 0.1973 | 0.2760 |

## Answer metrics (synthesis reuse)

Answer EM/F1 **not run** (ranking-only or synthesis reuse not attached).

## Routing vs scoring (narrative)

When Stage-2 has no type-filtered candidates (`empty_top1_chunks`), those examples are **omitted** from primary (scored-only) S2 nDCG/MRR and count as **0** in the secondary **pipeline-averaged** series. See Routing accounting for class counts — empty is not always “wrong Top-1 type.”

- `anyjev-l0-e5`: empty-Top-1 rate 36.0% (72 / 200 examples)
- `anyjev-l0-bm25`: empty-Top-1 rate 36.0% (72 / 200 examples)
- `lux-lux-shortlist`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `lux-e5-ce`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `anyjev-l0-lux`: empty-Top-1 rate 36.0% (72 / 200 examples)
- `lux-bm25`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `lux-e5`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `lux-lux`: empty-Top-1 rate 40.5% (81 / 200 examples)

## Latency / resources

| Pair | S1 p50/p95 (ms) | S2 p50/p95 (ms) | GPU high-water MB |
|---|---|---|---|
| anyjev-l0-e5 | 736.8272/746.5860 | 992.3035/2227.9132 | 1036.0420 |
| anyjev-l0-bm25 | 740.2709/750.9328 | 12.1413/44.4399 | 1036.0420 |
| lux-lux-shortlist | 161.1931/168.1033 | 3419.2340/3639.0994 | 1036.0420 |
| lux-e5-ce | 160.8450/165.6147 | 896.6003/2300.6152 | 1122.2271 |
| anyjev-l0-lux | 791.0231/803.1481 | 14293.9683/40648.4081 | 0.0000 |
| lux-bm25 | 166.8709/171.4857 | 10.2259/50.6086 | 0.0000 |
| lux-e5 | 166.4022/171.1671 | 861.5197/2262.9401 | 1035.5732 |
| lux-lux | 169.2432/176.0778 | 14075.4844/39874.8429 | 0.0000 |

### Latency notes

- BM25 is essentially free (p50 10.2259 ms) vs E5 (861.5197 ms) vs Lux Score (14075.4844 ms).

## Guardrails

- Block A holds Stage-2 fixed at `decision20-lux` — Stage-2 nDCG differences across these rows reflect routing quality, not a different scorer.
- Block B holds Stage-1 fixed at `decision20-lux` — compare Stage-2 overall nDCG vs **nDCG@5|Top-1** (scorer quality when routing was correct).
- Answer EM/F1 were **not** collected (ranking-only; Gemini synthesis off).

## Takeaways

- For typed Choice routing, prefer `anyjev-l0-lux` on this sample; cite OFR when claiming AnyJev robustness.
- For Stage-2 passage scoring after Lux Choice, `lux-lux-shortlist` leads on overall nDCG@5; also report conditional-on-Top-1 and latency.
- Always separate **router quality** (Block A / empty-Top-1 rate) from **scorer quality** (Block B S2|Top-1); overall S2 mixes both.
- Re-run with `--with-synthesis` when answer-span EM/F1 are needed for the paper.

## Pair outcomes

| Pair | Status | Completed | Empty Top-1 | Other fail | Inspect |
|---|---|---|---|---|---|
| anyjev-l0-e5 | measured | 128 | 72 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-anyjev-l0-e5) |
| anyjev-l0-bm25 | measured | 128 | 72 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-anyjev-l0-bm25) |
| lux-lux-shortlist | measured | 119 | 81 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-lux-lux-shortlist) |
| lux-e5-ce | measured | 119 | 81 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-lux-e5-ce) |
| anyjev-l0-lux | measured | 128 | 72 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-anyjev-l0-lux) |
| lux-bm25 | measured | 119 | 81 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-lux-bm25) |
| lux-e5 | measured | 119 | 81 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-lux-e5) |
| lux-lux | measured | 119 | 81 | 0 | [open](paper-p1-ceilings-n200.inspect.html#pair-lux-lux) |

## Limitations / threats to validity

- Sample N may be below full FinAgentBench; seed and N are recorded above.
- CLM Stage-2 is zero-shot Action Cache (2k context) unless shortlist optional row ran.
- E5 is general-domain, not finance-tuned; BM25 is lexical only.
- Empty-Top-1 rates depend on the Stage-1 engine — Block A rows are not comparable on Stage-2 overall nDCG without conditioning on Top-1.
- Deferred trained dual-encoder heads: [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) (`lux-clm-ft`).
- Cross-encoder IR ceiling (`lux-e5-ce`) is implemented as an optional P1 pair (pretrained CE; closes [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)).
- Champion cells (`anyjev-l0-e5` / `anyjev-l0-bm25`) are compound pairs, not orthogonal Block A/B.

## Skipped / deferred pairs

- `lux-clm-ft` — deferred_issue ([issue](https://github.com/caldeirav/finagent-mesh-mcp/issues/1))
- `lux-clm-shortlist` — optional_not_requested
- `one-shot-ar` — optional_not_requested
- `anyjev-l1-lux` — optional_not_requested

## Artifact index

- Interactive inspect (per-example): `paper-p1-ceilings-n200.inspect.html`
- Analysis JSON: `paper-p1-ceilings-n200.analysis.json`
- Matrix JSON / CSV: `paper-p1-ceilings-n200.json`, `paper-p1-ceilings-n200.csv`
