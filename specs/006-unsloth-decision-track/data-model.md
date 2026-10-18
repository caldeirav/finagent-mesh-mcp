# Data Model: Unsloth Decision Track (006)

## SplitManifest

| Field | Type | Rules |
|-------|------|-------|
| `manifest_id` | string | Stable id, e.g. `fab-paper-test-v1` |
| `created_at` | ISO-8601 | UTC |
| `test_source` | string | Must be `paper-n200-full` for default |
| `test_ids` | list[string] | Exact equality to paper `selected_example_ids` |
| `train_ids` | list[string] | Disjoint from test |
| `val_ids` | list[string] | Disjoint from test and train |
| `seed` | int | Split RNG for train/val partition of remainder |
| `content_hash` | string | Hash over sorted id lists + test_source |
| `n_train` / `n_val` / `n_test` | int | Derived counts |

**Validation**: `set(test) ∩ set(train) = ∅`, `set(test) ∩ set(val) = ∅`, `set(train) ∩ set(val) = ∅`. Builder fails closed on leakage.

## ScoreTrainingRow

| Field | Type | Rules |
|-------|------|-------|
| `example_id` | string | FinAgentBench id; must be in train or val |
| `query` | string | Question text |
| `candidates` | list[{id, text, doc_type}] | **Gold Stage-1 type only** |
| `score_criteria` | list[string] | Ordered legend for relevance 0/1/2 (fixed vocabulary) |
| `labels` | map id → {0,1,2} or ordinal targets | From FinAgentBench stage2 labels |
| `gold_doc_types` | list[string] | Stage-1 gold set used for filter |

**Validation**: Every candidate `doc_type` ∈ `gold_doc_types`. Empty candidate list → skip with report counter (not silent success).

## UnslothTrainRun

| Field | Type | Rules |
|-------|------|-------|
| `train_run_id` | string | Unique |
| `base_model_id` | string | Default `unsloth/Qwen3.8-27B-unsloth-bnb-4bit` |
| `checkpoint_dir` | path | Under `artifacts/unsloth/checkpoints/` |
| `split_manifest_id` | string | FK to SplitManifest |
| `lora` | object | r, alpha, dropout, max_seq_length, load_in_4bit |
| `seed` | int | |
| `mlflow_run_id` | string \| null | |
| `holdout_metrics` | object | accuracy / ece / loss from calibrate when available |
| `status` | enum | `pending` \| `running` \| `completed` \| `failed` |

## FrozenStage1Record

| Field | Type | Rules |
|-------|------|-------|
| `example_id` | string | Paper test id |
| `top1_doc_type` | string \| null | From frozen Lux Choice |
| `stage1_ordered_ids` | list[string] | Optional |
| `stage1_scores` | list[float] | Optional |
| `empty_top1` | bool | True if no chunks for Top-1 type |
| `source` | string | e.g. `paper-n200-full:lux-lux` |

## UnslothEvalMatrixRun

Same shape as existing `MatrixRun` with:

| Extra | Rules |
|-------|-------|
| `matrix_run_id` | MUST match `unsloth-*` |
| `frozen_stage1_source` | MUST be set for `lux-unsloth-score` |
| `shortlist_k` | Default 32 |
| `train_run_id` | Checkpoint provenance |
| `role` on pair | `trained_decision` |

**Immutability**: Writers MUST NOT open published paper artifact paths for write.

## ComparisonSummaryRow

| Field | Type |
|-------|------|
| `pair_id` | string (`lux-unsloth-score`) |
| `baseline_pair_id` | `lux-lux` \| `lux-lux-shortlist` \| `lux-e5` |
| `metric` | e.g. `stage2_ndcg_at_5` |
| `trained_value` | float |
| `baseline_value` | float (read-only from published JSON) |
| `delta` | float |

## Relationships

```text
SplitManifest ──produces──► ScoreTrainingRow[]
UnslothTrainRun ──uses──► SplitManifest + ScoreTrainingRow[train/val]
UnslothEvalMatrixRun ──uses──► FrozenStage1Record[] + UnslothTrainRun checkpoint
ComparisonSummaryRow ──reads──► UnslothEvalMatrixRun metrics + paper-n200-full / paper-p1 JSON (RO)
```
