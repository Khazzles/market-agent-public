# Market Packet — 2026-08-01T06:40:23.664615+08:00

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
| SPY | 2026-07-31 | 747.03 | 0.72 | 1.10 | 0.17 | 0.27 | 6.66 | 52.99 | 1.21 | 0.00 | 5.30 | ABOVE_50_AND_200 |
| QQQ | 2026-07-31 | 687.99 | 0.65 | 0.55 | -5.13 | -3.79 | 6.66 | 45.09 | 2.22 | -5.30 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-31 | 556.71 | 3.28 | -6.47 | -9.17 | -7.55 | -12.26 | 37.83 | 4.52 | -9.34 | -4.04 | BELOW_50_AND_200 |
| AMZN | 2026-07-31 | 271.58 | 15.32 | 17.00 | 12.36 | 10.12 | 15.56 | 67.88 | 3.50 | 12.19 | 17.49 | ABOVE_50_AND_200 |
| MU | 2026-07-31 | 823.03 | -5.90 | -10.63 | -20.27 | -14.70 | 58.85 | 43.58 | 11.00 | -20.44 | -15.14 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-31 | 129.87 | 1.81 | 12.94 | -8.86 | -21.25 | -29.08 | 43.80 | 5.96 | -9.03 | -3.74 | BELOW_50_AND_200 |
| SOFI | 2026-07-31 | 16.31 | -0.97 | -0.91 | -11.55 | -5.12 | -23.47 | 44.04 | 5.65 | -11.72 | -6.42 | BELOW_50_AND_200 |
| IAU | 2026-07-31 | 76.17 | -1.46 | -0.08 | 0.28 | -3.53 | -9.72 | 45.87 | 1.92 | 0.11 | 5.40 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-31 | 15.99 | -6.44 | -13.94 | -3.62 | -7.98 | BELOW_50_AND_200 |
| ^TNX | 2026-07-31 | 4.75 | 1.76 | 1.41 | 6.03 | 4.79 | ABOVE_50_AND_200 |
| CL=F | 2026-07-31 | 86.80 | 3.84 | -2.81 | 26.57 | 5.53 | ABOVE_50_AND_200 |
| GC=F | 2026-07-31 | 4098.60 | -0.04 | 0.76 | 0.74 | -2.46 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-31 | 99.80 | -0.21 | -1.64 | -1.57 | -0.62 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.26 | XLE, XOP, USO |
| semis_ai | 0.19 | SMH, SOXX |
| high_beta | -0.80 | IWM, ARKK, HIBL |
| rates | 0.49 | TLT, TBF, TBT |
| dollar | 0.11 | UUP |
| equity_hedges | -1.09 | SH, PSQ, SQQQ |
| housing_rates | -0.99 | XHB, ITB |
| defensives | -0.59 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | 1.45 | 15.38 | 7.93 | ABOVE_50_AND_200 |
| TBT | rates | 1.34 | 8.71 | 6.51 | ABOVE_50_AND_200 |
| USO | energy | 1.33 | 25.08 | 4.76 | ABOVE_50_AND_200 |
| XLE | energy | 1.00 | 12.76 | 5.08 | ABOVE_50_AND_200 |
| TBF | rates | 0.79 | 4.68 | 3.37 | ABOVE_50_AND_200 |
| HIBL | high_beta | 0.35 | -24.64 | -17.66 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.30 | -12.88 | -9.33 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.11 | -1.12 | -0.08 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -2.28 | -12.96 | -8.06 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -1.99 | 15.44 | 8.10 | MIXED |
| ITB | housing_rates | -1.18 | -7.64 | -2.54 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.79 | -7.94 | -3.39 | BELOW_50_AND_200 |
| XLU | defensives | -0.69 | -0.94 | -1.41 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.69 | 0.33 | -0.32 | BELOW_50_AND_200 |
| TLT | rates | -0.66 | -3.82 | -3.23 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.59 | 5.59 | 3.39 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
