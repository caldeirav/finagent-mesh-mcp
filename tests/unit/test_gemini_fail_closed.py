"""Fail-closed Gemini: never fabricate extractive answers."""

from __future__ import annotations

import pytest

from finagent_mesh.clients.gemini import GeminiClient, GeminiError


def test_missing_api_key_raises_not_extractive() -> None:
    client = GeminiClient(api_key=None, model="gemini-2.5-flash")
    with pytest.raises(GeminiError, match="fail closed"):
        client.synthesize("What is revenue?", [("c1", "Revenue was $1B last year.")])


def test_empty_api_key_raises() -> None:
    client = GeminiClient(api_key="", model="gemini-2.5-flash")
    with pytest.raises(GeminiError):
        client.synthesize("q", [("c1", "text")])
