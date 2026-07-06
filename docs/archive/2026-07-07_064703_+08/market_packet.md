# Market Packet — 2026-07-07T06:47:03.275269+08:00

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
| SPY | 2026-07-06 | 751.28 | 0.87 | 3.06 | -0.39 | 1.77 | 8.45 | 57.59 | 1.33 | 0.00 | 2.48 | ABOVE_50_AND_200 |
| QQQ | 2026-07-06 | 722.82 | 1.43 | 2.31 | -2.87 | 1.73 | 13.72 | 51.60 | 2.26 | -2.48 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-06 | 600.29 | 2.98 | 9.09 | -3.64 | -0.57 | -7.02 | 53.95 | 3.74 | -3.25 | -0.77 | BELOW_50_AND_200 |
| AMZN | 2026-07-06 | 244.16 | 0.61 | 4.93 | -2.34 | -4.32 | 4.77 | 50.05 | 3.27 | -1.95 | 0.53 | BELOW_50_ABOVE_200 |
| MU | 2026-07-06 | 984.75 | 0.94 | -13.03 | -8.78 | 14.24 | 119.58 | 49.04 | 9.45 | -8.39 | -5.91 | ABOVE_50_AND_200 |
| ORCL | 2026-07-06 | 143.76 | 2.49 | -3.21 | -37.59 | -22.50 | -27.78 | 30.05 | 6.81 | -37.19 | -34.71 | BELOW_50_AND_200 |
| SOFI | 2026-07-06 | 18.61 | 2.03 | 4.08 | 11.57 | 10.34 | -16.49 | 61.15 | 5.11 | 11.96 | 14.44 | MIXED |
| IAU | 2026-07-06 | 78.30 | 1.02 | 2.27 | -6.33 | -5.73 | -6.79 | 45.25 | 2.09 | -5.94 | -3.45 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-06 | 15.57 | -3.59 | -15.43 | -3.05 | -11.30 | BELOW_50_AND_200 |
| ^TNX | 2026-07-06 | 4.48 | -0.13 | 2.45 | -0.27 | 0.43 | ABOVE_50_AND_200 |
| CL=F | 2026-07-06 | 68.67 | -0.03 | -0.81 | -28.48 | -23.57 | BELOW_50_AND_200 |
| GC=F | 2026-07-06 | 4179.00 | 1.61 | 2.46 | -5.81 | -5.42 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-06 | 100.86 | -0.01 | -0.50 | 1.33 | 1.36 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.08 | XLE, XOP, USO |
| semis_ai | 2.35 | SMH, SOXX |
| high_beta | 2.74 | IWM, ARKK, HIBL |
| rates | 0.16 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | -2.14 | SH, PSQ, SQQQ |
| housing_rates | -1.34 | XHB, ITB |
| defensives | -1.03 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.89 | -8.23 | 7.18 | ABOVE_50_AND_200 |
| ARKK | high_beta | 2.90 | 6.97 | 7.52 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 2.68 | -5.55 | 5.99 | ABOVE_50_AND_200 |
| SMH | semis_ai | 2.03 | -5.27 | 3.82 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.44 | 3.90 | 4.14 | ABOVE_50_AND_200 |
| USO | energy | 0.36 | -25.92 | -20.03 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.29 | -0.73 | -0.45 | BELOW_50_ABOVE_200 |
| TBT | rates | 0.25 | -1.14 | -0.80 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -4.18 | 2.93 | -9.96 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.55 | 9.57 | 6.24 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.43 | 1.63 | -2.70 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.13 | 7.12 | 5.44 | ABOVE_50_AND_200 |
| XLP | defensives | -1.05 | 2.36 | 0.11 | ABOVE_50_AND_200 |
| XLU | defensives | -1.01 | 3.64 | 0.61 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.82 | -0.42 | -2.24 | BELOW_50_AND_200 |
| XOP | energy | -0.44 | -10.03 | -7.22 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
