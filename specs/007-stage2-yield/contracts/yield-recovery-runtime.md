# Contract: Yield recovery runtime behavior

## Gate

Recovery runs **only** when the active pair/run sets `yield_recovery: true` (or equivalent CLI). Default pairs MUST behave as today.

## Algorithm (Stage-2)

Inputs: `original_top1` = Choice Top-1; `ordered_ids` = Stage-1 ranking; `chunks` = example passages; `recovery_enabled`.

1. If `original_top1` missing → `missing_top1_doc_type` (unchanged).
2. If `original_top1 == "__all__"` → rank all chunks (one-shot); recovery N/A.
3. Let `pool(t) = {c in chunks | c.doc_type == t}`.
4. Set `original_top1_empty = (len(pool(original_top1)) == 0)`.
5. If not `original_top1_empty` OR not `recovery_enabled`:
   - Score `pool(original_top1)` or empty as today; `effective = original_top1`; `yield_recovery_used = false`.
6. Else:
   - `attempted = []`
   - For each `t` in `ordered_ids` (full list):
     - append `t` to `attempted`
     - if `len(pool(t)) > 0`: score that pool; `effective = t`; `yield_recovery_used = (t != original_top1)`; stop
   - If none: empty Stage-2; `effective = original_top1` or null; fail closed; `yield_recovery_used` may be false with attempted list recorded

**MUST NOT** use gold Stage-1 labels in step 6.

## Ranking payload MUST include

- `top1_doc_type` = original Choice Top-1  
- `original_top1_doc_type`, `original_top1_empty`  
- `effective_doc_type`  
- `yield_recovery_enabled`, `yield_recovery_used`, `yield_recovery_attempted_types`  
- `empty_top1_chunks` = post-recovery emptiness (no Stage-2 ordered ids)

## Frozen Choice

Fallback MUST use frozen `stage1_ordered_ids` when Stage-1 is frozen Lux. If ordered ids missing, do not invent an order from gold; skip recovery for that example and count a diagnostic `n_recovery_skipped_missing_order`.
