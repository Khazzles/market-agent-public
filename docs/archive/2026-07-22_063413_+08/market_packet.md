# Market Packet — 2026-07-22T06:34:13.297585+08:00

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
| SPY | 2026-07-21 | 748.28 | 0.83 | -0.47 | 0.21 | 0.46 | 7.28 | 52.46 | 1.11 | 0.00 | 4.48 | ABOVE_50_AND_200 |
| QQQ | 2026-07-21 | 708.97 | 1.85 | -1.49 | -4.27 | -1.44 | 10.46 | 48.04 | 2.10 | -4.48 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-21 | 643.81 | -0.32 | -2.61 | 11.54 | 6.29 | 0.64 | 56.17 | 3.85 | 11.33 | 15.81 | ABOVE_50_AND_200 |
| AMZN | 2026-07-21 | 247.55 | -0.98 | 0.02 | 1.29 | -1.44 | 5.63 | 51.31 | 2.89 | 1.09 | 5.57 | BELOW_50_ABOVE_200 |
| MU | 2026-07-21 | 970.82 | 12.17 | -1.25 | -14.39 | 2.82 | 97.92 | 51.04 | 8.82 | -14.60 | -10.12 | ABOVE_50_AND_200 |
| ORCL | 2026-07-21 | 127.05 | 4.67 | -0.70 | -31.06 | -27.76 | -33.11 | 33.02 | 6.42 | -31.27 | -26.79 | BELOW_50_AND_200 |
| SOFI | 2026-07-21 | 17.64 | 3.70 | -4.91 | -1.51 | 3.34 | -18.82 | 50.05 | 5.14 | -1.71 | 2.77 | MIXED |
| IAU | 2026-07-21 | 76.82 | 1.95 | 0.72 | -3.16 | -4.78 | -8.88 | 46.48 | 1.92 | -3.37 | 1.11 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-21 | 17.05 | -8.58 | 3.33 | 3.96 | -1.74 | BELOW_50_AND_200 |
| ^TNX | 2026-07-21 | 4.63 | 0.65 | 0.94 | 3.98 | 2.77 | ABOVE_50_AND_200 |
| CL=F | 2026-07-21 | 84.65 | 1.71 | 6.69 | 10.51 | -0.34 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-21 | 4085.60 | 1.88 | 0.60 | -3.28 | -4.81 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-21 | 101.19 | 0.20 | 0.25 | 0.34 | 1.14 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.95 | XLE, XOP, USO |
| semis_ai | 4.98 | SMH, SOXX |
| high_beta | 5.21 | IWM, ARKK, HIBL |
| rates | 0.24 | TLT, TBF, TBT |
| dollar | 0.32 | UUP |
| equity_hedges | -2.73 | SH, PSQ, SQQQ |
| housing_rates | -0.31 | XHB, ITB |
| defensives | -0.49 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 10.51 | -19.98 | -7.43 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 5.45 | -13.57 | -2.68 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 4.52 | -11.49 | -2.39 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 3.66 | -3.11 | -0.64 | BELOW_50_AND_200 |
| USO | energy | 2.66 | 12.17 | 2.62 | ABOVE_50_AND_200 |
| XOP | energy | 2.23 | 13.35 | 5.96 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.45 | 0.32 | 2.01 | ABOVE_50_AND_200 |
| XLE | energy | 0.97 | 8.80 | 3.37 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -5.55 | 9.69 | 0.46 | MIXED |
| PSQ | equity_hedges | -1.85 | 3.38 | 0.77 | MIXED |
| XLP | defensives | -0.94 | 0.91 | -0.14 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.78 | -0.66 | -0.67 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.50 | -4.35 | -0.73 | BELOW_50_AND_200 |
| TLT | rates | -0.27 | -3.56 | -1.83 | BELOW_50_AND_200 |
| XHB | housing_rates | -0.12 | -4.59 | -0.12 | BELOW_50_AND_200 |
| XLU | defensives | -0.04 | 0.36 | 0.15 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
