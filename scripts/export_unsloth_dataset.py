#!/usr/bin/env python3
"""Export FinAgentBench gold-type Score rows + leakage-safe paper holdout split."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from finagent_mesh.dataset.finagentbench import load_examples
from finagent_mesh.unsloth.export import export_score_rows
from finagent_mesh.unsloth.paths import assert_writable_artifact
from finagent_mesh.unsloth.split import SplitLeakageError, build_split_manifest, load_paper_test_ids

app = typer.Typer(add_completion=False)


@app.command()
def main(
    dataset_path: Path = typer.Option(Path("data/finagentbench"), "--dataset-path"),
    paper_matrix: Path = typer.Option(
        Path("artifacts/matrix_runs/paper-n200-full.json"),
        "--paper-matrix",
    ),
    out_dir: Path = typer.Option(
        Path("artifacts/unsloth/datasets/fab-paper-test-v1"),
        "--out-dir",
    ),
    seed: int = typer.Option(42, "--seed"),
    val_fraction: float = typer.Option(0.1, "--val-fraction"),
    max_candidates: int | None = typer.Option(None, "--max-candidates"),
    max_text_chars: int = typer.Option(4000, "--max-text-chars"),
) -> None:
    assert_writable_artifact(out_dir, purpose="export")
    out_dir.mkdir(parents=True, exist_ok=True)
    examples = load_examples(dataset_path)
    all_ids = [ex.example_id for ex in examples]
    try:
        manifest, leakage = build_split_manifest(
            all_ids,
            paper_matrix_path=paper_matrix,
            seed=seed,
            val_fraction=val_fraction,
        )
    except SplitLeakageError as exc:
        typer.echo(f"LEAKAGE FAIL: {exc}", err=True)
        raise typer.Exit(code=1) from exc

    paper_ids = load_paper_test_ids(paper_matrix)
    if set(manifest.test_ids) != set(paper_ids):
        typer.echo("test_ids != paper selected_example_ids", err=True)
        raise typer.Exit(code=1)

    train_rows, train_stats = export_score_rows(
        examples,
        allowed_ids=set(manifest.train_ids),
        max_candidates=max_candidates,
        max_text_chars=max_text_chars,
    )
    val_rows, val_stats = export_score_rows(
        examples,
        allowed_ids=set(manifest.val_ids),
        max_candidates=max_candidates,
        max_text_chars=max_text_chars,
    )

    def _write_jsonl(path: Path, rows: list[dict]) -> None:
        assert_writable_artifact(path, purpose="export")
        path.write_text(
            "\n".join(json.dumps(r) for r in rows) + ("\n" if rows else ""),
            encoding="utf-8",
        )

    split_path = out_dir / "split_manifest.json"
    assert_writable_artifact(split_path, purpose="export")
    split_path.write_text(json.dumps(manifest.to_dict(), indent=2), encoding="utf-8")
    (out_dir / "train_ids.json").write_text(
        json.dumps(manifest.train_ids, indent=2), encoding="utf-8"
    )
    (out_dir / "val_ids.json").write_text(
        json.dumps(manifest.val_ids, indent=2), encoding="utf-8"
    )
    (out_dir / "test_ids.json").write_text(
        json.dumps(manifest.test_ids, indent=2), encoding="utf-8"
    )
    _write_jsonl(out_dir / "train.jsonl", train_rows)
    _write_jsonl(out_dir / "val.jsonl", val_rows)

    leakage.update(
        {
            "content_hash": manifest.content_hash,
            "train_export": train_stats,
            "val_export": val_stats,
            "max_candidates": max_candidates,
            "max_text_chars": max_text_chars,
        }
    )
    leak_path = out_dir / "leakage_report.json"
    assert_writable_artifact(leak_path, purpose="export")
    leak_path.write_text(json.dumps(leakage, indent=2), encoding="utf-8")

    if leakage["train_overlap_count"] or leakage["val_overlap_count"]:
        typer.echo("LEAKAGE FAIL after export", err=True)
        raise typer.Exit(code=1)

    typer.echo(
        f"Wrote {out_dir}: n_train={manifest.n_train} n_val={manifest.n_val} "
        f"n_test={manifest.n_test} train_rows={len(train_rows)} val_rows={len(val_rows)}"
    )


if __name__ == "__main__":
    app()
