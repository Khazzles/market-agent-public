# Market Packet — 2026-08-28T13:36:16.232160+08:00

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
| SPY | 2026-08-27 | 771.10 | 0.66 | 1.11 | 5.71 | 2.35 | 8.70 | 58.59 | 0.81 | 0.00 | -3.27 | ABOVE_50_AND_200 |
| QQQ | 2026-08-27 | 721.11 | 1.37 | 1.43 | 8.97 | 1.25 | 10.14 | 54.76 | 1.46 | 3.27 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-27 | 571.10 | -0.87 | 4.63 | -2.48 | -3.52 | -8.33 | 46.93 | 3.54 | -8.19 | -11.45 | BELOW_50_AND_200 |
| AMZN | 2026-08-27 | 256.26 | -1.54 | -1.48 | 13.06 | 2.06 | 7.41 | 47.23 | 2.62 | 7.36 | 4.09 | ABOVE_50_AND_200 |
| MU | 2026-08-27 | 935.39 | -0.32 | -4.00 | 26.58 | -2.28 | 59.89 | 50.99 | 6.65 | 20.87 | 17.60 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-27 | 151.94 | 2.06 | 6.95 | 29.05 | 6.85 | -11.20 | 57.25 | 4.40 | 23.34 | 20.07 | MIXED |
| SOFI | 2026-08-27 | 19.18 | 1.80 | 7.03 | 25.77 | 7.65 | -5.60 | 58.44 | 4.39 | 20.06 | 16.80 | MIXED |
| IAU | 2026-08-27 | 86.62 | 0.29 | 1.75 | 13.91 | 9.58 | 1.97 | 66.75 | 1.70 | 8.21 | 4.94 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-27 | 14.51 | -4.60 | -9.37 | -29.77 | -12.53 | BELOW_50_AND_200 |
| ^TNX | 2026-08-27 | 4.67 | 0.17 | -0.51 | 1.08 | 1.67 | ABOVE_50_AND_200 |
| CL=F | 2026-08-28 | 83.24 | -0.35 | -4.39 | -0.42 | 4.97 | ABOVE_50_AND_200 |
| GC=F | 2026-08-28 | 4637.60 | 0.61 | 0.29 | 13.11 | 10.11 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-28 | 99.19 | 0.04 | 0.40 | -0.81 | -1.21 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.80 | XLE, XOP, USO |
| semis_ai | 2.52 | SMH, SOXX |
| high_beta | 1.40 | IWM, ARKK, HIBL |
| rates | 0.07 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -2.01 | SH, PSQ, SQQQ |
| housing_rates | -1.56 | XHB, ITB |
| defensives | -1.07 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SMH | semis_ai | 3.10 | 13.64 | -1.90 | BELOW_50_ABOVE_200 |
| USO | energy | 2.09 | 0.54 | 7.75 | ABOVE_50_AND_200 |
| HIBL | high_beta | 2.03 | 35.22 | 1.25 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.95 | 13.00 | -4.80 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 1.87 | 23.80 | 10.76 | ABOVE_50_AND_200 |
| XOP | energy | 0.55 | 7.81 | 9.59 | ABOVE_50_AND_200 |
| TBT | rates | 0.29 | -1.37 | 1.56 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.29 | 3.90 | 0.88 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -4.06 | -23.58 | -5.15 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.73 | -0.98 | -2.96 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.40 | -0.15 | -3.92 | BELOW_50_AND_200 |
| XLP | defensives | -1.38 | -2.61 | 0.29 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.35 | -8.10 | -1.16 | BELOW_50_AND_200 |
| XLU | defensives | -0.76 | -3.85 | -3.45 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.62 | -4.95 | -1.90 | BELOW_50_AND_200 |
| XLE | energy | -0.22 | 6.21 | 7.41 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
