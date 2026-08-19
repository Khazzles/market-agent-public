# Market Packet — 2026-08-20T05:58:53.213446+08:00

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
| SPY | 2026-08-19 | 769.06 | 0.21 | -0.44 | 2.78 | 2.48 | 8.82 | 57.78 | 0.92 | 0.00 | 1.77 | ABOVE_50_AND_200 |
| QQQ | 2026-08-19 | 716.08 | -0.20 | -1.05 | 1.00 | 0.43 | 9.83 | 51.45 | 1.68 | -1.77 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-19 | 546.03 | 0.43 | -5.67 | -15.19 | -8.10 | -12.65 | 37.05 | 3.99 | -17.96 | -16.19 | BELOW_50_AND_200 |
| AMZN | 2026-08-19 | 265.84 | 2.46 | -0.54 | 7.39 | 6.76 | 11.59 | 55.64 | 2.96 | 4.61 | 6.39 | ABOVE_50_AND_200 |
| MU | 2026-08-19 | 937.11 | -0.39 | 2.83 | -3.47 | -2.62 | 66.25 | 51.81 | 7.58 | -6.25 | -4.48 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-19 | 143.81 | 0.71 | -6.18 | 13.19 | -2.70 | -17.46 | 50.34 | 5.06 | 10.41 | 12.19 | BELOW_50_AND_200 |
| SOFI | 2026-08-19 | 18.42 | 4.30 | 2.68 | 4.42 | 4.76 | -10.72 | 55.53 | 4.33 | 1.64 | 3.42 | MIXED |
| IAU | 2026-08-19 | 84.84 | 3.83 | 2.24 | 10.44 | 8.49 | 0.28 | 67.14 | 1.80 | 7.66 | 9.44 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-19 | 14.89 | -6.00 | 2.34 | -12.67 | -12.31 | BELOW_50_AND_200 |
| ^TNX | 2026-08-19 | 4.65 | -1.13 | -0.62 | 0.54 | 1.78 | ABOVE_50_AND_200 |
| CL=F | 2026-08-19 | 84.40 | -0.64 | 1.36 | -0.60 | 6.66 | ABOVE_50_AND_200 |
| GC=F | 2026-08-19 | 4580.70 | 4.92 | 3.90 | 12.52 | 10.05 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-19 | 98.80 | -0.86 | -1.21 | -2.36 | -1.72 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.19 | XLE, XOP, USO |
| semis_ai | -1.88 | SMH, SOXX |
| high_beta | 3.20 | IWM, ARKK, HIBL |
| rates | -1.16 | TLT, TBF, TBT |
| dollar | -0.92 | UUP |
| equity_hedges | 0.20 | SH, PSQ, SQQQ |
| housing_rates | 2.62 | XHB, ITB |
| defensives | 0.56 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | 5.26 | 7.23 | 7.09 | ABOVE_50_AND_200 |
| HIBL | high_beta | 3.84 | 14.51 | -1.79 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | 3.10 | 4.56 | 0.79 | ABOVE_50_AND_200 |
| XHB | housing_rates | 2.15 | 2.16 | -0.67 | BELOW_50_ABOVE_200 |
| TLT | rates | 1.67 | -0.77 | -1.49 | BELOW_50_AND_200 |
| XLP | defensives | 1.12 | 2.95 | 2.13 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.65 | -4.42 | -3.67 | BELOW_50_AND_200 |
| XOP | energy | 0.53 | 7.19 | 11.95 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | -3.40 | 1.05 | 2.56 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.21 | -5.97 | -7.20 | BELOW_50_ABOVE_200 |
| TBF | rates | -1.76 | 0.68 | 1.42 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.55 | -3.97 | -4.94 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.92 | -2.11 | -1.40 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.25 | -2.36 | -2.22 | BELOW_50_AND_200 |
| XLE | energy | -0.16 | 8.68 | 11.02 | ABOVE_50_AND_200 |
| XLU | defensives | 0.00 | -2.00 | -1.86 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
