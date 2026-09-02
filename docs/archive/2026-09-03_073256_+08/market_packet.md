# Market Packet — 2026-09-03T07:32:56.380395+08:00

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
| SPY | 2026-09-02 | 765.16 | 0.44 | -0.12 | -0.80 | 1.30 | 7.60 | 51.93 | 0.81 | 0.00 | 1.22 | ABOVE_50_AND_200 |
| QQQ | 2026-09-02 | 709.24 | 0.23 | -0.30 | -2.02 | -0.23 | 8.02 | 47.61 | 1.38 | -1.22 | 0.00 | BELOW_50_ABOVE_200 |
| META | 2026-09-02 | 592.85 | 2.47 | 2.90 | 0.84 | -0.02 | -4.72 | 55.18 | 3.41 | 1.64 | 2.85 | BELOW_50_AND_200 |
| AMZN | 2026-09-02 | 254.98 | 0.02 | -2.04 | -8.09 | 0.85 | 6.74 | 46.38 | 2.72 | -7.29 | -6.07 | ABOVE_50_AND_200 |
| MU | 2026-09-02 | 956.08 | 2.43 | 1.88 | 7.10 | 1.28 | 59.60 | 53.23 | 5.81 | 7.90 | 9.12 | ABOVE_50_AND_200 |
| ORCL | 2026-09-02 | 145.75 | 3.13 | -2.10 | 0.01 | 4.27 | -13.98 | 50.69 | 4.49 | 0.81 | 2.03 | MIXED |
| SOFI | 2026-09-02 | 17.84 | 4.63 | -5.31 | -4.60 | 0.01 | -11.07 | 48.83 | 4.90 | -3.80 | -2.58 | MIXED |
| IAU | 2026-09-02 | 82.55 | 1.48 | -5.94 | 8.35 | 4.18 | -2.90 | 50.41 | 2.01 | 9.15 | 10.37 | MIXED |


## Macro Proxy Evidence

| Proxy | As Of | Close | 1D % | 5D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^VIX | 2026-09-02 | 15.20 | -6.98 | -1.62 | -4.16 | -7.74 | BELOW_50_AND_200 |
| ^TNX | 2026-09-02 | 4.80 | 0.00 | 3.38 | 2.35 | 3.95 | ABOVE_50_AND_200 |
| CL=F | 2026-09-02 | 90.71 | 0.54 | 10.31 | 19.72 | 13.19 | ABOVE_50_AND_200 |
| GC=F | 2026-09-02 | 4427.80 | 1.84 | -3.71 | 8.12 | 4.87 | MIXED |
| DX-Y.NYB | 2026-09-02 | 99.58 | -0.09 | 0.66 | -0.38 | -0.79 | BELOW_50_ABOVE_200 |


## Factor Group Evidence

| Group | Avg 1D % | Members |
| --- | --- | --- |
| energy | 0.28 | XLE, XOP, USO |
| semis_ai | 0.60 | SMH, SOXX |
| high_beta | 1.33 | IWM, ARKK, HIBL |
| rates | 0.22 | TLT, TBF, TBT |
| dollar | -0.14 | UUP |
| equity_hedges | -0.42 | SH, PSQ, SQQQ |
| housing_rates | 0.55 | XHB, ITB |
| defensives | 0.29 | XLP, XLU |


## Top Adjacent Daily Winners

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| HIBL | high_beta | 2.42 | -0.50 | -7.97 | BELOW_50_ABOVE_200 |
| IWM | high_beta | 1.18 | -0.75 | -1.04 | BELOW_50_ABOVE_200 |
| SMH | semis_ai | 0.96 | 0.92 | -4.77 | BELOW_50_ABOVE_200 |
| TBT | rates | 0.68 | 1.47 | 4.46 | ABOVE_50_AND_200 |
| XHB | housing_rates | 0.61 | -4.88 | -6.61 | BELOW_50_AND_200 |
| XLE | energy | 0.51 | 11.24 | 10.75 | ABOVE_50_AND_200 |
| ITB | housing_rates | 0.50 | -4.32 | -5.57 | BELOW_50_AND_200 |
| ARKK | high_beta | 0.37 | 13.39 | 5.30 | ABOVE_50_AND_200 |


## Top Adjacent Daily Losers

| Ticker | Group | 1D % | 21D % | vs SMA50 % | Regime |
| --- | --- | --- | --- | --- | --- |
| SQQQ | equity_hedges | -0.65 | 6.58 | -0.45 | BELOW_50_AND_200 |
| SH | equity_hedges | -0.43 | -0.46 | -0.86 | BELOW_50_AND_200 |
| PSQ | equity_hedges | -0.19 | -0.95 | 0.47 | MIXED |
| UUP | dollar | -0.14 | 0.00 | -0.34 | BELOW_50_ABOVE_200 |
| TBF | rates | -0.12 | 0.35 | 1.99 | ABOVE_50_AND_200 |
| TLT | rates | 0.10 | -0.29 | -2.08 | BELOW_50_AND_200 |
| USO | energy | 0.11 | 21.91 | 15.22 | ABOVE_50_AND_200 |
| SOXX | semis_ai | 0.23 | -7.52 | -7.55 | BELOW_50_ABOVE_200 |


## Downstream Manager Prompt

Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.
