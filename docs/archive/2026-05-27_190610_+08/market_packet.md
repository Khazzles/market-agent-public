# Market Packet — 2026-05-27T19:06:10.585045+08:00

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
| SPY | 2026-05-26 | 750.59 | 0.66 | 1.62 | 5.13 | 7.47 | 10.47 | 71.28 | 1.00 | 0.00 | -4.87 | ABOVE_50_AND_200 |
| QQQ | 2026-05-26 | 730.28 | 1.78 | 3.46 | 10.00 | 13.25 | 18.65 | 75.33 | 1.49 | 4.87 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-26 | 612.34 | 0.34 | 0.18 | -9.29 | -0.88 | -8.43 | 46.45 | 2.43 | -14.42 | -19.29 | BELOW_50_AND_200 |
| AMZN | 2026-05-26 | 265.29 | -0.39 | 0.16 | 0.49 | 9.14 | 14.96 | 56.61 | 2.53 | -4.64 | -9.51 | ABOVE_50_AND_200 |
| MU | 2026-05-26 | 895.88 | 19.29 | 31.45 | 80.36 | 69.54 | 174.41 | 74.86 | 6.24 | 75.23 | 70.36 | ABOVE_50_AND_200 |
| ORCL | 2026-05-26 | 193.06 | 0.51 | 3.46 | 11.42 | 14.94 | -7.05 | 60.09 | 4.36 | 6.28 | 1.41 | MIXED |
| SOFI | 2026-05-26 | 15.98 | 2.30 | 1.72 | -13.34 | -4.46 | -31.41 | 46.48 | 4.99 | -18.47 | -23.34 | BELOW_50_AND_200 |
| IAU | 2026-05-26 | 84.81 | 0.00 | -1.11 | -4.44 | -3.21 | 3.36 | 40.05 | 1.78 | -9.57 | -14.44 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-27 | 16.90 | -0.65 | -3.10 | -5.22 | -16.85 | BELOW_50_AND_200 |
| ^TNX | 2026-05-26 | 4.49 | -1.43 | -2.81 | 4.25 | 2.70 | ABOVE_50_AND_200 |
| CL=F | 2026-05-27 | 90.30 | -3.82 | -16.21 | -6.30 | -8.06 | BELOW_50_ABOVE_200 |
| GC=F | 2026-05-27 | 4474.80 | -0.57 | -0.70 | -4.29 | -3.71 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-27 | 99.13 | -0.02 | -0.17 | 0.66 | 0.20 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.98 | XLE, XOP, USO |
| semis_ai | 5.29 | SMH, SOXX |
| high_beta | 3.71 | IWM, ARKK, HIBL |
| rates | -0.38 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | -2.56 | SH, PSQ, SQQQ |
| housing_rates | 1.78 | XHB, ITB |
| defensives | -0.71 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 8.15 | 24.11 | 39.21 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 6.10 | 23.50 | 34.48 | ABOVE_50_AND_200 |
| SMH | semis_ai | 4.48 | 18.90 | 27.43 | ABOVE_50_AND_200 |
| XHB | housing_rates | 2.33 | -5.63 | 0.45 | MIXED |
| IWM | high_beta | 1.89 | 5.01 | 8.61 | ABOVE_50_AND_200 |
| ITB | housing_rates | 1.23 | -7.45 | -0.87 | BELOW_50_AND_200 |
| ARKK | high_beta | 1.09 | 0.95 | 4.48 | MIXED |
| TLT | rates | 0.50 | -1.86 | -1.04 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -5.35 | -25.18 | -34.53 | BELOW_50_AND_200 |
| XOP | energy | -3.40 | -1.16 | -3.88 | BELOW_50_ABOVE_200 |
| USO | energy | -2.78 | 3.47 | 3.76 | ABOVE_50_AND_200 |
| XLE | energy | -2.76 | 1.72 | -0.99 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -1.73 | -8.81 | -12.09 | BELOW_50_AND_200 |
| XLP | defensives | -1.38 | 0.48 | 0.70 | ABOVE_50_AND_200 |
| TBT | rates | -1.23 | 3.60 | 1.97 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.60 | -4.44 | -6.79 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
