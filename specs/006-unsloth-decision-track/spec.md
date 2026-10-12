# Feature Specification: Unsloth Decision-Model Training Track (Parallel to Paper Matrix)

**Feature Branch**: `006-unsloth-decision-track`

**Created**: 2026-10-12

**Status**: Draft

**Input**: GitHub issue [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5) — parallel **Unsloth `FastDecisionModel` / `DecisionTrainer`** Choice/Score training and evaluation on FinAgentBench, **without** modifying or overwriting published zero-shot paper matrix artifacts (`paper-n200-full`, `paper-p1-ceilings-n200`, etc.). Evaluation must use the **same metric contracts** (Stage-1 / Stage-2 nDCG@5, Top-1 recall, empty-Top-1, pipeline yield, conditional-on-Top-1) so results are **directly comparable** to non–RL-trained engines.

**Related**: [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) CLM-ft (separate), [#4](https://github.com/caldeirav/finagent-mesh-mcp/issues/4) LLM judge (separate). Issue [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) closed (CE ceiling); not in scope here.

## Clarifications

### Session 2026-10-12

- Q: For the first comparable eval run, which test example set should be the default? → A: **Paper slice only** — the published seed-42 N=200 `selected_example_ids` are the **test** split; train and validation MUST be drawn only from remaining labeled examples and MUST have zero intersection with that paper slice.
- Q: When building Stage-2 Score training rows, which passage candidate pool should each example use? → A: **Gold-type pool** — candidates are chunks of the gold Stage-1 filing type(s) only; eval still runs the compound pipeline (e.g. Lux Choice → trained Score).
- Q: For `lux-unsloth-score` eval on the paper test slice, how should Stage-1 Lux Choice be obtained? → A: **Reuse frozen Lux Choice** from `paper-n200-full` rankings/ledger for those example ids (same Top-1 / empty accounting as published Lux rows); do not re-run Lux Choice by default.
- Q: What should the v1 catalog / eval pairs include for the Unsloth track? → A: **Score pair only** — `lux-unsloth-score` (frozen Lux Choice × trained Score) is required for v1 acceptance; Choice train/eval and AnyJev×trained-Score compounds are deferred.
- Q: At eval time for trained Score under frozen Lux Top-1, full type pool or shortlist first? → A: **BM25 shortlist (k=32) → trained Score** (same K spirit as `lux-lux-shortlist`); analysis MUST compare to `lux-lux`, `lux-lux-shortlist`, and `lux-e5` read-only.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Leakage-safe training data from FinAgentBench (Priority: P1)

A researcher builds supervised decision-training examples from FinAgentBench (Stage-1 filing-type Choice; Stage-2 passage Score with relevance grades 0/1/2) using **example ids disjoint from the published paper evaluation sample** (seed 42, N=200 and its fixed `selected_example_ids`), documents the split hash, and can audit that no paper-test example appears in train/val.

**Why this priority**: Without a documented holdout, trained-model metrics cannot be compared fairly to the paper matrix.

**Independent Test**: Run the dataset builder; emit `train_ids.json`, `val_ids.json`, `test_ids.json`, and a leakage checklist that explicitly lists paper sample ids as **evaluation-only**; verify zero intersection with train/val.

**Acceptance Scenarios**:

1. **Given** the harness dataset, **When** the builder runs with the default split policy, **Then** `test_ids` equals the published paper `selected_example_ids` and train/val ids have **zero intersection** with that set (automated leakage test fails the build otherwise).
2. **Given** a Stage-2 training row, **When** materialized, **Then** each row includes query text, **gold Stage-1 type–filtered** passage candidates only, and Score criteria aligned to FinAgentBench relevance labels.
3. **Given** the builder completes, **When** an operator inspects metadata, **Then** split seed, counts, content hash, and explicit `test_source=paper-n200-full` are recorded for reproducibility.

---

### User Story 2 - Isolated Unsloth training pipeline (Priority: P1)

A researcher runs **supervised fine-tuning** (not RL in v1) in an **isolated** environment (separate optional dependency group / container from the default `uv sync --extra real` benchmark stack) to produce LoRA decision checkpoints for at least **Stage-2 Score**, with training config and metrics logged to MLflow or equivalent artifacts under a **dedicated prefix** (e.g. `unsloth-train/`), without invoking `scripts/run_benchmark.py` matrix execution or mutating existing `artifacts/benchmarks/paper-*` files.

**Why this priority**: Training is heavy and dependency-heavy; it must not destabilize the proven benchmark path.

**Independent Test**: Run training on a small smoke subset; confirm no changes to tracked `paper-n200-full*` / `paper-p1-ceilings-n200*` artifacts; confirm checkpoint + config artifacts exist under `artifacts/unsloth/` (or documented path).

**Acceptance Scenarios**:

1. **Given** missing Unsloth install, **When** an operator runs the default paper benchmark, **Then** behavior is unchanged (no import-time failure from optional training deps).
2. **Given** training completes, **When** artifacts are listed, **Then** run id, base model id, LoRA config, split hash, and final holdout/calibration metrics are persisted.
3. **Given** training is interrupted, **When** restarted with the same config, **Then** resume or explicit clean restart is documented (no silent partial overwrite of published eval runs).

---

### User Story 3 - Serve trained Score as a new engine family (Priority: P1)

A researcher registers a **new** System-1 engine family (e.g. `unsloth-decision-score`) with explicit **trained-track** labeling, exposes `/v1/systemone` Score (and optionally Choice in a later slice) via adapter or documented sidecar, and **fails closed** when checkpoint paths are missing (no silent fallback to Lux/CLM/E5).

**Why this priority**: Comparison requires the same agent harness contract as zero-shot engines.

**Independent Test**: Start sidecar with valid checkpoint; healthz OK; one FinAgentBench example returns ranked chunk ids; missing weights → explicit error.

**Acceptance Scenarios**:

1. **Given** `engines.yaml`, **When** listing engines, **Then** Unsloth-trained engines appear as optional / trained-track, not default required Block A/B pairs.
2. **Given** a missing checkpoint env var, **When** Score is requested, **Then** the engine reports unsupported/fail-closed (same spirit as other real engines).
3. **Given** inference, **When** scoring passages, **Then** output is consumable by existing Stage-2 node (ordered ids + scores).

---

### User Story 4 - Comparable evaluation run (separate from paper matrix) (Priority: P1)

A researcher runs a **dedicated eval command** (separate entrypoint from `run_benchmark.py` default matrix, e.g. `scripts/run_unsloth_eval.py` or `run_benchmark.py --unsloth-eval-only`) that reuses the **FinAgentBench harness**, ledger, and **metric definitions** on the paper test slice, with **Stage-1 Lux Choice frozen** from published `paper-n200-full` rankings and **Stage-2 = BM25 top-32 shortlist → trained Unsloth Score**, produces matrix-style reports under **`artifacts/benchmarks/unsloth-*`** (new run ids only), and analysis sections that **reference** but do not edit `paper-n200-full` / `paper-p1-ceilings-n200` tables.

**Why this priority**: Delivers the issue’s core value—measurable comparison to Lux/E5/shortlist-Lux—without contaminating published baselines; shortlist matches the Stage-2 pattern that already outperformed full-pool Lux Score on this sample.

**Independent Test**: Run eval for `lux-unsloth-score` on N=200 paper ids; output includes S2 nDCG@5 scored + pipeline + conditional Top-1; side-by-side vs `lux-lux`, `lux-lux-shortlist`, and `lux-e5` from published JSON (read-only).

**Acceptance Scenarios**:

1. **Given** a completed eval run, **When** analysis is generated, **Then** a **Trained decision track (Unsloth)** section appears with role labels distinct from zero-shot Block B.
2. **Given** published paper artifacts, **When** comparison summary is built, **Then** deltas are computed read-only vs at least `lux-lux`, `lux-lux-shortlist`, and `lux-e5` (no re-run of zero-shot engines required).
3. **Given** eval run id `unsloth-score-paper-n200`, **When** artifacts are written, **Then** no file overwrites `paper-n200-full.*` or `paper-p1-ceilings-n200.*`.
4. **Given** default `lux-unsloth-score` eval, **When** Stage-1 is applied, **Then** Top-1 doc types match the frozen Lux Choice from `paper-n200-full` for each test id (Stage-1 GPU re-inference is not required).
5. **Given** Stage-2 for `lux-unsloth-score`, **When** scoring runs, **Then** candidates under the frozen Top-1 type are BM25-shortlisted to **k=32** before the trained Score head; shortlist size is recorded in run metadata.

---

### User Story 5 - Optional Choice / compound cells (Priority: P3 — deferred past v1)

Out of v1 acceptance: trained Choice pairs and AnyJev×trained-Score compounds. May be added later after `lux-unsloth-score` lands; not required for issue #5 v1 close.

---

### Edge Cases

- Paper eval ids must never appear in train/val; if the operator overrides exclusions, the run must be labeled **non-comparable** in analysis.
- Examples with empty Top-1-type chunk pools must follow existing `empty_top1_chunks` semantics (no fabricated ranks).
- Very long gold-type passage lists: training and inference must document max candidates / truncation (aligned with Unsloth `max_seq_length` and GPU budget).
- Gold-type training vs Lux Top-1 eval mismatch: when Choice is wrong, empty-Top-1 and yield accounting stay as in the zero-shot harness; analysis MUST note Score was trained on gold-type pools.
- Checkpoint version skew (base model revision vs adapter): fail closed with explicit version metadata.
- Concurrent training and benchmark on one GPU: documented sequential policy (constitution-aligned), no implicit sharing.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a FinAgentBench → decision-training export that supports Unsloth-style **Score** rows (query + **gold-type** candidates + graded criteria) and optional **Choice** rows (typed criteria map). Score training candidates MUST be restricted to chunks whose filing type is in the example’s gold Stage-1 label set.
- **FR-002**: Default split MUST set **test** = published paper matrix `selected_example_ids` (seed 42, N=200 from `paper-n200-full`) and MUST build train/val only from remaining labeled examples with **zero id overlap** with test; the id lists + source run id MUST be versioned (content hash).
- **FR-003**: Training MUST run via a **separate** CLI/script and optional dependency group; MUST NOT be required for default `run_benchmark.py --real`.
- **FR-004**: Training outputs MUST include checkpoint path, base model identifier, LoRA hyperparameters, split hash, seed, and MLflow run id (or equivalent).
- **FR-005**: A new engine family MUST implement Score inference compatible with existing Stage-2 integration; MUST NOT reuse `decide_decision20`, CLM heads, or AnyJev weights.
- **FR-006**: Eval MUST reuse harness ranking metrics and inspect/analysis contracts; output paths MUST use distinct run id namespace (`unsloth-*`).
- **FR-007**: Analysis MUST include a trained-track section and a read-only comparison against published metrics for the same test ids vs at least `lux-lux`, `lux-lux-shortlist`, and `lux-e5`.
- **FR-008**: Catalog MUST add optional trained-track pair **`lux-unsloth-score`** (`role=trained_decision` or equivalent) for v1; Choice pairs and AnyJev×Unsloth compounds MUST NOT be required for v1 acceptance (may remain documented as future optional).
- **FR-009**: Missing trained weights MUST skip or error explicitly; MUST NOT substitute Lux, E5, BM25, or CLM under trained pair ids.
- **FR-010**: Published artifacts under `paper-n200-full*` and `paper-p1-ceilings-n200*` MUST remain immutable by this feature’s automation (no overwrite in scripts).
- **FR-011**: Documentation MUST state this is a **parallel stack** (not a drop-in upgrade to Decision-2.0 Lux weights).
- **FR-012**: v1 training MUST be **supervised** (`DecisionTrainer`); RL/GRPO for decision models is out of scope unless a later spec explicitly adds it.
- **FR-013**: Default `lux-unsloth-score` eval MUST **reuse frozen Stage-1 Lux Choice** (Top-1 and related ranking fields) from the published `paper-n200-full` investigation/ledger for paper test ids; Stage-1 metrics MAY be copied from the frozen source and labeled as such.
- **FR-014**: Default Stage-2 for `lux-unsloth-score` MUST apply a **BM25 shortlist of size 32** over the frozen Top-1 type pool, then the trained Unsloth Score head on that shortlist; shortlist size MUST appear in run metadata and analysis.

### Recommended training strategy (planning input — validated against Unsloth docs)

*Captured for `/speckit-plan`; not binding implementation detail in this spec. Direction locked to **Qwen3.8** per operator request (2026-10-12).*

| Decision | Recommendation | Rationale |
|----------|----------------|-----------|
| Base model (Score v1) | `unsloth/Qwen3.8-27B-unsloth-bnb-4bit` (4-bit QLoRA; text-only; `max_seq_length=2048` default, raise only if GPU allows) | Unsloth decision docs target fine-tuning **Qwen3.8** into typed decision models; [Qwen3.8 train guide](https://unsloth.ai/docs/models/qwen3.8/train) documents QLoRA on ~24GB and ZGX Nano / DGX Spark unified memory can host sequential 27B QLoRA |
| Vision / multimodal | **Off** (`finetune_vision_layers=False` if using FastModel PEFT knobs) | FinAgentBench is text passages only |
| Base model (smoke / CI) | Smaller Qwen3.5 decision recipe **only** for unit/smoke if 27B cannot load in CI; production train+eval remains Qwen3.8-27B | Keeps laptop/CI green without claiming parity |
| Method | Prefer `FastDecisionModel` + `DecisionTrainer` QLoRA (r=16–64) when the Qwen3.8 checkpoint is supported as `model_name`; else document fallback to Unsloth decision export path from the same family | Typed `choice`/`score`/`noul` + `predict`/`calibrate` match FinAgentBench; Qwen3.8 SFT-only (`FastModel`+`SFTTrainer`) is **not** the primary Score head path |
| Precision | Train and serve in **same** 4-bit QLoRA precision; optional merge/export later | Unsloth: train/serve same precision preserves accuracy |
| Score criteria | Map FinAgentBench relevance {0,1,2} to ordinal Score criteria list | Matches `type: score` + `criteria: [...]` in `FastDecisionModel.predict` |
| Choice criteria | Five filing types as `type: choice` criteria map | Matches Stage-1 harness enums |
| Post-train | `FastDecisionModel.calibrate` on held-out split when available | Aligns probabilities with accuracy per Unsloth decision docs |
| Split | Custom FinAgentBench id split + holdout on exported items | Paper ids held out for eval only |
| Env | Isolated Unsloth install (latest Transformers for `qwen3_5` arch); optional DGX Spark Docker | Avoid torch/transformers conflicts with benchmark stack; first run may compile Gated DeltaNet kernels |

References: [Qwen3.8 fine-tuning](https://unsloth.ai/docs/models/qwen3.8/train), [Train your own decision model](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth), [Decision Laya serve API](https://unsloth.ai/docs/models/decision-laya).

### Key Entities

- **TrainingExampleExport**: FinAgentBench example id, stage, query, candidates, labels, metadata (firm, doc types).
- **SplitManifest**: train/val/test id lists, paper_eval_excluded_ids, seed, content_hash, created_at.
- **UnslothTrainRun**: config, metrics, checkpoint paths, MLflow run id.
- **UnslothEvalMatrixRun**: same shape as `MatrixRun` but distinct namespace and trained-track metadata.
- **ComparisonSummary**: pair_id, metric name, trained value, published zero-shot value, delta (read-only source).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of paper matrix evaluation example ids are absent from train+val splits in the default configuration (automated leakage test).
- **SC-002**: A smoke training run (≤1k Stage-2 rows) completes and produces a loadable checkpoint with documented metadata.
- **SC-003**: A smoke eval run (≥20 examples) on trained Score produces harness metrics in the same schema as `paper-n200-full` rows (S1/S2 nDCG@5, empty rate, yield).
- **SC-004**: Comparison report lists trained vs published S2 nDCG@5 for `lux-unsloth-score` vs at least `lux-lux`, `lux-lux-shortlist`, and `lux-e5` on the same test ids without modifying published JSON.
- **SC-005**: Zero-shot benchmark regression: running `run_benchmark.py --analysis-from paper-n200-full` on a clean tree yields identical metrics JSON to committed `paper-n200-full.json` (checksum or diff test in CI).
- **SC-006**: Operators can complete train → eval → analysis using documented commands without editing `configs/engines.yaml` required pairs.

## Assumptions

- Primary v1 deliverable is **Stage-2 Score** training and the **`lux-unsloth-score`** eval pair only (frozen Lux Choice + BM25 k=32 + trained Score); Choice training and other compounds are deferred past v1.
- Training may still truncate gold-type pools for seq-length limits; eval shortlist policy (k=32) is independent and fixed for v1.
- **Base model family for production train/eval is Qwen3.8-27B** (Unsloth 4-bit QLoRA checkpoint), not Qwen3.5-4B.
- Default split: **test = paper slice only**; train/val = disjoint remainder. A secondary non-paper test split is out of scope for v1 unless later clarified.
- Training uses **supervised** decision fine-tuning (`DecisionTrainer` when supported on Qwen3.8), not RL/GRPO, unless scope is expanded (Qwen3.8 RL docs exist but are out of scope for v1).
- Checkpoints live under `artifacts/unsloth/` (gitignored except manifests); not committed to git.
- AnyJev L0/L1 calibration remains out of scope; Unsloth does not replace AnyJev.
- Issue #5 acceptance checklist items map to user stories 1–4.

## Out of Scope

- Replacing or hot-swapping Decision-2.0 Lux / AnyJev / CLM inference paths.
- RL / GRPO decision training (v1).
- LLM-as-judge answer metrics ([#4](https://github.com/caldeirav/finagent-mesh-mcp/issues/4)).
- CLM dual-encoder FT ([#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1)) unless explicitly merged later.
- Modifying published `paper-n200-full` / `paper-p1-ceilings-n200` artifact files or re-running zero-shot matrix as part of training CI.
