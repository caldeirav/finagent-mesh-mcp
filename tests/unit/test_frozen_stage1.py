"""Frozen Lux Choice Stage-1 loader (ledger fallbacks + inspect)."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest

from finagent_mesh.unsloth.frozen_stage1 import (
    load_frozen_from_inspect,
    load_frozen_from_ledger,
    load_frozen_stage1,
)


def _make_ledger(path: Path, run_id: str, example_ids: list[str]) -> None:
    conn = sqlite3.connect(str(path))
    try:
        conn.execute(
            "CREATE TABLE ledger_entries ("
            "run_id TEXT, example_id TEXT, ranking_payload_json TEXT)"
        )
        for eid in example_ids:
            payload = {
                "stage1": {
                    "ordered_ids": [f"type-{eid}", "other"],
                    "scores": [0.9, 0.1],
                },
                "top1_doc_type": f"type-{eid}",
            }
            conn.execute(
                "INSERT INTO ledger_entries VALUES (?, ?, ?)",
                (run_id, eid, json.dumps(payload)),
            )
        conn.commit()
    finally:
        conn.close()


def test_ledger_fallback_to_synth(tmp_path: Path) -> None:
    db = tmp_path / "eval_ledger.db"
    # Canonical stem empty; synth has rows.
    _make_ledger(db, "paper-n200-full-synth:lux-lux", ["dev:q1", "dev:q2"])
    recs = load_frozen_from_ledger(db, matrix_run_id="paper-n200-full")
    assert set(recs) == {"dev:q1", "dev:q2"}
    assert recs["dev:q1"].top1_doc_type == "type-dev:q1"
    assert recs["dev:q1"].source == "paper-n200-full-synth:lux-lux"


def test_load_frozen_stage1_falls_back_to_inspect(tmp_path: Path) -> None:
    # Empty ledger for primary; inspect has lux-lux.
    db = tmp_path / "eval_ledger.db"
    _make_ledger(db, "other:lux-lux", ["dev:q9"])
    inspect = tmp_path / "paper-n200-full.inspect.json"
    inspect.write_text(
        json.dumps(
            {
                "pairs": [
                    {
                        "pair_id": "lux-lux",
                        "examples": [
                            {
                                "example_id": "dev:qa",
                                "stage1": {
                                    "top1": "10-K",
                                    "ordered_ids": ["10-K"],
                                    "scores": [1.0],
                                },
                            },
                            {
                                "example_id": "dev:qb",
                                "error": "empty_top1_chunks",
                                "stage1": {"top1": None},
                                "stage2": {"skipped_reason": "empty_top1_chunks"},
                            },
                        ],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    recs = load_frozen_stage1(
        paper_matrix_id="paper-n200-full",
        ledger_path=db,
        inspect_path=inspect,
        repo_root=tmp_path,
    )
    assert len(recs) == 2
    assert recs["dev:qa"].top1_doc_type == "10-K"
    assert recs["dev:qb"].empty_top1 is True


def test_load_frozen_stage1_raises_when_empty(tmp_path: Path) -> None:
    db = tmp_path / "eval_ledger.db"
    _make_ledger(db, "unrelated:lux-lux", ["dev:qx"])
    with pytest.raises(FileNotFoundError, match="Could not load frozen Stage-1"):
        load_frozen_stage1(
            paper_matrix_id="paper-n200-full",
            ledger_path=db,
            inspect_path=tmp_path / "missing.inspect.json",
            repo_root=tmp_path,
        )


def test_inspect_loader_pair_missing(tmp_path: Path) -> None:
    p = tmp_path / "x.inspect.json"
    p.write_text(json.dumps({"pairs": [{"pair_id": "lux-e5", "examples": []}]}))
    with pytest.raises(KeyError, match="lux-lux"):
        load_frozen_from_inspect(p, pair_id="lux-lux")
