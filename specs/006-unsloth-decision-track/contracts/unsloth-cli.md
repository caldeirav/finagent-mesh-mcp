# Contract: Unsloth track CLIs

Separate from default paper matrix. None of these commands may overwrite `artifacts/benchmarks/paper-n200-full*` or `paper-p1-ceilings-n200*`.

## Export

```bash
uv run python scripts/export_unsloth_dataset.py \
  --dataset-path data/finagentbench \
  --paper-matrix artifacts/matrix_runs/paper-n200-full.json \
  --out-dir artifacts/unsloth/datasets/fab-paper-test-v1
```

**MUST**: Write `split_manifest.json`, train/val JSONL (or HF dataset dir), leakage report; exit non-zero on paper-id leakage into train/val.

## Train

```bash
uv run --extra unsloth python scripts/train_unsloth_score.py \
  --dataset-dir artifacts/unsloth/datasets/fab-paper-test-v1 \
  --base-model unsloth/Qwen3.8-27B-unsloth-bnb-4bit \
  --out-dir artifacts/unsloth/checkpoints/score-qwen38-r16 \
  --run-id unsloth-train-score-001
```

**MUST**: Persist train config JSON + MLflow tags; refuse if split test_ids ≠ paper selected ids.

## Eval

```bash
uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score \
  --paper-matrix artifacts/matrix_runs/paper-n200-full.json \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/score-qwen38-r16 \
  --records 200 --seed 42 \
  --run-id unsloth-score-paper-n200
```

**MUST**:
- Run id prefix / stem `unsloth-`
- Reuse frozen Lux Top-1 for each example
- Stage-2 BM25→Unsloth Score k=32
- Write under `artifacts/benchmarks/unsloth-score-paper-n200.*` and `artifacts/matrix_runs/unsloth-score-paper-n200.json`
- Emit comparison table vs published baselines (read-only)

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `UNSLOTH_SCORE_CHECKPOINT` | — | Path to LoRA / merged decision checkpoint |
| `UNSLOTH_SHORTLIST_K` | `32` | BM25 shortlist before trained Score |
| `UNSLOTH_BASE_MODEL` | `unsloth/Qwen3.8-27B-unsloth-bnb-4bit` | Base id for train/serve |

## Forbidden

- Writing published paper artifact paths
- Importing Unsloth inside `run_benchmark.py` module import path for default matrix
