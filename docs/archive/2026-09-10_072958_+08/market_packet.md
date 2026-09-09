# Market Packet — 2026-09-10T07:29:58.358364+08:00

## Manifest

- AS_OF policy: latest available market close per yfinance.

- Run timezone: Asia/Kuala_Lumpur

- Objective: public research packet only; no portfolio sizes, holdings, cost basis, or private notes.

- Core universe: SPY, QQQ, META, AMZN, MU, ORCL, SOFI, IAU

- Data source: yfinance for market prices and OHLCV-derived indicators.

- Interpretation layer: intended for downstream ChatGPT manager/supervisor review.


## Data Status

Potential issues:

- ^VIX: MISSING_DATA


## Core Universe Technical Evidence

| Ticker | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | vs SMA200 % | RSI14 | ATR14 % | RS vs SPY 21D | RS vs QQQ 21D | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 2026-09-09 | 762.40 | -0.46 | 0.08 | -1.38 | 0.58 | 6.90 | 48.04 | 0.79 | 0.00 | -0.74 | ABOVE_50_AND_200 |
| QQQ | 2026-09-09 | 716.31 | -0.29 | 1.23 | -0.63 | 0.72 | 8.71 | 51.65 | 1.25 | 0.74 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-09 | 653.69 | 6.55 | 12.99 | 9.88 | 9.21 | 4.98 | 70.43 | 3.29 | 11.25 | 10.51 | ABOVE_50_AND_200 |
| AMZN | 2026-09-09 | 252.40 | -1.78 | -0.99 | -9.24 | -0.90 | 5.41 | 44.06 | 2.56 | -7.86 | -8.61 | BELOW_50_ABOVE_200 |
| MU | 2026-09-09 | 1027.77 | 2.75 | 10.11 | 19.37 | 10.12 | 67.29 | 60.61 | 5.23 | 20.74 | 20.00 | ABOVE_50_AND_200 |
| ORCL | 2026-09-09 | 161.63 | -0.55 | 14.37 | 7.00 | 15.12 | -3.89 | 62.39 | 4.31 | 8.38 | 7.64 | MIXED |
| SOFI | 2026-09-09 | 17.33 | -3.78 | 1.64 | -4.36 | -3.00 | -12.84 | 45.10 | 4.69 | -2.98 | -3.73 | BELOW_50_AND_200 |
| IAU | 2026-09-09 | 82.69 | 0.90 | 1.65 | 0.22 | 3.42 | -2.91 | 50.22 | 1.93 | 1.59 | 0.85 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | UNK | UNK | UNK | UNK | UNK | UNK | UNK |
| ^TNX | 2026-09-09 | 4.84 | 0.65 | 0.85 | 2.94 | 3.99 | ABOVE_50_AND_200 |
| CL=F | 2026-09-09 | 97.14 | 4.42 | 7.67 | 18.28 | 18.52 | ABOVE_50_AND_200 |
| GC=F | 2026-09-09 | 4444.10 | 1.14 | 2.21 | 1.89 | 4.48 | MIXED |
| DX-Y.NYB | 2026-09-09 | 98.78 | -0.06 | -0.89 | -1.03 | -1.35 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.37 | XLE, XOP, USO |
| semis_ai | 0.39 | SMH, SOXX |
| high_beta | -2.05 | IWM, ARKK, HIBL |
| rates | 0.43 | TLT, TBF, TBT |
| dollar | -0.04 | UUP |
| equity_hedges | 0.57 | SH, PSQ, SQQQ |
| housing_rates | -1.16 | XHB, ITB |
| defensives | -1.16 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.70 | 19.10 | 19.45 | ABOVE_50_AND_200 |
| TBT | rates | 1.26 | 0.55 | 3.19 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.86 | 2.41 | -2.85 | BELOW_50_AND_200 |
| XLE | energy | 0.83 | 8.52 | 9.48 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.68 | 0.49 | -0.64 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.59 | 0.39 | 1.77 | ABOVE_50_AND_200 |
| XOP | energy | 0.57 | 10.85 | 11.34 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.49 | 1.90 | -0.07 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -3.01 | 0.29 | 0.24 | ABOVE_50_AND_200 |
| ARKK | high_beta | -1.77 | 5.12 | 5.71 | ABOVE_50_AND_200 |
| XHB | housing_rates | -1.51 | -8.32 | -7.38 | BELOW_50_AND_200 |
| IWM | high_beta | -1.37 | -3.11 | -2.06 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.17 | -0.44 | -3.12 | BELOW_50_AND_200 |
| XLP | defensives | -1.15 | -2.24 | -2.28 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.81 | -8.21 | -7.21 | BELOW_50_AND_200 |
| TLT | rates | -0.57 | -0.40 | -1.76 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
