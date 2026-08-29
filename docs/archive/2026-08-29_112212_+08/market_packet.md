# Market Packet — 2026-08-29T11:22:12.017617+08:00

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
| SPY | 2026-08-28 | 769.35 | -0.23 | 0.47 | 3.73 | 2.04 | 8.38 | 56.61 | 0.82 | 0.00 | -1.08 | ABOVE_50_AND_200 |
| QQQ | 2026-08-28 | 716.43 | -0.65 | 0.42 | 4.81 | 0.61 | 9.35 | 51.88 | 1.46 | 1.08 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-28 | 578.02 | 1.21 | 5.11 | 7.23 | -2.39 | -7.18 | 49.56 | 3.47 | 3.50 | 2.42 | BELOW_50_AND_200 |
| AMZN | 2026-08-28 | 266.43 | 3.97 | 3.02 | 13.13 | 5.87 | 11.63 | 55.85 | 2.64 | 9.40 | 8.32 | ABOVE_50_AND_200 |
| MU | 2026-08-28 | 932.86 | -0.27 | -3.51 | 6.65 | -2.32 | 58.54 | 50.68 | 6.48 | 2.92 | 1.84 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-28 | 150.85 | -0.72 | 2.99 | 18.26 | 6.57 | -11.61 | 56.05 | 4.32 | 14.53 | 13.45 | MIXED |
| SOFI | 2026-08-28 | 18.06 | -5.84 | -4.50 | 9.65 | 1.29 | -10.84 | 49.64 | 4.91 | 5.92 | 4.84 | MIXED |
| IAU | 2026-08-28 | 83.82 | -3.23 | -3.42 | 8.43 | 5.93 | -1.36 | 54.61 | 1.93 | 4.71 | 3.62 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-28 | 14.43 | -0.55 | -4.63 | -15.56 | -12.59 | BELOW_50_AND_200 |
| ^TNX | 2026-08-28 | 4.72 | 1.03 | -0.38 | 1.22 | 2.60 | ABOVE_50_AND_200 |
| CL=F | 2026-08-28 | 83.44 | -0.11 | -4.16 | -0.18 | 5.22 | ABOVE_50_AND_200 |
| GC=F | 2026-08-28 | 4504.10 | -2.29 | -2.60 | 9.85 | 7.00 | MIXED |
| DX-Y.NYB | 2026-08-28 | 99.68 | 0.52 | 0.89 | -0.33 | -0.74 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.21 | XLE, XOP, USO |
| semis_ai | -3.34 | SMH, SOXX |
| high_beta | -3.97 | IWM, ARKK, HIBL |
| rates | 0.29 | TLT, TBF, TBT |
| dollar | 0.57 | UUP |
| equity_hedges | 0.97 | SH, PSQ, SQQQ |
| housing_rates | 0.45 | XHB, ITB |
| defensives | -0.30 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.01 | -13.63 | -3.20 | BELOW_50_AND_200 |
| TBT | rates | 0.85 | -0.45 | 2.28 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.82 | 0.98 | -2.18 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.66 | -4.33 | -0.51 | BELOW_50_AND_200 |
| XLE | energy | 0.63 | 6.31 | 7.79 | ABOVE_50_AND_200 |
| UUP | dollar | 0.57 | 0.14 | -0.33 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.43 | -0.02 | 0.68 | ABOVE_50_AND_200 |
| TBF | rates | 0.32 | -0.12 | 1.27 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -7.35 | 11.42 | -5.87 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -3.47 | 2.64 | -5.07 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -3.20 | 0.81 | -7.54 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -3.19 | 16.04 | 7.06 | ABOVE_50_AND_200 |
| IWM | high_beta | -1.35 | 1.08 | -0.53 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.04 | -4.32 | -4.38 | BELOW_50_AND_200 |
| TLT | rates | -0.30 | 0.10 | -1.19 | BELOW_50_AND_200 |
| USO | energy | -0.24 | 1.74 | 7.22 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
