"""Default benchmark path must not import third-party unsloth."""

from __future__ import annotations

import importlib
import sys


def test_finagent_mesh_import_does_not_load_unsloth_third_party():
    # Ensure any prior accidental import is cleared for this check
    sys.modules.pop("unsloth", None)
    importlib.import_module("finagent_mesh")
    importlib.import_module("finagent_mesh.clients.engines.registry")
    assert "unsloth" not in sys.modules


def test_unsloth_package_lazy_no_third_party():
    sys.modules.pop("unsloth", None)
    importlib.import_module("finagent_mesh.unsloth")
    importlib.import_module("finagent_mesh.unsloth.paths")
    importlib.import_module("finagent_mesh.unsloth.split")
    importlib.import_module("finagent_mesh.unsloth.export")
    assert "unsloth" not in sys.modules
