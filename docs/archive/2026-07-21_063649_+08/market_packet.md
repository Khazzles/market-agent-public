# Market Packet — 2026-07-21T06:36:49.318254+08:00

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
| SPY | 2026-07-20 | 742.09 | -0.16 | -0.94 | 0.15 | -0.33 | 6.46 | 47.52 | 1.13 | 0.00 | 3.81 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-20 | 696.06 | 0.10 | -2.20 | -3.66 | -3.19 | 8.54 | 42.34 | 2.15 | -3.81 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-20 | 645.85 | -0.02 | -1.66 | 13.79 | 6.72 | 0.90 | 56.76 | 3.98 | 13.64 | 17.45 | ABOVE_50_AND_200 |
| AMZN | 2026-07-20 | 249.99 | 1.12 | 1.08 | 5.26 | -0.65 | 6.74 | 54.04 | 2.98 | 5.11 | 8.92 | BELOW_50_ABOVE_200 |
| MU | 2026-07-20 | 865.46 | 1.94 | -7.63 | -17.04 | -7.70 | 77.87 | 42.50 | 9.61 | -17.19 | -13.38 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-20 | 121.38 | -3.98 | -7.72 | -33.86 | -31.51 | -36.36 | 27.14 | 6.86 | -34.02 | -30.20 | BELOW_50_AND_200 |
| SOFI | 2026-07-20 | 17.01 | -1.56 | -6.18 | -2.35 | -0.16 | -21.86 | 44.31 | 5.44 | -2.51 | 1.31 | BELOW_50_AND_200 |
| IAU | 2026-07-20 | 75.35 | -0.20 | 0.13 | -5.39 | -6.87 | -10.60 | 39.72 | 1.95 | -5.54 | -1.73 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-20 | 18.65 | -0.64 | 8.68 | 1.14 | 7.47 | MIXED |
| ^TNX | 2026-07-20 | 4.60 | 1.26 | -0.24 | 3.02 | 2.21 | ABOVE_50_AND_200 |
| CL=F | 2026-07-20 | 82.59 | 0.12 | 5.69 | 7.55 | -2.98 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-20 | 4013.00 | 0.01 | 0.40 | -7.94 | -6.77 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-20 | 101.00 | 0.25 | -0.28 | 0.91 | 1.00 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.54 | XLE, XOP, USO |
| semis_ai | 0.43 | SMH, SOXX |
| high_beta | -0.94 | IWM, ARKK, HIBL |
| rates | 0.55 | TLT, TBF, TBT |
| dollar | 0.21 | UUP |
| equity_hedges | -0.06 | SH, PSQ, SQQQ |
| housing_rates | -1.99 | XHB, ITB |
| defensives | -0.45 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | 1.62 | 5.25 | 2.77 | ABOVE_50_AND_200 |
| USO | energy | 1.25 | 9.87 | -0.13 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.77 | 2.42 | 1.39 | ABOVE_50_AND_200 |
| XLE | energy | 0.45 | 5.98 | 2.47 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.45 | -12.60 | -7.51 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.41 | -10.44 | -6.47 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.21 | 0.75 | 1.28 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.15 | -0.83 | 0.07 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XHB | housing_rates | -2.01 | -1.17 | 0.07 | MIXED |
| ITB | housing_rates | -1.97 | -0.40 | -0.19 | BELOW_50_AND_200 |
| HIBL | high_beta | -1.89 | -22.08 | -16.16 | BELOW_50_ABOVE_200 |
| TLT | rates | -0.75 | -2.83 | -1.60 | BELOW_50_AND_200 |
| IWM | high_beta | -0.59 | 0.84 | 0.66 | ABOVE_50_AND_200 |
| XLU | defensives | -0.51 | 1.08 | 0.19 | ABOVE_50_AND_200 |
| XLP | defensives | -0.39 | 1.41 | 0.81 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.33 | -4.51 | -4.15 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
