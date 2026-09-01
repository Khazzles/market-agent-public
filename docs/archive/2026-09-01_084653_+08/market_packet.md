# Market Packet — 2026-09-01T08:46:53.598198+08:00

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
| SPY | 2026-08-31 | 767.05 | -0.30 | 0.47 | 2.68 | 1.68 | 7.99 | 54.04 | 0.81 | 0.00 | -1.50 | ABOVE_50_AND_200 |
| QQQ | 2026-08-31 | 716.76 | 0.05 | 1.48 | 4.18 | 0.73 | 9.32 | 52.07 | 1.40 | 1.50 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-31 | 572.34 | -0.98 | 2.38 | 2.81 | -3.33 | -8.05 | 47.48 | 3.38 | 0.13 | -1.37 | BELOW_50_AND_200 |
| AMZN | 2026-08-31 | 259.77 | -2.50 | -0.88 | -4.35 | 3.10 | 8.81 | 50.08 | 2.77 | -7.03 | -8.53 | ABOVE_50_AND_200 |
| MU | 2026-08-31 | 958.73 | 2.77 | 5.31 | 16.49 | 0.76 | 61.94 | 53.76 | 6.07 | 13.81 | 12.31 | ABOVE_50_AND_200 |
| ORCL | 2026-08-31 | 149.12 | -1.15 | 4.68 | 14.82 | 5.88 | -12.40 | 54.12 | 4.22 | 12.14 | 10.64 | MIXED |
| SOFI | 2026-08-31 | 17.88 | -1.00 | -1.97 | 9.63 | 0.29 | -11.44 | 48.37 | 4.81 | 6.95 | 5.44 | MIXED |
| IAU | 2026-08-31 | 83.71 | -0.13 | -4.30 | 9.90 | 5.67 | -1.53 | 54.19 | 1.86 | 7.22 | 5.72 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-31 | 14.92 | 3.40 | -5.87 | -6.69 | -9.46 | BELOW_50_AND_200 |
| ^TNX | 2026-08-31 | 4.76 | 0.81 | 1.15 | 0.27 | 3.29 | ABOVE_50_AND_200 |
| CL=F | 2026-08-31 | 86.62 | 3.86 | 1.89 | 2.30 | 8.96 | ABOVE_50_AND_200 |
| GC=F | 2026-08-31 | 4504.10 | 0.58 | -2.95 | 11.24 | 6.87 | MIXED |
| DX-Y.NYB | 2026-08-31 | 99.37 | -0.33 | 0.38 | -0.43 | -1.02 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.25 | XLE, XOP, USO |
| semis_ai | 0.56 | SMH, SOXX |
| high_beta | 0.23 | IWM, ARKK, HIBL |
| rates | 0.39 | TLT, TBF, TBT |
| dollar | -0.21 | UUP |
| equity_hedges | 0.08 | SH, PSQ, SQQQ |
| housing_rates | -1.75 | XHB, ITB |
| defensives | -0.86 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 3.08 | 3.51 | 10.18 | ABOVE_50_AND_200 |
| XLE | energy | 2.04 | 7.41 | 9.60 | ABOVE_50_AND_200 |
| XOP | energy | 1.62 | 6.52 | 10.80 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.16 | 20.12 | 8.15 | ABOVE_50_AND_200 |
| TBT | rates | 1.01 | -0.78 | 3.12 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.64 | 2.98 | -4.13 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.59 | -0.31 | 1.77 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.48 | 1.22 | -6.67 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -1.78 | 0.37 | -3.84 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.71 | -0.85 | -5.30 | BELOW_50_AND_200 |
| XLU | defensives | -1.17 | -4.78 | -5.39 | BELOW_50_AND_200 |
| IWM | high_beta | -0.62 | 0.94 | -1.13 | BELOW_50_ABOVE_200 |
| XLP | defensives | -0.55 | -0.08 | 0.09 | ABOVE_50_AND_200 |
| TLT | rates | -0.43 | 0.33 | -1.52 | BELOW_50_AND_200 |
| UUP | dollar | -0.21 | -0.18 | -0.53 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -0.08 | -11.94 | -3.36 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
