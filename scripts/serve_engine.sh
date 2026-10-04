#!/usr/bin/env bash
# Start / stop / health one engine config from configs/engines.yaml
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
REGISTRY="${ENGINES_REGISTRY_PATH:-$ROOT/configs/engines.yaml}"
RUNTIME="${PODMAN_OR_DOCKER:-podman}"
# local = process on host; podman = container
MODE="${SYSTEMONE_SERVE_MODE:-local}"
# lexical = fake scores; real = HF / Decision-2.0 / CLM / AR weights
BACKEND="${SYSTEMONE_BACKEND:-lexical}"
PID_DIR="${SYSTEMONE_PID_DIR:-$ROOT/artifacts/engine_pids}"
mkdir -p "$PID_DIR"

usage() {
  echo "Usage: $0 {start|stop|health} <config_id>" >&2
  echo "  SYSTEMONE_BACKEND=real|lexical (default lexical)" >&2
  exit 2
}

[[ $# -ge 2 ]] || usage
ACTION="$1"
CONFIG_ID="$2"

resolve_meta() {
  local validate="$1"
  VALIDATE_CAL="$validate" uv run python - "$CONFIG_ID" "$REGISTRY" "$ROOT" <<'PY'
import json, os, sys
from pathlib import Path
from finagent_mesh.clients.engines.registry import load_registry, validate_calibration

config_id, registry_path, root = sys.argv[1], sys.argv[2], sys.argv[3]
reg = load_registry(Path(registry_path))
cfg = reg.get(config_id)
if os.environ.get("VALIDATE_CAL") == "1" and cfg.calibration_ref:
    validate_calibration(cfg, Path(root))
port = int(cfg.base_url.rsplit(":", 1)[-1])
image = ""
if cfg.container_ref:
    image = f"finagent/{Path(cfg.container_ref).name}:arm64"
print(json.dumps({
  "config_id": cfg.config_id,
  "family": cfg.family,
  "model_revision": cfg.model_revision,
  "base_url": cfg.base_url,
  "health_url": cfg.health_url(),
  "port": port,
  "image": image,
  "weights_ref": cfg.weights_ref,
  "backend": cfg.backend,
}))
PY
}

if [[ "$ACTION" == "start" ]]; then
  META="$(resolve_meta 1)"
else
  META="$(resolve_meta 0)"
fi

PORT="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["port"])' "$META")"
FAMILY="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["family"])' "$META")"
REVISION="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["model_revision"])' "$META")"
HEALTH_URL="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["health_url"])' "$META")"
IMAGE="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["image"])' "$META")"
WEIGHTS="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["weights_ref"])' "$META")"
CFG_BACKEND="$(uv run python -c 'import json,sys; print(json.loads(sys.argv[1])["backend"])' "$META")"
CONTAINER_NAME="finagent-${CONFIG_ID}"
PID_FILE="$PID_DIR/${CONFIG_ID}.pid"

# Prefer explicit SYSTEMONE_BACKEND; else registry backend when real stack requested
EFFECTIVE_BACKEND="$BACKEND"
if [[ "$BACKEND" == "real" ]]; then
  EFFECTIVE_BACKEND="real"
elif [[ "$BACKEND" == "auto" ]]; then
  EFFECTIVE_BACKEND="real"
fi

start_local() {
  if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    # Restart if backend/model changed
    echo "already running $CONFIG_ID pid=$(cat "$PID_FILE")"
    return 0
  fi
  if [[ "$EFFECTIVE_BACKEND" == "real" && -z "$WEIGHTS" ]]; then
    echo "ERROR: real backend needs weights_ref/model id for $CONFIG_ID" >&2
    exit 2
  fi
  SYSTEMONE_ENGINE_ID="$CONFIG_ID" \
  SYSTEMONE_FAMILY="$FAMILY" \
  SYSTEMONE_MODEL_REVISION="$REVISION" \
  SYSTEMONE_PORT="$PORT" \
  SYSTEMONE_BACKEND="$EFFECTIVE_BACKEND" \
  SYSTEMONE_MODEL_ID="$WEIGHTS" \
    uv run python "$ROOT/scripts/systemone_sidecar.py" \
      >"$PID_DIR/${CONFIG_ID}.log" 2>&1 &
  echo $! >"$PID_FILE"
  for _ in $(seq 1 60); do
    if curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
      break
    fi
    sleep 0.5
  done
  echo "started local $CONFIG_ID backend=$EFFECTIVE_BACKEND model=$WEIGHTS port=$PORT pid=$(cat "$PID_FILE")"
}

stop_local() {
  if [[ -f "$PID_FILE" ]]; then
    kill "$(cat "$PID_FILE")" 2>/dev/null || true
    rm -f "$PID_FILE"
  fi
  echo "stopped local $CONFIG_ID"
}

start_podman() {
  if ! command -v "$RUNTIME" >/dev/null 2>&1; then
    echo "$RUNTIME not found; falling back to local" >&2
    start_local
    return
  fi
  "$RUNTIME" rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
  "$RUNTIME" run -d --name "$CONTAINER_NAME" \
    -e SYSTEMONE_ENGINE_ID="$CONFIG_ID" \
    -e SYSTEMONE_FAMILY="$FAMILY" \
    -e SYSTEMONE_MODEL_REVISION="$REVISION" \
    -e SYSTEMONE_PORT="$PORT" \
    -e SYSTEMONE_BACKEND="$EFFECTIVE_BACKEND" \
    -e SYSTEMONE_MODEL_ID="$WEIGHTS" \
    -p "${PORT}:${PORT}" \
    "$IMAGE"
  echo "started container $CONTAINER_NAME backend=$EFFECTIVE_BACKEND"
}

stop_podman() {
  "$RUNTIME" rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
  echo "stopped container $CONTAINER_NAME"
}

do_health() {
  curl -sf "$HEALTH_URL"
  echo
  echo "healthy $CONFIG_ID ($HEALTH_URL)"
}

case "$ACTION" in
  start)
    if [[ "$MODE" == "podman" || "$MODE" == "docker" ]]; then
      start_podman
    else
      start_local
    fi
    ;;
  stop)
    if [[ "$MODE" == "podman" || "$MODE" == "docker" ]]; then
      stop_podman
    else
      stop_local
    fi
    ;;
  health)
    do_health
    ;;
  *)
    usage
    ;;
esac
