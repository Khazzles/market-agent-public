# Market Packet — 2026-10-29T09:13:27.378465+08:00

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
| SPY | 2026-10-27 | 769.66 | 0.56 | 0.08 | 0.53 | 0.28 | 5.76 | 51.10 | 0.90 | 0.00 | 2.60 | ABOVE_50_AND_200 |
| QQQ | 2026-10-27 | 721.25 | 1.27 | 0.50 | -2.07 | -0.55 | 6.34 | 47.16 | 1.53 | -2.60 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-27 | 620.19 | -1.64 | -10.67 | -13.34 | -6.83 | -1.91 | 31.92 | 3.86 | -13.86 | -11.26 | BELOW_50_AND_200 |
| AMZN | 2026-10-27 | 253.10 | 1.61 | -3.63 | 2.82 | -0.83 | 4.01 | 48.58 | 2.45 | 2.29 | 4.90 | BELOW_50_ABOVE_200 |
| MU | 2026-10-27 | 928.76 | 2.77 | 3.65 | -11.88 | -5.20 | 25.86 | 46.05 | 5.08 | -12.41 | -9.81 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-27 | 130.53 | 3.55 | -0.47 | -1.56 | -8.13 | -17.33 | 44.59 | 5.64 | -2.09 | 0.51 | BELOW_50_AND_200 |
| SOFI | 2026-10-27 | 16.40 | 13.42 | 11.72 | 2.95 | -1.36 | -8.53 | 57.43 | 4.56 | 2.42 | 5.03 | BELOW_50_AND_200 |
| IAU | 2026-10-27 | 76.33 | 1.21 | -1.43 | -1.51 | -5.31 | -9.98 | 41.14 | 1.48 | -2.04 | 0.56 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-28 | 16.91 | -3.48 | 1.38 | 5.42 | 5.21 | MIXED |
| ^TNX | 2026-10-28 | 5.04 | 1.04 | -1.96 | -4.00 | 0.87 | ABOVE_50_AND_200 |
| CL=F | 2026-10-28 | 101.93 | 2.03 | 4.92 | 14.04 | 8.48 | ABOVE_50_AND_200 |
| GC=F | 2026-10-28 | 4054.90 | -0.48 | -2.29 | -2.99 | -6.11 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-28 | 102.25 | -0.07 | 0.46 | 0.87 | 1.55 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.94 | XLE, XOP, USO |
| semis_ai | 3.47 | SMH, SOXX |
| high_beta | 4.64 | IWM, ARKK, HIBL |
| rates | 0.08 | TLT, TBF, TBT |
| dollar | 0.38 | UUP |
| equity_hedges | -1.88 | SH, PSQ, SQQQ |
| housing_rates | 0.88 | XHB, ITB |
| defensives | -0.11 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 9.16 | -18.10 | -13.86 | BELOW_50_AND_200 |
| SOXX | semis_ai | 3.91 | -8.87 | -3.65 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 3.59 | -5.01 | -1.59 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 3.02 | -7.00 | -2.70 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 1.24 | 1.91 | 0.16 | MIXED |
| IWM | high_beta | 1.15 | 0.06 | -1.82 | BELOW_50_ABOVE_200 |
| XLU | defensives | 0.71 | 9.17 | 2.50 | MIXED |
| ITB | housing_rates | 0.53 | 1.80 | 0.33 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.78 | 6.03 | -0.05 | BELOW_50_AND_200 |
| XOP | energy | -2.37 | 11.03 | 4.83 | ABOVE_50_AND_200 |
| XLE | energy | -2.05 | 9.84 | 5.58 | ABOVE_50_AND_200 |
| USO | energy | -1.41 | 9.25 | 10.78 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.28 | 2.45 | 0.28 | MIXED |
| XLP | defensives | -0.92 | 5.92 | 3.18 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.59 | -0.06 | -0.30 | BELOW_50_AND_200 |
| TLT | rates | -0.06 | 3.83 | 1.34 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
