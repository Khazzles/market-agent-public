# Market Packet — 2026-06-02T20:28:15.314818+08:00

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
| SPY | 2026-06-01 | 758.54 | 0.27 | 1.73 | 5.55 | 7.50 | 11.27 | 75.11 | 0.89 | 0.00 | -5.68 | ABOVE_50_AND_200 |
| QQQ | 2026-06-01 | 742.74 | 0.60 | 3.51 | 11.23 | 13.24 | 20.06 | 78.43 | 1.39 | 5.68 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-01 | 600.47 | -5.07 | -1.60 | -1.87 | -2.90 | -9.80 | 41.61 | 2.83 | -7.42 | -13.10 | BELOW_50_AND_200 |
| AMZN | 2026-06-01 | 261.26 | -3.47 | -1.90 | -1.43 | 5.47 | 12.76 | 48.95 | 2.63 | -6.98 | -12.67 | ABOVE_50_AND_200 |
| MU | 2026-06-01 | 1035.50 | 6.64 | 37.88 | 100.23 | 81.86 | 201.64 | 80.72 | 5.54 | 94.68 | 89.00 | ABOVE_50_AND_200 |
| ORCL | 2026-06-01 | 248.15 | 9.91 | 29.19 | 53.76 | 43.47 | 19.86 | 80.70 | 4.33 | 48.21 | 42.53 | ABOVE_50_AND_200 |
| SOFI | 2026-06-01 | 18.58 | 1.98 | 18.95 | 15.40 | 10.99 | -19.87 | 66.05 | 4.83 | 9.85 | 4.17 | MIXED |
| IAU | 2026-06-01 | 84.27 | -1.43 | -0.64 | -2.97 | -3.19 | 2.18 | 40.93 | 1.90 | -8.52 | -14.20 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-02 | 16.15 | 0.62 | -5.06 | -11.70 | -17.34 | BELOW_50_AND_200 |
| ^TNX | 2026-06-01 | 4.47 | 0.49 | -1.82 | 1.94 | 1.87 | ABOVE_50_AND_200 |
| CL=F | 2026-06-02 | 90.70 | -1.58 | -3.40 | -11.03 | -7.10 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-02 | 4555.40 | 1.79 | 1.22 | -1.61 | -1.56 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-06-02 | 99.08 | -0.12 | -0.09 | 0.89 | 0.20 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 3.04 | XLE, XOP, USO |
| semis_ai | 0.99 | SMH, SOXX |
| high_beta | -0.18 | IWM, ARKK, HIBL |
| rates | -0.16 | TLT, TBF, TBT |
| dollar | 0.36 | UUP |
| equity_hedges | -0.83 | SH, PSQ, SQQQ |
| housing_rates | 0.27 | XHB, ITB |
| defensives | -2.02 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 4.97 | -7.88 | 1.80 | ABOVE_50_AND_200 |
| XOP | energy | 2.37 | -5.80 | -2.57 | BELOW_50_ABOVE_200 |
| XLE | energy | 1.79 | -3.94 | -1.71 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 1.48 | 19.95 | 24.30 | ABOVE_50_AND_200 |
| HIBL | high_beta | 0.81 | 37.21 | 44.38 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.58 | -2.61 | 1.13 | MIXED |
| SOXX | semis_ai | 0.50 | 23.94 | 29.32 | ABOVE_50_AND_200 |
| UUP | dollar | 0.36 | 1.46 | 0.65 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| XLU | defensives | -2.97 | -8.00 | -5.35 | BELOW_50_AND_200 |
| SQQQ | equity_hedges | -1.73 | -27.55 | -34.50 | BELOW_50_AND_200 |
| XLP | defensives | -1.06 | -2.70 | -1.22 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -0.84 | 7.15 | 8.91 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | -0.51 | -9.79 | -12.03 | BELOW_50_AND_200 |
| IWM | high_beta | -0.50 | 3.96 | 6.69 | ABOVE_50_AND_200 |
| TLT | rates | -0.34 | -0.18 | -0.45 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.24 | -4.79 | -6.74 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
