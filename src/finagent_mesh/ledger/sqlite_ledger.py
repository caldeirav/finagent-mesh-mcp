"""Atomic SQLite evaluation ledger with resume semantics."""

from __future__ import annotations

import json
import os
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

LedgerState = Literal[
    "pending",
    "in_progress",
    "skipped_invalid",
    "failed_retriable",
    "ranking_complete",
    "synthesis_retriable",
    "completed",
]

TERMINAL_NO_RERANK = frozenset({"ranking_complete", "synthesis_retriable", "completed"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class LedgerEntry:
    run_id: str
    example_id: str
    state: LedgerState
    attempts_stage1: int
    attempts_stage2: int
    attempts_synthesis: int
    last_error: str | None
    updated_at: str
    ranking_payload_json: dict[str, Any] | None
    synthesis_payload_json: dict[str, Any] | None


class SqliteLedger:
    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.path, timeout=60)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._init_schema()

    def close(self) -> None:
        self._conn.close()

    def _init_schema(self) -> None:
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS evaluation_runs (
              run_id TEXT PRIMARY KEY,
              created_at TEXT NOT NULL,
              config_json TEXT NOT NULL,
              status TEXT NOT NULL,
              lease_owner TEXT,
              lease_expires_at TEXT
            );
            CREATE TABLE IF NOT EXISTS ledger_entries (
              run_id TEXT NOT NULL,
              example_id TEXT NOT NULL,
              state TEXT NOT NULL,
              attempts_stage1 INTEGER NOT NULL DEFAULT 0,
              attempts_stage2 INTEGER NOT NULL DEFAULT 0,
              attempts_synthesis INTEGER NOT NULL DEFAULT 0,
              last_error TEXT,
              updated_at TEXT NOT NULL,
              ranking_payload_json TEXT,
              synthesis_payload_json TEXT,
              PRIMARY KEY (run_id, example_id)
            );
            """
        )
        self._conn.commit()

    def ensure_run(self, run_id: str, config: dict[str, Any]) -> None:
        cur = self._conn.execute(
            "SELECT run_id FROM evaluation_runs WHERE run_id=?", (run_id,)
        )
        if cur.fetchone() is None:
            self._conn.execute(
                "INSERT INTO evaluation_runs(run_id, created_at, config_json, status) "
                "VALUES (?,?,?,?)",
                (run_id, _utc_now(), json.dumps(config), "running"),
            )
            self._conn.commit()

    def acquire_lease(self, run_id: str, owner: str, ttl_sec: int = 300) -> None:
        now = time.time()
        expires = datetime.fromtimestamp(now + ttl_sec, tz=timezone.utc).isoformat()
        row = self._conn.execute(
            "SELECT lease_owner, lease_expires_at FROM evaluation_runs WHERE run_id=?",
            (run_id,),
        ).fetchone()
        if row is None:
            raise RuntimeError(f"Unknown run_id={run_id}")
        owner_cur, exp = row["lease_owner"], row["lease_expires_at"]
        if owner_cur and owner_cur != owner and exp:
            try:
                exp_ts = datetime.fromisoformat(exp).timestamp()
            except ValueError:
                exp_ts = 0
            if exp_ts > now:
                raise RuntimeError(
                    f"Ledger lease conflict for run_id={run_id}: held by {owner_cur}"
                )
        self._conn.execute(
            "UPDATE evaluation_runs SET lease_owner=?, lease_expires_at=?, status=? "
            "WHERE run_id=?",
            (owner, expires, "running", run_id),
        )
        self._conn.commit()

    def release_lease(self, run_id: str, owner: str) -> None:
        self._conn.execute(
            "UPDATE evaluation_runs SET lease_owner=NULL, lease_expires_at=NULL "
            "WHERE run_id=? AND lease_owner=?",
            (run_id, owner),
        )
        self._conn.commit()

    def ensure_examples(self, run_id: str, example_ids: list[str]) -> None:
        now = _utc_now()
        for eid in example_ids:
            self._conn.execute(
                "INSERT OR IGNORE INTO ledger_entries("
                "run_id, example_id, state, updated_at) VALUES (?,?,?,?)",
                (run_id, eid, "pending", now),
            )
        self._conn.commit()

    def get_entry(self, run_id: str, example_id: str) -> LedgerEntry | None:
        row = self._conn.execute(
            "SELECT * FROM ledger_entries WHERE run_id=? AND example_id=?",
            (run_id, example_id),
        ).fetchone()
        if row is None:
            return None
        return self._row_to_entry(row)

    def _row_to_entry(self, row: sqlite3.Row) -> LedgerEntry:
        return LedgerEntry(
            run_id=row["run_id"],
            example_id=row["example_id"],
            state=row["state"],
            attempts_stage1=row["attempts_stage1"],
            attempts_stage2=row["attempts_stage2"],
            attempts_synthesis=row["attempts_synthesis"],
            last_error=row["last_error"],
            updated_at=row["updated_at"],
            ranking_payload_json=(
                json.loads(row["ranking_payload_json"])
                if row["ranking_payload_json"]
                else None
            ),
            synthesis_payload_json=(
                json.loads(row["synthesis_payload_json"])
                if row["synthesis_payload_json"]
                else None
            ),
        )

    def transition(
        self,
        run_id: str,
        example_id: str,
        state: LedgerState,
        *,
        last_error: str | None = None,
        ranking_payload: dict[str, Any] | None = None,
        synthesis_payload: dict[str, Any] | None = None,
        inc_stage1: bool = False,
        inc_stage2: bool = False,
        inc_synthesis: bool = False,
    ) -> None:
        self._conn.execute("BEGIN IMMEDIATE")
        try:
            row = self._conn.execute(
                "SELECT * FROM ledger_entries WHERE run_id=? AND example_id=?",
                (run_id, example_id),
            ).fetchone()
            if row is None:
                raise RuntimeError(f"Missing ledger entry {run_id}/{example_id}")
            a1 = row["attempts_stage1"] + (1 if inc_stage1 else 0)
            a2 = row["attempts_stage2"] + (1 if inc_stage2 else 0)
            a3 = row["attempts_synthesis"] + (1 if inc_synthesis else 0)
            ranking_json = (
                json.dumps(ranking_payload)
                if ranking_payload is not None
                else row["ranking_payload_json"]
            )
            synth_json = (
                json.dumps(synthesis_payload)
                if synthesis_payload is not None
                else row["synthesis_payload_json"]
            )
            self._conn.execute(
                "UPDATE ledger_entries SET state=?, attempts_stage1=?, attempts_stage2=?, "
                "attempts_synthesis=?, last_error=?, updated_at=?, "
                "ranking_payload_json=?, synthesis_payload_json=? "
                "WHERE run_id=? AND example_id=?",
                (
                    state,
                    a1,
                    a2,
                    a3,
                    last_error,
                    _utc_now(),
                    ranking_json,
                    synth_json,
                    run_id,
                    example_id,
                ),
            )
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

    def status_counts(self, run_id: str) -> dict[str, int]:
        rows = self._conn.execute(
            "SELECT state, COUNT(*) AS c FROM ledger_entries WHERE run_id=? GROUP BY state",
            (run_id,),
        ).fetchall()
        return {r["state"]: r["c"] for r in rows}

    def lease_info(self, run_id: str) -> dict[str, Any]:
        row = self._conn.execute(
            "SELECT status, lease_owner, lease_expires_at FROM evaluation_runs WHERE run_id=?",
            (run_id,),
        ).fetchone()
        if row is None:
            return {}
        return dict(row)

    @staticmethod
    def default_owner() -> str:
        return f"{os.uname().nodename}:{os.getpid()}"
