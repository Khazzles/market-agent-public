# Market Packet — 2026-08-08T06:17:51.955612+08:00

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
| SPY | 2026-08-07 | 773.26 | 0.61 | 3.51 | 2.87 | 3.49 | 10.00 | 65.96 | 1.15 | 0.00 | 2.90 | ABOVE_50_AND_200 |
| QQQ | 2026-08-07 | 723.03 | 1.17 | 5.09 | -0.03 | 1.18 | 11.60 | 57.15 | 2.07 | -2.90 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-07 | 592.10 | 0.37 | 6.36 | -6.24 | -1.28 | -6.21 | 47.67 | 3.92 | -9.10 | -6.20 | BELOW_50_AND_200 |
| AMZN | 2026-08-07 | 274.48 | 0.82 | 1.07 | 11.11 | 10.90 | 16.04 | 64.21 | 3.40 | 8.24 | 11.14 | ABOVE_50_AND_200 |
| MU | 2026-08-07 | 877.57 | -0.44 | 6.63 | -11.50 | -9.62 | 64.03 | 47.63 | 9.46 | -14.37 | -11.47 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-07 | 147.02 | 2.47 | 13.21 | 1.94 | -8.28 | -18.01 | 56.56 | 5.16 | -0.93 | 1.98 | BELOW_50_AND_200 |
| SOFI | 2026-08-07 | 18.38 | 1.55 | 12.69 | -1.29 | 5.40 | -12.81 | 56.51 | 4.81 | -4.16 | -1.25 | MIXED |
| IAU | 2026-08-07 | 81.68 | 2.27 | 7.23 | 5.38 | 4.24 | -3.15 | 65.48 | 1.89 | 2.51 | 5.41 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-07 | 14.90 | -1.65 | -6.82 | -5.93 | -13.75 | BELOW_50_AND_200 |
| ^TNX | 2026-08-07 | 4.66 | -0.21 | -1.79 | 2.67 | 2.65 | ABOVE_50_AND_200 |
| CL=F | 2026-08-07 | 77.08 | -0.27 | -8.96 | 6.94 | -4.19 | BELOW_50_ABOVE_200 |
| GC=F | 2026-08-07 | 4401.30 | 3.76 | 8.70 | 6.55 | 5.53 | MIXED |
| DX-Y.NYB | 2026-08-07 | 99.60 | -0.37 | -0.20 | -1.32 | -0.88 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.76 | XLE, XOP, USO |
| semis_ai | 1.99 | SMH, SOXX |
| high_beta | 3.67 | IWM, ARKK, HIBL |
| rates | -0.21 | TLT, TBF, TBT |
| dollar | -0.43 | UUP |
| equity_hedges | -1.64 | SH, PSQ, SQQQ |
| housing_rates | 2.27 | XHB, ITB |
| defensives | 0.27 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 5.02 | -6.50 | -3.71 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 4.89 | -2.58 | 2.57 | ABOVE_50_AND_200 |
| ITB | housing_rates | 2.71 | 4.39 | 3.65 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 2.02 | -6.61 | -4.10 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.96 | -4.12 | -2.06 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 1.83 | 2.96 | 2.43 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.11 | 1.45 | 2.62 | ABOVE_50_AND_200 |
| XLU | defensives | 0.53 | -3.37 | -2.79 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.36 | -1.84 | -7.03 | BELOW_50_AND_200 |
| XLE | energy | -1.13 | 4.89 | 1.57 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.05 | 0.08 | -1.58 | BELOW_50_AND_200 |
| USO | energy | -0.75 | 8.23 | -2.64 | BELOW_50_ABOVE_200 |
| TBT | rates | -0.66 | 4.21 | 4.45 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.53 | -2.34 | -3.30 | BELOW_50_AND_200 |
| UUP | dollar | -0.43 | -1.02 | -0.57 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.39 | 4.35 | 1.26 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
