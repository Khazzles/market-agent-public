# Market Packet — 2026-07-31T06:45:14.286010+08:00

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
| SPY | 2026-07-30 | 741.69 | 1.68 | 0.48 | -0.68 | -0.41 | 5.96 | 49.19 | 1.19 | 0.00 | 6.50 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-30 | 683.55 | 3.30 | -1.22 | -7.18 | -4.45 | 6.04 | 43.17 | 2.23 | -6.50 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-30 | 539.03 | -7.95 | -11.07 | -4.31 | -10.62 | -15.15 | 32.11 | 4.75 | -3.63 | 2.87 | BELOW_50_AND_200 |
| AMZN | 2026-07-30 | 235.50 | 3.90 | 0.79 | -1.19 | -4.42 | 0.32 | 44.41 | 3.12 | -0.51 | 5.99 | BELOW_50_ABOVE_200 |
| MU | 2026-07-30 | 874.66 | 18.36 | -11.67 | -24.23 | -9.11 | 69.85 | 46.61 | 10.16 | -23.55 | -17.05 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-30 | 127.56 | 8.34 | 6.26 | -12.96 | -23.13 | -30.68 | 41.69 | 6.13 | -12.28 | -5.78 | BELOW_50_AND_200 |
| SOFI | 2026-07-30 | 16.47 | 8.00 | -1.08 | -8.14 | -4.07 | -22.91 | 45.06 | 5.71 | -7.46 | -0.97 | BELOW_50_AND_200 |
| IAU | 2026-07-30 | 77.30 | 1.66 | 1.51 | 2.37 | -2.30 | -8.39 | 50.36 | 1.87 | 3.05 | 9.55 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-30 | 17.09 | -17.28 | -8.61 | 3.89 | -1.82 | BELOW_50_AND_200 |
| ^TNX | 2026-07-30 | 4.66 | 0.89 | -0.85 | 5.55 | 3.01 | ABOVE_50_AND_200 |
| CL=F | 2026-07-30 | 84.12 | -0.40 | -8.75 | 21.04 | 1.74 | ABOVE_50_AND_200 |
| GC=F | 2026-07-30 | 4166.10 | 3.26 | 2.95 | 3.56 | -1.08 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-30 | 99.97 | -0.82 | -1.44 | -1.21 | -0.44 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.25 | XLE, XOP, USO |
| semis_ai | 7.69 | SMH, SOXX |
| high_beta | 5.71 | IWM, ARKK, HIBL |
| rates | -0.02 | TLT, TBF, TBT |
| dollar | -0.99 | UUP |
| equity_hedges | -4.88 | SH, PSQ, SQQQ |
| housing_rates | -0.65 | XHB, ITB |
| defensives | -1.36 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 12.44 | -29.91 | -17.89 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 8.50 | -21.26 | -11.10 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 6.88 | -17.84 | -9.62 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 3.29 | -9.80 | -5.98 | BELOW_50_AND_200 |
| XOP | energy | 1.65 | 13.36 | 6.37 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.39 | -2.62 | 0.16 | ABOVE_50_AND_200 |
| XLE | energy | 0.53 | 11.01 | 3.98 | ABOVE_50_AND_200 |
| TBF | rates | 0.08 | 4.37 | 2.57 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -9.75 | 22.89 | 10.26 | MIXED |
| PSQ | equity_hedges | -3.30 | 7.70 | 4.02 | MIXED |
| XLP | defensives | -2.16 | 2.89 | 1.42 | ABOVE_50_AND_200 |
| SH | equity_hedges | -1.59 | 1.12 | 0.33 | MIXED |
| USO | energy | -1.42 | 19.77 | 3.00 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.15 | -8.62 | -1.20 | BELOW_50_AND_200 |
| UUP | dollar | -0.99 | -0.95 | -0.16 | BELOW_50_ABOVE_200 |
| XLU | defensives | -0.56 | -1.50 | -0.72 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
