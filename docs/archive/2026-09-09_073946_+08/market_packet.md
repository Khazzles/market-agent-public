# Market Packet — 2026-09-09T07:39:46.959369+08:00

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
| SPY | 2026-09-08 | 765.96 | -0.55 | -0.14 | -0.94 | 1.10 | 7.48 | 51.36 | 0.80 | 0.00 | -0.30 | ABOVE_50_AND_200 |
| QQQ | 2026-09-08 | 718.36 | -0.08 | 0.22 | -0.65 | 0.99 | 9.12 | 53.19 | 1.28 | 0.30 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-08 | 613.48 | -0.53 | 7.19 | 3.61 | 2.80 | -1.43 | 60.86 | 3.22 | 4.55 | 4.26 | MIXED |
| AMZN | 2026-09-08 | 256.97 | -0.60 | -1.08 | -6.38 | 1.00 | 7.39 | 48.12 | 2.52 | -5.44 | -5.73 | ABOVE_50_AND_200 |
| MU | 2026-09-08 | 1000.26 | -1.61 | 4.33 | 13.98 | 6.91 | 63.89 | 57.66 | 5.40 | 14.92 | 14.63 | ABOVE_50_AND_200 |
| ORCL | 2026-09-08 | 162.52 | 2.36 | 8.99 | 10.54 | 15.99 | -3.55 | 63.40 | 4.39 | 11.49 | 11.19 | MIXED |
| SOFI | 2026-09-08 | 18.01 | -1.15 | 0.73 | -2.01 | 0.71 | -9.63 | 49.69 | 4.57 | -1.07 | -1.37 | MIXED |
| IAU | 2026-09-08 | 81.95 | -1.73 | -2.10 | 0.33 | 2.68 | -3.75 | 47.76 | 1.96 | 1.27 | 0.98 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-08 | 15.72 | 2.75 | -3.79 | 1.68 | -2.36 | BELOW_50_AND_200 |
| ^TNX | 2026-09-08 | 4.81 | 0.46 | 1.01 | 3.13 | 3.53 | ABOVE_50_AND_200 |
| CL=F | 2026-09-08 | 94.34 | 3.13 | 10.00 | 20.67 | 15.81 | ABOVE_50_AND_200 |
| GC=F | 2026-09-08 | 4400.70 | -0.66 | -0.69 | 1.38 | 3.66 | MIXED |
| DX-Y.NYB | 2026-09-08 | 98.84 | -0.33 | -0.60 | -0.77 | -1.35 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.88 | XLE, XOP, USO |
| semis_ai | 1.41 | SMH, SOXX |
| high_beta | 0.61 | IWM, ARKK, HIBL |
| rates | 0.01 | TLT, TBF, TBT |
| dollar | -0.32 | UUP |
| equity_hedges | 0.30 | SH, PSQ, SQQQ |
| housing_rates | -2.73 | XHB, ITB |
| defensives | 0.10 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.87 | 23.78 | 17.11 | ABOVE_50_AND_200 |
| HIBL | high_beta | 2.46 | 1.20 | 2.96 | ABOVE_50_AND_200 |
| XOP | energy | 1.68 | 16.53 | 11.21 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.64 | -2.74 | -1.62 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.19 | -1.54 | 0.09 | ABOVE_50_AND_200 |
| XLE | energy | 1.11 | 12.64 | 9.00 | ABOVE_50_AND_200 |
| XLU | defensives | 0.86 | -0.37 | -2.11 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.53 | 1.40 | -0.60 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -3.05 | -9.98 | -6.71 | BELOW_50_AND_200 |
| XHB | housing_rates | -2.42 | -9.07 | -6.25 | BELOW_50_AND_200 |
| XLP | defensives | -0.66 | -1.29 | -1.17 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.45 | -2.28 | -0.75 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.32 | -0.28 | -0.86 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.16 | 8.37 | 7.72 | ABOVE_50_AND_200 |
| TLT | rates | -0.01 | -0.68 | -1.33 | BELOW_50_AND_200 |
| TBT | rates | 0.00 | 0.93 | 2.15 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
