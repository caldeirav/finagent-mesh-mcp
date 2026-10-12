"""Supervised Unsloth DecisionTrainer wrappers (lazy Unsloth import).

Resume vs clean restart
-----------------------
- Default: if ``out_dir`` already contains a completed ``train_run.json`` with
  ``status=completed``, refuse to overwrite unless ``--force``.
- Interrupted runs (``status=running`` / missing final checkpoint): pass
  ``resume=True`` to continue from the latest adapter checkpoint when Unsloth
  supports it; otherwise delete the incomplete dir and restart cleanly.
- Never writes published paper artifact paths.

ZGX Nano / DGX Spark install (skip broken xformers)::

    bash scripts/install_unsloth_zgx.sh --with-real
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from finagent_mesh.unsloth.paths import assert_writable_artifact
from finagent_mesh.unsloth.types import DEFAULT_BASE_MODEL, SCORE_CRITERIA, UnslothTrainRun


class UnslothNotInstalledError(RuntimeError):
    pass


def _require_unsloth() -> None:
    try:
        import unsloth  # noqa: F401
    except ImportError as exc:
        raise UnslothNotInstalledError(
            "Unsloth is not installed. On ZGX Nano / DGX Spark run: "
            "bash scripts/install_unsloth_zgx.sh --with-real"
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


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def fab_row_to_decision_rows(row: dict[str, Any]) -> list[dict[str, Any]]:
    """Expand one gold-type FAB export row into Unsloth typed-decision Score rows.

    Unsloth ``build_dataset`` expects::

        {\"state\": str, \"questions\": {name: {type, instructions, criteria}}, \"gold\": {name: label}}

    Score labels are ordinal indices ``0|1|2`` matching ``SCORE_CRITERIA``.
    """
    query = str(row.get("query") or "")
    decision = row.get("decision") or {}
    criteria = list(decision.get("criteria") or SCORE_CRITERIA)
    instructions = str(
        decision.get("instructions")
        or "How relevant is this passage to answering the query?"
    )
    out: list[dict[str, Any]] = []
    for cand in row.get("candidates") or []:
        cid = str(cand.get("id") or "")
        text = str(cand.get("text") or "")
        rel = int(cand.get("relevance", (row.get("labels") or {}).get(cid, 0)))
        rel = max(0, min(2, rel))
        # Keep state compact: query + passage (criteria live on the question)
        state = f"Query: {query}\n\nPassage:\n{text}"
        name = "relevance"
        out.append(
            {
                "example_id": row.get("example_id"),
                "candidate_id": cid,
                "state": state,
                "questions": {
                    name: {
                        "type": "score",
                        "instructions": instructions,
                        "criteria": criteria,
                    }
                },
                "gold": {name: rel},
            }
        )
    return out


def load_decision_rows(
    jsonl_path: Path,
    *,
    max_items: int | None = None,
) -> list[dict[str, Any]]:
    """Stream FAB export JSONL → Unsloth decision rows, optionally capped."""
    items: list[dict[str, Any]] = []
    for row in iter_jsonl(jsonl_path):
        for dec in fab_row_to_decision_rows(row):
            items.append(dec)
            if max_items is not None and len(items) >= max_items:
                return items
    return items


def run_supervised_score_train(
    *,
    dataset_dir: Path,
    out_dir: Path,
    train_run_id: str,
    base_model: str = DEFAULT_BASE_MODEL,
    seed: int = 42,
    max_train_rows: int | None = None,
    max_steps: int | None = None,
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
    # Ensure Hub auth before from_pretrained (Unsloth/transformers read both env names).
    from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth

    ensure_hf_hub_auth()
    from unsloth import (  # type: ignore
        DecisionTrainer,
        FastDecisionModel,
        is_bfloat16_supported,
    )
    from transformers import TrainingArguments

    train_path = Path(dataset_dir) / "train.jsonl"
    val_path = Path(dataset_dir) / "val.jsonl"
    decision_rows = load_decision_rows(train_path, max_items=max_train_rows)
    if not decision_rows:
        raise RuntimeError(f"No Score decision rows produced from {train_path}")

    # Persist converted subset for resume / audit (not the multi-GB FAB export)
    subset_path = out_dir / "train_decision_rows.jsonl"
    assert_writable_artifact(subset_path, purpose="train")
    with subset_path.open("w", encoding="utf-8") as fh:
        for r in decision_rows:
            fh.write(json.dumps(r) + "\n")

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
        use_gradient_checkpointing="unsloth",
        random_state=seed,
    )

    train_items, report = FastDecisionModel.build_dataset(
        decision_rows, tokenizer, model
    )
    if not train_items:
        raise RuntimeError(
            f"build_dataset produced 0 items (skipped={report.get('skipped')}, "
            f"reason={report.get('reason')})"
        )

    eval_items: list | None = None
    if val_path.exists():
        # Small holdout for calibrate; cap to keep smoke fast
        val_cap = min(200, max(1, (max_train_rows or 200) // 5))
        val_rows = load_decision_rows(val_path, max_items=val_cap)
        if val_rows:
            eval_items, _ = FastDecisionModel.build_dataset(val_rows, tokenizer, model)

    # Smoke: few steps; full: ~1 epoch worth of steps when max_train_rows unset
    if max_steps is None:
        if max_train_rows is not None:
            max_steps = min(240, max(30, len(train_items) // 2))
        else:
            max_steps = max(100, min(2000, len(train_items) // 2))

    try:
        trainer = DecisionTrainer(
            model=model,
            processing_class=tokenizer,
            train_dataset=train_items,
            eval_dataset=eval_items,
            args=TrainingArguments(
                per_device_train_batch_size=1,
                gradient_accumulation_steps=4,
                warmup_steps=min(10, max_steps // 4),
                max_steps=int(max_steps),
                learning_rate=2e-5,
                lr_scheduler_type="cosine",
                weight_decay=0.01,
                bf16=is_bfloat16_supported(),
                fp16=not is_bfloat16_supported(),
                logging_steps=1,
                output_dir=str(out_dir / "hf_trainer"),
                report_to="none",
                seed=seed,
                save_steps=max(max_steps, 1),
                eval_strategy="no" if not eval_items else "steps",
                eval_steps=max(max_steps, 1) if eval_items else None,
            ),
        )
        trainer_stats = trainer.train()
        model.save_pretrained(str(out_dir))
        tokenizer.save_pretrained(str(out_dir))

        holdout: dict[str, Any] = {
            "n_fab_decision_rows": len(decision_rows),
            "n_train_items": len(train_items),
            "build_report": {
                k: report.get(k) for k in ("total", "skipped", "truncated", "reason")
            },
            "max_steps": max_steps,
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }
        if hasattr(trainer_stats, "metrics"):
            holdout["trainer_metrics"] = dict(trainer_stats.metrics)
        if eval_items:
            try:
                holdout["calibrate"] = FastDecisionModel.calibrate(
                    model, tokenizer, eval_items
                )
            except Exception as cal_exc:  # noqa: BLE001 — optional post-step
                holdout["calibrate_error"] = str(cal_exc)

        meta.status = "completed"
        meta.holdout_metrics = holdout
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
