# Market Packet — 2026-07-16T06:38:55.202238+08:00

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
| SPY | 2026-07-15 | 754.81 | 0.40 | 1.26 | 1.76 | 1.54 | 8.47 | 58.04 | 1.13 | 0.00 | 2.26 | ABOVE_50_AND_200 |
| QQQ | 2026-07-15 | 717.74 | -0.27 | 0.89 | -0.50 | -0.05 | 12.18 | 49.95 | 2.09 | -2.26 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-15 | 681.31 | 3.07 | 12.96 | 20.16 | 13.06 | 6.22 | 66.80 | 3.77 | 18.40 | 20.66 | ABOVE_50_AND_200 |
| AMZN | 2026-07-15 | 254.96 | 3.02 | 4.65 | 6.88 | 0.73 | 9.06 | 60.14 | 2.93 | 5.12 | 7.38 | ABOVE_50_AND_200 |
| MU | 2026-07-15 | 904.28 | -8.02 | -4.69 | -7.88 | -2.13 | 89.90 | 44.36 | 9.52 | -9.64 | -7.38 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-15 | 132.49 | 3.56 | -5.69 | -28.05 | -26.79 | -31.39 | 30.42 | 6.47 | -29.81 | -27.55 | BELOW_50_AND_200 |
| SOFI | 2026-07-15 | 17.87 | -3.67 | 0.79 | 7.78 | 5.27 | -18.48 | 51.06 | 5.41 | 6.02 | 8.28 | MIXED |
| IAU | 2026-07-15 | 76.28 | 0.01 | -0.60 | -3.67 | -6.49 | -9.45 | 41.39 | 2.07 | -5.44 | -3.18 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-15 | 15.67 | -5.03 | -7.28 | -11.37 | -9.46 | BELOW_50_AND_200 |
| ^TNX | 2026-07-15 | 4.54 | -0.87 | -0.53 | 1.29 | 1.26 | ABOVE_50_AND_200 |
| CL=F | 2026-07-15 | 80.34 | 1.26 | 9.28 | -5.35 | -6.95 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-15 | 4067.60 | 0.16 | -0.08 | -3.50 | -6.28 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-15 | 100.50 | -0.44 | -0.55 | 0.75 | 0.65 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.13 | XLE, XOP, USO |
| semis_ai | -1.91 | SMH, SOXX |
| high_beta | -0.47 | IWM, ARKK, HIBL |
| rates | -0.05 | TLT, TBF, TBT |
| dollar | -0.49 | UUP |
| equity_hedges | 0.25 | SH, PSQ, SQQQ |
| housing_rates | 0.77 | XHB, ITB |
| defensives | -0.48 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 1.01 | -3.23 | -4.29 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | 0.83 | 1.02 | 2.75 | MIXED |
| SQQQ | equity_hedges | 0.80 | -2.75 | -4.09 | BELOW_50_AND_200 |
| XHB | housing_rates | 0.70 | 1.24 | 3.05 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.43 | 0.96 | 2.09 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.31 | -0.50 | -0.73 | BELOW_50_AND_200 |
| TLT | rates | 0.19 | -1.78 | -1.28 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.10 | 5.22 | 1.60 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | -2.23 | -6.87 | -1.59 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -1.95 | -7.85 | -3.66 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -1.59 | -4.71 | -0.78 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.03 | 1.55 | 0.68 | ABOVE_50_AND_200 |
| XLE | energy | -0.79 | -1.82 | -0.19 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.60 | -0.29 | 0.29 | ABOVE_50_AND_200 |
| UUP | dollar | -0.49 | 1.07 | 0.98 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.37 | -2.47 | -1.85 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
