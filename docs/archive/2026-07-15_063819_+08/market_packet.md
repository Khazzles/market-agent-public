# Market Packet — 2026-07-15T06:38:19.618476+08:00

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
| SPY | 2026-07-14 | 751.83 | 0.36 | 0.55 | 1.91 | 1.24 | 8.12 | 56.04 | 1.16 | 0.00 | 1.55 | ABOVE_50_AND_200 |
| QQQ | 2026-07-14 | 719.69 | 1.12 | 1.45 | 0.36 | 0.35 | 12.59 | 50.69 | 2.09 | -1.55 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-14 | 661.04 | 0.66 | 7.38 | 16.29 | 9.96 | 3.01 | 63.51 | 3.84 | 14.39 | 15.93 | ABOVE_50_AND_200 |
| AMZN | 2026-07-14 | 247.49 | 0.07 | 0.61 | 2.48 | -2.32 | 5.94 | 53.10 | 2.97 | 0.57 | 2.12 | BELOW_50_ABOVE_200 |
| MU | 2026-07-14 | 983.12 | 4.92 | 4.77 | -1.28 | 7.24 | 108.09 | 49.72 | 8.57 | -3.19 | -1.64 | ABOVE_50_AND_200 |
| ORCL | 2026-07-14 | 127.94 | -2.74 | -9.65 | -30.51 | -29.61 | -34.02 | 25.52 | 6.84 | -32.41 | -30.86 | BELOW_50_AND_200 |
| SOFI | 2026-07-14 | 18.55 | 2.32 | 4.51 | 11.28 | 9.46 | -15.58 | 57.13 | 5.11 | 9.37 | 10.92 | MIXED |
| IAU | 2026-07-14 | 76.27 | 1.36 | -1.42 | -3.61 | -6.74 | -9.43 | 41.34 | 2.13 | -5.52 | -3.97 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-14 | 16.50 | -3.85 | 2.29 | -15.12 | -4.96 | BELOW_50_AND_200 |
| ^TNX | 2026-07-14 | 4.58 | -0.52 | 1.24 | 2.73 | 2.22 | ABOVE_50_AND_200 |
| CL=F | 2026-07-14 | 79.92 | 2.28 | 13.46 | -8.88 | -7.91 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-14 | 4056.20 | 1.48 | -2.15 | -0.83 | -6.78 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-14 | 100.94 | -0.33 | -0.20 | 1.08 | 1.14 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.93 | XLE, XOP, USO |
| semis_ai | 2.55 | SMH, SOXX |
| high_beta | 2.05 | IWM, ARKK, HIBL |
| rates | -0.13 | TLT, TBF, TBT |
| dollar | -0.39 | UUP |
| equity_hedges | -1.60 | SH, PSQ, SQQQ |
| housing_rates | 0.94 | XHB, ITB |
| defensives | -0.72 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.17 | -1.75 | -1.46 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 2.58 | -3.24 | 0.98 | ABOVE_50_AND_200 |
| SMH | semis_ai | 2.51 | -1.50 | 1.10 | ABOVE_50_AND_200 |
| USO | energy | 2.02 | -6.72 | -5.56 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 1.64 | 5.38 | 1.57 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.02 | 0.31 | 2.41 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.86 | -0.62 | 1.97 | MIXED |
| XOP | energy | 0.40 | 1.49 | 0.75 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.30 | -5.39 | -5.38 | BELOW_50_AND_200 |
| XLP | defensives | -1.38 | -2.17 | -0.82 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -1.16 | -1.46 | -1.19 | BELOW_50_AND_200 |
| TBT | rates | -0.41 | 3.62 | 2.21 | ABOVE_50_AND_200 |
| UUP | dollar | -0.39 | 1.57 | 1.54 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.33 | -2.61 | -1.58 | BELOW_50_AND_200 |
| TBF | rates | -0.12 | 1.68 | 1.08 | ABOVE_50_AND_200 |
| XLU | defensives | -0.07 | 3.72 | 1.67 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
