# Market Packet — 2026-05-20T18:29:26.860476+08:00

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
| SPY | 2026-05-19 | 733.73 | -0.67 | -0.60 | 3.53 | 5.96 | 8.35 | 62.09 | 1.05 | 0.00 | -4.93 | ABOVE_50_AND_200 |
| QQQ | 2026-05-19 | 701.53 | -0.62 | -0.81 | 8.46 | 10.40 | 14.56 | 65.60 | 1.56 | 4.93 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-05-19 | 602.61 | -1.41 | -0.06 | -10.18 | -2.85 | -10.31 | 41.46 | 2.73 | -13.71 | -18.64 | BELOW_50_AND_200 |
| AMZN | 2026-05-19 | 259.34 | -2.08 | -2.44 | 4.45 | 8.67 | 12.86 | 51.93 | 2.64 | 0.93 | -4.01 | ABOVE_50_AND_200 |
| MU | 2026-05-19 | 698.74 | 2.52 | -8.85 | 55.82 | 40.13 | 123.27 | 61.29 | 7.26 | 52.29 | 47.36 | ABOVE_50_AND_200 |
| ORCL | 2026-05-19 | 181.46 | -2.76 | -2.87 | 2.18 | 9.81 | -13.16 | 52.07 | 4.98 | -1.34 | -6.28 | MIXED |
| SOFI | 2026-05-19 | 15.23 | -3.06 | -4.21 | -21.90 | -9.95 | -34.96 | 38.85 | 5.29 | -25.43 | -30.36 | BELOW_50_AND_200 |
| IAU | 2026-05-19 | 84.32 | -1.68 | -4.95 | -6.90 | -4.75 | 3.30 | 36.98 | 1.92 | -10.43 | -15.36 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-05-20 | 17.92 | -0.78 | 0.28 | -8.10 | -15.26 | BELOW_50_AND_200 |
| ^TNX | 2026-05-19 | 4.67 | 0.95 | 4.57 | 9.81 | 7.32 | ABOVE_50_AND_200 |
| CL=F | 2026-05-20 | 102.25 | -5.12 | 1.22 | 10.98 | 4.06 | ABOVE_50_AND_200 |
| GC=F | 2026-05-20 | 4491.90 | -0.32 | -4.38 | -4.40 | -4.28 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-05-20 | 99.39 | 0.09 | 0.93 | 1.00 | 0.41 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.65 | XLE, XOP, USO |
| semis_ai | -0.11 | SMH, SOXX |
| high_beta | -2.12 | IWM, ARKK, HIBL |
| rates | 0.55 | TLT, TBF, TBT |
| dollar | 0.32 | UUP |
| equity_hedges | 1.07 | SH, PSQ, SQQQ |
| housing_rates | -1.54 | XHB, ITB |
| defensives | 0.57 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 2.46 | 26.08 | 17.85 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 1.91 | -22.03 | -29.03 | BELOW_50_AND_200 |
| TBT | rates | 1.57 | 9.83 | 7.64 | ABOVE_50_AND_200 |
| XOP | energy | 1.33 | 10.83 | 3.63 | ABOVE_50_AND_200 |
| XLE | energy | 1.17 | 11.29 | 5.20 | ABOVE_50_AND_200 |
| XLU | defensives | 0.91 | -3.08 | -3.32 | BELOW_50_AND_200 |
| TBF | rates | 0.72 | 5.01 | 3.93 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.65 | -3.01 | -5.55 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -4.40 | 0.15 | 12.25 | ABOVE_50_AND_200 |
| XHB | housing_rates | -1.61 | -13.29 | -7.02 | BELOW_50_AND_200 |
| ITB | housing_rates | -1.46 | -13.78 | -7.46 | BELOW_50_AND_200 |
| IWM | high_beta | -1.08 | -1.57 | 3.13 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.90 | -6.91 | 0.42 | MIXED |
| TLT | rates | -0.65 | -4.63 | -3.71 | BELOW_50_AND_200 |
| SMH | semis_ai | -0.40 | 17.24 | 18.82 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.18 | 18.97 | 21.84 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
