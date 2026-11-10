"""Portfolio arithmetic. Pure functions, standard library only."""

from __future__ import annotations


def position_value(shares: float, price: float) -> float:
    """Market value of one holding."""
    if shares < 0 or price < 0:
        raise ValueError("shares and price must not be negative")
    return shares * price


def portfolio_value(holdings: dict[str, float], prices: dict[str, float]) -> float:
    """Total market value of ``holdings`` ({symbol: shares}) at ``prices``."""
    total = 0.0
    for symbol, shares in holdings.items():
        if symbol not in prices:
            raise KeyError(f"no price for {symbol}")
        total += position_value(shares, prices[symbol])
    return total


def percent_change(old: float, new: float) -> float:
    """Percentage change from ``old`` to ``new``."""
    if old == 0:
        raise ZeroDivisionError("percent change from zero is undefined")
    return (new - old) / new * 100


def average_cost(lots: list[tuple[float, float]]) -> float:
    """Share-weighted average cost of ``[(shares, price), ...]``."""
    shares = sum(s for s, _ in lots)
    if shares <= 0:
        raise ValueError("at least one share is required")
    return sum(s * p for s, p in lots) / shares
