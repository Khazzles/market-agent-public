# Market Packet — 2026-06-17T00:09:02.489334+08:00

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
| SPY | 2026-06-16 | 753.32 | 1.56 | 1.91 | 0.69 | 3.94 | 9.68 | 59.66 | 1.31 | 0.00 | -3.04 | ABOVE_50_AND_200 |
| QQQ | 2026-06-16 | 735.34 | -1.16 | 3.89 | 3.73 | 6.89 | 17.27 | 58.60 | 2.09 | 3.04 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-16 | 594.99 | 0.25 | 1.78 | -3.13 | -4.44 | -9.37 | 46.89 | 3.24 | -3.82 | -6.86 | BELOW_50_AND_200 |
| AMZN | 2026-06-16 | 247.39 | 3.71 | 0.88 | -7.42 | -3.18 | 6.36 | 44.54 | 3.12 | -8.11 | -11.15 | BELOW_50_ABOVE_200 |
| MU | 2026-06-16 | 1052.42 | 7.21 | 10.87 | 35.62 | 52.22 | 172.38 | 64.82 | 7.37 | 34.93 | 31.89 | ABOVE_50_AND_200 |
| ORCL | 2026-06-16 | 189.93 | 3.15 | -10.33 | -2.90 | 2.19 | -7.63 | 45.28 | 7.04 | -3.59 | -6.63 | MIXED |
| SOFI | 2026-06-16 | 17.52 | 2.31 | 6.41 | 12.27 | 3.80 | -23.04 | 56.11 | 5.25 | 11.58 | 8.54 | MIXED |
| IAU | 2026-06-16 | 81.67 | 3.13 | 0.35 | -6.71 | -5.28 | -2.05 | 44.29 | 2.23 | -7.40 | -10.44 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-16 | 15.95 | -9.79 | -15.70 | -13.46 | -11.81 | BELOW_50_AND_200 |
| ^TNX | 2026-06-16 | 4.43 | -1.27 | -2.68 | -0.69 | 0.22 | ABOVE_50_AND_200 |
| CL=F | 2026-06-16 | 75.01 | -7.11 | -14.95 | -28.85 | -21.35 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-16 | 4358.40 | 0.70 | 2.31 | -4.33 | -4.74 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-16 | 99.49 | -0.26 | -0.56 | 0.61 | 0.61 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -6.06 | XLE, XOP, USO |
| semis_ai | -0.18 | SMH, SOXX |
| high_beta | -1.05 | IWM, ARKK, HIBL |
| rates | -0.38 | TLT, TBF, TBT |
| dollar | -0.16 | UUP |
| equity_hedges | -3.26 | SH, PSQ, SQQQ |
| housing_rates | 1.64 | XHB, ITB |
| defensives | 1.06 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | 2.12 | 14.88 | 23.66 | ABOVE_50_AND_200 |
| XHB | housing_rates | 2.01 | 9.66 | 6.00 | ABOVE_50_AND_200 |
| XLU | defensives | 1.98 | 1.14 | 0.32 | ABOVE_50_AND_200 |
| ITB | housing_rates | 1.26 | 9.76 | 4.60 | MIXED |
| TLT | rates | 0.61 | 3.08 | 0.68 | MIXED |
| XLP | defensives | 0.14 | 1.13 | 2.89 | ABOVE_50_AND_200 |
| UUP | dollar | -0.16 | 1.03 | 1.04 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.21 | 6.09 | 3.75 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -8.99 | -20.17 | -15.47 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -6.24 | -8.60 | -23.41 | BELOW_50_AND_200 |
| XOP | energy | -5.13 | -7.31 | -7.41 | BELOW_50_ABOVE_200 |
| XLE | energy | -4.05 | -4.91 | -4.33 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -2.65 | 29.58 | 27.43 | ABOVE_50_AND_200 |
| SMH | semis_ai | -2.48 | 13.43 | 17.15 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.97 | -2.20 | -7.30 | BELOW_50_AND_200 |
| SH | equity_hedges | -1.56 | -0.29 | -3.50 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
