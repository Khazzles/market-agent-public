# Market Packet — 2026-06-09T18:43:43.881925+08:00

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
| SPY | 2026-06-08 | 739.22 | 0.23 | -2.55 | 1.04 | 3.33 | 8.00 | 50.76 | 1.03 | 0.00 | -2.00 | ABOVE_50_AND_200 |
| QQQ | 2026-06-08 | 716.07 | 1.56 | -3.59 | 3.04 | 6.77 | 15.02 | 53.63 | 1.72 | 2.00 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-08 | 585.39 | -1.28 | -2.51 | -5.09 | -5.62 | -11.52 | 39.52 | 3.28 | -6.14 | -8.13 | BELOW_50_AND_200 |
| AMZN | 2026-06-08 | 245.22 | -0.33 | -6.14 | -9.57 | -2.66 | 5.59 | 37.27 | 2.91 | -10.61 | -12.61 | BELOW_50_ABOVE_200 |
| MU | 2026-06-08 | 949.28 | 9.87 | -8.33 | 46.80 | 50.86 | 160.07 | 60.84 | 7.18 | 45.76 | 43.76 | ABOVE_50_AND_200 |
| ORCL | 2026-06-08 | 211.82 | -0.87 | -14.64 | 8.85 | 17.09 | 2.50 | 54.67 | 5.82 | 7.81 | 5.81 | ABOVE_50_AND_200 |
| SOFI | 2026-06-08 | 16.50 | 2.93 | -11.19 | 3.12 | -1.54 | -28.34 | 48.69 | 5.66 | 2.08 | 0.08 | BELOW_50_AND_200 |
| IAU | 2026-06-08 | 81.38 | 0.20 | -3.43 | -8.00 | -6.45 | -1.92 | 33.84 | 1.89 | -9.05 | -11.04 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-09 | 18.07 | -4.49 | 14.58 | -1.69 | -2.33 | BELOW_50_AND_200 |
| ^TNX | 2026-06-08 | 4.55 | 0.35 | 1.72 | 3.64 | 3.32 | ABOVE_50_AND_200 |
| CL=F | 2026-06-09 | 89.28 | -2.21 | -4.78 | -6.43 | -8.52 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-09 | 4358.20 | 0.51 | -2.92 | -7.67 | -5.68 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-09 | 99.77 | -0.28 | 0.55 | 1.97 | 0.87 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.40 | XLE, XOP, USO |
| semis_ai | 5.43 | SMH, SOXX |
| high_beta | 2.80 | IWM, ARKK, HIBL |
| rates | 0.40 | TLT, TBF, TBT |
| dollar | 0.04 | UUP |
| equity_hedges | -2.07 | SH, PSQ, SQQQ |
| housing_rates | -0.29 | XHB, ITB |
| defensives | -1.16 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | 5.87 | 16.06 | 22.29 | ABOVE_50_AND_200 |
| HIBL | high_beta | 5.66 | 12.13 | 21.07 | ABOVE_50_AND_200 |
| SMH | semis_ai | 5.00 | 10.75 | 16.99 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.87 | -2.63 | 0.56 | MIXED |
| USO | energy | 1.60 | 0.13 | -0.06 | BELOW_50_ABOVE_200 |
| XOP | energy | 1.45 | 1.40 | -1.65 | BELOW_50_ABOVE_200 |
| XLE | energy | 1.14 | 4.25 | 0.42 | ABOVE_50_AND_200 |
| TBT | rates | 1.14 | 2.33 | 2.29 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -4.47 | -9.77 | -22.34 | BELOW_50_AND_200 |
| XLU | defensives | -1.87 | -3.55 | -4.19 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -1.51 | -2.83 | -6.83 | BELOW_50_AND_200 |
| TLT | rates | -0.52 | -1.20 | -1.33 | BELOW_50_AND_200 |
| XLP | defensives | -0.44 | -1.08 | -0.12 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -0.38 | -0.41 | -0.67 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.24 | -0.62 | -3.02 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.21 | 0.61 | 0.68 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
