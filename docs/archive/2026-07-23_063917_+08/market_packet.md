# Market Packet — 2026-07-23T06:39:17.571687+08:00

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
| SPY | 2026-07-22 | 747.41 | -0.12 | -0.98 | 0.41 | 0.31 | 7.10 | 51.72 | 1.07 | 0.00 | 4.82 | ABOVE_50_AND_200 |
| QQQ | 2026-07-22 | 705.35 | -0.51 | -1.73 | -4.42 | -1.92 | 9.81 | 46.65 | 2.02 | -4.82 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-22 | 627.17 | -2.58 | -7.95 | 11.23 | 3.48 | -1.88 | 51.52 | 3.95 | 10.82 | 15.65 | MIXED |
| AMZN | 2026-07-22 | 244.85 | -1.09 | -3.97 | 5.18 | -2.30 | 4.43 | 48.40 | 2.90 | 4.77 | 9.60 | BELOW_50_ABOVE_200 |
| MU | 2026-07-22 | 959.48 | -1.17 | 6.10 | -20.79 | 1.17 | 94.07 | 50.18 | 8.63 | -21.20 | -16.38 | ABOVE_50_AND_200 |
| ORCL | 2026-07-22 | 125.84 | -0.95 | -5.02 | -28.12 | -27.87 | -33.46 | 32.42 | 6.26 | -28.53 | -23.70 | BELOW_50_AND_200 |
| SOFI | 2026-07-22 | 17.07 | -3.23 | -4.48 | -0.18 | -0.15 | -21.28 | 45.48 | 5.21 | -0.58 | 4.24 | BELOW_50_AND_200 |
| IAU | 2026-07-22 | 77.69 | 1.13 | 1.85 | -1.41 | -3.43 | -7.88 | 50.05 | 1.90 | -1.81 | 3.01 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-22 | 16.64 | -2.40 | 6.19 | -3.70 | -3.91 | BELOW_50_AND_200 |
| ^TNX | 2026-07-22 | 4.66 | 0.63 | 2.46 | 3.28 | 3.28 | ABOVE_50_AND_200 |
| CL=F | 2026-07-22 | 88.15 | 3.82 | 10.74 | 17.82 | 3.95 | ABOVE_50_AND_200 |
| GC=F | 2026-07-22 | 4131.40 | 1.48 | 2.16 | -1.21 | -3.48 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-22 | 101.14 | -0.04 | 0.64 | 0.12 | 1.02 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.66 | XLE, XOP, USO |
| semis_ai | 0.50 | SMH, SOXX |
| high_beta | -1.39 | IWM, ARKK, HIBL |
| rates | 0.17 | TLT, TBF, TBT |
| dollar | -0.11 | UUP |
| equity_hedges | 0.74 | SH, PSQ, SQQQ |
| housing_rates | 0.73 | XHB, ITB |
| defensives | 1.31 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLU | defensives | 2.25 | 2.71 | 2.35 | ABOVE_50_AND_200 |
| USO | energy | 2.20 | 16.85 | 4.91 | ABOVE_50_AND_200 |
| XOP | energy | 1.59 | 14.00 | 7.49 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.56 | 10.86 | 2.11 | MIXED |
| XLE | energy | 1.20 | 9.51 | 4.48 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.93 | -2.03 | 0.72 | MIXED |
| PSQ | equity_hedges | 0.58 | 3.81 | 1.35 | MIXED |
| ITB | housing_rates | 0.54 | -1.95 | -0.25 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -2.14 | -3.06 | -2.69 | BELOW_50_AND_200 |
| HIBL | high_beta | -1.09 | -24.30 | -8.40 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.93 | -1.47 | 1.00 | ABOVE_50_AND_200 |
| TLT | rates | -0.26 | -3.08 | -2.02 | BELOW_50_AND_200 |
| UUP | dollar | -0.11 | 0.32 | 1.34 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.09 | -0.93 | -0.55 | BELOW_50_AND_200 |
| TBF | rates | 0.28 | 2.66 | 1.90 | ABOVE_50_AND_200 |
| XLP | defensives | 0.38 | 2.68 | 0.23 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
