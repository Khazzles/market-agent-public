# Market Packet — 2026-08-05T06:42:54.931444+08:00

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
| SPY | 2026-08-04 | 771.33 | 1.80 | 4.11 | 2.67 | 3.41 | 9.97 | 66.00 | 1.25 | 0.00 | 2.53 | ABOVE_50_AND_200 |
| QQQ | 2026-08-04 | 723.85 | 3.40 | 7.16 | 0.14 | 1.24 | 12.02 | 58.02 | 2.22 | -2.53 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-08-04 | 587.94 | -0.39 | -0.92 | -2.06 | -2.25 | -7.15 | 46.46 | 4.33 | -4.73 | -2.20 | BELOW_50_AND_200 |
| AMZN | 2026-08-04 | 277.42 | -2.32 | 20.17 | 13.62 | 12.23 | 17.72 | 67.04 | 3.54 | 10.95 | 13.48 | ABOVE_50_AND_200 |
| MU | 2026-08-04 | 892.67 | 7.62 | 8.79 | -9.35 | -7.92 | 70.09 | 48.76 | 9.82 | -12.02 | -9.49 | BELOW_50_ABOVE_200 |
| ORCL | 2026-08-04 | 145.74 | 2.74 | 21.49 | 1.38 | -10.65 | -19.72 | 55.84 | 5.56 | -1.29 | 1.23 | BELOW_50_AND_200 |
| SOFI | 2026-08-04 | 18.70 | 3.72 | 11.71 | 0.48 | 8.10 | -11.86 | 59.13 | 5.13 | -2.19 | 0.34 | MIXED |
| IAU | 2026-08-04 | 76.69 | 0.66 | 1.31 | -2.06 | -2.42 | -9.08 | 48.32 | 1.80 | -4.72 | -2.20 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-08-04 | 16.50 | 4.04 | -9.39 | 5.97 | -4.93 | BELOW_50_AND_200 |
| ^TNX | 2026-08-04 | 4.63 | -1.26 | 0.50 | 3.30 | 2.11 | ABOVE_50_AND_200 |
| CL=F | 2026-08-04 | 75.26 | -6.32 | -5.05 | 9.79 | -7.58 | BELOW_50_AND_200 |
| GC=F | 2026-08-04 | 4136.50 | 2.55 | 2.48 | -0.45 | -1.11 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-08-04 | 99.88 | -0.08 | -1.48 | -0.96 | -0.57 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -2.33 | XLE, XOP, USO |
| semis_ai | 6.17 | SMH, SOXX |
| high_beta | 5.96 | IWM, ARKK, HIBL |
| rates | -0.51 | TLT, TBF, TBT |
| dollar | -0.04 | UUP |
| equity_hedges | -5.07 | SH, PSQ, SQQQ |
| housing_rates | 2.81 | XHB, ITB |
| defensives | 0.02 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 11.65 | -5.99 | -1.26 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | 6.80 | -6.76 | -4.50 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 5.55 | -4.73 | -3.40 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | 4.38 | -8.19 | -0.88 | BELOW_50_AND_200 |
| XHB | housing_rates | 3.06 | -1.51 | 1.80 | ABOVE_50_AND_200 |
| ITB | housing_rates | 2.56 | -1.80 | 2.46 | ABOVE_50_AND_200 |
| IWM | high_beta | 1.85 | 0.94 | 2.90 | ABOVE_50_AND_200 |
| TLT | rates | 0.77 | -3.08 | -2.49 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -10.07 | -2.66 | -7.65 | BELOW_50_AND_200 |
| USO | energy | -5.19 | 10.95 | -5.35 | BELOW_50_ABOVE_200 |
| PSQ | equity_hedges | -3.38 | -0.20 | -1.82 | BELOW_50_AND_200 |
| SH | equity_hedges | -1.77 | -2.25 | -3.35 | BELOW_50_AND_200 |
| TBT | rates | -1.47 | 6.09 | 4.09 | ABOVE_50_AND_200 |
| XOP | energy | -1.34 | 11.68 | 4.60 | ABOVE_50_AND_200 |
| TBF | rates | -0.83 | 3.15 | 2.11 | ABOVE_50_AND_200 |
| XLU | defensives | -0.56 | -2.63 | -1.90 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
