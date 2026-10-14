# Market Packet — 2026-10-14T08:36:42.597026+08:00

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
| SPY | 2026-10-12 | 778.10 | -0.06 | 0.42 | 1.81 | 1.29 | 7.56 | 59.33 | 0.78 | 0.00 | -2.55 | ABOVE_50_AND_200 |
| QQQ | 2026-10-12 | 746.04 | -0.70 | -1.34 | 4.36 | 2.81 | 10.89 | 56.56 | 1.18 | 2.55 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-12 | 742.96 | 3.38 | 0.14 | 14.65 | 15.46 | 17.83 | 62.28 | 3.21 | 12.84 | 10.29 | ABOVE_50_AND_200 |
| AMZN | 2026-10-12 | 259.53 | -1.11 | 3.23 | 1.07 | 0.26 | 7.12 | 55.58 | 2.20 | -0.74 | -3.29 | ABOVE_50_AND_200 |
| MU | 2026-10-12 | 989.04 | -3.88 | -7.04 | 1.41 | 0.97 | 40.24 | 44.66 | 4.78 | -0.39 | -2.95 | ABOVE_50_AND_200 |
| ORCL | 2026-10-12 | 137.39 | -2.84 | -3.57 | -8.58 | -5.83 | -14.90 | 44.40 | 4.80 | -10.38 | -12.94 | BELOW_50_AND_200 |
| SOFI | 2026-10-12 | 15.23 | -3.61 | -4.33 | -12.07 | -12.33 | -18.18 | 33.24 | 3.57 | -13.87 | -16.43 | BELOW_50_AND_200 |
| IAU | 2026-10-12 | 78.34 | -0.67 | 0.67 | -4.12 | -3.80 | -7.98 | 43.87 | 1.57 | -5.93 | -8.48 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-13 | 15.27 | 0.39 | 1.73 | -10.70 | -1.17 | BELOW_50_AND_200 |
| ^TNX | 2026-10-13 | 5.22 | -0.44 | -0.99 | 5.16 | 6.15 | ABOVE_50_AND_200 |
| CL=F | 2026-10-13 | 94.94 | 1.28 | 6.15 | -6.36 | 5.87 | ABOVE_50_AND_200 |
| GC=F | 2026-10-13 | 4183.20 | -0.18 | -0.09 | -3.88 | -4.50 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-13 | 102.17 | -0.39 | 0.34 | 2.73 | 1.96 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.59 | XLE, XOP, USO |
| semis_ai | -2.32 | SMH, SOXX |
| high_beta | -2.64 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | 0.38 | UUP |
| equity_hedges | 0.94 | SH, PSQ, SQQQ |
| housing_rates | -0.83 | XHB, ITB |
| defensives | 0.85 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.06 | -13.48 | -9.16 | BELOW_50_AND_200 |
| USO | energy | 1.91 | -2.50 | 8.19 | ABOVE_50_AND_200 |
| XOP | energy | 1.45 | -0.73 | 4.84 | ABOVE_50_AND_200 |
| XLE | energy | 1.43 | 1.34 | 5.11 | ABOVE_50_AND_200 |
| XLP | defensives | 1.17 | 1.24 | 0.47 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.69 | -4.90 | -3.11 | BELOW_50_AND_200 |
| XLU | defensives | 0.53 | -1.79 | -1.30 | BELOW_50_AND_200 |
| UUP | dollar | 0.38 | 3.78 | 2.80 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.77 | 3.64 | 1.37 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.60 | 3.37 | 1.24 | ABOVE_50_AND_200 |
| SMH | semis_ai | -2.05 | 3.95 | 2.03 | ABOVE_50_AND_200 |
| ARKK | high_beta | -1.79 | 5.31 | 3.40 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.91 | -6.20 | -9.31 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.76 | -4.48 | -7.64 | BELOW_50_AND_200 |
| IWM | high_beta | -0.37 | -3.80 | -4.54 | BELOW_50_ABOVE_200 |
| TBF | rates | -0.19 | 3.02 | 3.24 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
