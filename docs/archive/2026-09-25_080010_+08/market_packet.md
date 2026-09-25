# Market Packet — 2026-09-25T08:00:10.974719+08:00

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
| SPY | 2026-09-23 | 767.81 | -0.72 | 1.82 | 0.57 | 0.91 | 7.00 | 53.04 | 0.87 | 0.00 | -4.37 | ABOVE_50_AND_200 |
| QQQ | 2026-09-23 | 741.21 | -0.84 | 5.18 | 4.94 | 4.19 | 11.56 | 63.22 | 1.32 | 4.37 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-23 | 744.10 | 1.02 | 10.51 | 33.11 | 21.57 | 18.96 | 76.95 | 3.61 | 32.54 | 28.17 | ABOVE_50_AND_200 |
| AMZN | 2026-09-23 | 249.27 | -2.24 | 1.35 | -4.88 | -2.74 | 3.59 | 44.07 | 2.39 | -5.45 | -9.82 | BELOW_50_ABOVE_200 |
| MU | 2026-09-23 | 1071.88 | -2.21 | 15.69 | 17.73 | 14.82 | 64.22 | 62.19 | 4.56 | 17.16 | 12.79 | ABOVE_50_AND_200 |
| ORCL | 2026-09-23 | 144.56 | -3.11 | 0.98 | 1.48 | 1.91 | -12.57 | 46.72 | 5.08 | 0.91 | -3.46 | MIXED |
| SOFI | 2026-09-23 | 16.55 | -3.55 | -1.72 | -9.27 | -6.07 | -14.37 | 40.76 | 4.37 | -9.83 | -14.21 | BELOW_50_AND_200 |
| IAU | 2026-09-23 | 80.52 | -1.41 | -0.32 | -7.22 | -0.28 | -5.60 | 44.40 | 1.83 | -7.79 | -12.16 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-24 | 15.67 | 3.23 | -11.52 | 1.42 | -2.68 | BELOW_50_AND_200 |
| ^TNX | 2026-09-24 | 5.16 | 0.94 | 3.12 | 9.74 | 8.73 | ABOVE_50_AND_200 |
| CL=F | 2026-09-24 | 93.96 | 1.95 | -7.80 | 14.08 | 7.07 | ABOVE_50_AND_200 |
| GC=F | 2026-09-24 | 4306.40 | -0.28 | -2.12 | -8.27 | -0.96 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-24 | 101.27 | 0.17 | 0.96 | 2.29 | 1.33 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.04 | XLE, XOP, USO |
| semis_ai | -1.11 | SMH, SOXX |
| high_beta | -0.94 | IWM, ARKK, HIBL |
| rates | 0.78 | TLT, TBF, TBT |
| dollar | 0.60 | UUP |
| equity_hedges | 0.25 | SH, PSQ, SQQQ |
| housing_rates | 0.40 | XHB, ITB |
| defensives | -0.81 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 3.30 | 12.57 | 10.73 | ABOVE_50_AND_200 |
| TBT | rates | 2.77 | 3.04 | 4.20 | ABOVE_50_AND_200 |
| TBF | rates | 1.13 | 1.41 | 2.07 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.10 | -15.05 | -13.79 | BELOW_50_AND_200 |
| XLE | energy | 0.95 | -1.17 | 1.36 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.67 | -8.92 | -6.87 | BELOW_50_AND_200 |
| XLP | defensives | 0.62 | -4.14 | -2.83 | BELOW_50_AND_200 |
| UUP | dollar | 0.60 | 2.69 | 1.56 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLU | defensives | -2.24 | -7.06 | -8.84 | BELOW_50_AND_200 |
| IWM | high_beta | -1.84 | -5.39 | -4.29 | BELOW_50_ABOVE_200 |
| TLT | rates | -1.58 | -2.54 | -2.40 | BELOW_50_AND_200 |
| SOXX | semis_ai | -1.23 | 11.76 | 7.64 | ABOVE_50_AND_200 |
| XOP | energy | -1.14 | -3.64 | 0.74 | ABOVE_50_AND_200 |
| ARKK | high_beta | -1.05 | 4.13 | 10.98 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.00 | 9.99 | 6.46 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.20 | -5.54 | -4.87 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
