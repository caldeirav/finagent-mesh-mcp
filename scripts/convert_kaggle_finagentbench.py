#!/usr/bin/env python3
"""Convert already-downloaded Kaggle FinAgentBench JSONL into harness format.

If raw files are missing, downloads them first (same path as the download script).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from finagent_mesh.dataset.kaggle_fetch import KaggleFetchError, ensure_local_finagentbench

app = typer.Typer(add_completion=False)


@app.command()
def main(
    raw_dir: Path = typer.Option(Path("data/finagentbench_kaggle"), "--raw-dir"),
    out_dir: Path = typer.Option(Path("data/finagentbench"), "--out-dir"),
    force: bool = typer.Option(False, "--force", help="Re-convert even if outputs exist"),
) -> None:
    os.chdir(ROOT)
    try:
        n = ensure_local_finagentbench(
            harness_out=out_dir,
            raw_dir=raw_dir,
            force_convert=force,
        )
    except KaggleFetchError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(2) from exc
    typer.echo(f"Harness dataset ready: {n} examples → {out_dir}")


if __name__ == "__main__":
    app()
