# Market Packet — 2026-08-04T06:38:42.645593+08:00

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
| SPY | 2026-08-03 | 757.67 | 1.42 | 2.51 | 1.73 | 1.66 | 8.11 | 59.50 | 1.22 | 0.00 | 3.49 | ABOVE_50_AND_200 |
| QQQ | 2026-08-03 | 700.07 | 1.76 | 2.63 | -1.76 | -2.06 | 8.45 | 50.02 | 2.19 | -3.49 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-03 | 590.24 | 6.02 | -0.61 | 1.26 | -1.94 | -6.89 | 46.96 | 4.45 | -0.47 | 3.02 | BELOW_50_AND_200 |
| AMZN | 2026-08-03 | 284.02 | 4.58 | 22.75 | 17.04 | 14.98 | 20.68 | 72.23 | 3.50 | 15.31 | 18.80 | ABOVE_50_AND_200 |
| MU | 2026-08-03 | 829.50 | 0.79 | -7.85 | -14.97 | -14.20 | 59.12 | 44.07 | 10.71 | -16.70 | -13.21 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-03 | 141.85 | 9.22 | 18.31 | 1.13 | -13.50 | -22.20 | 53.25 | 5.73 | -0.60 | 2.88 | BELOW_50_AND_200 |
| SOFI | 2026-08-03 | 18.03 | 10.55 | 6.81 | -1.15 | 4.60 | -15.20 | 55.59 | 5.44 | -2.88 | 0.61 | MIXED |
| IAU | 2026-08-03 | 76.19 | 0.03 | -0.77 | -1.70 | -3.28 | -9.69 | 45.96 | 1.84 | -3.43 | 0.06 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-03 | 15.86 | -0.81 | -15.05 | -1.80 | -8.64 | BELOW_50_AND_200 |
| ^TNX | 2026-08-03 | 4.69 | -1.24 | 0.97 | 4.48 | 3.43 | ABOVE_50_AND_200 |
| CL=F | 2026-08-03 | 80.00 | -5.52 | -3.16 | 16.47 | -2.25 | BELOW_50_ABOVE_200 |
| GC=F | 2026-08-03 | 4107.50 | 1.44 | 0.81 | -0.13 | -2.03 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-08-03 | 99.99 | 0.19 | -1.50 | -0.86 | -0.45 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.83 | XLE, XOP, USO |
| semis_ai | 0.73 | SMH, SOXX |
| high_beta | 4.20 | IWM, ARKK, HIBL |
| rates | -0.38 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -2.81 | SH, PSQ, SQQQ |
| housing_rates | 2.70 | XHB, ITB |
| defensives | -0.10 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 7.65 | -11.68 | -11.41 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 3.23 | -9.49 | -5.04 | BELOW_50_AND_200 |
| ITB | housing_rates | 2.83 | -5.72 | 0.08 | MIXED |
| XHB | housing_rates | 2.58 | -5.51 | -1.04 | BELOW_50_AND_200 |
| IWM | high_beta | 1.72 | -0.46 | 1.16 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.91 | -7.91 | -8.45 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 0.55 | -10.35 | -10.53 | BELOW_50_ABOVE_200 |
| XLU | defensives | 0.02 | -3.06 | -1.39 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -5.46 | 17.45 | -0.60 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -5.26 | 3.70 | 2.45 | MIXED |
| XOP | energy | -1.76 | 12.70 | 6.03 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.75 | 1.82 | 1.56 | MIXED |
| SH | equity_hedges | -1.42 | -1.30 | -1.68 | BELOW_50_AND_200 |
| XLE | energy | -1.28 | 10.47 | 3.78 | ABOVE_50_AND_200 |
| TBT | rates | -0.73 | 7.95 | 5.68 | ABOVE_50_AND_200 |
| TBF | rates | -0.35 | 4.31 | 2.98 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
