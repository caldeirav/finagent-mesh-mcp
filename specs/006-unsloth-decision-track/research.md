# Research: Unsloth Decision Track (006)

## 1. Base model

**Decision**: Production train/eval on `unsloth/Qwen3.8-27B-unsloth-bnb-4bit` (4-bit QLoRA, text-only, default `max_seq_length=2048`).

**Rationale**: Operator direction + Unsloth [Qwen3.8 train guide](https://unsloth.ai/docs/models/qwen3.8/train) (QLoRA ~24GB; ZGX Nano ~128GB unified). Decision docs describe fine-tuning **Qwen3.8** into typed decision models. Vision layers off for FinAgentBench text.

**Alternatives considered**:
- `unsloth/Qwen3.5-4B` (decision tutorial default) — retained only for CI/smoke if 27B cannot load.
- Full LoRA &gt;36GB / FFT — rejected for v1 VRAM budget.
- RL/GRPO on Qwen3.8 — out of scope (spec FR-012).

## 2. Training API path

**Decision**: Prefer `FastDecisionModel.from_pretrained` + `get_peft_model` + `DecisionTrainer` + `calibrate` / `predict` ([train your own decision model](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth)). If Qwen3.8-27B is not accepted as `FastDecisionModel` `model_name` at implement time, document a gated fallback (same family decision export) without switching to plain SFT as the Score head.

**Rationale**: Typed `score` with criteria lists maps to FinAgentBench relevance {0,1,2}; calibrated probabilities fit System-1 contracts. Plain `FastModel`+`SFTTrainer` does not produce Score primitives.

**Alternatives considered**: Conversational SFT only — rejected as primary Score path.

## 3. Data split & leakage

**Decision**: `test_ids` = `paper-n200-full.selected_example_ids` (N=200, seed 42). Train/val = remaining labeled examples; zero intersection enforced in CI/unit tests. Manifest stores content hash + `test_source=paper-n200-full`.

**Rationale**: Clarification A — direct comparability to published zero-shot metrics without training on the paper slice.

**Alternatives considered**: Dual non-paper test; paper ids never as test — rejected for v1.

## 4. Score training candidate pool

**Decision**: Gold Stage-1 type–filtered chunks only for training rows.

**Rationale**: Clarification — clean Score supervision; eval still uses frozen Lux Top-1 (pipeline realism).

**Alternatives considered**: Pipeline Top-1 pools; all-chunks — rejected for v1.

## 5. Eval Stage-1

**Decision**: Reuse frozen Lux Choice (Top-1, empty accounting) from `paper-n200-full` inspect JSON / ledger ranking payloads for each test example id. Do not re-run Lux Choice by default.

**Rationale**: Fair Score bake-off; identical yield/empty rates to published Lux rows; less GPU.

**Alternatives considered**: Live Lux re-run — optional later flag only if needed.

## 6. Eval Stage-2 orchestration

**Decision**: BM25 shortlist **k=32** then trained Unsloth Score (mirror `LuxShortlistAdapter` with Unsloth backend). Pair id `lux-unsloth-score`. Compare read-only to `lux-lux`, `lux-lux-shortlist`, `lux-e5`.

**Rationale**: Clarification B — shortlist-Lux already best published S2 (~0.35); 27B context/VRAM friendly.

**Alternatives considered**: Full Top-1 pool; dual full+shortlist pairs — rejected for v1 scope.

## 7. Isolation from paper matrix

**Decision**: Separate CLIs (`export_*`, `train_*`, `run_unsloth_eval.py`); run ids `unsloth-*`; artifacts under `artifacts/unsloth/` and `artifacts/benchmarks/unsloth-*`. Scripts MUST refuse to write paths matching published paper stems. Optional dependency group so `uv sync` / default `--extra real` does not require Unsloth.

**Rationale**: Spec FR-003/FR-010; issue #5 parallel track.

## 8. Serving

**Decision**: In-process or sidecar adapter implementing System-1 Score via `FastDecisionModel.for_inference` + `predict` with Score criteria over candidate texts; env `UNSLOTH_SCORE_CHECKPOINT` (fail-closed). Prefer in-process hybrid for BM25+Score like other shortlist engines; heavy 27B may need dedicated process — implement-time choice documented in quickstart.

**Rationale**: Align with [Decision Laya `/v1/systemone`](https://unsloth.ai/docs/models/decision-laya) vocabulary; harness Stage-2 already consumes ordered ids + scores.

## 9. Dependency strategy

**Decision**: `pyproject.toml` optional-extra `unsloth` (pin Unsloth + compatible torch/transformers). Document `uv sync --extra unsloth` (or separate venv) for train/eval. Unit tests mock Unsloth imports.

**Rationale**: Avoid breaking ARM64 real-stack pin for zero-shot benchmarks.
