# Paper analysis — paper-n200-full

## Executive summary

- **Best Choice router (Block A):** `anyjev-l0-lux` with Stage-1 nDCG@5 = 0.8625 (Top-1 filing-type recall 95.1%).
- **Best passage scorer (Block B, overall S2 nDCG@5):** `lux-e5` = 0.2825 (conditional-on-Top-1 0.3127).
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
| lux-lux | decision20-lux | 0.8413 | +0.0000 | 0.9387 | — | 0.0000 | 169.2432 |
| anyjev-l0-lux | anyjev-l0 | 0.8625 | +0.0212 | 0.9509 | 0.0900 | 0.0000 | 791.0231 |
| kai-lux | decision20-kai | 0.7830 | -0.0584 | 0.8405 | — | 0.0000 | 42.7675 |
| laya-lux | laya-modernbert | 0.7509 | -0.0905 | 0.8098 | — | 0.0000 | 0.0148 |
| ar-lux | ar-qwen3-8b-instruct | 0.7772 | -0.0641 | 0.7730 | — | 0.0000 | 4552.1743 |

### Block A findings

- Ranked by Stage-1 nDCG@5 (filing-type ranking quality). Lux Choice baseline (`lux-lux`) is 0.8413.
- 1. **`anyjev-l0-lux`** (`anyjev-l0`) — nDCG@5 0.8625 (+0.0212 vs Lux), Top-1 recall 95.1%, S1 p50 791.0231 ms, option-flip rate 9.0%.
- 2. **`lux-lux`** (`decision20-lux`) — nDCG@5 0.8413 (+0.0000 vs Lux), Top-1 recall 93.9%, S1 p50 169.2432 ms.
- 3. **`kai-lux`** (`decision20-kai`) — nDCG@5 0.7830 (-0.0584 vs Lux), Top-1 recall 84.0%, S1 p50 42.7675 ms.
- 4. **`ar-lux`** (`ar-qwen3-8b-instruct`) — nDCG@5 0.7772 (-0.0641 vs Lux), Top-1 recall 77.3%, S1 p50 4552.1743 ms.
- 5. **`laya-lux`** (`laya-modernbert`) — nDCG@5 0.7509 (-0.0905 vs Lux), Top-1 recall 81.0%, S1 p50 0.0148 ms.
- AnyJev L0 reports order sensitivity: OFR = 9.0% (fraction of examples whose top Choice flips when options are permuted).
- Kai is much faster than Lux Choice (42.7675 vs 169.2432 ms p50) but trails on nDCG@5 (0.7830 vs 0.8413).

## Block B — Stage-2 Score (Lux Choice fixed)

| Pair | S2 engine | S2 nDCG (scored) | S2 MRR (scored) | Δ nDCG vs Lux | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | Empty Top-1 | S2 p50 ms |
|---|---|---|---|---|---|---|---|---|
| lux-lux | decision20-lux | 0.2212 | 0.4053 | +0.0000 | 0.2326 | 0.1227 | 0.4050 | 14075.4844 |
| lux-clm | clm-8b | 0.1026 | 0.1818 | -0.1186 | 0.1066 | 0.0569 | 0.4050 | 30051.6439 |
| lux-bm25 | bm25-stage2 | 0.2648 | 0.4375 | +0.0437 | 0.2829 | 0.1470 | 0.4050 | 10.2259 |
| lux-e5 | e5-base | 0.2825 | 0.4959 | +0.0613 | 0.3127 | 0.1568 | 0.4050 | 861.5197 |

### Block B findings

