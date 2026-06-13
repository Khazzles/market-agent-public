# Market Packet — 2026-06-13T16:41:08.025804+08:00

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
| SPY | 2026-06-12 | 741.75 | 0.54 | 0.57 | -0.08 | 2.62 | 8.08 | 52.94 | 1.29 | 0.00 | -1.00 | ABOVE_50_AND_200 |
| QQQ | 2026-06-12 | 721.34 | 0.59 | 2.31 | 0.93 | 5.80 | 15.34 | 55.21 | 2.09 | 1.00 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-12 | 566.98 | -0.26 | -4.39 | -8.05 | -8.82 | -13.84 | 34.66 | 3.28 | -7.98 | -8.98 | BELOW_50_AND_200 |
| AMZN | 2026-06-12 | 238.55 | -1.23 | -3.04 | -11.69 | -6.37 | 2.60 | 34.76 | 3.13 | -11.62 | -12.62 | BELOW_50_ABOVE_200 |
| MU | 2026-06-12 | 981.61 | -1.43 | 13.61 | 22.15 | 44.86 | 157.16 | 60.77 | 7.50 | 22.22 | 21.22 | ABOVE_50_AND_200 |
| ORCL | 2026-06-12 | 184.13 | 0.02 | -13.83 | -2.97 | -0.46 | -10.55 | 42.09 | 7.35 | -2.89 | -3.89 | BELOW_50_AND_200 |
| SOFI | 2026-06-12 | 16.58 | -0.54 | 3.43 | 8.30 | -1.50 | -27.45 | 49.71 | 5.72 | 8.37 | 7.37 | BELOW_50_AND_200 |
| IAU | 2026-06-12 | 79.19 | 0.08 | -2.50 | -10.21 | -8.28 | -4.92 | 34.89 | 2.24 | -10.13 | -11.13 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-12 | 17.68 | -9.05 | -17.81 | 2.43 | -3.13 | BELOW_50_AND_200 |
| ^TNX | 2026-06-12 | 4.49 | 0.54 | -1.08 | 0.13 | 1.56 | ABOVE_50_AND_200 |
| CL=F | 2026-06-12 | 84.88 | -3.23 | -6.25 | -15.98 | -12.26 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-12 | 4215.00 | 3.05 | -2.82 | -10.28 | -8.13 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-12 | 99.75 | -0.11 | -0.32 | 1.29 | 0.86 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.24 | XLE, XOP, USO |
| semis_ai | 1.66 | SMH, SOXX |
| high_beta | 1.89 | IWM, ARKK, HIBL |
| rates | 0.19 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -1.03 | SH, PSQ, SQQQ |
| housing_rates | -0.52 | XHB, ITB |
| defensives | 0.87 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.55 | 15.37 | 22.54 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.72 | 8.30 | 17.22 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.59 | 12.86 | 22.43 | ABOVE_50_AND_200 |
| XOP | energy | 1.18 | -1.78 | -2.64 | BELOW_50_ABOVE_200 |
| XLU | defensives | 1.09 | -0.31 | -1.67 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.87 | 3.64 | 5.28 | ABOVE_50_AND_200 |
| XLE | energy | 0.75 | -0.14 | -0.43 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.65 | 1.30 | 2.85 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -2.64 | -11.69 | -7.44 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -1.93 | -4.64 | -19.62 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.81 | 8.97 | 3.47 | MIXED |
| PSQ | equity_hedges | -0.65 | -0.92 | -5.88 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.50 | 0.48 | -2.23 | BELOW_50_AND_200 |
| TLT | rates | -0.24 | 1.14 | 0.10 | MIXED |
| XHB | housing_rates | -0.22 | 8.70 | 4.14 | ABOVE_50_AND_200 |
| UUP | dollar | 0.00 | 1.60 | 1.21 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
