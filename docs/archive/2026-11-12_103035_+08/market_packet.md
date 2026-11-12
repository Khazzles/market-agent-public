# Market Packet — 2026-11-12T10:30:35.236261+08:00

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
| SPY | 2026-11-10 | 749.92 | -0.37 | -0.59 | -3.62 | -1.97 | 2.59 | 44.55 | 1.48 | 0.00 | 5.93 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-10 | 674.76 | -0.68 | -1.54 | -9.55 | -6.20 | -0.98 | 40.12 | 2.43 | -5.93 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-10 | 641.39 | 0.00 | 3.28 | -13.67 | -5.34 | 1.53 | 46.50 | 3.72 | -10.05 | -4.12 | BELOW_50_ABOVE_200 |
| AMZN | 2026-11-10 | 270.87 | 1.48 | 8.05 | 4.37 | 6.57 | 10.90 | 61.57 | 3.49 | 7.99 | 13.92 | ABOVE_50_AND_200 |
| MU | 2026-11-10 | 725.11 | -1.10 | -15.20 | -26.69 | -23.91 | -4.60 | 35.82 | 8.39 | -23.06 | -17.13 | BELOW_50_AND_200 |
| ORCL | 2026-11-10 | 117.98 | -1.51 | -6.51 | -14.13 | -14.43 | -23.78 | 40.71 | 7.10 | -10.51 | -4.57 | BELOW_50_AND_200 |
| SOFI | 2026-11-10 | 16.37 | -2.27 | -2.39 | 7.49 | 0.45 | -6.24 | 51.62 | 5.10 | 11.11 | 17.04 | MIXED |
| IAU | 2026-11-10 | 75.74 | -2.62 | 2.81 | -3.32 | -3.69 | -9.94 | 45.89 | 1.84 | 0.30 | 6.24 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-11 | 17.49 | -10.12 | 5.30 | 14.54 | 2.10 | MIXED |
| ^TNX | 2026-11-11 | 5.00 | 0.30 | 2.13 | -4.20 | -0.93 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-11 | 86.01 | -0.03 | -2.39 | -8.64 | -9.90 | BELOW_50_AND_200 |
| GC=F | 2026-11-11 | 3993.10 | -0.92 | -1.96 | -4.41 | -5.04 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-11 | 102.94 | 0.69 | 1.41 | 0.74 | 1.66 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.12 | XLE, XOP, USO |
| semis_ai | -0.45 | SMH, SOXX |
| high_beta | -2.30 | IWM, ARKK, HIBL |
| rates | 1.02 | TLT, TBF, TBT |
| dollar | 0.62 | UUP |
| equity_hedges | 0.93 | SH, PSQ, SQQQ |
| housing_rates | -2.96 | XHB, ITB |
| defensives | 0.01 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | 2.69 | -7.43 | -2.29 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | 1.80 | 29.53 | 15.50 | MIXED |
| TBF | rates | 1.69 | -3.04 | -0.51 | BELOW_50_ABOVE_200 |
| XOP | energy | 0.79 | -9.66 | -8.04 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 0.63 | 10.14 | 5.93 | MIXED |
| UUP | dollar | 0.62 | 0.07 | 1.49 | ABOVE_50_AND_200 |
| XLE | energy | 0.44 | -5.76 | -4.33 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | 0.36 | 3.96 | 1.97 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -3.84 | -35.52 | -27.70 | BELOW_50_AND_200 |
| ITB | housing_rates | -3.28 | 14.53 | 7.16 | ABOVE_50_AND_200 |
| XHB | housing_rates | -2.63 | 9.70 | 4.79 | MIXED |
| ARKK | high_beta | -2.38 | -12.41 | -9.49 | BELOW_50_AND_200 |
| TLT | rates | -1.32 | 3.63 | 0.69 | MIXED |
| USO | energy | -0.85 | -6.34 | -7.33 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -0.78 | -18.17 | -14.08 | BELOW_50_AND_200 |
| IWM | high_beta | -0.68 | 0.96 | -0.35 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
