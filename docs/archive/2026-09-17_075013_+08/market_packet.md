# Market Packet — 2026-09-17T07:50:13.661172+08:00

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
| SPY | 2026-09-16 | 754.05 | -0.44 | -1.10 | -2.41 | -0.68 | 5.39 | 41.76 | 0.87 | 0.00 | 1.04 | BELOW_50_ABOVE_200 |
| QQQ | 2026-09-16 | 704.72 | 0.03 | -1.62 | -3.45 | -0.73 | 6.52 | 44.12 | 1.30 | -1.04 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-16 | 673.31 | 0.46 | 3.00 | 18.34 | 11.27 | 7.93 | 72.24 | 3.11 | 20.75 | 21.78 | ABOVE_50_AND_200 |
| AMZN | 2026-09-16 | 245.96 | -0.99 | -2.55 | -5.87 | -3.75 | 2.44 | 39.45 | 2.49 | -3.46 | -2.43 | BELOW_50_ABOVE_200 |
| MU | 2026-09-16 | 926.55 | -0.11 | -9.85 | -8.42 | 0.04 | 46.48 | 46.77 | 5.32 | -6.01 | -4.98 | ABOVE_50_AND_200 |
| ORCL | 2026-09-16 | 143.16 | 2.00 | -11.43 | -2.38 | 1.72 | -14.16 | 45.71 | 5.34 | 0.03 | 1.07 | MIXED |
| SOFI | 2026-09-16 | 16.84 | -1.35 | -2.83 | -8.03 | -5.23 | -14.26 | 42.21 | 4.43 | -5.62 | -4.58 | BELOW_50_AND_200 |
| IAU | 2026-09-16 | 80.32 | -0.57 | -2.87 | -3.36 | -0.05 | -5.79 | 43.17 | 1.99 | -0.95 | 0.09 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-16 | 17.71 | 2.97 | 7.59 | 11.81 | 9.41 | MIXED |
| ^TNX | 2026-09-16 | 5.01 | 0.20 | 3.49 | 5.97 | 6.48 | ABOVE_50_AND_200 |
| CL=F | 2026-09-16 | 101.95 | -3.67 | 6.14 | 20.65 | 19.58 | ABOVE_50_AND_200 |
| GC=F | 2026-09-16 | 4309.10 | -0.55 | -3.40 | -3.68 | -0.06 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-09-16 | 100.34 | 0.69 | 1.59 | 0.70 | 0.36 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -3.45 | XLE, XOP, USO |
| semis_ai | 0.64 | SMH, SOXX |
| high_beta | -0.18 | IWM, ARKK, HIBL |
| rates | -0.13 | TLT, TBF, TBT |
| dollar | 0.64 | UUP |
| equity_hedges | 0.14 | SH, PSQ, SQQQ |
| housing_rates | -1.05 | XHB, ITB |
| defensives | -0.24 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | 0.64 | -10.21 | -4.82 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.64 | 1.07 | 0.69 | ABOVE_50_AND_200 |
| SMH | semis_ai | 0.64 | -8.17 | -3.63 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | 0.46 | 2.96 | 1.20 | MIXED |
| HIBL | high_beta | 0.27 | -19.58 | -10.05 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.21 | -0.58 | -2.23 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.00 | 3.95 | 1.07 | MIXED |
| XLU | defensives | 0.00 | -6.47 | -6.03 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | -3.96 | 4.61 | 7.03 | ABOVE_50_AND_200 |
| USO | energy | -3.52 | 19.86 | 19.43 | ABOVE_50_AND_200 |
| XLE | energy | -2.88 | 2.32 | 5.30 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.12 | -9.93 | -8.22 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.98 | -10.53 | -8.40 | BELOW_50_AND_200 |
| XLP | defensives | -0.48 | -1.59 | -1.90 | BELOW_50_AND_200 |
| IWM | high_beta | -0.43 | -6.62 | -3.94 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.37 | 1.75 | 3.75 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
