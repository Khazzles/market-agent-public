# Market Packet — 2026-06-04T18:46:07.797830+08:00

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
| SPY | 2026-06-03 | 754.24 | -0.70 | 0.50 | 5.05 | 6.26 | 10.45 | 67.91 | 0.86 | 0.00 | -5.55 | ABOVE_50_AND_200 |
| QQQ | 2026-06-03 | 744.21 | -0.26 | 2.02 | 10.60 | 12.36 | 19.97 | 77.31 | 1.33 | 5.55 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-03 | 622.98 | 4.24 | -1.93 | 2.06 | 0.66 | -6.17 | 51.45 | 2.79 | -2.99 | -8.54 | MIXED |
| AMZN | 2026-06-03 | 250.02 | -2.53 | -8.03 | -8.10 | 0.19 | 7.80 | 39.39 | 2.82 | -13.14 | -18.70 | ABOVE_50_AND_200 |
| MU | 2026-06-03 | 1079.57 | 1.45 | 16.28 | 87.28 | 81.22 | 206.02 | 82.37 | 5.29 | 82.23 | 76.68 | ABOVE_50_AND_200 |
| ORCL | 2026-06-03 | 230.33 | -5.83 | 20.62 | 27.76 | 30.59 | 11.30 | 66.97 | 4.84 | 22.71 | 17.15 | ABOVE_50_AND_200 |
| SOFI | 2026-06-03 | 16.68 | -5.98 | 3.15 | 2.96 | -0.40 | -27.87 | 49.65 | 5.58 | -2.08 | -7.64 | BELOW_50_AND_200 |
| IAU | 2026-06-03 | 83.59 | -0.98 | -0.17 | -1.62 | -3.98 | 1.09 | 38.74 | 1.80 | -6.67 | -12.22 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-04 | 16.58 | 3.24 | 5.34 | -4.66 | -13.36 | BELOW_50_AND_200 |
| ^TNX | 2026-06-03 | 4.49 | 0.81 | 0.22 | 1.01 | 2.13 | ABOVE_50_AND_200 |
| CL=F | 2026-06-04 | 94.96 | -1.10 | 6.82 | -7.15 | -3.01 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-04 | 4497.30 | 1.37 | -0.04 | -1.28 | -2.84 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-06-04 | 99.30 | -0.23 | 0.28 | 0.83 | 0.41 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.75 | XLE, XOP, USO |
| semis_ai | 1.33 | SMH, SOXX |
| high_beta | -1.94 | IWM, ARKK, HIBL |
| rates | 0.28 | TLT, TBF, TBT |
| dollar | 0.36 | UUP |
| equity_hedges | 0.58 | SH, PSQ, SQQQ |
| housing_rates | -0.63 | XHB, ITB |
| defensives | -0.01 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.62 | -4.57 | 5.09 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.76 | 33.25 | 35.82 | ABOVE_50_AND_200 |
| XOP | energy | 1.35 | -5.46 | -0.54 | BELOW_50_ABOVE_200 |
| XLE | energy | 1.29 | -1.15 | 0.79 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.90 | 25.87 | 27.87 | ABOVE_50_AND_200 |
| TBT | rates | 0.76 | -1.08 | 0.62 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.76 | -26.37 | -32.94 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.70 | -4.35 | -5.65 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -2.25 | 38.56 | 44.28 | ABOVE_50_AND_200 |
| ARKK | high_beta | -2.19 | -0.09 | 4.25 | ABOVE_50_AND_200 |
| IWM | high_beta | -1.37 | 3.52 | 5.51 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.85 | 1.29 | -0.65 | BELOW_50_AND_200 |
| XLU | defensives | -0.43 | -5.74 | -3.94 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.41 | 2.46 | 1.52 | MIXED |
| TLT | rates | -0.40 | 0.41 | -0.61 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.28 | -9.35 | -11.35 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
