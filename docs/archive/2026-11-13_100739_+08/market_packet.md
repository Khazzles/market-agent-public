# Market Packet — 2026-11-13T10:07:39.285909+08:00

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
| SPY | 2026-11-11 | 759.81 | 1.32 | -0.91 | -2.34 | -0.67 | 3.90 | 49.86 | 1.44 | 0.00 | 4.81 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-11 | 690.38 | 2.31 | -0.23 | -7.15 | -3.99 | 1.27 | 46.06 | 2.36 | -4.81 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-11-11 | 628.77 | -1.97 | -0.20 | -17.54 | -7.34 | -0.43 | 43.36 | 3.65 | -15.20 | -10.39 | BELOW_50_AND_200 |
| AMZN | 2026-11-11 | 266.17 | -1.74 | 0.05 | 2.94 | 4.62 | 8.93 | 57.34 | 3.50 | 5.27 | 10.09 | ABOVE_50_AND_200 |
| MU | 2026-11-11 | 811.30 | 11.89 | 2.02 | -14.89 | -14.65 | 6.46 | 45.10 | 7.37 | -12.55 | -7.73 | BELOW_50_ABOVE_200 |
| ORCL | 2026-11-11 | 128.38 | 8.82 | 3.76 | -10.35 | -6.71 | -16.94 | 49.36 | 6.39 | -8.01 | -3.20 | BELOW_50_AND_200 |
| SOFI | 2026-11-11 | 16.27 | -0.61 | -6.39 | 6.76 | -0.06 | -6.56 | 50.81 | 5.05 | 9.10 | 13.91 | BELOW_50_AND_200 |
| IAU | 2026-11-11 | 74.87 | -1.15 | -1.96 | -4.32 | -4.64 | -10.85 | 43.18 | 1.97 | -1.98 | 2.83 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-12 | 18.70 | 6.92 | -33.64 | 10.85 | 8.61 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-12 | 5.10 | 2.10 | 5.50 | -1.68 | 1.03 | ABOVE_50_AND_200 |
| CL=F | 2026-11-12 | 88.09 | 1.80 | -2.68 | -7.36 | -7.67 | BELOW_50_ABOVE_200 |
| GC=F | 2026-11-12 | 3916.10 | -2.11 | -4.80 | -4.67 | -6.65 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-12 | 103.13 | 0.22 | 1.56 | 0.57 | 1.78 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.50 | XLE, XOP, USO |
| semis_ai | 5.42 | SMH, SOXX |
| high_beta | 4.04 | IWM, ARKK, HIBL |
| rates | -0.09 | TLT, TBF, TBT |
| dollar | 0.69 | UUP |
| equity_hedges | -3.50 | SH, PSQ, SQQQ |
| housing_rates | -0.42 | XHB, ITB |
| defensives | 0.33 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 9.46 | -28.35 | -20.54 | BELOW_50_AND_200 |
| SOXX | semis_ai | 6.01 | -14.29 | -9.91 | BELOW_50_AND_200 |
| SMH | semis_ai | 4.82 | -13.80 | -9.81 | BELOW_50_AND_200 |
| XOP | energy | 2.63 | -9.85 | -5.49 | BELOW_50_ABOVE_200 |
| XLE | energy | 1.86 | -5.70 | -2.50 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 1.78 | -9.98 | -7.78 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.89 | 2.31 | 0.59 | ABOVE_50_AND_200 |
| UUP | dollar | 0.69 | 1.14 | 2.10 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -6.91 | 19.30 | 7.48 | MIXED |
| PSQ | equity_hedges | -2.32 | 7.24 | 3.44 | MIXED |
| SH | equity_hedges | -1.27 | 2.61 | 0.68 | MIXED |
| ITB | housing_rates | -0.77 | 12.77 | 6.26 | MIXED |
| TBF | rates | -0.39 | -3.05 | -0.91 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -0.07 | 8.95 | 4.67 | MIXED |
| USO | energy | 0.01 | -7.59 | -7.32 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.05 | 3.25 | 0.76 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
