# Market Packet — 2026-11-06T09:47:51.589126+08:00

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
| SPY | 2026-11-04 | 766.81 | 1.65 | -0.71 | -1.58 | -0.03 | 5.05 | 50.70 | 1.38 | 0.00 | 7.34 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-04 | 691.95 | 0.97 | -4.64 | -8.91 | -4.37 | 1.67 | 38.52 | 2.21 | -7.34 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-11-04 | 630.00 | 1.44 | 2.86 | -14.74 | -6.47 | -0.34 | 40.12 | 3.87 | -13.16 | -5.82 | BELOW_50_AND_200 |
| AMZN | 2026-11-04 | 266.03 | 6.12 | 4.49 | 3.80 | 4.78 | 9.18 | 59.87 | 3.56 | 5.38 | 12.71 | ABOVE_50_AND_200 |
| MU | 2026-11-04 | 795.23 | -7.00 | -19.12 | -23.94 | -18.20 | 5.48 | 35.38 | 7.29 | -22.37 | -15.03 | BELOW_50_ABOVE_200 |
| ORCL | 2026-11-04 | 123.73 | -1.95 | -14.40 | -14.53 | -11.94 | -20.69 | 42.64 | 6.76 | -12.96 | -5.62 | BELOW_50_AND_200 |
| SOFI | 2026-11-04 | 17.38 | 3.64 | 1.40 | 10.28 | 5.54 | -1.52 | 60.98 | 5.00 | 11.86 | 19.19 | MIXED |
| IAU | 2026-11-04 | 76.37 | 3.67 | -0.26 | -2.55 | -3.72 | -9.54 | 47.84 | 1.77 | -0.98 | 6.36 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-05 | 28.18 | 69.66 | 63.84 | 86.87 | 68.76 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-05 | 4.84 | -1.16 | -3.05 | -8.34 | -3.83 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-05 | 91.13 | 3.42 | -10.66 | 3.23 | -4.41 | BELOW_50_ABOVE_200 |
| GC=F | 2026-11-05 | 4082.40 | 0.23 | 1.27 | -1.41 | -3.75 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-05 | 101.62 | 0.11 | -0.41 | -0.60 | 0.59 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -6.40 | XLE, XOP, USO |
| semis_ai | -2.94 | SMH, SOXX |
| high_beta | -0.34 | IWM, ARKK, HIBL |
| rates | -0.49 | TLT, TBF, TBT |
| dollar | -0.38 | UUP |
| equity_hedges | -1.76 | SH, PSQ, SQQQ |
| housing_rates | 6.34 | XHB, ITB |
| defensives | 1.90 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 7.25 | 15.35 | 11.90 | ABOVE_50_AND_200 |
| XHB | housing_rates | 5.43 | 10.42 | 9.15 | ABOVE_50_AND_200 |
| XLP | defensives | 3.36 | 12.40 | 8.37 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.51 | 0.95 | 0.29 | ABOVE_50_AND_200 |
| TLT | rates | 0.80 | 5.80 | 1.65 | MIXED |
| XLU | defensives | 0.44 | 5.95 | 4.38 | MIXED |
| ARKK | high_beta | 0.06 | -11.18 | -6.50 | BELOW_50_ABOVE_200 |
| UUP | dollar | -0.38 | 0.00 | 0.88 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -8.07 | 0.34 | -3.98 | BELOW_50_ABOVE_200 |
| XOP | energy | -6.39 | -4.87 | -6.53 | BELOW_50_ABOVE_200 |
| XLE | energy | -4.74 | -0.36 | -2.43 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -3.14 | 129.24 | 132.79 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -2.78 | 30.57 | 11.94 | MIXED |
| SMH | semis_ai | -2.75 | -20.27 | -11.53 | BELOW_50_AND_200 |
| HIBL | high_beta | -2.58 | -37.50 | -23.84 | BELOW_50_AND_200 |
| SH | equity_hedges | -1.61 | 2.11 | 0.16 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
