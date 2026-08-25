# Market Packet — 2026-08-26T05:58:36.910877+08:00

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
| SPY | 2026-08-25 | 765.91 | 0.32 | -0.20 | 3.63 | 1.75 | 8.11 | 54.20 | 0.85 | 0.00 | -0.56 | ABOVE_50_AND_200 |
| QQQ | 2026-08-25 | 710.72 | 0.62 | -0.95 | 4.19 | -0.32 | 8.73 | 48.95 | 1.55 | 0.56 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-25 | 570.05 | 1.97 | 4.85 | -4.01 | -3.85 | -8.57 | 46.45 | 3.39 | -7.64 | -8.20 | BELOW_50_AND_200 |
| AMZN | 2026-08-25 | 261.06 | -0.39 | 0.62 | 12.82 | 4.18 | 9.48 | 51.59 | 2.70 | 9.19 | 8.63 | ABOVE_50_AND_200 |
| MU | 2026-08-25 | 932.97 | 2.48 | -0.83 | 3.64 | -3.01 | 61.40 | 50.78 | 7.01 | 0.01 | -0.55 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-25 | 144.76 | 1.62 | 1.38 | 20.73 | 0.66 | -15.85 | 51.14 | 4.63 | 17.11 | 16.54 | MIXED |
| SOFI | 2026-08-25 | 19.00 | 4.17 | 7.59 | 12.56 | 7.02 | -6.88 | 57.58 | 4.51 | 8.93 | 8.37 | MIXED |
| IAU | 2026-08-25 | 87.76 | 0.33 | 7.40 | 14.30 | 11.32 | 3.45 | 73.23 | 1.71 | 10.67 | 10.11 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-25 | 15.45 | -2.52 | -2.46 | -17.25 | -7.18 | BELOW_50_AND_200 |
| ^TNX | 2026-08-25 | 4.64 | -1.38 | -1.42 | -0.04 | 1.14 | ABOVE_50_AND_200 |
| CL=F | 2026-08-25 | 81.11 | -4.59 | -4.51 | -1.82 | 2.72 | ABOVE_50_AND_200 |
| GC=F | 2026-08-25 | 4715.90 | 1.62 | 8.01 | 15.74 | 12.36 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-25 | 98.91 | -0.09 | -0.74 | -2.56 | -1.53 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.71 | XLE, XOP, USO |
| semis_ai | 1.60 | SMH, SOXX |
| high_beta | 2.61 | IWM, ARKK, HIBL |
| rates | -0.79 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | -0.90 | SH, PSQ, SQQQ |
| housing_rates | 0.22 | XHB, ITB |
| defensives | -0.43 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.48 | 11.49 | -2.83 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 2.92 | 19.08 | 9.88 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.65 | 1.33 | -5.27 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 1.56 | -0.42 | -7.46 | BELOW_50_ABOVE_200 |
| TLT | rates | 1.10 | -0.33 | -0.69 | BELOW_50_AND_200 |
| IWM | high_beta | 0.42 | 2.16 | 0.77 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.36 | 0.18 | -0.44 | BELOW_50_AND_200 |
| XLU | defensives | 0.21 | -5.19 | -3.29 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -4.58 | 1.11 | 4.91 | ABOVE_50_AND_200 |
| TBT | rates | -2.24 | -0.16 | 1.05 | ABOVE_50_AND_200 |
| XOP | energy | -1.88 | 8.07 | 8.67 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -1.82 | -12.74 | -0.81 | BELOW_50_AND_200 |
| XLE | energy | -1.66 | 6.34 | 7.53 | ABOVE_50_AND_200 |
| TBF | rates | -1.22 | 0.12 | 0.62 | ABOVE_50_AND_200 |
| XLP | defensives | -1.06 | 1.36 | 1.99 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.61 | -3.91 | 0.35 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
