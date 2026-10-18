"""Artifact path guards for the Unsloth / yield tracks (FR-010 / 007)."""

from __future__ import annotations

from pathlib import Path

# Immutable published stems — never overwrite via Unsloth or yield CLIs.
PUBLISHED_PAPER_STEMS = (
    "paper-n200-full",
    "paper-p1-ceilings-n200",
)

IMMUTABLE_EVAL_STEMS = (
    *PUBLISHED_PAPER_STEMS,
    "unsloth-score-paper-n200",
)


class PublishedArtifactWriteError(RuntimeError):
    """Raised when a write would mutate published paper / baseline artifacts."""


def is_published_paper_path(path: Path | str) -> bool:
    """True if path name matches an immutable published paper stem."""
    return _matches_immutable_stem(path, PUBLISHED_PAPER_STEMS)


def is_immutable_eval_path(path: Path | str) -> bool:
    """True for paper baselines and published Unsloth N=200 eval stems."""
    return _matches_immutable_stem(path, IMMUTABLE_EVAL_STEMS)


def is_yield_artifact_stem(path: Path | str) -> bool:
    """Yield-recovery run ids / files (writable; never collide with immutables)."""
    name = Path(path).name
    stem = name.split(".")[0] if name else ""
    if stem.startswith("yield-") or "-yield" in stem or stem.endswith("-yield"):
        return True
    return False


def _matches_immutable_stem(path: Path | str, stems: tuple[str, ...]) -> bool:
    name = Path(path).name
    for stem in stems:
        if name == stem or name.startswith(f"{stem}."):
            return True
    return False


def assert_writable_artifact(path: Path | str, *, purpose: str = "write") -> Path:
    """Refuse paths that would overwrite published paper / Unsloth baseline stems.

    Yield stems (`yield-*`, `*-yield*`) are always allowed through the stem check
    (they do not match immutable prefixes).
    """
    p = Path(path)
    if is_yield_artifact_stem(p):
        return p
    if is_immutable_eval_path(p):
        raise PublishedArtifactWriteError(
            f"Refusing to {purpose} immutable eval artifact: {p} "
            f"(immutable stems: {', '.join(IMMUTABLE_EVAL_STEMS)})"
        )
    for part in p.parts:
        if is_immutable_eval_path(part):
            raise PublishedArtifactWriteError(
                f"Refusing to {purpose} path under immutable stem: {p}"
            )
    return p


def assert_unsloth_run_id(run_id: str) -> str:
    rid = (run_id or "").strip()
    if not rid.startswith("unsloth"):
        raise ValueError(
            f"Unsloth eval run_id must start with 'unsloth' (got {run_id!r})"
        )
    if is_immutable_eval_path(rid):
        raise PublishedArtifactWriteError(
            f"Run id collides with immutable eval stem: {rid!r}"
        )
    return rid


def assert_yield_run_id(run_id: str) -> str:
    """Validate yield-recovery run ids (prefix ``yield-``; no immutable collision)."""
    rid = (run_id or "").strip()
    if not rid.startswith("yield-"):
        raise ValueError(
            f"Yield recovery run_id must start with 'yield-' (got {run_id!r})"
        )
    if is_immutable_eval_path(rid):
        raise PublishedArtifactWriteError(
            f"Run id collides with immutable eval stem: {rid!r}"
        )
    return rid
