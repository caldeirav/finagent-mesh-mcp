"""Gates for production / real FinAgentBench + real-model runs."""

from __future__ import annotations

from pathlib import Path

from finagent_mesh.dataset.finagentbench import DatasetError, load_examples


class RealRunError(RuntimeError):
    pass


def assert_real_dataset(path: Path, *, min_examples: int = 100) -> int:
    """Require a real FinAgentBench dump (not the 2-example wiring sample)."""
    if not path.exists():
        raise RealRunError(
            f"FINAGENTBENCH_PATH not found: {path}. "
            "Place the official FinAgentBench dump (JSON/JSONL with stage1_labels, "
            "stage2_labels, chunks) and point FINAGENTBENCH_PATH at it, or run "
            "`uv run python scripts/run_benchmark.py --real` (auto-downloads from Kaggle)."
        )
    try:
        examples = load_examples(path)
    except DatasetError as exc:
        raise RealRunError(str(exc)) from exc
    n = len(examples)
    # Detect the repo wiring sample
    sample_only = path.name == "finagentbench" and n <= 5
    if sample_only or n < min_examples:
        raise RealRunError(
            f"Dataset at {path} has only {n} example(s). Real runs require the full "
            f"FinAgentBench dump (≥{min_examples} labeled examples with stage1_labels / "
            "stage2_labels / chunks). The repo `data/finagentbench/sample.jsonl` is for "
            "wiring only — replace FINAGENTBENCH_PATH with your official dataset root."
        )
    missing_stage = sum(1 for e in examples if not e.stage1_labels and not e.stage2_labels)
    if missing_stage == n:
        raise RealRunError(
            f"Dataset at {path} has no stage1_labels/stage2_labels — not a FinAgentBench "
            "ranking dump in the harness schema."
        )
    return n


def assert_real_runtime(*, systemone_mock: bool, backend: str) -> None:
    if systemone_mock:
        raise RealRunError(
            "SYSTEMONE_MOCK=1 is set. Real model runs require SYSTEMONE_MOCK=0 in .env."
        )
    if backend not in {"real", "auto"}:
        raise RealRunError(
            f"SYSTEMONE_BACKEND={backend!r}. Real model runs require "
            "SYSTEMONE_BACKEND=real (and `uv sync --extra real`)."
        )