- Ranked by overall Stage-2 nDCG@5 (full pipeline after Lux Choice). Lux Score baseline (`lux-lux`) is 0.2212 (conditional 0.2326).
- 1. **`lux-e5`** (`e5-base`) — S2 nDCG@5 0.2825 (+0.0613 vs Lux), S2|Top-1 0.3127, empty-Top-1 40.5%, S2 p50 861.5197 ms.
- 2. **`lux-bm25`** (`bm25-stage2`) — S2 nDCG@5 0.2648 (+0.0437 vs Lux), S2|Top-1 0.2829, empty-Top-1 40.5%, S2 p50 10.2259 ms.
- 3. **`lux-lux`** (`decision20-lux`) — S2 nDCG@5 0.2212 (+0.0000 vs Lux), S2|Top-1 0.2326, empty-Top-1 40.5%, S2 p50 14075.4844 ms.
- 4. **`lux-clm`** (`clm-8b`) — S2 nDCG@5 0.1026 (-0.1186 vs Lux), S2|Top-1 0.1066, empty-Top-1 40.5%, S2 p50 30051.6439 ms.
- CLM zero-shot Action Cache is weakest on this sample (S2 nDCG@5 0.1026) and slowest (p50 30051.6439 ms) — treat as a stress baseline, not a production scorer, until shortlist/FT variants run.
- E5 (general-domain dense) and/or BM25 beat Lux Score on overall passage nDCG here — surprising for a finance-specialized ordinal Score head; confirm on full FinAgentBench and with finance-tuned dense/CE ceilings.

## Routing accounting

Mutually exclusive classes reconcile Top-1 recall vs empty-Top-1. **Pipeline yield** = fraction of examples with a Stage-2 ranking list. Primary Stage-2 nDCG/MRR are **scored-only** means; **pipeline-averaged** treats empty/unscored as 0.

| Pair | N | Top-1 recall | Empty rate | Yield | correct_scored | correct_empty | wrong_scored | wrong_empty | missing/other |
|---|---|---|---|---|---|---|---|---|---|
| lux-lux | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| anyjev-l0-lux | 200 | 0.9509 | 0.3600 | 0.6400 | 95 | 60 | 33 | 12 | 0 |
| kai-lux | 200 | 0.8405 | 0.5300 | 0.4700 | 61 | 76 | 33 | 30 | 0 |
| laya-lux | 200 | 0.8098 | 0.5750 | 0.4250 | 52 | 80 | 33 | 35 | 0 |
| ar-lux | 200 | 0.7730 | 0.5700 | 0.4300 | 53 | 73 | 33 | 41 | 0 |
| lux-clm | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| lux-bm25 | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |
| lux-e5 | 200 | 0.9387 | 0.4050 | 0.5950 | 86 | 67 | 33 | 14 | 0 |

## Stage-2 metric series (scored vs pipeline)

| Pair | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | S2 MRR (pipeline) |
|---|---|---|---|---|---|
| lux-lux | 0.2212 | 0.4053 | 0.2326 | 0.1227 | 0.2249 |
| anyjev-l0-lux | 0.2300 | 0.4274 | 0.2427 | 0.1380 | 0.2564 |
| kai-lux | 0.1975 | 0.3973 | 0.2039 | 0.0849 | 0.1708 |
| laya-lux | 0.2145 | 0.4089 | 0.2302 | 0.0826 | 0.1574 |
| ar-lux | 0.2142 | 0.4177 | 0.2294 | 0.0835 | 0.1629 |
| lux-clm | 0.1026 | 0.1818 | 0.1066 | 0.0569 | 0.1009 |
| lux-bm25 | 0.2648 | 0.4375 | 0.2829 | 0.1470 | 0.2428 |
| lux-e5 | 0.2825 | 0.4959 | 0.3127 | 0.1568 | 0.2752 |

_Footnote: **scored** = mean over examples with a Stage-2 ranking list; **pipeline** = mean over all N with empty/unscored as 0._

## Strata (Block B)

