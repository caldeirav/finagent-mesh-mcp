"""Decision-2.0 MODEL_MANIFEST repair (no GPU / no Hub)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from finagent_mesh.clients.engines.real_infer import repair_decision20_package


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _hub_layout(tmp: Path, *, wrong_readme: bytes, good_readme: bytes) -> Path:
    """Minimal HF Hub snapshot with a drifted README and a matching blob."""
    root = tmp / "models--vllm-sr--Decision-2.0-Fake"
    snap = root / "snapshots" / "abc123"
    blobs = root / "blobs"
    snap.mkdir(parents=True)
    blobs.mkdir(parents=True)

    good_blob = blobs / "goodreadme"
    good_blob.write_bytes(good_readme)
    bad_blob = blobs / "badreadme"
    bad_blob.write_bytes(wrong_readme)

    (snap / "MODEL_MANIFEST.json").write_text(
        json.dumps(
            {
                "schema": "dev2-package-manifest/1",
                "files_sha256": {"README.md": _sha(good_readme)},
            }
        ),
        encoding="utf-8",
    )
    (snap / "README.md").symlink_to("../../blobs/badreadme")
    return snap


def test_repair_retargets_readme_to_manifest_blob(tmp_path: Path) -> None:
    good = b"---\nlicense: apache-2.0\n---\ncorrect card\n"
    wrong = b"---\npipeline_tag: zero-shot-classification\n---\nwrong card\n"
    snap = _hub_layout(tmp_path, wrong_readme=wrong, good_readme=good)

    assert hashlib.sha256((snap / "README.md").read_bytes()).hexdigest() == _sha(wrong)
    repaired = repair_decision20_package(snap)
    assert repaired == ["README.md"]
    assert hashlib.sha256((snap / "README.md").read_bytes()).hexdigest() == _sha(good)
    # Idempotent.
    assert repair_decision20_package(snap) == []


def test_repair_noop_without_hub_blobs(tmp_path: Path) -> None:
    pkg = tmp_path / "flat-package"
    pkg.mkdir()
    good = b"ok\n"
    (pkg / "MODEL_MANIFEST.json").write_text(
        json.dumps({"files_sha256": {"README.md": _sha(good)}}),
        encoding="utf-8",
    )
    (pkg / "README.md").write_bytes(b"drifted\n")
    assert repair_decision20_package(pkg) == []
