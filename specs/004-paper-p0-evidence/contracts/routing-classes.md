# Contract: Routing Outcome Classes

Per pair, every example is assigned exactly one class (see [data-model.md](../data-model.md)).

## Class ids (stable)

| class_id | Meaning |
|----------|---------|
| `correct_top1_scored` | Top-1 type correct; Stage-2 ranking list non-empty |
| `correct_top1_empty` | Top-1 type correct; empty type-filtered chunk list |
| `wrong_top1_scored` | Top-1 type incorrect; Stage-2 ranking list non-empty |
| `wrong_top1_empty` | Top-1 type incorrect; empty type-filtered chunk list |
| `missing_top1` | No Top-1 type |
| `other` | Residual anomalies |

## Derived rates

- `empty_top1_chunk_rate` = (`correct_top1_empty` + `wrong_top1_empty` + relevant empties in `other`) / N — MUST remain consistent with existing field within ± rounding, or document delta after audit.
- `pipeline_yield` = (`correct_top1_scored` + `wrong_top1_scored`) / N.

## Analysis report rendering

Markdown **Routing accounting** table columns:

`Pair | N | Top-1 recall | Empty rate | Yield | correct_scored | correct_empty | wrong_scored | wrong_empty | missing/other`

Findings MUST cite these columns when discussing the Top-1 recall vs empty-rate tension.
