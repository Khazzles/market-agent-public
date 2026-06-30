# Market Packet — 2026-07-01T06:55:44.184638+08:00

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
| SPY | 2026-06-30 | 746.77 | 0.78 | 1.80 | -1.28 | 1.48 | 8.00 | 54.95 | 1.38 | 0.00 | -1.02 | ABOVE_50_AND_200 |
| QQQ | 2026-06-30 | 736.40 | 1.70 | 3.19 | -0.26 | 4.27 | 16.22 | 56.64 | 2.22 | 1.02 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-30 | 563.29 | 0.12 | 0.19 | -10.94 | -7.37 | -13.09 | 42.76 | 3.27 | -9.66 | -10.69 | BELOW_50_AND_200 |
| AMZN | 2026-06-30 | 238.34 | -0.75 | 1.81 | -11.93 | -6.79 | 2.35 | 44.91 | 3.48 | -10.65 | -11.68 | BELOW_50_ABOVE_200 |
| MU | 2026-06-30 | 1154.29 | 0.79 | 9.75 | 18.88 | 39.09 | 164.82 | 59.99 | 8.10 | 20.16 | 19.14 | ABOVE_50_AND_200 |
| ORCL | 2026-06-30 | 146.55 | -0.82 | -11.27 | -35.09 | -22.00 | -27.25 | 28.92 | 7.29 | -33.81 | -34.83 | BELOW_50_AND_200 |
| SOFI | 2026-06-30 | 17.93 | -1.43 | 3.70 | -1.59 | 6.05 | -20.02 | 56.92 | 5.14 | -0.31 | -1.33 | MIXED |
| IAU | 2026-06-30 | 75.51 | -0.03 | -2.35 | -11.67 | -9.87 | -9.98 | 33.06 | 2.19 | -10.39 | -11.42 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-30 | 16.45 | -6.80 | -15.60 | 7.38 | -7.29 | BELOW_50_AND_200 |
| ^TNX | 2026-06-30 | 4.42 | 1.05 | -2.02 | -0.83 | -0.61 | BELOW_50_ABOVE_200 |
| CL=F | 2026-06-30 | 69.94 | -1.14 | -4.47 | -19.94 | -23.34 | BELOW_50_AND_200 |
| GC=F | 2026-06-30 | 4028.90 | 0.16 | -2.45 | -11.66 | -9.59 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-30 | 101.17 | 0.06 | -0.23 | 2.29 | 1.84 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.73 | XLE, XOP, USO |
| semis_ai | 4.04 | SMH, SOXX |
| high_beta | 1.74 | IWM, ARKK, HIBL |
| rates | 0.87 | TLT, TBF, TBT |
| dollar | 0.14 | UUP |
| equity_hedges | -2.39 | SH, PSQ, SQQQ |
| housing_rates | 0.32 | XHB, ITB |
| defensives | -1.51 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.48 | 6.09 | 21.13 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 4.30 | 12.60 | 18.86 | ABOVE_50_AND_200 |
| SMH | semis_ai | 3.78 | 9.51 | 14.30 | ABOVE_50_AND_200 |
| TBT | rates | 2.49 | -2.32 | -2.14 | BELOW_50_ABOVE_200 |
| TBF | rates | 1.30 | -1.30 | -1.19 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.49 | 3.45 | 5.17 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.49 | 12.27 | 9.71 | ABOVE_50_AND_200 |
| ARKK | high_beta | 0.24 | -1.38 | 4.22 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -4.85 | -4.65 | -16.68 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -1.61 | -0.91 | -5.13 | BELOW_50_AND_200 |
| XLP | defensives | -1.54 | 0.19 | -0.97 | BELOW_50_ABOVE_200 |
| XLU | defensives | -1.48 | 2.07 | 0.71 | ABOVE_50_AND_200 |
| TLT | rates | -1.18 | 0.77 | 0.88 | MIXED |
| XLE | energy | -0.88 | -5.65 | -6.96 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.72 | 0.43 | -2.06 | BELOW_50_AND_200 |
| XOP | energy | -0.71 | -5.93 | -7.40 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
