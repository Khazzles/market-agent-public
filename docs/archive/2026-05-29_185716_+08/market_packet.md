# Market Packet — 2026-05-29T18:57:16.301156+08:00

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
| SPY | 2026-05-28 | 754.60 | 0.55 | 1.80 | 6.03 | 7.53 | 10.87 | 73.20 | 0.95 | 0.00 | -5.84 | ABOVE_50_AND_200 |
| QQQ | 2026-05-28 | 735.60 | 0.84 | 3.15 | 11.87 | 13.16 | 19.21 | 76.42 | 1.45 | 5.84 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-28 | 635.29 | 0.00 | 5.00 | -5.37 | 2.77 | -4.81 | 56.87 | 2.48 | -11.40 | -17.24 | MIXED |
| AMZN | 2026-05-28 | 274.00 | 0.79 | 3.39 | 5.51 | 11.63 | 18.47 | 64.40 | 2.46 | -0.52 | -6.36 | ABOVE_50_AND_200 |
| MU | 2026-05-28 | 923.52 | -0.53 | 26.17 | 83.13 | 68.72 | 176.07 | 75.68 | 6.05 | 77.10 | 71.26 | ABOVE_50_AND_200 |
| ORCL | 2026-05-28 | 203.70 | 6.67 | 8.26 | 22.74 | 20.07 | -1.67 | 66.06 | 4.22 | 16.71 | 10.87 | MIXED |
| SOFI | 2026-05-28 | 16.97 | 4.95 | 8.16 | -7.57 | 1.68 | -26.98 | 55.60 | 4.86 | -13.60 | -19.44 | MIXED |
| IAU | 2026-05-28 | 84.59 | 1.03 | -1.10 | -2.16 | -3.02 | 2.84 | 40.98 | 1.85 | -8.19 | -14.03 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-29 | 15.85 | 0.70 | -5.09 | -6.16 | -20.60 | BELOW_50_AND_200 |
| ^TNX | 2026-05-28 | 4.46 | -0.58 | -2.56 | 2.32 | 1.59 | ABOVE_50_AND_200 |
| CL=F | 2026-05-29 | 86.98 | -2.16 | -9.72 | -18.62 | -11.11 | BELOW_50_ABOVE_200 |
| GC=F | 2026-05-29 | 4569.00 | 1.55 | 0.64 | 0.52 | -1.33 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-29 | 99.08 | 0.06 | -0.11 | 0.16 | 0.18 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.24 | XLE, XOP, USO |
| semis_ai | 0.85 | SMH, SOXX |
| high_beta | 2.67 | IWM, ARKK, HIBL |
| rates | -0.40 | TLT, TBF, TBT |
| dollar | -0.18 | UUP |
| equity_hedges | -1.25 | SH, PSQ, SQQQ |
| housing_rates | -0.47 | XHB, ITB |
| defensives | -0.65 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | 3.93 | 7.37 | 9.18 | ABOVE_50_AND_200 |
| HIBL | high_beta | 3.53 | 39.32 | 41.58 | ABOVE_50_AND_200 |
| XOP | energy | 0.98 | -3.90 | -4.44 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 0.97 | 29.81 | 31.51 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.73 | 22.11 | 24.80 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.57 | 6.62 | 8.50 | ABOVE_50_AND_200 |
| TLT | rates | 0.52 | -0.73 | -0.21 | BELOW_50_AND_200 |
| XLE | energy | -0.07 | -1.32 | -2.45 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -2.46 | -28.83 | -34.40 | BELOW_50_AND_200 |
| TBT | rates | -1.24 | 1.22 | 0.33 | ABOVE_50_AND_200 |
| XLU | defensives | -1.13 | -3.50 | -2.24 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -0.78 | -10.35 | -12.00 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.52 | -3.88 | 0.82 | MIXED |
| SH | equity_hedges | -0.51 | -5.29 | -6.88 | BELOW_50_AND_200 |
| TBF | rates | -0.49 | 0.86 | 0.44 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.42 | -4.84 | 0.34 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
