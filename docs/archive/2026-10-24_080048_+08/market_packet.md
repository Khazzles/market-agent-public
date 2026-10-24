# Market Packet — 2026-10-24T08:00:48.476330+08:00

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
| SPY | 2026-10-22 | 763.96 | -1.18 | -1.01 | -0.50 | -0.55 | 5.13 | 45.17 | 0.94 | 0.00 | 4.46 | BELOW_50_ABOVE_200 |
| QQQ | 2026-10-22 | 704.47 | -2.86 | -3.23 | -4.96 | -3.01 | 4.07 | 36.54 | 1.64 | -4.46 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-22 | 648.85 | -6.98 | -11.93 | -12.80 | -2.11 | 2.58 | 36.83 | 4.02 | -12.30 | -7.84 | BELOW_50_ABOVE_200 |
| AMZN | 2026-10-22 | 250.38 | -4.57 | -1.72 | 0.45 | -2.19 | 2.93 | 45.11 | 2.66 | 0.95 | 5.40 | BELOW_50_ABOVE_200 |
| MU | 2026-10-22 | 856.49 | -6.26 | -8.03 | -20.09 | -12.97 | 17.42 | 34.65 | 5.59 | -19.59 | -15.14 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-22 | 125.54 | -2.78 | -6.64 | -13.16 | -12.51 | -20.99 | 38.39 | 5.22 | -12.66 | -8.20 | BELOW_50_AND_200 |
| SOFI | 2026-10-22 | 14.77 | -0.87 | -2.12 | -10.76 | -12.17 | -18.46 | 39.64 | 4.38 | -10.25 | -5.80 | BELOW_50_AND_200 |
| IAU | 2026-10-22 | 75.66 | -2.64 | -3.58 | -6.04 | -6.61 | -10.90 | 35.68 | 1.57 | -5.53 | -1.08 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-23 | 19.45 | 2.21 | -2.70 | 24.12 | 22.06 | ABOVE_50_AND_200 |
| ^TNX | 2026-10-23 | 4.99 | 0.71 | -2.16 | -3.37 | 0.09 | ABOVE_50_AND_200 |
| CL=F | 2026-10-23 | 103.44 | 3.99 | 2.00 | 9.33 | 11.31 | ABOVE_50_AND_200 |
| GC=F | 2026-10-23 | 4010.00 | -1.24 | -4.09 | -6.70 | -7.64 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-23 | 101.75 | 0.14 | -0.09 | 0.46 | 1.21 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.08 | XLE, XOP, USO |
| semis_ai | -6.39 | SMH, SOXX |
| high_beta | -6.21 | IWM, ARKK, HIBL |
| rates | -1.35 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 4.22 | SH, PSQ, SQQQ |
| housing_rates | 4.58 | XHB, ITB |
| defensives | 2.69 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 8.55 | 15.99 | 7.54 | MIXED |
| ITB | housing_rates | 5.39 | 2.76 | 0.75 | MIXED |
| XHB | housing_rates | 3.77 | 2.17 | -0.43 | BELOW_50_AND_200 |
| XLP | defensives | 3.31 | 9.17 | 6.71 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 2.88 | 5.54 | 2.70 | MIXED |
| XLU | defensives | 2.07 | 7.85 | 2.32 | MIXED |
| TLT | rates | 1.87 | 1.59 | 1.44 | MIXED |
| USO | energy | 1.70 | 9.19 | 11.63 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -14.53 | -28.83 | -24.36 | BELOW_50_AND_200 |
| SOXX | semis_ai | -6.79 | -15.91 | -10.92 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -5.99 | -12.98 | -9.19 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -4.17 | -8.81 | -4.91 | BELOW_50_ABOVE_200 |
| TBT | rates | -3.97 | -3.60 | -3.71 | BELOW_50_ABOVE_200 |
| TBF | rates | -1.96 | -1.66 | -1.79 | BELOW_50_ABOVE_200 |
| XOP | energy | -1.08 | 7.79 | 3.87 | ABOVE_50_AND_200 |
| XLE | energy | -0.87 | 8.34 | 5.29 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
