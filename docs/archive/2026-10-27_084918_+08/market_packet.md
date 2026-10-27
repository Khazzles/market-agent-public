# Market Packet — 2026-10-27T08:49:18.514260+08:00

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
| SPY | 2026-10-23 | 759.97 | -0.52 | -0.43 | -0.94 | -1.02 | 4.53 | 42.09 | 0.96 | 0.00 | 4.01 | BELOW_50_ABOVE_200 |
| QQQ | 2026-10-23 | 704.40 | -0.01 | -0.76 | -4.95 | -2.95 | 4.00 | 36.51 | 1.63 | -4.01 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-23 | 642.62 | -0.96 | -9.40 | -17.36 | -3.19 | 1.60 | 35.73 | 3.99 | -16.42 | -12.41 | BELOW_50_ABOVE_200 |
| AMZN | 2026-10-23 | 248.00 | -0.95 | -0.80 | -0.55 | -2.99 | 1.93 | 43.17 | 2.60 | 0.39 | 4.40 | BELOW_50_ABOVE_200 |
| MU | 2026-10-23 | 877.55 | 2.46 | -0.15 | -18.79 | -10.70 | 19.87 | 38.17 | 5.37 | -17.85 | -13.83 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-23 | 126.16 | 0.49 | -1.61 | -9.59 | -11.71 | -20.43 | 39.13 | 5.07 | -8.65 | -4.64 | BELOW_50_AND_200 |
| SOFI | 2026-10-23 | 14.62 | -1.05 | 0.45 | -13.01 | -12.70 | -19.04 | 38.28 | 4.24 | -12.07 | -8.05 | BELOW_50_AND_200 |
| IAU | 2026-10-23 | 75.15 | -0.67 | -4.07 | -6.41 | -7.08 | -11.46 | 34.06 | 1.54 | -5.47 | -1.46 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-26 | 18.39 | -5.45 | -0.27 | 23.67 | 14.94 | ABOVE_50_AND_200 |
| ^TNX | 2026-10-26 | 4.99 | -0.04 | -2.92 | -3.82 | -0.07 | BELOW_50_ABOVE_200 |
| CL=F | 2026-10-26 | 101.20 | -2.00 | -2.37 | 9.51 | 8.46 | ABOVE_50_AND_200 |
| GC=F | 2026-10-26 | 4023.30 | 0.38 | -3.29 | -6.89 | -7.16 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-26 | 102.02 | 0.21 | 0.04 | 1.04 | 1.43 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 3.12 | XLE, XOP, USO |
| semis_ai | 0.63 | SMH, SOXX |
| high_beta | -0.85 | IWM, ARKK, HIBL |
| rates | 0.40 | TLT, TBF, TBT |
| dollar | 0.21 | UUP |
| equity_hedges | 0.31 | SH, PSQ, SQQQ |
| housing_rates | -0.78 | XHB, ITB |
| defensives | -1.32 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 4.32 | 10.74 | 15.74 | ABOVE_50_AND_200 |
| XLE | energy | 2.60 | 10.75 | 7.76 | ABOVE_50_AND_200 |
| XOP | energy | 2.45 | 9.58 | 6.17 | ABOVE_50_AND_200 |
| TBT | rates | 1.12 | -5.10 | -2.66 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.74 | -12.21 | -8.33 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | 0.62 | 1.55 | 1.03 | MIXED |
| TBF | rates | 0.55 | -2.29 | -1.27 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 0.53 | -15.52 | -10.21 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -2.38 | -30.12 | -25.64 | BELOW_50_AND_200 |
| XLP | defensives | -1.92 | 8.03 | 4.60 | ABOVE_50_AND_200 |
| XHB | housing_rates | -0.83 | 1.63 | -1.03 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.73 | 2.56 | 0.21 | MIXED |
| XLU | defensives | -0.72 | 8.13 | 1.65 | MIXED |
| TLT | rates | -0.49 | 2.42 | 0.97 | MIXED |
| IWM | high_beta | -0.33 | -2.10 | -3.72 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.11 | 5.62 | 2.74 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
