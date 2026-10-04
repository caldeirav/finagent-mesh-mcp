#!/usr/bin/env bash
# Install real-model deps and optionally prefetch HuggingFace weights.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Installing real extras (torch, transformers, accelerate)"
uv sync --extra real --group dev

echo "==> Engine model ids (from configs/engines.yaml after env expansion)"
uv run python - <<'PY'
from pathlib import Path
from finagent_mesh.clients.engines.registry import load_registry
reg = load_registry(Path("configs/engines.yaml"))
for eid in reg.all_ids():
    cfg = reg.get(eid)
    print(f"  {eid:28} {cfg.weights_ref}")
PY

PREFETCH="${1:-}"
if [[ "$PREFETCH" == "--prefetch" ]]; then
  echo "==> Prefetching HF weights (large download)"
  uv run python - <<'PY'
from pathlib import Path
from huggingface_hub import snapshot_download
from finagent_mesh.clients.engines.registry import load_registry
reg = load_registry(Path("configs/engines.yaml"))
seen = set()
for eid in reg.all_ids():
    mid = reg.get(eid).weights_ref
    if not mid or mid in seen:
        continue
    seen.add(mid)
    print(f"download {mid}")
    snapshot_download(mid)
print("prefetch complete")
PY
fi

cat <<EOF

Next:
  1. Put Kaggle credentials in .env (KAGGLE_USERNAME / KAGGLE_KEY) if FinAgentBench is not already local
  2. Set SYSTEMONE_MOCK=0 and SYSTEMONE_BACKEND=real in .env
  3. Set GOOGLE_API_KEY for Gemini synthesis
  4. Run (downloads + converts from Kaggle if data/finagentbench is missing):
       uv run python scripts/run_benchmark.py --real --run-id prod-full
     Or a reproducible subset:
       uv run python scripts/run_benchmark.py --real --records 200 --seed 42 --run-id prod-200
EOF
