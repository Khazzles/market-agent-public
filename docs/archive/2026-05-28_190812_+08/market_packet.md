# Market Packet — 2026-05-28T19:08:12.151585+08:00

## Manifest

- AS_OF policy: latest available market close per yfinance.

- Run timezone: Asia/Kuala_Lumpur

- Objective: public research packet only; no portfolio sizes, holdings, cost basis, or private notes.

- Core universe: SPY, QQQ, META, AMZN, MU, ORCL, SOFI, IAU

- Data source: yfinance for market prices and OHLCV-derived indicators.

- Interpretation layer: intended for downstream ChatGPT manager/supervisor review.


## Data Status

Potential issues:

- SMH: MISSING_DATA


## Core Universe Technical Evidence

| Ticker | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | vs SMA200 % | RSI14 | ATR14 % | RS vs SPY 21D | RS vs QQQ 21D | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 2026-05-27 | 750.46 | -0.02 | 2.28 | 4.93 | 7.20 | 10.36 | 71.12 | 0.96 | 0.00 | -4.88 | ABOVE_50_AND_200 |
| QQQ | 2026-05-27 | 729.45 | -0.11 | 3.98 | 9.82 | 12.67 | 18.37 | 74.61 | 1.47 | 4.88 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-27 | 635.26 | 3.74 | 5.42 | -6.39 | 2.80 | -4.90 | 56.86 | 2.51 | -11.32 | -16.21 | MIXED |
| AMZN | 2026-05-27 | 271.85 | 2.47 | 4.82 | 4.11 | 11.29 | 17.68 | 62.65 | 2.48 | -0.83 | -5.71 | ABOVE_50_AND_200 |
| MU | 2026-05-27 | 928.41 | 3.63 | 32.87 | 76.99 | 72.52 | 180.89 | 76.45 | 6.11 | 72.05 | 67.17 | ABOVE_50_AND_200 |
| ORCL | 2026-05-27 | 190.96 | -1.09 | 5.24 | 10.41 | 13.22 | -7.93 | 57.87 | 4.28 | 5.47 | 0.59 | MIXED |
| SOFI | 2026-05-27 | 16.17 | 1.19 | 6.17 | -13.81 | -3.16 | -30.51 | 48.40 | 4.90 | -18.74 | -23.62 | BELOW_50_AND_200 |
| IAU | 2026-05-27 | 83.73 | -1.27 | -0.70 | -4.93 | -4.21 | 1.92 | 36.49 | 1.84 | -9.86 | -14.75 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-28 | 16.75 | 2.82 | -0.06 | -10.95 | -16.86 | BELOW_50_AND_200 |
| ^TNX | 2026-05-27 | 4.48 | -0.27 | -3.99 | 3.34 | 2.30 | ABOVE_50_AND_200 |
| CL=F | 2026-05-28 | 91.06 | 2.68 | -7.33 | -8.88 | -7.16 | BELOW_50_ABOVE_200 |
| GC=F | 2026-05-28 | 4413.70 | -0.76 | -2.60 | -3.87 | -4.78 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-28 | 99.39 | 0.19 | 0.29 | 0.78 | 0.47 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.50 | XLE, XOP, USO |
| semis_ai | -1.07 | SMH, SOXX |
| high_beta | 0.54 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | 0.16 | SH, PSQ, SQQQ |
| housing_rates | 1.28 | XHB, ITB |
| defensives | 0.36 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 1.61 | -5.83 | 0.74 | MIXED |
| XLP | defensives | 1.14 | 2.72 | 1.85 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.95 | -4.69 | 1.37 | MIXED |
| ARKK | high_beta | 0.93 | 1.83 | 5.28 | MIXED |
| HIBL | high_beta | 0.73 | 26.52 | 38.50 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.41 | -24.80 | -33.51 | BELOW_50_AND_200 |
| TLT | rates | 0.23 | -1.14 | -0.77 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.12 | -8.71 | -11.64 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -4.36 | -2.74 | -1.00 | BELOW_50_ABOVE_200 |
| XOP | energy | -1.65 | -3.61 | -5.42 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.49 | 0.39 | -2.43 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -1.07 | 23.84 | 31.64 | ABOVE_50_AND_200 |
| XLU | defensives | -0.42 | -2.27 | -1.23 | BELOW_50_ABOVE_200 |
| TBT | rates | -0.22 | 2.44 | 1.66 | ABOVE_50_AND_200 |
| TBF | rates | -0.20 | 1.27 | 0.97 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.05 | 4.77 | 8.22 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
