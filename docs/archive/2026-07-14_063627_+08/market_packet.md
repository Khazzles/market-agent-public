# Market Packet — 2026-07-14T06:36:27.648553+08:00

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
| SPY | 2026-07-13 | 749.17 | -0.77 | -0.28 | 3.27 | 0.97 | 7.81 | 54.24 | 1.21 | 0.00 | 0.67 | ABOVE_50_AND_200 |
| QQQ | 2026-07-13 | 711.74 | -1.90 | -1.53 | 2.60 | -0.62 | 11.46 | 47.73 | 2.16 | -0.67 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-07-13 | 656.73 | -1.86 | 9.40 | 15.02 | 9.42 | 2.26 | 62.78 | 3.96 | 11.75 | 12.42 | ABOVE_50_AND_200 |
| AMZN | 2026-07-13 | 247.31 | 0.80 | 1.29 | 3.91 | -2.53 | 5.93 | 52.91 | 3.06 | 0.64 | 1.31 | BELOW_50_ABOVE_200 |
| MU | 2026-07-13 | 937.00 | -4.32 | -4.85 | 5.06 | 3.26 | 100.07 | 46.19 | 9.21 | 1.79 | 2.46 | ABOVE_50_AND_200 |
| ORCL | 2026-07-13 | 131.54 | -6.47 | -8.50 | -34.64 | -27.89 | -32.48 | 26.91 | 6.88 | -37.91 | -37.24 | BELOW_50_AND_200 |
| SOFI | 2026-07-13 | 18.13 | -3.46 | -2.58 | 14.24 | 7.29 | -17.67 | 54.00 | 5.33 | 10.97 | 11.64 | MIXED |
| IAU | 2026-07-13 | 75.25 | -2.60 | -3.90 | -2.01 | -8.23 | -10.61 | 36.75 | 2.14 | -5.28 | -4.61 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-13 | 17.16 | 14.17 | 10.21 | -22.77 | -1.21 | BELOW_50_AND_200 |
| ^TNX | 2026-07-13 | 4.61 | 0.88 | 2.90 | 1.48 | 2.85 | ABOVE_50_AND_200 |
| CL=F | 2026-07-13 | 78.16 | 9.45 | 14.02 | -13.18 | -10.46 | BELOW_50_ABOVE_200 |
| GC=F | 2026-07-13 | 4011.30 | -2.26 | -3.46 | -2.36 | -8.05 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-13 | 101.28 | 0.30 | 0.42 | 1.33 | 1.54 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 5.18 | XLE, XOP, USO |
| semis_ai | -4.46 | SMH, SOXX |
| high_beta | -3.64 | IWM, ARKK, HIBL |
| rates | 0.45 | TLT, TBF, TBT |
| dollar | 0.39 | UUP |
| equity_hedges | 2.80 | SH, PSQ, SQQQ |
| housing_rates | -1.46 | XHB, ITB |
| defensives | 0.62 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| USO | energy | 8.36 | -12.29 | -7.82 | BELOW_50_ABOVE_200 |
| SQQQ | equity_hedges | 5.74 | -11.71 | -2.76 | BELOW_50_AND_200 |
| XOP | energy | 4.17 | -1.67 | 0.20 | ABOVE_50_AND_200 |
| XLE | energy | 3.01 | -2.59 | 0.06 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.93 | -3.53 | -0.20 | BELOW_50_AND_200 |
| TBT | rates | 1.35 | 1.35 | 2.66 | ABOVE_50_AND_200 |
| SH | equity_hedges | 0.73 | -3.91 | -1.35 | BELOW_50_AND_200 |
| XLU | defensives | 0.68 | 3.91 | 1.69 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -7.56 | 9.83 | -5.06 | BELOW_50_ABOVE_200 |
| SOXX | semis_ai | -4.77 | 2.23 | -1.19 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | -4.16 | 2.58 | -1.06 | BELOW_50_ABOVE_200 |
| ARKK | high_beta | -2.50 | 7.16 | 0.02 | ABOVE_50_AND_200 |
| ITB | housing_rates | -1.49 | 2.90 | 1.11 | MIXED |
| XHB | housing_rates | -1.42 | 3.47 | 1.42 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.85 | 4.05 | 1.53 | ABOVE_50_AND_200 |
| TLT | rates | -0.59 | -1.07 | -1.66 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