### By gold_type

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| 10-K | lux-lux | 72 | 0.2446 |
| 10-K | lux-bm25 | 72 | 0.2802 |
| 10-K | lux-e5 | 72 | 0.3258 |
| 10-K | lux-clm | 72 | 0.0942 |
| 10-Q | lux-lux | 10 | 0.2016 |
| 10-Q | lux-bm25 | 10 | 0.2866 |
| 10-Q | lux-e5 | 10 | 0.2156 |
| 10-Q | lux-clm | 10 | 0.2387 |
| DEF14A | lux-lux | 2 | 0.1871 |
| DEF14A | lux-bm25 | 2 | 0.3614 |
| DEF14A | lux-e5 | 2 | 0.3331 |
| DEF14A | lux-clm | 2 | 0.0000 |
| Earnings | lux-lux | 2 | 0.0000 |
| Earnings | lux-bm25 | 2 | 0.2853 |
| Earnings | lux-e5 | 2 | 0.3066 |
| Earnings | lux-clm | 2 | 0.0000 |
| unknown | lux-lux | 33 | 0.1378 |
| unknown | lux-bm25 | 33 | 0.1536 |
| unknown | lux-e5 | 33 | 0.1353 |
| unknown | lux-clm | 33 | 0.0673 |

### By cand_size

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| 1-8 | lux-lux | 1 | 1.0000 |
| 1-8 | lux-bm25 | 1 | 0.4307 |
| 1-8 | lux-e5 | 1 | 0.4307 |
| 1-8 | lux-clm | 1 | 0.5000 |
| 129+ | lux-lux | 60 | 0.1925 |
| 129+ | lux-bm25 | 60 | 0.1983 |
| 129+ | lux-e5 | 60 | 0.2450 |
| 129+ | lux-clm | 60 | 0.0631 |
| 33-128 | lux-lux | 51 | 0.2023 |
| 33-128 | lux-bm25 | 51 | 0.2811 |
| 33-128 | lux-e5 | 51 | 0.2788 |
| 33-128 | lux-clm | 51 | 0.1300 |
| 9-32 | lux-lux | 7 | 0.2401 |
| 9-32 | lux-bm25 | 7 | 0.3908 |
| 9-32 | lux-e5 | 7 | 0.2862 |
| 9-32 | lux-clm | 7 | 0.0674 |

### By length

| Bucket | Pair | N | S2 nDCG@5 |
|---|---|---|---|
| Q1(≤3325) | lux-lux | 83 | 0.1810 |
| Q1(≤3325) | lux-bm25 | 2 | 0.2153 |
| Q1(≤3325) | lux-e5 | 5 | 0.2088 |
| Q1(≤3325) | lux-clm | 29 | 0.1121 |
| Q2(≤5517) | lux-lux | 11 | 0.1913 |
| Q2(≤5517) | lux-bm25 | 28 | 0.1565 |
| Q2(≤5517) | lux-e5 | 21 | 0.1985 |
| Q2(≤5517) | lux-clm | 59 | 0.0881 |
| Q3(≤6000) | lux-lux | 25 | 0.2969 |
| Q3(≤6000) | lux-bm25 | 89 | 0.2762 |
| Q3(≤6000) | lux-e5 | 93 | 0.2811 |
| Q3(≤6000) | lux-clm | 31 | 0.0947 |


## Win/tie/loss vs Lux Score

Decided by per-example Stage-2 **nDCG@5**; `|Δ| < 0.01` counts as tie.

| Challenger | N compared | Wins | Ties | Losses |
|---|---|---|---|---|
| lux-e5 | 111 | 51 | 26 | 34 |
| lux-bm25 | 111 | 51 | 23 | 37 |
| lux-clm | 111 | 19 | 44 | 48 |

### Samples — `lux-e5`

**Wins:**
- `dev:q25119b32a2f9` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q25119b32a2f9))
- `dev:q84038a74fd59` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q84038a74fd59))
- `dev:qa602975e3d19` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:qa602975e3d19))
- `dev:q7c284aabbba4` Δ=0.9521 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q7c284aabbba4))
- `dev:q4d8ac905167b` Δ=0.9026 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q4d8ac905167b))

