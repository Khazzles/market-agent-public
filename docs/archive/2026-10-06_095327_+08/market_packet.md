# Market Packet — 2026-10-06T09:53:27.175775+08:00

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
| SPY | 2026-10-05 | 774.83 | 0.67 | 1.20 | 0.21 | 1.36 | 7.47 | 58.83 | 0.88 | 0.00 | -5.15 | ABOVE_50_AND_200 |
| QQQ | 2026-10-05 | 756.20 | 0.88 | 2.67 | 5.37 | 5.28 | 12.98 | 68.44 | 1.24 | 5.15 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-05 | 741.90 | 1.90 | 3.67 | 21.49 | 18.14 | 17.99 | 63.96 | 3.37 | 21.27 | 16.12 | ABOVE_50_AND_200 |
| AMZN | 2026-10-05 | 251.40 | -0.05 | 2.13 | -2.90 | -2.15 | 4.10 | 48.41 | 2.20 | -3.11 | -8.27 | BELOW_50_ABOVE_200 |
| MU | 2026-10-05 | 1063.96 | -1.02 | 0.95 | 11.04 | 10.96 | 55.15 | 57.26 | 4.19 | 10.83 | 5.67 | ABOVE_50_AND_200 |
| ORCL | 2026-10-05 | 142.48 | 0.13 | 7.45 | -7.50 | -1.15 | -12.40 | 48.51 | 4.70 | -7.72 | -12.87 | BELOW_50_AND_200 |
| SOFI | 2026-10-05 | 15.92 | 0.95 | -0.06 | -13.99 | -8.73 | -15.72 | 38.47 | 3.93 | -14.21 | -19.36 | BELOW_50_AND_200 |
| IAU | 2026-10-05 | 77.82 | -0.17 | 0.41 | -7.47 | -4.24 | -8.72 | 38.33 | 1.75 | -7.68 | -12.84 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-05 | 15.52 | 1.37 | -3.42 | 6.81 | -1.28 | BELOW_50_AND_200 |
| ^TNX | 2026-10-05 | 5.31 | 0.64 | 1.35 | 11.53 | 9.63 | ABOVE_50_AND_200 |
| CL=F | 2026-10-05 | 89.47 | -1.80 | -3.38 | -2.00 | 1.01 | ABOVE_50_AND_200 |
| GC=F | 2026-10-05 | 4160.10 | -0.05 | -0.20 | -8.37 | -4.76 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-05 | 102.08 | 0.15 | 0.87 | 3.12 | 2.07 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.02 | XLE, XOP, USO |
| semis_ai | 0.31 | SMH, SOXX |
| high_beta | 1.72 | IWM, ARKK, HIBL |
| rates | 0.33 | TLT, TBF, TBT |
| dollar | 0.35 | UUP |
| equity_hedges | -1.39 | SH, PSQ, SQQQ |
| housing_rates | -0.82 | XHB, ITB |
| defensives | 0.49 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | 3.28 | 6.47 | 11.20 | ABOVE_50_AND_200 |
| XOP | energy | 1.36 | -2.54 | 2.21 | ABOVE_50_AND_200 |
| HIBL | high_beta | 1.22 | 16.75 | 13.94 | ABOVE_50_AND_200 |
| XLE | energy | 1.00 | -1.81 | 2.02 | ABOVE_50_AND_200 |
| TBT | rates | 0.94 | 12.23 | 10.39 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.66 | -4.00 | -3.09 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.63 | -4.95 | -3.89 | BELOW_50_AND_200 |
| SMH | semis_ai | 0.52 | 14.71 | 10.96 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -2.63 | -15.88 | -15.87 | BELOW_50_AND_200 |
| USO | energy | -2.29 | 1.34 | 4.71 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.22 | -8.59 | -8.75 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.90 | -5.78 | -5.56 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.65 | -0.90 | -1.75 | BELOW_50_AND_200 |
| TLT | rates | -0.48 | -6.04 | -5.44 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.41 | -5.84 | -6.44 | BELOW_50_AND_200 |
| SOXX | semis_ai | 0.10 | 17.39 | 11.02 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
