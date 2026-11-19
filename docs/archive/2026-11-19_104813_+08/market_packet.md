# Market Packet — 2026-11-19T10:48:13.713740+08:00

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
| SPY | 2026-11-18 | 730.20 | -0.31 | -3.90 | -5.05 | -4.24 | -0.32 | 36.60 | 1.55 | 0.00 | 3.05 | BELOW_50_AND_200 |
| QQQ | 2026-11-18 | 659.51 | 0.39 | -4.47 | -8.10 | -7.68 | -3.41 | 37.69 | 2.44 | -3.05 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-18 | 616.38 | -0.40 | -1.97 | -11.22 | -9.27 | -2.08 | 41.43 | 3.45 | -6.16 | -3.12 | BELOW_50_AND_200 |
| AMZN | 2026-11-18 | 267.74 | 3.82 | 0.59 | 1.95 | 4.95 | 9.32 | 57.19 | 3.37 | 7.00 | 10.04 | ABOVE_50_AND_200 |
| MU | 2026-11-18 | 705.27 | -1.00 | -13.07 | -21.29 | -23.81 | -8.40 | 37.00 | 8.16 | -16.24 | -13.19 | BELOW_50_AND_200 |
| ORCL | 2026-11-18 | 113.89 | -0.97 | -11.29 | -13.15 | -14.99 | -25.78 | 39.26 | 6.77 | -8.10 | -5.05 | BELOW_50_AND_200 |
| SOFI | 2026-11-18 | 14.11 | -1.19 | -13.28 | -3.88 | -11.64 | -18.00 | 35.87 | 5.52 | 1.17 | 4.22 | BELOW_50_AND_200 |
| IAU | 2026-11-18 | 69.96 | -3.20 | -6.56 | -9.66 | -9.64 | -16.13 | 30.50 | 2.03 | -4.61 | -1.56 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-18 | 24.56 | -3.54 | 40.42 | 41.88 | 37.81 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-18 | 5.07 | -0.73 | 1.36 | -1.00 | -0.20 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-18 | 82.29 | -4.33 | -4.90 | -19.16 | -13.23 | BELOW_50_AND_200 |
| GC=F | 2026-11-18 | 3743.50 | -3.12 | -6.42 | -9.63 | -9.65 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-18 | 103.86 | 0.36 | 0.93 | 2.10 | 2.13 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -3.20 | XLE, XOP, USO |
| semis_ai | 0.08 | SMH, SOXX |
| high_beta | 0.56 | IWM, ARKK, HIBL |
| rates | -0.58 | TLT, TBF, TBT |
| dollar | 0.27 | UUP |
| equity_hedges | -0.46 | SH, PSQ, SQQQ |
| housing_rates | 1.34 | XHB, ITB |
| defensives | -0.00 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XHB | housing_rates | 1.68 | 4.71 | 2.33 | MIXED |
| ITB | housing_rates | 1.01 | 6.12 | 3.06 | MIXED |
| HIBL | high_beta | 0.98 | -31.97 | -35.17 | BELOW_50_AND_200 |
| TLT | rates | 0.84 | 0.11 | 0.19 | MIXED |
| IWM | high_beta | 0.40 | -2.05 | -3.31 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.31 | -14.82 | -15.24 | BELOW_50_AND_200 |
| XLU | defensives | 0.30 | 3.99 | 3.88 | MIXED |
| SH | equity_hedges | 0.29 | 5.46 | 4.50 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | -3.40 | -14.24 | -9.34 | BELOW_50_AND_200 |
| XLE | energy | -3.27 | -9.83 | -5.52 | BELOW_50_ABOVE_200 |
| USO | energy | -2.94 | -15.25 | -10.68 | BELOW_50_ABOVE_200 |
| TBT | rates | -1.71 | -0.60 | -0.94 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -1.28 | 23.01 | 20.97 | MIXED |
| TBF | rates | -0.88 | -0.15 | -0.28 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -0.39 | 8.27 | 7.64 | ABOVE_50_AND_200 |
| XLP | defensives | -0.31 | 3.91 | 5.88 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
