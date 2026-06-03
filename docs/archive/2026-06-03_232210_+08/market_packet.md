# Market Packet — 2026-06-03T23:22:10.921298+08:00

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
| SPY | 2026-06-03 | 755.88 | -0.49 | 0.72 | 5.27 | 6.48 | 10.69 | 70.11 | 0.85 | 0.00 | -5.45 | ABOVE_50_AND_200 |
| QQQ | 2026-06-03 | 745.03 | -0.15 | 2.14 | 10.72 | 12.48 | 20.10 | 78.16 | 1.33 | 5.45 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-03 | 617.18 | 3.27 | -2.85 | 1.11 | -0.25 | -7.04 | 49.34 | 2.76 | -4.17 | -9.61 | BELOW_50_AND_200 |
| AMZN | 2026-06-03 | 250.62 | -2.30 | -7.81 | -7.88 | 0.43 | 8.06 | 39.82 | 2.74 | -13.15 | -18.60 | ABOVE_50_AND_200 |
| MU | 2026-06-03 | 1061.56 | -0.24 | 14.34 | 84.15 | 78.31 | 200.99 | 81.36 | 5.37 | 78.88 | 73.43 | ABOVE_50_AND_200 |
| ORCL | 2026-06-03 | 231.91 | -5.18 | 21.44 | 28.63 | 31.46 | 12.06 | 68.01 | 4.77 | 23.36 | 17.91 | ABOVE_50_AND_200 |
| SOFI | 2026-06-03 | 16.71 | -5.78 | 3.37 | 3.18 | -0.20 | -27.72 | 49.89 | 5.53 | -2.10 | -7.54 | BELOW_50_AND_200 |
| IAU | 2026-06-03 | 83.59 | -0.98 | -0.16 | -1.62 | -3.98 | 1.10 | 38.76 | 1.80 | -6.89 | -12.34 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-03 | 16.08 | 1.97 | -1.29 | -7.48 | -16.74 | BELOW_50_AND_200 |
| ^TNX | 2026-06-03 | 4.49 | 0.67 | 0.09 | 0.88 | 2.00 | ABOVE_50_AND_200 |
| CL=F | 2026-06-03 | 95.67 | 2.04 | 7.88 | -10.10 | -2.22 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-03 | 4478.10 | -0.24 | 0.69 | -0.92 | -3.23 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-06-03 | 99.47 | 0.25 | 0.26 | 1.01 | 0.58 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.79 | XLE, XOP, USO |
| semis_ai | 1.14 | SMH, SOXX |
| high_beta | -1.54 | IWM, ARKK, HIBL |
| rates | 0.25 | TLT, TBF, TBT |
| dollar | 0.29 | UUP |
| equity_hedges | 0.38 | SH, PSQ, SQQQ |
| housing_rates | -0.38 | XHB, ITB |
| defensives | 0.85 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XOP | energy | 1.90 | -4.95 | -0.01 | BELOW_50_ABOVE_200 |
| USO | energy | 1.78 | -5.35 | 4.26 | ABOVE_50_AND_200 |
| XLE | energy | 1.69 | -0.76 | 1.17 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.48 | 32.87 | 35.45 | ABOVE_50_AND_200 |
| XLU | defensives | 0.93 | -4.45 | -2.65 | BELOW_50_AND_200 |
| SMH | semis_ai | 0.79 | 25.74 | 27.74 | ABOVE_50_AND_200 |
| XLP | defensives | 0.77 | -1.29 | -0.75 | BELOW_50_ABOVE_200 |
| TBT | rates | 0.73 | -1.10 | 0.59 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -2.05 | 0.06 | 4.40 | ABOVE_50_AND_200 |
| HIBL | high_beta | -1.43 | 39.73 | 45.47 | ABOVE_50_AND_200 |
| IWM | high_beta | -1.15 | 3.76 | 5.74 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.55 | 1.59 | -0.36 | BELOW_50_AND_200 |
| TLT | rates | -0.41 | 0.40 | -0.62 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.20 | 2.67 | 1.73 | MIXED |
| PSQ | equity_hedges | 0.16 | -9.46 | -11.46 | BELOW_50_AND_200 |
| UUP | dollar | 0.29 | 1.31 | 0.91 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
