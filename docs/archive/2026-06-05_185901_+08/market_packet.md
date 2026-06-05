# Market Packet — 2026-06-05T18:59:01.886130+08:00

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
| SPY | 2026-06-04 | 757.09 | 0.38 | 0.33 | 4.60 | 6.35 | 10.78 | 69.69 | 0.86 | 0.00 | -4.05 | ABOVE_50_AND_200 |
| QQQ | 2026-06-04 | 740.61 | -0.48 | 0.68 | 8.66 | 11.29 | 19.23 | 73.52 | 1.35 | 4.05 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-03 | 622.98 | 4.24 | -1.93 | 2.06 | 0.66 | -6.17 | 51.45 | 2.81 | -2.54 | -6.60 | MIXED |
| AMZN | 2026-06-04 | 253.79 | 1.51 | -7.38 | -7.22 | 1.32 | 9.37 | 43.50 | 2.74 | -11.83 | -15.88 | ABOVE_50_AND_200 |
| MU | 2026-06-04 | 996.00 | -7.74 | 7.85 | 55.58 | 63.89 | 178.88 | 69.65 | 6.09 | 50.97 | 46.92 | ABOVE_50_AND_200 |
| ORCL | 2026-06-04 | 236.34 | 2.61 | 16.02 | 27.51 | 32.65 | 14.24 | 68.92 | 4.83 | 22.91 | 18.85 | ABOVE_50_AND_200 |
| SOFI | 2026-06-03 | 16.68 | -5.98 | 3.15 | 2.96 | -0.40 | -27.87 | 49.65 | 5.46 | -1.64 | -5.69 | BELOW_50_AND_200 |
| IAU | 2026-06-04 | 84.28 | 0.83 | -0.37 | -1.65 | -3.22 | 1.80 | 42.38 | 1.78 | -6.25 | -10.30 | BELOW_50_ABOVE_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-05 | 15.63 | 1.49 | 2.02 | -8.49 | -17.20 | BELOW_50_AND_200 |
| ^TNX | 2026-06-04 | 4.48 | -0.31 | 0.49 | 1.38 | 1.77 | ABOVE_50_AND_200 |
| CL=F | 2026-06-05 | 93.09 | 0.05 | 6.56 | -2.09 | -4.93 | BELOW_50_ABOVE_200 |
| GC=F | 2026-06-05 | 4492.60 | 0.38 | -1.49 | -4.04 | -2.91 | BELOW_50_ABOVE_200 |
| DX-Y.NYB | 2026-06-05 | 99.19 | -0.23 | 0.28 | 1.19 | 0.30 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | -0.97 | XLE, XOP, USO |
| semis_ai | -1.87 | SMH, SOXX |
| high_beta | -0.98 | IWM, ARKK, HIBL |
| rates | -0.17 | TLT, TBF, TBT |
| dollar | -0.07 | UUP |
| equity_hedges | 0.54 | SH, PSQ, SQQQ |
| housing_rates | 0.90 | XHB, ITB |
| defensives | 0.19 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 1.53 | -22.29 | -30.88 | BELOW_50_AND_200 |
| IWM | high_beta | 1.51 | 3.34 | 6.76 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.99 | 0.61 | 0.29 | MIXED |
| XHB | housing_rates | 0.80 | 1.86 | 2.23 | MIXED |
| XLU | defensives | 0.53 | -5.24 | -3.38 | BELOW_50_AND_200 |
| PSQ | equity_hedges | 0.48 | -7.75 | -10.50 | BELOW_50_AND_200 |
| TLT | rates | 0.22 | 0.08 | -0.38 | BELOW_50_AND_200 |
| XLE | energy | 0.07 | -1.18 | 0.93 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | -2.92 | -5.15 | 1.68 | ABOVE_50_AND_200 |
| HIBL | high_beta | -2.25 | 38.56 | 44.28 | ABOVE_50_AND_200 |
| ARKK | high_beta | -2.19 | -0.09 | 4.25 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -2.10 | 24.86 | 31.45 | ABOVE_50_AND_200 |
| SMH | semis_ai | -1.63 | 20.06 | 24.63 | ABOVE_50_AND_200 |
| TBT | rates | -0.50 | -0.56 | 0.12 | ABOVE_50_AND_200 |
| SH | equity_hedges | -0.39 | -3.97 | -5.75 | BELOW_50_AND_200 |
| TBF | rates | -0.24 | -0.08 | 0.25 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
