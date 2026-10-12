#!/usr/bin/env python3
"""Supervised Unsloth DecisionTrainer Score fine-tune (isolated optional extra).

Resume: pass --resume to continue an interrupted run in --out-dir.
Clean restart: pass --force to overwrite a completed/failed checkpoint dir.
Never writes published paper-* artifacts.

ZGX Nano / DGX Spark install (skip broken xformers):
  bash scripts/install_unsloth_zgx.sh
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from finagent_mesh.unsloth.paths import assert_writable_artifact
from finagent_mesh.unsloth.split import load_paper_test_ids
from finagent_mesh.unsloth.train import assert_split_matches_paper, run_supervised_score_train
from finagent_mesh.unsloth.types import DEFAULT_BASE_MODEL

app = typer.Typer(add_completion=False)


@app.command()
def main(
    dataset_dir: Path = typer.Option(
        Path("artifacts/unsloth/datasets/fab-paper-test-v1"),
        "--dataset-dir",
    ),
    base_model: str = typer.Option(DEFAULT_BASE_MODEL, "--base-model"),
    out_dir: Path = typer.Option(
        Path("artifacts/unsloth/checkpoints/score-qwen38-r16"),
        "--out-dir",
    ),
    run_id: str = typer.Option("unsloth-train-score-001", "--run-id"),
    paper_matrix: Path = typer.Option(
        Path("artifacts/matrix_runs/paper-n200-full.json"),
        "--paper-matrix",
    ),
    max_train_rows: int | None = typer.Option(
        None,
        "--max-train-rows",
        help="Cap expanded per-passage Score decision rows (smoke: 1000).",
    ),
    max_steps: int | None = typer.Option(
        None,
        "--max-steps",
        help="Trainer max_steps override (default scales with --max-train-rows).",
    ),
    seed: int = typer.Option(42, "--seed"),
    force: bool = typer.Option(False, "--force"),
    resume: bool = typer.Option(False, "--resume"),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Persist train_run.json + stub adapter without loading Unsloth/GPU.",
    ),
) -> None:
    assert_writable_artifact(out_dir, purpose="train")
    split = json.loads((dataset_dir / "split_manifest.json").read_text(encoding="utf-8"))
    paper_ids = load_paper_test_ids(paper_matrix)
    try:
        assert_split_matches_paper(split, paper_ids)
    except ValueError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    meta = run_supervised_score_train(
        dataset_dir=dataset_dir,
        out_dir=out_dir,
        train_run_id=run_id,
        base_model=base_model,
        seed=seed,
        max_train_rows=max_train_rows,
        max_steps=max_steps,
        force=force,
        resume=resume,
        dry_run=dry_run,
    )
    typer.echo(f"Train status={meta.status} checkpoint={meta.checkpoint_dir}")
    if meta.status == "failed":
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
