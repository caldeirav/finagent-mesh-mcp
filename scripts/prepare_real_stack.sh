#!/usr/bin/env bash
# Install real-model deps and optionally prefetch HuggingFace weights.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Export .env (HF_TOKEN, weight overrides) before Hub downloads.
if [[ -f "$ROOT/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT/.env"
  set +a
fi

echo "==> Installing real extras (torch, transformers, accelerate)"
uv sync --extra real --group dev

echo "==> Engine model ids (from configs/engines.yaml after env expansion)"
uv run python - <<'PY'
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(".env"))
from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth
from finagent_mesh.clients.engines.registry import load_registry

ensure_hf_hub_auth()
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
from dotenv import load_dotenv
from huggingface_hub import snapshot_download

load_dotenv(Path(".env"))
from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth
from finagent_mesh.clients.engines.registry import load_registry

token = ensure_hf_hub_auth()
reg = load_registry(Path("configs/engines.yaml"))
seen = set()
for eid in reg.all_ids():
    mid = reg.get(eid).weights_ref
    if not mid or mid in seen:
        continue
    seen.add(mid)
    print(f"download {mid}")
    snapshot_download(mid, token=token)
print("download Qwen/Qwen3-8B (CLM encoder)")
snapshot_download("Qwen/Qwen3-8B", token=token)
print("download intfloat/e5-base-v2 (Block B dense IR)")
snapshot_download("intfloat/e5-base-v2", token=token)
print("prefetch complete")
PY
fi

cat <<EOF

Next:
  1. Put HF_TOKEN in .env (https://huggingface.co/settings/tokens) to avoid Hub rate limits
  2. Put Kaggle credentials in .env (KAGGLE_USERNAME / KAGGLE_KEY) if FinAgentBench is not already local
  3. Set SYSTEMONE_MOCK=0 and SYSTEMONE_BACKEND=real in .env
  4. Set GOOGLE_API_KEY for Gemini synthesis (optional; --real is ranking-only by default)
  5. Run Block A/B paper matrix (see README):
       uv run python scripts/run_benchmark.py --real --run-id paper-n200
     AR smoke only:
       uv run python scripts/run_benchmark.py --real --pairs ar-lux --records 10 --seed 42 --run-id ar-smoke
EOF
