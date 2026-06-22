# Market Packet — 2026-06-23T07:05:47.560014+08:00

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
| SPY | 2026-06-22 | 744.39 | -0.31 | 0.36 | 0.42 | 1.84 | 8.06 | 52.54 | 1.28 | 0.00 | -3.05 | ABOVE_50_AND_200 |
| QQQ | 2026-06-22 | 737.95 | -0.36 | 2.30 | 3.48 | 6.07 | 17.23 | 57.96 | 2.10 | 3.05 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-22 | 563.85 | -2.32 | -0.55 | -6.81 | -9.15 | -13.79 | 39.38 | 3.53 | -7.23 | -10.29 | BELOW_50_AND_200 |
| AMZN | 2026-06-22 | 232.79 | -4.75 | -2.41 | -12.16 | -9.45 | -0.02 | 36.54 | 3.44 | -12.58 | -15.64 | BELOW_50_AND_200 |
| MU | 2026-06-22 | 1211.38 | 6.82 | 23.41 | 65.49 | 61.82 | 198.21 | 69.77 | 6.59 | 65.07 | 62.01 | ABOVE_50_AND_200 |
| ORCL | 2026-06-22 | 175.07 | -5.00 | -4.92 | -6.96 | -7.43 | -14.48 | 39.02 | 7.00 | -7.38 | -10.43 | BELOW_50_AND_200 |
| SOFI | 2026-06-22 | 17.10 | -4.52 | 3.14 | 8.99 | 0.84 | -24.54 | 51.63 | 5.59 | 8.56 | 5.51 | MIXED |
| IAU | 2026-06-22 | 78.80 | -0.67 | -0.49 | -7.87 | -7.83 | -5.80 | 36.76 | 2.24 | -8.29 | -11.35 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-22 | 17.28 | 5.37 | -2.26 | 3.10 | -2.65 | BELOW_50_AND_200 |
| ^TNX | 2026-06-22 | 4.51 | 1.30 | 0.49 | -1.38 | 1.71 | ABOVE_50_AND_200 |
| CL=F | 2026-06-22 | 74.29 | -3.02 | -12.48 | -24.39 | -20.84 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-22 | 4208.50 | -0.37 | -0.15 | -7.12 | -7.44 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-22 | 101.00 | 0.14 | 1.25 | 1.90 | 2.05 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.12 | XLE, XOP, USO |
| semis_ai | 1.90 | SMH, SOXX |
| high_beta | 1.08 | IWM, ARKK, HIBL |
| rates | 0.51 | TLT, TBF, TBT |
| dollar | 0.21 | UUP |
| equity_hedges | 0.34 | SH, PSQ, SQQQ |
| housing_rates | -1.82 | XHB, ITB |
| defensives | -0.72 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.55 | 41.99 | 33.01 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 2.43 | 25.89 | 27.52 | ABOVE_50_AND_200 |
| TBT | rates | 1.47 | -5.18 | -1.23 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.37 | 18.46 | 21.10 | ABOVE_50_AND_200 |
| XOP | energy | 1.00 | -11.35 | -7.74 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.88 | 6.54 | 5.71 | ABOVE_50_AND_200 |
| TBF | rates | 0.83 | -2.55 | -0.39 | BELOW_50_ABOVE_200 |
| XLE | energy | 0.54 | -9.60 | -5.78 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -2.19 | 3.42 | 1.64 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.92 | 7.99 | 3.25 | MIXED |
| USO | energy | -1.90 | -21.89 | -15.75 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -1.72 | 10.32 | 4.72 | ABOVE_50_AND_200 |
| XLP | defensives | -1.34 | -3.91 | -1.71 | BELOW_50_ABOVE_200 |
| TLT | rates | -0.76 | 2.60 | 0.53 | MIXED |
| XLU | defensives | -0.09 | 0.47 | -0.85 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 0.16 | -3.59 | -6.13 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
