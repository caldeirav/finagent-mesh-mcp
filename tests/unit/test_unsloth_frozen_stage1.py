"""Frozen Lux Choice Stage-1 loader tests."""

from __future__ import annotations

import json
from pathlib import Path

from finagent_mesh.clients.engines.frozen_lux_choice import (
    FrozenLuxChoiceAdapter,
    clear_frozen_stage1_records,
    set_frozen_stage1_records,
)
from finagent_mesh.clients.engines.registry import EngineConfiguration
from finagent_mesh.unsloth.frozen_stage1 import load_frozen_from_inspect
from finagent_mesh.unsloth.types import FrozenStage1Record


def test_load_frozen_from_inspect(tmp_path: Path):
    path = tmp_path / "paper.inspect.json"
    path.write_text(
        json.dumps(
            {
                "pairs": [
                    {
                        "pair_id": "lux-lux",
                        "examples": [
                            {
                                "example_id": "e1",
                                "stage1": {"top1": "10-K", "ordered_ids": ["10-K", "8-K"]},
                                "stage2": {},
                                "error": None,
                            },
                            {
                                "example_id": "e2",
                                "stage1": {"top1": "8-K"},
                                "stage2": {"skipped_reason": "empty_top1_chunks"},
                                "error": "empty_top1_chunks",
                            },
                        ],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    recs = load_frozen_from_inspect(path)
    assert recs["e1"].top1_doc_type == "10-K"
    assert recs["e2"].empty_top1 is True


def test_frozen_adapter_decide():
    set_frozen_stage1_records(
        {
            "e1": FrozenStage1Record(
                example_id="e1",
                top1_doc_type="10-Q",
                empty_top1=False,
                stage1_ordered_ids=["10-Q", "10-K"],
            )
        }
    )
    try:
        ad = FrozenLuxChoiceAdapter(
            EngineConfiguration(
                config_id="frozen-lux-choice",
                family="frozen-choice",
                display_name="f",
                primitives=["choice"],
                primary_stages=["stage1"],
                base_url="http://localhost:8710",
                backend="frozen_lux_choice",
                model_revision="t",
            )
        )
        out = ad.decide(
            "choice",
            "q",
            [{"id": "10-K", "text": "t"}, {"id": "10-Q", "text": "t"}],
            {"example_id": "e1"},
        )
        assert out["ranking"][0]["id"] == "10-Q"
        assert out["frozen_stage1"] is True
    finally:
        clear_frozen_stage1_records()
