# Market Packet — 2026-08-21T05:59:56.614946+08:00

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
| SPY | 2026-08-20 | 762.60 | -0.84 | -1.96 | 2.03 | 1.55 | 7.84 | 51.74 | 0.93 | 0.00 | 1.24 | ABOVE_50_AND_200 |
| QQQ | 2026-08-20 | 710.93 | -0.72 | -2.89 | 0.79 | -0.30 | 8.98 | 48.80 | 1.65 | -1.24 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-20 | 545.83 | -0.04 | -8.26 | -12.97 | -8.02 | -12.61 | 37.01 | 3.85 | -15.00 | -13.76 | BELOW_50_AND_200 |
| AMZN | 2026-08-20 | 260.11 | -2.16 | -1.89 | 6.23 | 4.33 | 9.15 | 50.92 | 2.98 | 4.20 | 5.44 | ABOVE_50_AND_200 |
| MU | 2026-08-20 | 974.33 | 3.97 | 2.58 | 1.55 | 1.17 | 71.71 | 55.16 | 7.13 | -0.48 | 0.76 | ABOVE_50_AND_200 |
| ORCL | 2026-08-20 | 142.07 | -1.21 | -9.06 | 12.90 | -3.04 | -18.18 | 48.82 | 5.00 | 10.86 | 12.11 | BELOW_50_AND_200 |
| SOFI | 2026-08-20 | 17.92 | -2.71 | -2.77 | 4.98 | 1.75 | -12.90 | 51.16 | 4.64 | 2.95 | 4.19 | MIXED |
| IAU | 2026-08-20 | 85.13 | 0.34 | 4.10 | 9.58 | 8.72 | 0.57 | 67.79 | 1.78 | 7.54 | 8.79 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-20 | 16.01 | 7.52 | 9.43 | -14.70 | -6.46 | BELOW_50_AND_200 |
| ^TNX | 2026-08-20 | 4.70 | 0.92 | 1.19 | 0.84 | 2.65 | ABOVE_50_AND_200 |
| CL=F | 2026-08-20 | 86.21 | 0.44 | 6.10 | -0.71 | 8.96 | ABOVE_50_AND_200 |
| GC=F | 2026-08-20 | 4575.10 | 1.91 | 4.85 | 10.33 | 9.80 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-20 | 98.87 | 0.04 | -1.09 | -1.87 | -1.59 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.21 | XLE, XOP, USO |
| semis_ai | 0.41 | SMH, SOXX |
| high_beta | -2.18 | IWM, ARKK, HIBL |
| rates | 0.52 | TLT, TBF, TBT |
| dollar | 0.11 | UUP |
| equity_hedges | 1.29 | SH, PSQ, SQQQ |
| housing_rates | -2.48 | XHB, ITB |
| defensives | -0.99 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.77 | 2.17 | 11.97 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 2.18 | -3.83 | -1.40 | BELOW_50_AND_200 |
| TBT | rates | 1.52 | 4.95 | 4.25 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.93 | -1.54 | -1.24 | BELOW_50_AND_200 |
| TBF | rates | 0.87 | 2.67 | 2.37 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.78 | -0.69 | 0.23 | MIXED |
| XOP | energy | 0.60 | 6.15 | 12.31 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.52 | -5.97 | -6.59 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.16 | 6.54 | -7.11 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -2.54 | -0.61 | -1.72 | BELOW_50_AND_200 |
| XHB | housing_rates | -2.41 | -2.43 | -2.99 | BELOW_50_AND_200 |
| XLP | defensives | -1.41 | 1.11 | 0.66 | ABOVE_50_AND_200 |
| IWM | high_beta | -1.34 | 1.32 | 0.46 | ABOVE_50_AND_200 |
| TLT | rates | -0.82 | -1.32 | -2.24 | BELOW_50_AND_200 |
| XLU | defensives | -0.57 | -4.70 | -2.41 | BELOW_50_AND_200 |
| ARKK | high_beta | -0.05 | 7.18 | 6.84 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
