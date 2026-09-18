# Market Packet — 2026-09-19T07:34:23.677751+08:00

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
| SPY | 2026-09-18 | 761.69 | -0.12 | -0.34 | -0.96 | 0.26 | 6.34 | 49.18 | 0.87 | 0.00 | -1.71 | ABOVE_50_AND_200 |
| QQQ | 2026-09-18 | 721.45 | 0.63 | 0.92 | 0.75 | 1.62 | 8.88 | 55.86 | 1.29 | 1.71 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-18 | 665.75 | -2.43 | 2.73 | 21.93 | 9.61 | 6.66 | 65.85 | 3.19 | 22.88 | 21.18 | ABOVE_50_AND_200 |
| AMZN | 2026-09-18 | 253.71 | 1.00 | -1.20 | -4.56 | -0.83 | 5.58 | 48.04 | 2.38 | -3.60 | -5.31 | BELOW_50_ABOVE_200 |
| MU | 2026-09-18 | 1015.80 | 3.92 | 4.16 | 8.40 | 9.55 | 58.68 | 58.28 | 4.85 | 9.36 | 7.65 | ABOVE_50_AND_200 |
| ORCL | 2026-09-18 | 147.61 | -1.98 | -1.78 | 2.64 | 4.69 | -11.21 | 49.64 | 5.18 | 3.60 | 1.89 | MIXED |
| SOFI | 2026-09-18 | 16.96 | 1.37 | -2.08 | -7.93 | -4.27 | -13.10 | 43.76 | 4.22 | -6.97 | -8.68 | BELOW_50_AND_200 |
| IAU | 2026-09-18 | 82.23 | 0.66 | 0.64 | -3.08 | 2.09 | -3.57 | 50.62 | 1.92 | -2.12 | -3.83 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-18 | 14.81 | -4.08 | -6.50 | -7.50 | -8.43 | BELOW_50_AND_200 |
| ^TNX | 2026-09-18 | 5.00 | 1.03 | 0.46 | 7.41 | 5.93 | ABOVE_50_AND_200 |
| CL=F | 2026-09-18 | 95.47 | -6.32 | -4.58 | 11.23 | 10.62 | ABOVE_50_AND_200 |
| GC=F | 2026-09-18 | 4415.90 | 0.37 | 0.16 | -2.85 | 2.10 | MIXED |
| DX-Y.NYB | 2026-09-18 | 100.22 | -0.01 | 1.10 | 1.40 | 0.26 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.75 | XLE, XOP, USO |
| semis_ai | 2.45 | SMH, SOXX |
| high_beta | 1.31 | IWM, ARKK, HIBL |
| rates | 0.54 | TLT, TBF, TBT |
| dollar | 0.04 | UUP |
| equity_hedges | -0.77 | SH, PSQ, SQQQ |
| housing_rates | -0.99 | XHB, ITB |
| defensives | -1.12 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 2.90 | -5.22 | -0.39 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 2.69 | 2.58 | 1.41 | ABOVE_50_AND_200 |
| SMH | semis_ai | 2.21 | 2.15 | 1.45 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.51 | 5.91 | 9.68 | ABOVE_50_AND_200 |
| TBT | rates | 1.45 | 4.18 | 3.06 | ABOVE_50_AND_200 |
| TBF | rates | 0.82 | 2.34 | 1.82 | ABOVE_50_AND_200 |
| UUP | dollar | 0.04 | 1.83 | 0.65 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.06 | 1.24 | 0.01 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -1.71 | -1.71 | -5.04 | BELOW_50_AND_200 |
| XLU | defensives | -1.42 | -6.63 | -6.21 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.29 | -11.94 | -8.64 | BELOW_50_AND_200 |
| XOP | energy | -1.03 | 2.30 | 5.64 | ABOVE_50_AND_200 |
| USO | energy | -0.96 | 17.50 | 16.07 | ABOVE_50_AND_200 |
| XLP | defensives | -0.83 | -4.32 | -2.49 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.70 | -10.94 | -8.44 | BELOW_50_AND_200 |
| TLT | rates | -0.65 | -2.13 | -1.65 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
