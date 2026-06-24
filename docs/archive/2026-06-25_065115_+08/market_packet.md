# Market Packet — 2026-06-25T06:51:15.970407+08:00

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
| SPY | 2026-06-24 | 733.24 | -0.05 | -2.28 | -1.66 | 0.04 | 6.31 | 45.73 | 1.32 | 0.00 | -0.70 | ABOVE_50_AND_200 |
| QQQ | 2026-06-24 | 710.62 | -0.42 | -2.64 | -0.96 | 1.57 | 12.65 | 47.82 | 2.28 | 0.70 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-24 | 557.67 | -0.81 | -7.09 | -8.62 | -9.72 | -14.49 | 37.79 | 3.38 | -6.95 | -7.65 | BELOW_50_AND_200 |
| AMZN | 2026-06-24 | 234.27 | 0.07 | -4.77 | -12.03 | -8.80 | 0.61 | 38.00 | 3.37 | -10.37 | -11.07 | BELOW_50_ABOVE_200 |
| MU | 2026-06-24 | 1048.51 | -0.31 | 2.72 | 39.62 | 35.53 | 152.39 | 56.81 | 8.28 | 41.28 | 40.58 | ABOVE_50_AND_200 |
| ORCL | 2026-06-24 | 157.53 | -4.62 | -16.35 | -17.99 | -16.96 | -22.79 | 32.52 | 7.62 | -16.32 | -17.02 | BELOW_50_AND_200 |
| SOFI | 2026-06-24 | 17.31 | 0.12 | -2.26 | 10.82 | 1.92 | -23.33 | 53.08 | 5.65 | 12.48 | 11.78 | MIXED |
| IAU | 2026-06-24 | 74.99 | -3.03 | -7.99 | -11.58 | -11.74 | -10.45 | 28.60 | 2.44 | -9.92 | -10.61 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-24 | 18.63 | -4.41 | 13.53 | 12.30 | 4.88 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-24 | 4.40 | -1.10 | -1.89 | -3.72 | -0.65 | BELOW_50_ABOVE_200 |
| CL=F | 2026-06-24 | 69.84 | -4.60 | -8.17 | -27.70 | -24.75 | BELOW_50_AND_200 |
| GC=F | 2026-06-24 | 4019.00 | -2.69 | -7.20 | -11.10 | -11.06 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-24 | 101.58 | 0.17 | 2.05 | 2.28 | 2.52 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.47 | XLE, XOP, USO |
| semis_ai | -0.41 | SMH, SOXX |
| high_beta | 0.64 | IWM, ARKK, HIBL |
| rates | -1.19 | TLT, TBF, TBT |
| dollar | 0.28 | UUP |
| equity_hedges | -0.49 | SH, PSQ, SQQQ |
| housing_rates | 5.89 | XHB, ITB |
| defensives | 0.95 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 6.15 | 13.58 | 9.33 | ABOVE_50_AND_200 |
| XHB | housing_rates | 5.62 | 14.27 | 9.39 | ABOVE_50_AND_200 |
| HIBL | high_beta | 1.41 | 15.38 | 16.11 | ABOVE_50_AND_200 |
| TLT | rates | 1.37 | 3.19 | 2.03 | MIXED |
| XLU | defensives | 1.04 | 0.42 | 1.09 | ABOVE_50_AND_200 |
| XLP | defensives | 0.86 | -0.42 | 0.89 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.46 | 4.06 | 4.69 | ABOVE_50_AND_200 |
| UUP | dollar | 0.28 | 2.74 | 2.97 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -4.47 | -24.57 | -20.11 | BELOW_50_ABOVE_200 |
| TBT | rates | -3.04 | -7.17 | -4.68 | BELOW_50_AND_200 |
| TBF | rates | -1.89 | -3.66 | -2.46 | BELOW_50_AND_200 |
| XLE | energy | -1.63 | -9.95 | -6.44 | BELOW_50_ABOVE_200 |
| XOP | energy | -1.30 | -11.00 | -8.53 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.83 | 0.84 | -0.80 | BELOW_50_AND_200 |
| SMH | semis_ai | -0.50 | 7.39 | 10.61 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.38 | -0.23 | -2.79 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
