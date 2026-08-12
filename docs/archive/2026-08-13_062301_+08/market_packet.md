# Market Packet — 2026-08-13T06:23:01.640700+08:00

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
| SPY | 2026-08-12 | 772.49 | 0.25 | 0.35 | 2.75 | 3.26 | 9.65 | 64.44 | 1.03 | 0.00 | 2.19 | ABOVE_50_AND_200 |
| QQQ | 2026-08-12 | 723.70 | 0.73 | 0.89 | 0.56 | 1.43 | 11.42 | 57.06 | 1.85 | -2.19 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-12 | 578.85 | -3.38 | -1.68 | -12.43 | -3.18 | -8.00 | 43.87 | 3.93 | -15.18 | -12.99 | BELOW_50_AND_200 |
| AMZN | 2026-08-12 | 267.28 | -1.83 | -1.97 | 8.00 | 7.89 | 12.62 | 57.06 | 3.30 | 5.25 | 7.44 | ABOVE_50_AND_200 |
| MU | 2026-08-12 | 911.29 | 4.92 | 2.03 | -7.31 | -5.58 | 67.15 | 51.08 | 8.34 | -10.05 | -7.86 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-12 | 153.28 | 5.36 | 6.16 | 19.81 | -1.57 | -13.61 | 59.56 | 4.96 | 17.06 | 19.25 | BELOW_50_AND_200 |
| SOFI | 2026-08-12 | 17.94 | -0.22 | -1.70 | -3.29 | 2.85 | -14.28 | 53.05 | 4.61 | -6.04 | -3.85 | MIXED |
| IAU | 2026-08-12 | 82.98 | 0.97 | 3.92 | 8.80 | 6.08 | -1.70 | 68.00 | 1.78 | 6.05 | 8.24 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-12 | 14.55 | -4.78 | -7.97 | -11.82 | -15.59 | BELOW_50_AND_200 |
| ^TNX | 2026-08-12 | 4.68 | -0.04 | 1.41 | 2.12 | 2.83 | ABOVE_50_AND_200 |
| CL=F | 2026-08-12 | 82.72 | -0.58 | 9.97 | 4.26 | 3.32 | ABOVE_50_AND_200 |
| GC=F | 2026-08-12 | 4461.40 | 1.79 | 5.08 | 9.86 | 7.18 | MIXED |
| DX-Y.NYB | 2026-08-12 | 99.98 | 0.17 | 0.30 | -0.95 | -0.55 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.01 | XLE, XOP, USO |
| semis_ai | 2.20 | SMH, SOXX |
| high_beta | 2.86 | IWM, ARKK, HIBL |
| rates | 0.18 | TLT, TBF, TBT |
| dollar | 0.21 | UUP |
| equity_hedges | -1.06 | SH, PSQ, SQQQ |
| housing_rates | -2.04 | XHB, ITB |
| defensives | 0.47 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 7.07 | 6.09 | 1.34 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 2.32 | -3.75 | -3.16 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 2.08 | -2.58 | -1.44 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 0.96 | 2.33 | 5.12 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.57 | 2.78 | 2.78 | ABOVE_50_AND_200 |
| XLU | defensives | 0.48 | -4.05 | -2.21 | BELOW_50_AND_200 |
| XLP | defensives | 0.46 | 1.99 | 0.79 | ABOVE_50_AND_200 |
| TBF | rates | 0.32 | 2.54 | 2.90 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -2.32 | 1.07 | 0.24 | MIXED |
| SQQQ | equity_hedges | -2.15 | -3.39 | -7.19 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.77 | 0.18 | -0.17 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -0.74 | -0.51 | -1.77 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.28 | -2.31 | -3.08 | BELOW_50_AND_200 |
| USO | energy | -0.24 | 5.93 | 5.31 | ABOVE_50_AND_200 |
| TLT | rates | -0.10 | -2.34 | -2.93 | BELOW_50_AND_200 |
| XOP | energy | 0.12 | 7.68 | 8.19 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
