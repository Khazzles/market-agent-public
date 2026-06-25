# Market Packet — 2026-06-26T07:01:59.191448+08:00

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
| SPY | 2026-06-25 | 734.30 | 0.14 | -0.90 | -2.17 | 0.07 | 6.40 | 46.49 | 1.31 | 0.00 | -0.27 | ABOVE_50_AND_200 |
| QQQ | 2026-06-25 | 716.38 | 0.81 | -0.85 | -1.90 | 2.13 | 13.44 | 49.95 | 2.31 | 0.27 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-25 | 542.87 | -2.65 | -4.35 | -11.35 | -11.78 | -16.62 | 34.15 | 3.46 | -9.17 | -9.44 | BELOW_50_AND_200 |
| AMZN | 2026-06-25 | 227.01 | -3.10 | -4.42 | -14.43 | -11.48 | -2.49 | 33.63 | 3.50 | -12.26 | -12.53 | BELOW_50_AND_200 |
| MU | 2026-06-25 | 1213.56 | 15.74 | 16.33 | 35.46 | 53.88 | 188.36 | 64.54 | 7.86 | 37.63 | 37.36 | ABOVE_50_AND_200 |
| ORCL | 2026-06-25 | 152.46 | -3.22 | -16.93 | -21.03 | -19.55 | -25.12 | 30.85 | 7.65 | -18.86 | -19.13 | BELOW_50_AND_200 |
| SOFI | 2026-06-25 | 17.30 | -0.06 | -0.69 | 8.26 | 1.93 | -23.23 | 52.99 | 5.56 | 10.43 | 10.16 | MIXED |
| IAU | 2026-06-25 | 75.71 | 0.96 | -4.93 | -10.73 | -10.57 | -9.63 | 31.77 | 2.34 | -8.56 | -8.83 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-25 | 18.89 | 1.40 | 2.44 | 11.05 | 6.25 | ABOVE_50_AND_200 |
| ^TNX | 2026-06-25 | 4.39 | -1.33 | -2.12 | -3.94 | -0.87 | BELOW_50_ABOVE_200 |
| CL=F | 2026-06-25 | 71.45 | 1.58 | -6.95 | -23.90 | -22.69 | BELOW_50_AND_200 |
| GC=F | 2026-06-25 | 4039.40 | 1.23 | -7.33 | -10.24 | -10.29 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-25 | 101.44 | -0.17 | 1.35 | 2.29 | 2.31 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 1.64 | XLE, XOP, USO |
| semis_ai | 3.42 | SMH, SOXX |
| high_beta | 2.25 | IWM, ARKK, HIBL |
| rates | 0.08 | TLT, TBF, TBT |
| dollar | -0.18 | UUP |
| equity_hedges | -1.08 | SH, PSQ, SQQQ |
| housing_rates | 1.17 | XHB, ITB |
| defensives | 0.04 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 6.22 | 13.33 | 22.13 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 3.94 | 9.67 | 18.71 | ABOVE_50_AND_200 |
| SMH | semis_ai | 2.90 | 5.77 | 13.07 | ABOVE_50_AND_200 |
| USO | energy | 2.84 | -20.21 | -17.66 | BELOW_50_ABOVE_200 |
| XHB | housing_rates | 1.44 | 13.27 | 10.74 | ABOVE_50_AND_200 |
| XOP | energy | 1.12 | -6.84 | -7.41 | BELOW_50_ABOVE_200 |
| XLE | energy | 0.97 | -6.50 | -5.47 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | 0.90 | 13.20 | 10.12 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -2.42 | 0.48 | -11.80 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.81 | 0.70 | -3.30 | BELOW_50_AND_200 |
| XLP | defensives | -0.59 | 0.37 | 0.24 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.23 | -0.89 | -1.16 | BELOW_50_AND_200 |
| UUP | dollar | -0.18 | 2.63 | 2.71 | ABOVE_50_AND_200 |
| TLT | rates | -0.03 | 2.64 | 1.99 | MIXED |
| SH | equity_hedges | 0.00 | 1.45 | -0.68 | BELOW_50_AND_200 |
| TBF | rates | 0.08 | -3.19 | -2.37 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
