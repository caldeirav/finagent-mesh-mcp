# Data Model: Decision Model Serving & Benchmark Matrix

**Feature**: `002-decision-model-bench` | **Date**: 2026-10-04

Extends entities from `specs/001-finagentbench-harness/data-model.md` (BenchmarkExample, StageRankingResult, LedgerEntry, AnswerScore, EvaluationRun).

## Entities

### EngineConfiguration

Named matrix / pipeline engine row.

| Field | Type | Notes |
|-------|------|-------|
| `config_id` | string (PK) | e.g. `anyjev-l0`, `clm-8b`, `decision20-kai` |
| `family` | string | anyjev, clm, vllm-sr, laya, ar-baseline |
| `display_name` | string | Human label |
| `primitives` | list[enum] | `choice`, `score`, `action_cache`, `json_choice` |
| `primary_stages` | list[enum] | `stage1`, `stage2` |
| `base_url` | string | Default serve URL |
| `health_path` | string | default `/healthz` |
| `decide_path` | string | default `/v1/systemone` |
| `container_ref` | string | Image/tag or local process key |
| `weights_ref` | string | Operator path / HF id |
| `calibration_ref` | string \| null | Required for `anyjev-l1` |
| `is_heavy_gpu` | bool | Variable-engine exclusivity applies when true |
| `is_light_edge` | bool | e.g. Laya |
| `model_revision` | string | Recorded in traces |

**Validation**: `config_id` unique; `anyjev-l1` MUST have calibration_ref resolving to 200 IDs.

### FixedStagePartners

| Field | Type | Notes |
|-------|------|-------|
| `stage2_partner_id` | string | Default `clm-8b` |
| `stage1_partner_id` | string | Default `anyjev-l0` |

### PipelineBinding

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | string | FK |
| `stage1_config_id` | string | FK EngineConfiguration |
| `stage2_config_id` | string | FK EngineConfiguration |
| `variable_config_id` | string \| null | Matrix row under test; null for free pipeline bind |
| `gemini_model` | string | Default `gemini-2.5-flash` |
| `synthesis_enabled` | bool | Default true |
| `systemone_mock` | bool | MUST be false for official claims |

### MatrixRun

| Field | Type | Notes |
|-------|------|-------|
| `matrix_run_id` | string (PK) | |
| `created_at` | datetime | |
| `dataset_path` | string | |
| `sample_size` | int \| null | null = full set |
| `sample_seed` | int \| null | Required if sample_size set |
| `selected_example_ids` | list[string] | Persisted when sampled |
| `config_ids` | list[string] | Variable engines to evaluate |
| `status` | enum | `pending`, `running`, `completed`, `failed` |
| `partner_ids` | object | Copy of FixedStagePartners used |

**Relationships**: Has many `MatrixRowResult`; each row spawns/links an `EvaluationRun` (`run_id = matrix_run_id + ":" + config_id`).

### MatrixRowResult

| Field | Type | Notes |
|-------|------|-------|
| `matrix_run_id` | string | PK part |
| `variable_config_id` | string | PK part |
| `eval_run_id` | string | Ledger/harness run |
| `stage1_engine_id` | string | Actual producer |
| `stage2_engine_id` | string | Actual producer |
| `metrics` | object | See EngineMetricsRecord |
| `status` | enum | `pending`, `running`, `completed`, `failed` |
| `error` | string \| null | |

### EngineMetricsRecord

| Field | Type | Notes |
|-------|------|-------|
| `stage1_ndcg_at_5` | float \| null | Attributed to stage1_engine_id |
| `stage1_map_at_5` | float \| null | |
| `stage1_mrr_at_5` | float \| null | |
| `stage2_ndcg_at_5` | float \| null | Attributed to stage2_engine_id |
| `stage2_map_at_5` | float \| null | |
| `stage2_mrr_at_5` | float \| null | |
| `latency_ms_p50` | float \| null | Decision latency |
| `latency_ms_p95` | float \| null | |
| `parse_failure_rate` | float \| null | AR baseline |
| `answer_normalized_em` | float \| null | Gemini path |
| `answer_token_f1` | float \| null | |
| `n_examples` | int | |
| `n_synthesis_attempted` | int | |
| `n_synthesis_failed` | int | |

### CalibrationSet

| Field | Type | Notes |
|-------|------|-------|
| `calibration_id` | string | e.g. `anyjev_l1_heldout` |
| `example_ids` | list[string] | Exactly 200 |
| `source` | string | FinAgentBench split descriptor |

### ActionCacheArtifact

| Field | Type | Notes |
|-------|------|-------|
| `cache_id` | string | |
| `engine_config_id` | string | `clm-8b` |
| `embedding_dim` | int | |
| `candidate_space` | string | e.g. doc-types or chunk vocab key |
| `storage_uri` | string | Local path |

## Matrix row binding rules

```text
for variable V in matrix.config_ids:
  if V.primary includes stage1 and not stage2:
    stage1 = V; stage2 = partners.stage2_partner_id  # clm-8b
  else if V.primary includes stage2 and not stage1:
    stage2 = V; stage1 = partners.stage1_partner_id  # anyjev-l0
  else:
    stage1 = V; stage2 = V   # or explicit dual-capable
  run agentic process once per example with (stage1, stage2)
  attribute metrics to producing engine ids
```

## State transitions (MatrixRun)

```text
pending → running → completed
                 ↘ failed
```

Row-level mirrors harness ledger states for the linked `eval_run_id`.

## Validation rules

1. Official matrix: `systemone_mock` MUST be false.
2. Default `synthesis_enabled` true; Gemini model default Flash.
3. Partner + variable may co-run; two *variable* heavy engines MUST NOT.
4. Calibration set size MUST be 200 for AnyJev L1 start.
5. Selected sample IDs MUST be stable for `(seed, size, dataset_version)`.
