"""Ledger seeding for --synthesis-from-rankings (no GPU / Gemini)."""

from __future__ import annotations

from pathlib import Path

from finagent_mesh.ledger.sqlite_ledger import SqliteLedger


def test_seed_rankings_resets_completed_to_ranking_complete(tmp_path: Path) -> None:
    db = tmp_path / "ledger.sqlite"
    ledger = SqliteLedger(db)
    try:
        ledger.ensure_run("src:lux-lux", {"ranking_only": True})
        ledger.ensure_examples("src:lux-lux", ["ex-ok", "ex-empty", "ex-missing"])
        ledger.transition(
            "src:lux-lux",
            "ex-ok",
            "completed",
            ranking_payload={"stage2_ordered_ids": ["c1"], "stage2_chunks": []},
        )
        ledger.transition(
            "src:lux-lux",
            "ex-empty",
            "failed_retriable",
            last_error="empty_top1_chunks",
            ranking_payload={"error": "empty_top1_chunks"},
        )

        counts = ledger.seed_rankings_for_synthesis(
            "src:lux-lux",
            "synth:lux-lux",
            ["ex-ok", "ex-empty", "ex-missing"],
            config={"synthesis": True},
        )
        assert counts["seeded"] == 1
        assert counts["failed_kept"] == 1
        assert counts["missing_source"] == 1

        ok = ledger.get_entry("synth:lux-lux", "ex-ok")
        assert ok is not None
        assert ok.state == "ranking_complete"
        assert ok.synthesis_payload_json is None
        assert ok.ranking_payload_json == {
            "stage2_ordered_ids": ["c1"],
            "stage2_chunks": [],
        }

        empty = ledger.get_entry("synth:lux-lux", "ex-empty")
        assert empty is not None
        assert empty.state == "failed_retriable"
        assert empty.last_error == "empty_top1_chunks"

        # Re-seed must not clobber in-progress / completed dest rows.
        ledger.transition(
            "synth:lux-lux",
            "ex-ok",
            "completed",
            synthesis_payload={"answer": "done"},
        )
        counts2 = ledger.seed_rankings_for_synthesis(
            "src:lux-lux",
            "synth:lux-lux",
            ["ex-ok", "ex-empty"],
            config={"synthesis": True},
        )
        assert counts2["skipped_existing"] == 1
        assert ledger.get_entry("synth:lux-lux", "ex-ok").synthesis_payload_json == {
            "answer": "done"
        }
    finally:
        ledger.close()
