# Market Packet — 2026-11-03T11:03:24.160509+08:00

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
| SPY | 2026-11-02 | 752.10 | -0.48 | -1.73 | -2.28 | -1.97 | 3.15 | 37.98 | 1.07 | 0.00 | 6.86 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-02 | 681.09 | -1.36 | -4.37 | -9.14 | -5.97 | 0.19 | 32.08 | 1.93 | -6.86 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-11-02 | 606.73 | -1.34 | -3.78 | -16.67 | -9.59 | -4.00 | 31.72 | 3.74 | -14.39 | -7.53 | BELOW_50_AND_200 |
| AMZN | 2026-11-02 | 245.63 | 2.20 | -1.39 | -2.34 | -3.30 | 0.90 | 43.86 | 3.13 | -0.06 | 6.80 | BELOW_50_ABOVE_200 |
| MU | 2026-11-02 | 833.59 | -5.78 | -7.76 | -22.45 | -14.60 | 11.25 | 37.42 | 6.06 | -20.17 | -13.31 | BELOW_50_ABOVE_200 |
| ORCL | 2026-11-02 | 119.22 | -8.76 | -5.43 | -16.22 | -15.60 | -23.88 | 38.34 | 6.68 | -13.94 | -7.08 | BELOW_50_AND_200 |
| SOFI | 2026-11-02 | 16.60 | -0.95 | 14.80 | 5.26 | 0.43 | -6.41 | 55.54 | 4.80 | 7.54 | 14.40 | MIXED |
| IAU | 2026-11-02 | 74.15 | 1.69 | -1.68 | -4.87 | -7.10 | -12.30 | 36.99 | 1.74 | -2.60 | 4.26 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-02 | 21.15 | 8.91 | 15.01 | 38.15 | 29.84 | ABOVE_50_AND_200 |
| ^TNX | 2026-11-02 | 4.89 | -0.71 | -1.85 | -7.26 | -2.43 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-02 | 96.63 | -7.19 | -5.04 | 6.06 | 1.91 | ABOVE_50_AND_200 |
| GC=F | 2026-11-02 | 3959.10 | 1.54 | -1.96 | -4.88 | -7.51 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-02 | 101.82 | -0.06 | -0.14 | -0.11 | 0.93 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -5.35 | XLE, XOP, USO |
| semis_ai | -3.25 | SMH, SOXX |
| high_beta | -2.54 | IWM, ARKK, HIBL |
| rates | -0.45 | TLT, TBF, TBT |
| dollar | -0.14 | UUP |
| equity_hedges | 1.99 | SH, PSQ, SQQQ |
| housing_rates | 4.07 | XHB, ITB |
| defensives | 1.06 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | 4.56 | 11.92 | 8.14 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | 4.11 | 31.49 | 17.59 | MIXED |
| XHB | housing_rates | 3.58 | 8.15 | 6.10 | MIXED |
| XLP | defensives | 1.58 | 12.79 | 7.23 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.35 | 10.07 | 5.95 | MIXED |
| XLU | defensives | 0.55 | 9.64 | 4.55 | MIXED |
| SH | equity_hedges | 0.52 | 2.83 | 2.10 | MIXED |
| IWM | high_beta | -0.07 | -0.85 | -1.66 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -7.08 | 6.45 | 4.21 | ABOVE_50_AND_200 |
| HIBL | high_beta | -5.33 | -36.68 | -26.21 | BELOW_50_AND_200 |
| XOP | energy | -5.01 | 4.67 | 0.93 | ABOVE_50_AND_200 |
| XLE | energy | -3.96 | 7.05 | 3.46 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -3.79 | -22.97 | -14.05 | BELOW_50_AND_200 |
| SMH | semis_ai | -2.71 | -19.39 | -11.07 | BELOW_50_AND_200 |
| ARKK | high_beta | -2.22 | -12.10 | -8.34 | BELOW_50_ABOVE_200 |
| TBT | rates | -0.78 | -10.41 | -4.08 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
