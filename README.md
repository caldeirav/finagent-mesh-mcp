# finagent-mesh-mcp

Hybrid financial agent architecture and benchmark harness using LangGraph, open System-1 decision models (CLM-8B, AnyJev, vLLM-sr), Gemini System-2 reasoning, AgentGateway, MCP tooling, and MLflow agentic tracing against FinAgentBench.

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
uv run python main.py   # run in the project environment
uv lock                 # refresh the lockfile when needed
```