**Losses:**
- `dev:qe1811f4fd3dc` Δ=-1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:qe1811f4fd3dc))
- `dev:q8ba6a388d681` Δ=-0.8319 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q8ba6a388d681))
- `dev:q31f6fd1f392c` Δ=-0.7817 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:q31f6fd1f392c))
- `dev:qa5c748248a5b` Δ=-0.6716 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:qa5c748248a5b))
- `dev:qdec70f55027f` Δ=-0.5934 ([inspect](paper-n200-full.inspect.html#pair-lux-e5-ex-dev:qdec70f55027f))

### Samples — `lux-bm25`

**Wins:**
- `dev:q25119b32a2f9` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:q25119b32a2f9))
- `dev:q84038a74fd59` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:q84038a74fd59))
- `dev:q9dd3907388e3` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:q9dd3907388e3))
- `dev:q4d8ac905167b` Δ=0.8304 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:q4d8ac905167b))
- `dev:q9a5cfe35fecd` Δ=0.7557 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:q9a5cfe35fecd))

**Losses:**
- `dev:qe1811f4fd3dc` Δ=-1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:qe1811f4fd3dc))
- `dev:qf8cbcec9fec6` Δ=-1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:qf8cbcec9fec6))
- `dev:qdec70f55027f` Δ=-0.7727 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:qdec70f55027f))
- `dev:qa5c748248a5b` Δ=-0.7429 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:qa5c748248a5b))
- `dev:chunk-only:qb7d1dfae8271` Δ=-0.6992 ([inspect](paper-n200-full.inspect.html#pair-lux-bm25-ex-dev:chunk-only:qb7d1dfae8271))

### Samples — `lux-clm`

**Wins:**
- `dev:q3ef7ce37ae77` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:q3ef7ce37ae77))
- `dev:q84038a74fd59` Δ=1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:q84038a74fd59))
- `dev:q7c284aabbba4` Δ=0.6062 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:q7c284aabbba4))
- `dev:chunk-only:q7b219decf5da` Δ=0.3392 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:chunk-only:q7b219decf5da))
- `dev:q4bf1699a63fe` Δ=0.3156 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:q4bf1699a63fe))

