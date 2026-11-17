# Market Packet — 2026-11-17T12:10:04.355147+08:00

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
| SPY | 2026-11-16 | 739.95 | -1.91 | -1.69 | -3.05 | -3.13 | 1.06 | 40.43 | 1.54 | 0.00 | 3.72 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-16 | 661.75 | -2.67 | -2.59 | -6.77 | -7.67 | -3.03 | 37.76 | 2.50 | -3.72 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-16 | 626.41 | -2.38 | -2.33 | -11.69 | -7.88 | -0.62 | 43.87 | 3.62 | -8.64 | -4.92 | BELOW_50_AND_200 |
| AMZN | 2026-11-16 | 257.75 | -3.34 | -3.44 | 3.10 | 1.16 | 5.34 | 49.63 | 3.55 | 6.15 | 9.87 | ABOVE_50_AND_200 |
| MU | 2026-11-16 | 719.02 | -7.62 | -1.93 | -18.19 | -23.33 | -6.27 | 38.01 | 8.23 | -15.13 | -11.42 | BELOW_50_AND_200 |
| ORCL | 2026-11-16 | 119.09 | -4.99 | -0.58 | -7.13 | -12.35 | -22.61 | 42.64 | 6.71 | -4.08 | -0.36 | BELOW_50_AND_200 |
| SOFI | 2026-11-16 | 14.85 | -3.70 | -11.34 | 2.06 | -7.80 | -14.08 | 40.40 | 5.44 | 5.11 | 8.83 | BELOW_50_AND_200 |
| IAU | 2026-11-16 | 72.34 | -0.74 | -6.99 | -7.66 | -7.11 | -13.47 | 36.42 | 1.90 | -4.61 | -0.89 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-16 | 22.91 | 18.70 | 15.01 | 14.61 | 31.17 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-16 | 5.12 | -0.64 | 5.28 | 0.45 | 1.10 | ABOVE_50_AND_200 |
| CL=F | 2026-11-17 | 85.00 | -0.84 | -1.21 | -18.00 | -10.61 | BELOW_50_AND_200 |
| GC=F | 2026-11-17 | 3873.20 | 0.52 | -3.90 | -6.90 | -6.84 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-17 | 103.50 | -0.05 | 1.24 | 1.49 | 1.87 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.79 | XLE, XOP, USO |
| semis_ai | -5.26 | SMH, SOXX |
| high_beta | -5.83 | IWM, ARKK, HIBL |
| rates | -0.07 | TLT, TBF, TBT |
| dollar | 0.20 | UUP |
| equity_hedges | 4.23 | SH, PSQ, SQQQ |
| housing_rates | -0.83 | XHB, ITB |
| defensives | 0.23 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 8.10 | 17.99 | 20.83 | MIXED |
| PSQ | equity_hedges | 2.67 | 6.83 | 7.62 | ABOVE_50_AND_200 |
| SH | equity_hedges | 1.91 | 3.33 | 3.28 | MIXED |
| XLP | defensives | 0.27 | 5.68 | 7.92 | ABOVE_50_AND_200 |
| UUP | dollar | 0.20 | 2.21 | 2.53 | ABOVE_50_AND_200 |
| XLU | defensives | 0.18 | 4.53 | 5.26 | MIXED |
| TLT | rates | 0.00 | -0.84 | -0.96 | BELOW_50_AND_200 |
| TBF | rates | 0.00 | 0.85 | 0.88 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -11.23 | -27.05 | -34.84 | BELOW_50_AND_200 |
| SOXX | semis_ai | -5.41 | -14.13 | -17.54 | BELOW_50_AND_200 |
| SMH | semis_ai | -5.11 | -14.43 | -17.18 | BELOW_50_AND_200 |
| ARKK | high_beta | -4.59 | -12.37 | -15.24 | BELOW_50_AND_200 |
| USO | energy | -3.81 | -13.43 | -8.34 | BELOW_50_ABOVE_200 |
| XOP | energy | -2.61 | -10.18 | -5.29 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.96 | -6.67 | -1.98 | BELOW_50_ABOVE_200 |
| IWM | high_beta | -1.66 | 0.92 | -2.63 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
