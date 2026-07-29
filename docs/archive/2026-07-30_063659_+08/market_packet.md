# Market Packet — 2026-07-30T06:36:59.366017+08:00

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
| SPY | 2026-07-29 | 729.46 | -1.54 | -2.40 | -1.56 | -2.04 | 4.28 | 38.63 | 1.17 | 0.00 | 7.05 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-29 | 661.73 | -2.04 | -6.18 | -8.61 | -7.55 | 2.73 | 32.40 | 2.21 | -7.05 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-29 | 585.61 | -1.31 | -6.63 | 4.09 | -3.13 | -7.94 | 41.44 | 3.91 | 5.65 | 12.70 | BELOW_50_AND_200 |
| AMZN | 2026-07-29 | 226.65 | -1.82 | -7.43 | -5.62 | -8.23 | -3.41 | 33.31 | 3.04 | -4.06 | 2.99 | BELOW_50_AND_200 |
| MU | 2026-07-29 | 739.00 | -9.94 | -22.98 | -35.47 | -22.90 | 44.48 | 35.69 | 11.45 | -33.92 | -26.86 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-29 | 117.74 | -1.85 | -6.44 | -20.32 | -29.55 | -36.30 | 31.54 | 6.46 | -18.76 | -11.71 | BELOW_50_AND_200 |
| SOFI | 2026-07-29 | 15.25 | -8.90 | -10.66 | -16.16 | -11.10 | -28.78 | 34.38 | 6.02 | -14.61 | -7.55 | BELOW_50_AND_200 |
| IAU | 2026-07-29 | 76.04 | 0.45 | -2.12 | 0.68 | -4.10 | -9.87 | 44.76 | 1.90 | 2.23 | 9.29 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-29 | 20.66 | 13.45 | 24.16 | 17.05 | 18.56 | ABOVE_50_AND_200 |
| ^TNX | 2026-07-29 | 4.62 | 0.39 | -0.75 | 5.67 | 2.13 | ABOVE_50_AND_200 |
| CL=F | 2026-07-29 | 84.44 | 6.54 | -2.75 | 19.35 | 1.52 | ABOVE_50_AND_200 |
| GC=F | 2026-07-29 | 4130.60 | 2.34 | -0.39 | 2.69 | -2.14 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-29 | 100.80 | -0.57 | -0.33 | -0.30 | 0.41 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 4.20 | XLE, XOP, USO |
| semis_ai | -5.09 | SMH, SOXX |
| high_beta | -4.94 | IWM, ARKK, HIBL |
| rates | 1.25 | TLT, TBF, TBT |
| dollar | -0.56 | UUP |
| equity_hedges | 3.32 | SH, PSQ, SQQQ |
| housing_rates | -4.13 | XHB, ITB |
| defensives | -0.50 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 7.32 | 20.76 | 4.11 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 6.30 | 29.56 | 22.24 | MIXED |
| TBT | rates | 3.71 | 11.38 | 5.22 | ABOVE_50_AND_200 |
| XOP | energy | 3.41 | 10.73 | 4.63 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 2.12 | 9.58 | 7.62 | MIXED |
| XLE | energy | 1.88 | 9.46 | 3.37 | ABOVE_50_AND_200 |
| TBF | rates | 1.69 | 5.64 | 2.50 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.53 | 2.01 | 1.94 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -10.60 | -34.87 | -26.98 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -5.38 | -24.31 | -18.04 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -4.79 | -20.22 | -15.45 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -4.52 | -9.28 | -2.16 | BELOW_50_AND_200 |
| ITB | housing_rates | -3.74 | -7.11 | 0.11 | MIXED |
| ARKK | high_beta | -2.58 | -12.46 | -9.01 | BELOW_50_AND_200 |
| TLT | rates | -1.65 | -5.26 | -2.56 | BELOW_50_AND_200 |
| IWM | high_beta | -1.64 | -3.48 | -1.10 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
