#!/usr/bin/env python3
"""Minimal System-1 sidecar implementing /healthz + /v1/systemone.

Used for local/dev and as the Container CMD until operator-provided GPU weights
replace the scoring backend. Engine identity and family bias differentiate matrix rows.
"""

from __future__ import annotations

import json
import os
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlparse


ENGINE_ID = os.getenv("SYSTEMONE_ENGINE_ID", "anyjev-l0")
MODEL_REVISION = os.getenv("SYSTEMONE_MODEL_REVISION", ENGINE_ID)
FAMILY = os.getenv("SYSTEMONE_FAMILY", "anyjev")
PORT = int(os.getenv("SYSTEMONE_PORT", "8000"))
HOST = os.getenv("SYSTEMONE_HOST", "0.0.0.0")


def _stable_rank(ids: list[str], scores: list[float]) -> list[tuple[str, float, int]]:
    pairs = sorted(zip(ids, scores), key=lambda x: (-x[1], x[0]))
    return [(i, s, r + 1) for r, (i, s) in enumerate(pairs)]


def _score_candidates(
    query: str,
    candidates: list[dict[str, str]],
    *,
    family: str,
    engine_id: str,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    q_tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
    # Family-specific bias so matrix rows are distinguishable without GPU weights.
    family_bias = {
        "anyjev": 0.15 if "l1" in engine_id else 0.10,
        "clm": 0.05,
        "vllm-sr": 0.20 if "lux" in engine_id else 0.12,
        "laya": 0.08,
        "ar-baseline": 0.03,
    }.get(family, 0.0)
    scored: list[tuple[str, float]] = []
    for idx, c in enumerate(candidates):
        cid = c["id"]
        text = (c.get("text") or "").lower()
        tokens = set(re.findall(r"[a-z0-9]+", text))
        overlap = float(len(q_tokens & tokens))
        # Cyclic-shift style perturbation for AnyJev L0
        shift = ((idx + hash(engine_id)) % max(len(candidates), 1)) * 0.01
        temp = 1.0
        if metadata.get("anyjev_mode") == "l1":
            temp = 0.7  # temperature scaling stand-in
        score = (overlap + family_bias + shift + 0.001 * len(text)) / temp
        if family == "clm" or metadata.get("action_cache"):
            score += 0.02 * (1.0 / (1 + idx))
        scored.append((cid, score))

    # Optional AR JSON generation path with injectable parse failure
    if metadata.get("json_choice") or family == "ar-baseline":
        if metadata.get("force_parse_failure"):
            return {
                "primitive": "choice",
                "ranking": [],
                "distribution": {},
                "parse_failure": True,
                "raw_json": "{not-json",
                "engine": ENGINE_ID,
                "model_revision": MODEL_REVISION,
            }
        ordered = [s[0] for s in sorted(scored, key=lambda x: (-x[1], x[0]))]
        scores = [s[1] for s in sorted(scored, key=lambda x: (-x[1], x[0]))]
        payload = {"ordered_ids": ordered, "scores": scores}
        ranked = _stable_rank(ordered, scores)
        total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
        return {
            "primitive": "choice",
            "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
            "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
            "raw_json": json.dumps(payload),
            "engine": ENGINE_ID,
            "model_revision": MODEL_REVISION,
        }

    ids = [s[0] for s in scored]
    scores = [s[1] for s in scored]
    ranked = _stable_rank(ids, scores)
    total = sum(max(s, 0.0) for _, s, _ in ranked) or 1.0
    return {
        "primitive": "choice",
        "ranking": [{"id": i, "score": s, "rank": r} for i, s, r in ranked],
        "distribution": {i: max(s, 0.0) / total for i, s, _ in ranked},
        "engine": ENGINE_ID,
        "model_revision": MODEL_REVISION,
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args: Any) -> None:  # quieter default
        return

    def _send(self, code: int, body: dict[str, Any]) -> None:
        raw = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/healthz":
            self._send(200, {"status": "ok", "engine": ENGINE_ID})
            return
        self._send(404, {"error": "not_found"})

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path != "/v1/systemone":
            self._send(404, {"error": "not_found"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except Exception:  # noqa: BLE001
            self._send(400, {"error": "invalid_json"})
            return
        primitive = payload.get("primitive")
        query = str(payload.get("query") or "")
        candidates = list(payload.get("candidates") or [])
        metadata = dict(payload.get("metadata") or {})
        if not candidates:
            self._send(400, {"error": "candidates_required"})
            return
        if FAMILY == "clm" and primitive not in {"score", "action_cache", "choice"}:
            self._send(400, {"error": f"unsupported_primitive:{primitive}"})
            return
        result = _score_candidates(
            query, candidates, family=FAMILY, engine_id=ENGINE_ID, metadata=metadata
        )
        if primitive:
            result["primitive"] = primitive
        self._send(200, result)


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"systemone_sidecar engine={ENGINE_ID} family={FAMILY} on {HOST}:{PORT}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
