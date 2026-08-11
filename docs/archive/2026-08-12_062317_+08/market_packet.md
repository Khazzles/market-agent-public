# Market Packet — 2026-08-12T06:23:17.040866+08:00

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
| SPY | 2026-08-11 | 770.56 | -0.32 | -0.10 | 2.86 | 3.04 | 9.46 | 63.34 | 1.07 | 0.00 | 1.91 | ABOVE_50_AND_200 |
| QQQ | 2026-08-11 | 718.45 | -0.34 | -0.75 | 0.94 | 0.64 | 10.71 | 55.06 | 1.91 | -1.91 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-11 | 599.12 | 0.71 | 1.90 | -8.77 | 0.14 | -4.89 | 49.92 | 3.75 | -11.63 | -9.71 | MIXED |
| AMZN | 2026-08-11 | 272.27 | -2.09 | -1.86 | 10.09 | 9.95 | 14.84 | 60.97 | 3.31 | 7.24 | 9.15 | ABOVE_50_AND_200 |
| MU | 2026-08-11 | 868.52 | 0.87 | -2.71 | -7.31 | -10.24 | 60.34 | 47.02 | 8.82 | -10.16 | -8.25 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-11 | 145.48 | -3.69 | -0.18 | 10.60 | -7.71 | -18.30 | 54.12 | 5.13 | 7.74 | 9.65 | BELOW_50_AND_200 |
| SOFI | 2026-08-11 | 17.98 | -0.77 | -3.85 | -0.83 | 3.00 | -14.30 | 53.38 | 4.63 | -3.68 | -1.77 | MIXED |
| IAU | 2026-08-11 | 82.18 | -0.40 | 7.16 | 9.21 | 5.02 | -2.62 | 65.87 | 1.82 | 6.35 | 8.27 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-11 | 15.28 | -1.16 | -7.39 | -10.96 | -11.51 | BELOW_50_AND_200 |
| ^TNX | 2026-08-11 | 4.68 | -0.32 | 1.23 | 1.63 | 2.97 | ABOVE_50_AND_200 |
| CL=F | 2026-08-11 | 83.52 | 1.69 | 10.23 | 6.89 | 4.06 | ABOVE_50_AND_200 |
| GC=F | 2026-08-11 | 4432.90 | 1.63 | 8.24 | 10.91 | 6.46 | MIXED |
| DX-Y.NYB | 2026-08-11 | 99.81 | 0.00 | -0.08 | -1.45 | -0.70 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.33 | XLE, XOP, USO |
| semis_ai | 0.76 | SMH, SOXX |
| high_beta | 0.70 | IWM, ARKK, HIBL |
| rates | -0.20 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | 0.59 | SH, PSQ, SQQQ |
| housing_rates | 2.02 | XHB, ITB |
| defensives | 0.43 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 2.14 | 4.36 | 2.72 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.90 | 3.02 | 1.72 | ABOVE_50_AND_200 |
| HIBL | high_beta | 1.56 | 0.64 | -3.78 | BELOW_50_ABOVE_200 |
| XOP | energy | 1.39 | 7.98 | 8.21 | ABOVE_50_AND_200 |
| USO | energy | 1.34 | 8.34 | 5.42 | ABOVE_50_AND_200 |
| XLE | energy | 1.25 | 7.38 | 7.33 | ABOVE_50_AND_200 |
| XLU | defensives | 1.16 | -4.57 | -2.65 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | 1.09 | -4.53 | -5.16 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | -0.42 | 4.05 | 5.41 | ABOVE_50_AND_200 |
| TBF | rates | -0.35 | 2.09 | 2.66 | ABOVE_50_AND_200 |
| XLP | defensives | -0.31 | 0.12 | 0.40 | ABOVE_50_AND_200 |
| UUP | dollar | 0.00 | -1.26 | -0.39 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.16 | -2.12 | -2.91 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.20 | 3.02 | 4.13 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.31 | -0.93 | -1.01 | BELOW_50_AND_200 |
| IWM | high_beta | 0.34 | 2.56 | 2.29 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
