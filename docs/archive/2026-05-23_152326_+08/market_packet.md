# Market Packet — 2026-05-23T15:23:26.973546+08:00

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
| SPY | 2026-05-22 | 745.64 | 0.39 | 0.88 | 5.25 | 7.03 | 9.84 | 68.77 | 1.02 | 0.00 | -4.90 | ABOVE_50_AND_200 |
| QQQ | 2026-05-22 | 717.54 | 0.42 | 1.21 | 10.15 | 11.75 | 16.74 | 71.37 | 1.49 | 4.90 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-22 | 610.26 | 0.47 | -0.65 | -7.42 | -1.22 | -8.84 | 45.34 | 2.51 | -12.67 | -17.57 | BELOW_50_AND_200 |
| AMZN | 2026-05-22 | 266.32 | -0.80 | 0.83 | 4.41 | 10.08 | 15.51 | 57.98 | 2.50 | -0.84 | -5.74 | ABOVE_50_AND_200 |
| MU | 2026-05-22 | 751.00 | -1.46 | 3.63 | 55.90 | 44.70 | 132.83 | 65.07 | 6.31 | 50.65 | 45.75 | ABOVE_50_AND_200 |
| ORCL | 2026-05-22 | 192.08 | 1.22 | -0.45 | 8.96 | 14.87 | -7.64 | 59.42 | 4.53 | 3.71 | -1.19 | MIXED |
| SOFI | 2026-05-22 | 15.62 | -0.19 | 0.06 | -14.74 | -6.81 | -33.04 | 42.75 | 4.85 | -19.99 | -24.89 | BELOW_50_AND_200 |
| IAU | 2026-05-22 | 84.81 | -0.73 | -0.82 | -4.00 | -3.42 | 3.49 | 40.05 | 1.83 | -9.25 | -14.15 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-22 | 16.70 | -0.36 | -9.39 | -13.52 | -19.62 | BELOW_50_AND_200 |
| ^TNX | 2026-05-22 | 4.56 | -0.61 | -0.81 | 5.44 | 4.28 | ABOVE_50_AND_200 |
| CL=F | 2026-05-22 | 96.60 | 0.26 | -8.37 | 0.78 | -1.81 | BELOW_50_ABOVE_200 |
| GC=F | 2026-05-22 | 4521.00 | -0.41 | -0.76 | -3.91 | -3.17 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-22 | 99.32 | 0.13 | 0.05 | 0.53 | 0.36 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.08 | XLE, XOP, USO |
| semis_ai | 1.95 | SMH, SOXX |
| high_beta | 1.66 | IWM, ARKK, HIBL |
| rates | -0.22 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | -0.59 | SH, PSQ, SQQQ |
| housing_rates | 0.31 | XHB, ITB |
| defensives | 0.47 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.33 | 19.94 | 30.42 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 2.41 | 21.84 | 28.20 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.49 | 19.61 | 23.08 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.93 | 3.48 | 6.95 | ABOVE_50_AND_200 |
| XLU | defensives | 0.78 | -1.61 | -0.93 | BELOW_50_ABOVE_200 |
| XOP | energy | 0.76 | 1.41 | -0.52 | BELOW_50_ABOVE_200 |
| XLE | energy | 0.61 | 4.41 | 1.82 | ABOVE_50_AND_200 |
| TLT | rates | 0.55 | -2.16 | -1.56 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -1.14 | 4.60 | 7.00 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -1.10 | -25.44 | -31.66 | BELOW_50_AND_200 |
| TBT | rates | -0.68 | 4.62 | 3.29 | ABOVE_50_AND_200 |
| TBF | rates | -0.52 | 2.35 | 1.66 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.34 | -8.99 | -10.90 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.33 | -4.56 | -6.46 | BELOW_50_AND_200 |
| ARKK | high_beta | -0.29 | -0.13 | 3.55 | MIXED |
| UUP | dollar | 0.14 | 0.87 | 0.67 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
