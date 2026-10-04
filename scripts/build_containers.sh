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

cat <<EOF
Build complete.

Suggested serve mapping (NVIDIA Container Toolkit required):
  Stage-1 Choice  -> localhost:8000  (finagent/vllm-sr:arm64 and/or finagent/anyjev:arm64)
  Stage-2 Score   -> localhost:8001  (finagent/clm-8b:arm64)

Example (podman):
  podman run -d --name s1 --device nvidia.com/gpu=all -p 8000:8000 finagent/anyjev:arm64
  podman run -d --name s2 --device nvidia.com/gpu=all -p 8001:8001 finagent/clm-8b:arm64
EOF
