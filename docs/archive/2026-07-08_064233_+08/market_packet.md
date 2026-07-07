# Market Packet — 2026-07-08T06:42:33.207033+08:00

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
| SPY | 2026-07-07 | 747.71 | -0.48 | 0.91 | -1.24 | 1.18 | 7.87 | 54.74 | 1.30 | 0.00 | 2.97 | ABOVE_50_AND_200 |
| QQQ | 2026-07-07 | 709.43 | -1.85 | -2.02 | -4.21 | -0.31 | 11.51 | 47.13 | 2.32 | -2.97 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-07 | 615.58 | 2.55 | 9.42 | -1.91 | 2.11 | -4.53 | 57.43 | 3.68 | -0.67 | 2.30 | MIXED |
| AMZN | 2026-07-07 | 245.98 | 0.75 | 2.43 | -3.08 | -3.54 | 5.52 | 51.72 | 3.20 | -1.84 | 1.13 | BELOW_50_ABOVE_200 |
| MU | 2026-07-07 | 938.38 | -4.71 | -18.07 | -5.79 | 7.72 | 107.44 | 46.26 | 9.92 | -4.55 | -1.58 | ABOVE_50_AND_200 |
| ORCL | 2026-07-07 | 141.60 | -1.50 | -4.17 | -40.09 | -23.38 | -28.58 | 29.17 | 6.83 | -38.85 | -35.88 | BELOW_50_AND_200 |
| SOFI | 2026-07-07 | 17.75 | -4.62 | -2.42 | 3.50 | 5.32 | -20.18 | 52.66 | 5.39 | 4.74 | 7.71 | MIXED |
| IAU | 2026-07-07 | 77.37 | -1.19 | 2.44 | -8.20 | -6.60 | -7.94 | 42.30 | 2.12 | -6.96 | -3.99 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-07 | 16.13 | 3.60 | -8.61 | 4.74 | -8.07 | BELOW_50_AND_200 |
| ^TNX | 2026-07-07 | 4.53 | 0.98 | 3.59 | 0.85 | 1.53 | ABOVE_50_AND_200 |
| CL=F | 2026-07-07 | 72.37 | 5.57 | 2.29 | -22.22 | -19.03 | BELOW_50_AND_200 |
| GC=F | 2026-07-07 | 4110.90 | -1.06 | 2.20 | -8.15 | -6.70 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-07 | 101.12 | 0.27 | 0.01 | 1.72 | 1.58 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 3.14 | XLE, XOP, USO |
| semis_ai | -4.45 | SMH, SOXX |
| high_beta | -4.27 | IWM, ARKK, HIBL |
| rates | 0.73 | TLT, TBF, TBT |
| dollar | 0.28 | UUP |
| equity_hedges | 2.62 | SH, PSQ, SQQQ |
| housing_rates | -1.56 | XHB, ITB |
| defensives | 0.89 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 5.49 | 6.94 | -4.33 | BELOW_50_AND_200 |
| USO | energy | 4.38 | -20.35 | -16.20 | BELOW_50_ABOVE_200 |
| XLE | energy | 2.84 | -7.00 | -3.92 | BELOW_50_ABOVE_200 |
| TBT | rates | 2.23 | 1.57 | 1.35 | ABOVE_50_AND_200 |
| XOP | energy | 2.21 | -7.99 | -5.03 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 1.88 | 3.05 | -0.68 | BELOW_50_AND_200 |
| TBF | rates | 1.02 | 0.53 | 0.53 | ABOVE_50_AND_200 |
| XLP | defensives | 0.90 | 3.44 | 0.98 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -9.01 | -16.12 | -2.82 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -5.13 | -8.47 | 0.15 | ABOVE_50_AND_200 |
| SMH | semis_ai | -3.78 | -7.34 | -0.44 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.89 | 1.40 | 4.28 | ABOVE_50_AND_200 |
| XHB | housing_rates | -1.69 | 4.48 | 3.66 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.42 | 6.95 | 4.75 | ABOVE_50_AND_200 |
| TLT | rates | -1.05 | -1.11 | -1.17 | BELOW_50_AND_200 |
| IWM | high_beta | -0.91 | 1.43 | 3.04 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
