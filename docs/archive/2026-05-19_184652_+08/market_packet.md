# Market Packet — 2026-05-19T18:46:52.097316+08:00

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
| SPY | 2026-05-18 | 738.65 | -0.07 | -0.09 | 4.01 | 6.84 | 9.17 | 67.37 | 1.05 | 0.00 | -4.77 | ABOVE_50_AND_200 |
| QQQ | 2026-05-18 | 705.88 | -0.43 | -1.04 | 8.79 | 11.41 | 15.40 | 68.98 | 1.54 | 4.77 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-18 | 611.21 | -0.49 | 2.06 | -11.23 | -1.61 | -9.13 | 44.50 | 2.73 | -15.25 | -20.02 | BELOW_50_AND_200 |
| AMZN | 2026-05-18 | 264.86 | 0.27 | -1.54 | 5.71 | 11.41 | 15.37 | 59.27 | 2.50 | 1.69 | -3.08 | ABOVE_50_AND_200 |
| MU | 2026-05-18 | 681.54 | -5.95 | -14.31 | 49.77 | 38.39 | 119.86 | 59.62 | 7.18 | 45.75 | 40.98 | ABOVE_50_AND_200 |
| ORCL | 2026-05-18 | 186.61 | -3.29 | -3.73 | 6.60 | 13.34 | -10.83 | 56.47 | 4.90 | 2.58 | -2.19 | MIXED |
| SOFI | 2026-05-18 | 15.71 | 0.64 | -3.38 | -19.15 | -7.50 | -33.00 | 42.02 | 5.14 | -23.16 | -27.94 | BELOW_50_AND_200 |
| IAU | 2026-05-18 | 85.76 | 0.29 | -3.71 | -6.11 | -3.39 | 5.20 | 41.27 | 1.88 | -10.12 | -14.90 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-19 | 18.15 | 1.85 | 0.89 | -3.82 | -14.75 | BELOW_50_AND_200 |
| ^TNX | 2026-05-18 | 4.62 | 0.61 | 4.83 | 8.88 | 6.57 | ABOVE_50_AND_200 |
| CL=F | 2026-05-19 | 103.09 | -5.13 | 0.89 | 15.04 | 5.42 | ABOVE_50_AND_200 |
| GC=F | 2026-05-19 | 4544.60 | -0.17 | -2.84 | -5.45 | -3.47 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-19 | 99.23 | 0.27 | 0.96 | 1.21 | 0.27 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.28 | XLE, XOP, USO |
| semis_ai | -2.16 | SMH, SOXX |
| high_beta | -2.11 | IWM, ARKK, HIBL |
| rates | 0.10 | TLT, TBF, TBT |
| dollar | -0.25 | UUP |
| equity_hedges | 0.64 | SH, PSQ, SQQQ |
| housing_rates | 0.66 | XHB, ITB |
| defensives | 0.82 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLE | energy | 1.92 | 10.11 | 4.16 | ABOVE_50_AND_200 |
| XLP | defensives | 1.49 | 4.17 | 3.41 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.30 | -22.79 | -30.94 | BELOW_50_AND_200 |
| ITB | housing_rates | 1.23 | -10.61 | -6.32 | BELOW_50_AND_200 |
| XOP | energy | 1.19 | 10.35 | 2.47 | ABOVE_50_AND_200 |
| USO | energy | 0.72 | 28.65 | 15.89 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.46 | -7.85 | -10.64 | BELOW_50_AND_200 |
| TBT | rates | 0.21 | 8.10 | 6.26 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.21 | 6.81 | 18.02 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.49 | 19.28 | 22.59 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.83 | 17.67 | 20.09 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.59 | 0.07 | 4.40 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.52 | -5.96 | 1.31 | MIXED |
| UUP | dollar | -0.25 | 1.24 | 0.48 | ABOVE_50_AND_200 |
| TLT | rates | -0.12 | -4.03 | -3.22 | BELOW_50_AND_200 |
| XHB | housing_rates | 0.09 | -10.11 | -5.70 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
