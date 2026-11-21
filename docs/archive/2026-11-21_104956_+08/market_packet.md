# Market Packet — 2026-11-21T10:49:56.135310+08:00

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
| SPY | 2026-11-20 | 689.81 | -3.64 | -8.56 | -9.71 | -9.26 | -5.86 | 24.91 | 1.97 | 0.00 | 3.92 | BELOW_50_AND_200 |
| QQQ | 2026-11-20 | 608.45 | -5.67 | -10.51 | -13.63 | -14.42 | -10.92 | 26.63 | 3.09 | -3.92 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-20 | 560.84 | -5.93 | -12.60 | -13.56 | -17.12 | -10.78 | 30.26 | 4.15 | -3.86 | 0.07 | BELOW_50_AND_200 |
| AMZN | 2026-11-20 | 246.82 | -4.10 | -7.44 | -1.42 | -3.22 | 0.68 | 42.30 | 4.04 | 8.28 | 12.21 | BELOW_50_ABOVE_200 |
| MU | 2026-11-20 | 594.51 | -13.89 | -23.62 | -30.59 | -34.83 | -23.05 | 29.52 | 10.40 | -20.88 | -16.96 | BELOW_50_AND_200 |
| ORCL | 2026-11-20 | 101.19 | -8.48 | -19.27 | -19.40 | -23.42 | -33.91 | 31.83 | 7.84 | -9.69 | -5.77 | BELOW_50_AND_200 |
| SOFI | 2026-11-20 | 12.48 | -7.76 | -19.07 | -15.50 | -21.00 | -27.17 | 27.69 | 6.51 | -5.80 | -1.87 | BELOW_50_AND_200 |
| IAU | 2026-11-20 | 66.23 | -3.62 | -9.12 | -12.46 | -13.84 | -20.37 | 23.66 | 2.28 | -2.76 | 1.17 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-20 | 35.89 | 26.20 | 85.96 | 88.60 | 94.68 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-20 | 4.91 | -2.77 | -4.70 | -0.83 | -3.25 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-20 | 83.62 | 0.49 | -5.58 | -15.93 | -11.18 | BELOW_50_AND_200 |
| GC=F | 2026-11-20 | 3539.00 | -3.98 | -8.94 | -12.84 | -13.92 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-20 | 103.84 | -0.06 | 0.42 | 2.19 | 1.92 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.21 | XLE, XOP, USO |
| semis_ai | -10.57 | SMH, SOXX |
| high_beta | -10.21 | IWM, ARKK, HIBL |
| rates | -0.86 | TLT, TBF, TBT |
| dollar | -0.03 | UUP |
| equity_hedges | 8.53 | SH, PSQ, SQQQ |
| housing_rates | -0.46 | XHB, ITB |
| defensives | -0.04 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 16.53 | 45.43 | 48.12 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 5.46 | 14.71 | 15.49 | ABOVE_50_AND_200 |
| SH | equity_hedges | 3.60 | 10.69 | 10.08 | ABOVE_50_AND_200 |
| TLT | rates | 1.37 | -0.35 | 1.72 | MIXED |
| USO | energy | 1.12 | -14.08 | -7.94 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.67 | 0.52 | 4.70 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.41 | -0.10 | 1.29 | MIXED |
| UUP | dollar | -0.03 | 2.49 | 2.29 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -20.90 | -43.91 | -50.92 | BELOW_50_AND_200 |
| SMH | semis_ai | -10.60 | -23.56 | -26.93 | BELOW_50_AND_200 |
| SOXX | semis_ai | -10.55 | -22.18 | -26.60 | BELOW_50_AND_200 |
| ARKK | high_beta | -6.83 | -21.55 | -22.78 | BELOW_50_AND_200 |
| IWM | high_beta | -2.88 | -7.25 | -7.78 | BELOW_50_AND_200 |
| TBT | rates | -2.53 | 0.58 | -3.76 | BELOW_50_ABOVE_200 |
| TBF | rates | -1.43 | 0.51 | -1.69 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | -1.32 | -2.62 | -1.87 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
