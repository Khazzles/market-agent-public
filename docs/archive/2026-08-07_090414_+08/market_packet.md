# Market Packet — 2026-08-07T09:04:14.005811+08:00

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
| SPY | 2026-08-06 | 768.56 | -0.16 | 3.62 | 3.11 | 2.92 | 9.41 | 63.69 | 1.19 | 0.00 | 2.66 | ABOVE_50_AND_200 |
| QQQ | 2026-08-06 | 714.65 | -0.37 | 4.55 | 0.45 | -0.01 | 10.41 | 54.32 | 2.15 | -2.66 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-08-06 | 589.90 | 0.19 | 9.44 | -2.19 | -1.78 | -6.66 | 47.00 | 4.07 | -5.30 | -2.64 | BELOW_50_AND_200 |
| AMZN | 2026-08-06 | 272.26 | -0.14 | 15.61 | 11.76 | 10.02 | 15.24 | 63.20 | 3.52 | 8.65 | 11.30 | ABOVE_50_AND_200 |
| MU | 2026-08-06 | 881.47 | -1.31 | 0.78 | -7.10 | -9.31 | 65.79 | 47.93 | 9.64 | -10.20 | -7.55 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-06 | 143.47 | -0.64 | 12.47 | 2.12 | -10.98 | -20.28 | 53.90 | 5.44 | -0.99 | 1.67 | BELOW_50_AND_200 |
| SOFI | 2026-08-06 | 18.10 | -0.82 | 9.90 | 2.09 | 4.06 | -14.34 | 54.84 | 5.04 | -1.02 | 1.64 | MIXED |
| IAU | 2026-08-06 | 79.87 | 0.03 | 3.32 | 4.08 | 1.88 | -5.30 | 60.23 | 1.87 | 0.97 | 3.63 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-06 | 15.15 | -4.17 | -11.35 | -10.36 | -12.44 | BELOW_50_AND_200 |
| ^TNX | 2026-08-06 | 4.67 | 1.15 | 0.15 | 2.21 | 2.95 | ABOVE_50_AND_200 |
| CL=F | 2026-08-06 | 78.06 | 3.78 | -6.62 | 6.18 | -3.27 | BELOW_50_ABOVE_200 |
| GC=F | 2026-08-06 | 4292.10 | 1.09 | 4.68 | 5.43 | 2.87 | MIXED |
| DX-Y.NYB | 2026-08-06 | 99.98 | 0.29 | -0.03 | -1.06 | -0.49 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.03 | XLE, XOP, USO |
| semis_ai | 0.33 | SMH, SOXX |
| high_beta | -2.37 | IWM, ARKK, HIBL |
| rates | 0.52 | TLT, TBF, TBT |
| dollar | 0.36 | UUP |
| equity_hedges | 0.54 | SH, PSQ, SQQQ |
| housing_rates | -2.13 | XHB, ITB |
| defensives | -0.45 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 3.47 | 5.94 | -2.11 | BELOW_50_ABOVE_200 |
| TBT | rates | 1.49 | 4.67 | 5.24 | ABOVE_50_AND_200 |
| XLE | energy | 1.48 | 4.60 | 2.76 | ABOVE_50_AND_200 |
| XOP | energy | 1.13 | 3.12 | 1.69 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.07 | -3.44 | -3.90 | BELOW_50_AND_200 |
| TBF | rates | 0.64 | 2.26 | 2.52 | ABOVE_50_AND_200 |
| UUP | dollar | 0.36 | -0.60 | -0.12 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | 0.35 | -0.50 | -0.54 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -6.00 | -3.07 | -8.42 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | -2.39 | 2.67 | 1.07 | MIXED |
| XHB | housing_rates | -1.87 | 2.61 | 0.73 | ABOVE_50_AND_200 |
| XLU | defensives | -0.64 | -4.37 | -3.37 | BELOW_50_AND_200 |
| ARKK | high_beta | -0.59 | -5.53 | -2.17 | BELOW_50_AND_200 |
| TLT | rates | -0.58 | -2.18 | -2.75 | BELOW_50_AND_200 |
| IWM | high_beta | -0.51 | 1.63 | 1.57 | ABOVE_50_AND_200 |
| XLP | defensives | -0.26 | 0.85 | 0.97 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
