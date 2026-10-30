# Market Packet — 2026-10-30T09:20:48.347358+08:00

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
| SPY | 2026-10-28 | 772.31 | 0.34 | -0.10 | 1.06 | 0.61 | 6.06 | 53.33 | 0.89 | 0.00 | 2.73 | ABOVE_50_AND_200 |
| QQQ | 2026-10-28 | 725.61 | 0.60 | 0.06 | -1.67 | 0.03 | 6.91 | 49.59 | 1.55 | -2.73 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-28 | 612.49 | -1.24 | -12.19 | -17.10 | -8.18 | -3.11 | 30.66 | 3.89 | -18.16 | -15.43 | BELOW_50_AND_200 |
| AMZN | 2026-10-28 | 254.60 | 0.59 | -2.96 | 3.21 | -0.20 | 4.61 | 50.10 | 2.63 | 2.15 | 4.88 | BELOW_50_ABOVE_200 |
| MU | 2026-10-28 | 983.23 | 5.86 | 7.61 | -7.68 | 0.27 | 32.67 | 53.15 | 4.86 | -8.75 | -6.02 | ABOVE_50_AND_200 |
| ORCL | 2026-10-28 | 144.54 | 10.73 | 11.93 | 4.90 | 1.71 | -8.28 | 57.60 | 5.12 | 3.84 | 6.57 | MIXED |
| SOFI | 2026-10-28 | 17.14 | 4.51 | 15.03 | 7.73 | 3.16 | -4.15 | 62.44 | 4.37 | 6.67 | 9.40 | MIXED |
| IAU | 2026-10-28 | 76.57 | 0.31 | -1.47 | -2.48 | -4.89 | -9.64 | 42.52 | 1.49 | -3.54 | -0.81 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-29 | 17.20 | 1.72 | -9.62 | 5.26 | 6.85 | MIXED |
| ^TNX | 2026-10-29 | 4.99 | -1.11 | 0.73 | -5.74 | -0.38 | BELOW_50_ABOVE_200 |
| CL=F | 2026-10-29 | 102.76 | -0.02 | 3.31 | 13.65 | 8.95 | ABOVE_50_AND_200 |
| GC=F | 2026-10-29 | 4012.80 | -0.96 | -1.17 | -4.15 | -6.85 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-29 | 101.62 | -0.56 | 0.01 | 0.17 | 0.87 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.72 | XLE, XOP, USO |
| semis_ai | 1.93 | SMH, SOXX |
| high_beta | 2.22 | IWM, ARKK, HIBL |
| rates | 0.51 | TLT, TBF, TBT |
| dollar | -0.21 | UUP |
| equity_hedges | -0.91 | SH, PSQ, SQQQ |
| housing_rates | -1.35 | XHB, ITB |
| defensives | -0.60 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.69 | -16.69 | -9.63 | BELOW_50_AND_200 |
| SOXX | semis_ai | 2.13 | -8.02 | -1.57 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.74 | -6.46 | -1.00 | BELOW_50_ABOVE_200 |
| USO | energy | 1.64 | 16.20 | 12.05 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.58 | -3.72 | -0.19 | BELOW_50_ABOVE_200 |
| TBT | rates | 1.40 | -7.19 | -1.77 | BELOW_50_ABOVE_200 |
| TBF | rates | 0.90 | -3.53 | -0.79 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.40 | 0.82 | -1.30 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -1.76 | 4.67 | -1.70 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.51 | 0.69 | -1.02 | BELOW_50_AND_200 |
| XHB | housing_rates | -1.20 | 1.03 | -0.88 | BELOW_50_AND_200 |
| XLU | defensives | -0.84 | 7.00 | 1.71 | MIXED |
| TLT | rates | -0.78 | 3.53 | 0.56 | MIXED |
| PSQ | equity_hedges | -0.63 | 2.01 | -0.32 | BELOW_50_AND_200 |
| XLP | defensives | -0.36 | 6.10 | 2.78 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.34 | -0.53 | -0.63 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
