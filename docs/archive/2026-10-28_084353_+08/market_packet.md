# Market Packet — 2026-10-28T08:43:53.683300+08:00

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
| SPY | 2026-10-26 | 765.37 | 0.71 | -0.14 | -0.78 | -0.29 | 5.22 | 47.32 | 0.94 | 0.00 | 3.56 | BELOW_50_ABOVE_200 |
| QQQ | 2026-10-26 | 712.20 | 1.11 | -0.86 | -4.34 | -1.82 | 5.08 | 41.73 | 1.60 | -3.56 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-26 | 630.56 | -1.88 | -10.61 | -16.11 | -5.13 | -0.30 | 33.65 | 3.90 | -15.34 | -11.77 | BELOW_50_AND_200 |
| AMZN | 2026-10-26 | 249.09 | 0.44 | -5.09 | -0.23 | -2.46 | 2.38 | 44.35 | 2.57 | 0.54 | 4.11 | BELOW_50_ABOVE_200 |
| MU | 2026-10-26 | 903.70 | 2.98 | -0.13 | -16.50 | -7.91 | 22.95 | 42.32 | 5.10 | -15.73 | -12.16 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-26 | 126.06 | -0.08 | -2.72 | -8.05 | -11.47 | -20.33 | 39.05 | 5.06 | -7.28 | -3.71 | BELOW_50_AND_200 |
| SOFI | 2026-10-26 | 14.46 | -1.06 | 1.12 | -12.79 | -13.23 | -19.60 | 36.91 | 5.12 | -12.01 | -8.45 | BELOW_50_AND_200 |
| IAU | 2026-10-26 | 75.42 | 0.36 | -3.12 | -6.50 | -6.59 | -11.10 | 35.73 | 1.52 | -5.72 | -2.16 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-27 | 17.52 | -4.73 | 1.21 | 9.02 | 9.28 | MIXED |
| ^TNX | 2026-10-27 | 4.99 | 0.14 | -2.42 | -4.71 | -0.03 | BELOW_50_ABOVE_200 |
| CL=F | 2026-10-27 | 100.61 | -1.13 | -1.16 | 8.65 | 7.45 | ABOVE_50_AND_200 |
| GC=F | 2026-10-27 | 4076.00 | 0.93 | -1.61 | -2.22 | -5.78 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-27 | 102.33 | 0.37 | 0.59 | 1.12 | 1.68 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.02 | XLE, XOP, USO |
| semis_ai | 2.79 | SMH, SOXX |
| high_beta | 1.72 | IWM, ARKK, HIBL |
| rates | -0.28 | TLT, TBF, TBT |
| dollar | 0.17 | UUP |
| equity_hedges | -1.68 | SH, PSQ, SQQQ |
| housing_rates | -0.60 | XHB, ITB |
| defensives | -0.18 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.88 | -28.88 | -21.50 | BELOW_50_AND_200 |
| SOXX | semis_ai | 2.85 | -14.12 | -7.45 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 2.74 | -10.71 | -5.67 | BELOW_50_ABOVE_200 |
| XOP | energy | 1.57 | 12.87 | 7.56 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.45 | -1.77 | -3.10 | BELOW_50_AND_200 |
| XLE | energy | 0.45 | 12.25 | 7.98 | ABOVE_50_AND_200 |
| TLT | rates | 0.42 | 2.98 | 1.41 | MIXED |
| UUP | dollar | 0.17 | 1.36 | 1.78 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -3.28 | 13.72 | 3.90 | MIXED |
| USO | energy | -1.95 | 12.07 | 12.88 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -1.07 | 4.91 | 1.59 | MIXED |
| TBT | rates | -0.85 | -6.28 | -3.48 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -0.77 | 0.49 | -0.37 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.70 | 1.31 | 0.29 | MIXED |
| XHB | housing_rates | -0.44 | -0.38 | -1.24 | BELOW_50_AND_200 |
| TBF | rates | -0.39 | -2.97 | -1.65 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
