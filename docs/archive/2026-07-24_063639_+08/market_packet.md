# Market Packet — 2026-07-24T06:36:39.924069+08:00

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
| SPY | 2026-07-23 | 738.18 | -1.23 | -1.67 | 0.63 | -0.92 | 5.73 | 44.56 | 1.12 | 0.00 | 3.67 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-23 | 691.96 | -1.90 | -1.98 | -3.04 | -3.73 | 7.65 | 41.82 | 2.09 | -3.67 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-23 | 606.10 | -3.36 | -8.79 | 7.81 | -0.02 | -5.10 | 46.30 | 4.15 | 7.18 | 10.85 | BELOW_50_AND_200 |
| AMZN | 2026-07-23 | 233.66 | -4.57 | -6.49 | -0.19 | -6.50 | -0.37 | 38.62 | 3.21 | -0.82 | 2.85 | BELOW_50_AND_200 |
| MU | 2026-07-23 | 990.21 | 3.20 | 16.06 | -5.85 | 3.98 | 98.67 | 52.52 | 8.14 | -6.48 | -2.81 | ABOVE_50_AND_200 |
| ORCL | 2026-07-23 | 120.04 | -4.61 | -3.36 | -27.32 | -30.61 | -36.24 | 29.63 | 6.47 | -27.95 | -24.28 | BELOW_50_AND_200 |
| SOFI | 2026-07-23 | 16.65 | -2.46 | -3.87 | -3.70 | -2.66 | -23.07 | 42.41 | 5.22 | -4.33 | -0.66 | BELOW_50_AND_200 |
| IAU | 2026-07-23 | 76.15 | -1.98 | 1.80 | -1.53 | -5.04 | -9.72 | 44.40 | 1.96 | -2.15 | 1.51 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-23 | 18.70 | 12.38 | 11.78 | -4.05 | 7.90 | MIXED |
| ^TNX | 2026-07-23 | 4.70 | 0.99 | 2.93 | 4.67 | 4.17 | ABOVE_50_AND_200 |
| CL=F | 2026-07-23 | 92.21 | 6.20 | 16.80 | 25.95 | 8.92 | ABOVE_50_AND_200 |
| GC=F | 2026-07-23 | 4052.00 | -2.29 | 1.67 | -1.89 | -5.04 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-23 | 101.44 | 0.29 | 0.70 | 0.03 | 1.25 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.90 | XLE, XOP, USO |
| semis_ai | -0.96 | SMH, SOXX |
| high_beta | -2.46 | IWM, ARKK, HIBL |
| rates | 0.18 | TLT, TBF, TBT |
| dollar | 0.39 | UUP |
| equity_hedges | 2.94 | SH, PSQ, SQQQ |
| housing_rates | -0.58 | XHB, ITB |
| defensives | -0.41 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 5.93 | 25.37 | 11.12 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 5.69 | 6.68 | 7.87 | MIXED |
| PSQ | equity_hedges | 1.83 | 2.34 | 3.17 | MIXED |
| SH | equity_hedges | 1.30 | -1.03 | 0.75 | MIXED |
| XLU | defensives | 0.57 | 2.48 | 2.88 | ABOVE_50_AND_200 |
| TBT | rates | 0.54 | 6.86 | 4.22 | ABOVE_50_AND_200 |
| UUP | dollar | 0.39 | 0.39 | 1.64 | ABOVE_50_AND_200 |
| TBF | rates | 0.32 | 3.20 | 2.17 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -3.90 | -17.07 | -11.86 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.89 | -3.72 | -5.35 | BELOW_50_AND_200 |
| XLP | defensives | -1.39 | -0.61 | -1.15 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -1.15 | -6.73 | -3.12 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -0.94 | -2.87 | -1.25 | BELOW_50_AND_200 |
| SOXX | semis_ai | -0.77 | -8.64 | -3.12 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.58 | -1.09 | 0.37 | ABOVE_50_AND_200 |
| XOP | energy | -0.53 | 13.30 | 6.84 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
