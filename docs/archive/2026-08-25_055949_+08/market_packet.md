# Market Packet — 2026-08-25T05:59:49.770123+08:00

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
| SPY | 2026-08-24 | 763.47 | -0.29 | -1.19 | 3.32 | 1.49 | 7.84 | 52.14 | 0.88 | 0.00 | 0.09 | ABOVE_50_AND_200 |
| QQQ | 2026-08-24 | 706.32 | -1.00 | -3.23 | 3.23 | -0.97 | 8.13 | 46.42 | 1.60 | -0.09 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-24 | 559.02 | 1.66 | -1.75 | -6.08 | -5.70 | -10.38 | 42.30 | 3.56 | -9.40 | -9.31 | BELOW_50_AND_200 |
| AMZN | 2026-08-24 | 262.07 | 1.33 | 0.29 | 12.91 | 4.77 | 9.93 | 52.48 | 2.78 | 9.59 | 9.68 | ABOVE_50_AND_200 |
| MU | 2026-08-24 | 910.43 | -5.83 | -10.01 | -1.14 | -5.45 | 58.46 | 48.50 | 7.43 | -4.46 | -4.37 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-24 | 142.45 | -2.74 | -2.86 | 23.88 | -1.48 | -17.44 | 49.04 | 4.86 | 20.56 | 20.65 | BELOW_50_AND_200 |
| SOFI | 2026-08-24 | 18.24 | -3.54 | -0.38 | 10.81 | 3.02 | -10.85 | 52.66 | 4.66 | 7.49 | 7.59 | MIXED |
| IAU | 2026-08-24 | 87.47 | 0.78 | 5.25 | 14.74 | 11.19 | 3.18 | 72.66 | 1.74 | 11.42 | 11.52 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-24 | 15.85 | 4.76 | 4.34 | -14.69 | -5.03 | BELOW_50_AND_200 |
| ^TNX | 2026-08-24 | 4.70 | -0.72 | -0.42 | 0.53 | 2.63 | ABOVE_50_AND_200 |
| CL=F | 2026-08-24 | 84.98 | -2.39 | 0.57 | -4.85 | 7.52 | ABOVE_50_AND_200 |
| GC=F | 2026-08-24 | 4710.00 | 1.86 | 6.61 | 15.79 | 12.46 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-24 | 98.98 | 0.18 | -0.66 | -2.45 | -1.48 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.46 | XLE, XOP, USO |
| semis_ai | -2.55 | SMH, SOXX |
| high_beta | -2.92 | IWM, ARKK, HIBL |
| rates | -0.41 | TLT, TBF, TBT |
| dollar | 0.22 | UUP |
| equity_hedges | 1.45 | SH, PSQ, SQQQ |
| housing_rates | 0.07 | XHB, ITB |
| defensives | 1.38 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 3.00 | -10.27 | 1.00 | MIXED |
| XLP | defensives | 1.70 | 3.95 | 3.10 | ABOVE_50_AND_200 |
| XLU | defensives | 1.05 | -6.63 | -3.55 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 1.04 | -3.00 | 0.98 | MIXED |
| TLT | rates | 0.62 | -0.83 | -1.83 | BELOW_50_AND_200 |
| ITB | housing_rates | 0.33 | 0.74 | -0.77 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.31 | -2.84 | -1.14 | BELOW_50_AND_200 |
| UUP | dollar | 0.22 | -2.17 | -1.10 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.43 | 6.29 | -7.19 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -2.67 | -3.95 | -9.15 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.66 | 16.73 | 7.05 | ABOVE_50_AND_200 |
| SMH | semis_ai | -2.43 | -2.56 | -7.01 | BELOW_50_ABOVE_200 |
| USO | energy | -1.80 | -3.28 | 9.96 | ABOVE_50_AND_200 |
| XOP | energy | -1.74 | 7.00 | 10.99 | ABOVE_50_AND_200 |
| TBT | rates | -1.22 | 1.68 | 3.45 | ABOVE_50_AND_200 |
| XLE | energy | -0.83 | 5.85 | 9.52 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
