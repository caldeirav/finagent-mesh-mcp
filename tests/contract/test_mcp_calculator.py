import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from mcp_servers.mcp_financial_calculator.server import handle_tool


def test_ratio_and_npv():
    ratio = handle_tool(
        "ratio_analysis",
        {"ratio": "current_ratio", "inputs": {"current_assets": 200, "current_liabilities": 100}},
    )
    assert ratio["value"] == 2.0
    npv = handle_tool("compute_npv", {"rate": 0.1, "cashflows": [-100, 60, 60]})
    assert isinstance(npv["npv"], float)
