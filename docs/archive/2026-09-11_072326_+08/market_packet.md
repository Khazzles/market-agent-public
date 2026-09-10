# Market Packet — 2026-09-11T07:23:26.567676+08:00

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
| SPY | 2026-09-10 | 757.83 | -0.60 | -0.96 | -1.65 | -0.05 | 6.18 | 44.09 | 0.80 | 0.00 | -0.29 | BELOW_50_ABOVE_200 |
| QQQ | 2026-09-10 | 708.69 | -1.06 | -0.08 | -1.36 | -0.27 | 7.46 | 46.31 | 1.27 | 0.29 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-10 | 644.38 | -1.42 | 8.69 | 7.55 | 7.36 | 3.44 | 66.38 | 3.33 | 9.21 | 8.91 | ABOVE_50_AND_200 |
| AMZN | 2026-09-10 | 251.89 | -0.20 | -1.21 | -7.49 | -1.20 | 5.12 | 43.62 | 2.49 | -5.83 | -6.13 | BELOW_50_ABOVE_200 |
| MU | 2026-09-10 | 977.41 | -4.90 | 2.23 | 12.54 | 5.13 | 58.10 | 53.29 | 5.50 | 14.19 | 13.90 | ABOVE_50_AND_200 |
| ORCL | 2026-09-10 | 152.94 | -5.38 | 4.93 | 5.13 | 8.84 | -8.90 | 53.46 | 4.65 | 6.78 | 6.49 | MIXED |
| SOFI | 2026-09-10 | 17.21 | -0.69 | -3.53 | -4.28 | -3.60 | -13.27 | 44.32 | 4.58 | -2.63 | -2.92 | BELOW_50_AND_200 |
| IAU | 2026-09-10 | 81.27 | -1.72 | -1.55 | -1.11 | 1.50 | -4.60 | 45.76 | 1.96 | 0.54 | 0.25 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-10 | 17.84 | 8.38 | 24.58 | 22.61 | 10.64 | MIXED |
| ^TNX | 2026-09-10 | 4.94 | 2.21 | 3.09 | 5.55 | 6.05 | ABOVE_50_AND_200 |
| CL=F | 2026-09-10 | 103.78 | 8.05 | 14.03 | 24.74 | 25.60 | ABOVE_50_AND_200 |
| GC=F | 2026-09-10 | 4357.20 | -1.33 | -0.21 | -0.59 | 2.29 | MIXED |
| DX-Y.NYB | 2026-09-10 | 99.09 | 0.32 | -0.47 | -0.73 | -1.00 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.75 | XLE, XOP, USO |
| semis_ai | -2.59 | SMH, SOXX |
| high_beta | -3.08 | IWM, ARKK, HIBL |
| rates | 0.70 | TLT, TBF, TBT |
| dollar | 0.18 | UUP |
| equity_hedges | 1.66 | SH, PSQ, SQQQ |
| housing_rates | -2.33 | XHB, ITB |
| defensives | -0.46 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 5.61 | 24.11 | 25.12 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 3.26 | 4.61 | 0.14 | MIXED |
| TBT | rates | 2.20 | 3.19 | 5.20 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.12 | 1.83 | 0.60 | MIXED |
| TBF | rates | 1.06 | 1.81 | 2.71 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.61 | 2.14 | 0.55 | MIXED |
| XOP | energy | 0.24 | 9.59 | 11.08 | ABOVE_50_AND_200 |
| UUP | dollar | 0.18 | -0.39 | -0.67 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -6.45 | -7.62 | -5.65 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -2.74 | -3.14 | -2.92 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -2.44 | -2.21 | -1.73 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -2.34 | -12.14 | -9.23 | BELOW_50_AND_200 |
| ITB | housing_rates | -2.31 | -12.22 | -9.05 | BELOW_50_AND_200 |
| ARKK | high_beta | -1.77 | 3.05 | 3.78 | ABOVE_50_AND_200 |
| TLT | rates | -1.16 | -1.72 | -2.77 | BELOW_50_AND_200 |
| IWM | high_beta | -1.01 | -4.42 | -2.96 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
