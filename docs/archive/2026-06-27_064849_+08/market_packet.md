# Market Packet — 2026-06-27T06:48:49.308581+08:00

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
| SPY | 2026-06-26 | 728.99 | -0.72 | -2.38 | -2.86 | -0.73 | 5.57 | 43.21 | 1.32 | 0.00 | 0.28 | BELOW_50_ABOVE_200 |
| QQQ | 2026-06-26 | 706.52 | -1.38 | -4.60 | -3.14 | 0.53 | 11.76 | 46.46 | 2.31 | -0.28 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-26 | 550.25 | 1.36 | -4.67 | -13.38 | -10.22 | -15.35 | 37.38 | 3.38 | -10.52 | -10.24 | BELOW_50_AND_200 |
| AMZN | 2026-06-26 | 232.69 | 2.50 | -4.79 | -14.40 | -9.15 | -0.03 | 39.49 | 3.38 | -11.54 | -11.26 | BELOW_50_AND_200 |
| MU | 2026-06-26 | 1132.33 | -6.69 | -0.15 | 21.96 | 41.16 | 165.91 | 58.95 | 8.40 | 24.83 | 25.11 | ABOVE_50_AND_200 |
| ORCL | 2026-06-26 | 148.53 | -2.58 | -19.40 | -22.22 | -21.44 | -26.88 | 29.59 | 7.56 | -19.36 | -19.08 | BELOW_50_AND_200 |
| SOFI | 2026-06-26 | 17.88 | 3.35 | -0.17 | 10.58 | 5.46 | -20.51 | 57.36 | 5.39 | 13.44 | 13.72 | MIXED |
| IAU | 2026-06-26 | 76.56 | 1.12 | -3.49 | -8.56 | -9.27 | -8.66 | 35.42 | 2.27 | -5.70 | -5.42 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-26 | 18.41 | -2.54 | 12.26 | 13.01 | 3.50 | MIXED |
| ^TNX | 2026-06-26 | 4.37 | -1.77 | -2.56 | -4.37 | -1.31 | BELOW_50_ABOVE_200 |
| CL=F | 2026-06-26 | 70.24 | -2.34 | -8.30 | -20.79 | -23.66 | BELOW_50_AND_200 |
| GC=F | 2026-06-26 | 4103.00 | 1.80 | -2.87 | -7.75 | -8.59 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-26 | 101.37 | -0.06 | 0.51 | 2.17 | 2.16 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.33 | XLE, XOP, USO |
| semis_ai | -4.80 | SMH, SOXX |
| high_beta | -1.94 | IWM, ARKK, HIBL |
| rates | 0.01 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 2.23 | SH, PSQ, SQQQ |
| housing_rates | 0.19 | XHB, ITB |
| defensives | 0.84 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.66 | 4.74 | -6.93 | BELOW_50_AND_200 |
| ARKK | high_beta | 2.08 | 0.23 | 0.87 | MIXED |
| PSQ | equity_hedges | 1.52 | 2.11 | -1.61 | BELOW_50_AND_200 |
| XLP | defensives | 0.92 | 0.15 | 1.07 | ABOVE_50_AND_200 |
| XLU | defensives | 0.76 | 2.35 | 2.57 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.62 | 12.11 | 10.55 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.51 | 1.99 | -0.09 | BELOW_50_AND_200 |
| IWM | high_beta | 0.31 | 3.26 | 5.35 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -8.19 | 3.28 | 11.31 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -5.64 | 4.60 | 11.22 | ABOVE_50_AND_200 |
| SMH | semis_ai | -3.97 | 2.71 | 7.97 | ABOVE_50_AND_200 |
| USO | energy | -3.50 | -19.50 | -20.34 | BELOW_50_ABOVE_200 |
| XLE | energy | -0.46 | -5.53 | -5.84 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -0.24 | 11.94 | 10.21 | ABOVE_50_AND_200 |
| UUP | dollar | -0.07 | 2.56 | 2.55 | ABOVE_50_AND_200 |
| TBF | rates | -0.04 | -3.04 | -2.39 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
