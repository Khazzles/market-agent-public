# Market Packet — 2026-11-11T09:28:41.165205+08:00

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
| SPY | 2026-11-09 | 752.69 | 2.37 | 0.08 | -3.32 | -1.65 | 3.01 | 45.81 | 1.45 | 0.00 | 6.25 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-09 | 679.35 | 3.54 | -0.26 | -9.57 | -5.68 | -0.27 | 41.37 | 2.36 | -6.25 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-09 | 641.37 | 5.12 | 5.71 | -10.76 | -5.15 | 1.51 | 46.49 | 3.76 | -7.43 | -1.18 | BELOW_50_ABOVE_200 |
| AMZN | 2026-11-09 | 266.93 | 2.94 | 8.67 | 1.71 | 5.11 | 9.36 | 59.23 | 3.55 | 5.04 | 11.29 | ABOVE_50_AND_200 |
| MU | 2026-11-09 | 733.15 | 6.25 | -12.05 | -28.75 | -23.44 | -3.33 | 36.36 | 7.86 | -25.43 | -19.18 | BELOW_50_AND_200 |
| ORCL | 2026-11-09 | 119.79 | 3.18 | 0.48 | -15.28 | -13.51 | -22.77 | 41.87 | 6.71 | -11.96 | -5.71 | BELOW_50_AND_200 |
| SOFI | 2026-11-09 | 16.75 | 3.33 | 0.90 | 6.01 | 2.60 | -4.32 | 54.70 | 5.10 | 9.34 | 15.59 | MIXED |
| IAU | 2026-11-09 | 77.78 | 1.83 | 4.90 | -1.38 | -1.30 | -7.62 | 53.17 | 1.84 | 1.94 | 8.19 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-10 | 19.46 | -2.31 | -6.58 | 27.94 | 13.91 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-10 | 4.98 | 2.45 | 0.63 | -4.90 | -1.14 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-10 | 86.48 | -0.43 | -10.00 | -7.74 | -9.49 | BELOW_50_AND_200 |
| GC=F | 2026-11-10 | 4034.20 | -1.95 | 2.38 | -3.73 | -4.25 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-10 | 102.30 | 0.63 | 0.42 | -0.28 | 1.09 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.05 | XLE, XOP, USO |
| semis_ai | 6.27 | SMH, SOXX |
| high_beta | 8.39 | IWM, ARKK, HIBL |
| rates | -0.05 | TLT, TBF, TBT |
| dollar | -0.55 | UUP |
| equity_hedges | -5.35 | SH, PSQ, SQQQ |
| housing_rates | 3.31 | XHB, ITB |
| defensives | 1.21 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 17.27 | -36.82 | -25.30 | BELOW_50_AND_200 |
| SOXX | semis_ai | 7.49 | -21.29 | -15.27 | BELOW_50_AND_200 |
| SMH | semis_ai | 5.05 | -19.21 | -13.63 | BELOW_50_AND_200 |
| ARKK | high_beta | 4.66 | -11.87 | -7.46 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 3.59 | 11.81 | 7.63 | ABOVE_50_AND_200 |
| IWM | high_beta | 3.23 | 1.28 | 0.24 | ABOVE_50_AND_200 |
| ITB | housing_rates | 3.02 | 17.33 | 10.82 | ABOVE_50_AND_200 |
| XLU | defensives | 1.53 | 5.75 | 4.77 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -10.29 | 29.86 | 13.76 | MIXED |
| USO | energy | -3.87 | -3.74 | -6.44 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -3.43 | 10.21 | 5.38 | MIXED |
| SH | equity_hedges | -2.31 | 3.65 | 1.64 | MIXED |
| UUP | dollar | -0.55 | -0.17 | 0.93 | ABOVE_50_AND_200 |
| TBT | rates | -0.34 | -9.94 | -4.81 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.05 | 5.10 | 1.99 | MIXED |
| TBF | rates | 0.16 | -4.84 | -2.14 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
