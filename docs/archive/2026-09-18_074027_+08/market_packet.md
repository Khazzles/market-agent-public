# Market Packet — 2026-09-18T07:40:27.902357+08:00

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
| SPY | 2026-09-17 | 762.60 | 1.13 | 0.63 | -0.63 | 0.40 | 6.53 | 49.98 | 0.89 | 0.00 | -0.55 | ABOVE_50_AND_200 |
| QQQ | 2026-09-17 | 716.92 | 1.73 | 1.16 | -0.08 | 0.98 | 8.28 | 53.05 | 1.32 | 0.55 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-17 | 682.31 | 1.34 | 5.89 | 25.50 | 12.46 | 9.34 | 73.97 | 3.02 | 26.13 | 25.58 | ABOVE_50_AND_200 |
| AMZN | 2026-09-17 | 251.19 | 2.13 | -0.28 | -3.18 | -1.77 | 4.57 | 45.39 | 2.46 | -2.55 | -3.10 | BELOW_50_ABOVE_200 |
| MU | 2026-09-17 | 977.50 | 5.50 | 0.01 | 3.91 | 5.47 | 53.63 | 53.81 | 5.12 | 4.54 | 3.99 | ABOVE_50_AND_200 |
| ORCL | 2026-09-17 | 150.59 | 5.19 | -1.54 | 5.46 | 6.85 | -9.57 | 52.20 | 5.14 | 6.09 | 5.54 | MIXED |
| SOFI | 2026-09-17 | 16.73 | -0.65 | -2.79 | -5.27 | -5.74 | -14.54 | 41.43 | 4.42 | -4.63 | -5.18 | BELOW_50_AND_200 |
| IAU | 2026-09-17 | 81.69 | 1.71 | 0.52 | -0.02 | 1.53 | -4.19 | 48.62 | 1.99 | 0.61 | 0.06 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-17 | 15.44 | -12.82 | -13.45 | 3.69 | -4.56 | BELOW_50_AND_200 |
| ^TNX | 2026-09-17 | 4.95 | -1.18 | 0.06 | 5.12 | 5.06 | ABOVE_50_AND_200 |
| CL=F | 2026-09-17 | 101.09 | -1.31 | -1.36 | 19.01 | 17.80 | ABOVE_50_AND_200 |
| GC=F | 2026-09-17 | 4382.90 | -0.10 | -0.55 | -0.85 | 1.47 | MIXED |
| DX-Y.NYB | 2026-09-17 | 100.24 | -0.07 | 1.16 | 0.59 | 0.27 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.19 | XLE, XOP, USO |
| semis_ai | 3.08 | SMH, SOXX |
| high_beta | 4.09 | IWM, ARKK, HIBL |
| rates | -0.76 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | -2.67 | SH, PSQ, SQQQ |
| housing_rates | 0.38 | XHB, ITB |
| defensives | 0.54 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 7.23 | -4.35 | -3.43 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 4.50 | 9.82 | 8.23 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 3.39 | -2.31 | -1.43 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 2.76 | -1.61 | -0.86 | BELOW_50_ABOVE_200 |
| TLT | rates | 1.11 | 0.15 | -1.08 | BELOW_50_AND_200 |
| XLU | defensives | 0.90 | -5.29 | -5.03 | BELOW_50_AND_200 |
| XLE | energy | 0.70 | 1.26 | 5.73 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.53 | -4.93 | -3.38 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -5.12 | 0.65 | -3.39 | BELOW_50_AND_200 |
| TBT | rates | -2.35 | -0.80 | 1.74 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.75 | 0.43 | -0.70 | BELOW_50_AND_200 |
| SH | equity_hedges | -1.15 | 1.05 | 0.06 | MIXED |
| TBF | rates | -1.04 | -0.27 | 1.08 | ABOVE_50_AND_200 |
| USO | energy | -0.55 | 18.87 | 17.99 | ABOVE_50_AND_200 |
| UUP | dollar | -0.07 | 0.85 | 0.62 | ABOVE_50_AND_200 |
| XLP | defensives | 0.19 | -2.44 | -1.69 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
