# Market Packet — 2026-08-22T05:58:17.110309+08:00

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
| SPY | 2026-08-21 | 765.72 | 0.41 | -1.37 | 3.73 | 1.86 | 8.22 | 54.23 | 0.91 | 0.00 | 0.63 | ABOVE_50_AND_200 |
| QQQ | 2026-08-21 | 713.44 | 0.35 | -2.41 | 3.10 | -0.00 | 9.29 | 50.15 | 1.59 | -0.63 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-21 | 549.90 | 0.75 | -6.77 | -9.27 | -7.27 | -11.89 | 38.66 | 3.68 | -13.00 | -12.38 | BELOW_50_AND_200 |
| AMZN | 2026-08-21 | 258.63 | -0.57 | -1.53 | 10.69 | 3.56 | 8.52 | 49.74 | 2.89 | 6.96 | 7.58 | ABOVE_50_AND_200 |
| MU | 2026-08-21 | 966.78 | -0.77 | -0.50 | -2.37 | 0.23 | 69.28 | 54.34 | 6.90 | -6.10 | -5.47 | ABOVE_50_AND_200 |
| ORCL | 2026-08-21 | 146.47 | 3.10 | -2.69 | 22.02 | 0.72 | -15.37 | 52.71 | 4.81 | 18.29 | 18.91 | MIXED |
| SOFI | 2026-08-21 | 18.91 | 5.52 | 3.39 | 13.57 | 7.00 | -7.82 | 58.18 | 4.56 | 9.84 | 10.47 | MIXED |
| IAU | 2026-08-21 | 86.79 | 1.95 | 5.48 | 13.97 | 10.56 | 2.46 | 71.33 | 1.78 | 10.24 | 10.87 | ABOVE_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-21 | 15.13 | -5.50 | 6.18 | -19.09 | -9.74 | BELOW_50_AND_200 |
| ^TNX | 2026-08-21 | 4.74 | 0.89 | 0.89 | 0.74 | 3.48 | ABOVE_50_AND_200 |
| CL=F | 2026-08-21 | 86.64 | -1.35 | 5.15 | -6.02 | 9.55 | ABOVE_50_AND_200 |
| GC=F | 2026-08-21 | 4661.60 | 3.22 | 6.42 | 15.20 | 11.61 | ABOVE_50_AND_200 |
| DX-Y.NYB | 2026-08-21 | 98.84 | -0.06 | -0.83 | -2.55 | -1.64 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.34 | XLE, XOP, USO |
| semis_ai | -0.42 | SMH, SOXX |
| high_beta | 3.15 | IWM, ARKK, HIBL |
| rates | 0.35 | TLT, TBF, TBT |
| dollar | -0.04 | UUP |
| equity_hedges | -0.54 | SH, PSQ, SQQQ |
| housing_rates | 0.80 | XHB, ITB |
| defensives | -0.75 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 5.14 | 8.70 | -2.05 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 3.53 | 16.77 | 10.21 | ABOVE_50_AND_200 |
| XOP | energy | 1.11 | 7.90 | 13.27 | ABOVE_50_AND_200 |
| TBT | rates | 0.97 | 2.53 | 4.88 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.83 | -0.18 | -2.29 | BELOW_50_AND_200 |
| XLP | defensives | 0.79 | 3.34 | 1.44 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.78 | 3.12 | -1.09 | BELOW_50_AND_200 |
| IWM | high_beta | 0.77 | 2.69 | 1.11 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLU | defensives | -2.28 | -7.40 | -4.58 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -0.89 | -9.82 | -1.98 | BELOW_50_AND_200 |
| SOXX | semis_ai | -0.44 | -5.66 | -6.93 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.40 | -3.19 | -1.52 | BELOW_50_AND_200 |
| SMH | semis_ai | -0.40 | -3.40 | -4.90 | BELOW_50_ABOVE_200 |
| TLT | rates | -0.35 | -1.35 | -2.52 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.35 | -2.81 | -0.05 | BELOW_50_AND_200 |
| XLE | energy | -0.17 | 7.17 | 10.67 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
