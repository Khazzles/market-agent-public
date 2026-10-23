# Market Packet — 2026-10-23T08:09:50.286874+08:00

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
| SPY | 2026-10-21 | 773.09 | 0.53 | 0.45 | -0.04 | 0.62 | 6.44 | 53.48 | 0.95 | 0.00 | 2.94 | ABOVE_50_AND_200 |
| QQQ | 2026-10-21 | 725.20 | 1.05 | -0.51 | -2.98 | -0.21 | 7.20 | 45.98 | 1.63 | -2.94 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-21 | 697.52 | 0.47 | -5.43 | -5.31 | 5.45 | 10.26 | 47.35 | 3.85 | -5.27 | -2.33 | ABOVE_50_AND_200 |
| AMZN | 2026-10-21 | 262.37 | -0.10 | 3.26 | 2.90 | 2.36 | 7.88 | 57.10 | 2.62 | 2.94 | 5.88 | ABOVE_50_AND_200 |
| MU | 2026-10-21 | 913.67 | 1.96 | -0.05 | -16.65 | -7.27 | 25.70 | 40.45 | 5.34 | -16.61 | -13.67 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-21 | 129.13 | -1.53 | -1.09 | -13.45 | -10.35 | -18.90 | 41.07 | 5.23 | -13.41 | -10.47 | BELOW_50_AND_200 |
| SOFI | 2026-10-21 | 14.90 | 1.50 | 4.78 | -13.17 | -11.73 | -18.02 | 40.77 | 4.40 | -13.13 | -10.19 | BELOW_50_AND_200 |
| IAU | 2026-10-21 | 77.71 | 0.35 | 0.83 | -5.27 | -4.25 | -8.54 | 43.43 | 1.55 | -5.23 | -2.29 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-22 | 19.03 | 14.09 | 15.61 | 25.36 | 20.21 | ABOVE_50_AND_200 |
| ^TNX | 2026-10-22 | 4.95 | -3.75 | -2.67 | -3.15 | -0.47 | BELOW_50_ABOVE_200 |
| CL=F | 2026-10-22 | 99.29 | 2.20 | 1.35 | 7.74 | 7.36 | ABOVE_50_AND_200 |
| GC=F | 2026-10-22 | 4038.50 | -2.69 | -3.16 | -6.48 | -7.15 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-22 | 101.57 | -0.21 | -0.42 | 0.46 | 1.06 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.25 | XLE, XOP, USO |
| semis_ai | 1.98 | SMH, SOXX |
| high_beta | 2.56 | IWM, ARKK, HIBL |
| rates | -0.02 | TLT, TBF, TBT |
| dollar | 0.07 | UUP |
| equity_hedges | -1.60 | SH, PSQ, SQQQ |
| housing_rates | -0.75 | XHB, ITB |
| defensives | -0.22 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 5.04 | -19.27 | -12.06 | BELOW_50_AND_200 |
| ARKK | high_beta | 2.40 | -6.76 | -0.76 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 2.07 | -10.90 | -4.68 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.89 | -8.36 | -3.61 | BELOW_50_ABOVE_200 |
| XLU | defensives | 0.29 | 3.63 | 0.20 | MIXED |
| XLE | energy | 0.28 | 10.33 | 6.43 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.25 | -3.74 | -3.83 | BELOW_50_AND_200 |
| TLT | rates | 0.14 | -1.85 | -0.43 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.18 | 8.02 | -0.81 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -1.09 | 2.38 | -0.13 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.86 | -4.90 | -4.55 | BELOW_50_AND_200 |
| XLP | defensives | -0.73 | 5.29 | 3.41 | ABOVE_50_AND_200 |
| XHB | housing_rates | -0.64 | -3.83 | -4.22 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.53 | -0.40 | -0.73 | BELOW_50_AND_200 |
| XOP | energy | -0.51 | 9.59 | 5.21 | ABOVE_50_AND_200 |
| USO | energy | -0.50 | 10.91 | 10.30 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
