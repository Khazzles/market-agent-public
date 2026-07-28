# Market Packet — 2026-07-29T06:40:57.770818+08:00

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
| SPY | 2026-07-28 | 740.86 | 0.24 | -0.99 | 1.63 | -0.54 | 5.95 | 47.10 | 1.10 | 0.00 | 6.02 | BELOW_50_ABOVE_200 |
| QQQ | 2026-07-28 | 675.49 | -0.97 | -4.72 | -4.39 | -5.76 | 4.91 | 36.45 | 2.12 | -6.02 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-28 | 593.41 | -0.08 | -7.83 | 7.84 | -1.93 | -6.82 | 43.40 | 3.93 | 6.22 | 12.24 | BELOW_50_AND_200 |
| AMZN | 2026-07-28 | 230.86 | -0.23 | -6.74 | -0.79 | -6.81 | -1.62 | 36.54 | 2.99 | -2.41 | 3.61 | BELOW_50_AND_200 |
| MU | 2026-07-28 | 820.53 | -8.85 | -15.48 | -27.54 | -14.37 | 61.28 | 40.29 | 10.13 | -29.16 | -23.14 | BELOW_50_ABOVE_200 |
| ORCL | 2026-07-28 | 119.96 | 0.05 | -5.58 | -19.24 | -28.86 | -35.41 | 32.74 | 6.47 | -20.86 | -14.84 | BELOW_50_AND_200 |
| SOFI | 2026-07-28 | 16.74 | -0.83 | -5.10 | -6.38 | -2.45 | -22.07 | 44.10 | 5.05 | -8.00 | -1.98 | BELOW_50_AND_200 |
| IAU | 2026-07-28 | 75.70 | -1.41 | -1.46 | -1.12 | -4.75 | -10.27 | 43.15 | 1.83 | -2.75 | 3.27 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-28 | 18.21 | -2.46 | -2.36 | -3.60 | 4.86 | MIXED |
| ^TNX | 2026-07-28 | 4.60 | -0.80 | 0.13 | 4.83 | 1.84 | ABOVE_50_AND_200 |
| CL=F | 2026-07-28 | 82.60 | -0.01 | -2.72 | 19.31 | -1.27 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-28 | 4019.90 | -1.34 | -1.26 | -1.44 | -4.95 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-28 | 101.39 | -0.12 | 0.40 | -0.04 | 1.08 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.13 | XLE, XOP, USO |
| semis_ai | -4.13 | SMH, SOXX |
| high_beta | -1.49 | IWM, ARKK, HIBL |
| rates | -0.60 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 1.19 | SH, PSQ, SQQQ |
| housing_rates | 1.38 | XHB, ITB |
| defensives | 0.82 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 2.85 | 12.59 | 15.36 | MIXED |
| ITB | housing_rates | 2.40 | -3.76 | 4.38 | ABOVE_50_AND_200 |
| XLP | defensives | 1.99 | 3.72 | 3.34 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 0.92 | 4.59 | 5.51 | MIXED |
| TLT | rates | 0.59 | -3.57 | -0.95 | BELOW_50_AND_200 |
| XHB | housing_rates | 0.37 | -5.42 | 2.80 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.16 | -2.15 | 0.62 | ABOVE_50_AND_200 |
| UUP | dollar | -0.07 | 0.42 | 1.48 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | -4.80 | -16.69 | -13.51 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -4.51 | -22.87 | -18.55 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -3.45 | -13.41 | -11.35 | BELOW_50_ABOVE_200 |
| USO | energy | -3.42 | 14.23 | -3.29 | BELOW_50_ABOVE_200 |
| TBT | rates | -1.69 | 7.27 | 1.55 | ABOVE_50_AND_200 |
| XOP | energy | -1.60 | 7.56 | 1.16 | ABOVE_50_AND_200 |
| XLE | energy | -1.35 | 6.93 | 1.44 | ABOVE_50_AND_200 |
| TBF | rates | -0.68 | 3.76 | 0.84 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
