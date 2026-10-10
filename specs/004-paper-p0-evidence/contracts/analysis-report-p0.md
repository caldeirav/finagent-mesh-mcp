# Contract: P0 Analysis Report Extensions

Extends Spec 003 [analysis-report.md](../../003-choice-score-paper/contracts/analysis-report.md). Rebuild still via `--analysis-from` (no engines) for S0/S3/S4-from-saved-run sections.

## Additional Markdown sections (insert after existing Block B / routing)

Order after **How to read** / **Run facts** / Block A / Block B:

1. **Routing accounting** — per [routing-classes.md](./routing-classes.md); reconciliation note when empty rate and Top-1 recall diverge.
2. **Stage-2 metric series** — Block B table columns MUST include:
   - Primary: `S2 nDCG@5 (scored)`, `S2 MRR@5 (scored)`, conditional-on-eligible columns as today
   - Secondary: `S2 nDCG@5 (pipeline)`, `S2 MRR@5 (pipeline)` with footnote: empties/unscored = 0
3. **Strata (Block B)** — gold type / candidate size / length; Lux vs BM25 vs E5 (+ CLM if present); N per cell.
4. **Win/tie/loss vs Lux Score** — nDCG@5, ε=0.01; sample inspect links (`#pair-…-ex-…` or pair anchors + example ids).
5. **Uncertainty** — seed-42 bootstrap 95% CIs for headline metrics and Δ vs Lux; multi-seed table when rollup present (per-seed, mean-of-means, min–max).
6. **Answer metrics (synthesis reuse)** — when synthesis run attached: EM/F1, attempted/failed/skipped-no-evidence; else “not run”.
7. **Optional baselines** — `lux-clm-shortlist`, `one-shot-ar` when measured; #1/#2 deferred links unchanged.

## Findings guardrails (additions)

- MUST NOT claim empties are averaged as zero into **primary** S2 series.
- MUST mention pipeline-averaged series when discussing end-to-end agent yield.
- MUST cite bootstrap CI and/or multi-seed min–max when claiming E5>Lux or AnyJev>Lux.
- MUST state synthesis rankings were **reused** (no Choice/Score re-inference) when answer metrics present.
- MUST label `one-shot-ar` as collapsed-stage baseline.

## Analysis JSON extensions

```json
{
  "pipeline_yield": [{ "pair_id": "lux-lux", "n_scored": 119, "pipeline_yield": 0.595 }],
  "routing_classes": [{ "pair_id": "lux-lux", "counts": { "correct_top1_empty": 0 }, "rates": {} }],
  "stage2_series": {
    "lux-e5": {
      "scored_mean": { "stage2_ndcg_at_5": 0.28, "stage2_mrr_at_5": 0.50 },
      "pipeline_mean": { "stage2_ndcg_at_5": 0.17, "stage2_mrr_at_5": 0.30 }
    }
  },
  "strata": [],
  "win_loss": [],
  "uncertainty": { "bootstrap": [], "multi_seed": [] },
  "synthesis_reuse": null
}
```

Field names may be nested under `findings_detail` / top-level keys as long as rebuild consumers documented in code remain stable within this feature.
