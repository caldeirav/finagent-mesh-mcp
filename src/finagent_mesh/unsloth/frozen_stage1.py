"""Load frozen Lux Choice Top-1 from paper-n200-full ledger / inspect."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from finagent_mesh.unsloth.types import FrozenStage1Record

# Ledger run_id candidates when the canonical paper matrix stem has no rows
# (e.g. rankings were stored under synth / multi-seed cores / earlier stems).
_LEDGER_RUN_FALLBACKS = (
    "{matrix}:lux-lux",
    "{matrix}-synth:lux-lux",
    "paper-n200:lux-lux",
    "paper-n200-s123-core:lux-lux",
    "paper-n200-s7-core:lux-lux",
)


def _empty_from_payload(payload: dict[str, Any]) -> bool:
    if payload.get("empty_top1_chunks") is True:
        return True
    if payload.get("error") == "empty_top1_chunks":
        return True
    stage2 = payload.get("stage2") or {}
    if isinstance(stage2, dict) and stage2.get("skipped_reason") == "empty_top1_chunks":
        return True
    return False


def _records_from_rows(
    rows: list[tuple[Any, Any]],
    *,
    source: str,
) -> dict[str, FrozenStage1Record]:
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
            source=source,
            stage1_ordered_ids=[str(x) for x in ordered],
            stage1_scores=scores,
        )
    return out


def load_frozen_from_ledger(
    ledger_path: Path | str,
    *,
    matrix_run_id: str = "paper-n200-full",
    pair_id: str = "lux-lux",
    source: str | None = None,
) -> dict[str, FrozenStage1Record]:
    """Read ranking_payload_json for ``{matrix_run_id}:{pair_id}`` (and fallbacks)."""
    path = Path(ledger_path)
    if not path.exists():
        raise FileNotFoundError(f"Eval ledger not found: {path}")

    candidates: list[str] = []
    primary = f"{matrix_run_id}:{pair_id}"
    candidates.append(primary)
    if pair_id == "lux-lux":
        for tmpl in _LEDGER_RUN_FALLBACKS:
            rid = tmpl.format(matrix=matrix_run_id)
            if rid not in candidates:
                candidates.append(rid)

    conn = sqlite3.connect(str(path))
    try:
        for run_id in candidates:
            cur = conn.execute(
                "SELECT example_id, ranking_payload_json FROM ledger_entries "
                "WHERE run_id = ?",
                (run_id,),
            )
            rows = cur.fetchall()
            if rows:
                return _records_from_rows(rows, source=source or run_id)
    finally:
        conn.close()
    return {}


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
    """Load frozen Stage-1; ledger first (with fallbacks), then inspect JSON.

    Raises ``FileNotFoundError`` if no non-empty source is found.
    """
    root = repo_root or Path.cwd()
    tried: list[str] = []

    ledger = Path(ledger_path) if ledger_path is not None else root / "eval_ledger.db"
    if ledger.exists():
        tried.append(str(ledger))
        recs = load_frozen_from_ledger(
            ledger, matrix_run_id=paper_matrix_id, pair_id=pair_id
        )
        if recs:
            return recs

    inspect = (
        Path(inspect_path)
        if inspect_path is not None
        else root / "artifacts" / "benchmarks" / f"{paper_matrix_id}.inspect.json"
    )
    if inspect.exists():
        tried.append(str(inspect))
        recs = load_frozen_from_inspect(inspect, pair_id=pair_id)
        if recs:
            return recs

    raise FileNotFoundError(
        f"Could not load frozen Stage-1 for {paper_matrix_id}:{pair_id} "
        f"(tried: {tried or ['no ledger/inspect paths']}). "
        "Need ledger rows or artifacts/benchmarks/"
        f"{paper_matrix_id}.inspect.json with pair lux-lux."
    )
