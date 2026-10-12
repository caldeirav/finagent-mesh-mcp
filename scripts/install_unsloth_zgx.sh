#!/usr/bin/env bash
# Install Unsloth on ZGX Nano / DGX Spark (aarch64 + GB10) without building xformers.
#
# Why: `uv sync --extra unsloth` used to depend on the PyPI `unsloth` package, which
# pulls `xformers` — that has no usable aarch64 wheel and fails to compile
# (ValueError in get_extensions). NVIDIA's DGX Spark playbook installs Unsloth with
# `--no-deps` and relies on PyTorch SDPA instead of xformers.
#
# Usage (from repo root):
#   bash scripts/install_unsloth_zgx.sh
#   # optional: also keep the real-matrix stack
#   bash scripts/install_unsloth_zgx.sh --with-real
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

WITH_REAL=0
for arg in "$@"; do
  case "$arg" in
    --with-real) WITH_REAL=1 ;;
    -h|--help)
      sed -n '2,16p' "$0"
      exit 0
      ;;
  esac
done

echo "==> Syncing project + unsloth support deps (no PyPI unsloth / no xformers)"
if [[ "$WITH_REAL" -eq 1 ]]; then
  uv sync --extra real --extra unsloth
else
  uv sync --extra unsloth
fi

echo "==> Ensuring torchvision (required by Qwen3.8 decision load path)"
uv pip install torchvision

echo "==> Installing unsloth + unsloth_zoo with --no-deps (NVIDIA Spark pattern)"
# bitsandbytes is already in the unsloth extra; still include here for parity with NVIDIA docs
uv pip install --no-deps unsloth unsloth_zoo

echo "==> Verifying import (xformers is optional / skipped)"
uv run python - <<'PY'
import importlib.util
import torch

assert torch.cuda.is_available(), "CUDA not available — check nvidia-smi / drivers"
spec = importlib.util.find_spec("unsloth")
assert spec is not None, "unsloth not installed"
import unsloth  # noqa: F401
xf = importlib.util.find_spec("xformers")
print(f"ok: unsloth imported; torch={torch.__version__}; cuda={torch.version.cuda}; xformers={'present' if xf else 'absent (OK — SDPA)'}")
PY

echo
echo "Done. Train with:"
echo "  uv run --extra unsloth python scripts/train_unsloth_score.py ..."
echo "Or (same env after this script):"
echo "  uv run python scripts/train_unsloth_score.py ..."
