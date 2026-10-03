# Market Packet — 2026-10-03T08:43:47.213685+08:00

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
| SPY | 2026-10-01 | 763.99 | 0.18 | -0.42 | 0.29 | 0.12 | 6.11 | 49.19 | 0.89 | 0.00 | -4.57 | ABOVE_50_AND_200 |
| QQQ | 2026-10-01 | 742.03 | 0.31 | 0.13 | 4.86 | 3.68 | 11.10 | 61.47 | 1.28 | 4.57 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-10-01 | 725.93 | 0.10 | -6.64 | 25.48 | 16.60 | 15.60 | 61.11 | 3.50 | 25.19 | 20.62 | ABOVE_50_AND_200 |
| AMZN | 2026-10-01 | 248.23 | -0.37 | -0.46 | -2.62 | -3.11 | 2.91 | 44.20 | 2.27 | -2.91 | -7.48 | BELOW_50_ABOVE_200 |
| MU | 2026-10-01 | 1097.39 | 3.03 | 1.56 | 17.56 | 14.99 | 61.99 | 63.52 | 4.24 | 17.27 | 12.70 | ABOVE_50_AND_200 |
| ORCL | 2026-10-01 | 138.07 | 0.56 | -1.05 | -2.30 | -3.55 | -15.35 | 43.56 | 4.98 | -2.59 | -7.16 | BELOW_50_AND_200 |
| SOFI | 2026-10-01 | 15.84 | 0.76 | -5.71 | -7.10 | -9.34 | -16.60 | 36.79 | 4.03 | -7.39 | -11.96 | BELOW_50_AND_200 |
| IAU | 2026-10-01 | 78.47 | 0.47 | -2.28 | -3.54 | -3.36 | -7.99 | 40.40 | 1.81 | -3.83 | -8.40 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-10-02 | 15.31 | -6.59 | 2.96 | 6.91 | -3.00 | BELOW_50_AND_200 |
| ^TNX | 2026-10-02 | 5.28 | 0.76 | 1.79 | 10.03 | 9.21 | ABOVE_50_AND_200 |
| CL=F | 2026-10-02 | 91.26 | -1.73 | -1.24 | 0.27 | 3.03 | ABOVE_50_AND_200 |
| GC=F | 2026-10-02 | 4172.10 | -0.72 | -3.45 | -5.49 | -4.45 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-10-02 | 101.92 | -0.17 | 0.94 | 2.37 | 1.92 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 2.57 | XLE, XOP, USO |
| semis_ai | 1.40 | SMH, SOXX |
| high_beta | 1.26 | IWM, ARKK, HIBL |
| rates | -0.40 | TLT, TBF, TBT |
| dollar | 0.66 | UUP |
| equity_hedges | -0.47 | SH, PSQ, SQQQ |
| housing_rates | 0.59 | XHB, ITB |
| defensives | 0.14 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 3.96 | 18.40 | 9.30 | ABOVE_50_AND_200 |
| USO | energy | 2.99 | 6.40 | 9.34 | ABOVE_50_AND_200 |
| XOP | energy | 2.77 | -4.37 | 0.74 | ABOVE_50_AND_200 |
| XLE | energy | 1.95 | -3.20 | 1.05 | ABOVE_50_AND_200 |
| SMH | semis_ai | 1.45 | 13.31 | 8.61 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 1.35 | 15.19 | 8.95 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.78 | -3.76 | -6.37 | BELOW_50_AND_200 |
| UUP | dollar | 0.66 | 2.66 | 2.49 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -0.87 | -14.66 | -12.06 | BELOW_50_AND_200 |
| TBT | rates | -0.71 | 9.67 | 9.05 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.58 | 6.62 | 7.11 | ABOVE_50_AND_200 |
| TBF | rates | -0.41 | 4.62 | 4.44 | ABOVE_50_AND_200 |
| XLP | defensives | -0.34 | -5.77 | -4.87 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.32 | -5.43 | -4.21 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.22 | -1.07 | -0.64 | BELOW_50_AND_200 |
| TLT | rates | -0.09 | -5.08 | -4.98 | BELOW_50_AND_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
