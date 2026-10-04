"""Idempotent Kaggle FinAgentBench fetch + convert.

If raw JSONL or harness JSONL is already on disk, skip that step.
Used by `scripts/download_finagentbench_kaggle.py` and `run_benchmark.py --real`.
"""

from __future__ import annotations

import os
import zipfile
from pathlib import Path

from dotenv import load_dotenv

from finagent_mesh.dataset.finagentbench import DatasetError
from finagent_mesh.dataset.kaggle_convert import convert_kaggle_dir
from finagent_mesh.dataset.validate_real import RealRunError, assert_real_dataset

COMPETITION = "acm-icaif-25-ai-agentic-retrieval-grand-challenge"
EXPECTED_RAW = [
    "document_ranking_kaggle_dev.jsonl",
    "document_ranking_kaggle_eval.jsonl",
    "chunk_ranking_kaggle_dev.jsonl",
    "chunk_ranking_kaggle_eval.jsonl",
]


class KaggleFetchError(RuntimeError):
    pass


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def configure_kaggle_auth(*, env_file: Path | None = None) -> None:
    """Load .env and map KGAT_ tokens to KAGGLE_API_TOKEN."""
    root = _repo_root()
    load_dotenv(env_file or (root / ".env"), override=True)
    key = os.getenv("KAGGLE_KEY") or os.getenv("KAGGLE_API_TOKEN")
    username = os.getenv("KAGGLE_USERNAME")
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if key and key.startswith("KGAT_"):
        os.environ["KAGGLE_API_TOKEN"] = key
        token_path = Path.home() / ".kaggle" / "access_token"
        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(key)
        token_path.chmod(0o600)
    if not key and not kaggle_json.exists():
        raise KaggleFetchError(
            "Missing Kaggle credentials. Accept competition rules, then set "
            "KAGGLE_USERNAME + KAGGLE_KEY (or KAGGLE_API_TOKEN) in .env, "
            "or place ~/.kaggle/kaggle.json.\n"
            f"https://www.kaggle.com/competitions/{COMPETITION}/data"
        )
    _ = username  # optional for KGAT tokens


def _archive_wiring_sample(harness_out: Path) -> None:
    sample = harness_out / "sample.jsonl"
    if sample.exists():
        archive = harness_out / "sample.jsonl.wiring-only"
        sample.rename(archive)


def download_kaggle_files(raw_dir: Path, *, force: bool = False) -> list[Path]:
    """Download missing competition JSONL files. Skip files already present."""
    configure_kaggle_auth()
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError as exc:
        raise KaggleFetchError("kaggle package missing; run `uv add kaggle && uv sync`") from exc

    raw_dir.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    print(f"Downloading {COMPETITION} → {raw_dir}", flush=True)
    for name in EXPECTED_RAW:
        dest = raw_dir / name
        if not force and dest.exists() and dest.stat().st_size > 0:
            print(f"skip existing {name} ({dest.stat().st_size / 1e6:.1f} MB)", flush=True)
            continue
        print(f"downloading {name} …", flush=True)
        api.competition_download_file(COMPETITION, name, path=str(raw_dir), force=True, quiet=False)
        zipped = raw_dir / f"{name}.zip"
        if zipped.exists():
            with zipfile.ZipFile(zipped, "r") as zf:
                zf.extractall(raw_dir)
            zipped.unlink()
    missing = [n for n in EXPECTED_RAW if not (raw_dir / n).exists()]
    if missing:
        print(f"Warning: still missing {missing}", flush=True)
    return sorted(raw_dir.glob("*.jsonl"))


def _raw_newer_than_harness(raw_dir: Path, harness_out: Path) -> bool:
    raws = list(raw_dir.glob("*.jsonl"))
    outs = list(harness_out.glob("finagentbench_*.jsonl"))
    if not outs:
        return True
    if not raws:
        return False
    return max(p.stat().st_mtime for p in raws) > max(p.stat().st_mtime for p in outs)


def harness_ready(harness_out: Path, *, min_examples: int = 100) -> bool:
    try:
        assert_real_dataset(harness_out, min_examples=min_examples)
        return True
    except (RealRunError, DatasetError, FileNotFoundError, OSError, ValueError):
        return False


def ensure_local_finagentbench(
    *,
    harness_out: Path,
    raw_dir: Path,
    min_examples: int = 100,
    force_download: bool = False,
    force_convert: bool = False,
    convert: bool = True,
) -> int:
    """Make harness FinAgentBench present locally. Download/convert only if needed.

    Returns example count after ensure (0 if convert=False).
    """
    harness_out = Path(harness_out)
    raw_dir = Path(raw_dir)
    _archive_wiring_sample(harness_out)

    need_download = force_download or any(
        not (raw_dir / name).exists() or (raw_dir / name).stat().st_size == 0
        for name in EXPECTED_RAW
    )
    if need_download:
        download_kaggle_files(raw_dir, force=force_download)
    else:
        print(f"Raw Kaggle JSONL already present under {raw_dir}", flush=True)

    if not convert:
        return 0

    need_convert = (
        force_convert
        or not harness_ready(harness_out, min_examples=min_examples)
        or _raw_newer_than_harness(raw_dir, harness_out)
    )
    if need_convert:
        if not list(raw_dir.glob("*.jsonl")):
            raise KaggleFetchError(f"No Kaggle JSONL in {raw_dir}; cannot convert")
        print(f"Converting {raw_dir} → {harness_out}", flush=True)
        convert_kaggle_dir(raw_dir, harness_out)
    else:
        print(f"Harness dataset already present under {harness_out}", flush=True)

    return assert_real_dataset(harness_out, min_examples=min_examples)
