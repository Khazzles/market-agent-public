# Market Packet — 2026-09-29T09:15:40.498158+08:00

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
| SPY | 2026-09-25 | 771.35 | 0.54 | 1.27 | 0.69 | 1.28 | 7.36 | 55.89 | 0.87 | 0.00 | -3.97 | ABOVE_50_AND_200 |
| QQQ | 2026-09-25 | 744.50 | 0.46 | 3.19 | 4.66 | 4.47 | 11.86 | 64.69 | 1.31 | 3.97 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-25 | 751.66 | -3.33 | 12.90 | 30.46 | 22.07 | 19.98 | 71.33 | 3.73 | 29.78 | 25.81 | ABOVE_50_AND_200 |
| AMZN | 2026-09-25 | 249.67 | 0.12 | -1.59 | -4.08 | -2.54 | 3.66 | 44.54 | 2.30 | -4.76 | -8.73 | BELOW_50_ABOVE_200 |
| MU | 2026-09-25 | 1082.28 | 0.16 | 6.54 | 15.33 | 14.94 | 63.71 | 63.20 | 4.47 | 14.64 | 10.68 | ABOVE_50_AND_200 |
| ORCL | 2026-09-25 | 137.10 | -1.75 | -7.12 | -7.91 | -3.62 | -16.68 | 40.60 | 5.09 | -8.59 | -12.56 | BELOW_50_AND_200 |
| SOFI | 2026-09-25 | 16.58 | -1.31 | -2.24 | -12.00 | -5.71 | -13.73 | 41.69 | 4.22 | -12.68 | -16.65 | BELOW_50_AND_200 |
| IAU | 2026-09-25 | 80.66 | 0.45 | -1.91 | -6.61 | -0.49 | -5.47 | 45.23 | 1.94 | -7.30 | -11.27 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-28 | 16.07 | 8.07 | 8.07 | 11.37 | 0.93 | MIXED |
| ^TNX | 2026-09-28 | 5.24 | 1.08 | 5.58 | 12.16 | 9.57 | ABOVE_50_AND_200 |
| CL=F | 2026-09-28 | 93.36 | 1.03 | -2.53 | 11.77 | 5.78 | ABOVE_50_AND_200 |
| GC=F | 2026-09-28 | 4153.30 | -3.89 | -5.26 | -10.95 | -4.68 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-28 | 101.21 | 0.24 | 0.78 | 2.07 | 1.25 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.80 | XLE, XOP, USO |
| semis_ai | 1.09 | SMH, SOXX |
| high_beta | 0.71 | IWM, ARKK, HIBL |
| rates | 0.19 | TLT, TBF, TBT |
| dollar | -0.24 | UUP |
| equity_hedges | -0.71 | SH, PSQ, SQQQ |
| housing_rates | 1.42 | XHB, ITB |
| defensives | 0.41 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 3.04 | 5.90 | 10.77 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.57 | -7.25 | -5.62 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.27 | -8.10 | -5.67 | BELOW_50_AND_200 |
| SOXX | semis_ai | 1.17 | 11.11 | 8.74 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.01 | 9.14 | 7.19 | ABOVE_50_AND_200 |
| XLP | defensives | 0.44 | -4.88 | -3.13 | BELOW_50_AND_200 |
| TBT | rates | 0.39 | 9.56 | 6.87 | ABOVE_50_AND_200 |
| XLU | defensives | 0.38 | -9.19 | -8.68 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -3.11 | 16.47 | 9.36 | ABOVE_50_AND_200 |
| XOP | energy | -1.39 | -1.60 | -0.44 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -1.26 | -14.30 | -14.26 | BELOW_50_AND_200 |
| ARKK | high_beta | -1.01 | 5.82 | 11.17 | ABOVE_50_AND_200 |
| XLE | energy | -0.89 | -0.62 | 0.46 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.47 | -1.36 | -1.83 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.40 | -5.23 | -5.03 | BELOW_50_AND_200 |
| UUP | dollar | -0.24 | 2.14 | 1.39 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
