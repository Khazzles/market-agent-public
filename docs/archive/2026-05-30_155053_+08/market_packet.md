# Market Packet — 2026-05-30T15:50:53.115140+08:00

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
| SPY | 2026-05-29 | 756.48 | 0.25 | 1.85 | 6.31 | 7.51 | 11.06 | 74.11 | 0.91 | 0.00 | -5.29 | ABOVE_50_AND_200 |
| QQQ | 2026-05-29 | 738.31 | 0.37 | 3.33 | 11.60 | 13.08 | 19.50 | 77.19 | 1.40 | 5.29 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-29 | 632.51 | -0.44 | 4.14 | -5.47 | 2.26 | -5.11 | 55.36 | 2.45 | -11.78 | -17.07 | MIXED |
| AMZN | 2026-05-29 | 270.64 | -1.23 | 0.81 | 2.89 | 9.72 | 16.90 | 59.70 | 2.45 | -3.42 | -8.71 | ABOVE_50_AND_200 |
| MU | 2026-05-29 | 971.00 | 5.14 | 27.41 | 87.29 | 74.15 | 186.65 | 78.01 | 5.77 | 80.98 | 75.69 | ABOVE_50_AND_200 |
| ORCL | 2026-05-29 | 225.78 | 10.84 | 18.98 | 37.81 | 31.95 | 9.06 | 75.09 | 4.25 | 31.50 | 26.21 | ABOVE_50_AND_200 |
| SOFI | 2026-05-29 | 18.22 | 7.37 | 16.42 | 17.36 | 9.04 | -21.51 | 64.04 | 4.84 | 11.05 | 5.76 | MIXED |
| IAU | 2026-05-29 | 85.49 | 1.06 | 0.07 | -0.07 | -1.86 | 3.79 | 45.34 | 1.85 | -6.38 | -11.67 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-29 | 15.32 | -2.67 | -8.26 | -9.30 | -23.21 | BELOW_50_AND_200 |
| ^TNX | 2026-05-29 | 4.45 | -0.04 | -2.90 | 0.79 | 1.46 | ABOVE_50_AND_200 |
| CL=F | 2026-05-29 | 87.36 | -1.73 | -9.33 | -18.26 | -10.73 | BELOW_50_ABOVE_200 |
| GC=F | 2026-05-29 | 4560.50 | 1.36 | 0.46 | 0.34 | -1.51 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-29 | 98.91 | -0.11 | -0.28 | -0.01 | 0.01 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.01 | XLE, XOP, USO |
| semis_ai | -0.11 | SMH, SOXX |
| high_beta | 1.55 | IWM, ARKK, HIBL |
| rates | 0.03 | TLT, TBF, TBT |
| dollar | -0.14 | UUP |
| equity_hedges | -0.52 | SH, PSQ, SQQQ |
| housing_rates | -0.13 | XHB, ITB |
| defensives | -1.14 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.04 | 44.19 | 45.23 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.16 | 11.45 | 10.14 | ABOVE_50_AND_200 |
| TBT | rates | 0.14 | -0.31 | 0.43 | ABOVE_50_AND_200 |
| TLT | rates | 0.02 | 0.07 | -0.16 | BELOW_50_AND_200 |
| SOXX | semis_ai | -0.07 | 26.46 | 30.04 | ABOVE_50_AND_200 |
| TBF | rates | -0.08 | -0.04 | 0.33 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.13 | -2.16 | 0.18 | MIXED |
| XHB | housing_rates | -0.14 | -1.36 | 0.63 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLP | defensives | -1.80 | -0.01 | -0.16 | BELOW_50_ABOVE_200 |
| USO | energy | -1.29 | -14.30 | -2.75 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.16 | -4.64 | -3.51 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -1.01 | -28.26 | -34.23 | BELOW_50_AND_200 |
| XOP | energy | -0.59 | -7.73 | -4.90 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -0.55 | 6.74 | 7.55 | ABOVE_50_AND_200 |
| XLU | defensives | -0.47 | -2.76 | -2.60 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.39 | -10.16 | -11.97 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
