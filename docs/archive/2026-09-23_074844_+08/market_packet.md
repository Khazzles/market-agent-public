# Market Packet — 2026-09-23T07:48:44.029535+08:00

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
| SPY | 2026-09-22 | 773.38 | -0.02 | 2.11 | 1.00 | 1.68 | 7.83 | 58.31 | 0.87 | 0.00 | -3.77 | ABOVE_50_AND_200 |
| QQQ | 2026-09-22 | 747.46 | 0.81 | 6.09 | 4.77 | 5.13 | 12.60 | 67.96 | 1.33 | 3.77 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-22 | 736.60 | -0.63 | 9.90 | 33.95 | 20.67 | 17.83 | 76.04 | 3.54 | 32.95 | 29.18 | ABOVE_50_AND_200 |
| AMZN | 2026-09-22 | 254.98 | -1.34 | 2.64 | -1.41 | -0.50 | 6.01 | 49.22 | 2.34 | -2.41 | -6.18 | BELOW_50_ABOVE_200 |
| MU | 2026-09-22 | 1096.16 | 5.00 | 18.17 | 13.38 | 17.65 | 69.04 | 66.06 | 4.61 | 12.38 | 8.61 | ABOVE_50_AND_200 |
| ORCL | 2026-09-22 | 149.20 | 0.43 | 6.31 | 1.86 | 5.43 | -9.96 | 51.06 | 4.83 | 0.86 | -2.90 | MIXED |
| SOFI | 2026-09-22 | 17.16 | 1.12 | 0.53 | -9.25 | -2.83 | -11.52 | 45.93 | 4.28 | -10.25 | -14.02 | BELOW_50_AND_200 |
| IAU | 2026-09-22 | 82.03 | 0.44 | 1.55 | -5.48 | 1.56 | -3.84 | 49.96 | 1.83 | -6.48 | -10.25 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-22 | 14.21 | -4.44 | -17.38 | -10.35 | -11.64 | BELOW_50_AND_200 |
| ^TNX | 2026-09-22 | 4.97 | 0.10 | -0.56 | 4.85 | 4.96 | ABOVE_50_AND_200 |
| CL=F | 2026-09-22 | 89.65 | -6.40 | -15.29 | 2.98 | 2.91 | ABOVE_50_AND_200 |
| GC=F | 2026-09-22 | 4402.90 | 0.43 | 1.62 | -5.93 | 1.48 | MIXED |
| DX-Y.NYB | 2026-09-22 | 100.56 | 0.13 | 0.91 | 1.78 | 0.64 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.85 | XLE, XOP, USO |
| semis_ai | 2.16 | SMH, SOXX |
| high_beta | 1.59 | IWM, ARKK, HIBL |
| rates | -0.00 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -1.05 | SH, PSQ, SQQQ |
| housing_rates | 2.87 | XHB, ITB |
| defensives | 0.33 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 3.22 | 6.90 | 11.90 | ABOVE_50_AND_200 |
| ITB | housing_rates | 3.21 | -6.63 | -4.56 | BELOW_50_AND_200 |
| XHB | housing_rates | 2.53 | -6.66 | -5.22 | BELOW_50_AND_200 |
| SOXX | semis_ai | 2.40 | 10.14 | 8.97 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.92 | 8.39 | 7.53 | ABOVE_50_AND_200 |
| XLP | defensives | 0.99 | -3.79 | -2.48 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.98 | 6.26 | 13.21 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.57 | -4.25 | -2.58 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -2.75 | 7.01 | 7.65 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -2.40 | -13.45 | -14.92 | BELOW_50_AND_200 |
| XOP | energy | -1.70 | -4.18 | 0.18 | ABOVE_50_AND_200 |
| XLE | energy | -1.09 | -2.92 | 0.58 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.80 | -4.36 | -4.74 | BELOW_50_AND_200 |
| XLU | defensives | -0.32 | -5.24 | -7.09 | BELOW_50_AND_200 |
| TLT | rates | -0.06 | -0.37 | -0.93 | BELOW_50_AND_200 |
| UUP | dollar | 0.00 | 2.08 | 0.97 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
