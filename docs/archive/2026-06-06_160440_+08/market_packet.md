# Market Packet — 2026-06-06T16:04:40.253645+08:00

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
| SPY | 2026-06-05 | 737.55 | -2.58 | -2.50 | 0.51 | 3.37 | 7.84 | 49.44 | 1.03 | 0.00 | -0.83 | ABOVE_50_AND_200 |
| QQQ | 2026-06-05 | 705.06 | -4.80 | -4.50 | 1.34 | 5.58 | 13.39 | 48.33 | 1.69 | 0.83 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-05 | 593.00 | -5.51 | -6.25 | -3.24 | -4.28 | -10.48 | 41.56 | 3.30 | -3.75 | -4.58 | BELOW_50_AND_200 |
| AMZN | 2026-06-05 | 246.03 | -3.06 | -9.09 | -10.53 | -2.04 | 5.99 | 37.81 | 2.94 | -11.04 | -11.87 | BELOW_50_ABOVE_200 |
| MU | 2026-06-05 | 864.01 | -13.25 | -11.02 | 29.62 | 39.95 | 139.43 | 55.17 | 7.62 | 29.11 | 28.28 | ABOVE_50_AND_200 |
| ORCL | 2026-06-05 | 213.68 | -9.59 | -5.36 | 10.13 | 19.03 | 3.34 | 55.61 | 5.86 | 9.62 | 8.79 | ABOVE_50_AND_200 |
| SOFI | 2026-06-05 | 16.03 | -6.53 | -12.02 | -1.66 | -4.28 | -30.47 | 45.42 | 5.93 | -2.16 | -2.99 | BELOW_50_AND_200 |
| IAU | 2026-06-05 | 81.22 | -3.63 | -4.99 | -8.02 | -6.65 | -2.01 | 33.02 | 1.99 | -8.53 | -9.35 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-05 | 21.51 | 39.68 | 40.40 | 25.94 | 13.24 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-05 | 4.54 | 1.32 | 1.86 | 4.13 | 3.02 | ABOVE_50_AND_200 |
| CL=F | 2026-06-05 | 90.54 | -2.69 | 3.64 | -4.77 | -7.49 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-05 | 4337.10 | -3.10 | -4.90 | -7.36 | -6.21 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-05 | 100.07 | 0.66 | 1.17 | 2.09 | 1.17 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.50 | XLE, XOP, USO |
| semis_ai | -9.83 | SMH, SOXX |
| high_beta | -9.31 | IWM, ARKK, HIBL |
| rates | 0.37 | TLT, TBF, TBT |
| dollar | 0.65 | UUP |
| equity_hedges | 7.29 | SH, PSQ, SQQQ |
| housing_rates | -0.83 | XHB, ITB |
| defensives | 1.32 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 14.38 | -5.26 | -19.95 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 4.84 | -1.23 | -5.83 | BELOW_50_AND_200 |
| SH | equity_hedges | 2.65 | -0.06 | -3.04 | BELOW_50_AND_200 |
| XLP | defensives | 1.71 | -0.95 | 0.37 | ABOVE_50_AND_200 |
| TBT | rates | 1.15 | 2.27 | 1.20 | ABOVE_50_AND_200 |
| XLU | defensives | 0.93 | -2.98 | -2.44 | BELOW_50_AND_200 |
| UUP | dollar | 0.65 | 2.45 | 1.52 | ABOVE_50_AND_200 |
| TBF | rates | 0.49 | 1.19 | 0.70 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -17.42 | 1.67 | 15.88 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -10.44 | 6.49 | 16.73 | ABOVE_50_AND_200 |
| SMH | semis_ai | -9.22 | 3.63 | 12.38 | ABOVE_50_AND_200 |
| ARKK | high_beta | -6.97 | -6.40 | -1.05 | BELOW_50_AND_200 |
| IWM | high_beta | -3.55 | -1.80 | 2.75 | ABOVE_50_AND_200 |
| XOP | energy | -2.94 | -1.97 | -3.25 | BELOW_50_ABOVE_200 |
| USO | energy | -2.72 | -0.69 | -1.37 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.84 | 1.18 | -0.83 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
