# Market Packet — 2026-06-18T07:07:21.414223+08:00

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
| SPY | 2026-06-17 | 740.96 | -1.25 | 2.14 | 0.31 | 1.75 | 7.72 | 50.74 | 1.33 | 0.00 | -2.04 | ABOVE_50_AND_200 |
| QQQ | 2026-06-17 | 722.51 | -1.01 | 4.15 | 2.36 | 4.64 | 15.09 | 53.38 | 2.15 | 2.04 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-17 | 567.58 | -5.44 | -0.60 | -7.14 | -8.84 | -13.44 | 39.27 | 3.58 | -7.45 | -9.49 | BELOW_50_AND_200 |
| AMZN | 2026-06-17 | 237.50 | -3.46 | -0.21 | -10.33 | -7.46 | 2.06 | 36.89 | 3.15 | -10.64 | -12.69 | BELOW_50_ABOVE_200 |
| MU | 2026-06-17 | 1043.19 | 2.20 | 16.97 | 53.06 | 45.24 | 163.65 | 61.74 | 7.46 | 52.75 | 50.71 | ABOVE_50_AND_200 |
| ORCL | 2026-06-17 | 183.53 | -2.55 | -8.81 | -1.65 | -2.16 | -10.54 | 42.62 | 6.85 | -1.96 | -4.01 | BELOW_50_AND_200 |
| SOFI | 2026-06-17 | 17.42 | -1.64 | 9.77 | 10.88 | 3.00 | -23.37 | 54.87 | 5.58 | 10.57 | 8.53 | MIXED |
| IAU | 2026-06-17 | 79.64 | -2.28 | 3.71 | -7.14 | -7.30 | -4.65 | 38.87 | 2.34 | -7.45 | -9.49 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-17 | 18.44 | 12.37 | -17.01 | 2.10 | 3.29 | MIXED |
| ^TNX | 2026-06-17 | 4.46 | -0.53 | -1.96 | 0.04 | 0.95 | ABOVE_50_AND_200 |
| CL=F | 2026-06-17 | 75.43 | -0.82 | -16.22 | -30.58 | -20.30 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-17 | 4286.90 | -1.02 | 4.35 | -5.83 | -6.14 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-17 | 100.39 | 0.85 | 0.44 | 1.43 | 1.51 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.07 | XLE, XOP, USO |
| semis_ai | 1.36 | SMH, SOXX |
| high_beta | -1.20 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | 0.90 | UUP |
| equity_hedges | 1.79 | SH, PSQ, SQQQ |
| housing_rates | -2.40 | XHB, ITB |
| defensives | -1.78 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 3.05 | -9.23 | -16.82 | BELOW_50_AND_200 |
| SOXX | semis_ai | 1.44 | 20.95 | 19.29 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.29 | 14.25 | 14.94 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.27 | -0.03 | -1.41 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 1.06 | -2.42 | -4.81 | BELOW_50_AND_200 |
| UUP | dollar | 0.90 | 1.73 | 1.99 | ABOVE_50_AND_200 |
| TLT | rates | 0.16 | 3.31 | 0.79 | MIXED |
| TBF | rates | -0.04 | -3.22 | -0.73 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -2.51 | 9.46 | 1.79 | MIXED |
| XHB | housing_rates | -2.29 | 11.33 | 3.27 | MIXED |
| XLP | defensives | -2.23 | -2.58 | 0.07 | ABOVE_50_AND_200 |
| HIBL | high_beta | -2.10 | 31.60 | 21.27 | ABOVE_50_AND_200 |
| XLU | defensives | -1.33 | 1.18 | -1.62 | BELOW_50_AND_200 |
| XLE | energy | -1.25 | -9.76 | -4.97 | BELOW_50_ABOVE_200 |
| USO | energy | -1.07 | -23.48 | -14.90 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.90 | -11.61 | -7.57 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
