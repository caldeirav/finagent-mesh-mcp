# Paper analysis — yield-paper-n200-lux

## Executive summary

- **Coverage:** 1/1 matrix pairs have measurable ranking metrics on N=200 (seed=42).

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

## Block B — Stage-2 Score (Lux Choice fixed)

| Pair | S2 engine | S2 nDCG (scored) | S2 MRR (scored) | Δ nDCG vs Lux | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | Empty Top-1 | S2 p50 ms |
|---|---|---|---|---|---|---|---|---|

## Yield recovery

Opt-in Stage-2 type fallback (007 / #10): when the **original** Choice Top-1 filing type has no chunks, walk Choice-ranked types until a non-empty pool (first-non-empty; never peeks at gold). Empty pools are a **routing / corpus yield** issue — not a Stage-2 Score failure.

- **Run id**: `yield-paper-n200-lux`
- **N**: 200 · **Seed**: 42
- **Recovery pairs**: `lux-lux-yield`
- **Published Lux Choice empty (reference)**: 40.5% on `paper-n200-full`

### Dual empty / yield

| Pair | Empty (original Top-1) | Empty (post-recovery) | Pipeline yield | n fallback | Fallback rate | Still empty |
|---|---|---|---|---|---|---|
| lux-lux-yield | 40.5% | 2.0% | 94.0% | 77 | 38.5% | 0 |

### Pipeline vs scored + dual conditional

| Pair | S2 nDCG (scored) | S2 nDCG (pipeline) | S2 nDCG\|Top-1 | S2 nDCG\|effective type |
|---|---|---|---|---|
| lux-lux-yield | 0.2272 | 0.2136 | 0.2399 | 0.2341 |

### Δ vs read-only baselines

| Pair | Baseline | Δ empty | Δ pipeline S2 nDCG | Baseline empty | Baseline yield |
|---|---|---|---|---|---|
| lux-lux-yield | `lux-lux` | -0.3850 | — | 40.5% | — |

**Limitations:** first-non-empty may select a non-gold filing type; corpus-limited empties (all Choice types empty) remain after full exhaust. Do not treat effective-type conditional as published Top-1 conditional.


## Routing accounting

Mutually exclusive classes reconcile Top-1 recall vs empty-Top-1. **Pipeline yield** = fraction of examples with a Stage-2 ranking list. Primary Stage-2 nDCG/MRR are **scored-only** means; **pipeline-averaged** treats empty/unscored as 0.

| Pair | N | Top-1 recall | Empty rate | Yield | correct_scored | correct_empty | wrong_scored | wrong_empty | missing/other |
|---|---|---|---|---|---|---|---|---|---|
| lux-lux-yield | 200 | 0.9387 | 0.0200 | 0.9800 | 153 | 0 | 43 | 4 | 0 |

## Stage-2 metric series (scored vs pipeline)

| Pair | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\|Top-1 | S2 nDCG (pipeline) | S2 MRR (pipeline) |
|---|---|---|---|---|---|
| lux-lux-yield | 0.2272 | 0.4057 | 0.2399 | 0.2136 | 0.3813 |

_Footnote: **scored** = mean over examples with a Stage-2 ranking list; **pipeline** = mean over all N with empty/unscored as 0._

## Uncertainty (bootstrap 95% CI)

| Id | Metric | Point | CI low | CI high | N |
|---|---|---|---|---|---|

## Multi-seed summary

_Pending: run core-subset seeds `{42,7,123}` (`lux-lux`, `anyjev-l0-lux`, `lux-e5`, `lux-bm25`) and rebuild analysis._


## Answer metrics (synthesis reuse)

Answer EM/F1 **not run** (ranking-only or synthesis reuse not attached).

## Routing vs scoring (narrative)

When Stage-2 has no type-filtered candidates (`empty_top1_chunks`), those examples are a **routing / yield** miss (empty filing-type pool) — **not** a Stage-2 Score crash. They are **omitted** from primary (scored-only) S2 nDCG/MRR and count as **0** in the secondary **pipeline-averaged** series. See Routing accounting — empty is not always “wrong Top-1 type.”

- `lux-lux-yield`: empty-Top-1 rate 2.0% (4 / 200 examples)

## Latency / resources

| Pair | S1 p50/p95 (ms) | S2 p50/p95 (ms) | GPU high-water MB |
|---|---|---|---|
| lux-lux-yield | 160.2974/166.0872 | 14005.3210/39353.5916 | 0.0000 |

## Guardrails

- Answer EM/F1 were **not** collected (ranking-only; Gemini synthesis off).

## Takeaways

- Always separate **router quality** (Block A / empty-Top-1 rate) from **scorer quality** (Block B S2|Top-1); overall S2 mixes both.
- Re-run with `--with-synthesis` when answer-span EM/F1 are needed for the paper.

## Pair outcomes

| Pair | Status | Completed | Empty Top-1 | Other fail | Inspect |
|---|---|---|---|---|---|
| lux-lux-yield | measured | 196 | 4 | 0 | [open](yield-paper-n200-lux.inspect/lux-lux-yield.md) |

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
- `unsloth-choice-lux` — deferred_issue ([issue](https://github.com/caldeirav/finagent-mesh-mcp/issues/5))
- `anyjev-l0-unsloth-score` — deferred_issue ([issue](https://github.com/caldeirav/finagent-mesh-mcp/issues/5))
- `lux-clm-shortlist` — optional_not_requested
- `lux-lux-shortlist` — optional_not_requested
- `lux-e5-ce` — optional_not_requested
- `anyjev-l0-e5` — optional_not_requested
- `anyjev-l0-bm25` — optional_not_requested
- `one-shot-ar` — optional_not_requested
- `lux-unsloth-score` — optional_not_requested
- `lux-unsloth-score-yield` — optional_not_requested
- `anyjev-l1-lux` — optional_not_requested

## Artifact index

- Compact inspect (GitHub): `yield-paper-n200-lux.inspect.md`
- Full inspect HTML (download / open locally): `yield-paper-n200-lux.inspect.html`
- Analysis JSON: `yield-paper-n200-lux.analysis.json`
- Matrix JSON / CSV: `yield-paper-n200-lux.json`, `yield-paper-n200-lux.csv`
