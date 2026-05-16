# Market Packet — 2026-05-16T17:30:22.122925+08:00

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
| SPY | 2026-05-15 | 739.17 | -1.20 | 0.21 | 5.35 | 7.12 | 9.33 | 67.93 | 1.04 | 0.00 | -5.34 | ABOVE_50_AND_200 |
| QQQ | 2026-05-15 | 708.93 | -1.51 | -0.32 | 10.69 | 12.27 | 16.04 | 71.38 | 1.51 | 5.34 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-15 | 614.23 | -0.68 | 0.75 | -9.25 | -1.23 | -8.79 | 45.59 | 2.78 | -14.60 | -19.94 | BELOW_50_AND_200 |
| AMZN | 2026-05-15 | 264.14 | -1.15 | -3.13 | 5.78 | 11.59 | 15.14 | 58.56 | 2.52 | 0.44 | -4.91 | ABOVE_50_AND_200 |
| MU | 2026-05-15 | 724.66 | -6.62 | -2.97 | 58.49 | 49.03 | 135.95 | 66.28 | 6.28 | 53.14 | 47.80 | ABOVE_50_AND_200 |
| ORCL | 2026-05-15 | 192.95 | -1.36 | -1.53 | 8.19 | 17.67 | -7.95 | 62.51 | 4.71 | 2.85 | -2.50 | MIXED |
| SOFI | 2026-05-15 | 15.61 | -2.56 | -0.89 | -17.97 | -8.44 | -33.52 | 41.09 | 5.08 | -23.32 | -28.66 | BELOW_50_AND_200 |
| IAU | 2026-05-15 | 85.51 | -2.32 | -3.78 | -5.16 | -3.91 | 5.05 | 40.15 | 1.94 | -10.50 | -15.85 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-15 | 18.43 | 6.78 | 7.21 | 2.73 | -14.95 | BELOW_50_ABOVE_200 |
| ^TNX | 2026-05-15 | 4.59 | 3.00 | 5.29 | 6.64 | 6.16 | ABOVE_50_AND_200 |
| CL=F | 2026-05-15 | 105.42 | 4.20 | 10.48 | 11.33 | 8.38 | ABOVE_50_AND_200 |
| GC=F | 2026-05-15 | 4555.80 | -2.61 | -3.49 | -4.80 | -3.70 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-15 | 99.27 | 0.39 | 1.46 | 1.07 | 0.30 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.97 | XLE, XOP, USO |
| semis_ai | -3.93 | SMH, SOXX |
| high_beta | -4.40 | IWM, ARKK, HIBL |
| rates | 1.07 | TLT, TBF, TBT |
| dollar | 0.54 | UUP |
| equity_hedges | 2.49 | SH, PSQ, SQQQ |
| housing_rates | -3.55 | XHB, ITB |
| defensives | -1.35 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.65 | -26.67 | -32.47 | BELOW_50_AND_200 |
| USO | energy | 3.66 | 17.79 | 15.80 | ABOVE_50_AND_200 |
| TBT | rates | 3.11 | 6.07 | 6.26 | ABOVE_50_AND_200 |
| XOP | energy | 2.90 | 3.76 | 1.40 | ABOVE_50_AND_200 |
| XLE | energy | 2.36 | 5.05 | 2.34 | ABOVE_50_AND_200 |
| TBF | rates | 1.58 | 3.25 | 3.25 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.54 | -9.44 | -11.33 | BELOW_50_AND_200 |
| SH | equity_hedges | 1.27 | -4.66 | -6.61 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -6.80 | 18.82 | 25.40 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -4.06 | 25.27 | 26.80 | ABOVE_50_AND_200 |
| ARKK | high_beta | -3.97 | -3.15 | 1.90 | MIXED |
| SMH | semis_ai | -3.80 | 22.33 | 23.22 | ABOVE_50_AND_200 |
| XHB | housing_rates | -3.77 | -5.90 | -5.95 | BELOW_50_AND_200 |
| ITB | housing_rates | -3.34 | -7.65 | -7.67 | BELOW_50_AND_200 |
| IWM | high_beta | -2.41 | 2.83 | 5.22 | ABOVE_50_AND_200 |
| XLU | defensives | -2.29 | -5.35 | -4.57 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
