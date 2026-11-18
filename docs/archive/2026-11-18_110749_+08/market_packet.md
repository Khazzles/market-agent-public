# Market Packet — 2026-11-18T11:07:49.634046+08:00

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
| SPY | 2026-11-17 | 732.44 | -1.01 | -2.33 | -4.44 | -4.02 | 0.01 | 37.47 | 1.57 | 0.00 | 4.11 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-17 | 656.95 | -0.73 | -2.64 | -8.55 | -8.18 | -3.76 | 36.53 | 2.52 | -4.11 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-17 | 618.87 | -1.20 | -3.51 | -12.27 | -9.00 | -1.75 | 42.04 | 3.57 | -7.83 | -3.72 | BELOW_50_AND_200 |
| AMZN | 2026-11-17 | 257.89 | 0.05 | -4.79 | -1.74 | 1.21 | 5.36 | 49.75 | 3.46 | 2.70 | 6.81 | ABOVE_50_AND_200 |
| MU | 2026-11-17 | 712.42 | -0.92 | -1.75 | -21.27 | -23.57 | -7.30 | 37.54 | 8.32 | -16.83 | -12.72 | BELOW_50_AND_200 |
| ORCL | 2026-11-17 | 115.00 | -3.43 | -2.53 | -11.26 | -14.77 | -25.16 | 39.98 | 6.94 | -6.82 | -2.71 | BELOW_50_AND_200 |
| SOFI | 2026-11-17 | 14.28 | -3.84 | -12.77 | -0.14 | -10.93 | -17.19 | 36.87 | 5.66 | 4.30 | 8.41 | BELOW_50_AND_200 |
| IAU | 2026-11-17 | 72.27 | -0.10 | -4.58 | -7.17 | -6.97 | -13.48 | 36.22 | 1.86 | -2.73 | 1.38 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-17 | 25.46 | 11.13 | 30.83 | 38.07 | 44.17 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-17 | 5.10 | -0.35 | 2.41 | -0.64 | 0.62 | ABOVE_50_AND_200 |
| CL=F | 2026-11-17 | 85.06 | -0.77 | -1.14 | -17.94 | -10.55 | BELOW_50_AND_200 |
| GC=F | 2026-11-17 | 3802.60 | -1.31 | -5.65 | -8.59 | -8.51 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-17 | 103.61 | 0.06 | 1.35 | 1.60 | 1.98 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.56 | XLE, XOP, USO |
| semis_ai | -0.11 | SMH, SOXX |
| high_beta | -1.95 | IWM, ARKK, HIBL |
| rates | -0.07 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 1.35 | SH, PSQ, SQQQ |
| housing_rates | -1.85 | XHB, ITB |
| defensives | -1.41 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.29 | 25.13 | 23.03 | MIXED |
| SH | equity_hedges | 1.04 | 4.89 | 4.27 | MIXED |
| PSQ | equity_hedges | 0.72 | 8.91 | 8.22 | ABOVE_50_AND_200 |
| TLT | rates | 0.21 | 0.11 | -0.69 | BELOW_50_AND_200 |
| SOXX | semis_ai | 0.17 | -15.45 | -17.06 | BELOW_50_AND_200 |
| USO | energy | 0.15 | -12.79 | -8.13 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.07 | 1.86 | 2.35 | ABOVE_50_AND_200 |
| TBF | rates | -0.19 | -0.19 | 0.63 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -3.44 | -31.38 | -36.43 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.90 | 5.27 | 0.68 | MIXED |
| ITB | housing_rates | -1.81 | 7.99 | 2.08 | MIXED |
| XLU | defensives | -1.59 | 4.98 | 3.60 | MIXED |
| IWM | high_beta | -1.43 | -0.82 | -3.84 | BELOW_50_AND_200 |
| XOP | energy | -1.32 | -10.96 | -6.38 | BELOW_50_ABOVE_200 |
| XLP | defensives | -1.23 | 4.87 | 6.40 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.99 | -13.94 | -15.78 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
