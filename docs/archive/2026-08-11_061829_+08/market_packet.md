# Market Packet — 2026-08-11T06:18:29.755131+08:00

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
| SPY | 2026-08-10 | 773.03 | -0.03 | 2.03 | 2.39 | 3.41 | 9.89 | 65.74 | 1.09 | 0.00 | 3.03 | ABOVE_50_AND_200 |
| QQQ | 2026-08-10 | 720.87 | -0.30 | 2.97 | -0.64 | 0.92 | 11.18 | 56.18 | 1.97 | -3.03 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-10 | 594.92 | 0.48 | 0.79 | -11.10 | -0.67 | -5.66 | 48.56 | 3.82 | -13.50 | -10.46 | BELOW_50_AND_200 |
| AMZN | 2026-08-10 | 278.09 | 1.32 | -2.09 | 13.35 | 12.32 | 17.43 | 65.87 | 3.28 | 10.95 | 13.99 | ABOVE_50_AND_200 |
| MU | 2026-08-10 | 861.00 | -1.89 | 3.80 | -12.08 | -11.21 | 59.94 | 46.30 | 9.29 | -14.47 | -11.44 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-10 | 151.05 | 2.74 | 6.49 | 7.40 | -5.14 | -15.47 | 59.42 | 4.92 | 5.01 | 8.04 | BELOW_50_AND_200 |
| SOFI | 2026-08-10 | 18.12 | -1.41 | 0.50 | -3.51 | 3.78 | -13.82 | 54.49 | 4.70 | -5.91 | -2.87 | MIXED |
| IAU | 2026-08-10 | 82.51 | 1.02 | 8.30 | 6.80 | 5.36 | -2.20 | 67.59 | 1.87 | 4.40 | 7.43 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-10 | 15.46 | 3.76 | -2.52 | 2.86 | -10.48 | BELOW_50_AND_200 |
| ^TNX | 2026-08-10 | 4.70 | 0.84 | 0.28 | 2.85 | 3.40 | ABOVE_50_AND_200 |
| CL=F | 2026-08-10 | 82.23 | 5.18 | 2.35 | 15.15 | 2.36 | ABOVE_50_AND_200 |
| GC=F | 2026-08-10 | 4450.20 | 2.52 | 10.33 | 8.43 | 6.76 | MIXED |
| DX-Y.NYB | 2026-08-10 | 99.81 | 0.21 | -0.15 | -1.15 | -0.69 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 5.71 | XLE, XOP, USO |
| semis_ai | -2.42 | SMH, SOXX |
| high_beta | -0.46 | IWM, ARKK, HIBL |
| rates | 0.58 | TLT, TBF, TBT |
| dollar | 0.25 | UUP |
| equity_hedges | 0.40 | SH, PSQ, SQQQ |
| housing_rates | -2.51 | XHB, ITB |
| defensives | -0.65 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 6.73 | 15.84 | 4.00 | ABOVE_50_AND_200 |
| XOP | energy | 5.73 | 10.95 | 6.91 | ABOVE_50_AND_200 |
| XLE | energy | 4.66 | 9.26 | 6.18 | ABOVE_50_AND_200 |
| TBT | rates | 1.64 | 5.89 | 6.00 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.27 | 0.24 | 3.89 | ABOVE_50_AND_200 |
| TBF | rates | 0.95 | 3.07 | 3.09 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.88 | -0.13 | -6.18 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.31 | 0.67 | -1.29 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -2.72 | 0.64 | 0.72 | MIXED |
| SOXX | semis_ai | -2.55 | -8.94 | -6.41 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -2.31 | -0.34 | -0.04 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -2.28 | -6.81 | -4.19 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -2.13 | -8.40 | -5.53 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.10 | -5.02 | -3.80 | BELOW_50_AND_200 |
| TLT | rates | -0.85 | -2.85 | -3.15 | BELOW_50_AND_200 |
| IWM | high_beta | -0.52 | 1.35 | 2.02 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
