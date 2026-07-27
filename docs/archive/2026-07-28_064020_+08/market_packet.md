# Market Packet — 2026-07-28T06:40:20.453408+08:00

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
| SPY | 2026-07-27 | 739.09 | 0.12 | -0.56 | 0.80 | -0.80 | 5.80 | 45.37 | 1.13 | 0.00 | 4.81 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-27 | 682.12 | -1.42 | -1.90 | -4.01 | -5.03 | 6.06 | 38.65 | 2.14 | -4.81 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-27 | 593.87 | -2.02 | -8.07 | 6.49 | -2.01 | -6.93 | 43.54 | 4.15 | 5.69 | 10.50 | BELOW_50_AND_200 |
| AMZN | 2026-07-27 | 231.39 | -0.97 | -6.41 | -1.23 | -7.15 | -1.36 | 36.99 | 3.16 | -2.03 | 2.78 | BELOW_50_AND_200 |
| MU | 2026-07-27 | 900.20 | -9.09 | 6.04 | -14.14 | -5.74 | 79.34 | 45.73 | 9.39 | -14.94 | -10.13 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-27 | 119.90 | -0.12 | -5.15 | -23.89 | -30.15 | -36.03 | 29.57 | 6.33 | -24.69 | -19.88 | BELOW_50_AND_200 |
| SOFI | 2026-07-27 | 16.88 | 1.38 | -2.31 | -2.48 | -1.42 | -21.83 | 44.62 | 5.14 | -3.28 | 1.53 | BELOW_50_AND_200 |
| IAU | 2026-07-27 | 76.78 | 0.83 | 1.70 | 2.39 | -3.97 | -8.98 | 47.04 | 1.88 | 1.59 | 6.40 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-27 | 18.67 | -0.16 | -0.53 | 0.21 | 7.63 | MIXED |
| ^TNX | 2026-07-27 | 4.64 | -1.32 | 2.20 | 5.43 | 2.71 | ABOVE_50_AND_200 |
| CL=F | 2026-07-27 | 81.98 | -8.21 | -1.50 | 13.99 | -2.43 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-27 | 4074.20 | 0.16 | 1.59 | 1.08 | -3.96 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-27 | 101.51 | 0.08 | 0.76 | -0.09 | 1.26 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -5.34 | XLE, XOP, USO |
| semis_ai | -5.90 | SMH, SOXX |
| high_beta | -1.72 | IWM, ARKK, HIBL |
| rates | -0.24 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | 2.00 | SH, PSQ, SQQQ |
| housing_rates | 3.01 | XHB, ITB |
| defensives | 0.74 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.51 | 11.79 | 12.62 | MIXED |
| ITB | housing_rates | 3.64 | -5.17 | 2.18 | MIXED |
| XLP | defensives | 2.58 | 1.09 | 1.38 | ABOVE_50_AND_200 |
| XHB | housing_rates | 2.39 | -4.41 | 2.63 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.58 | 4.35 | 4.74 | MIXED |
| TLT | rates | 0.70 | -4.15 | -1.58 | BELOW_50_AND_200 |
| IWM | high_beta | 0.28 | -1.27 | 0.58 | ABOVE_50_AND_200 |
| UUP | dollar | 0.14 | 0.25 | 1.70 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -10.56 | 17.38 | -0.31 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -6.35 | -14.18 | -9.27 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -5.45 | -11.37 | -8.37 | BELOW_50_ABOVE_200 |
| XOP | energy | -3.75 | 10.49 | 2.84 | ABOVE_50_AND_200 |
| HIBL | high_beta | -3.67 | -21.23 | -14.99 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -1.76 | -5.46 | -6.88 | BELOW_50_AND_200 |
| XLE | energy | -1.72 | 8.94 | 2.89 | ABOVE_50_AND_200 |
| XLU | defensives | -1.10 | 0.31 | 1.72 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
