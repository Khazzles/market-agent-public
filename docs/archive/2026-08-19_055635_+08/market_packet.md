# Market Packet — 2026-08-19T05:56:35.616089+08:00

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
| SPY | 2026-08-18 | 767.45 | -0.68 | -0.40 | 3.42 | 2.35 | 8.66 | 56.61 | 0.94 | 0.00 | 0.34 | ABOVE_50_AND_200 |
| QQQ | 2026-08-18 | 717.51 | -1.69 | -0.13 | 3.08 | 0.63 | 10.13 | 52.18 | 1.71 | -0.34 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-18 | 543.67 | -4.45 | -9.26 | -15.82 | -8.62 | -13.11 | 36.19 | 4.08 | -19.24 | -18.90 | BELOW_50_AND_200 |
| AMZN | 2026-08-18 | 259.45 | -0.71 | -4.71 | 3.78 | 4.37 | 9.01 | 50.93 | 3.03 | 0.37 | 0.70 | ABOVE_50_AND_200 |
| MU | 2026-08-18 | 940.76 | -7.02 | 8.32 | 8.70 | -2.27 | 67.96 | 52.17 | 7.77 | 5.28 | 5.62 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-18 | 142.79 | -2.63 | -1.85 | 17.64 | -4.27 | -18.31 | 49.48 | 5.02 | 14.22 | 14.56 | BELOW_50_AND_200 |
| SOFI | 2026-08-18 | 17.66 | -3.55 | -1.78 | 3.82 | 0.66 | -14.63 | 49.43 | 4.40 | 0.40 | 0.74 | MIXED |
| IAU | 2026-08-18 | 81.71 | -1.68 | -0.57 | 8.44 | 4.58 | -3.36 | 58.67 | 1.72 | 5.02 | 5.36 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-18 | 15.84 | 4.28 | 3.66 | -15.07 | -7.16 | BELOW_50_AND_200 |
| ^TNX | 2026-08-18 | 4.71 | -0.38 | 0.47 | 2.35 | 2.99 | ABOVE_50_AND_200 |
| CL=F | 2026-08-18 | 84.42 | -0.09 | 1.47 | 1.43 | 6.51 | ABOVE_50_AND_200 |
| GC=F | 2026-08-18 | 4389.50 | -0.64 | 0.15 | 9.46 | 5.57 | MIXED |
| DX-Y.NYB | 2026-08-18 | 99.65 | 0.01 | -0.17 | -1.32 | -0.89 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.04 | XLE, XOP, USO |
| semis_ai | -4.53 | SMH, SOXX |
| high_beta | -4.76 | IWM, ARKK, HIBL |
| rates | -0.09 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | 2.51 | SH, PSQ, SQQQ |
| housing_rates | -1.83 | XHB, ITB |
| defensives | 0.35 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 5.11 | -10.31 | -4.42 | BELOW_50_AND_200 |
| XLE | energy | 1.76 | 9.91 | 11.40 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.70 | -2.90 | -0.78 | BELOW_50_AND_200 |
| XOP | energy | 1.09 | 9.00 | 11.60 | ABOVE_50_AND_200 |
| XLP | defensives | 1.06 | 0.85 | 1.08 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.72 | -2.88 | -2.06 | BELOW_50_AND_200 |
| TLT | rates | 0.38 | -2.66 | -3.14 | BELOW_50_AND_200 |
| USO | energy | 0.28 | 4.10 | 8.72 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -9.85 | 10.27 | -5.40 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -4.96 | 1.38 | -5.28 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -4.09 | 1.96 | -3.56 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -3.18 | 5.60 | 1.94 | ABOVE_50_AND_200 |
| XHB | housing_rates | -2.07 | -0.11 | -2.67 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.59 | 0.91 | -2.10 | BELOW_50_AND_200 |
| IWM | high_beta | -1.26 | 2.71 | 1.53 | ABOVE_50_AND_200 |
| TBT | rates | -0.54 | 5.31 | 6.23 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
