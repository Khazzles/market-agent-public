# Market Packet — 2026-07-17T06:36:30.305621+08:00

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
| SPY | 2026-07-16 | 750.72 | -0.54 | -0.13 | -0.54 | 0.90 | 7.82 | 54.39 | 1.12 | 0.00 | 4.57 | ABOVE_50_AND_200 |
| QQQ | 2026-07-16 | 705.94 | -1.64 | -2.40 | -5.12 | -1.78 | 10.24 | 45.57 | 2.12 | -4.57 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-16 | 664.54 | -2.46 | 5.24 | 11.97 | 10.08 | 3.67 | 61.83 | 3.82 | 12.52 | 17.09 | ABOVE_50_AND_200 |
| AMZN | 2026-07-16 | 249.89 | -1.99 | 1.15 | 1.57 | -1.10 | 6.82 | 54.19 | 3.07 | 2.12 | 6.69 | BELOW_50_ABOVE_200 |
| MU | 2026-07-16 | 853.20 | -5.65 | -13.96 | -21.58 | -8.21 | 77.88 | 41.26 | 9.90 | -21.04 | -16.46 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-16 | 124.21 | -6.25 | -13.87 | -35.52 | -30.93 | -35.41 | 26.94 | 6.92 | -34.98 | -30.41 | BELOW_50_AND_200 |
| SOFI | 2026-07-16 | 17.32 | -3.08 | -6.98 | 1.11 | 1.90 | -20.80 | 46.74 | 5.48 | 1.65 | 6.22 | MIXED |
| IAU | 2026-07-16 | 74.80 | -1.94 | -3.50 | -7.95 | -8.08 | -11.23 | 36.88 | 2.12 | -7.41 | -2.83 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-16 | 16.73 | 6.76 | 5.62 | 3.27 | -3.27 | BELOW_50_AND_200 |
| ^TNX | 2026-07-16 | 4.57 | 0.53 | 0.66 | 2.24 | 1.73 | ABOVE_50_AND_200 |
| CL=F | 2026-07-16 | 78.93 | -0.84 | 9.50 | -2.25 | -7.98 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-16 | 3978.70 | -1.61 | -3.68 | -8.07 | -8.09 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-16 | 100.71 | 0.21 | -0.23 | 1.08 | 0.82 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.06 | XLE, XOP, USO |
| semis_ai | -4.08 | SMH, SOXX |
| high_beta | -3.74 | IWM, ARKK, HIBL |
| rates | 0.05 | TLT, TBF, TBT |
| dollar | 0.32 | UUP |
| equity_hedges | 2.41 | SH, PSQ, SQQQ |
| housing_rates | 2.01 | XHB, ITB |
| defensives | 1.68 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 5.01 | 12.61 | 1.19 | MIXED |
| XLP | defensives | 2.80 | 0.39 | 1.98 | ABOVE_50_AND_200 |
| ITB | housing_rates | 2.30 | 3.19 | 4.92 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.73 | 2.28 | 4.64 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.67 | 4.35 | 1.05 | MIXED |
| XOP | energy | 0.96 | 5.10 | 1.43 | ABOVE_50_AND_200 |
| XLE | energy | 0.92 | 2.65 | 0.82 | ABOVE_50_AND_200 |
| XLU | defensives | 0.55 | 1.63 | 1.28 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -7.48 | -22.33 | -10.99 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -4.46 | -15.59 | -6.20 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -3.70 | -12.08 | -4.65 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -3.68 | -3.72 | -2.10 | BELOW_50_AND_200 |
| USO | energy | -1.71 | -1.58 | -5.51 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.06 | 0.32 | 1.90 | ABOVE_50_AND_200 |
| TLT | rates | -0.04 | -1.76 | -1.30 | BELOW_50_AND_200 |
| TBF | rates | 0.00 | 1.22 | 0.89 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
