# Market Packet — 2026-07-18T06:29:56.508600+08:00

## Manifest

- AS_OF policy: latest available market close per yfinance.

- Run timezone: Asia/Kuala_Lumpur

- Objective: public research packet only; no portfolio sizes, holdings, cost basis, or private notes.

- Core universe: SPY, QQQ, META, AMZN, MU, ORCL, SOFI, IAU

- Data source: yfinance for market prices and OHLCV-derived indicators.

- Interpretation layer: intended for downstream ChatGPT manager/supervisor review.


## Data Status

No missing ticker metrics detected in this run.


## Core Universe Technical Evidence

| Ticker | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | vs SMA200 % | RSI14 | ATR14 % | RS vs SPY 21D | RS vs QQQ 21D | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 2026-07-17 | 743.29 | -0.99 | -1.54 | -0.94 | -0.15 | 6.69 | 48.42 | 1.14 | 0.00 | 3.79 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-17 | 695.33 | -1.50 | -4.16 | -4.73 | -3.29 | 8.50 | 42.00 | 2.20 | -3.79 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-17 | 646.01 | -2.79 | -3.47 | 7.63 | 6.86 | 0.86 | 56.80 | 4.08 | 8.57 | 12.36 | ABOVE_50_AND_200 |
| AMZN | 2026-07-17 | 247.23 | -1.06 | 0.77 | 0.50 | -1.94 | 5.63 | 51.32 | 3.07 | 1.44 | 5.23 | BELOW_50_ABOVE_200 |
| MU | 2026-07-17 | 848.95 | -0.50 | -13.31 | -16.83 | -9.08 | 75.73 | 41.00 | 10.08 | -15.89 | -12.10 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-17 | 126.41 | 1.77 | -10.12 | -32.88 | -29.25 | -34.00 | 29.26 | 6.70 | -31.94 | -28.15 | BELOW_50_AND_200 |
| SOFI | 2026-07-17 | 17.28 | -0.23 | -7.99 | -2.43 | 1.51 | -20.80 | 46.43 | 5.55 | -1.49 | 2.30 | MIXED |
| IAU | 2026-07-17 | 75.50 | 0.94 | -2.28 | -7.36 | -6.98 | -10.41 | 40.20 | 2.06 | -6.42 | -2.63 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-17 | 18.77 | 12.19 | 24.88 | 14.38 | 8.35 | ABOVE_50_AND_200 |
| ^TNX | 2026-07-17 | 4.54 | -0.61 | -0.61 | 2.55 | 1.05 | ABOVE_50_AND_200 |
| CL=F | 2026-07-17 | 81.77 | 3.57 | 14.51 | 7.52 | -4.21 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-17 | 4023.00 | 0.94 | -1.98 | -7.11 | -6.84 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-17 | 100.75 | 0.02 | -0.21 | 1.22 | 0.82 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.44 | XLE, XOP, USO |
| semis_ai | -1.91 | SMH, SOXX |
| high_beta | -2.20 | IWM, ARKK, HIBL |
| rates | -0.25 | TLT, TBF, TBT |
| dollar | -0.04 | UUP |
| equity_hedges | 2.41 | SH, PSQ, SQQQ |
| housing_rates | -2.58 | XHB, ITB |
| defensives | -0.69 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.65 | 11.58 | 6.20 | MIXED |
| USO | energy | 3.91 | 7.35 | -1.50 | BELOW_50_ABOVE_200 |
| XOP | energy | 2.25 | 8.28 | 3.84 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.53 | 4.04 | 2.66 | MIXED |
| XLE | energy | 1.16 | 4.19 | 2.05 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.06 | 0.27 | -0.11 | BELOW_50_AND_200 |
| TLT | rates | 0.37 | -1.94 | -0.91 | BELOW_50_AND_200 |
| UUP | dollar | -0.04 | 1.43 | 1.14 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -4.17 | -22.25 | -14.68 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -2.85 | -0.95 | 1.82 | MIXED |
| XHB | housing_rates | -2.30 | -1.45 | 2.13 | ABOVE_50_AND_200 |
| SMH | semis_ai | -2.18 | -9.65 | -6.83 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -1.92 | -4.91 | -3.95 | BELOW_50_AND_200 |
| SOXX | semis_ai | -1.64 | -11.74 | -7.87 | BELOW_50_ABOVE_200 |
| TBT | rates | -0.90 | 3.24 | 1.22 | ABOVE_50_AND_200 |
| XLP | defensives | -0.72 | -0.47 | 1.22 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
