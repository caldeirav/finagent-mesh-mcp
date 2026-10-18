# Data Model: Stage-2 Yield Recovery (007)

## Entities

### YieldRecoveryAudit (per example, ranking payload)

| Field | Type | Description |
|-------|------|-------------|
| `original_top1_doc_type` | string \| null | Choice Top-1 before recovery |
| `original_top1_empty` | bool | True if Top-1 type had zero chunks |
| `effective_doc_type` | string \| null | Type used for Stage-2 scoring after recovery (equals original when no fallback) |
| `yield_recovery_enabled` | bool | Run/pair flag |
| `yield_recovery_used` | bool | True if effective type ≠ original Top-1 due to empty Top-1 pool |
| `yield_recovery_attempted_types` | string[] | Types checked in order until success or exhaust |
| `top1_doc_type` | string \| null | **Canonical Choice Top-1** (unchanged for recall compatibility) |

**Validation**:
- If `yield_recovery_used`, then `original_top1_empty` MUST be true and `effective_doc_type` MUST be set and ≠ `original_top1_doc_type` (unless `__all__` edge).
- If recovery enabled and all types empty: `yield_recovery_used` false or true with still-empty Stage-2; `error` / skipped_reason remains empty-pool class; no Stage-2 `ordered_ids`.

### RankingPayload (extensions)

Existing harness ranking JSON gains the audit fields above plus unchanged `stage1`, `stage2`, `expected`, `empty_top1_chunks` (post-recovery emptiness for pipeline), and optional:

| Field | Meaning |
|-------|---------|
| `empty_original_top1` | Alias/persistence of `original_top1_empty` for metrics |
| `empty_top1_chunks` | Post-recovery: no Stage-2 list (legacy name retained for pipeline) |

### PairConfiguration (catalog)

| Field | Type | Description |
|-------|------|-------------|
| `pair_id` | string | e.g. `lux-lux-yield`, `lux-unsloth-score-yield` |
| `yield_recovery` | bool | Opt-in; default false/absent |
| `optional` | bool | true for v1 yield pairs |
| `role` | string | e.g. `yield_recovery` |
| Stage-1 / Stage-2 engine ids | string | Twin of baseline pairs |

### Matrix / analysis aggregates

| Metric | Scope |
|--------|--------|
| `empty_top1_chunk_rate` | Prefer **post-recovery** empty rate for recovery pairs (document in report); also emit `empty_original_top1_rate` |
| `pipeline_yield` | Post-recovery scored fraction |
| `empty_original_top1_rate` | Original Top-1 empty fraction |
| `n_yield_fallback` | Count `yield_recovery_used` |
| `stage2_*_given_top1` | Conditional on **original** Top-1 ∈ gold |
| `stage2_*_given_effective_type` | Conditional on **effective** type ∈ gold (recovery pairs) |

### Artifact stems

| Stem pattern | Writable? |
|--------------|-----------|
| `paper-n200-full*`, `paper-p1-ceilings-n200*` | **No** |
| `unsloth-score-paper-n200*` | **No** (read-only baseline for Δ) |
| `yield-*` or `*-yield*` | **Yes** |

## Relationships

```text
MatrixPair (yield_recovery)
  └─▶ EvalRun
        └─▶ RankingPayload per example
              ├─ Choice Top-1 (original)
              ├─ Effective type (Stage-2 filter)
              └─ Stage-2 scores / empty
```

## State transitions (Stage-2 pool selection)

```text
[recovery off]
  Top-1 pool non-empty → score Top-1
  Top-1 pool empty → empty_top1_chunks (stop)

[recovery on]
  Top-1 pool non-empty → score Top-1 (no fallback)
  Top-1 pool empty → walk ordered_ids
       → first non-empty → score that type (yield_recovery_used)
       → none → empty (fail closed)
```
