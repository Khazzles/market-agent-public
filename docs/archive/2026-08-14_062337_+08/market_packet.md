# Market Packet — 2026-08-14T06:23:37.880827+08:00

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
| SPY | 2026-08-13 | 777.88 | 0.70 | 1.21 | 3.06 | 3.93 | 10.34 | 67.36 | 1.02 | 0.00 | 1.06 | ABOVE_50_AND_200 |
| QQQ | 2026-08-13 | 732.07 | 1.16 | 2.44 | 2.00 | 2.64 | 12.61 | 60.12 | 1.80 | -1.06 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-13 | 594.97 | 2.78 | 0.86 | -12.67 | -0.47 | -5.33 | 49.15 | 3.75 | -15.73 | -14.67 | BELOW_50_AND_200 |
| AMZN | 2026-08-13 | 265.13 | -0.80 | -2.62 | 3.99 | 6.94 | 11.62 | 55.41 | 3.22 | 0.93 | 1.99 | ABOVE_50_AND_200 |
| MU | 2026-08-13 | 949.83 | 4.23 | 7.76 | 5.04 | -1.35 | 73.06 | 54.46 | 7.97 | 1.98 | 3.04 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-13 | 156.22 | 1.92 | 8.89 | 17.91 | 1.47 | -11.63 | 61.41 | 4.85 | 14.85 | 15.91 | MIXED |
| SOFI | 2026-08-13 | 18.43 | 2.73 | 1.82 | 3.13 | 5.57 | -11.72 | 56.61 | 4.47 | 0.08 | 1.14 | MIXED |
| IAU | 2026-08-13 | 81.78 | -1.45 | 2.39 | 7.21 | 4.62 | -3.15 | 61.76 | 1.79 | 4.15 | 5.21 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-13 | 14.63 | 0.55 | -3.43 | -2.66 | -14.77 | BELOW_50_AND_200 |
| ^TNX | 2026-08-13 | 4.64 | -0.88 | -0.62 | UNK | UNK | UNK |
| CL=F | 2026-08-13 | 81.07 | -2.64 | 4.89 | 1.85 | 1.57 | ABOVE_50_AND_200 |
| GC=F | 2026-08-13 | 4411.20 | 0.05 | 3.99 | 9.08 | 6.04 | MIXED |
| DX-Y.NYB | 2026-08-13 | 99.95 | -0.06 | -0.02 | -1.01 | -0.50 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.47 | XLE, XOP, USO |
| semis_ai | 0.74 | SMH, SOXX |
| high_beta | 1.18 | IWM, ARKK, HIBL |
| rates | -0.43 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | -1.70 | SH, PSQ, SQQQ |
| housing_rates | 1.24 | XHB, ITB |
| defensives | 0.77 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 1.79 | -0.18 | 2.31 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.50 | 3.86 | 6.52 | ABOVE_50_AND_200 |
| ITB | housing_rates | 1.39 | 1.81 | 1.61 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.09 | 0.85 | 0.94 | ABOVE_50_AND_200 |
| XLP | defensives | 1.08 | 3.03 | 1.78 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.76 | -0.82 | -2.24 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.73 | -0.28 | -0.57 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.58 | -1.96 | -2.29 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.43 | -7.45 | -10.34 | BELOW_50_AND_200 |
| USO | energy | -1.78 | 3.01 | 3.64 | ABOVE_50_AND_200 |
| TBT | rates | -1.20 | 4.52 | 4.53 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.06 | -1.87 | -2.82 | BELOW_50_AND_200 |
| TBF | rates | -0.67 | 2.35 | 2.32 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.62 | -2.57 | -3.63 | BELOW_50_AND_200 |
| UUP | dollar | -0.07 | -0.25 | -0.31 | BELOW_50_ABOVE_200 |
| XLE | energy | 0.05 | 8.07 | 7.30 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
