# Market Packet — 2026-09-16T07:42:02.928177+08:00

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
| SPY | 2026-09-15 | 757.39 | -0.46 | -1.12 | -2.44 | -0.22 | 5.91 | 44.41 | 0.81 | 0.00 | 1.19 | BELOW_50_ABOVE_200 |
| QQQ | 2026-09-15 | 704.54 | -0.65 | -1.92 | -3.63 | -0.77 | 6.56 | 43.98 | 1.28 | -1.19 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-15 | 670.24 | 0.70 | 9.25 | 13.63 | 10.98 | 7.47 | 71.65 | 3.19 | 16.07 | 17.26 | ABOVE_50_AND_200 |
| AMZN | 2026-09-15 | 248.42 | -2.02 | -3.33 | -5.42 | -2.79 | 3.50 | 41.42 | 2.50 | -2.98 | -1.79 | BELOW_50_ABOVE_200 |
| MU | 2026-09-15 | 927.60 | 0.39 | -7.26 | -4.53 | 0.13 | 47.45 | 46.91 | 5.53 | -2.09 | -0.91 | ABOVE_50_AND_200 |
| ORCL | 2026-09-15 | 140.35 | -3.07 | -13.64 | -6.76 | -0.25 | -16.00 | 42.99 | 5.46 | -4.32 | -3.13 | BELOW_50_AND_200 |
| SOFI | 2026-09-15 | 17.07 | -3.29 | -5.22 | -6.67 | -4.03 | -13.35 | 43.81 | 4.42 | -4.23 | -3.04 | BELOW_50_AND_200 |
| IAU | 2026-09-15 | 80.78 | 0.30 | -1.43 | -1.82 | 0.60 | -5.24 | 44.65 | 1.88 | 0.62 | 1.81 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-15 | 17.20 | 0.58 | 9.41 | 13.23 | 6.37 | MIXED |
| ^TNX | 2026-09-15 | 5.00 | 0.71 | 3.95 | 6.39 | 6.48 | ABOVE_50_AND_200 |
| CL=F | 2026-09-15 | 105.46 | 4.01 | 13.36 | 27.99 | 24.63 | ABOVE_50_AND_200 |
| GC=F | 2026-09-15 | 4323.70 | -0.65 | -2.60 | -2.56 | 0.35 | MIXED |
| DX-Y.NYB | 2026-09-15 | 99.61 | 0.15 | 0.78 | -0.06 | -0.39 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.90 | XLE, XOP, USO |
| semis_ai | 0.20 | SMH, SOXX |
| high_beta | -1.54 | IWM, ARKK, HIBL |
| rates | 0.25 | TLT, TBF, TBT |
| dollar | 0.18 | UUP |
| equity_hedges | 1.04 | SH, PSQ, SQQQ |
| housing_rates | -0.78 | XHB, ITB |
| defensives | -1.01 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 3.32 | 27.85 | 24.68 | ABOVE_50_AND_200 |
| XOP | energy | 3.22 | 10.64 | 11.87 | ABOVE_50_AND_200 |
| XLE | energy | 2.17 | 6.49 | 8.76 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.98 | 12.09 | 1.78 | MIXED |
| TBT | rates | 0.71 | 2.91 | 4.75 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.69 | 4.20 | 1.09 | MIXED |
| SH | equity_hedges | 0.46 | 2.97 | 0.74 | MIXED |
| TBF | rates | 0.31 | 1.69 | 2.66 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -2.22 | -19.53 | -10.54 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -1.45 | 2.95 | 4.19 | ABOVE_50_AND_200 |
| XLU | defensives | -1.20 | -6.75 | -6.22 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.03 | -9.78 | -7.41 | BELOW_50_AND_200 |
| IWM | high_beta | -0.96 | -6.54 | -3.61 | BELOW_50_ABOVE_200 |
| XLP | defensives | -0.82 | -2.74 | -1.47 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -0.52 | -10.33 | -7.71 | BELOW_50_AND_200 |
| TLT | rates | -0.27 | -1.62 | -2.53 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
