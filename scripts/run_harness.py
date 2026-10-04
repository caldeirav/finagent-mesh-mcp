#!/usr/bin/env python3
"""CLI entrypoint for FinAgentBench evaluation harness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from finagent_mesh.runtime.harness import Harness

app = typer.Typer(help="FinAgent Mesh FinAgentBench harness")


@app.command()
def run(
    run_id: str = typer.Option(..., "--run-id", help="Evaluation run identity"),
    limit: Optional[int] = typer.Option(None, "--limit", help="Max examples"),
    dataset_path: Optional[Path] = typer.Option(None, "--dataset-path"),
    synthesis_k: Optional[int] = typer.Option(None, "--synthesis-k"),
    skip_synthesis: bool = typer.Option(False, "--skip-synthesis"),
) -> None:
    harness = Harness()
    result = harness.run(
        run_id,
        limit=limit,
        dataset_path=dataset_path,
        skip_synthesis=skip_synthesis,
        synthesis_k=synthesis_k,
    )
    typer.echo(json.dumps(result, indent=2))


@app.command("export-metrics")
def export_metrics(
    run_id: str = typer.Option(..., "--run-id"),
    out: Optional[Path] = typer.Option(None, "--out"),
) -> None:
    harness = Harness()
    payload = harness.export_metrics(run_id, out)
    if out is None:
        typer.echo(json.dumps(payload["summary"], indent=2))
    else:
        typer.echo(f"Wrote {out}")


@app.command()
def status(run_id: str = typer.Option(..., "--run-id")) -> None:
    harness = Harness()
    typer.echo(json.dumps(harness.status(run_id), indent=2))


if __name__ == "__main__":
    app()
