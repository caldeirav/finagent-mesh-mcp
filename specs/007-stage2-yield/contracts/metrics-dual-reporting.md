# Contract: Dual empty / yield / conditional metrics

## Empty & yield

| Name | Definition |
|------|------------|
| `empty_original_top1_rate` | Mean of `original_top1_empty` over N |
| `empty_top1_chunk_rate` (recovery pairs) | Mean of post-recovery empty (no Stage-2 list) |
| `pipeline_yield` | Fraction with non-empty Stage-2 `ordered_ids` after recovery |
| `n_yield_fallback` / `yield_fallback_rate` | Count/rate of `yield_recovery_used` |

On **non-recovery** pairs, `empty_original_top1_rate` MAY equal `empty_top1_chunk_rate` (today’s behavior).

## Conditional Stage-2

| Name | Condition set |
|------|----------------|
| `stage2_ndcg_at_5_given_top1` (and map/mrr) | Examples where **original** Choice Top-1 ∈ gold Stage-1 labels **and** Stage-2 scored |
| `stage2_ndcg_at_5_given_effective_type` (and map/mrr) | Examples where **effective** type ∈ gold **and** Stage-2 scored; required on recovery pairs when any fallback occurred |

Reports MUST label the second series explicitly (e.g. “S2 nDCG \| effective type”).

## Routing classes

Existing classes remain based on **original** Top-1 correctness. Additionally report:

- `n_fallback_scored` — `yield_recovery_used` and scored  
- `n_fallback_still_empty` — recovery attempted, still empty after full exhaust  

Do not remove `correct_top1_empty` accounting for “original type had no chunks.”
