# Market Packet — 2026-09-30T08:45:18.634352+08:00

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
| SPY | 2026-09-28 | 765.61 | -0.74 | -1.02 | -0.71 | 0.47 | 6.50 | 50.50 | 0.86 | 0.00 | -2.85 | ABOVE_50_AND_200 |
| QQQ | 2026-09-28 | 736.53 | -1.07 | -0.67 | 2.14 | 3.23 | 10.57 | 58.47 | 1.28 | 2.85 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-28 | 715.62 | -4.79 | -3.46 | 25.31 | 15.96 | 14.18 | 60.93 | 3.89 | 26.02 | 23.17 | ABOVE_50_AND_200 |
| AMZN | 2026-09-28 | 246.15 | -1.41 | -4.76 | -3.95 | -3.91 | 2.16 | 41.24 | 2.27 | -3.23 | -6.08 | BELOW_50_ABOVE_200 |
| MU | 2026-09-28 | 1053.98 | -2.61 | 0.96 | 12.68 | 11.45 | 58.47 | 58.35 | 4.45 | 13.39 | 10.54 | ABOVE_50_AND_200 |
| ORCL | 2026-09-28 | 132.60 | -3.28 | -10.74 | -12.73 | -6.86 | -19.19 | 37.27 | 5.49 | -12.02 | -14.87 | BELOW_50_AND_200 |
| SOFI | 2026-09-28 | 15.93 | -3.92 | -6.13 | -16.94 | -9.27 | -16.87 | 36.68 | 4.23 | -16.23 | -19.08 | BELOW_50_AND_200 |
| IAU | 2026-09-28 | 77.50 | -3.92 | -5.11 | -10.53 | -4.43 | -9.16 | 35.31 | 1.97 | -9.82 | -12.67 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-29 | 16.04 | -0.19 | 12.88 | 7.51 | 0.87 | MIXED |
| ^TNX | 2026-09-29 | 5.25 | 0.29 | 5.78 | 11.33 | 9.58 | ABOVE_50_AND_200 |
| CL=F | 2026-09-29 | 89.21 | -3.66 | -5.69 | 6.97 | 0.96 | ABOVE_50_AND_200 |
| GC=F | 2026-09-29 | 4215.40 | 1.13 | -3.68 | -6.94 | -3.35 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-29 | 101.41 | 0.20 | 0.80 | 1.71 | 1.44 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.16 | XLE, XOP, USO |
| semis_ai | -1.58 | SMH, SOXX |
| high_beta | -2.52 | IWM, ARKK, HIBL |
| rates | 0.50 | TLT, TBF, TBT |
| dollar | 0.28 | UUP |
| equity_hedges | 1.69 | SH, PSQ, SQQQ |
| housing_rates | -0.90 | XHB, ITB |
| defensives | -0.20 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 3.20 | -7.81 | -11.16 | BELOW_50_AND_200 |
| TBT | rates | 1.52 | 10.89 | 8.20 | ABOVE_50_AND_200 |
| USO | energy | 1.13 | 15.38 | 10.18 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.10 | -2.88 | -3.87 | BELOW_50_AND_200 |
| TBF | rates | 0.88 | 5.24 | 4.07 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.78 | 0.03 | -1.00 | BELOW_50_AND_200 |
| UUP | dollar | 0.28 | 2.43 | 1.65 | ABOVE_50_AND_200 |
| XLP | defensives | 0.27 | -3.29 | -2.80 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.21 | -1.61 | 4.75 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.08 | 6.73 | 6.33 | ABOVE_50_AND_200 |
| ARKK | high_beta | -1.67 | 2.14 | 8.93 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.08 | 4.71 | 5.87 | ABOVE_50_AND_200 |
| XHB | housing_rates | -1.04 | -6.91 | -6.40 | BELOW_50_AND_200 |
| TLT | rates | -0.88 | -5.43 | -4.27 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.76 | -7.19 | -6.22 | BELOW_50_AND_200 |
| XOP | energy | -0.75 | -2.87 | -1.29 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
