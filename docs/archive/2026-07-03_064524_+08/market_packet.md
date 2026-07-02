# Market Packet — 2026-07-03T06:45:24.342697+08:00

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
| SPY | 2026-07-02 | 744.78 | -0.13 | 1.43 | -1.95 | 1.00 | 7.58 | 53.50 | 1.36 | 0.00 | 2.55 | ABOVE_50_AND_200 |
| QQQ | 2026-07-02 | 712.60 | -1.73 | -0.53 | -4.50 | 0.49 | 12.23 | 48.12 | 2.32 | -2.55 | 0.00 | ABOVE_50_AND_200 |
| META | 2026-07-02 | 582.90 | -4.90 | 7.37 | -2.46 | -3.69 | -9.84 | 49.60 | 3.86 | -0.52 | 2.03 | BELOW_50_AND_200 |
| AMZN | 2026-07-02 | 242.67 | 0.40 | 6.90 | -5.40 | -4.99 | 4.16 | 48.70 | 3.38 | -3.45 | -0.90 | BELOW_50_ABOVE_200 |
| MU | 2026-07-02 | 975.56 | -5.49 | -19.61 | -8.32 | 14.49 | 119.55 | 48.47 | 9.93 | -6.37 | -3.82 | ABOVE_50_AND_200 |
| ORCL | 2026-07-02 | 140.27 | -1.56 | -8.00 | -42.65 | -24.74 | -29.82 | 26.72 | 7.23 | -40.70 | -38.15 | BELOW_50_AND_200 |
| SOFI | 2026-07-02 | 18.24 | -1.08 | 5.43 | 2.82 | 8.09 | -18.32 | 58.48 | 5.24 | 4.77 | 7.32 | MIXED |
| IAU | 2026-07-02 | 77.51 | 2.04 | 2.38 | -8.19 | -6.92 | -7.68 | 42.06 | 2.19 | -6.24 | -3.69 | BELOW_50_AND_200 |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-07-02 | 16.15 | -2.65 | -14.51 | 2.41 | -8.39 | BELOW_50_AND_200 |
| ^TNX | 2026-07-02 | 4.49 | 2.58 | -0.53 | 0.67 | 0.86 | ABOVE_50_AND_200 |
| CL=F | 2026-07-02 | 68.52 | -0.09 | -4.73 | -26.92 | -24.14 | BELOW_50_AND_200 |
| GC=F | 2026-07-02 | 4138.10 | 1.72 | 2.67 | -7.82 | -6.59 | BELOW_50_AND_200 |
| DX-Y.NYB | 2026-07-02 | 100.85 | -0.53 | -0.57 | 1.64 | 1.40 | ABOVE_50_AND_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.68 | XLE, XOP, USO |
| semis_ai | -5.05 | SMH, SOXX |
| high_beta | -3.15 | IWM, ARKK, HIBL |
| rates | -0.01 | TLT, TBF, TBT |
| dollar | -0.53 | UUP |
| equity_hedges | 2.52 | SH, PSQ, SQQQ |
| housing_rates | 0.34 | XHB, ITB |
| defensives | 2.12 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | 5.46 | 8.24 | -6.75 | BELOW_50_AND_200 |
| XLU | defensives | 2.21 | 4.24 | 1.66 | ABOVE_50_AND_200 |
| XLP | defensives | 2.03 | 3.86 | 1.22 | ABOVE_50_AND_200 |
| PSQ | equity_hedges | 1.89 | 3.39 | -1.51 | BELOW_50_AND_200 |
| XLE | energy | 0.78 | -8.18 | -6.61 | BELOW_50_ABOVE_200 |
| ITB | housing_rates | 0.74 | 10.35 | 7.94 | ABOVE_50_AND_200 |
| USO | energy | 0.69 | -24.25 | -20.62 | BELOW_50_ABOVE_200 |
| XOP | energy | 0.58 | -8.42 | -6.97 | BELOW_50_ABOVE_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | -8.15 | -14.48 | 2.71 | ABOVE_50_AND_200 |
| SOXX | semis_ai | -5.57 | -6.40 | 3.79 | ABOVE_50_AND_200 |
| SMH | semis_ai | -4.54 | -6.31 | 2.21 | ABOVE_50_AND_200 |
| ARKK | high_beta | -0.73 | 1.68 | 4.60 | ABOVE_50_AND_200 |
| IWM | high_beta | -0.58 | 2.03 | 3.84 | ABOVE_50_AND_200 |
| UUP | dollar | -0.53 | 2.09 | 1.82 | ABOVE_50_AND_200 |
| XHB | housing_rates | -0.06 | 7.90 | 6.70 | ABOVE_50_AND_200 |
| TBT | rates | -0.03 | -0.65 | -1.02 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
