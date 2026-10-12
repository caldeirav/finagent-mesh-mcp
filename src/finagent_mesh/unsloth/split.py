"""Paper-holdout split builder (test = paper-n200-full selected_example_ids)."""

from __future__ import annotations

import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from finagent_mesh.unsloth.types import DEFAULT_TEST_SOURCE, SplitManifest


class SplitLeakageError(RuntimeError):
    pass


def load_paper_test_ids(paper_matrix_path: Path | str) -> list[str]:
    path = Path(paper_matrix_path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    ids = list(raw.get("selected_example_ids") or [])
    if not ids:
        raise ValueError(f"No selected_example_ids in {path}")
    return [str(x) for x in ids]


def content_hash(
    *,
    test_ids: Iterable[str],
    train_ids: Iterable[str],
    val_ids: Iterable[str],
    test_source: str,
) -> str:
    payload = {
        "test_source": test_source,
        "test_ids": sorted(test_ids),
        "train_ids": sorted(train_ids),
        "val_ids": sorted(val_ids),
    }
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def assert_no_leakage(
    test_ids: list[str],
    train_ids: list[str],
    val_ids: list[str],
) -> dict[str, Any]:
    test, train, val = set(test_ids), set(train_ids), set(val_ids)
    train_overlap = sorted(test & train)
    val_overlap = sorted(test & val)
    train_val_overlap = sorted(train & val)
    report = {
        "paper_test_ids_count": len(test_ids),
        "train_overlap_count": len(train_overlap),
        "val_overlap_count": len(val_overlap),
        "train_val_overlap_count": len(train_val_overlap),
        "train_overlap_ids": train_overlap[:20],
        "val_overlap_ids": val_overlap[:20],
    }
    if train_overlap or val_overlap or train_val_overlap:
        raise SplitLeakageError(
            f"Leakage detected: train∩test={len(train_overlap)} "
            f"val∩test={len(val_overlap)} train∩val={len(train_val_overlap)}"
        )
    return report


def build_split_manifest(
    all_example_ids: list[str],
    *,
    paper_matrix_path: Path | str,
    seed: int = 42,
    val_fraction: float = 0.1,
    manifest_id: str = "fab-paper-test-v1",
    test_source: str = DEFAULT_TEST_SOURCE,
) -> tuple[SplitManifest, dict[str, Any]]:
    test_ids = load_paper_test_ids(paper_matrix_path)
    test_set = set(test_ids)
    if test_source == DEFAULT_TEST_SOURCE and len(test_ids) != 200:
        raise ValueError(
            f"Expected 200 paper test ids from {paper_matrix_path}, got {len(test_ids)}"
        )
    remainder = sorted({str(x) for x in all_example_ids if str(x) not in test_set})
    rng = random.Random(seed)
    shuffled = list(remainder)
    rng.shuffle(shuffled)
    n_val = max(1, int(round(len(shuffled) * val_fraction))) if shuffled else 0
    if n_val >= len(shuffled) and len(shuffled) > 1:
        n_val = max(1, len(shuffled) // 10)
    val_ids = sorted(shuffled[:n_val])
    train_ids = sorted(shuffled[n_val:])
    report = assert_no_leakage(test_ids, train_ids, val_ids)
    ch = content_hash(
        test_ids=test_ids,
        train_ids=train_ids,
        val_ids=val_ids,
        test_source=test_source,
    )
    report["content_hash"] = ch
    report["test_source"] = test_source
    manifest = SplitManifest(
        manifest_id=manifest_id,
        created_at=datetime.now(timezone.utc).isoformat(),
        test_source=test_source,
        test_ids=list(test_ids),
        train_ids=train_ids,
        val_ids=val_ids,
        seed=seed,
        content_hash=ch,
    )
    return manifest, report