**Losses:**
- `dev:qe1811f4fd3dc` Δ=-1.0000 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:qe1811f4fd3dc))
- `dev:qa5c748248a5b` Δ=-0.8688 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:qa5c748248a5b))
- `dev:q8ba6a388d681` Δ=-0.8319 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:q8ba6a388d681))
- `dev:chunk-only:qb7d1dfae8271` Δ=-0.6992 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:chunk-only:qb7d1dfae8271))
- `dev:qeccd6f3b9d06` Δ=-0.6730 ([inspect](paper-n200-full.inspect.html#pair-lux-clm-ex-dev:qeccd6f3b9d06))


## Uncertainty (bootstrap 95% CI)

| Id | Metric | Point | CI low | CI high | N |
|---|---|---|---|---|---|
| lux-lux | stage1_ndcg_at_5 | 0.8413 | 0.8191 | 0.8631 | 163 |
| lux-lux | stage2_ndcg_at_5_scored | 0.2212 | 0.1712 | 0.2786 | 111 |
| lux-lux | stage2_mrr_at_5_scored | 0.4053 | 0.3245 | 0.4958 | 111 |
| anyjev-l0-lux | stage1_ndcg_at_5 | 0.8625 | 0.8403 | 0.8849 | 163 |
| anyjev-l0-lux | stage2_ndcg_at_5_scored | 0.2300 | 0.1828 | 0.2823 | 120 |
| anyjev-l0-lux | stage2_mrr_at_5_scored | 0.4274 | 0.3489 | 0.5086 | 120 |
| delta:anyjev-l0-lux-vs-lux-lux | stage1_ndcg_at_5 | 0.0212 | -0.0089 | 0.0527 | 163 |
| delta:anyjev-l0-lux-vs-lux-lux | stage2_ndcg_at_5 | 0.0088 | -0.0624 | 0.0844 | 111 |
| delta:kai-lux-vs-lux-lux | stage1_ndcg_at_5 | -0.0584 | -0.0889 | -0.0264 | 163 |
| delta:kai-lux-vs-lux-lux | stage2_ndcg_at_5 | -0.0237 | -0.0984 | 0.0521 | 86 |
| delta:laya-lux-vs-lux-lux | stage1_ndcg_at_5 | -0.0905 | -0.1221 | -0.0575 | 163 |
| delta:laya-lux-vs-lux-lux | stage2_ndcg_at_5 | -0.0067 | -0.0903 | 0.0742 | 77 |
| delta:ar-lux-vs-lux-lux | stage1_ndcg_at_5 | -0.0641 | -0.0960 | -0.0300 | 163 |
| delta:ar-lux-vs-lux-lux | stage2_ndcg_at_5 | -0.0070 | -0.0856 | 0.0728 | 78 |
| delta:lux-clm-vs-lux-lux | stage1_ndcg_at_5 | 0.0000 | -0.0315 | 0.0312 | 163 |
| delta:lux-clm-vs-lux-lux | stage2_ndcg_at_5 | -0.1186 | -0.1864 | -0.0594 | 111 |
| lux-bm25 | stage1_ndcg_at_5 | 0.8413 | 0.8191 | 0.8631 | 163 |
| lux-bm25 | stage2_ndcg_at_5_scored | 0.2648 | 0.2190 | 0.3139 | 111 |
| lux-bm25 | stage2_mrr_at_5_scored | 0.4375 | 0.3667 | 0.5171 | 111 |
| delta:lux-bm25-vs-lux-lux | stage1_ndcg_at_5 | 0.0000 | -0.0315 | 0.0312 | 163 |
| delta:lux-bm25-vs-lux-lux | stage2_ndcg_at_5 | 0.0437 | -0.0336 | 0.1136 | 111 |
| lux-e5 | stage1_ndcg_at_5 | 0.8413 | 0.8191 | 0.8631 | 163 |
| lux-e5 | stage2_ndcg_at_5_scored | 0.2825 | 0.2312 | 0.3338 | 111 |
| lux-e5 | stage2_mrr_at_5_scored | 0.4959 | 0.4240 | 0.5742 | 111 |
| delta:lux-e5-vs-lux-lux | stage1_ndcg_at_5 | 0.0000 | -0.0315 | 0.0312 | 163 |
| delta:lux-e5-vs-lux-lux | stage2_ndcg_at_5 | 0.0613 | -0.0158 | 0.1316 | 111 |

## Multi-seed summary

_Pending: run core-subset seeds `{42,7,123}` (`lux-lux`, `anyjev-l0-lux`, `lux-e5`, `lux-bm25`) and rebuild analysis._


## Answer metrics (synthesis reuse)

Answer EM/F1 **not run** (ranking-only or synthesis reuse not attached).

## Routing vs scoring (narrative)

When Stage-2 has no type-filtered candidates (`empty_top1_chunks`), those examples are **omitted** from primary (scored-only) S2 nDCG/MRR and count as **0** in the secondary **pipeline-averaged** series. See Routing accounting for class counts — empty is not always “wrong Top-1 type.”

- `lux-lux`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `anyjev-l0-lux`: empty-Top-1 rate 36.0% (72 / 200 examples)
- `kai-lux`: empty-Top-1 rate 53.0% (106 / 200 examples)
- `laya-lux`: empty-Top-1 rate 57.5% (115 / 200 examples)
- `ar-lux`: empty-Top-1 rate 57.0% (114 / 200 examples)
- `lux-clm`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `lux-bm25`: empty-Top-1 rate 40.5% (81 / 200 examples)
- `lux-e5`: empty-Top-1 rate 40.5% (81 / 200 examples)

## Latency / resources

| Pair | S1 p50/p95 (ms) | S2 p50/p95 (ms) | GPU high-water MB |
|---|---|---|---|
| lux-lux | 169.2432/176.0778 | 14075.4844/39874.8429 | 0.0000 |
| anyjev-l0-lux | 791.0231/803.1481 | 14293.9683/40648.4081 | 0.0000 |
| kai-lux | 42.7675/48.3982 | 15573.9454/39826.3222 | 0.0000 |
| laya-lux | 0.0148/0.0231 | 12836.9209/35003.4663 | 0.0000 |
| ar-lux | 4552.1743/4667.0662 | 13169.0006/38469.1875 | 0.0000 |
| lux-clm | 168.5464/175.3781 | 30051.6439/75747.0745 | 0.0000 |
| lux-bm25 | 166.8709/171.4857 | 10.2259/50.6086 | 0.0000 |
| lux-e5 | 166.4022/171.1671 | 861.5197/2262.9401 | 1035.5732 |

### Latency notes

- BM25 is essentially free (p50 10.2259 ms) vs E5 (861.5197 ms) vs Lux Score (14075.4844 ms).

## Guardrails

- Block A holds Stage-2 fixed at `decision20-lux` — Stage-2 nDCG differences across these rows reflect routing quality, not a different scorer.
- Block B holds Stage-1 fixed at `decision20-lux` — compare Stage-2 overall nDCG vs **nDCG@5|Top-1** (scorer quality when routing was correct).
- Answer EM/F1 were **not** collected (ranking-only; Gemini synthesis off).

## Takeaways

- For typed Choice routing, prefer `anyjev-l0-lux` on this sample; cite OFR when claiming AnyJev robustness.
- For Stage-2 passage scoring after Lux Choice, `lux-e5` leads on overall nDCG@5; also report conditional-on-Top-1 and latency.
- Always separate **router quality** (Block A / empty-Top-1 rate) from **scorer quality** (Block B S2|Top-1); overall S2 mixes both.
- Re-run with `--with-synthesis` when answer-span EM/F1 are needed for the paper.

## Pair outcomes

| Pair | Status | Completed | Empty Top-1 | Other fail | Inspect |
|---|---|---|---|---|---|
| lux-lux | measured | 119 | 81 | 0 | [open](paper-n200-full.inspect.html#pair-lux-lux) |
| anyjev-l0-lux | measured | 128 | 72 | 0 | [open](paper-n200-full.inspect.html#pair-anyjev-l0-lux) |
| kai-lux | measured | 94 | 106 | 0 | [open](paper-n200-full.inspect.html#pair-kai-lux) |
| laya-lux | measured | 85 | 115 | 0 | [open](paper-n200-full.inspect.html#pair-laya-lux) |
| ar-lux | measured | 86 | 114 | 0 | [open](paper-n200-full.inspect.html#pair-ar-lux) |
| lux-clm | measured | 119 | 81 | 0 | [open](paper-n200-full.inspect.html#pair-lux-clm) |
| lux-bm25 | measured | 119 | 81 | 0 | [open](paper-n200-full.inspect.html#pair-lux-bm25) |
| lux-e5 | measured | 119 | 81 | 0 | [open](paper-n200-full.inspect.html#pair-lux-e5) |

## Limitations / threats to validity

- Sample N may be below full FinAgentBench; seed and N are recorded above.
- CLM Stage-2 is zero-shot Action Cache (2k context) unless shortlist optional row ran.
- E5 is general-domain, not finance-tuned; BM25 is lexical only.
- Empty-Top-1 rates depend on the Stage-1 engine — Block A rows are not comparable on Stage-2 overall nDCG without conditioning on Top-1.
- Deferred trained heads: [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1).
- Deferred cross-encoder ceiling: [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2).

## Skipped / deferred pairs

- `lux-clm-ft` — deferred_issue ([issue](https://github.com/caldeirav/finagent-mesh-mcp/issues/1))
- `lux-e5-ce` — deferred_issue ([issue](https://github.com/caldeirav/finagent-mesh-mcp/issues/2))
- `lux-clm-shortlist` — optional_not_requested
- `one-shot-ar` — optional_not_requested
- `anyjev-l1-lux` — optional_not_requested

## Artifact index

- Interactive inspect (per-example): `paper-n200-full.inspect.html`
- Analysis JSON: `paper-n200-full.analysis.json`
- Matrix JSON / CSV: `paper-n200-full.json`, `paper-n200-full.csv`
