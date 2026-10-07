# Market Packet — 2026-10-07T09:00:43.019191+08:00

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
| SPY | 2026-10-06 | 779.09 | 0.55 | 1.95 | 1.16 | 1.81 | 7.98 | 62.00 | 0.87 | 0.00 | -4.51 | ABOVE_50_AND_200 |
| QQQ | 2026-10-06 | 759.66 | 0.46 | 2.94 | 5.66 | 5.54 | 13.36 | 69.93 | 1.21 | 4.51 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-05 | 741.90 | 1.90 | 3.67 | 21.49 | 18.14 | 17.99 | 63.96 | 3.23 | 20.33 | 15.83 | ABOVE_50_AND_200 |
| AMZN | 2026-10-06 | 256.29 | 1.95 | 3.90 | -0.86 | -0.44 | 6.04 | 54.52 | 2.16 | -2.01 | -6.52 | BELOW_50_ABOVE_200 |
| MU | 2026-10-06 | 1045.56 | -1.73 | -1.83 | 2.85 | 8.71 | 51.56 | 53.94 | 4.15 | 1.69 | -2.81 | ABOVE_50_AND_200 |
| ORCL | 2026-10-06 | 144.77 | 1.61 | 5.07 | -8.82 | 0.09 | -10.90 | 51.08 | 4.51 | -9.98 | -14.48 | MIXED |
| SOFI | 2026-10-05 | 15.92 | 0.95 | -0.06 | -13.99 | -8.73 | -15.72 | 38.47 | 3.84 | -15.15 | -19.65 | BELOW_50_AND_200 |
| IAU | 2026-10-06 | 78.37 | 0.71 | -0.19 | -6.02 | -3.60 | -8.05 | 41.24 | 1.69 | -7.18 | -11.68 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-06 | 15.01 | -3.29 | -6.42 | -1.90 | -4.13 | BELOW_50_AND_200 |
| ^TNX | 2026-10-06 | 5.27 | -0.79 | 0.27 | 10.14 | 8.48 | ABOVE_50_AND_200 |
| CL=F | 2026-10-06 | 89.99 | 0.63 | 0.68 | -1.63 | 1.42 | ABOVE_50_AND_200 |
| GC=F | 2026-10-06 | 4184.80 | 0.67 | 0.12 | -6.52 | -4.24 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-06 | 101.94 | -0.22 | 0.57 | 2.81 | 1.92 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.55 | XLE, XOP, USO |
| semis_ai | -0.12 | SMH, SOXX |
| high_beta | 1.26 | IWM, ARKK, HIBL |
| rates | -0.14 | TLT, TBF, TBT |
| dollar | -0.31 | UUP |
| equity_hedges | -0.78 | SH, PSQ, SQQQ |
| housing_rates | 1.36 | XHB, ITB |
| defensives | 1.96 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | 3.28 | 6.47 | 11.20 | ABOVE_50_AND_200 |
| XLU | defensives | 2.98 | -4.46 | -3.07 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.60 | -7.41 | -7.07 | BELOW_50_AND_200 |
| HIBL | high_beta | 1.22 | 16.75 | 13.94 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.11 | -5.69 | -5.18 | BELOW_50_AND_200 |
| XLP | defensives | 0.94 | -3.29 | -2.91 | BELOW_50_AND_200 |
| USO | energy | 0.64 | 2.08 | 5.07 | ABOVE_50_AND_200 |
| XOP | energy | 0.54 | -1.18 | 2.55 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -1.30 | -16.63 | -16.38 | BELOW_50_AND_200 |
| IWM | high_beta | -0.72 | -4.96 | -3.71 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.53 | -1.89 | -2.16 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.49 | -6.17 | -5.81 | BELOW_50_AND_200 |
| TBT | rates | -0.42 | 12.00 | 9.61 | ABOVE_50_AND_200 |
| UUP | dollar | -0.31 | 2.92 | 2.20 | ABOVE_50_AND_200 |
| TBF | rates | -0.22 | 5.90 | 4.85 | ABOVE_50_AND_200 |
| SMH | semis_ai | -0.22 | 11.55 | 10.39 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
