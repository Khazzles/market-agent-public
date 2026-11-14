# Market Packet — 2026-11-14T09:46:37.651365+08:00

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
| SPY | 2026-11-13 | 754.37 | -0.36 | 2.59 | -2.26 | -1.32 | 3.07 | 47.08 | 1.46 | 0.00 | 4.35 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-13 | 679.89 | -1.20 | 3.63 | -6.61 | -5.29 | -0.34 | 42.81 | 2.40 | -4.35 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-12 | 623.61 | -0.82 | 3.06 | -15.45 | -8.18 | -1.21 | 42.11 | 3.65 | -13.19 | -8.84 | BELOW_50_AND_200 |
| AMZN | 2026-11-13 | 266.66 | -0.29 | 2.84 | 4.67 | 4.65 | 9.02 | 57.43 | 3.41 | 6.93 | 11.28 | ABOVE_50_AND_200 |
| MU | 2026-11-13 | 778.31 | -2.52 | 12.80 | -16.42 | -17.53 | 1.66 | 42.45 | 7.58 | -14.17 | -9.81 | BELOW_50_ABOVE_200 |
| ORCL | 2026-11-13 | 125.35 | -1.38 | 7.97 | -6.78 | -8.28 | -18.66 | 47.11 | 6.43 | -4.53 | -0.17 | BELOW_50_AND_200 |
| SOFI | 2026-11-12 | 15.63 | -3.93 | -2.56 | 9.92 | -3.73 | -10.01 | 45.86 | 5.19 | 12.17 | 16.52 | BELOW_50_AND_200 |
| IAU | 2026-11-13 | 72.88 | 0.12 | -4.58 | -7.12 | -6.68 | -12.92 | 37.86 | 1.94 | -4.87 | -0.52 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-13 | 19.30 | 3.21 | -24.73 | 17.25 | 11.48 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-13 | 5.15 | 1.00 | 6.07 | 1.28 | 1.88 | ABOVE_50_AND_200 |
| CL=F | 2026-11-13 | 88.92 | 0.20 | -2.10 | -9.24 | -6.77 | BELOW_50_ABOVE_200 |
| GC=F | 2026-11-13 | 3887.60 | 0.06 | -4.60 | -6.77 | -7.03 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-13 | 103.41 | 0.23 | 1.09 | 1.38 | 1.97 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.52 | XLE, XOP, USO |
| semis_ai | -3.33 | SMH, SOXX |
| high_beta | -2.65 | IWM, ARKK, HIBL |
| rates | 0.34 | TLT, TBF, TBT |
| dollar | 0.27 | UUP |
| equity_hedges | 1.81 | SH, PSQ, SQQQ |
| housing_rates | 0.50 | XHB, ITB |
| defensives | 0.97 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 3.74 | 17.49 | 12.23 | MIXED |
| XLP | defensives | 1.42 | 6.54 | 7.83 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.28 | 6.73 | 4.98 | MIXED |
| TBT | rates | 1.00 | 1.28 | 1.53 | ABOVE_50_AND_200 |
| XLE | energy | 0.98 | -2.40 | -0.04 | BELOW_50_ABOVE_200 |
| XOP | energy | 0.92 | -5.18 | -2.87 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 0.74 | 6.60 | 3.62 | MIXED |
| XLU | defensives | 0.53 | 5.74 | 5.13 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.12 | -22.60 | -24.21 | BELOW_50_AND_200 |
| SOXX | semis_ai | -3.67 | -12.98 | -13.15 | BELOW_50_AND_200 |
| SMH | semis_ai | -2.99 | -12.90 | -13.05 | BELOW_50_AND_200 |
| ARKK | high_beta | -2.51 | -9.45 | -9.95 | BELOW_50_AND_200 |
| TLT | rates | -0.43 | -0.74 | -1.03 | BELOW_50_AND_200 |
| USO | energy | -0.34 | -7.46 | -4.73 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.32 | 0.89 | -1.15 | BELOW_50_AND_200 |
| ITB | housing_rates | 0.26 | 8.37 | 4.62 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
