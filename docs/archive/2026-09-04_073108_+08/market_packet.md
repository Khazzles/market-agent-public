# Market Packet — 2026-09-04T07:31:08.023769+08:00

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
| SPY | 2026-09-03 | 773.17 | 1.05 | 0.27 | 0.44 | 2.25 | 8.65 | 58.79 | 0.82 | 0.00 | 0.39 | ABOVE_50_AND_200 |
| QQQ | 2026-09-03 | 717.67 | 1.19 | -0.48 | 0.05 | 0.93 | 9.21 | 52.85 | 1.36 | -0.39 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-03 | 610.68 | 3.01 | 6.93 | 3.72 | 2.81 | -1.85 | 60.69 | 3.39 | 3.28 | 3.67 | MIXED |
| AMZN | 2026-09-03 | 258.90 | 1.54 | 1.03 | -5.04 | 2.20 | 8.33 | 49.90 | 2.61 | -5.48 | -5.09 | ABOVE_50_AND_200 |
| MU | 2026-09-03 | 958.16 | 0.22 | 2.43 | 7.27 | 1.69 | 59.00 | 53.49 | 5.69 | 6.83 | 7.22 | ABOVE_50_AND_200 |
| ORCL | 2026-09-03 | 154.04 | 5.69 | 1.38 | 6.68 | 10.26 | -8.90 | 57.58 | 4.45 | 6.24 | 6.63 | MIXED |
| SOFI | 2026-09-03 | 18.51 | 3.76 | -3.49 | 1.42 | 3.62 | -7.52 | 53.23 | 4.72 | 0.99 | 1.37 | MIXED |
| IAU | 2026-09-03 | 84.10 | 1.88 | -2.91 | 5.32 | 5.72 | -1.15 | 54.92 | 1.96 | 4.88 | 5.27 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-03 | 14.32 | -5.79 | -1.31 | -9.42 | -12.08 | BELOW_50_AND_200 |
| ^TNX | 2026-09-03 | 4.76 | -0.71 | 1.93 | 3.14 | 2.95 | ABOVE_50_AND_200 |
| CL=F | 2026-09-03 | 91.86 | 0.93 | 9.97 | 22.12 | 14.00 | ABOVE_50_AND_200 |
| GC=F | 2026-09-03 | 4519.30 | 3.50 | -1.96 | 6.44 | 6.80 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-09-03 | 99.00 | -0.56 | -0.16 | -0.69 | -1.27 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.17 | XLE, XOP, USO |
| semis_ai | 0.27 | SMH, SOXX |
| high_beta | 2.99 | IWM, ARKK, HIBL |
| rates | -0.37 | TLT, TBF, TBT |
| dollar | -0.57 | UUP |
| equity_hedges | -1.91 | SH, PSQ, SQQQ |
| housing_rates | 0.97 | XHB, ITB |
| defensives | 0.26 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | 4.50 | 14.39 | 9.53 | ABOVE_50_AND_200 |
| HIBL | high_beta | 4.07 | -5.89 | -3.58 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 1.09 | -7.77 | -5.32 | BELOW_50_AND_200 |
| ITB | housing_rates | 0.86 | -7.20 | -4.55 | BELOW_50_AND_200 |
| XLU | defensives | 0.84 | -1.44 | -3.29 | BELOW_50_AND_200 |
| USO | energy | 0.67 | 23.69 | 15.31 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.40 | -1.53 | -0.63 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.39 | -3.00 | -3.96 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.45 | 0.13 | -3.79 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -1.23 | 0.31 | -0.74 | BELOW_50_AND_200 |
| TBT | rates | -1.21 | 1.97 | 2.81 | ABOVE_50_AND_200 |
| SH | equity_hedges | -1.04 | 0.06 | -1.72 | BELOW_50_AND_200 |
| XLE | energy | -0.74 | 12.76 | 9.52 | ABOVE_50_AND_200 |
| UUP | dollar | -0.57 | -0.28 | -0.85 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.43 | 16.43 | 11.27 | ABOVE_50_AND_200 |
| XLP | defensives | -0.32 | -0.08 | 0.28 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
