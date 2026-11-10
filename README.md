# STONKS

A tiny, dependency-free Python library for portfolio arithmetic. It exists as a
disposable fixture for PWR acceptance testing.

```bash
python -m unittest -q
```

## Functions

* `position_value(shares, price)` — market value of one holding.
* `portfolio_value(holdings, prices)` — total value of `{symbol: shares}` at `{symbol: price}`.
* `percent_change(old, new)` — percentage change from `old` to `new`
  (`percent_change(100, 150)` is `50.0`; `percent_change(200, 150)` is `-25.0`).
* `average_cost(lots)` — share-weighted average cost of `[(shares, price), ...]`.
