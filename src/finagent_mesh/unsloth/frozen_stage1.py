"""Load frozen Lux Choice Top-1 from paper-n200-full ledger / inspect."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from finagent_mesh.unsloth.types import FrozenStage1Record


def _empty_from_payload(payload: dict[str, Any]) -> bool:
    if payload.get("empty_top1_chunks") is True:
        return True
    if payload.get("error") == "empty_top1_chunks":
        return True
    stage2 = payload.get("stage2") or {}
    if isinstance(stage2, dict) and stage2.get("skipped_reason") == "empty_top1_chunks":
        return True
    return False


def load_frozen_from_ledger(
    ledger_path: Path | str,
    *,
    matrix_run_id: str = "paper-n200-full",
    pair_id: str = "lux-lux",
    source: str | None = None,
) -> dict[str, FrozenStage1Record]:
    """Read ranking_payload_json for ``{matrix_run_id}:{pair_id}``."""
    path = Path(ledger_path)
    run_id = f"{matrix_run_id}:{pair_id}"
    src = source or run_id
    if not path.exists():
        raise FileNotFoundError(f"Eval ledger not found: {path}")
    conn = sqlite3.connect(str(path))
    try:
        cur = conn.execute(
            "SELECT example_id, ranking_payload_json FROM ledger_entries "
            "WHERE run_id = ?",
            (run_id,),
        )
        rows = cur.fetchall()
    finally:
        conn.close()
    out: dict[str, FrozenStage1Record] = {}
    for example_id, payload_json in rows:
        payload: dict[str, Any] = {}
        if payload_json:
            try:
                payload = json.loads(payload_json)
            except (TypeError, ValueError):
                payload = {}
        stage1 = payload.get("stage1") or {}
        ordered = list(stage1.get("ordered_ids") or [])
        scores = [float(x) for x in (stage1.get("scores") or [])]
        top1 = payload.get("top1_doc_type")
        if top1 is None and ordered:
            top1 = ordered[0]
        eid = str(example_id)
        out[eid] = FrozenStage1Record(
            example_id=eid,
            top1_doc_type=str(top1) if top1 is not None else None,
            empty_top1=_empty_from_payload(payload),
            source=src,
            stage1_ordered_ids=[str(x) for x in ordered],
            stage1_scores=scores,
        )
    return out


def load_frozen_from_inspect(
    inspect_path: Path | str,
    *,
    pair_id: str = "lux-lux",
    source: str | None = None,
) -> dict[str, FrozenStage1Record]:
    """Load from ``*.inspect.json`` pair examples (stage1.top1 / error)."""
    path = Path(inspect_path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    src = source or f"inspect:{path.name}:{pair_id}"
    pairs = raw.get("pairs") or []
    target = next((p for p in pairs if p.get("pair_id") == pair_id), None)
    if target is None:
        raise KeyError(f"pair_id={pair_id!r} not found in {path}")
    out: dict[str, FrozenStage1Record] = {}
    for ex in target.get("examples") or []:
        eid = str(ex.get("example_id") or "")
        if not eid:
            continue
        stage1 = ex.get("stage1") or {}
        top1 = stage1.get("top1")
        empty = (
            ex.get("error") == "empty_top1_chunks"
            or (ex.get("stage2") or {}).get("skipped_reason") == "empty_top1_chunks"
        )
        out[eid] = FrozenStage1Record(
            example_id=eid,
            top1_doc_type=str(top1) if top1 is not None else None,
            empty_top1=bool(empty),
            source=src,
            stage1_ordered_ids=list(stage1.get("ordered_ids") or []),
            stage1_scores=[float(x) for x in (stage1.get("scores") or [])],
        )
    return out


def load_frozen_stage1(
    *,
    paper_matrix_id: str = "paper-n200-full",
    pair_id: str = "lux-lux",
    ledger_path: Path | str | None = None,
    inspect_path: Path | str | None = None,
    repo_root: Path | None = None,
) -> dict[str, FrozenStage1Record]:
    """Prefer ledger; fall back to inspect JSON under artifacts/benchmarks."""
    root = repo_root or Path.cwd()
    if ledger_path is not None:
        return load_frozen_from_ledger(
            ledger_path, matrix_run_id=paper_matrix_id, pair_id=pair_id
        )
    if inspect_path is not None:
        return load_frozen_from_inspect(inspect_path, pair_id=pair_id)
    # Defaults
    default_ledger = root / "eval_ledger.db"
    if default_ledger.exists():
        try:
            recs = load_frozen_from_ledger(
                default_ledger, matrix_run_id=paper_matrix_id, pair_id=pair_id
            )
            if recs:
                return recs
        except Exception:
            pass
    inspect = root / "artifacts" / "benchmarks" / f"{paper_matrix_id}.inspect.json"
    if inspect.exists():
        return load_frozen_from_inspect(inspect, pair_id=pair_id)
    raise FileNotFoundError(
        f"Could not load frozen Stage-1 for {paper_matrix_id}:{pair_id}; "
        f"provide ledger_path or inspect_path"
    )
