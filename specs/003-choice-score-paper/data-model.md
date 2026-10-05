# Data Model: Paper-Ready Choice/Score Matrix

**Feature**: `003-choice-score-paper` | **Date**: 2026-10-05

Extends [002 data-model](../002-decision-model-bench/data-model.md). Only new/changed entities are detailed below.

## EvaluationPair (extended)

| Field | Type | Rules |
|-------|------|-------|
| `pair_id` | string | Stable identity; unique in catalog |
| `stage1` | config_id \| null | Null only for `baseline_collapsed` one-shot |
| `stage2` | config_id | Required except when collapsed into one AR call |
| `blocks` | list[`A`\|`B`] | Membership for report tables; `lux-lux` → `[A,B]` |
| `role` | string | `production` \| `latency` \| `calibrated` \| `baseline` \| `baseline_collapsed` \| `ir_floor` \| `ir_dense` \| `optional` |
| `optional` | bool | Default false; omitted from default `--real` |
| `deferred` | bool | If true, never run; appear in skip/deferred section only |
| `deferred_issue` | string \| null | GitHub issue URL for deferred rows |
| `rationale` | string | Paper table caption |

**Validation**: Required pairs must have non-null stage1+stage2 except `baseline_collapsed`. Deferred pairs must not be selected by default resolvers.

## MatrixRun (extended)

| Field | Type | Notes |
|-------|------|-------|
| `matrix_run_id` | string | Existing |
| `n_examples` | int | Actual N run |
| `sample_seed` | int | Required for publishable claims |
| `dataset_path` | string | FinAgentBench path |
| `synthesis_enabled` | bool | Default **false** for paper `--real` |
| `blocks_present` | list | Which blocks have ≥1 completed pair |
| `pairs` | list[PairResult] | See below |
| `skip_records` | list[SkipRecord] | Optional/deferred not run |

## PairResult (extended metrics)

| Field | Type | Notes |
|-------|------|-------|
| `pair_id` | string | |
| `blocks` | list | Copied from catalog |
| `stage1_engine` / `stage2_engine` | string | Shared-partner check for Block A/B |
| `stage1_ndcg_at_5` / `map` / `mrr` | float \| null | Existing |
| `stage2_ndcg_at_5` / `map` / `mrr` | float \| null | Overall |
| `stage2_ndcg_at_5_given_top1` | float \| null | Conditional on Top-1 type correct |
| `stage2_map_at_5_given_top1` | float \| null | |
| `stage2_mrr_at_5_given_top1` | float \| null | |
| `stage1_top1_recall` | float \| null | |
| `stage1_top5_recall` | float \| null | |
| `empty_top1_chunk_rate` | float \| null | |
| `option_flip_rate` | float \| null | AnyJev L0 only |
| `parse_failure_rate` | float \| null | AR rows |
| `latency_stage1_p50_ms` / `p95_ms` | float \| null | |
| `latency_stage2_p50_ms` / `p95_ms` | float \| null | |
| `gpu_mem_high_water_mb` | float \| null | Best-effort |
| `answer_em` / `answer_f1` | float \| null | Null / “not run” if synthesis off |
| `n_completed` / `n_failed` / `n_empty_top1` | int | |
| `status` | string | completed \| failed \| skipped |

## SkipRecord

| Field | Type | Notes |
|-------|------|-------|
| `pair_id` | string | |
| `reason` | string | `optional_not_requested` \| `deferred_issue` \| `missing_weights` \| `missing_calibration` \| … |
| `issue_url` | string \| null | For deferred |

## RoutingOutcome (per example, in ranking_payload)

| Field | Type | Notes |
|-------|------|-------|
| `top1_doc_type` | string \| null | Predicted |
| `gold_stage1_labels` | list | From expected |
| `top1_correct` | bool | Intersection / grade rule aligned with existing Stage-1 scorer |
| `empty_top1_chunks` | bool | |

## ScoringOutcome (per example)

| Field | Type | Notes |
|-------|------|-------|
| `stage2_ranks` | list | Predicted chunk ids |
| `gold_stage2_labels` | list | |
| `metrics` | object | Per-example nDCG etc. when computable |
| `eligible_for_conditional_s2` | bool | `top1_correct && not empty_top1` |

## InvestigationRecord

Unchanged in spirit from inspect payload: `expected`, `io_traces`, stage dumps, errors. Must exist for ≥90% completed examples and for failed/pre-filter with error or `trace_missing`.

## AnalysisReport

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | |
| `research_questions` | list[string] | Fixed template + run facts |
| `block_a_table` | list[PairResult] | Pairs with `A` in blocks |
| `block_b_table` | list[PairResult] | Pairs with `B` in blocks |
| `routing_vs_scoring` | narrative + metrics | |
| `latency_table` | list | |
| `findings` | list[string] | Rule-checked: Block A S2 partner identity constant |
| `limitations` | list[string] | Includes deferred #1/#2 |
| `artifact_index` | list[{pair_id, example_id, inspect_href}] | |
| `skip_records` | list[SkipRecord] | |

## State transitions

Matrix pair row: `pending` → `running` → `completed` \| `failed` \| `skipped`.  
One-shot pair: harness sets `collapsed_stages=true` on AgentState / ranking_payload; Stage-1 metrics null or N/A.

## Identity rules

- Same `pair_id` always means same stage1/stage2 roles across runs.
- Deduplicate physical runs: if both blocks need `lux-lux`, execute once; attach to both tables.
- Example ids shared across all pairs in a matrix run (single seeded sample).
