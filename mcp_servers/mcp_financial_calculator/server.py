"""Deterministic financial calculator MCP tool handlers."""

from __future__ import annotations

from typing import Any

def compute_irr(cashflows: list[float]) -> dict[str, float]:
    return {"irr": float(_irr_newton(cashflows))}


def _irr_newton(cashflows: list[float], guess: float = 0.1) -> float:
    rate = guess
    for _ in range(100):
        npv = sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows))
        d_npv = sum(-i * cf / ((1 + rate) ** (i + 1)) for i, cf in enumerate(cashflows) if i > 0)
        if abs(d_npv) < 1e-12:
            break
        new_rate = rate - npv / d_npv
        if abs(new_rate - rate) < 1e-10:
            return new_rate
        rate = new_rate
    return rate


def compute_npv(rate: float, cashflows: list[float]) -> dict[str, float]:
    npv = sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows))
    return {"npv": float(npv)}


def amortization_schedule(
    principal: float,
    annual_rate: float,
    periods: int,
    payments_per_year: int = 12,
) -> dict[str, Any]:
    r = annual_rate / payments_per_year
    if r == 0:
        payment = principal / periods
    else:
        payment = principal * (r * (1 + r) ** periods) / ((1 + r) ** periods - 1)
    balance = principal
    schedule = []
    for p in range(1, periods + 1):
        interest = balance * r
        principal_pay = payment - interest
        balance = max(0.0, balance - principal_pay)
        schedule.append(
            {
                "period": p,
                "interest": float(interest),
                "principal": float(principal_pay),
                "balance": float(balance),
            }
        )
    return {"payment": float(payment), "schedule": schedule}


def ratio_analysis(ratio: str, inputs: dict[str, float]) -> dict[str, Any]:
    def req(*keys: str) -> None:
        missing = [k for k in keys if k not in inputs]
        if missing:
            raise ValueError(f"Missing inputs for {ratio}: {missing}")

    if ratio == "current_ratio":
        req("current_assets", "current_liabilities")
        value = inputs["current_assets"] / inputs["current_liabilities"]
    elif ratio == "quick_ratio":
        req("current_assets", "inventory", "current_liabilities")
        value = (inputs["current_assets"] - inputs["inventory"]) / inputs["current_liabilities"]
    elif ratio == "debt_to_equity":
        req("total_liabilities", "equity")
        value = inputs["total_liabilities"] / inputs["equity"]
    elif ratio == "gross_margin":
        req("gross_profit", "revenue")
        value = inputs["gross_profit"] / inputs["revenue"]
    elif ratio == "net_margin":
        req("net_income", "revenue")
        value = inputs["net_income"] / inputs["revenue"]
    elif ratio == "roe":
        req("net_income", "equity")
        value = inputs["net_income"] / inputs["equity"]
    elif ratio == "roa":
        req("net_income", "total_assets")
        value = inputs["net_income"] / inputs["total_assets"]
    else:
        raise ValueError(f"Unsupported ratio: {ratio}")
    return {"ratio": ratio, "value": float(value)}


def handle_tool(tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool == "compute_irr":
        return compute_irr(list(map(float, arguments["cashflows"])))
    if tool == "compute_npv":
        return compute_npv(float(arguments["rate"]), list(map(float, arguments["cashflows"])))
    if tool == "amortization_schedule":
        return amortization_schedule(
            float(arguments["principal"]),
            float(arguments["annual_rate"]),
            int(arguments["periods"]),
            int(arguments.get("payments_per_year", 12)),
        )
    if tool == "ratio_analysis":
        return ratio_analysis(str(arguments["ratio"]), {k: float(v) for k, v in arguments["inputs"].items()})
    raise ValueError(f"Unknown tool {tool}")
