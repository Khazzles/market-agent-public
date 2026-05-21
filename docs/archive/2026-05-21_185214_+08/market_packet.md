# Market Packet — 2026-05-21T18:52:14.873218+08:00

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
| SPY | 2026-05-20 | 741.25 | 1.02 | -0.14 | 5.28 | 6.85 | 9.37 | 66.42 | 1.04 | 0.00 | -5.40 | ABOVE_50_AND_200 |
| QQQ | 2026-05-20 | 713.15 | 1.66 | -0.22 | 10.68 | 11.86 | 16.31 | 69.85 | 1.54 | 5.40 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-20 | 605.06 | 0.41 | -1.88 | -9.54 | -2.30 | -9.83 | 42.66 | 2.64 | -14.82 | -20.22 | BELOW_50_AND_200 |
| AMZN | 2026-05-20 | 265.01 | 2.19 | -1.90 | 6.04 | 10.57 | 15.19 | 57.72 | 2.57 | 0.76 | -4.64 | ABOVE_50_AND_200 |
| MU | 2026-05-20 | 731.99 | 4.76 | -8.91 | 62.89 | 44.88 | 131.58 | 64.36 | 6.79 | 57.61 | 52.21 | ABOVE_50_AND_200 |
| ORCL | 2026-05-20 | 188.16 | 3.69 | -0.84 | 3.86 | 13.34 | -9.81 | 56.79 | 4.82 | -1.42 | -6.82 | MIXED |
| SOFI | 2026-05-20 | 15.69 | 3.02 | 2.48 | -16.68 | -6.95 | -32.91 | 43.27 | 5.08 | -21.95 | -27.36 | BELOW_50_AND_200 |
| IAU | 2026-05-20 | 85.53 | 1.44 | -3.02 | -2.85 | -3.11 | 4.65 | 42.40 | 1.90 | -8.13 | -13.53 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-21 | 17.56 | 0.69 | 1.74 | -7.19 | -16.40 | BELOW_50_AND_200 |
| ^TNX | 2026-05-20 | 4.57 | -2.04 | 2.03 | 6.52 | 4.92 | ABOVE_50_AND_200 |
| CL=F | 2026-05-21 | 100.91 | 2.70 | -0.26 | 8.55 | 2.49 | ABOVE_50_AND_200 |
| GC=F | 2026-05-21 | 4511.50 | -0.44 | -3.56 | -4.67 | -3.60 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-21 | 99.31 | 0.21 | 0.44 | 0.73 | 0.34 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -3.42 | XLE, XOP, USO |
| semis_ai | 4.28 | SMH, SOXX |
| high_beta | 4.77 | IWM, ARKK, HIBL |
| rates | -0.72 | TLT, TBF, TBT |
| dollar | -0.22 | UUP |
| equity_hedges | -2.51 | SH, PSQ, SQQQ |
| housing_rates | 4.41 | XHB, ITB |
| defensives | -0.14 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 9.07 | 10.16 | 21.51 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 4.74 | 23.68 | 26.49 | ABOVE_50_AND_200 |
| ITB | housing_rates | 4.53 | -10.00 | -3.12 | BELOW_50_AND_200 |
| XHB | housing_rates | 4.28 | -9.08 | -2.94 | BELOW_50_AND_200 |
| SMH | semis_ai | 3.81 | 21.52 | 22.45 | ABOVE_50_AND_200 |
| ARKK | high_beta | 2.71 | -1.99 | 3.05 | MIXED |
| IWM | high_beta | 2.52 | 1.95 | 5.51 | ABOVE_50_AND_200 |
| TLT | rates | 1.07 | -3.07 | -2.58 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -5.68 | 12.49 | 10.50 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -4.91 | -26.74 | -31.90 | BELOW_50_AND_200 |
| XLE | energy | -2.43 | 7.03 | 2.49 | ABOVE_50_AND_200 |
| TBT | rates | -2.21 | 6.40 | 5.06 | ABOVE_50_AND_200 |
| XOP | energy | -2.14 | 5.90 | 1.22 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.62 | -9.42 | -10.99 | BELOW_50_AND_200 |
| TBF | rates | -1.03 | 3.38 | 2.76 | ABOVE_50_AND_200 |
| SH | equity_hedges | -1.00 | -4.59 | -6.33 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
