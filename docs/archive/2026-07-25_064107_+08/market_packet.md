# Market Packet — 2026-07-25T06:41:07.590246+08:00

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
| SPY | 2026-07-24 | 738.93 | 0.10 | -0.59 | 0.78 | -0.82 | 5.78 | 45.23 | 1.10 | 0.00 | 4.49 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-24 | 684.23 | -1.12 | -1.60 | -3.71 | -4.74 | 6.38 | 39.29 | 2.07 | -4.49 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-24 | 595.19 | -1.80 | -7.87 | 6.73 | -1.80 | -6.72 | 43.82 | 4.11 | 5.95 | 10.44 | BELOW_50_AND_200 |
| AMZN | 2026-07-24 | 232.11 | -0.66 | -6.12 | -0.92 | -6.87 | -1.06 | 37.49 | 3.11 | -1.70 | 2.79 | BELOW_50_AND_200 |
| MU | 2026-07-24 | 920.95 | -6.99 | 8.48 | -12.17 | -3.60 | 83.43 | 47.14 | 8.80 | -12.94 | -8.45 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-24 | 114.99 | -4.21 | -9.03 | -27.00 | -32.97 | -38.64 | 27.42 | 6.79 | -27.78 | -23.29 | BELOW_50_AND_200 |
| SOFI | 2026-07-24 | 16.46 | -1.14 | -4.75 | -4.91 | -3.83 | -23.77 | 41.06 | 5.12 | -5.69 | -1.20 | BELOW_50_AND_200 |
| IAU | 2026-07-24 | 76.23 | 0.11 | 0.97 | 1.65 | -4.65 | -9.63 | 44.75 | 1.88 | 0.88 | 5.37 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-24 | 18.58 | -0.64 | -1.01 | -0.27 | 7.12 | MIXED |
| ^TNX | 2026-07-24 | 4.68 | -0.51 | 3.04 | 6.29 | 3.54 | ABOVE_50_AND_200 |
| CL=F | 2026-07-24 | 90.47 | -1.87 | 9.67 | 28.62 | 7.16 | ABOVE_50_AND_200 |
| GC=F | 2026-07-24 | 4055.70 | 0.22 | 1.07 | 1.64 | -4.67 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-24 | 101.47 | 0.03 | 0.71 | -0.14 | 1.21 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.84 | XLE, XOP, USO |
| semis_ai | -3.83 | SMH, SOXX |
| high_beta | -2.08 | IWM, ARKK, HIBL |
| rates | -0.17 | TLT, TBF, TBT |
| dollar | 0.07 | UUP |
| equity_hedges | 1.56 | SH, PSQ, SQQQ |
| housing_rates | 2.17 | XHB, ITB |
| defensives | 0.66 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 3.51 | 10.73 | 11.58 | MIXED |
| ITB | housing_rates | 2.70 | -6.03 | 1.27 | MIXED |
| XHB | housing_rates | 1.64 | -5.11 | 1.90 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.24 | 4.01 | 4.40 | MIXED |
| XLP | defensives | 1.11 | -0.37 | -0.05 | BELOW_50_ABOVE_200 |
| XLE | energy | 0.40 | 11.29 | 5.06 | ABOVE_50_AND_200 |
| XLU | defensives | 0.22 | 1.65 | 3.05 | ABOVE_50_AND_200 |
| TLT | rates | 0.10 | -4.73 | -2.15 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | -4.40 | -12.38 | -7.41 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -3.29 | -20.91 | -14.66 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -3.27 | -9.33 | -6.29 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.63 | -6.30 | -7.69 | BELOW_50_AND_200 |
| USO | energy | -2.01 | 28.60 | 9.02 | ABOVE_50_AND_200 |
| XOP | energy | -0.92 | 13.74 | 5.80 | ABOVE_50_AND_200 |
| TBT | rates | -0.40 | 9.77 | 3.74 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.32 | -1.86 | -0.01 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
