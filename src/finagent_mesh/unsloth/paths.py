"""Artifact path guards for the Unsloth track (FR-010)."""

from __future__ import annotations

from pathlib import Path

PUBLISHED_PAPER_STEMS = (
    "paper-n200-full",
    "paper-p1-ceilings-n200",
)


class PublishedArtifactWriteError(RuntimeError):
    """Raised when a write would mutate published paper artifacts."""


def is_published_paper_path(path: Path | str) -> bool:
    name = Path(path).name
    for stem in PUBLISHED_PAPER_STEMS:
        if name == stem or name.startswith(f"{stem}."):
            return True
    return False


def assert_writable_artifact(path: Path | str, *, purpose: str = "write") -> Path:
    """Refuse paths that would overwrite published paper stems."""
    p = Path(path)
    if is_published_paper_path(p):
        raise PublishedArtifactWriteError(
            f"Refusing to {purpose} published paper artifact: {p} "
            f"(immutable stems: {', '.join(PUBLISHED_PAPER_STEMS)})"
        )
    # Also refuse matrix_runs / benchmarks children that match stems
    for part in p.parts:
        if is_published_paper_path(part):
            raise PublishedArtifactWriteError(
                f"Refusing to {purpose} path under published paper stem: {p}"
            )
    return p


def assert_unsloth_run_id(run_id: str) -> str:
    rid = (run_id or "").strip()
    if not rid.startswith("unsloth"):
        raise ValueError(
            f"Unsloth eval run_id must start with 'unsloth' (got {run_id!r})"
        )
    if is_published_paper_path(rid):
        raise PublishedArtifactWriteError(
            f"Run id collides with published paper stem: {rid!r}"
        )
    return rid
