# Market Packet — 2026-08-27T09:03:25.001817+08:00

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
| SPY | 2026-08-26 | 766.08 | 0.02 | -0.39 | 3.40 | 1.74 | 8.07 | 54.35 | 0.82 | 0.00 | -1.91 | ABOVE_50_AND_200 |
| QQQ | 2026-08-26 | 711.37 | 0.09 | -0.66 | 5.31 | -0.14 | 8.75 | 49.33 | 1.49 | 1.91 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-26 | 576.14 | 1.07 | 5.51 | -2.91 | -2.76 | -7.56 | 48.64 | 3.50 | -6.31 | -8.22 | BELOW_50_AND_200 |
| AMZN | 2026-08-26 | 260.28 | -0.30 | -2.09 | 12.74 | 3.75 | 9.12 | 50.88 | 2.62 | 9.34 | 7.43 | ABOVE_50_AND_200 |
| MU | 2026-08-26 | 938.40 | 0.58 | 0.14 | 14.37 | -2.14 | 61.37 | 51.34 | 6.63 | 10.96 | 9.05 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-26 | 148.87 | 2.84 | 3.52 | 24.10 | 4.16 | -13.22 | 54.73 | 4.51 | 20.70 | 18.79 | MIXED |
| SOFI | 2026-08-26 | 18.84 | -0.84 | 2.28 | 12.54 | 5.92 | -7.48 | 56.25 | 4.46 | 9.14 | 7.23 | MIXED |
| IAU | 2026-08-26 | 86.37 | -1.58 | 1.80 | 14.10 | 9.41 | 1.74 | 66.13 | 1.75 | 10.69 | 8.78 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-26 | 15.21 | -1.55 | 2.15 | -16.47 | -8.52 | BELOW_50_AND_200 |
| ^TNX | 2026-08-26 | 4.66 | 0.54 | 0.24 | 1.30 | 1.60 | ABOVE_50_AND_200 |
| CL=F | 2026-08-26 | 81.66 | -0.85 | -4.86 | 3.03 | 3.36 | ABOVE_50_AND_200 |
| GC=F | 2026-08-26 | 4655.00 | 0.36 | 3.69 | 15.33 | 10.78 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-26 | 99.13 | 0.21 | 0.30 | -2.22 | -1.31 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.83 | XLE, XOP, USO |
| semis_ai | 0.13 | SMH, SOXX |
| high_beta | 0.23 | IWM, ARKK, HIBL |
| rates | 0.21 | TLT, TBF, TBT |
| dollar | 0.29 | UUP |
| equity_hedges | -0.10 | SH, PSQ, SQQQ |
| housing_rates | -0.61 | XHB, ITB |
| defensives | 0.09 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 1.48 | 18.48 | -1.01 | BELOW_50_ABOVE_200 |
| USO | energy | 0.95 | 5.69 | 5.80 | ABOVE_50_AND_200 |
| XOP | energy | 0.95 | 10.87 | 9.36 | ABOVE_50_AND_200 |
| XLE | energy | 0.60 | 8.44 | 7.91 | ABOVE_50_AND_200 |
| XLU | defensives | 0.46 | -4.42 | -2.79 | BELOW_50_AND_200 |
| TBT | rates | 0.43 | 1.99 | 1.39 | ABOVE_50_AND_200 |
| TBF | rates | 0.40 | 1.21 | 0.97 | ABOVE_50_AND_200 |
| UUP | dollar | 0.29 | -1.96 | -0.89 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -0.87 | -3.01 | -1.31 | BELOW_50_AND_200 |
| ARKK | high_beta | -0.68 | 18.40 | 8.96 | ABOVE_50_AND_200 |
| XHB | housing_rates | -0.36 | -3.32 | -2.66 | BELOW_50_AND_200 |
| XLP | defensives | -0.29 | -0.91 | 1.68 | ABOVE_50_AND_200 |
| TLT | rates | -0.20 | -1.12 | -0.84 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -0.20 | -15.33 | -1.16 | BELOW_50_AND_200 |
| IWM | high_beta | -0.10 | 1.90 | 0.64 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.08 | -4.87 | 0.20 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
