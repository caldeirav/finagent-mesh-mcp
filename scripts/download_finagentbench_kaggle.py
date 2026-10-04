#!/usr/bin/env python3
"""Download + convert FinAgentBench from Kaggle if it is not already local.

Idempotent: existing JSONL files are skipped; harness convert runs only when
raw files are new or the harness dump is missing/too small.

https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/data
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
    out_dir: Path = typer.Option(
        Path("data/finagentbench_kaggle"),
        "--out-dir",
        help="Directory for raw Kaggle JSONL files",
    ),
    convert: bool = typer.Option(
        True,
        "--convert/--no-convert",
        help="Convert into harness JSONL under --harness-out",
    ),
    harness_out: Path = typer.Option(
        Path("data/finagentbench"),
        "--harness-out",
        help="Harness-ready output directory",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Re-download files even if they already exist",
    ),
    force_convert: bool = typer.Option(
        False,
        "--force-convert",
        help="Re-run conversion even if harness JSONL looks up to date",
    ),
) -> None:
    os.chdir(ROOT)
    try:
        n = ensure_local_finagentbench(
            harness_out=harness_out,
            raw_dir=out_dir,
            force_download=force,
            force_convert=force_convert,
            convert=convert,
        )
    except KaggleFetchError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(2) from exc
    except Exception as exc:  # noqa: BLE001
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(1) from exc

    if convert:
        typer.secho(f"FinAgentBench ready: {n} examples at {harness_out}", fg=typer.colors.GREEN)
        typer.echo(
            f"\nSet FINAGENTBENCH_PATH={harness_out.resolve()} then:\n"
            "  uv run python scripts/run_benchmark.py --real --run-id prod-kaggle\n"
        )
    else:
        typer.secho(f"Raw Kaggle JSONL ready under {out_dir}", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
