# Market Packet — 2026-11-07T09:11:45.955911+08:00

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
| SPY | 2026-11-05 | 733.00 | -4.41 | -4.73 | -5.69 | -4.36 | 0.39 | 33.50 | 1.43 | 0.00 | 8.92 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-05 | 647.05 | -6.49 | -9.55 | -14.61 | -10.41 | -4.94 | 26.86 | 2.39 | -8.92 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-05 | 605.08 | -3.96 | -3.11 | -16.11 | -10.24 | -4.28 | 34.94 | 3.99 | -10.42 | -1.51 | BELOW_50_AND_200 |
| AMZN | 2026-11-05 | 260.21 | -2.19 | 6.74 | 0.11 | 2.49 | 6.72 | 54.97 | 3.53 | 5.80 | 14.72 | ABOVE_50_AND_200 |
| MU | 2026-11-05 | 656.39 | -17.46 | -29.74 | -39.67 | -32.09 | -13.09 | 27.05 | 8.95 | -33.98 | -25.06 | BELOW_50_AND_200 |
| ORCL | 2026-11-05 | 115.16 | -6.93 | -17.48 | -19.78 | -17.64 | -26.04 | 37.73 | 7.38 | -14.09 | -5.18 | BELOW_50_AND_200 |
| SOFI | 2026-11-05 | 16.04 | -7.71 | -8.92 | 2.43 | -2.27 | -8.87 | 49.58 | 5.32 | 8.12 | 17.03 | BELOW_50_AND_200 |
| IAU | 2026-11-05 | 77.00 | 0.82 | 1.89 | -0.08 | -2.69 | -8.72 | 50.23 | 1.75 | 5.61 | 14.53 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-06 | 25.64 | -9.01 | 32.03 | 66.39 | 51.52 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-06 | 4.86 | 0.45 | -1.42 | -7.11 | -3.46 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-06 | 90.34 | -0.20 | -13.23 | -1.26 | -5.36 | BELOW_50_ABOVE_200 |
| GC=F | 2026-11-06 | 4079.50 | -0.83 | 4.63 | -1.86 | -3.57 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-06 | 102.28 | 0.72 | 0.39 | 0.14 | 1.17 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.31 | XLE, XOP, USO |
| semis_ai | -11.68 | SMH, SOXX |
| high_beta | -12.72 | IWM, ARKK, HIBL |
| rates | -0.19 | TLT, TBF, TBT |
| dollar | 0.07 | UUP |
| equity_hedges | 9.97 | SH, PSQ, SQQQ |
| housing_rates | -2.54 | XHB, ITB |
| defensives | -0.73 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 19.23 | 54.51 | 32.73 | MIXED |
| PSQ | equity_hedges | 6.32 | 16.62 | 10.71 | ABOVE_50_AND_200 |
| SH | equity_hedges | 4.38 | 6.32 | 4.46 | MIXED |
| USO | energy | 1.93 | 2.99 | -2.40 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.21 | 6.20 | 1.90 | MIXED |
| UUP | dollar | 0.07 | -0.41 | 0.89 | ABOVE_50_AND_200 |
| TBF | rates | -0.28 | -5.94 | -2.27 | BELOW_50_ABOVE_200 |
| TBT | rates | -0.50 | -11.96 | -4.86 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -24.57 | -51.33 | -41.97 | BELOW_50_AND_200 |
| SOXX | semis_ai | -12.15 | -32.11 | -24.38 | BELOW_50_AND_200 |
| SMH | semis_ai | -11.21 | -28.37 | -21.15 | BELOW_50_AND_200 |
| ARKK | high_beta | -8.98 | -17.16 | -14.64 | BELOW_50_AND_200 |
| IWM | high_beta | -4.59 | -2.42 | -4.12 | BELOW_50_AND_200 |
| XHB | housing_rates | -3.41 | 9.44 | 5.47 | MIXED |
| XLE | energy | -2.98 | -2.73 | -5.31 | BELOW_50_ABOVE_200 |
| XOP | energy | -2.89 | -7.51 | -9.13 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
