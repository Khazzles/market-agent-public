# Market Packet — 2026-10-09T09:26:46.311697+08:00

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
| SPY | 2026-10-08 | 773.93 | -0.42 | 1.30 | 1.51 | 0.93 | 7.12 | 56.09 | 0.87 | 0.00 | -2.85 | ABOVE_50_AND_200 |
| QQQ | 2026-10-08 | 747.58 | -1.34 | 0.75 | 4.37 | 3.38 | 11.33 | 58.83 | 1.26 | 2.85 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-08 | 720.89 | -0.06 | -0.69 | 10.28 | 13.32 | 14.45 | 57.51 | 3.17 | 8.77 | 5.91 | ABOVE_50_AND_200 |
| AMZN | 2026-10-08 | 254.06 | -2.25 | 2.35 | 0.66 | -1.74 | 4.99 | 50.82 | 2.24 | -0.85 | -3.71 | BELOW_50_ABOVE_200 |
| MU | 2026-10-08 | 1035.84 | -4.79 | -5.61 | 0.79 | 6.45 | 48.42 | 51.21 | 4.50 | -0.73 | -3.58 | ABOVE_50_AND_200 |
| ORCL | 2026-10-08 | 135.69 | -5.48 | -1.72 | -16.05 | -6.72 | -16.25 | 41.61 | 4.79 | -17.56 | -20.41 | BELOW_50_AND_200 |
| SOFI | 2026-10-08 | 15.61 | -0.32 | -1.45 | -9.93 | -10.32 | -16.66 | 35.52 | 3.70 | -11.44 | -14.29 | BELOW_50_AND_200 |
| IAU | 2026-10-08 | 77.66 | 0.78 | -1.03 | -6.08 | -4.55 | -8.84 | 39.98 | 1.68 | -7.60 | -10.45 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-08 | 15.41 | 2.19 | -5.98 | -6.38 | -0.66 | BELOW_50_AND_200 |
| ^TNX | 2026-10-08 | 5.23 | -0.87 | -0.11 | 8.15 | 7.13 | ABOVE_50_AND_200 |
| CL=F | 2026-10-08 | 90.94 | 3.01 | -2.08 | -5.32 | 2.15 | ABOVE_50_AND_200 |
| GC=F | 2026-10-08 | 4182.30 | 1.00 | -0.48 | -6.24 | -4.41 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-08 | 102.04 | -0.19 | -0.06 | 3.31 | 1.98 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.77 | XLE, XOP, USO |
| semis_ai | -3.10 | SMH, SOXX |
| high_beta | -2.30 | IWM, ARKK, HIBL |
| rates | -0.62 | TLT, TBF, TBT |
| dollar | -0.21 | UUP |
| equity_hedges | 1.98 | SH, PSQ, SQQQ |
| housing_rates | 1.11 | XHB, ITB |
| defensives | 0.96 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.05 | -13.64 | -10.91 | BELOW_50_AND_200 |
| XLE | energy | 2.97 | -0.11 | 4.31 | ABOVE_50_AND_200 |
| XOP | energy | 2.79 | -0.78 | 4.79 | ABOVE_50_AND_200 |
| USO | energy | 2.55 | -1.59 | 6.36 | ABOVE_50_AND_200 |
| XLP | defensives | 2.11 | 0.45 | -0.77 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 1.40 | -4.95 | -3.74 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.38 | -4.92 | -7.70 | BELOW_50_AND_200 |
| TLT | rates | 0.93 | -4.72 | -4.07 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -6.05 | 5.47 | 4.31 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -3.35 | 5.88 | 5.04 | ABOVE_50_AND_200 |
| SMH | semis_ai | -2.84 | 5.74 | 5.26 | ABOVE_50_AND_200 |
| TBT | rates | -1.84 | 9.13 | 7.57 | ABOVE_50_AND_200 |
| TBF | rates | -0.96 | 4.34 | 3.67 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.79 | 3.60 | 3.72 | ABOVE_50_AND_200 |
| UUP | dollar | -0.21 | 3.57 | 2.41 | ABOVE_50_AND_200 |
| XLU | defensives | -0.19 | -4.35 | -2.91 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
