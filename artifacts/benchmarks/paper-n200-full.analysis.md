# Paper analysis — paper-n200-full

## Executive summary

- **Best Choice router (Block A):** `anyjev-l0-lux` with Stage-1 nDCG@5 = 0.8625 (Top-1 filing-type recall 95.1%).
- **Best passage scorer (Block B, overall S2 nDCG@5):** `lux-e5` = 0.2825 (conditional-on-Top-1 0.3127).
- **Routing ceiling:** ~40.5% of examples under Lux Choice yield empty Stage-2 candidate sets — passage scoring cannot recover those misses.
- **Coverage:** 8/8 matrix pairs have measurable ranking metrics on N=200 (seed=42).

## How to read this report

1. **Block A** varies the Stage-1 **Choice** router; Stage-2 Score stays Lux. Higher S1 nDCG@5 / Top-1 recall = better filing-type routing.
2. **Block B** varies the Stage-2 **Score** (or dense/lexical) head; Stage-1 Choice stays Lux. Compare overall S2 nDCG@5 (full pipeline) and **S2 nDCG@5|Top-1** (scorer only, when Top-1 type was correct).
3. **`empty_top1_chunks`** means the router picked the wrong filing type so no gold passages remain — a routing failure, not a scorer bug.

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

| Pair | S2 engine | S2 nDCG@5 | Δ vs Lux | S2 nDCG@5\|Top-1 | Empty Top-1 | S2 p50 ms |
|---|---|---|---|---|---|---|
| lux-lux | decision20-lux | 0.2212 | +0.0000 | 0.2326 | 0.4050 | 14075.4844 |
| lux-clm | clm-8b | 0.1026 | -0.1186 | 0.1066 | 0.4050 | 30051.6439 |
| lux-bm25 | bm25-stage2 | 0.2648 | +0.0437 | 0.2829 | 0.4050 | 10.2259 |
| lux-e5 | e5-base | 0.2825 | +0.0613 | 0.3127 | 0.4050 | 861.5197 |

### Block B findings

- Ranked by overall Stage-2 nDCG@5 (full pipeline after Lux Choice). Lux Score baseline (`lux-lux`) is 0.2212 (conditional 0.2326).
- 1. **`lux-e5`** (`e5-base`) — S2 nDCG@5 0.2825 (+0.0613 vs Lux), S2|Top-1 0.3127, empty-Top-1 40.5%, S2 p50 861.5197 ms.
- 2. **`lux-bm25`** (`bm25-stage2`) — S2 nDCG@5 0.2648 (+0.0437 vs Lux), S2|Top-1 0.2829, empty-Top-1 40.5%, S2 p50 10.2259 ms.
- 3. **`lux-lux`** (`decision20-lux`) — S2 nDCG@5 0.2212 (+0.0000 vs Lux), S2|Top-1 0.2326, empty-Top-1 40.5%, S2 p50 14075.4844 ms.
- 4. **`lux-clm`** (`clm-8b`) — S2 nDCG@5 0.1026 (-0.1186 vs Lux), S2|Top-1 0.1066, empty-Top-1 40.5%, S2 p50 30051.6439 ms.
- CLM zero-shot Action Cache is weakest on this sample (S2 nDCG@5 0.1026) and slowest (p50 30051.6439 ms) — treat as a stress baseline, not a production scorer, until shortlist/FT variants run.
- E5 (general-domain dense) and/or BM25 beat Lux Score on overall passage nDCG here — surprising for a finance-specialized ordinal Score head; confirm on full FinAgentBench and with finance-tuned dense/CE ceilings.

## Routing vs scoring

When Stage-1 Top-1 filing type is wrong, Stage-2 sees no gold chunks (`empty_top1_chunks`). Those examples contribute 0 to overall S2 nDCG and are excluded from **S2 nDCG@5|Top-1**.

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
