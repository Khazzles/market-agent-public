# Market Packet — 2026-10-22T08:13:03.436820+08:00

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
| SPY | 2026-10-20 | 769.05 | 0.34 | -1.15 | -0.58 | 0.10 | 5.95 | 49.68 | 0.91 | 0.00 | 2.64 | ABOVE_50_AND_200 |
| QQQ | 2026-10-20 | 717.63 | -0.10 | -3.49 | -3.22 | -1.24 | 6.17 | 40.79 | 1.52 | -2.64 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-20 | 694.25 | -1.59 | -8.95 | -6.34 | 5.27 | 9.78 | 46.40 | 3.53 | -5.77 | -3.13 | ABOVE_50_AND_200 |
| AMZN | 2026-10-20 | 262.63 | 0.07 | 1.57 | 1.62 | 2.38 | 8.05 | 57.41 | 2.40 | 2.19 | 4.83 | ABOVE_50_AND_200 |
| MU | 2026-10-20 | 896.07 | -0.98 | -5.99 | -14.17 | -8.97 | 23.79 | 37.46 | 5.31 | -13.59 | -10.95 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-20 | 131.14 | 1.20 | -8.42 | -11.73 | -9.16 | -17.80 | 42.62 | 5.17 | -11.15 | -8.51 | BELOW_50_AND_200 |
| SOFI | 2026-10-20 | 14.68 | 2.66 | -3.67 | -13.49 | -13.35 | -19.55 | 37.99 | 4.54 | -12.92 | -10.28 | BELOW_50_AND_200 |
| IAU | 2026-10-20 | 77.44 | -0.53 | -1.04 | -5.18 | -4.69 | -8.89 | 41.89 | 1.45 | -4.60 | -1.96 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-21 | 16.68 | -3.64 | -1.13 | 17.38 | 5.95 | MIXED |
| ^TNX | 2026-10-21 | 5.15 | 0.57 | -0.85 | 3.58 | 3.52 | ABOVE_50_AND_200 |
| CL=F | 2026-10-21 | 98.09 | -3.63 | 3.15 | 3.70 | 6.41 | ABOVE_50_AND_200 |
| GC=F | 2026-10-21 | 4139.70 | -0.07 | 0.77 | -5.41 | -5.01 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-21 | 101.69 | -0.04 | -0.84 | 1.09 | 1.22 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.14 | XLE, XOP, USO |
| semis_ai | -0.38 | SMH, SOXX |
| high_beta | 1.62 | IWM, ARKK, HIBL |
| rates | -0.66 | TLT, TBF, TBT |
| dollar | -0.34 | UUP |
| equity_hedges | 0.12 | SH, PSQ, SQQQ |
| housing_rates | 2.51 | XHB, ITB |
| defensives | 0.94 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 2.80 | -1.00 | -4.02 | BELOW_50_AND_200 |
| XHB | housing_rates | 2.22 | -0.76 | -3.88 | BELOW_50_AND_200 |
| HIBL | high_beta | 1.86 | -20.68 | -16.50 | BELOW_50_AND_200 |
| IWM | high_beta | 1.66 | -3.43 | -4.24 | BELOW_50_AND_200 |
| ARKK | high_beta | 1.35 | -8.05 | -2.98 | BELOW_50_ABOVE_200 |
| XLU | defensives | 1.26 | 3.00 | -0.16 | BELOW_50_AND_200 |
| TLT | rates | 0.84 | -2.04 | -0.62 | BELOW_50_AND_200 |
| XLP | defensives | 0.62 | 7.12 | 4.23 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | -1.90 | 3.24 | 0.41 | ABOVE_50_AND_200 |
| TBF | rates | -0.92 | 1.56 | 0.34 | ABOVE_50_AND_200 |
| SMH | semis_ai | -0.38 | -8.33 | -5.46 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -0.38 | -10.61 | -6.70 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.34 | 1.47 | 1.62 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.25 | 0.19 | -0.21 | BELOW_50_AND_200 |
| USO | energy | -0.12 | 8.40 | 11.35 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.20 | 2.68 | 0.95 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
