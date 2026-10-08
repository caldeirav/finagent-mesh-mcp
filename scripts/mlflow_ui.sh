#!/usr/bin/env bash
# Start MLflow UI with repo .env tracking URI (SQLite by default).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

export MLFLOW_DISABLE_AGENT_HINT="${MLFLOW_DISABLE_AGENT_HINT:-1}"
# Keep file-store opt-in for anyone still on ./mlruns
export MLFLOW_ALLOW_FILE_STORE="${MLFLOW_ALLOW_FILE_STORE:-true}"

URI="${MLFLOW_TRACKING_URI:-sqlite:///mlflow.db}"
PORT="${1:-5000}"

echo "MLflow UI  backend=$URI  http://127.0.0.1:${PORT}"
exec uv run mlflow ui --backend-store-uri "$URI" --port "$PORT"
