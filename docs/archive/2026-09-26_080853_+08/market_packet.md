# Market Packet — 2026-09-26T08:08:53.253212+08:00

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
| SPY | 2026-09-24 | 767.18 | -0.08 | 0.60 | 0.17 | 0.79 | 6.85 | 52.47 | 0.87 | 0.00 | -4.11 | ABOVE_50_AND_200 |
| QQQ | 2026-09-24 | 741.10 | -0.01 | 3.37 | 4.27 | 4.10 | 11.45 | 63.13 | 1.29 | 4.11 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-24 | 777.59 | 4.50 | 13.96 | 36.41 | 26.64 | 24.21 | 80.51 | 3.50 | 36.24 | 32.13 | ABOVE_50_AND_200 |
| AMZN | 2026-09-24 | 249.38 | 0.04 | -0.72 | -4.47 | -2.65 | 3.59 | 44.20 | 2.33 | -4.64 | -8.75 | BELOW_50_ABOVE_200 |
| MU | 2026-09-24 | 1080.53 | 0.81 | 10.54 | 15.82 | 15.31 | 64.48 | 63.02 | 4.44 | 15.65 | 11.54 | ABOVE_50_AND_200 |
| ORCL | 2026-09-24 | 139.54 | -3.47 | -7.34 | -3.61 | -1.72 | -15.41 | 42.52 | 5.08 | -3.77 | -7.88 | BELOW_50_AND_200 |
| SOFI | 2026-09-24 | 16.80 | 1.51 | 0.42 | -11.58 | -4.54 | -12.83 | 43.56 | 4.16 | -11.74 | -15.85 | BELOW_50_AND_200 |
| IAU | 2026-09-24 | 80.30 | -0.27 | -1.70 | -8.50 | -0.79 | -5.88 | 43.55 | 1.77 | -8.67 | -12.78 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-25 | 14.87 | -5.11 | 0.41 | 2.48 | -6.91 | BELOW_50_AND_200 |
| ^TNX | 2026-09-25 | 5.18 | 0.43 | 3.72 | 11.15 | 8.72 | ABOVE_50_AND_200 |
| CL=F | 2026-09-25 | 92.44 | -2.29 | -7.84 | 12.42 | 5.00 | ABOVE_50_AND_200 |
| GC=F | 2026-09-25 | 4320.50 | 0.52 | -2.36 | -7.15 | -0.78 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-25 | 101.03 | -0.25 | 0.81 | 1.88 | 1.08 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.33 | XLE, XOP, USO |
| semis_ai | -0.04 | SMH, SOXX |
| high_beta | 0.50 | IWM, ARKK, HIBL |
| rates | 0.88 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | 0.08 | SH, PSQ, SQQQ |
| housing_rates | -0.42 | XHB, ITB |
| defensives | -0.93 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.86 | 21.36 | 13.36 | ABOVE_50_AND_200 |
| TBT | rates | 2.72 | 9.60 | 6.69 | ABOVE_50_AND_200 |
| ARKK | high_beta | 2.15 | 6.17 | 12.70 | ABOVE_50_AND_200 |
| TBF | rates | 1.20 | 4.55 | 3.12 | ABOVE_50_AND_200 |
| XOP | energy | 0.77 | 0.72 | 1.13 | ABOVE_50_AND_200 |
| XLE | energy | 0.37 | 0.87 | 1.53 | ABOVE_50_AND_200 |
| UUP | dollar | 0.14 | 2.68 | 1.66 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 0.12 | -13.38 | -13.48 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TLT | rates | -1.29 | -4.85 | -3.55 | BELOW_50_AND_200 |
| XLU | defensives | -0.98 | -9.12 | -9.28 | BELOW_50_AND_200 |
| XLP | defensives | -0.89 | -5.57 | -3.64 | BELOW_50_AND_200 |
| HIBL | high_beta | -0.57 | 4.29 | 7.79 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.54 | -10.03 | -7.06 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.30 | -9.01 | -7.30 | BELOW_50_AND_200 |
| SMH | semis_ai | -0.15 | 8.04 | 6.26 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.09 | -5.87 | -4.29 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
