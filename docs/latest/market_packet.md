# Market Packet — 2026-10-31T09:02:38.230557+08:00

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
| SPY | 2026-10-29 | 769.36 | -0.38 | 0.71 | 0.88 | 0.23 | 5.60 | 50.57 | 1.00 | 0.00 | 4.18 | ABOVE_50_AND_200 |
| QQQ | 2026-10-29 | 715.34 | -1.42 | 1.54 | -3.30 | -1.39 | 5.33 | 44.40 | 1.78 | -4.18 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-10-29 | 624.52 | 1.96 | -3.75 | -13.88 | -6.59 | -1.20 | 34.97 | 3.73 | -14.76 | -10.58 | BELOW_50_AND_200 |
| AMZN | 2026-10-29 | 243.79 | -4.25 | -2.63 | -2.15 | -4.27 | 0.17 | 40.72 | 2.98 | -3.03 | 1.15 | BELOW_50_ABOVE_200 |
| MU | 2026-10-29 | 934.27 | -4.98 | 9.08 | -12.28 | -4.71 | 25.56 | 47.15 | 5.31 | -13.17 | -8.98 | BELOW_50_ABOVE_200 |
| ORCL | 2026-10-29 | 139.56 | -3.45 | 11.17 | 1.65 | -1.74 | -11.27 | 52.85 | 5.46 | 0.76 | 4.95 | BELOW_50_AND_200 |
| SOFI | 2026-10-29 | 17.61 | 2.74 | 19.23 | 12.02 | 6.09 | -1.26 | 65.25 | 4.42 | 11.14 | 15.33 | MIXED |
| IAU | 2026-10-29 | 75.57 | -1.31 | -0.12 | -3.24 | -5.91 | -10.77 | 38.48 | 1.67 | -4.12 | 0.06 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-30 | 19.42 | 12.91 | -0.15 | 18.49 | 20.00 | ABOVE_50_AND_200 |
| ^TNX | 2026-10-30 | 4.93 | -1.20 | -1.18 | -5.88 | -1.67 | BELOW_50_ABOVE_200 |
| CL=F | 2026-10-30 | 102.95 | 0.93 | -0.31 | 10.85 | 8.82 | ABOVE_50_AND_200 |
| GC=F | 2026-10-30 | 3884.90 | -3.63 | -3.07 | -7.55 | -9.54 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-30 | 101.96 | -0.07 | 0.15 | -0.13 | 1.14 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.31 | XLE, XOP, USO |
| semis_ai | -1.30 | SMH, SOXX |
| high_beta | 0.22 | IWM, ARKK, HIBL |
| rates | -0.36 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 2.03 | SH, PSQ, SQQQ |
| housing_rates | 3.43 | XHB, ITB |
| defensives | 1.54 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 4.27 | 9.94 | 2.54 | MIXED |
| ITB | housing_rates | 3.49 | 5.84 | 2.60 | MIXED |
| XHB | housing_rates | 3.37 | 5.46 | 2.60 | MIXED |
| XLP | defensives | 1.54 | 9.40 | 4.32 | ABOVE_50_AND_200 |
| XLU | defensives | 1.53 | 9.38 | 3.31 | MIXED |
| PSQ | equity_hedges | 1.42 | 3.63 | 1.10 | MIXED |
| USO | energy | 0.97 | 15.47 | 12.58 | ABOVE_50_AND_200 |
| IWM | high_beta | 0.97 | 2.20 | -0.22 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SOXX | semis_ai | -1.55 | -9.63 | -3.07 | BELOW_50_ABOVE_200 |
| TBT | rates | -1.13 | -9.23 | -2.93 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -1.06 | -7.77 | -2.05 | BELOW_50_ABOVE_200 |
| TBF | rates | -0.58 | -4.66 | -1.40 | BELOW_50_ABOVE_200 |
| XOP | energy | -0.42 | 11.26 | 4.26 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.17 | -3.51 | -0.43 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | -0.14 | -15.23 | -9.49 | BELOW_50_AND_200 |
| UUP | dollar | -0.07 | 0.94 | 1.67 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
