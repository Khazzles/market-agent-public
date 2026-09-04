# Market Packet — 2026-09-05T07:19:42.528766+08:00

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
| SPY | 2026-09-04 | 770.19 | -0.39 | 0.11 | 0.21 | 1.76 | 8.15 | 55.61 | 0.81 | 0.00 | -0.39 | ABOVE_50_AND_200 |
| QQQ | 2026-09-04 | 718.96 | 0.18 | 0.35 | 0.60 | 1.11 | 9.31 | 53.62 | 1.31 | 0.39 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-09-04 | 616.77 | 1.00 | 6.70 | 4.55 | 3.57 | -0.89 | 62.40 | 3.26 | 4.34 | 3.95 | MIXED |
| AMZN | 2026-09-04 | 258.51 | -0.15 | -2.97 | -5.05 | 1.80 | 8.11 | 49.55 | 2.59 | -5.26 | -5.65 | ABOVE_50_AND_200 |
| MU | 2026-09-04 | 1016.59 | 6.10 | 8.98 | 15.33 | 8.35 | 67.62 | 60.15 | 5.39 | 15.12 | 14.73 | ABOVE_50_AND_200 |
| ORCL | 2026-09-04 | 158.78 | 3.08 | 5.26 | 10.67 | 13.55 | -5.93 | 60.94 | 4.27 | 10.46 | 10.07 | MIXED |
| SOFI | 2026-09-04 | 18.22 | -1.57 | 0.89 | 0.66 | 1.89 | -8.76 | 51.18 | 4.67 | 0.45 | 0.06 | MIXED |
| IAU | 2026-09-04 | 83.39 | -0.84 | -0.51 | 4.41 | 4.62 | -2.02 | 52.45 | 1.94 | 4.20 | 3.80 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-04 | 14.53 | 1.47 | 0.69 | -4.09 | -10.31 | BELOW_50_AND_200 |
| ^TNX | 2026-09-04 | 4.78 | 0.46 | 1.36 | 2.44 | 3.25 | ABOVE_50_AND_200 |
| CL=F | 2026-09-04 | 91.22 | -0.09 | 9.38 | 18.02 | 12.68 | ABOVE_50_AND_200 |
| GC=F | 2026-09-04 | 4477.20 | -0.32 | -0.02 | 5.54 | 5.60 | MIXED |
| DX-Y.NYB | 2026-09-04 | 99.16 | 0.16 | -0.54 | -0.81 | -1.08 | BELOW_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.60 | XLE, XOP, USO |
| semis_ai | 3.06 | SMH, SOXX |
| high_beta | 0.94 | IWM, ARKK, HIBL |
| rates | -0.09 | TLT, TBF, TBT |
| dollar | 0.25 | UUP |
| equity_hedges | -0.01 | SH, PSQ, SQQQ |
| housing_rates | 0.63 | XHB, ITB |
| defensives | -0.34 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 3.60 | 3.73 | 0.31 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 3.52 | -2.38 | -3.43 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 2.61 | -0.78 | -1.21 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 0.96 | -5.11 | -4.19 | BELOW_50_AND_200 |
| SH | equity_hedges | 0.47 | 0.34 | -1.19 | BELOW_50_AND_200 |
| ITB | housing_rates | 0.31 | -4.63 | -4.05 | BELOW_50_AND_200 |
| IWM | high_beta | 0.28 | -0.75 | -0.34 | BELOW_50_ABOVE_200 |
| UUP | dollar | 0.25 | -0.39 | -0.58 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -1.06 | 13.85 | 8.11 | ABOVE_50_AND_200 |
| XLE | energy | -0.87 | 10.14 | 8.20 | ABOVE_50_AND_200 |
| XOP | energy | -0.84 | 14.16 | 9.87 | ABOVE_50_AND_200 |
| XLP | defensives | -0.80 | -0.62 | -0.53 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | -0.42 | -1.34 | -4.13 | BELOW_50_AND_200 |
| TBF | rates | -0.24 | 0.43 | 1.39 | ABOVE_50_AND_200 |
| TBT | rates | -0.21 | 0.26 | 2.37 | ABOVE_50_AND_200 |
| USO | energy | -0.09 | 19.42 | 14.60 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
