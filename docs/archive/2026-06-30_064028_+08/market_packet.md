# Market Packet — 2026-06-30T06:40:28.648118+08:00

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
| SPY | 2026-06-29 | 741.00 | 1.65 | -0.46 | -1.80 | 0.80 | 7.24 | 51.54 | 1.42 | 0.00 | -0.24 | ABOVE_50_AND_200 |
| QQQ | 2026-06-29 | 724.08 | 2.49 | -1.88 | -1.57 | 2.78 | 14.41 | 52.78 | 2.29 | 0.24 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-06-29 | 562.60 | 2.24 | -0.22 | -11.44 | -7.86 | -13.32 | 42.48 | 3.33 | -9.64 | -9.88 | BELOW_50_AND_200 |
| AMZN | 2026-06-29 | 240.14 | 3.20 | 3.16 | -12.36 | -6.17 | 3.15 | 46.20 | 3.58 | -10.56 | -10.79 | BELOW_50_ABOVE_200 |
| MU | 2026-06-29 | 1145.28 | 1.14 | -5.46 | 24.01 | 40.37 | 165.81 | 59.55 | 8.50 | 25.81 | 25.58 | ABOVE_50_AND_200 |
| ORCL | 2026-06-29 | 147.76 | -0.52 | -15.60 | -27.46 | -21.60 | -26.94 | 29.34 | 7.50 | -25.66 | -25.90 | BELOW_50_AND_200 |
| SOFI | 2026-06-29 | 18.19 | 1.73 | 6.37 | 7.19 | 7.39 | -19.00 | 59.53 | 5.23 | 8.99 | 8.76 | MIXED |
| IAU | 2026-06-29 | 75.53 | -1.35 | -4.15 | -10.71 | -10.18 | -9.92 | 33.11 | 2.27 | -8.91 | -9.14 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-06-29 | 17.65 | -4.13 | 2.14 | 12.13 | -0.79 | BELOW_50_AND_200 |
| ^TNX | 2026-06-29 | 4.37 | 0.05 | -2.99 | -1.82 | -1.58 | BELOW_50_ABOVE_200 |
| CL=F | 2026-06-29 | 70.38 | 1.66 | -5.93 | -20.83 | -23.08 | BELOW_50_AND_200 |
| GC=F | 2026-06-29 | 4028.90 | -1.22 | -3.66 | -10.46 | -9.93 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-06-29 | 101.11 | -0.25 | 0.09 | 2.11 | 1.85 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.49 | XLE, XOP, USO |
| semis_ai | 3.73 | SMH, SOXX |
| high_beta | 2.93 | IWM, ARKK, HIBL |
| rates | -0.06 | TLT, TBF, TBT |
| dollar | -0.32 | UUP |
| equity_hedges | -3.88 | SH, PSQ, SQQQ |
| housing_rates | -0.55 | XHB, ITB |
| defensives | -0.40 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 5.89 | 5.64 | 16.90 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 4.14 | 7.88 | 14.92 | ABOVE_50_AND_200 |
| SMH | semis_ai | 3.33 | 5.36 | 10.88 | ABOVE_50_AND_200 |
| ARKK | high_beta | 3.20 | -0.47 | 4.01 | ABOVE_50_AND_200 |
| USO | energy | 1.52 | -18.12 | -18.90 | BELOW_50_ABOVE_200 |
| XOP | energy | 0.45 | -5.81 | -6.79 | BELOW_50_ABOVE_200 |
| TLT | rates | 0.10 | 1.99 | 2.07 | MIXED |
| TBF | rates | -0.08 | -2.65 | -2.44 | BELOW_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -7.63 | -0.81 | -13.23 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -2.53 | 0.32 | -3.84 | BELOW_50_AND_200 |
| SH | equity_hedges | -1.48 | 1.00 | -1.46 | BELOW_50_AND_200 |
| ITB | housing_rates | -0.89 | 11.58 | 9.33 | ABOVE_50_AND_200 |
| XLE | energy | -0.48 | -5.92 | -6.20 | BELOW_50_ABOVE_200 |
| XLP | defensives | -0.40 | -0.07 | 0.59 | ABOVE_50_AND_200 |
| XLU | defensives | -0.39 | 3.11 | 2.19 | ABOVE_50_AND_200 |
| UUP | dollar | -0.32 | 2.42 | 2.15 | ABOVE_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
