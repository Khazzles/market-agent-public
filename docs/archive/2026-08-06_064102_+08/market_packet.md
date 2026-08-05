# Market Packet — 2026-08-06T06:41:02.294959+08:00

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
| SPY | 2026-08-05 | 769.79 | -0.20 | 5.53 | 2.95 | 3.14 | 9.67 | 64.74 | 1.23 | 0.00 | 1.84 | ABOVE_50_AND_200 |
| QQQ | 2026-08-05 | 717.30 | -0.90 | 8.40 | 1.11 | 0.32 | 10.91 | 55.39 | 2.20 | -1.84 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-05 | 588.77 | 0.14 | 0.54 | -4.36 | -2.05 | -6.93 | 46.68 | 4.27 | -7.31 | -5.46 | BELOW_50_AND_200 |
| AMZN | 2026-08-05 | 272.65 | -1.72 | 20.30 | 10.84 | 10.24 | 15.55 | 63.49 | 3.66 | 7.89 | 9.73 | ABOVE_50_AND_200 |
| MU | 2026-08-05 | 893.19 | 0.06 | 20.86 | -4.82 | -8.13 | 69.08 | 48.80 | 9.49 | -7.77 | -5.92 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-05 | 144.39 | -0.93 | 22.63 | 1.97 | -10.96 | -20.10 | 54.71 | 5.40 | -0.98 | 0.86 | BELOW_50_AND_200 |
| SOFI | 2026-08-05 | 18.25 | -2.41 | 19.67 | 2.82 | 5.18 | -13.81 | 55.91 | 5.13 | -0.14 | 1.71 | MIXED |
| IAU | 2026-08-05 | 79.85 | 4.12 | 5.01 | 3.21 | 1.72 | -5.33 | 60.17 | 1.92 | 0.25 | 2.10 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-05 | 15.81 | -4.18 | -23.48 | -1.98 | -8.82 | BELOW_50_AND_200 |
| ^TNX | 2026-08-05 | 4.62 | -0.22 | -0.11 | 1.94 | 1.87 | ABOVE_50_AND_200 |
| CL=F | 2026-08-05 | 75.13 | -0.84 | -11.05 | 6.66 | -7.26 | BELOW_50_AND_200 |
| GC=F | 2026-08-05 | 4308.50 | 5.20 | 6.79 | 3.94 | 3.13 | MIXED |
| DX-Y.NYB | 2026-08-05 | 99.69 | -0.20 | -1.10 | -1.43 | -0.77 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.26 | XLE, XOP, USO |
| semis_ai | -1.58 | SMH, SOXX |
| high_beta | -0.95 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | -0.25 | UUP |
| equity_hedges | 1.31 | SH, PSQ, SQQQ |
| housing_rates | 1.28 | XHB, ITB |
| defensives | -0.53 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.76 | -5.18 | -4.94 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.40 | 1.01 | 3.68 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.16 | 1.34 | 2.77 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.94 | -1.12 | -0.87 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.22 | -2.51 | -3.08 | BELOW_50_AND_200 |
| TLT | rates | 0.22 | -1.83 | -2.24 | BELOW_50_AND_200 |
| XLP | defensives | -0.05 | 0.55 | 1.26 | ABOVE_50_AND_200 |
| TBF | rates | -0.16 | 1.95 | 1.92 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | -3.93 | 4.98 | 0.57 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.12 | -3.80 | -6.51 | BELOW_50_ABOVE_200 |
| XLE | energy | -2.07 | 4.89 | 1.26 | ABOVE_50_AND_200 |
| HIBL | high_beta | -1.46 | 1.82 | -2.77 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -1.04 | -2.02 | -4.38 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.02 | -4.46 | -2.83 | BELOW_50_AND_200 |
| USO | energy | -0.78 | 5.47 | -5.68 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.76 | -6.17 | -1.63 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
