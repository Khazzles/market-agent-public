# Market Packet — 2026-09-02T07:32:59.518688+08:00

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
| SPY | 2026-09-01 | 761.78 | -0.69 | -0.54 | 0.54 | 0.94 | 7.19 | 48.58 | 0.83 | 0.00 | -0.54 | ABOVE_50_AND_200 |
| QQQ | 2026-09-01 | 707.64 | -1.27 | -0.43 | 1.08 | -0.47 | 7.86 | 46.56 | 1.44 | 0.54 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-01 | 578.54 | 1.08 | 1.49 | -1.98 | -2.33 | -7.03 | 49.95 | 3.45 | -2.52 | -3.06 | BELOW_50_AND_200 |
| AMZN | 2026-09-01 | 254.92 | -1.87 | -2.35 | -10.25 | 0.99 | 6.76 | 46.33 | 2.84 | -10.79 | -11.33 | ABOVE_50_AND_200 |
| MU | 2026-09-01 | 933.44 | -2.64 | 0.05 | 12.53 | -1.32 | 56.76 | 50.45 | 6.15 | 11.99 | 11.45 | BELOW_50_ABOVE_200 |
| ORCL | 2026-09-01 | 141.32 | -5.23 | -2.38 | -0.37 | 0.82 | -16.77 | 46.37 | 4.60 | -0.92 | -1.45 | MIXED |
| SOFI | 2026-09-01 | 17.05 | -4.64 | -10.26 | -5.44 | -4.36 | -15.23 | 42.95 | 5.06 | -5.98 | -6.52 | BELOW_50_AND_200 |
| IAU | 2026-09-01 | 81.35 | -2.82 | -7.00 | 6.80 | 2.76 | -4.29 | 46.59 | 2.07 | 6.26 | 5.72 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-01 | 16.34 | 9.52 | 3.09 | 2.19 | -1.07 | BELOW_50_AND_200 |
| ^TNX | 2026-09-01 | 4.80 | 0.80 | 1.96 | 1.07 | 4.08 | ABOVE_50_AND_200 |
| CL=F | 2026-09-01 | 90.79 | 5.87 | 10.24 | 13.01 | 13.77 | ABOVE_50_AND_200 |
| GC=F | 2026-09-01 | 4373.40 | -1.30 | -5.71 | 8.42 | 3.71 | MIXED |
| DX-Y.NYB | 2026-09-01 | 99.65 | 0.23 | 0.66 | -0.15 | -0.74 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.91 | XLE, XOP, USO |
| semis_ai | -2.07 | SMH, SOXX |
| high_beta | -3.33 | IWM, ARKK, HIBL |
| rates | 0.16 | TLT, TBF, TBT |
| dollar | 0.32 | UUP |
| equity_hedges | 1.95 | SH, PSQ, SQQQ |
| housing_rates | -2.32 | XHB, ITB |
| defensives | 0.55 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 5.46 | 15.46 | 15.66 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 3.79 | -3.52 | 0.15 | MIXED |
| XOP | energy | 1.99 | 8.64 | 12.91 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.36 | -2.50 | 0.73 | MIXED |
| XLE | energy | 1.27 | 10.17 | 10.59 | ABOVE_50_AND_200 |
| TBT | rates | 0.84 | 0.05 | 3.95 | ABOVE_50_AND_200 |
| XLU | defensives | 0.78 | -4.04 | -4.65 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.71 | -1.45 | -0.49 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -5.94 | 4.58 | -10.78 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.91 | 16.62 | 5.04 | ABOVE_50_AND_200 |
| ITB | housing_rates | -2.46 | -2.10 | -6.12 | BELOW_50_AND_200 |
| XHB | housing_rates | -2.19 | -3.02 | -7.31 | BELOW_50_AND_200 |
| SOXX | semis_ai | -2.10 | -1.45 | -8.11 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -2.05 | 0.87 | -6.07 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -1.14 | -0.22 | -2.22 | BELOW_50_ABOVE_200 |
| TLT | rates | -0.79 | -0.39 | -2.19 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
