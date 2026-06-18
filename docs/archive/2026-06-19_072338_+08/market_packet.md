# Market Packet — 2026-06-19T07:23:38.757420+08:00

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
| SPY | 2026-06-18 | 746.74 | 0.78 | 1.22 | 1.77 | 2.34 | 8.48 | 54.11 | 1.30 | 0.00 | -3.80 | ABOVE_50_AND_200 |
| QQQ | 2026-06-18 | 740.62 | 2.51 | 3.28 | 5.57 | 6.84 | 17.81 | 59.09 | 2.14 | 3.80 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-18 | 577.22 | 1.70 | 1.55 | -4.21 | -7.18 | -11.86 | 42.82 | 3.48 | -5.99 | -9.79 | BELOW_50_AND_200 |
| AMZN | 2026-06-18 | 244.39 | 2.90 | 1.19 | -5.76 | -4.94 | 4.98 | 44.03 | 3.14 | -7.54 | -11.34 | BELOW_50_ABOVE_200 |
| MU | 2026-06-18 | 1133.99 | 8.70 | 13.87 | 62.29 | 54.75 | 182.97 | 66.39 | 7.04 | 60.52 | 56.72 | ABOVE_50_AND_200 |
| ORCL | 2026-06-18 | 184.29 | 0.41 | 0.10 | 1.56 | -2.17 | -10.08 | 43.08 | 6.74 | -0.21 | -4.01 | BELOW_50_AND_200 |
| SOFI | 2026-06-18 | 17.91 | 2.81 | 7.44 | 17.60 | 5.72 | -21.09 | 58.00 | 5.33 | 15.82 | 12.02 | MIXED |
| IAU | 2026-06-18 | 79.33 | -0.39 | 0.25 | -5.92 | -7.45 | -5.10 | 38.10 | 2.31 | -7.69 | -11.49 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-18 | 16.40 | -11.06 | -15.64 | -5.96 | -7.81 | BELOW_50_AND_200 |
| ^TNX | 2026-06-18 | 4.45 | -0.80 | -2.22 | -0.22 | 0.68 | ABOVE_50_AND_200 |
| CL=F | 2026-06-18 | 75.32 | -1.91 | -14.13 | -30.11 | -20.12 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-18 | 4217.70 | -3.24 | 3.11 | -6.40 | -7.47 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-18 | 100.81 | 0.72 | 0.96 | 1.52 | 1.91 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.87 | XLE, XOP, USO |
| semis_ai | 6.19 | SMH, SOXX |
| high_beta | 3.92 | IWM, ARKK, HIBL |
| rates | -0.24 | TLT, TBF, TBT |
| dollar | 0.43 | UUP |
| equity_hedges | -3.43 | SH, PSQ, SQQQ |
| housing_rates | 3.53 | XHB, ITB |
| defensives | 0.11 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 7.61 | 48.12 | 28.92 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 6.62 | 28.73 | 25.84 | ABOVE_50_AND_200 |
| SMH | semis_ai | 5.76 | 21.31 | 20.51 | ABOVE_50_AND_200 |
| ITB | housing_rates | 3.61 | 15.10 | 5.33 | MIXED |
| XHB | housing_rates | 3.46 | 17.06 | 6.66 | ABOVE_50_AND_200 |
| ARKK | high_beta | 2.17 | 8.60 | 4.18 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.97 | 8.27 | 5.06 | ABOVE_50_AND_200 |
| XLU | defensives | 0.67 | 0.95 | -0.87 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -7.01 | -17.17 | -21.58 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -2.33 | -5.30 | -6.64 | BELOW_50_AND_200 |
| XLE | energy | -1.65 | -12.27 | -6.39 | BELOW_50_ABOVE_200 |
| XOP | energy | -1.53 | -14.11 | -8.79 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.95 | -1.63 | -2.16 | BELOW_50_AND_200 |
| TBT | rates | -0.77 | -8.61 | -2.63 | BELOW_50_ABOVE_200 |
| XLP | defensives | -0.45 | -3.24 | -0.40 | BELOW_50_ABOVE_200 |
| TBF | rates | -0.45 | -4.34 | -1.19 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
