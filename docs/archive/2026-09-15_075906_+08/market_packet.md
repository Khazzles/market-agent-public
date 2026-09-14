# Market Packet — 2026-09-15T07:59:06.208077+08:00

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
| SPY | 2026-09-14 | 760.88 | -0.45 | -1.21 | -2.19 | 0.26 | 6.46 | 47.32 | 0.82 | 0.00 | 0.94 | ABOVE_50_AND_200 |
| QQQ | 2026-09-14 | 709.18 | -0.80 | -1.36 | -3.13 | -0.16 | 7.34 | 46.91 | 1.30 | -0.94 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-14 | 665.60 | 2.71 | 7.92 | 11.87 | 10.46 | 6.75 | 70.77 | 3.20 | 14.06 | 15.00 | ABOVE_50_AND_200 |
| AMZN | 2026-09-14 | 253.54 | -1.26 | -1.92 | -4.37 | -0.76 | 5.67 | 45.84 | 2.45 | -2.19 | -1.24 | BELOW_50_ABOVE_200 |
| MU | 2026-09-14 | 924.03 | -5.25 | -9.10 | -2.72 | -0.38 | 47.71 | 46.41 | 5.77 | -0.53 | 0.41 | BELOW_50_ABOVE_200 |
| ORCL | 2026-09-14 | 144.79 | -3.65 | -8.81 | -7.32 | 2.86 | -13.49 | 46.40 | 5.44 | -5.13 | -4.19 | MIXED |
| SOFI | 2026-09-14 | 17.65 | 1.91 | -3.13 | -4.23 | -0.94 | -10.66 | 48.06 | 4.29 | -2.05 | -1.11 | BELOW_50_AND_200 |
| IAU | 2026-09-14 | 80.54 | -1.43 | -3.42 | -1.52 | 0.36 | -5.50 | 43.72 | 1.97 | 0.67 | 1.61 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-14 | 17.10 | 7.95 | 11.76 | 20.00 | 5.89 | MIXED |
| ^TNX | 2026-09-14 | 4.96 | -0.28 | 3.70 | 6.90 | 5.97 | ABOVE_50_AND_200 |
| CL=F | 2026-09-14 | 102.10 | 2.05 | 11.61 | 25.66 | 21.70 | ABOVE_50_AND_200 |
| GC=F | 2026-09-14 | 4328.80 | -1.82 | -2.28 | -0.80 | 1.35 | MIXED |
| DX-Y.NYB | 2026-09-14 | 99.49 | 0.37 | 0.33 | -0.47 | -0.54 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.32 | XLE, XOP, USO |
| semis_ai | -5.19 | SMH, SOXX |
| high_beta | -2.99 | IWM, ARKK, HIBL |
| rates | -0.14 | TLT, TBF, TBT |
| dollar | 0.36 | UUP |
| equity_hedges | 1.26 | SH, PSQ, SQQQ |
| housing_rates | 0.19 | XHB, ITB |
| defensives | -0.05 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.47 | 10.52 | -0.08 | BELOW_50_AND_200 |
| ARKK | high_beta | 1.36 | 2.58 | 5.72 | ABOVE_50_AND_200 |
| XLP | defensives | 1.25 | -1.84 | -0.66 | BELOW_50_ABOVE_200 |
| USO | energy | 1.14 | 25.30 | 21.75 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.81 | 3.61 | 0.46 | MIXED |
| ITB | housing_rates | 0.57 | -9.52 | -6.68 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.49 | 2.76 | 0.29 | MIXED |
| UUP | dollar | 0.36 | -0.04 | -0.13 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -10.01 | -17.46 | -8.95 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -5.63 | -9.69 | -6.18 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -4.75 | -8.08 | -4.68 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.34 | -5.04 | -5.26 | BELOW_50_AND_200 |
| XOP | energy | -1.15 | 7.98 | 8.94 | ABOVE_50_AND_200 |
| XLE | energy | -0.94 | 5.68 | 6.90 | ABOVE_50_AND_200 |
| TBT | rates | -0.48 | 3.61 | 4.24 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.34 | -5.14 | -2.76 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
