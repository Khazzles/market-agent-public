# Market Packet — 2026-07-11T06:38:56.728496+08:00

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
| SPY | 2026-07-10 | 754.95 | 0.43 | 1.37 | 2.43 | 1.85 | 8.71 | 59.14 | 1.22 | 0.00 | -0.07 | ABOVE_50_AND_200 |
| QQQ | 2026-07-10 | 725.51 | 0.31 | 1.81 | 2.50 | 1.45 | 13.72 | 52.83 | 2.12 | 0.07 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-10 | 669.21 | 5.97 | 14.81 | 14.48 | 11.45 | 4.12 | 66.34 | 3.93 | 12.05 | 11.98 | ABOVE_50_AND_200 |
| AMZN | 2026-07-10 | 245.34 | -0.69 | 1.10 | 0.47 | -3.42 | 5.15 | 50.93 | 3.15 | -1.96 | -2.03 | BELOW_50_ABOVE_200 |
| MU | 2026-07-10 | 979.30 | -1.24 | 0.38 | 4.64 | 8.93 | 110.84 | 49.12 | 8.89 | 2.21 | 2.14 | ABOVE_50_AND_200 |
| ORCL | 2026-07-10 | 140.64 | -2.48 | 0.26 | -31.67 | -23.18 | -28.14 | 30.86 | 6.42 | -34.09 | -34.16 | BELOW_50_AND_200 |
| SOFI | 2026-07-10 | 18.78 | 0.86 | 2.96 | 14.03 | 11.48 | -14.93 | 60.34 | 5.05 | 11.60 | 11.53 | MIXED |
| IAU | 2026-07-10 | 77.26 | -0.32 | -0.32 | -3.51 | -6.01 | -8.20 | 42.89 | 2.01 | -5.94 | -6.01 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-10 | 15.03 | -5.11 | -6.93 | -24.36 | -13.45 | BELOW_50_AND_200 |
| ^TNX | 2026-07-10 | 4.57 | 0.66 | 2.10 | 0.37 | 2.10 | ABOVE_50_AND_200 |
| CL=F | 2026-07-10 | 71.51 | -0.79 | 4.11 | -18.92 | -18.61 | BELOW_50_AND_200 |
| GC=F | 2026-07-10 | 4128.90 | -0.04 | 0.39 | -3.08 | -5.60 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-10 | 100.97 | 0.02 | 0.10 | 1.06 | 1.27 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.12 | XLE, XOP, USO |
| semis_ai | 0.24 | SMH, SOXX |
| high_beta | -0.70 | IWM, ARKK, HIBL |
| rates | 0.00 | TLT, TBF, TBT |
| dollar | 0.11 | UUP |
| equity_hedges | -0.48 | SH, PSQ, SQQQ |
| housing_rates | 0.91 | XHB, ITB |
| defensives | 0.86 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLP | defensives | 1.11 | 0.02 | 0.03 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.93 | 1.49 | 2.93 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.90 | 1.55 | 2.67 | MIXED |
| XLU | defensives | 0.62 | 3.25 | 1.00 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.54 | 3.39 | 3.53 | ABOVE_50_AND_200 |
| XLE | energy | 0.47 | -4.03 | -2.95 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.11 | 1.36 | 1.68 | ABOVE_50_AND_200 |
| TBT | rates | 0.03 | 0.78 | 1.35 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -1.58 | 6.99 | 2.71 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -0.84 | -11.46 | -8.63 | BELOW_50_AND_200 |
| XOP | energy | -0.56 | -3.34 | -3.96 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.42 | 3.85 | 2.55 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.34 | -3.08 | -2.17 | BELOW_50_AND_200 |
| USO | energy | -0.28 | -17.21 | -15.37 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -0.27 | -3.45 | -2.26 | BELOW_50_AND_200 |
| HIBL | high_beta | -0.09 | 4.57 | 3.09 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
