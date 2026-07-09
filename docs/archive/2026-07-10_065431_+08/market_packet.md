# Market Packet — 2026-07-10T06:54:31.175068+08:00

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
| SPY | 2026-07-09 | 751.71 | 0.85 | 0.80 | 1.69 | 1.53 | 8.31 | 57.12 | 1.25 | 0.00 | 0.68 | ABOVE_50_AND_200 |
| QQQ | 2026-07-09 | 723.28 | 1.66 | -0.26 | 1.01 | 1.33 | 13.48 | 52.06 | 2.19 | -0.68 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-09 | 631.48 | 4.70 | 3.03 | 7.87 | 5.16 | -1.82 | 59.96 | 3.92 | 6.18 | 6.87 | MIXED |
| AMZN | 2026-07-09 | 247.04 | 1.40 | 2.21 | 0.74 | -2.86 | 5.91 | 52.71 | 3.16 | -0.95 | -0.26 | BELOW_50_ABOVE_200 |
| MU | 2026-07-09 | 991.64 | 4.52 | -3.94 | 4.46 | 11.48 | 115.38 | 49.98 | 9.11 | 2.77 | 3.46 | ABOVE_50_AND_200 |
| ORCL | 2026-07-09 | 144.22 | 2.65 | 1.21 | -31.91 | -21.44 | -26.67 | 32.61 | 6.40 | -33.60 | -32.92 | BELOW_50_AND_200 |
| SOFI | 2026-07-09 | 18.62 | 5.02 | 0.98 | 12.85 | 10.59 | -15.87 | 59.25 | 5.02 | 11.16 | 11.84 | MIXED |
| IAU | 2026-07-09 | 77.51 | 1.00 | 2.04 | -4.76 | -5.92 | -7.87 | 43.74 | 2.07 | -6.45 | -5.76 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-09 | 15.84 | -6.27 | -4.52 | -16.28 | -9.18 | BELOW_50_AND_200 |
| ^TNX | 2026-07-09 | 4.54 | -0.66 | 2.74 | 0.07 | 1.53 | ABOVE_50_AND_200 |
| CL=F | 2026-07-09 | 71.85 | -2.27 | 4.77 | -21.30 | -18.75 | BELOW_50_AND_200 |
| GC=F | 2026-07-09 | 4131.90 | 1.50 | 1.56 | -4.70 | -5.73 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-09 | 100.94 | -0.11 | -0.45 | 0.89 | 1.29 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -1.94 | XLE, XOP, USO |
| semis_ai | 2.99 | SMH, SOXX |
| high_beta | 3.95 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | 0.00 | UUP |
| equity_hedges | -2.46 | SH, PSQ, SQQQ |
| housing_rates | 1.25 | XHB, ITB |
| defensives | -0.96 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 8.87 | 3.34 | 3.74 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 3.50 | 1.79 | 4.74 | ABOVE_50_AND_200 |
| SMH | semis_ai | 2.48 | 1.60 | 3.39 | ABOVE_50_AND_200 |
| ARKK | high_beta | 1.71 | 7.45 | 4.48 | ABOVE_50_AND_200 |
| XHB | housing_rates | 1.48 | 4.18 | 2.02 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.28 | 4.62 | 3.14 | ABOVE_50_AND_200 |
| ITB | housing_rates | 1.02 | 4.69 | 1.75 | MIXED |
| TLT | rates | 0.15 | -0.15 | -1.14 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -4.94 | -7.66 | -8.58 | BELOW_50_AND_200 |
| USO | energy | -2.85 | -19.34 | -15.54 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -1.62 | -2.07 | -2.20 | BELOW_50_AND_200 |
| XOP | energy | -1.56 | -5.30 | -3.58 | BELOW_50_ABOVE_200 |
| XLP | defensives | -1.41 | 0.16 | -1.04 | BELOW_50_ABOVE_200 |
| XLE | energy | -1.40 | -6.02 | -3.50 | BELOW_50_ABOVE_200 |
| SH | equity_hedges | -0.82 | -2.41 | -1.96 | BELOW_50_AND_200 |
| XLU | defensives | -0.51 | 3.70 | 0.34 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
