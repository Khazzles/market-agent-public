# Market Packet — 2026-07-09T06:42:38.919439+08:00

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
| SPY | 2026-07-08 | 745.40 | -0.31 | -0.18 | 1.06 | 0.78 | 7.47 | 52.92 | 1.29 | 0.00 | 0.16 | ABOVE_50_AND_200 |
| QQQ | 2026-07-08 | 711.44 | 0.28 | -3.39 | 0.90 | -0.16 | 11.73 | 47.86 | 2.26 | -0.16 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-08 | 603.12 | -2.02 | 7.07 | 1.71 | 0.28 | -6.34 | 53.86 | 3.70 | 0.64 | 0.80 | MIXED |
| AMZN | 2026-07-08 | 243.62 | -0.96 | 2.22 | -0.98 | -4.31 | 4.48 | 49.41 | 3.16 | -2.04 | -1.88 | BELOW_50_ABOVE_200 |
| MU | 2026-07-08 | 948.80 | 1.11 | -17.80 | 9.81 | 7.79 | 107.95 | 46.99 | 9.55 | 8.75 | 8.91 | ABOVE_50_AND_200 |
| ORCL | 2026-07-08 | 140.49 | -0.78 | -4.14 | -34.25 | -23.71 | -28.86 | 28.70 | 6.61 | -35.32 | -35.16 | BELOW_50_AND_200 |
| SOFI | 2026-07-08 | 17.73 | -0.11 | -1.12 | 10.61 | 5.29 | -20.09 | 52.47 | 5.28 | 9.54 | 9.70 | MIXED |
| IAU | 2026-07-08 | 76.74 | -0.81 | 1.63 | -5.52 | -7.09 | -8.74 | 40.38 | 2.14 | -6.58 | -6.42 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-08 | 16.90 | 4.77 | 2.74 | -21.43 | -3.32 | BELOW_50_AND_200 |
| ^TNX | 2026-07-08 | 4.57 | 0.88 | 4.46 | 2.05 | 2.31 | ABOVE_50_AND_200 |
| CL=F | 2026-07-08 | 74.52 | 5.79 | 7.22 | -17.69 | -16.21 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-08 | 4086.60 | -1.42 | 1.58 | -5.78 | -7.00 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-08 | 101.07 | -0.07 | -0.12 | 1.00 | 1.47 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.57 | XLE, XOP, USO |
| semis_ai | 1.93 | SMH, SOXX |
| high_beta | -1.15 | IWM, ARKK, HIBL |
| rates | 0.16 | TLT, TBF, TBT |
| dollar | -0.14 | UUP |
| equity_hedges | -0.24 | SH, PSQ, SQQQ |
| housing_rates | -3.52 | XHB, ITB |
| defensives | -0.65 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 3.02 | -15.64 | -13.40 | BELOW_50_ABOVE_200 |
| XOP | energy | 2.94 | -2.41 | -2.17 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.99 | 4.09 | 1.23 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.87 | 4.12 | 1.66 | ABOVE_50_AND_200 |
| XLE | energy | 1.76 | -3.59 | -2.19 | BELOW_50_ABOVE_200 |
| TBT | rates | 0.39 | 0.80 | 1.66 | ABOVE_50_AND_200 |
| TBF | rates | 0.30 | 0.34 | 0.80 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.30 | -1.84 | -1.26 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -3.97 | 3.24 | 0.67 | MIXED |
| XHB | housing_rates | -3.08 | 2.44 | 0.52 | MIXED |
| ARKK | high_beta | -1.27 | 7.61 | 2.86 | ABOVE_50_AND_200 |
| HIBL | high_beta | -1.26 | 0.29 | -4.29 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.92 | 4.20 | 1.98 | ABOVE_50_AND_200 |
| XLU | defensives | -0.74 | 2.28 | 0.80 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -0.74 | -7.20 | -4.48 | BELOW_50_AND_200 |
| XLP | defensives | -0.55 | 1.14 | 0.40 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
