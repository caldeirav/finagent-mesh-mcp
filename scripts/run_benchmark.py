#!/usr/bin/env python3
"""One-command FinAgentBench multi-engine decision-model benchmark.

Paper / production (real models + ranking-only default):
  SYSTEMONE_MOCK=0 SYSTEMONE_BACKEND=real \\
    uv run python scripts/run_benchmark.py --real --run-id paper-n200

Smoke:
  ... run_benchmark.py --real --records 10 --seed 42 --run-id paper-smoke-10
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from finagent_mesh.config import get_settings
from finagent_mesh.dataset.validate_real import RealRunError, assert_real_dataset, assert_real_runtime
from finagent_mesh.matrix.analysis import write_analysis_reports
from finagent_mesh.matrix.inspect import build_inspect_payload, write_inspect_reports
from finagent_mesh.matrix.interpret import report_summary_dict, write_interpretation_report
from finagent_mesh.matrix.partners import pairs_from_registry, resolve_matrix_pairs
from finagent_mesh.matrix.report import write_report
from finagent_mesh.matrix.runner import MatrixRunner


def main(
    records: Optional[int] = typer.Option(
        None,
        "--records",
        "-n",
        help="Sample N examples. With --real and omit: default min(200, dataset size).",
    ),
    seed: int = typer.Option(42, "--seed", "-s", help="RNG seed for reproducible sampling."),
    engines: Optional[str] = typer.Option(
        None,
        "--engines",
        "-e",
        help="Legacy ablation: comma-separated engine ids with fixed partners.",
    ),
    pairs: Optional[str] = typer.Option(
        None,
        "--pairs",
        "-p",
        help="Comma-separated matrix pair_ids from configs/engines.yaml.",
    ),
    include_baseline: bool = typer.Option(
        False,
        "--include-baseline",
        help="Legacy: also unlock baseline-role optional pairs when not using --include-optional.",
    ),
    include_optional: bool = typer.Option(
        False,
        "--include-optional",
        help="Include optional Block B rows (lux-clm-shortlist, one-shot-ar).",
    ),
    list_pairs: bool = typer.Option(False, "--list-pairs"),
    run_id: Optional[str] = typer.Option(None, "--run-id"),
    dataset_path: Optional[Path] = typer.Option(None, "--dataset-path"),
    out_dir: Path = typer.Option(Path("artifacts/benchmarks"), "--out-dir"),
    skip_synthesis: bool = typer.Option(
        False,
        "--skip-synthesis",
        help="Ranking-only (skip Gemini). Default under --real.",
    ),
    with_synthesis: bool = typer.Option(
        False,
        "--with-synthesis",
        help="Enable Gemini synthesis + answer scoring (overrides ranking-only default for --real).",
    ),
    gemini_model: Optional[str] = typer.Option(None, "--gemini-model"),
    allow_mock: bool = typer.Option(False, "--allow-mock", help="Debug only."),
    no_manage_servers: bool = typer.Option(False, "--no-manage-servers"),
    force_restart: bool = typer.Option(
        False,
        "--force-restart",
        help="Kill all System-1 sidecars and ports 8000/8001/8002 before the run.",
    ),
    keep_servers: bool = typer.Option(
        False,
        "--keep-servers",
        help="With --real, reuse already-running sidecars instead of a full restart.",
    ),
    list_engines: bool = typer.Option(False, "--list-engines"),
    inspect_from: Optional[str] = typer.Option(
        None,
        "--inspect-from",
        help="Rebuild inspect HTML/JSON from an existing matrix --run-id (no re-run).",
    ),
    analysis_from: Optional[str] = typer.Option(
        None,
        "--analysis-from",
        help="Rebuild analysis MD/JSON from an existing matrix --run-id (no engines).",
    ),
    multi_seed_from: Optional[str] = typer.Option(
        None,
        "--multi-seed-from",
        help="Comma-separated extra matrix run ids to roll into multi-seed summary "
        "(with --analysis-from).",
    ),
    synthesis_from_rankings: Optional[str] = typer.Option(
        None,
        "--synthesis-from-rankings",
        help="Reuse saved Stage-1/2 rankings from this matrix run id; run Gemini only "
        "(no Choice/Score re-inference). Use with --with-synthesis and --run-id.",
    ),
    real: bool = typer.Option(
        False,
        "--real",
        help="Production mode: require real HF models + real FinAgentBench dump.",
    ),
    min_examples: int = typer.Option(
        100,
        "--min-examples",
        help="With --real, minimum labeled examples required in FINAGENTBENCH_PATH.",
    ),
    fetch_data: bool = typer.Option(
        True,
        "--fetch-data/--no-fetch-data",
        help="If FinAgentBench is missing locally, download from Kaggle and convert.",
    ),
) -> None:
    """Run FinAgentBench across open decision models; write JSON/CSV/Markdown reports."""
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.chdir(ROOT)
    settings = get_settings()
    # Prefer authenticated Hub downloads during --real (sidecars also load .env).
    try:
        from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth

        ensure_hf_hub_auth()
    except Exception:  # noqa: BLE001
        pass

    if analysis_from or inspect_from:
        rid = analysis_from or inspect_from
        assert rid is not None
        runner = MatrixRunner(settings, allow_mock=True, manage_servers=False, repo_root=ROOT)
        try:
            matrix = runner.load(rid)
        except FileNotFoundError as exc:
            typer.secho(f"No saved matrix run {rid}: {exc}", fg=typer.colors.RED, err=True)
            raise typer.Exit(2) from exc
        out_dir.mkdir(parents=True, exist_ok=True)
        if inspect_from or analysis_from:
            ins_json, ins_html = write_inspect_reports(
                matrix,
                ledger_path=settings.eval_ledger_path,
                out_json=out_dir / f"{rid}.inspect.json",
                out_html=out_dir / f"{rid}.inspect.html",
                dataset_path=Path(matrix.dataset_path),
            )
            typer.secho(f"Inspect HTML : {ins_html}", fg=typer.colors.GREEN)
            typer.secho(f"Inspect JSON : {ins_json}", fg=typer.colors.GREEN)
        if analysis_from:
            inspect_payload = build_inspect_payload(
                matrix,
                ledger_path=settings.eval_ledger_path,
                dataset_path=Path(matrix.dataset_path),
            )
            multi_mats = []
            if multi_seed_from:
                for mid in [x.strip() for x in multi_seed_from.split(",") if x.strip()]:
                    try:
                        multi_mats.append(runner.load(mid))
                    except FileNotFoundError as exc:
                        typer.secho(f"Missing multi-seed run {mid}: {exc}", fg=typer.colors.YELLOW)
            md_a, js_a = write_analysis_reports(
                matrix,
                out_md=out_dir / f"{rid}.analysis.md",
                out_json=out_dir / f"{rid}.analysis.json",
                inspect_payload=inspect_payload,
                multi_seed_matrices=multi_mats or None,
            )
            typer.secho(f"Analysis MD  : {md_a}", fg=typer.colors.GREEN)
            typer.secho(f"Analysis JSON: {js_a}", fg=typer.colors.GREEN)
        raise typer.Exit(0)

    if synthesis_from_rankings:
        if not with_synthesis:
            typer.secho(
                "--synthesis-from-rankings requires --with-synthesis",
                fg=typer.colors.RED,
                err=True,
            )
            raise typer.Exit(2)
        rid = run_id or f"{synthesis_from_rankings}-synth"
        pair_list = (
            [p.strip() for p in pairs.split(",") if p.strip()]
            if pairs
            else ["anyjev-l0-lux", "lux-lux", "lux-e5", "lux-bm25"]
        )
        runner = MatrixRunner(settings, allow_mock=True, manage_servers=False, repo_root=ROOT)
        try:
            matrix = runner.synthesis_from_rankings(
                synthesis_from_rankings,
                new_run_id=rid,
                pair_ids=pair_list,
                gemini_model=gemini_model,
            )
        except Exception as exc:  # noqa: BLE001
            typer.secho(f"synthesis-from-rankings failed: {exc}", fg=typer.colors.RED, err=True)
            raise typer.Exit(2) from exc
        out_dir.mkdir(parents=True, exist_ok=True)
        write_report(matrix, out_dir / f"{rid}.json", fmt="json")
        write_report(matrix, out_dir / f"{rid}.csv", fmt="csv")
        write_interpretation_report(matrix, out_dir / f"{rid}.md")
        inspect_payload = build_inspect_payload(
            matrix,
            ledger_path=settings.eval_ledger_path,
            dataset_path=Path(matrix.dataset_path),
        )
        write_inspect_reports(
            matrix,
            ledger_path=settings.eval_ledger_path,
            out_json=out_dir / f"{rid}.inspect.json",
            out_html=out_dir / f"{rid}.inspect.html",
            dataset_path=Path(matrix.dataset_path),
        )
        write_analysis_reports(
            matrix,
            out_md=out_dir / f"{rid}.analysis.md",
            out_json=out_dir / f"{rid}.analysis.json",
            inspect_payload=inspect_payload,
        )
        typer.secho(f"Synthesis-reuse matrix saved as {rid}", fg=typer.colors.GREEN)
        raise typer.Exit(0 if matrix.status == "completed" else 1)

    if list_engines or list_pairs:
        from finagent_mesh.clients.engines.registry import load_registry

        reg = load_registry(settings.engines_registry_path)
        if list_engines:
            for eid in reg.all_ids():
                cfg = reg.get(eid)
                typer.echo(
                    f"{eid:28} family={cfg.family:12} backend={cfg.backend:12} "
                    f"model={cfg.weights_ref}"
                )
        default_ids = {
            p.pair_id
            for p in resolve_matrix_pairs(reg, include_optional=False, repo_root=ROOT)
        }
        catalog = pairs_from_registry(reg)
        typer.echo("")
        typer.echo("Matrix pairs (default = optional=false Block A/B):")
        for pair in catalog:
            flag = "default" if pair.pair_id in default_ids else (
                "optional" if pair.optional else pair.role
            )
            blocks = ",".join(pair.blocks) if pair.blocks else "-"
            typer.echo(
                f"  {pair.pair_id:22} blocks=[{blocks:5}] "
                f"S1={pair.stage1_config_id:24} S2={pair.stage2_config_id:24} "
                f"opt={pair.optional} collapsed={pair.collapsed_stages} [{flag}]"
            )
        if reg.deferred_pairs:
            typer.echo("")
            typer.echo("Deferred (not runnable):")
            for d in reg.deferred_pairs:
                typer.echo(f"  {d.get('pair_id'):22} {d.get('issue')}")
        raise typer.Exit(0)

    if real:
        if allow_mock:
            typer.secho(
                "--allow-mock cannot be combined with --real",
                fg=typer.colors.RED,
                err=True,
            )
            raise typer.Exit(2)
        os.environ["SYSTEMONE_BACKEND"] = "real"
        try:
            assert_real_runtime(systemone_mock=settings.systemone_mock, backend="real")
        except RealRunError as exc:
            typer.secho(str(exc), fg=typer.colors.RED, err=True)
            raise typer.Exit(2) from exc

    # Paper defaults: --real → ranking-only unless --with-synthesis
    effective_skip_synthesis = skip_synthesis
    if real and not with_synthesis:
        effective_skip_synthesis = True
    if with_synthesis:
        effective_skip_synthesis = False

    pair_list = [p.strip() for p in (pairs or "").split(",") if p.strip()] or None
    engine_list = [e.strip() for e in (engines or "").split(",") if e.strip()] or None
    if pair_list and engine_list:
        typer.secho("Pass either --pairs or --engines, not both.", fg=typer.colors.RED, err=True)
        raise typer.Exit(2)
    matrix_run_id = run_id or datetime.now(timezone.utc).strftime("bench-%Y%m%d-%H%M%S")
    path = dataset_path or settings.finagentbench_path
    if path is None:
        typer.secho("FINAGENTBENCH_PATH is required.", fg=typer.colors.RED, err=True)
        raise typer.Exit(2)

    sample_n = records
    if real:
        path = Path(path)
        if fetch_data:
            from finagent_mesh.dataset.kaggle_fetch import KaggleFetchError, ensure_local_finagentbench

            raw_dir = ROOT / "data" / "finagentbench_kaggle"
            try:
                n = ensure_local_finagentbench(
                    harness_out=path,
                    raw_dir=raw_dir,
                    min_examples=min_examples,
                )
                typer.echo(f"Real dataset OK: {n} examples at {path}")
            except KaggleFetchError as exc:
                typer.secho(str(exc), fg=typer.colors.RED, err=True)
                raise typer.Exit(2) from exc
            except RealRunError as exc:
                typer.secho(str(exc), fg=typer.colors.RED, err=True)
                raise typer.Exit(2) from exc
        else:
            try:
                n = assert_real_dataset(path, min_examples=min_examples)
                typer.echo(f"Real dataset OK: {n} examples at {path}")
            except RealRunError as exc:
                typer.secho(str(exc), fg=typer.colors.RED, err=True)
                raise typer.Exit(2) from exc
        if sample_n is None:
            sample_n = min(200, n)

    backend = os.getenv("SYSTEMONE_BACKEND", "lexical")
    do_force = bool(force_restart) or (bool(real) and not keep_servers)
    if keep_servers:
        do_force = False

    typer.echo("=== FinAgent Mesh · FinAgentBench multi-engine benchmark ===")
    typer.echo(f"mode       : {'REAL (HF models)' if real or backend == 'real' else 'lexical/wiring'}")
    typer.echo(f"run_id     : {matrix_run_id}")
    typer.echo(f"dataset    : {path}")
    typer.echo(f"records    : {sample_n if sample_n is not None else 'ALL (full dataset)'}")
    typer.echo(f"seed       : {seed if sample_n is not None else 'n/a'}")
    typer.echo(
        f"pairs      : {', '.join(pair_list) if pair_list else ('legacy engines' if engine_list else 'Block A/B default')}"
    )
    if engine_list:
        typer.echo(f"engines    : {', '.join(engine_list)}")
    typer.echo(f"optional   : {'on' if include_optional else 'off'}")
    model = gemini_model or settings.gemini_model
    typer.echo(f"synthesis  : {'off' if effective_skip_synthesis else f'on ({model})'}")
    typer.echo(f"backend    : {backend}")
    typer.echo(f"servers    : {'force-restart' if do_force else 'reuse-if-running'}")
    typer.echo("")

    runner = MatrixRunner(
        settings,
        allow_mock=allow_mock,
        manage_servers=not no_manage_servers,
        force_restart=do_force,
        repo_root=ROOT,
    )

    try:
        matrix = runner.run(
            matrix_run_id,
            engines=engine_list,
            pair_ids=pair_list,
            include_baseline=include_baseline,
            include_optional=include_optional,
            sample_size=sample_n,
            sample_seed=seed if sample_n is not None else None,
            gemini_model=gemini_model,
            skip_synthesis=effective_skip_synthesis,
            dataset_path=Path(path),
        )
    except Exception as exc:  # noqa: BLE001
        typer.secho(f"Benchmark failed: {exc}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1) from exc

    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{matrix_run_id}.json"
    md_path = out_dir / f"{matrix_run_id}.md"
    csv_path = out_dir / f"{matrix_run_id}.csv"
    write_report(matrix, json_path, fmt="json")
    write_report(matrix, csv_path, fmt="csv")
    write_interpretation_report(matrix, md_path)
    ins_json, ins_html = write_inspect_reports(
        matrix,
        ledger_path=settings.eval_ledger_path,
        out_json=out_dir / f"{matrix_run_id}.inspect.json",
        out_html=out_dir / f"{matrix_run_id}.inspect.html",
        dataset_path=Path(path),
    )
    inspect_payload = build_inspect_payload(
        matrix,
        ledger_path=settings.eval_ledger_path,
        dataset_path=Path(path),
    )
    an_md, an_json = write_analysis_reports(
        matrix,
        out_md=out_dir / f"{matrix_run_id}.analysis.md",
        out_json=out_dir / f"{matrix_run_id}.analysis.json",
        inspect_payload=inspect_payload,
    )

    summary = report_summary_dict(matrix)
    typer.echo("")
    typer.echo("=== Summary ===")
    typer.echo(json.dumps(summary, indent=2))
    typer.echo("")
    typer.secho(f"JSON report : {json_path}", fg=typer.colors.GREEN)
    typer.secho(f"CSV report  : {csv_path}", fg=typer.colors.GREEN)
    typer.secho(f"MD report   : {md_path}", fg=typer.colors.GREEN)
    typer.secho(f"Analysis MD : {an_md}", fg=typer.colors.GREEN)
    typer.secho(f"Analysis JSON: {an_json}", fg=typer.colors.GREEN)
    typer.secho(f"Inspect HTML: {ins_html}", fg=typer.colors.GREEN)
    typer.secho(f"Inspect JSON: {ins_json}", fg=typer.colors.GREEN)

    if matrix.status != "completed":
        raise typer.Exit(1)


if __name__ == "__main__":
    typer.run(main)
