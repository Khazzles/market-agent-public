# Market Packet — 2026-06-11T20:31:46.867846+08:00

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
| SPY | 2026-06-10 | 725.43 | -1.58 | -3.82 | -1.88 | 0.85 | 5.85 | 40.72 | 1.26 | 0.00 | 0.87 | ABOVE_50_AND_200 |
| QQQ | 2026-06-10 | 693.69 | -2.00 | -6.79 | -2.75 | 2.58 | 11.19 | 43.41 | 2.10 | -0.87 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-10 | 570.98 | -2.33 | -8.35 | -4.66 | -8.22 | -13.48 | 35.69 | 3.35 | -2.78 | -1.91 | BELOW_50_AND_200 |
| AMZN | 2026-06-10 | 238.00 | -2.53 | -4.81 | -11.52 | -6.13 | 2.41 | 32.46 | 3.07 | -9.64 | -8.77 | BELOW_50_ABOVE_200 |
| MU | 2026-06-10 | 891.88 | -4.70 | -17.39 | 12.14 | 36.75 | 139.12 | 55.46 | 8.19 | 14.02 | 14.89 | ABOVE_50_AND_200 |
| ORCL | 2026-06-10 | 201.26 | -2.21 | -12.62 | 3.83 | 9.70 | -2.47 | 49.43 | 6.54 | 5.70 | 6.58 | MIXED |
| SOFI | 2026-06-10 | 15.87 | -3.64 | -4.86 | -2.40 | -5.52 | -30.84 | 44.56 | 6.08 | -0.52 | 0.35 | BELOW_50_AND_200 |
| IAU | 2026-06-10 | 76.79 | -4.10 | -8.13 | -13.78 | -11.46 | -7.63 | 24.17 | 2.24 | -11.90 | -11.03 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-11 | 20.76 | -6.57 | 34.81 | 16.17 | 12.82 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-10 | 4.54 | 0.31 | 1.14 | 2.99 | 2.95 | ABOVE_50_AND_200 |
| CL=F | 2026-06-11 | 89.50 | -0.59 | -3.80 | -12.41 | -7.81 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-11 | 4098.20 | -0.24 | -8.44 | -12.39 | -10.89 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-11 | 100.08 | 0.13 | 0.67 | 1.82 | 1.19 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.06 | XLE, XOP, USO |
| semis_ai | -3.54 | SMH, SOXX |
| high_beta | -5.23 | IWM, ARKK, HIBL |
| rates | 0.26 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | 3.22 | SH, PSQ, SQQQ |
| housing_rates | -3.05 | XHB, ITB |
| defensives | 0.85 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 6.05 | 7.18 | -11.88 | BELOW_50_AND_200 |
| XOP | energy | 2.40 | -0.40 | -1.41 | BELOW_50_ABOVE_200 |
| USO | energy | 2.28 | -3.14 | -0.85 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 2.01 | 2.87 | -2.95 | BELOW_50_AND_200 |
| XLP | defensives | 1.65 | 2.54 | 2.64 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.60 | 2.33 | -0.55 | BELOW_50_AND_200 |
| XLE | energy | 1.50 | 1.89 | 0.59 | ABOVE_50_AND_200 |
| TBT | rates | 0.78 | 1.42 | 1.68 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -11.99 | -9.38 | 3.02 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -3.67 | 1.64 | 13.60 | ABOVE_50_AND_200 |
| SMH | semis_ai | -3.40 | -0.94 | 9.83 | ABOVE_50_AND_200 |
| XHB | housing_rates | -3.31 | 1.86 | 0.50 | MIXED |
| ITB | housing_rates | -2.78 | 2.30 | 0.17 | MIXED |
| ARKK | high_beta | -2.65 | -8.77 | -3.75 | BELOW_50_AND_200 |
| IWM | high_beta | -1.04 | -1.15 | 1.99 | ABOVE_50_AND_200 |
| TLT | rates | -0.28 | -0.79 | -0.97 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
