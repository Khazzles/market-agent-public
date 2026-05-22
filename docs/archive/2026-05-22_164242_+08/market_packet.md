# Market Packet — 2026-05-22T16:42:42.145675+08:00

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
| SPY | 2026-05-21 | 742.72 | 0.20 | -0.73 | 4.43 | 6.85 | 9.50 | 67.21 | 1.04 | 0.00 | -4.64 | ABOVE_50_AND_200 |
| QQQ | 2026-05-21 | 714.51 | 0.19 | -0.73 | 9.07 | 11.69 | 16.39 | 70.31 | 1.53 | 4.64 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-21 | 607.38 | 0.38 | -1.79 | -9.98 | -1.78 | -9.38 | 43.84 | 2.62 | -14.41 | -19.05 | BELOW_50_AND_200 |
| AMZN | 2026-05-21 | 268.46 | 1.30 | 0.46 | 5.13 | 11.49 | 16.55 | 60.81 | 2.57 | 0.70 | -3.94 | ABOVE_50_AND_200 |
| MU | 2026-05-21 | 762.10 | 4.11 | -1.79 | 56.33 | 48.82 | 138.65 | 66.92 | 6.37 | 51.90 | 47.27 | ABOVE_50_AND_200 |
| ORCL | 2026-05-21 | 189.77 | 0.86 | -2.99 | 1.21 | 13.94 | -8.90 | 57.86 | 4.65 | -3.22 | -7.86 | MIXED |
| SOFI | 2026-05-21 | 15.65 | -0.25 | -2.31 | -17.89 | -6.87 | -33.00 | 42.98 | 4.93 | -22.32 | -26.96 | BELOW_50_AND_200 |
| IAU | 2026-05-21 | 85.43 | -0.12 | -2.41 | -4.22 | -2.96 | 4.38 | 42.08 | 1.87 | -8.65 | -13.28 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-22 | 16.74 | -0.12 | -9.17 | -13.31 | -19.43 | BELOW_50_AND_200 |
| ^TNX | 2026-05-21 | 4.59 | 0.31 | 2.80 | 6.80 | 5.06 | ABOVE_50_AND_200 |
| CL=F | 2026-05-22 | 98.71 | 2.45 | -6.37 | 2.98 | 0.29 | ABOVE_50_AND_200 |
| GC=F | 2026-05-22 | 4524.70 | -0.33 | -0.68 | -3.83 | -3.09 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-22 | 99.25 | 0.06 | -0.02 | 0.46 | 0.29 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.55 | XLE, XOP, USO |
| semis_ai | 0.71 | SMH, SOXX |
| high_beta | 2.30 | IWM, ARKK, HIBL |
| rates | -0.29 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -0.33 | SH, PSQ, SQQQ |
| housing_rates | 0.70 | XHB, ITB |
| defensives | 0.05 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.93 | 12.20 | 26.39 | ABOVE_50_AND_200 |
| XLU | defensives | 1.10 | 0.29 | -1.75 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 1.03 | -3.38 | 4.01 | MIXED |
| IWM | high_beta | 0.94 | 2.17 | 6.26 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.85 | 21.53 | 26.44 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.75 | -8.97 | -2.29 | BELOW_50_AND_200 |
| XHB | housing_rates | 0.65 | -8.50 | -2.25 | BELOW_50_AND_200 |
| SMH | semis_ai | 0.57 | 19.09 | 22.26 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | -2.33 | 1.42 | -1.21 | BELOW_50_ABOVE_200 |
| USO | energy | -1.20 | 10.15 | 8.60 | ABOVE_50_AND_200 |
| XLE | energy | -1.12 | 4.58 | 1.27 | ABOVE_50_AND_200 |
| XLP | defensives | -1.01 | 3.11 | 1.92 | ABOVE_50_AND_200 |
| TBT | rates | -0.81 | 5.87 | 4.09 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -0.55 | -23.33 | -31.64 | BELOW_50_AND_200 |
| TBF | rates | -0.44 | 3.10 | 2.24 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.23 | -8.16 | -10.92 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
