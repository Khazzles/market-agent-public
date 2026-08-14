# Market Packet — 2026-08-15T05:57:31.499362+08:00

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
| SPY | 2026-08-14 | 776.34 | -0.20 | 0.40 | 3.41 | 3.66 | 10.05 | 65.70 | 0.98 | 0.00 | -0.15 | ABOVE_50_AND_200 |
| QQQ | 2026-08-14 | 731.07 | -0.14 | 1.11 | 3.56 | 2.54 | 12.37 | 59.57 | 1.73 | 0.15 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-14 | 589.85 | -0.86 | -0.38 | -11.24 | -1.22 | -6.02 | 47.62 | 3.67 | -14.65 | -14.80 | BELOW_50_AND_200 |
| AMZN | 2026-08-14 | 262.65 | -0.94 | -4.31 | 5.11 | 5.84 | 10.50 | 53.49 | 3.11 | 1.69 | 1.55 | ABOVE_50_AND_200 |
| MU | 2026-08-14 | 971.66 | 2.30 | 10.72 | 13.88 | 1.14 | 75.83 | 56.30 | 7.49 | 10.47 | 10.32 | ABOVE_50_AND_200 |
| ORCL | 2026-08-14 | 150.52 | -3.65 | 2.38 | 21.18 | -1.21 | -14.54 | 56.04 | 5.04 | 17.77 | 17.62 | BELOW_50_AND_200 |
| SOFI | 2026-08-14 | 18.29 | -0.76 | -0.49 | 5.60 | 4.58 | -12.14 | 55.32 | 4.30 | 2.19 | 2.04 | MIXED |
| IAU | 2026-08-14 | 82.28 | 0.61 | 0.73 | 10.00 | 5.29 | -2.60 | 63.27 | 1.73 | 6.59 | 6.44 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-14 | 14.25 | -2.60 | -4.36 | -14.82 | -17.05 | BELOW_50_AND_200 |
| ^TNX | 2026-08-14 | 4.70 | 1.19 | 0.77 | 2.78 | 2.96 | ABOVE_50_AND_200 |
| CL=F | 2026-08-14 | 82.40 | 1.42 | 5.40 | 4.37 | 3.58 | ABOVE_50_AND_200 |
| GC=F | 2026-08-14 | 4432.00 | 1.57 | 2.10 | 11.20 | 6.56 | MIXED |
| DX-Y.NYB | 2026-08-14 | 99.64 | -0.32 | 0.04 | -1.09 | -0.91 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.13 | XLE, XOP, USO |
| semis_ai | -0.14 | SMH, SOXX |
| high_beta | -0.33 | IWM, ARKK, HIBL |
| rates | 0.51 | TLT, TBF, TBT |
| dollar | -0.25 | UUP |
| equity_hedges | 0.31 | SH, PSQ, SQQQ |
| housing_rates | -0.61 | XHB, ITB |
| defensives | 0.36 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| TBT | rates | 1.40 | 4.96 | 5.49 | ABOVE_50_AND_200 |
| XLE | energy | 1.39 | 8.58 | 8.67 | ABOVE_50_AND_200 |
| USO | energy | 1.26 | 6.12 | 5.19 | ABOVE_50_AND_200 |
| TBF | rates | 0.79 | 2.82 | 2.88 | ABOVE_50_AND_200 |
| XOP | energy | 0.74 | 8.44 | 9.09 | ABOVE_50_AND_200 |
| XLU | defensives | 0.61 | -2.55 | -1.19 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | 0.55 | -11.37 | -9.80 | BELOW_50_AND_200 |
| IWM | high_beta | 0.52 | 3.21 | 3.38 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ARKK | high_beta | -1.80 | 5.78 | 4.62 | ABOVE_50_AND_200 |
| ITB | housing_rates | -0.75 | -1.41 | 0.60 | ABOVE_50_AND_200 |
| TLT | rates | -0.67 | -2.58 | -2.87 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.47 | -1.61 | 0.25 | ABOVE_50_AND_200 |
| UUP | dollar | -0.25 | -0.81 | -0.57 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -0.22 | 3.32 | -0.62 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -0.06 | 3.75 | -2.07 | BELOW_50_ABOVE_200 |
| XLP | defensives | 0.10 | 0.33 | 1.79 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
