# Market Packet — 2026-09-12T07:31:10.905149+08:00

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
| SPY | 2026-09-11 | 764.29 | 0.85 | -1.15 | -1.06 | 0.75 | 7.01 | 50.31 | 0.81 | 0.00 | 0.16 | ABOVE_50_AND_200 |
| QQQ | 2026-09-11 | 714.88 | 0.87 | -0.39 | -1.22 | 0.63 | 8.29 | 50.77 | 1.26 | -0.16 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-11 | 648.03 | 0.57 | 6.12 | 11.95 | 7.84 | 3.98 | 67.18 | 3.30 | 13.01 | 13.17 | ABOVE_50_AND_200 |
| AMZN | 2026-09-11 | 256.78 | 1.94 | -0.82 | -3.93 | 0.60 | 7.08 | 48.91 | 2.42 | -2.87 | -2.71 | ABOVE_50_AND_200 |
| MU | 2026-09-11 | 975.26 | -0.22 | 1.78 | 7.02 | 5.02 | 56.78 | 52.99 | 5.32 | 8.08 | 8.24 | ABOVE_50_AND_200 |
| ORCL | 2026-09-11 | 150.28 | -1.74 | -2.44 | -1.96 | 6.82 | -10.36 | 51.05 | 5.17 | -0.90 | -0.74 | MIXED |
| SOFI | 2026-09-11 | 17.32 | 0.64 | -6.43 | -3.46 | -2.86 | -12.54 | 45.25 | 4.38 | -2.39 | -2.24 | BELOW_50_AND_200 |
| IAU | 2026-09-11 | 81.71 | 0.54 | -2.84 | -1.53 | 1.90 | -4.11 | 47.32 | 1.94 | -0.47 | -0.31 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-11 | 15.84 | -11.21 | 9.02 | 8.27 | -1.73 | BELOW_50_AND_200 |
| ^TNX | 2026-09-11 | 4.97 | 0.63 | 4.47 | 6.26 | 6.49 | ABOVE_50_AND_200 |
| CL=F | 2026-09-11 | 99.99 | -2.43 | 9.52 | 20.08 | 20.14 | ABOVE_50_AND_200 |
| GC=F | 2026-09-11 | 4390.00 | 0.58 | -2.26 | -0.43 | 2.90 | MIXED |
| DX-Y.NYB | 2026-09-11 | 99.09 | 0.01 | 0.10 | -0.91 | -0.95 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.58 | XLE, XOP, USO |
| semis_ai | 1.67 | SMH, SOXX |
| high_beta | 2.52 | IWM, ARKK, HIBL |
| rates | 0.04 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | -1.42 | SH, PSQ, SQQQ |
| housing_rates | 1.55 | XHB, ITB |
| defensives | 0.02 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 6.53 | -6.64 | 0.84 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.86 | -3.57 | -0.84 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 1.60 | -9.13 | -7.53 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.50 | -8.79 | -7.45 | BELOW_50_AND_200 |
| SMH | semis_ai | 1.47 | -2.79 | -0.10 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 0.63 | 2.72 | 4.38 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.41 | -4.57 | -2.49 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.35 | -2.00 | -1.90 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -2.58 | 4.15 | -2.49 | BELOW_50_AND_200 |
| USO | energy | -2.20 | 21.68 | 21.38 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.88 | 1.69 | -0.33 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.79 | 1.62 | -0.22 | BELOW_50_AND_200 |
| XLU | defensives | -0.31 | -3.31 | -4.14 | BELOW_50_AND_200 |
| TBT | rates | 0.00 | 2.86 | 4.97 | ABOVE_50_AND_200 |
| TBF | rates | 0.00 | 1.49 | 2.59 | ABOVE_50_AND_200 |
| TLT | rates | 0.11 | -1.51 | -2.55 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
