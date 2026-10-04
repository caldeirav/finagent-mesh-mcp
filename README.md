# finagent-mesh-mcp

Hybrid financial agent architecture and benchmark harness using LangGraph, open System-1 decision models (CLM-8B, AnyJev, vLLM-sr, Laya, AR baseline), Gemini System-2 reasoning, AgentGateway, MCP tooling, and MLflow agentic tracing against FinAgentBench.

**Active feature**: [`specs/002-decision-model-bench/`](specs/002-decision-model-bench/) — serve real System-1 engines, sequential benchmark matrix, fail-closed Gemini Flash.

Prior harness: [`specs/001-finagentbench-harness/`](specs/001-finagentbench-harness/).

**Target hardware**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, 128GB unified memory). Containers build via Podman + `nvidia-container-toolkit` (`scripts/build_containers.sh`).

## Python tooling

This repository uses **[uv](https://docs.astral.sh/uv/)** as the single tool for Python versioning, virtualenvs, and dependencies.

```bash
uv sync --group dev
```

Optional edge/GPU extras: `uv sync --extra engines` (Transformers for Laya).

## Quick start

```bash
cp .env.example .env
# Set FINAGENTBENCH_PATH, GOOGLE_API_KEY; keep SYSTEMONE_MOCK=0 for official runs

# Local System-1 sidecars (wiring / smoke without GPU weights)
./scripts/serve_engine.sh start anyjev-l0
./scripts/serve_engine.sh start clm-8b
./scripts/serve_engine.sh health anyjev-l0

# Pipeline with per-stage binding + Gemini Flash (fail-closed)
uv run python scripts/run_harness.py run \
  --run-id e2e-20 \
  --stage1-engine anyjev-l0 \
  --stage2-engine clm-8b \
  --sample-size 20 --sample-seed 7 \
  --skip-synthesis   # omit to attempt Gemini synthesis

# Sequential matrix (fixed partners; one variable engine at a time)
uv run python scripts/run_matrix.py run \
  --matrix-run-id matrix-smoke \
  --engines anyjev-l0,clm-8b,laya-modernbert \
  --sample-size 10 --sample-seed 42 \
  --skip-synthesis

uv run python scripts/run_matrix.py export \
  --matrix-run-id matrix-smoke \
  --out ./artifacts/matrix-smoke.json
```

Operator validation: [`specs/002-decision-model-bench/quickstart.md`](specs/002-decision-model-bench/quickstart.md).

AnyJev L1 requires `configs/calibration/anyjev_l1_heldout.json` with **exactly 200** example IDs before `serve_engine.sh start anyjev-l1`.

## Layout

- `src/finagent_mesh/` — harness, LangGraph agent, ledger, metrics, engine adapters, matrix runner
- `configs/engines.yaml` — seven matrix engine configurations + fixed partners
- `containers/` — ARM64 Containerfiles (AnyJev, CLM-8B, vLLM-sr, Laya, AR)
- `scripts/run_harness.py` — pipeline CLI (`--stage1-engine`, `--stage2-engine`, sample flags)
- `scripts/run_matrix.py` — matrix CLI (`run`, `export`, `status`)
- `scripts/serve_engine.sh` — start/stop/health one registry config
- `scripts/build_containers.sh` — Podman/docker buildx ARM64 builds
