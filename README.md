# finagent-mesh-mcp

Hybrid financial agent architecture and benchmark harness using LangGraph, open System-1 decision models (CLM-8B, AnyJev, vLLM-sr), Gemini System-2 reasoning, AgentGateway, MCP tooling, and MLflow agentic tracing against FinAgentBench.

**Active feature**: [`specs/001-finagentbench-harness/`](specs/001-finagentbench-harness/) — plan, contracts, quickstart, and tasks.

**Target hardware**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, 128GB unified memory). Containers build via Podman + `nvidia-container-toolkit` (`scripts/build_containers.sh`).

## Python tooling

This repository uses **[uv](https://docs.astral.sh/uv/)** as the single tool for Python versioning, virtualenvs, and dependencies.

- Python version is pinned in `.python-version` (uv-managed CPython)
- Dependencies live in `pyproject.toml`; the lockfile is `uv.lock`
- Do **not** use pip, poetry, pipenv, conda, or pyenv for this project

```bash
# Install uv: https://docs.astral.sh/uv/getting-started/installation/
uv sync                 # create/update .venv from uv.lock
uv add <package>        # add a runtime dependency
uv add --dev <package>  # add a dev dependency
uv lock                 # refresh the lockfile when needed
```

## Quick start (dev / mock System-1)

```bash
cp .env.example .env
# FINAGENTBENCH_PATH defaults to ./data/finagentbench; SYSTEMONE_MOCK=1 for no GPU engines
uv sync --group dev
uv run pytest -q
uv run python scripts/run_harness.py run --run-id smoke-rank --limit 2 --skip-synthesis
uv run python scripts/run_harness.py status --run-id smoke-rank
uv run python scripts/run_harness.py export-metrics --run-id smoke-rank
```

Full operator validation: [`specs/001-finagentbench-harness/quickstart.md`](specs/001-finagentbench-harness/quickstart.md).

## Layout

- `src/finagent_mesh/` — harness, LangGraph agent, ledger, metrics, clients
- `mcp_servers/` — `mcp-sec-edgar`, `mcp-financial-calculator`
- `containers/` — ARM64 Containerfiles for System-1 engines
- `scripts/run_harness.py` — CLI (`run`, `status`, `export-metrics`)
- `scripts/build_containers.sh` — Podman/docker buildx ARM64 builds
