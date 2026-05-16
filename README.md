# Market Agent — Data-Only Public Research Packet

This repository generates a public market research packet without using the OpenAI API.

It is designed to be used as a data/evidence layer for a ChatGPT scheduled task or manual ChatGPT analysis.

## What it does

The GitHub Actions workflow runs after the US market close and generates:

```text
docs/latest/manifest.json
docs/latest/evidence_ledger.json
docs/latest/technicals.json
docs/latest/market_packet.md
docs/archive/<run_timestamp>/...
```

The packet includes:

- Core universe prices and daily moves
- SMA20 / SMA50 / SMA100 / SMA200
- EMA20
- RSI14
- ATR14
- 5D / 21D / 63D returns
- Relative strength vs SPY and QQQ
- Factor adjacency winners and losers
- Macro proxy evidence

## What it deliberately does not include

- Portfolio size
- Holdings
- Position sizes
- Cost basis
- Private thesis notes
- Account data
- Trade execution instructions
- OpenAI API calls

This repo is safe to make public only if you keep it limited to public market data and neutral watchlist research.

## Manual run

On GitHub:

1. Open the repository.
2. Click **Actions**.
3. Select **Daily Market Packet**.
4. Click **Run workflow**.

## Schedule

The workflow runs at:

```text
21:45 UTC Monday-Friday
05:45 Malaysia/Singapore time Tuesday-Saturday
```

This is intended to run after the prior US market close.

## Public raw URLs

Once the repository is public, the latest files should be accessible at:

```text
https://raw.githubusercontent.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/main/docs/latest/market_packet.md
https://raw.githubusercontent.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/main/docs/latest/evidence_ledger.json
https://raw.githubusercontent.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/main/docs/latest/technicals.json
```

Replace `<YOUR_GITHUB_USERNAME>` and `<YOUR_REPO_NAME>` with your actual GitHub username and repository name.

## ChatGPT scheduled task prompt

Use a task prompt like this:

```text
Open the latest public market packet:
[RAW_URL_TO_market_packet.md]
[RAW_URL_TO_evidence_ledger.json]
[RAW_URL_TO_technicals.json]

Run the Supervised Market Research Pipeline using the packet as the evidence layer.

Rules:
- Treat the GitHub packet as public market evidence only.
- Do not infer portfolio size, holdings, cost basis, or private positions.
- Mark stale or missing data as UNK.
- Run ENUM, factor decomposition, core universe analysis, adjacency scan, cross-impact map, asymmetry engine, red team, supervisor QC, close loops, and final decision matrix.
- No recommendation without downside, invalidation, and opportunity-cost comparison versus SPY, QQQ, and cash.
```

## Notes

This is a research automation layer, not trading infrastructure. Scheduled GitHub Actions are not guaranteed to run at the exact minute, and this workflow should not be used for real-time execution.
