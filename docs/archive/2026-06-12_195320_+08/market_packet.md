# Market Packet — 2026-06-12T19:53:20.462238+08:00

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
| SPY | 2026-06-11 | 737.76 | 1.70 | -2.55 | -0.06 | 2.31 | 7.57 | 50.29 | 1.30 | 0.00 | -1.45 | ABOVE_50_AND_200 |
| QQQ | 2026-06-11 | 717.12 | 3.38 | -3.17 | 1.40 | 5.60 | 14.81 | 53.64 | 2.13 | 1.45 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-11 | 568.43 | -0.45 | -9.42 | -5.73 | -8.62 | -13.75 | 35.04 | 3.31 | -5.68 | -7.13 | BELOW_50_AND_200 |
| AMZN | 2026-06-11 | 241.51 | 1.47 | -4.84 | -9.15 | -5.00 | 3.89 | 36.77 | 3.01 | -9.09 | -10.54 | BELOW_50_ABOVE_200 |
| MU | 2026-06-11 | 995.87 | 11.66 | -0.01 | 29.91 | 49.67 | 163.89 | 62.11 | 7.56 | 29.97 | 28.51 | ABOVE_50_AND_200 |
| ORCL | 2026-06-11 | 184.10 | -8.53 | -22.10 | -1.46 | -0.06 | -10.67 | 42.07 | 7.64 | -1.40 | -2.86 | BELOW_50_AND_200 |
| SOFI | 2026-06-11 | 16.67 | 5.04 | -2.80 | 4.84 | -0.85 | -27.20 | 50.34 | 5.82 | 4.90 | 3.45 | BELOW_50_AND_200 |
| IAU | 2026-06-11 | 79.13 | 3.05 | -6.11 | -10.80 | -8.58 | -4.90 | 34.64 | 2.30 | -10.74 | -12.20 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-12 | 18.92 | -2.67 | -12.04 | 9.62 | 3.53 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-11 | 4.46 | -1.74 | -0.31 | 0.00 | 1.09 | ABOVE_50_AND_200 |
| CL=F | 2026-06-12 | 84.40 | -3.77 | -6.78 | -16.45 | -12.75 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-12 | 4229.50 | 3.40 | -2.48 | -9.97 | -7.81 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-12 | 99.72 | -0.14 | -0.35 | 1.26 | 0.84 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.91 | XLE, XOP, USO |
| semis_ai | 7.57 | SMH, SOXX |
| high_beta | 7.59 | IWM, ARKK, HIBL |
| rates | -0.84 | TLT, TBF, TBT |
| dollar | -0.36 | UUP |
| equity_hedges | -4.89 | SH, PSQ, SQQQ |
| housing_rates | 4.32 | XHB, ITB |
| defensives | -0.07 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 16.44 | 10.18 | 18.61 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 8.39 | 13.75 | 21.81 | ABOVE_50_AND_200 |
| SMH | semis_ai | 6.75 | 8.59 | 16.24 | ABOVE_50_AND_200 |
| ITB | housing_rates | 4.43 | 8.18 | 4.45 | MIXED |
| XHB | housing_rates | 4.20 | 7.86 | 4.54 | ABOVE_50_AND_200 |
| ARKK | high_beta | 3.36 | -3.52 | -0.72 | BELOW_50_AND_200 |
| IWM | high_beta | 2.96 | 2.77 | 4.70 | ABOVE_50_AND_200 |
| TLT | rates | 1.30 | 1.16 | 0.33 | MIXED |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -9.77 | -5.73 | -19.24 | BELOW_50_AND_200 |
| USO | energy | -4.07 | -10.72 | -4.92 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -3.24 | -1.33 | -5.67 | BELOW_50_AND_200 |
| XOP | energy | -2.73 | -3.73 | -3.89 | BELOW_50_ABOVE_200 |
| TBT | rates | -2.59 | -2.54 | -0.96 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.94 | -0.78 | -1.22 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -1.66 | 0.45 | -1.97 | BELOW_50_AND_200 |
| TBF | rates | -1.21 | -1.17 | -0.33 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
