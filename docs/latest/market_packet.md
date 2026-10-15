# Market Packet — 2026-10-15T08:06:09.289012+08:00

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
| SPY | 2026-10-13 | 778.01 | -0.01 | -0.14 | 2.25 | 1.22 | 7.49 | 59.22 | 0.83 | 0.00 | -2.60 | ABOVE_50_AND_200 |
| QQQ | 2026-10-13 | 743.57 | -0.33 | -2.12 | 4.85 | 2.34 | 10.42 | 54.59 | 1.27 | 2.60 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-13 | 762.50 | 2.63 | 3.20 | 14.56 | 17.87 | 20.84 | 66.01 | 3.17 | 12.31 | 9.71 | ABOVE_50_AND_200 |
| AMZN | 2026-10-13 | 258.58 | -0.37 | 0.89 | 1.99 | 0.09 | 6.67 | 54.45 | 2.24 | -0.26 | -2.86 | ABOVE_50_AND_200 |
| MU | 2026-10-13 | 953.19 | -3.62 | -8.83 | 3.16 | -2.93 | 34.52 | 40.35 | 4.90 | 0.90 | -1.69 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-13 | 143.20 | 4.23 | -1.08 | -1.10 | -1.87 | -11.15 | 50.46 | 4.97 | -3.35 | -5.95 | BELOW_50_AND_200 |
| SOFI | 2026-10-13 | 15.24 | 0.07 | -3.30 | -13.65 | -11.99 | -17.86 | 33.43 | 3.93 | -15.91 | -18.50 | BELOW_50_AND_200 |
| IAU | 2026-10-13 | 78.25 | -0.11 | -0.15 | -2.84 | -3.96 | -8.06 | 43.52 | 1.62 | -5.09 | -7.69 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-14 | 16.87 | 10.48 | 11.87 | -1.92 | 9.03 | MIXED |
| ^TNX | 2026-10-14 | 5.19 | -0.52 | -1.65 | 3.88 | 5.36 | ABOVE_50_AND_200 |
| CL=F | 2026-10-14 | 94.76 | 0.66 | 7.34 | -10.46 | 5.24 | ABOVE_50_AND_200 |
| GC=F | 2026-10-14 | 4130.10 | -1.13 | -0.26 | -4.68 | -5.70 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-14 | 102.21 | 0.03 | -0.03 | 2.57 | 1.95 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.00 | XLE, XOP, USO |
| semis_ai | -0.33 | SMH, SOXX |
| high_beta | -0.97 | IWM, ARKK, HIBL |
| rates | -0.28 | TLT, TBF, TBT |
| dollar | -0.38 | UUP |
| equity_hedges | 0.48 | SH, PSQ, SQQQ |
| housing_rates | 0.70 | XHB, ITB |
| defensives | 0.16 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | 2.85 | 3.28 | 7.53 | ABOVE_50_AND_200 |
| XLE | energy | 1.80 | 4.14 | 6.72 | ABOVE_50_AND_200 |
| USO | energy | 1.36 | -2.28 | 9.18 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.07 | -14.66 | -7.82 | BELOW_50_AND_200 |
| ITB | housing_rates | 0.77 | -6.01 | -8.37 | BELOW_50_AND_200 |
| XHB | housing_rates | 0.62 | -3.70 | -6.85 | BELOW_50_AND_200 |
| XLU | defensives | 0.58 | 0.12 | -0.62 | BELOW_50_AND_200 |
| TLT | rates | 0.41 | -3.16 | -3.15 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -1.50 | 13.43 | -0.31 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.97 | 2.89 | 2.07 | ABOVE_50_AND_200 |
| TBT | rates | -0.88 | 5.90 | 5.57 | ABOVE_50_AND_200 |
| SMH | semis_ai | -0.49 | 8.61 | 1.38 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.43 | -3.89 | -4.82 | BELOW_50_AND_200 |
| UUP | dollar | -0.38 | 3.02 | 2.35 | ABOVE_50_AND_200 |
| TBF | rates | -0.38 | 2.63 | 2.76 | ABOVE_50_AND_200 |
| XLP | defensives | -0.26 | -0.27 | 0.23 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
