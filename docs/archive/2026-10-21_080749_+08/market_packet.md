# Market Packet — 2026-10-21T08:07:49.531756+08:00

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
| SPY | 2026-10-19 | 766.48 | 0.42 | -1.49 | 0.63 | -0.25 | 5.66 | 47.12 | 0.93 | 0.00 | 1.06 | BELOW_50_ABOVE_200 |
| QQQ | 2026-10-19 | 718.36 | 1.21 | -3.71 | -0.43 | -1.14 | 6.36 | 41.15 | 1.52 | -1.06 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-19 | 705.44 | -0.55 | -5.05 | 5.96 | 7.29 | 11.58 | 49.24 | 3.48 | 5.33 | 6.39 | ABOVE_50_AND_200 |
| AMZN | 2026-10-19 | 262.45 | 4.98 | 1.13 | 3.44 | 2.19 | 8.05 | 57.26 | 2.44 | 2.82 | 3.87 | ABOVE_50_AND_200 |
| MU | 2026-10-19 | 904.90 | 2.97 | -8.51 | -10.92 | -8.01 | 25.52 | 38.36 | 5.33 | -11.55 | -10.49 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-19 | 129.59 | 1.06 | -5.68 | -12.21 | -10.48 | -18.94 | 41.03 | 5.30 | -12.84 | -11.78 | BELOW_50_AND_200 |
| SOFI | 2026-10-19 | 14.30 | -1.72 | -6.11 | -15.68 | -15.93 | -21.90 | 32.93 | 4.78 | -16.31 | -15.26 | BELOW_50_AND_200 |
| IAU | 2026-10-19 | 77.85 | -0.63 | -0.63 | -5.33 | -4.30 | -8.43 | 43.56 | 1.49 | -5.96 | -4.90 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-20 | 17.31 | -6.13 | 13.36 | 16.41 | 10.25 | MIXED |
| ^TNX | 2026-10-20 | 5.12 | -0.37 | -1.92 | 3.10 | 3.12 | ABOVE_50_AND_200 |
| CL=F | 2026-10-20 | 98.38 | -5.09 | 4.50 | 2.71 | 7.15 | ABOVE_50_AND_200 |
| GC=F | 2026-10-20 | 4132.90 | -0.65 | -1.06 | -5.73 | -5.29 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-20 | 101.79 | -0.18 | -0.38 | 1.36 | 1.35 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.56 | XLE, XOP, USO |
| semis_ai | 1.67 | SMH, SOXX |
| high_beta | 1.25 | IWM, ARKK, HIBL |
| rates | 0.62 | TLT, TBF, TBT |
| dollar | 0.28 | UUP |
| equity_hedges | -1.74 | SH, PSQ, SQQQ |
| housing_rates | -1.26 | XHB, ITB |
| defensives | -1.24 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 2.64 | -15.15 | -18.29 | BELOW_50_AND_200 |
| TBT | rates | 1.75 | 3.81 | 2.43 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.73 | -5.84 | -6.44 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.61 | -4.28 | -5.17 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.85 | 1.75 | 1.31 | ABOVE_50_AND_200 |
| ARKK | high_beta | 0.81 | -6.71 | -4.20 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.31 | -4.51 | -5.96 | BELOW_50_AND_200 |
| UUP | dollar | 0.28 | 2.15 | 2.03 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.55 | -0.92 | 1.93 | MIXED |
| XLU | defensives | -2.01 | 0.63 | -1.46 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.69 | -2.83 | -6.86 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -1.20 | -0.47 | 0.75 | MIXED |
| XHB | housing_rates | -0.82 | -2.34 | -6.19 | BELOW_50_AND_200 |
| TLT | rates | -0.74 | -2.20 | -1.49 | BELOW_50_AND_200 |
| XLE | energy | -0.64 | 5.43 | 6.37 | ABOVE_50_AND_200 |
| USO | energy | -0.59 | 4.54 | 12.03 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
