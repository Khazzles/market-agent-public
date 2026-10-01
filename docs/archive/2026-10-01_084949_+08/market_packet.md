# Market Packet — 2026-10-01T08:49:49.606678+08:00

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
| SPY | 2026-09-29 | 764.20 | -0.18 | -1.19 | -0.67 | 0.23 | 6.25 | 49.24 | 0.86 | 0.00 | -3.67 | ABOVE_50_AND_200 |
| QQQ | 2026-09-29 | 737.93 | 0.19 | -1.27 | 3.00 | 3.31 | 10.68 | 59.21 | 1.26 | 3.67 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-29 | 738.79 | 3.24 | 0.30 | 27.81 | 19.35 | 17.79 | 64.52 | 3.66 | 28.48 | 24.81 | ABOVE_50_AND_200 |
| AMZN | 2026-09-29 | 246.67 | 0.21 | -3.26 | -7.42 | -3.68 | 2.35 | 41.93 | 2.29 | -6.75 | -10.42 | BELOW_50_ABOVE_200 |
| MU | 2026-09-29 | 1065.08 | 1.05 | -2.84 | 14.17 | 12.15 | 59.18 | 59.66 | 4.23 | 14.84 | 11.17 | ABOVE_50_AND_200 |
| ORCL | 2026-09-29 | 137.79 | 3.91 | -7.65 | -8.66 | -3.44 | -15.81 | 43.07 | 5.10 | -7.99 | -11.66 | BELOW_50_AND_200 |
| SOFI | 2026-09-29 | 15.91 | -0.13 | -7.28 | -11.90 | -9.27 | -16.74 | 36.54 | 4.14 | -11.24 | -14.91 | BELOW_50_AND_200 |
| IAU | 2026-09-29 | 78.52 | 1.32 | -4.28 | -6.32 | -3.25 | -7.96 | 39.89 | 1.88 | -5.65 | -9.32 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-30 | 16.34 | 1.87 | 7.64 | 0.00 | 2.80 | MIXED |
| ^TNX | 2026-09-30 | 5.29 | 0.72 | 3.50 | 11.24 | 10.07 | ABOVE_50_AND_200 |
| CL=F | 2026-09-30 | 90.54 | 1.30 | -1.76 | 5.57 | 2.33 | ABOVE_50_AND_200 |
| GC=F | 2026-09-30 | 4173.00 | -0.16 | -3.37 | -6.88 | -4.35 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-30 | 101.49 | 0.12 | 0.39 | 2.07 | 1.52 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.06 | XLE, XOP, USO |
| semis_ai | 1.17 | SMH, SOXX |
| high_beta | 0.93 | IWM, ARKK, HIBL |
| rates | 0.42 | TLT, TBF, TBT |
| dollar | 0.17 | UUP |
| equity_hedges | -0.19 | SH, PSQ, SQQQ |
| housing_rates | -0.38 | XHB, ITB |
| defensives | 0.32 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 2.92 | 9.29 | 7.45 | ABOVE_50_AND_200 |
| TBT | rates | 1.20 | 11.28 | 9.21 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.19 | 11.56 | 7.41 | ABOVE_50_AND_200 |
| XLU | defensives | 1.17 | -7.07 | -7.74 | BELOW_50_AND_200 |
| SMH | semis_ai | 1.15 | 9.72 | 6.90 | ABOVE_50_AND_200 |
| TBF | rates | 0.57 | 5.50 | 4.52 | ABOVE_50_AND_200 |
| ARKK | high_beta | 0.22 | 5.75 | 8.79 | ABOVE_50_AND_200 |
| UUP | dollar | 0.17 | 2.02 | 1.80 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -4.44 | 10.52 | 5.01 | ABOVE_50_AND_200 |
| XLE | energy | -0.90 | -1.82 | -0.61 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.84 | -3.93 | -2.21 | BELOW_50_ABOVE_200 |
| XLP | defensives | -0.52 | -4.21 | -3.24 | BELOW_50_AND_200 |
| TLT | rates | -0.50 | -5.61 | -4.62 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -0.49 | -10.07 | -11.23 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.42 | -8.33 | -6.47 | BELOW_50_AND_200 |
| IWM | high_beta | -0.36 | -5.66 | -4.92 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
