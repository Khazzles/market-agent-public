# Market Packet — 2026-08-18T05:57:56.830382+08:00

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
| SPY | 2026-08-17 | 772.67 | -0.47 | -0.05 | 3.95 | 3.13 | 9.46 | 61.78 | 0.95 | 0.00 | -1.01 | ABOVE_50_AND_200 |
| QQQ | 2026-08-17 | 729.87 | -0.16 | 1.25 | 4.97 | 2.40 | 12.10 | 58.88 | 1.66 | 1.01 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-17 | 568.97 | -3.54 | -4.36 | -11.93 | -4.53 | -9.21 | 41.88 | 3.85 | -15.88 | -16.89 | BELOW_50_AND_200 |
| AMZN | 2026-08-17 | 261.31 | -0.51 | -6.03 | 5.70 | 5.23 | 9.86 | 52.43 | 3.11 | 1.74 | 0.73 | ABOVE_50_AND_200 |
| MU | 2026-08-17 | 1011.75 | 4.13 | 17.51 | 19.18 | 5.28 | 81.79 | 59.53 | 7.13 | 15.22 | 14.21 | ABOVE_50_AND_200 |
| ORCL | 2026-08-17 | 146.65 | -2.57 | -2.91 | 16.01 | -2.61 | -16.42 | 52.67 | 5.04 | 12.06 | 11.04 | BELOW_50_AND_200 |
| SOFI | 2026-08-17 | 18.31 | 0.11 | 1.05 | 5.96 | 4.55 | -11.77 | 55.48 | 4.29 | 2.01 | 0.99 | MIXED |
| IAU | 2026-08-17 | 83.11 | 1.01 | 0.73 | 10.08 | 6.39 | -1.66 | 65.70 | 1.68 | 6.13 | 5.11 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-17 | 15.19 | 6.60 | -1.75 | -19.07 | -11.56 | BELOW_50_AND_200 |
| ^TNX | 2026-08-17 | 4.72 | 0.60 | 0.53 | 4.03 | 3.46 | ABOVE_50_AND_200 |
| CL=F | 2026-08-17 | 84.95 | 3.09 | 3.43 | 2.98 | 7.00 | ABOVE_50_AND_200 |
| GC=F | 2026-08-17 | 4473.10 | 2.12 | 2.55 | 11.47 | 7.58 | MIXED |
| DX-Y.NYB | 2026-08-17 | 99.58 | -0.09 | -0.23 | -1.16 | -0.97 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.86 | XLE, XOP, USO |
| semis_ai | 1.32 | SMH, SOXX |
| high_beta | 0.27 | IWM, ARKK, HIBL |
| rates | 0.47 | TLT, TBF, TBT |
| dollar | -0.04 | UUP |
| equity_hedges | 0.40 | SH, PSQ, SQQQ |
| housing_rates | -0.86 | XHB, ITB |
| defensives | -0.97 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.91 | 5.11 | 8.37 | ABOVE_50_AND_200 |
| TBT | rates | 1.59 | 7.60 | 6.96 | ABOVE_50_AND_200 |
| XOP | energy | 1.58 | 7.74 | 10.65 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.58 | 7.15 | -0.37 | BELOW_50_ABOVE_200 |
| XLE | energy | 1.08 | 8.50 | 9.70 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.06 | 6.75 | 0.55 | ABOVE_50_AND_200 |
| ARKK | high_beta | 0.80 | 8.71 | 5.42 | ABOVE_50_AND_200 |
| TBF | rates | 0.67 | 3.72 | 3.47 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLP | defensives | -1.64 | -0.60 | 0.06 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.95 | 0.52 | -0.45 | BELOW_50_AND_200 |
| TLT | rates | -0.84 | -3.75 | -3.59 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.76 | -0.06 | -0.57 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.34 | 3.41 | 2.95 | ABOVE_50_AND_200 |
| XLU | defensives | -0.29 | -2.19 | -1.50 | BELOW_50_AND_200 |
| UUP | dollar | -0.04 | -0.81 | -0.63 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 0.24 | -4.60 | -2.49 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
