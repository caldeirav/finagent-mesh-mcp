#!/usr/bin/env bash
# Install Unsloth fine-tune stack entirely via uv sync (pyproject extras).
#
# Usage:
#   bash scripts/install_unsloth_zgx.sh
#   bash scripts/install_unsloth_zgx.sh --with-real
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

WITH_REAL=0
for arg in "$@"; do
  case "$arg" in
    --with-real) WITH_REAL=1 ;;
    -h|--help)
      sed -n '2,8p' "$0"
      exit 0
      ;;
  esac
done

echo "==> uv sync (Unsloth extra from pyproject.toml)"
if [[ "$WITH_REAL" -eq 1 ]]; then
  uv sync --extra real --extra unsloth
else
  uv sync --extra unsloth
fi

echo "==> Verifying imports"
uv run python - <<'PY'
import importlib.util
import torch

required = [
    "torch", "torchvision", "transformers", "accelerate", "peft", "trl",
    "datasets", "bitsandbytes", "sentencepiece", "hf_transfer", "diffusers",
    "unsloth", "unsloth_zoo",
]
missing = [n for n in required if importlib.util.find_spec(n) is None]
assert not missing, f"missing: {missing}"
assert torch.cuda.is_available(), "CUDA not available"
from unsloth import DecisionTrainer, FastDecisionModel  # noqa: F401
print(
    f"ok: uv-managed Unsloth stack; torch={torch.__version__}; "
    f"cuda={torch.version.cuda}; xformers="
    f"{'present' if importlib.util.find_spec('xformers') else 'absent (OK)'}"
)
PY

echo
echo "Train: uv run python scripts/train_unsloth_score.py ..."
