# Market Packet — 2026-10-16T07:51:23.717907+08:00

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
| SPY | 2026-10-15 | 771.79 | 0.28 | -0.28 | 2.35 | 0.41 | 6.51 | 51.80 | 0.85 | 0.00 | -0.95 | ABOVE_50_AND_200 |
| QQQ | 2026-10-15 | 728.00 | -0.13 | -2.62 | 3.30 | 0.16 | 7.94 | 44.09 | 1.34 | 0.95 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-15 | 736.72 | -0.11 | 2.20 | 9.42 | 12.85 | 16.61 | 57.86 | 3.32 | 7.07 | 6.11 | ABOVE_50_AND_200 |
| AMZN | 2026-10-15 | 254.76 | 0.27 | 0.28 | 3.58 | -1.07 | 4.99 | 50.10 | 2.31 | 1.23 | 0.27 | BELOW_50_ABOVE_200 |
| MU | 2026-10-15 | 931.24 | 1.87 | -10.10 | 0.51 | -5.28 | 30.26 | 39.16 | 5.22 | -1.85 | -2.80 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-15 | 134.47 | 3.00 | -0.90 | -6.07 | -7.53 | -16.24 | 43.99 | 5.29 | -8.42 | -9.37 | BELOW_50_AND_200 |
| SOFI | 2026-10-15 | 15.09 | 6.12 | -3.33 | -10.39 | -12.08 | -18.12 | 38.73 | 4.28 | -12.74 | -13.70 | BELOW_50_AND_200 |
| IAU | 2026-10-15 | 78.47 | 1.82 | 1.04 | -2.30 | -3.67 | -7.74 | 46.11 | 1.62 | -4.66 | -5.61 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-15 | 16.46 | -2.43 | 6.81 | -7.06 | 6.20 | MIXED |
| ^TNX | 2026-10-15 | 5.09 | -1.95 | -2.71 | 1.66 | 3.11 | ABOVE_50_AND_200 |
| CL=F | 2026-10-15 | 96.13 | 1.09 | 5.07 | -6.15 | 6.26 | ABOVE_50_AND_200 |
| GC=F | 2026-10-15 | 4177.10 | 1.68 | 0.48 | -4.80 | -4.57 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-15 | 102.04 | -0.49 | -0.09 | 1.73 | 1.73 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.21 | XLE, XOP, USO |
| semis_ai | -0.98 | SMH, SOXX |
| high_beta | 1.09 | IWM, ARKK, HIBL |
| rates | -1.05 | TLT, TBF, TBT |
| dollar | -0.41 | UUP |
| equity_hedges | 0.09 | SH, PSQ, SQQQ |
| housing_rates | 3.58 | XHB, ITB |
| defensives | 0.28 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 4.03 | -1.55 | -5.46 | BELOW_50_AND_200 |
| XHB | housing_rates | 3.13 | -1.08 | -5.15 | BELOW_50_AND_200 |
| USO | energy | 2.44 | 0.73 | 10.92 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.43 | 3.02 | -0.06 | BELOW_50_ABOVE_200 |
| TLT | rates | 1.37 | -1.13 | -1.00 | BELOW_50_AND_200 |
| IWM | high_beta | 1.37 | -3.11 | -5.02 | BELOW_50_AND_200 |
| XLP | defensives | 0.72 | 4.02 | 3.14 | ABOVE_50_AND_200 |
| HIBL | high_beta | 0.47 | 2.10 | -11.53 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | -2.94 | 1.22 | 1.05 | ABOVE_50_AND_200 |
| TBF | rates | -1.59 | 0.50 | 0.43 | ABOVE_50_AND_200 |
| XLE | energy | -1.58 | 3.95 | 5.09 | ABOVE_50_AND_200 |
| XOP | energy | -1.49 | 1.61 | 4.25 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.04 | 2.43 | -3.59 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -0.91 | 2.52 | -4.35 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.41 | 2.11 | 2.15 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.25 | -2.99 | -0.63 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
