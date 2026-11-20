# Market Packet — 2026-11-20T10:35:23.737266+08:00

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
| SPY | 2026-11-19 | 715.87 | -1.96 | -5.45 | -7.40 | -6.01 | -2.30 | 31.59 | 1.71 | 0.00 | 3.65 | BELOW_50_AND_200 |
| QQQ | 2026-11-19 | 645.04 | -2.19 | -6.27 | -11.05 | -9.54 | -5.56 | 33.91 | 2.67 | -3.65 | 0.00 | BELOW_50_AND_200 |
| META | 2026-11-18 | 616.38 | -0.40 | -1.97 | -11.22 | -9.27 | -2.08 | 41.43 | 3.60 | -3.81 | -0.16 | BELOW_50_AND_200 |
| AMZN | 2026-11-19 | 257.37 | -3.87 | -3.77 | -1.91 | 0.84 | 5.04 | 48.97 | 3.73 | 5.50 | 9.15 | ABOVE_50_AND_200 |
| MU | 2026-11-19 | 690.44 | -2.10 | -13.53 | -24.43 | -24.94 | -10.51 | 35.86 | 8.47 | -17.03 | -13.38 | BELOW_50_AND_200 |
| ORCL | 2026-11-19 | 110.57 | -2.92 | -13.01 | -14.37 | -16.94 | -27.86 | 37.12 | 7.01 | -6.97 | -3.32 | BELOW_50_AND_200 |
| SOFI | 2026-11-18 | 14.11 | -1.19 | -13.28 | -3.88 | -11.64 | -18.00 | 35.87 | 5.56 | 3.52 | 7.17 | BELOW_50_AND_200 |
| IAU | 2026-11-19 | 68.72 | -1.77 | -5.59 | -11.57 | -10.96 | -17.49 | 27.95 | 2.04 | -4.17 | -0.52 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-19 | 28.44 | 15.80 | 52.09 | 70.50 | 57.70 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-19 | 5.05 | -0.28 | -1.00 | -1.83 | -0.51 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-19 | 82.77 | -0.59 | -6.73 | -14.80 | -12.38 | BELOW_50_AND_200 |
| GC=F | 2026-11-19 | 3534.60 | -5.54 | -9.03 | -14.83 | -14.33 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-19 | 103.90 | 0.03 | 0.70 | 2.08 | 2.07 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.05 | XLE, XOP, USO |
| semis_ai | -2.69 | SMH, SOXX |
| high_beta | -0.30 | IWM, ARKK, HIBL |
| rates | -0.07 | TLT, TBF, TBT |
| dollar | 0.03 | UUP |
| equity_hedges | 3.62 | SH, PSQ, SQQQ |
| housing_rates | -2.43 | XHB, ITB |
| defensives | -1.34 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 6.62 | 35.47 | 28.35 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 2.23 | 11.90 | 9.85 | ABOVE_50_AND_200 |
| SH | equity_hedges | 2.00 | 8.14 | 6.47 | ABOVE_50_AND_200 |
| USO | energy | 1.45 | -13.59 | -9.14 | BELOW_50_ABOVE_200 |
| HIBL | high_beta | 0.98 | -31.97 | -35.17 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.31 | -14.82 | -15.24 | BELOW_50_AND_200 |
| TLT | rates | 0.16 | 0.14 | 0.36 | MIXED |
| UUP | dollar | 0.03 | 2.46 | 2.43 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XHB | housing_rates | -2.84 | 2.40 | -0.59 | BELOW_50_AND_200 |
| SOXX | semis_ai | -2.75 | -18.91 | -18.45 | BELOW_50_AND_200 |
| SMH | semis_ai | -2.62 | -19.62 | -18.77 | BELOW_50_AND_200 |
| IWM | high_beta | -2.18 | -4.43 | -5.27 | BELOW_50_AND_200 |
| ITB | housing_rates | -2.03 | 4.86 | 0.92 | MIXED |
| XLP | defensives | -1.45 | 3.16 | 4.18 | ABOVE_50_AND_200 |
| XLU | defensives | -1.24 | 2.40 | 2.56 | MIXED |
| XOP | energy | -0.95 | -14.61 | -9.96 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
