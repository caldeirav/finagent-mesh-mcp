# Contract: Analysis report (Unsloth trained track)

Extends `*.analysis.md` / `*.analysis.json` for runs with `unsloth-*` matrix ids or `role=trained_decision`.

## Section: Trained decision track (Unsloth)

MUST include:

1. Base model id, train_run_id, split manifest hash, shortlist_k
2. Statement that Stage-1 Lux Choice was **frozen** from `paper-n200-full` (not re-inferred)
3. Statement that Score was trained on **gold-type** pools (eval uses Top-1 type pools)
4. Table for `lux-unsloth-score`: S1 (copied/frozen), S2 scored nDCG/MRR, S2|Top-1, pipeline, empty, yield, S2 p50
5. Comparison table (read-only baselines):

| Baseline | S2 nDCG (scored) | Δ vs trained |
|----------|------------------|--------------|
| lux-lux | … | … |
| lux-lux-shortlist | … | … |
| lux-e5 | … | … |

6. Limitations: parallel stack; not a Decision-2.0 drop-in; #1 CLM-ft still deferred

## JSON keys

```json
{
  "trained_decision_pairs": ["lux-unsloth-score"],
  "frozen_stage1_source": "paper-n200-full",
  "comparison_vs_published": [ { "baseline_pair_id": "lux-lux", "metric": "stage2_ndcg_at_5", "delta": 0.0 } ]
}
```

## Immutability

Analysis generation for unsloth runs MUST NOT rewrite published paper analysis files.
