# Market Packet — 2026-06-24T06:51:09.828013+08:00

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
| SPY | 2026-06-23 | 733.58 | -1.45 | -2.82 | -1.23 | 0.21 | 6.43 | 45.92 | 1.32 | 0.00 | -1.11 | ABOVE_50_AND_200 |
| QQQ | 2026-06-23 | 713.65 | -3.29 | -4.08 | -0.12 | 2.27 | 13.25 | 48.83 | 2.27 | 1.11 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-23 | 562.20 | -0.29 | -5.27 | -7.44 | -9.21 | -13.92 | 38.97 | 3.43 | -6.21 | -7.32 | BELOW_50_AND_200 |
| AMZN | 2026-06-23 | 234.11 | 0.57 | -4.84 | -12.80 | -8.91 | 0.55 | 37.83 | 3.32 | -11.56 | -12.67 | BELOW_50_ABOVE_200 |
| MU | 2026-06-23 | 1051.77 | -13.18 | -3.33 | 38.01 | 38.17 | 156.00 | 57.04 | 8.22 | 39.24 | 38.13 | ABOVE_50_AND_200 |
| ORCL | 2026-06-23 | 165.16 | -5.66 | -14.26 | -12.97 | -12.92 | -19.20 | 35.17 | 7.34 | -11.74 | -12.85 | BELOW_50_AND_200 |
| SOFI | 2026-06-23 | 17.29 | 1.11 | 0.93 | 10.48 | 1.83 | -23.56 | 52.93 | 5.53 | 11.71 | 10.60 | MIXED |
| IAU | 2026-06-23 | 77.33 | -1.87 | -4.84 | -9.48 | -9.29 | -7.61 | 33.27 | 2.26 | -8.25 | -9.36 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-23 | 19.49 | 12.79 | 20.31 | 16.71 | 9.75 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-23 | 4.49 | 0.94 | 0.13 | -1.73 | 1.36 | ABOVE_50_AND_200 |
| CL=F | 2026-06-23 | 73.01 | -2.42 | -9.59 | -24.22 | -21.82 | BELOW_50_AND_200 |
| GC=F | 2026-06-23 | 4119.00 | -1.50 | -4.83 | -9.27 | -9.14 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-23 | 101.39 | 0.37 | 1.77 | 2.22 | 2.39 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.15 | XLE, XOP, USO |
| semis_ai | -7.44 | SMH, SOXX |
| high_beta | -5.15 | IWM, ARKK, HIBL |
| rates | -0.20 | TLT, TBF, TBT |
| dollar | 0.32 | UUP |
| equity_hedges | 4.84 | SH, PSQ, SQQQ |
| housing_rates | -0.43 | XHB, ITB |
| defensives | 1.33 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 9.83 | -3.34 | -11.26 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 3.29 | -0.19 | -2.72 | BELOW_50_AND_200 |
| XLP | defensives | 1.87 | -1.11 | 0.10 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.41 | 1.35 | -0.11 | BELOW_50_AND_200 |
| XLU | defensives | 0.78 | 0.16 | 0.01 | ABOVE_50_AND_200 |
| XLE | energy | 0.74 | -7.90 | -5.00 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.32 | 2.60 | 2.77 | ABOVE_50_AND_200 |
| TLT | rates | 0.13 | 2.35 | 0.67 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -12.27 | 18.71 | 15.55 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -7.88 | 14.99 | 16.48 | ABOVE_50_AND_200 |
| SMH | semis_ai | -7.01 | 9.54 | 11.87 | ABOVE_50_AND_200 |
| ARKK | high_beta | -2.23 | 0.08 | -0.81 | BELOW_50_AND_200 |
| USO | energy | -1.27 | -21.94 | -16.65 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.96 | 4.54 | 4.44 | ABOVE_50_AND_200 |
| XHB | housing_rates | -0.85 | 8.68 | 3.74 | ABOVE_50_AND_200 |
| TBT | rates | -0.51 | -4.90 | -1.73 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
