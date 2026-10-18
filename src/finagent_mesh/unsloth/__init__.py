"""Unsloth decision-Score track (optional dependency group).

Importing this package MUST NOT import the third-party ``unsloth`` library.
Heavy train/serve APIs live behind lazy imports in ``train`` / engine adapters.
"""

from __future__ import annotations

__all__ = [
    "assert_writable_artifact",
    "is_published_paper_path",
]
