# Data Model: FinAgentBench Hybrid Evaluation Harness

**Feature**: `001-finagentbench-harness` | **Date**: 2026-10-04

## Entities

### EvaluationRun

Named harness execution over a dataset slice or full set.

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string (PK) | Operator-supplied or generated UUID |
| `created_at` | datetime | UTC |
| `config_json` | object | model ids, K, max attempts, ports, dataset path, sample limit |
| `status` | enum | `running`, `stopped`, `completed`, `failed` |
| `lease_owner` | string \| null | PID/host lease for single-writer |
| `lease_expires_at` | datetime \| null | Stale-lease recovery |

**Relationships**: Has many `LedgerEntry`, `StageRankingResult`, `AnswerScore`, `TraceRecord`.

### BenchmarkExample

One FinAgentBench item as consumed by the harness.

| Field | Type | Notes |
|-------|------|-------|
| `example_id` | string (PK within dataset) | Stable FinAgentBench id |
| `firm_id` | string | S&P-500 firm / ticker reference |
| `query_text` | string | User/analyst question |
| `query_category` | string | One of 10 FinAgentBench categories |
| `stage1_labels` | list[string] | Relevance labels/ranks over document types |
| `stage2_labels` | list[object] | Chunk ids + relevance for Top-1 type passages |
| `answer_label` | string \| null | Ground-truth final answer when present |

**Validation**: Document types in labels ⊆ {`10-K`,`10-Q`,`8-K`,`Earnings`,`DEF14A`}. Missing stage labels → skip metrics for that stage with reason.

### DocumentTypeCandidate

| Field | Type | Notes |
|-------|------|-------|
| `doc_type` | enum | `10-K`, `10-Q`, `8-K`, `Earnings`, `DEF14A` |
| `score` | float | System-1 Choice score/logit/prob |
| `rank` | int | 1-based after stable sort |

### PassageChunk

| Field | Type | Notes |
|-------|------|-------|
| `chunk_id` | string | Stable within filing |
| `doc_type` | enum | MUST equal Top-1 Stage-1 type for Stage 2 |
| `text` | string | Paragraph or preserved table unit |
| `is_table` | bool | Tables kept as single units |
| `score` | float | Stage-2 score |
| `rank` | int | 1-based |

### StageRankingResult

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | FK |
| `example_id` | string | FK |
| `stage` | enum | `stage1`, `stage2` |
| `ordered_ids` | list[string] | doc types or chunk ids |
| `scores` | list[float] | Aligned with ordered_ids |
| `ndcg_at_5` | float | |
| `map_at_5` | float | |
| `mrr_at_5` | float | |
| `decision_distribution` | object | Probabilities/scores for MLflow |

### AnswerScore

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | FK |
| `example_id` | string | FK |
| `prediction` | string | Synthesized answer |
| `label` | string | Ground truth |
| `normalized_em` | float | 0 or 1 (official) |
| `token_f1` | float | Diagnostic |
| `status` | enum | `scored`, `skipped_no_label` |

### LedgerEntry

Atomic per-example progress in `eval_ledger.db`.

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | PK part |
| `example_id` | string | PK part |
| `state` | enum | See transitions |
| `attempts_stage1` | int | |
| `attempts_stage2` | int | |
| `attempts_synthesis` | int | |
| `last_error` | string \| null | |
| `updated_at` | datetime | |
| `ranking_payload_json` | object \| null | Durable Stage 1/2 + metrics at ranking-complete |
| `synthesis_payload_json` | object \| null | Answer + answer score when present |

### ToolInvocationRecord

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | |
| `example_id` | string | |
| `tool_name` | string | `mcp-sec-edgar.*` or `mcp-financial-calculator.*` |
| `request_json` | object | |
| `response_summary` | object | Redact secrets; keep numeric results |
| `status` | enum | `ok`, `error` |
| `latency_ms` | int | |

### TraceRecord

Logical MLflow-linked audit (ids stored in ledger or side table).

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | |
| `example_id` | string | |
| `mlflow_run_id` | string | |
| `span_names` | list[string] | Graph node names |
| `artifacts` | object | Pointers to rankings, tools, synthesis |

## Ledger state machine

```text
pending
  → in_progress
      → skipped_invalid          (missing required labels/content)
      → failed_retriable         (attempts exhausted on ranking; may resume later)
      → ranking_complete         (Stage1+Stage2+metrics committed)
            → synthesis_retriable  (synthesis failed after attempts)
            → completed            (synthesis + answer score path done, or synthesis intentionally disabled)
```

**Rules**:
- `ranking_complete` and `completed` MUST NOT re-run Stage 1/2 on resume.
- `synthesis_retriable` resumes at synthesis only.
- Transitions MUST be transactional (BEGIN IMMEDIATE / single commit).
- Only lease holder may transition states for a `run_id`.

## Validation rules

1. Stage 2 chunks MUST all share the Top-1 Stage-1 `doc_type`.
2. Metric functions MUST be pure given (ranking, labels).
3. Financial numerics in traces MUST reference calculator tool invocation ids.
4. Default K=5 for synthesis context; `HARNESS_MAX_ATTEMPTS` default 3.
5. Fail closed if health checks for required System-1 ports fail before ranking.
