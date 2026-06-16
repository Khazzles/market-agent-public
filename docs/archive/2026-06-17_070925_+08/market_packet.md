# Market Packet — 2026-06-17T07:09:25.646879+08:00

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
| SPY | 2026-06-16 | 750.33 | -0.60 | 1.80 | 1.51 | 3.26 | 9.16 | 57.05 | 1.28 | 0.00 | -1.44 | ABOVE_50_AND_200 |
| QQQ | 2026-06-16 | 729.86 | -1.90 | 3.11 | 2.95 | 6.11 | 16.41 | 56.34 | 2.14 | 1.44 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-16 | 600.21 | 1.13 | 2.67 | -2.28 | -3.62 | -8.58 | 48.80 | 3.21 | -3.79 | -5.23 | BELOW_50_AND_200 |
| AMZN | 2026-06-16 | 246.00 | -0.01 | 0.74 | -6.87 | -3.97 | 5.73 | 43.20 | 2.98 | -8.38 | -9.82 | BELOW_50_ABOVE_200 |
| MU | 2026-06-16 | 1020.76 | -6.18 | 9.07 | 40.86 | 44.80 | 161.03 | 60.48 | 7.61 | 39.35 | 37.91 | ABOVE_50_AND_200 |
| ORCL | 2026-06-16 | 188.33 | -2.24 | -8.49 | -2.39 | 0.84 | -8.30 | 44.73 | 6.88 | -3.90 | -5.35 | MIXED |
| SOFI | 2026-06-16 | 17.71 | 3.39 | 7.53 | 13.45 | 4.87 | -22.23 | 57.22 | 5.33 | 11.94 | 10.50 | MIXED |
| IAU | 2026-06-16 | 81.50 | 0.30 | 1.79 | -4.69 | -5.33 | -2.34 | 43.81 | 2.17 | -6.20 | -7.64 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-16 | 16.41 | 1.30 | -17.41 | -7.91 | -8.34 | BELOW_50_AND_200 |
| ^TNX | 2026-06-16 | 4.43 | -1.31 | -2.72 | -0.74 | 0.17 | ABOVE_50_AND_200 |
| CL=F | 2026-06-16 | 75.94 | -5.96 | -13.90 | -27.96 | -20.39 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-16 | 4355.40 | 0.63 | 2.24 | -4.40 | -4.81 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-16 | 99.54 | -0.09 | -0.37 | 0.27 | 0.67 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.94 | XLE, XOP, USO |
| semis_ai | -5.36 | SMH, SOXX |
| high_beta | -1.95 | IWM, ARKK, HIBL |
| rates | -0.35 | TLT, TBF, TBT |
| dollar | -0.14 | UUP |
| equity_hedges | 2.68 | SH, PSQ, SQQQ |
| housing_rates | 1.30 | XHB, ITB |
| defensives | 0.42 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 5.62 | -10.77 | -20.50 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 1.84 | -3.00 | -6.21 | BELOW_50_AND_200 |
| XHB | housing_rates | 1.39 | 14.04 | 5.89 | ABOVE_50_AND_200 |
| ITB | housing_rates | 1.21 | 13.66 | 4.57 | MIXED |
| XLU | defensives | 0.72 | 2.71 | -0.38 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | 0.58 | -1.13 | -2.86 | BELOW_50_AND_200 |
| TLT | rates | 0.55 | 3.02 | 0.62 | MIXED |
| XLP | defensives | 0.13 | 1.12 | 2.41 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | -5.92 | 16.27 | 18.79 | ABOVE_50_AND_200 |
| SMH | semis_ai | -4.81 | 10.72 | 14.42 | ABOVE_50_AND_200 |
| USO | energy | -4.74 | -22.10 | -14.28 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -4.28 | 27.41 | 25.35 | ABOVE_50_AND_200 |
| TBT | rates | -1.04 | -5.96 | -1.55 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.87 | 5.22 | 4.35 | ABOVE_50_AND_200 |
| XOP | energy | -0.75 | -9.74 | -7.00 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.69 | 5.58 | 3.26 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
