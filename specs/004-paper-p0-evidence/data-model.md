# Data Model: Paper P0 Evidence Pack

**Feature**: `004-paper-p0-evidence` | **Date**: 2026-10-09

Extends Spec 003 matrix/analysis entities; does not replace pair catalog identities.

## Entities

### PipelineYield (per pair)

| Field | Type | Notes |
|-------|------|-------|
| pair_id | string | Stable catalog id |
| n_examples | int | N |
| n_scored | int | Non-empty Stage-2 ranking list |
| n_empty_top1 | int | empty_top1_chunks |
| pipeline_yield | float | n_scored / N |
| stage1_top1_recall | float | Existing |

### RoutingClassCounts (per pair)

| Field | Type | Notes |
|-------|------|-------|
| pair_id | string | |
| counts | map[class_id → int] | See research.md class ids |
| rates | map[class_id → float] | counts / N |

**Validation**: Sum of class counts = N (or N − unexplained with `other` absorbing residuals).

### Stage2MetricSeries (per pair)

| Field | Type | Notes |
|-------|------|-------|
| scored_mean | map[metric → float\|null] | Primary: ndcg@5, map@5, mrr@5 (+ conditional) |
| pipeline_mean | map[metric → float\|null] | Secondary: empties/unscored as 0; at least ndcg@5, mrr@5 |
| label_scored | string | e.g. `scored_only` |
| label_pipeline | string | e.g. `pipeline_averaged` |

### StratumCell

| Field | Type | Notes |
|-------|------|-------|
| axis | enum | `gold_type` \| `cand_size` \| `length` |
| bucket | string | Type name or bucket label |
| pair_id | string | Block B scorer pair |
| n | int | Scored examples in cell |
| stage2_ndcg_at_5 | float\|null | Mean in cell |

### WinLossSummary

| Field | Type | Notes |
|-------|------|-------|
| challenger_pair_id | string | e.g. `lux-e5` |
| baseline_pair_id | string | `lux-lux` |
| metric | string | `stage2_ndcg_at_5` |
| tie_epsilon | float | `0.01` |
| n_compared | int | Examples scored in both |
| wins | int | Challenger − baseline ≥ ε |
| losses | int | Baseline − challenger ≥ ε |
| ties | int | \|Δ\| < ε |
| sample_wins | list[{example_id, delta, href}] | Extreme \|Δ\| |
| sample_losses | list[{example_id, delta, href}] | |

### BootstrapInterval

| Field | Type | Notes |
|-------|------|-------|
| pair_id | string | Or `delta:challenger-baseline` |
| metric | string | |
| point | float | Observed mean / Δ |
| ci_low | float | 2.5th percentile |
| ci_high | float | 97.5th percentile |
| n_resamples | int | ≥1000 |
| bootstrap_seed | int | |

### SeedReplicate

| Field | Type | Notes |
|-------|------|-------|
| seed | int | 42, 7, or 123 |
| matrix_run_id | string | |
| pair_id | string | Core subset |
| metrics | map | Primary scored-only headline metrics |
| selected_example_ids | list[string] | Independent sample |

### MultiSeedRollup

| Field | Type | Notes |
|-------|------|-------|
| pair_id | string | |
| metric | string | |
| per_seed | map[seed → float] | |
| mean_of_means | float | |
| min | float | |
| max | float | |

### SynthesisReuseRun

| Field | Type | Notes |
|-------|------|-------|
| run_id | string | e.g. `paper-n200-full-synth` |
| ranking_source_run_ids | list[string] | Eval/matrix sources for rankings |
| pairs | list[string] | Four synthesis pairs |
| n_attempted | int | |
| n_failed | int | |
| n_skipped_no_evidence | int | |
| answer_normalized_em | float\|null | Per pair aggregates |
| answer_token_f1 | float\|null | |

## Relationships

```text
MatrixRun
  └── MatrixRowResult (pair)
        ├── PipelineYield
        ├── RoutingClassCounts
        ├── Stage2MetricSeries
        └── BootstrapInterval*

AnalysisPayload
  ├── findings_detail (routing, strata narrative, takeaways)
  ├── strata: StratumCell[]
  ├── win_loss: WinLossSummary[]
  ├── uncertainty: BootstrapInterval[]
  ├── multi_seed: MultiSeedRollup[] (optional if rollup file exists)
  └── synthesis: SynthesisReuseRun summary (optional)

SeedReplicate[] ──rollup──► MultiSeedRollup[]
```

## State / lifecycle notes

- Ranking metrics for `paper-n200-full` are **immutable** under synthesis reuse; synthesis attaches answer fields without recomputing S1/S2 nDCG.
- Multi-seed replicates are separate MatrixRuns; rollup is derived at analysis time.
- Optional pairs may be merged into an analysis view of the published sample via existing `merge_matrix_runs` or side-by-side sections.
