#!/usr/bin/env python3
"""CLI for sequential decision-engine benchmark matrix."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from finagent_mesh.matrix.runner import MatrixRunner

app = typer.Typer(help="FinAgent Mesh decision-model benchmark matrix")


@app.command()
def run(
    matrix_run_id: str = typer.Option(..., "--matrix-run-id"),
    engines: Optional[str] = typer.Option(
        None, "--engines", help="Comma-separated config_ids (default: all registry)"
    ),
    sample_size: Optional[int] = typer.Option(None, "--sample-size"),
    sample_seed: Optional[int] = typer.Option(None, "--sample-seed"),
    gemini_model: Optional[str] = typer.Option(None, "--gemini-model"),
    skip_synthesis: bool = typer.Option(False, "--skip-synthesis"),
    allow_mock: bool = typer.Option(False, "--allow-mock"),
    dataset_path: Optional[Path] = typer.Option(None, "--dataset-path"),
    manage_servers: bool = typer.Option(True, "--manage-servers/--no-manage-servers"),
) -> None:
    engine_list = [e.strip() for e in engines.split(",") if e.strip()] if engines else None
    runner = MatrixRunner(allow_mock=allow_mock, manage_servers=manage_servers)
    result = runner.run(
        matrix_run_id,
        engines=engine_list,
        sample_size=sample_size,
        sample_seed=sample_seed,
        gemini_model=gemini_model,
        skip_synthesis=skip_synthesis,
        dataset_path=dataset_path,
    )
    typer.echo(json.dumps({"status": result.status, "rows": len(result.rows)}, indent=2))


@app.command()
def export(
    matrix_run_id: str = typer.Option(..., "--matrix-run-id"),
    out: Optional[Path] = typer.Option(None, "--out"),
    fmt: str = typer.Option("json", "--format", help="json|csv"),
) -> None:
    runner = MatrixRunner(allow_mock=True, manage_servers=False)
    path = runner.export(matrix_run_id, out=out, fmt=fmt)
    typer.echo(f"Wrote {path}")


@app.command()
def status(matrix_run_id: str = typer.Option(..., "--matrix-run-id")) -> None:
    runner = MatrixRunner(allow_mock=True, manage_servers=False)
    typer.echo(json.dumps(runner.status(matrix_run_id), indent=2))


if __name__ == "__main__":
    app()
