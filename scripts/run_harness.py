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
    limit: Optional[int] = typer.Option(None, "--limit", help="Max examples (legacy; prefer --sample-size)"),
    dataset_path: Optional[Path] = typer.Option(None, "--dataset-path"),
    synthesis_k: Optional[int] = typer.Option(None, "--synthesis-k"),
    skip_synthesis: bool = typer.Option(False, "--skip-synthesis"),
    stage1_engine: Optional[str] = typer.Option(None, "--stage1-engine"),
    stage2_engine: Optional[str] = typer.Option(None, "--stage2-engine"),
    gemini_model: Optional[str] = typer.Option(None, "--gemini-model"),
    sample_size: Optional[int] = typer.Option(None, "--sample-size"),
    sample_seed: Optional[int] = typer.Option(None, "--sample-seed"),
    allow_mock: bool = typer.Option(False, "--allow-mock"),
) -> None:
    harness = Harness(
        stage1_engine=stage1_engine,
        stage2_engine=stage2_engine,
        gemini_model=gemini_model,
        allow_mock=allow_mock,
    )
    result = harness.run(
        run_id,
        limit=limit,
        dataset_path=dataset_path,
        skip_synthesis=skip_synthesis,
        synthesis_k=synthesis_k,
        sample_size=sample_size,
        sample_seed=sample_seed,
    )
    typer.echo(json.dumps(result, indent=2))


@app.command("export-metrics")
def export_metrics(
    run_id: str = typer.Option(..., "--run-id"),
    out: Optional[Path] = typer.Option(None, "--out"),
) -> None:
    harness = Harness(allow_mock=True)
    payload = harness.export_metrics(run_id, out)
    if out is None:
        typer.echo(json.dumps(payload["summary"], indent=2))
    else:
        typer.echo(f"Wrote {out}")


@app.command()
def status(run_id: str = typer.Option(..., "--run-id")) -> None:
    harness = Harness(allow_mock=True)
    typer.echo(json.dumps(harness.status(run_id), indent=2))


if __name__ == "__main__":
    app()
