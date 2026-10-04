#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME="${PODMAN_OR_DOCKER:-podman}"
PLATFORM="linux/arm64"

if ! command -v "$RUNTIME" >/dev/null 2>&1; then
  if command -v docker >/dev/null 2>&1; then
    RUNTIME=docker
  else
    echo "Neither podman nor docker found" >&2
    exit 1
  fi
fi

build_one() {
  local name="$1"
  local dir="$ROOT/containers/$name"
  cp "$ROOT/scripts/systemone_sidecar.py" "$dir/systemone_sidecar.py"
  echo "==> Building $name ($PLATFORM) with $RUNTIME"
  if [[ "$RUNTIME" == "podman" ]]; then
    podman build --platform "$PLATFORM" -f "$dir/Containerfile" -t "finagent/$name:arm64" "$dir"
  else
    docker buildx build --platform "$PLATFORM" -f "$dir/Containerfile" -t "finagent/$name:arm64" --load "$dir"
  fi
}

build_one vllm-sr
build_one anyjev
build_one clm-8b
build_one laya
build_one ar-qwen3-instruct

cat <<EOF
Build complete.

Engine images:
  finagent/anyjev:arm64
  finagent/clm-8b:arm64
  finagent/vllm-sr:arm64
  finagent/laya:arm64
  finagent/ar-qwen3-instruct:arm64

Serve (local sidecar, no GPU required for wiring tests):
  SYSTEMONE_SERVE_MODE=local ./scripts/serve_engine.sh start anyjev-l0
  SYSTEMONE_SERVE_MODE=local ./scripts/serve_engine.sh start clm-8b

Serve (Podman + NVIDIA toolkit):
  SYSTEMONE_SERVE_MODE=podman ./scripts/serve_engine.sh start anyjev-l0
  SYSTEMONE_SERVE_MODE=podman ./scripts/serve_engine.sh start clm-8b

Default ports: Stage-1 Choice :8000, Stage-2 Score :8001 (see configs/engines.yaml).
EOF
