# Research: Decision Model Serving & Benchmark Matrix

**Feature**: `002-decision-model-bench` | **Date**: 2026-10-04

## 1. Unified decision interface

**Decision**: Keep the harness-facing contract as System-1 `/healthz` + `/v1/systemone` (`choice` | `score` | `action_cache`), with thin per-engine adapters that translate native engine APIs into that shape.

**Rationale**: Existing `OpenDecisionClient` and LangGraph nodes already speak this contract. Adapters isolate anyjev / clm-serve / vLLM-sr / Transformers / instruct-JSON quirks without rewriting the agent graph.

**Alternatives considered**:
- Native SDK calls from graph nodes — couples orchestration to five stacks.
- OpenAI-compat chat only — insufficient for Choice/Score distributions and Action Cache.

## 2. Engine matrix catalog

**Decision**: Seven named configurations in `configs/engines.yaml`:

| Config ID | Family | Primary stage | Runtime |
|-----------|--------|---------------|---------|
| `anyjev-l0` | AnyJev L0 (Qwen3-8B) | Stage 1 Choice | anyjev + local vLLM |
| `anyjev-l1` | AnyJev L1 (Qwen3-8B) | Stage 1 Choice | anyjev + vLLM + 200-ex calibration |
| `clm-8b` | CLM-8B Action Cache | Stage 2 Score | clm-serve + `vllm serve … --runner pooling` |
| `decision20-kai` | vLLM-sr Decision-2.0 Kai-0.6B | Stage 1 Choice | vLLM feature extraction |
| `decision20-lux` | vLLM-sr Decision-2.0 Lux-9B | Stage 1 Choice | vLLM feature extraction |
| `laya-modernbert` | Laya ModernBERT 421M | Stage 1 Choice (edge) | HF Transformers |
| `ar-qwen3-8b-instruct` | Autoregressive baseline | Stage 1 JSON choice | instruct generation endpoint |

**Rationale**: Matches clarified spec matrix rows; separates L0/L1 and Kai/Lux for reporting.

**Alternatives considered**: Collapsing L0/L1 into one row — loses calibration comparison.

## 3. Architecture-true Stage 1×2 pairs (default matrix)

**Decision**: Default production matrix is an explicit `matrix_pairs` list in `configs/engines.yaml`, not a full cross-product and not “every engine × fixed partner”.

| Pair | Stage 1 | Stage 2 | Role |
|------|---------|---------|------|
| `lux-clm` | `decision20-lux` | `clm-8b` | Production Choice × Action Cache Score |
| `anyjev-l0-clm` | `anyjev-l0` | `clm-8b` | Order-debiased Choice × CLM |
| `anyjev-l1-clm` | `anyjev-l1` | `clm-8b` | Optional; requires 200-id calibration |
| `kai-clm` | `decision20-kai` | `clm-8b` | Latency S1 router × CLM |
| `laya-clm` | `laya-modernbert` | `clm-8b` | Edge S1 × CLM |
| `lux-lux` | `decision20-lux` | `decision20-lux` | Long-context Score control |
| `ar-clm` | `ar-qwen3-8b-instruct` | `clm-8b` | Baseline; `--include-baseline` |

Rationale: FinAgentBench Stage 1 is K=5 **Choice** (filing types); Stage 2 is **Score** over long enumerated chunks. CLM’s Action Cache matches Stage 2; compact bidirectional models match Stage 1 routing only. Stage-1 errors impose a pre-filtering recall ceiling on Stage 2. `--engines` preserves the older one-variable + fixed-partner ablation (`stage2_partner_id=clm-8b`, `stage1_partner_id=anyjev-l0`).

**Alternatives considered**: Full S1×S2 cross-product — ops/GPU cost. CLM or Laya as both stages — primitive/context mismatch. Offline stage-only jobs — rejected by operator (end-to-end LangGraph still required).

## 4. Sequential matrix orchestration

**Decision**: `scripts/run_matrix.py` iterates matrix rows: stop previous variable engine → start row engine (+ ensure partner) → health check → run seeded sample/full pipeline with bindings → export row metrics → next row.

**Rationale**: Avoids multi-large-model OOM on 128GB unified memory while keeping partner available.

**Alternatives considered**: Full concurrent matrix — memory risk. Fully serial including tearing down partner — slower and breaks Action Cache warm state unnecessarily.

## 5. Fail-closed Gemini System-2

**Decision**: Remove extractive chunk-head fallback in `GeminiClient`. Missing key / API errors → raise; harness marks `synthesis_retriable` / failed. Default model `gemini-2.5-flash`; Pro via env/flag.

**Rationale**: Spec FR-012/013/023 and SC-004/010.

**Alternatives considered**: Keep offline extractive path — violates fail-closed requirement.

## 6. Mock disable for official runs

**Decision**: Official matrix/pipeline claims require `SYSTEMONE_MOCK=0`. Matrix runner refuses to start if mock is enabled unless `--allow-mock` debug flag is set (recorded in config).

**Rationale**: SC-003 / FR-004.

## 7. Sampling

**Decision**: Seeded Fisher–Yates / `random.Random(seed).sample` over example IDs; persist `sample_seed`, `sample_size`, and selected IDs in run config.

**Rationale**: SC-005 reproducibility.

## 8. Autoregressive baseline metrics

**Decision**: Adapter prompts for JSON `{"ordered_ids":[...],"scores":[...]}` (or ranked list); on parse failure record `parse_failure=1` and fail the example’s Stage-1 structured ranking; always log generation latency_ms and optional token logprobs for calibration summaries.

**Rationale**: FR-009 / SC-006.

## 9. AnyJev L1 calibration

**Decision**: Require `configs/calibration/anyjev_l1_heldout.json` (200 example IDs). Startup of `anyjev-l1` fails closed if missing or wrong cardinality.

**Rationale**: Spec edge case + FR-005.

## 10. Port map (default)

**Decision** (overridable in `engines.yaml`):

| Role | Default port |
|------|----------------|
| Variable / Stage-1 Choice | 8000 |
| Stage-2 partner CLM-8B | 8001 |
| Alternate Choice partner when CLM is under test | 8002 |

When the variable engine *is* CLM-8B, Stage-1 partner `anyjev-l0` binds to 8000 and CLM to 8001.

**Rationale**: Preserves prior harness defaults; adds explicit partner port when both Choice engines would collide.

## 11. Reporting

**Decision**: Matrix export JSON (+ optional CSV) with one section per variable engine: Stage-1/2 metrics attributed to producing engine ids, latency percentiles, synthesis/answer-score aggregates, parse_failure_rate (AR), calibration fields (AnyJev-L1 / AR).

**Rationale**: FR-015/021, SC-007.
