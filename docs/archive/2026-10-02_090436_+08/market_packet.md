# Market Packet — 2026-10-02T09:04:36.825394+08:00

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
| SPY | 2026-09-30 | 762.63 | -0.21 | -0.67 | -0.58 | -0.01 | 5.98 | 47.82 | 0.87 | 0.00 | -3.79 | BELOW_50_ABOVE_200 |
| QQQ | 2026-09-30 | 739.77 | 0.25 | -0.19 | 3.21 | 3.47 | 10.87 | 60.22 | 1.25 | 3.79 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-30 | 725.18 | -1.84 | -2.54 | 26.70 | 16.85 | 15.55 | 60.98 | 3.61 | 27.28 | 23.49 | ABOVE_50_AND_200 |
| AMZN | 2026-09-30 | 249.15 | 1.01 | -0.05 | -4.09 | -2.72 | 3.34 | 45.20 | 2.27 | -3.51 | -7.30 | BELOW_50_ABOVE_200 |
| MU | 2026-09-30 | 1065.11 | 0.00 | -0.63 | 11.10 | 11.93 | 58.23 | 59.66 | 4.44 | 11.67 | 7.89 | ABOVE_50_AND_200 |
| ORCL | 2026-09-30 | 137.30 | -0.36 | -5.02 | -7.93 | -3.92 | -15.95 | 42.67 | 5.01 | -7.35 | -11.14 | BELOW_50_AND_200 |
| SOFI | 2026-09-30 | 15.72 | -1.19 | -5.02 | -12.08 | -10.15 | -17.48 | 35.11 | 4.12 | -11.50 | -15.29 | BELOW_50_AND_200 |
| IAU | 2026-09-30 | 78.10 | -0.53 | -3.01 | -6.70 | -3.80 | -8.44 | 38.68 | 1.82 | -6.13 | -9.91 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-01 | 16.39 | 0.31 | 4.59 | 7.83 | 3.41 | MIXED |
| ^TNX | 2026-10-01 | 5.24 | -1.06 | 1.45 | 9.20 | 8.64 | ABOVE_50_AND_200 |
| CL=F | 2026-10-01 | 93.14 | 3.01 | -1.55 | 3.24 | 5.12 | ABOVE_50_AND_200 |
| GC=F | 2026-10-01 | 4189.50 | 0.07 | -2.52 | -4.71 | -3.99 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-01 | 102.08 | 0.62 | 0.78 | 2.42 | 2.09 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.65 | XLE, XOP, USO |
| semis_ai | 0.28 | SMH, SOXX |
| high_beta | -0.88 | IWM, ARKK, HIBL |
| rates | 0.37 | TLT, TBF, TBT |
| dollar | 0.07 | UUP |
| equity_hedges | -0.19 | SH, PSQ, SQQQ |
| housing_rates | -1.25 | XHB, ITB |
| defensives | -1.10 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 1.61 | 8.95 | 6.44 | ABOVE_50_AND_200 |
| TBT | rates | 1.09 | 11.38 | 10.10 | ABOVE_50_AND_200 |
| TBF | rates | 0.60 | 5.51 | 5.00 | ABOVE_50_AND_200 |
| XOP | energy | 0.39 | -5.10 | -1.89 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.35 | 9.41 | 7.18 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.31 | -0.15 | -0.47 | BELOW_50_AND_200 |
| SOXX | semis_ai | 0.21 | 11.27 | 7.58 | ABOVE_50_AND_200 |
| UUP | dollar | 0.07 | 2.31 | 1.85 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -1.85 | 7.12 | 5.36 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.54 | -8.10 | -7.75 | BELOW_50_AND_200 |
| XLP | defensives | -1.53 | -5.15 | -4.64 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.97 | -6.59 | -7.28 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -0.72 | -10.65 | -11.60 | BELOW_50_AND_200 |
| XLU | defensives | -0.68 | -6.61 | -8.14 | BELOW_50_AND_200 |
| TLT | rates | -0.58 | -5.74 | -5.03 | BELOW_50_AND_200 |
| IWM | high_beta | -0.40 | -5.46 | -5.18 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
