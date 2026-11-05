# Market Packet — 2026-11-05T09:47:53.087306+08:00

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
| SPY | 2026-11-03 | 754.35 | 0.30 | -1.99 | -2.64 | -1.65 | 3.41 | 40.19 | 1.10 | 0.00 | 6.74 | BELOW_50_ABOVE_200 |
| QQQ | 2026-11-03 | 685.28 | 0.62 | -4.99 | -9.38 | -5.34 | 0.76 | 34.60 | 1.90 | -6.74 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-11-03 | 621.03 | 2.36 | 0.14 | -16.29 | -7.63 | -1.74 | 36.99 | 3.60 | -13.65 | -6.91 | BELOW_50_AND_200 |
| AMZN | 2026-11-03 | 250.69 | 2.06 | -0.95 | -0.28 | -1.22 | 2.95 | 48.66 | 3.42 | 2.36 | 9.10 | BELOW_50_ABOVE_200 |
| MU | 2026-11-03 | 855.10 | 2.58 | -7.93 | -19.63 | -12.29 | 13.74 | 40.35 | 5.92 | -16.99 | -10.25 | BELOW_50_ABOVE_200 |
| ORCL | 2026-11-03 | 126.19 | 5.85 | -3.32 | -11.43 | -10.46 | -19.26 | 44.18 | 6.36 | -8.79 | -2.05 | BELOW_50_AND_200 |
| SOFI | 2026-11-03 | 16.77 | 1.02 | 2.26 | 5.34 | 1.63 | -5.20 | 56.78 | 4.66 | 7.98 | 14.72 | MIXED |
| IAU | 2026-11-03 | 73.67 | -0.65 | -3.48 | -5.33 | -7.39 | -12.81 | 35.55 | 1.84 | -2.69 | 4.05 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-11-04 | 16.61 | -20.26 | -1.77 | 10.66 | 1.13 | MIXED |
| ^TNX | 2026-11-04 | 4.89 | -1.17 | -2.99 | -7.12 | -2.63 | BELOW_50_ABOVE_200 |
| CL=F | 2026-11-04 | 87.31 | -9.14 | -15.05 | -2.38 | -8.23 | BELOW_50_ABOVE_200 |
| GC=F | 2026-11-04 | 4130.00 | 4.81 | 1.94 | -1.36 | -2.92 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-11-04 | 101.33 | -0.53 | -0.85 | -0.49 | 0.34 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.36 | XLE, XOP, USO |
| semis_ai | 2.26 | SMH, SOXX |
| high_beta | 2.26 | IWM, ARKK, HIBL |
| rates | 0.47 | TLT, TBF, TBT |
| dollar | 0.17 | UUP |
| equity_hedges | -0.89 | SH, PSQ, SQQQ |
| housing_rates | -3.02 | XHB, ITB |
| defensives | -1.32 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 4.83 | -34.42 | -22.28 | BELOW_50_AND_200 |
| SOXX | semis_ai | 2.50 | -21.12 | -11.76 | BELOW_50_AND_200 |
| SMH | semis_ai | 2.01 | -18.20 | -9.19 | BELOW_50_AND_200 |
| ARKK | high_beta | 1.72 | -13.43 | -6.68 | BELOW_50_ABOVE_200 |
| TBT | rates | 1.39 | -10.01 | -2.78 | BELOW_50_ABOVE_200 |
| USO | energy | 0.83 | 9.85 | 4.71 | ABOVE_50_AND_200 |
| TBF | rates | 0.79 | -5.11 | -1.26 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 0.23 | -1.27 | -1.31 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| ITB | housing_rates | -3.56 | 9.28 | 4.39 | MIXED |
| XHB | housing_rates | -2.49 | 5.90 | 3.55 | MIXED |
| XLP | defensives | -2.07 | 9.76 | 4.98 | ABOVE_50_AND_200 |
| SQQQ | equity_hedges | -1.84 | 32.56 | 15.28 | MIXED |
| XOP | energy | -1.05 | 2.18 | -0.18 | BELOW_50_ABOVE_200 |
| XLE | energy | -0.85 | 5.09 | 2.47 | ABOVE_50_AND_200 |
| TLT | rates | -0.76 | 5.19 | 0.80 | MIXED |
| XLU | defensives | -0.57 | 8.63 | 3.94 | MIXED |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
