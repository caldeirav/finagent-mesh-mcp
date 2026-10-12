#!/usr/bin/env python3
"""Dedicated Unsloth-track eval (frozen Lux Choice + BM25 k=32 → trained Score).

Writes only ``unsloth-*`` artifact stems. Never mutates paper-n200-full* /
paper-p1-ceilings-n200*.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Optional

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from finagent_mesh.clients.engines.frozen_lux_choice import (
    clear_frozen_stage1_records,
    set_frozen_stage1_records,
)
from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth
from finagent_mesh.config import get_settings
from finagent_mesh.dataset.validate_real import RealRunError, assert_real_dataset, assert_real_runtime
from finagent_mesh.matrix.analysis import write_analysis_reports
from finagent_mesh.matrix.inspect import write_inspect_reports
from finagent_mesh.matrix.interpret import write_interpretation_report
from finagent_mesh.matrix.report import write_report
from finagent_mesh.matrix.runner import MatrixRunner
from finagent_mesh.unsloth.frozen_stage1 import load_frozen_stage1
from finagent_mesh.unsloth.paths import (
    PublishedArtifactWriteError,
    assert_unsloth_run_id,
    assert_writable_artifact,
)

app = typer.Typer(add_completion=False)


@app.command()
def main(
    records: Optional[int] = typer.Option(20, "--records", "-n"),
    seed: int = typer.Option(42, "--seed", "-s"),
    pairs: str = typer.Option("lux-unsloth-score", "--pairs", "-p"),
    run_id: str = typer.Option("unsloth-score-smoke20", "--run-id"),
    checkpoint: Optional[Path] = typer.Option(None, "--checkpoint"),
    frozen_stage1_from: str = typer.Option("paper-n200-full", "--frozen-stage1-from"),
    paper_matrix: Path = typer.Option(
        Path("artifacts/matrix_runs/paper-n200-full.json"),
        "--paper-matrix",
    ),
    dataset_path: Optional[Path] = typer.Option(None, "--dataset-path"),
    out_dir: Path = typer.Option(Path("artifacts/benchmarks"), "--out-dir"),
    skip_synthesis: bool = typer.Option(True, "--skip-synthesis/--with-synthesis"),
    real: bool = typer.Option(True, "--real/--allow-mock"),
    ledger_path: Optional[Path] = typer.Option(None, "--ledger-path"),
    inspect_path: Optional[Path] = typer.Option(None, "--inspect-path"),
) -> None:
    try:
        assert_unsloth_run_id(run_id)
        assert_writable_artifact(out_dir / f"{run_id}.json", purpose="eval")
        assert_writable_artifact(
            Path("artifacts/matrix_runs") / f"{run_id}.json", purpose="eval"
        )
    except (ValueError, PublishedArtifactWriteError) as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    if checkpoint:
        os.environ["UNSLOTH_SCORE_CHECKPOINT"] = str(checkpoint.resolve())
    ckpt = os.getenv("UNSLOTH_SCORE_CHECKPOINT", "").strip()
    if not ckpt:
        typer.echo(
            "UNSLOTH_SCORE_CHECKPOINT / --checkpoint required "
            "(fail-closed; no Lux/E5 fallback)",
            err=True,
        )
        raise typer.Exit(code=1)
    if not Path(ckpt).exists():
        typer.echo(f"Checkpoint not found: {ckpt}", err=True)
        raise typer.Exit(code=1)

    settings = get_settings()
    ensure_hf_hub_auth()
    if real:
        os.environ.setdefault("SYSTEMONE_MOCK", "0")
        try:
            assert_real_runtime(
                systemone_mock=settings.systemone_mock, backend="real"
            )
            assert_real_dataset(dataset_path or Path(settings.finagentbench_path))
        except RealRunError as exc:
            typer.echo(str(exc), err=True)
            raise typer.Exit(code=1) from exc

    try:
        frozen = load_frozen_stage1(
            paper_matrix_id=frozen_stage1_from,
            pair_id="lux-lux",
            ledger_path=ledger_path or settings.eval_ledger_path,
            inspect_path=inspect_path,
            repo_root=ROOT,
        )
    except FileNotFoundError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    set_frozen_stage1_records(frozen)
    typer.echo(f"Loaded {len(frozen)} frozen Stage-1 records from {frozen_stage1_from}")

    force_ids: list[str] | None = None
    if paper_matrix.exists() and records == 200 and seed == 42:
        force_ids = list(
            json.loads(paper_matrix.read_text(encoding="utf-8")).get(
                "selected_example_ids"
            )
            or []
        )

    pair_list = [p.strip() for p in pairs.split(",") if p.strip()]
    runner = MatrixRunner(
        settings=settings,
        allow_mock=not real,
        manage_servers=False,  # Unsloth path is in-process; no Lux sidecars
        force_restart=False,
        repo_root=ROOT,
    )
    try:
        matrix = runner.run(
            matrix_run_id=run_id,
            pair_ids=pair_list,
            sample_size=records,
            sample_seed=seed,
            dataset_path=dataset_path,
            skip_synthesis=skip_synthesis,
            selected_example_ids=force_ids,
        )
    finally:
        clear_frozen_stage1_records()

    out_dir.mkdir(parents=True, exist_ok=True)
    write_report(matrix, out_dir)
    write_interpretation_report(matrix, out_dir)
    try:
        write_inspect_reports(matrix, out_dir, ledger_path=settings.eval_ledger_path)
    except Exception as exc:
        typer.echo(f"inspect skipped: {exc}", err=True)
    write_analysis_reports(matrix, out_dir)
    typer.echo(f"Wrote unsloth eval under {out_dir}/{run_id}.*")


if __name__ == "__main__":
    app()
