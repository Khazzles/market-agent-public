# Market Packet — 2026-10-20T08:38:50.608840+08:00

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
| SPY | 2026-10-16 | 763.25 | -1.11 | -1.97 | 0.09 | -0.68 | 5.27 | 43.79 | 0.92 | 0.00 | 1.08 | BELOW_50_ABOVE_200 |
| QQQ | 2026-10-16 | 709.80 | -2.50 | -5.52 | -0.99 | -2.34 | 5.17 | 35.00 | 1.53 | -1.08 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-16 | 709.33 | -3.72 | -1.30 | 3.96 | 8.26 | 12.24 | 50.23 | 3.47 | 3.87 | 4.95 | ABOVE_50_AND_200 |
| AMZN | 2026-10-16 | 250.00 | -1.87 | -4.74 | -0.47 | -2.75 | 3.00 | 44.99 | 2.60 | -0.56 | 0.52 | BELOW_50_ABOVE_200 |
| MU | 2026-10-16 | 878.84 | -5.63 | -14.59 | -10.09 | -10.61 | 22.43 | 34.03 | 5.59 | -10.18 | -9.10 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-16 | 128.23 | -4.64 | -9.31 | -14.85 | -11.64 | -19.95 | 39.67 | 5.35 | -14.93 | -13.86 | BELOW_50_AND_200 |
| SOFI | 2026-10-16 | 14.55 | -3.58 | -7.91 | -13.03 | -14.87 | -20.79 | 34.66 | 4.63 | -13.12 | -12.04 | BELOW_50_AND_200 |
| IAU | 2026-10-16 | 78.34 | -0.17 | -0.67 | -4.10 | -3.79 | -7.87 | 45.58 | 1.52 | -4.19 | -3.11 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-19 | 18.44 | -7.75 | 21.24 | 24.51 | 17.75 | ABOVE_50_AND_200 |
| ^TNX | 2026-10-19 | 5.14 | 0.75 | -1.98 | 2.76 | 3.68 | ABOVE_50_AND_200 |
| CL=F | 2026-10-19 | 98.46 | -2.91 | 5.04 | -1.83 | 7.74 | ABOVE_50_AND_200 |
| GC=F | 2026-10-19 | 4155.20 | -0.62 | -0.84 | -6.09 | -4.91 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-19 | 101.92 | 0.08 | -0.64 | 1.70 | 1.53 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.72 | XLE, XOP, USO |
| semis_ai | -3.78 | SMH, SOXX |
| high_beta | -5.69 | IWM, ARKK, HIBL |
| rates | 0.03 | TLT, TBF, TBT |
| dollar | -0.28 | UUP |
| equity_hedges | 3.80 | SH, PSQ, SQQQ |
| housing_rates | -0.64 | XHB, ITB |
| defensives | 1.21 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 7.64 | 0.96 | 5.68 | MIXED |
| USO | energy | 2.83 | 4.15 | 13.37 | ABOVE_50_AND_200 |
| XOP | energy | 2.82 | 4.04 | 6.81 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 2.57 | 0.19 | 1.98 | MIXED |
| XLE | energy | 2.52 | 5.83 | 7.40 | ABOVE_50_AND_200 |
| XLU | defensives | 1.34 | 1.25 | 0.45 | MIXED |
| SH | equity_hedges | 1.18 | -0.70 | 0.53 | MIXED |
| XLP | defensives | 1.08 | 4.95 | 4.20 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -10.67 | -14.94 | -20.70 | BELOW_50_AND_200 |
| ARKK | high_beta | -4.71 | -6.06 | -4.90 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -4.14 | -4.95 | -8.18 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -3.41 | -3.71 | -6.78 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -1.69 | -5.25 | -6.44 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.88 | -2.23 | -5.73 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.40 | -2.43 | -5.60 | BELOW_50_AND_200 |
| UUP | dollar | -0.28 | 1.90 | 1.82 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
