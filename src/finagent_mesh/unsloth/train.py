"""Supervised Unsloth DecisionTrainer wrappers (lazy Unsloth import).

Resume vs clean restart
-----------------------
- Default: if ``out_dir`` already contains a completed ``train_run.json`` with
  ``status=completed``, refuse to overwrite unless ``--force``.
- Interrupted runs (``status=running`` / missing final checkpoint): pass
  ``resume=True`` to continue from the latest adapter checkpoint when Unsloth
  supports it; otherwise delete the incomplete dir and restart cleanly.
- Never writes published paper artifact paths.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from finagent_mesh.unsloth.paths import assert_writable_artifact
from finagent_mesh.unsloth.types import DEFAULT_BASE_MODEL, UnslothTrainRun


class UnslothNotInstalledError(RuntimeError):
    pass


def _require_unsloth():
    try:
        import unsloth  # noqa: F401
    except ImportError as exc:
        raise UnslothNotInstalledError(
            "Unsloth is not installed. Run: uv sync --extra unsloth"
        ) from exc


def default_lora_config() -> dict[str, Any]:
    return {
        "r": 16,
        "lora_alpha": 16,
        "lora_dropout": 0.0,
        "max_seq_length": 2048,
        "load_in_4bit": True,
    }


def write_train_run_meta(meta: UnslothTrainRun, out_dir: Path) -> Path:
    assert_writable_artifact(out_dir, purpose="train")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "train_run.json"
    assert_writable_artifact(path, purpose="train")
    path.write_text(json.dumps(meta.to_dict(), indent=2), encoding="utf-8")
    return path


def assert_split_matches_paper(
    split_manifest: dict[str, Any],
    paper_test_ids: list[str],
) -> None:
    test_ids = list(split_manifest.get("test_ids") or [])
    if set(test_ids) != set(paper_test_ids):
        raise ValueError(
            "Split test_ids must equal paper selected_example_ids "
            f"(manifest={len(test_ids)} paper={len(paper_test_ids)})"
        )


def run_supervised_score_train(
    *,
    dataset_dir: Path,
    out_dir: Path,
    train_run_id: str,
    base_model: str = DEFAULT_BASE_MODEL,
    seed: int = 42,
    max_train_rows: int | None = None,
    force: bool = False,
    resume: bool = False,
    dry_run: bool = False,
) -> UnslothTrainRun:
    """Train Score head. ``dry_run=True`` writes metadata only (unit/smoke without GPU)."""
    assert_writable_artifact(out_dir, purpose="train")
    out_dir = Path(out_dir)
    meta_path = out_dir / "train_run.json"
    if meta_path.exists() and not force and not resume:
        existing = json.loads(meta_path.read_text(encoding="utf-8"))
        if existing.get("status") == "completed":
            raise RuntimeError(
                f"Checkpoint dir already completed: {out_dir}. "
                "Pass force=True to overwrite or resume=True to continue."
            )

    split_path = Path(dataset_dir) / "split_manifest.json"
    split = json.loads(split_path.read_text(encoding="utf-8"))
    lora = default_lora_config()
    meta = UnslothTrainRun(
        train_run_id=train_run_id,
        base_model_id=base_model,
        checkpoint_dir=str(out_dir),
        split_manifest_id=str(split.get("manifest_id") or ""),
        lora=lora,
        seed=seed,
        status="running",
        split_content_hash=str(split.get("content_hash") or ""),
    )
    write_train_run_meta(meta, out_dir)

    if dry_run:
        meta.status = "completed"
        meta.holdout_metrics = {"dry_run": True, "max_train_rows": max_train_rows}
        write_train_run_meta(meta, out_dir)
        (out_dir / "adapter_config.json").write_text(
            json.dumps({"dry_run": True, "base_model": base_model}, indent=2),
            encoding="utf-8",
        )
        return meta

    _require_unsloth()
    # Real training path — imported only when Unsloth is installed.
    from unsloth import FastDecisionModel  # type: ignore
    from trl import DecisionTrainer  # type: ignore  # may vary by Unsloth version

    train_file = Path(dataset_dir) / "train.jsonl"
    rows = [
        json.loads(line)
        for line in train_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if max_train_rows is not None:
        rows = rows[: max(0, int(max_train_rows))]

    model, tokenizer = FastDecisionModel.from_pretrained(
        model_name=base_model,
        max_seq_length=int(lora["max_seq_length"]),
        load_in_4bit=bool(lora["load_in_4bit"]),
    )
    model = FastDecisionModel.get_peft_model(
        model,
        r=int(lora["r"]),
        lora_alpha=int(lora["lora_alpha"]),
        lora_dropout=float(lora["lora_dropout"]),
        finetune_vision_layers=False,
    )
    # Dataset formatting is Unsloth-version-specific; keep rows on disk for trainer.
    train_subset = out_dir / "train_subset.jsonl"
    train_subset.write_text(
        "\n".join(json.dumps(r) for r in rows) + ("\n" if rows else ""),
        encoding="utf-8",
    )
    # DecisionTrainer API evolves; call with minimal kwargs and persist whatever succeeds.
    try:
        trainer = DecisionTrainer(
            model=model,
            tokenizer=tokenizer,
            train_dataset=rows,
        )
        trainer.train()
        model.save_pretrained(str(out_dir))
        tokenizer.save_pretrained(str(out_dir))
        meta.status = "completed"
        meta.holdout_metrics = {
            "n_train_rows": len(rows),
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:
        meta.status = "failed"
        meta.holdout_metrics = {"error": str(exc)}
        write_train_run_meta(meta, out_dir)
        raise
    mlflow_id = os.getenv("MLFLOW_RUN_ID")
    if mlflow_id:
        meta.mlflow_run_id = mlflow_id
    write_train_run_meta(meta, out_dir)
    return meta
