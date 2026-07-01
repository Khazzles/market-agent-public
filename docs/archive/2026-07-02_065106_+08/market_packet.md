# Market Packet — 2026-07-02T06:51:06.483888+08:00

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
| SPY | 2026-07-01 | 745.76 | -0.14 | 1.71 | -1.68 | 1.24 | 7.79 | 54.23 | 1.35 | 0.00 | 0.68 | ABOVE_50_AND_200 |
| QQQ | 2026-07-01 | 725.17 | -1.52 | 2.05 | -2.37 | 2.46 | 14.32 | 52.43 | 2.21 | -0.68 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-01 | 612.91 | 8.81 | 9.91 | 2.07 | 0.98 | -5.33 | 58.45 | 3.55 | 3.76 | 4.44 | MIXED |
| AMZN | 2026-07-01 | 241.70 | 1.41 | 3.17 | -7.49 | -5.42 | 3.77 | 47.85 | 3.48 | -5.80 | -5.12 | BELOW_50_ABOVE_200 |
| MU | 2026-07-01 | 1032.28 | -10.57 | -1.55 | -0.31 | 22.66 | 134.47 | 51.79 | 9.26 | 1.37 | 2.05 | ABOVE_50_AND_200 |
| ORCL | 2026-07-01 | 142.50 | -2.76 | -9.54 | -42.58 | -23.87 | -28.99 | 27.50 | 7.22 | -40.89 | -40.21 | BELOW_50_AND_200 |
| SOFI | 2026-07-01 | 18.44 | 2.84 | 6.53 | -0.75 | 9.20 | -17.59 | 60.57 | 4.99 | 0.93 | 1.61 | MIXED |
| IAU | 2026-07-01 | 75.96 | 0.60 | 1.29 | -9.86 | -9.01 | -9.49 | 35.20 | 2.20 | -8.18 | -7.50 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-01 | 16.59 | 0.85 | -10.95 | 3.36 | -6.19 | BELOW_50_AND_200 |
| ^TNX | 2026-07-01 | 4.47 | 2.36 | -0.75 | 0.45 | 0.64 | ABOVE_50_AND_200 |
| CL=F | 2026-07-01 | 68.02 | -2.13 | -3.30 | -26.19 | -25.08 | BELOW_50_AND_200 |
| GC=F | 2026-07-01 | 4051.50 | 0.71 | 1.53 | -9.47 | -8.77 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-01 | 101.41 | 0.22 | -0.19 | 2.23 | 2.02 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.29 | XLE, XOP, USO |
| semis_ai | -5.90 | SMH, SOXX |
| high_beta | -1.93 | IWM, ARKK, HIBL |
| rates | 0.23 | TLT, TBF, TBT |
| dollar | 0.28 | UUP |
| equity_hedges | 1.94 | SH, PSQ, SQQQ |
| housing_rates | -2.39 | XHB, ITB |
| defensives | -0.49 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.32 | 1.23 | -12.31 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 1.40 | 0.99 | -3.56 | BELOW_50_AND_200 |
| ARKK | high_beta | 1.27 | 0.73 | 5.48 | ABOVE_50_AND_200 |
| TBT | rates | 1.23 | -1.06 | -0.97 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.50 | -0.73 | -0.71 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.28 | 2.63 | 2.42 | ABOVE_50_AND_200 |
| XLP | defensives | 0.28 | 1.55 | -0.72 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | 0.09 | 0.76 | -1.87 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -6.67 | -1.79 | 12.34 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -6.41 | 4.86 | 10.50 | ABOVE_50_AND_200 |
| SMH | semis_ai | -5.40 | 2.08 | 7.54 | ABOVE_50_AND_200 |
| USO | energy | -2.98 | -23.79 | -21.46 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -2.54 | 9.11 | 6.84 | ABOVE_50_AND_200 |
| ITB | housing_rates | -2.24 | 9.80 | 7.21 | ABOVE_50_AND_200 |
| XLU | defensives | -1.26 | 3.87 | -0.51 | BELOW_50_ABOVE_200 |
| TLT | rates | -1.04 | 0.06 | -0.13 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
