from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yaml
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "universe.yaml"
DOCS_LATEST = ROOT / "docs" / "latest"
DOCS_ARCHIVE = ROOT / "docs" / "archive"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def flatten_universe(config: dict) -> dict[str, list[str]]:
    core = list(config.get("core_universe", []))
    factors_by_group = config.get("factor_adjacency", {}) or {}
    macro_by_group = config.get("macro_proxies", {}) or {}

    factors = []
    for tickers in factors_by_group.values():
        factors.extend(tickers)

    macros = []
    for tickers in macro_by_group.values():
        macros.extend(tickers)

    all_tickers = []
    seen = set()
    for ticker in core + factors + macros:
        if ticker not in seen:
            all_tickers.append(ticker)
            seen.add(ticker)

    return {"core": core, "factors": factors, "macros": macros, "all": all_tickers}


def safe_float(x):
    if x is None:
        return None
    try:
        if pd.isna(x):
            return None
        value = float(x)
        if math.isnan(value) or math.isinf(value):
            return None
        return round(value, 4)
    except Exception:
        return None


def safe_pct(x):
    value = safe_float(x)
    if value is None:
        return None
    return round(value, 4)


def download_history(ticker: str, period: str) -> pd.DataFrame:
    try:
        df = yf.download(
            ticker,
            period=period,
            interval="1d",
            progress=False,
            auto_adjust=False,
            threads=False,
        )
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    # yfinance sometimes returns multi-index columns even for one ticker.
    if isinstance(df.columns, pd.MultiIndex):
        try:
            df.columns = df.columns.get_level_values(0)
        except Exception:
            pass

    df = df.dropna(how="all")
    return df


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out = 100 - (100 / (1 + rs))
    return out


def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high = df["High"]
    low = df["Low"]
    close = df["Close"]
    prev_close = close.shift(1)
    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return tr.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()


def last_return(close: pd.Series, periods: int) -> float | None:
    close = close.dropna()
    if len(close) <= periods:
        return None
    start = close.iloc[-periods - 1]
    end = close.iloc[-1]
    if start == 0 or pd.isna(start) or pd.isna(end):
        return None
    return float((end / start - 1) * 100)


def compute_ticker_metrics(ticker: str, df: pd.DataFrame) -> dict:
    required = {"Open", "High", "Low", "Close", "Volume"}
    missing_cols = sorted(list(required - set(df.columns)))
    if df.empty or missing_cols:
        return {
            "ticker": ticker,
            "status": "MISSING_DATA",
            "missing_columns": missing_cols,
        }

    close = df["Close"].dropna()
    if close.empty:
        return {"ticker": ticker, "status": "MISSING_CLOSE"}

    latest_date = close.index[-1]
    latest_close = close.iloc[-1]
    prev_close = close.iloc[-2] if len(close) > 1 else np.nan
    daily_change_pct = ((latest_close / prev_close - 1) * 100) if prev_close and not pd.isna(prev_close) else np.nan

    sma_20 = close.rolling(20).mean().iloc[-1] if len(close) >= 20 else np.nan
    sma_50 = close.rolling(50).mean().iloc[-1] if len(close) >= 50 else np.nan
    sma_100 = close.rolling(100).mean().iloc[-1] if len(close) >= 100 else np.nan
    sma_200 = close.rolling(200).mean().iloc[-1] if len(close) >= 200 else np.nan
    ema_20 = close.ewm(span=20, adjust=False).mean().iloc[-1] if len(close) >= 20 else np.nan
    rsi_14 = rsi(close, 14).iloc[-1] if len(close) >= 20 else np.nan
    atr_14 = atr(df, 14).iloc[-1] if len(close) >= 20 else np.nan

    def pct_vs(level):
        if pd.isna(level) or level == 0:
            return None
        return float((latest_close / level - 1) * 100)

    technical_regime = "UNK"
    if not pd.isna(sma_50) and not pd.isna(sma_200):
        if latest_close > sma_50 and latest_close > sma_200:
            technical_regime = "ABOVE_50_AND_200"
        elif latest_close < sma_50 and latest_close > sma_200:
            technical_regime = "BELOW_50_ABOVE_200"
        elif latest_close < sma_50 and latest_close < sma_200:
            technical_regime = "BELOW_50_AND_200"
        else:
            technical_regime = "MIXED"

    return {
        "ticker": ticker,
        "status": "OK",
        "as_of": latest_date.strftime("%Y-%m-%d"),
        "close": safe_float(latest_close),
        "prev_close": safe_float(prev_close),
        "daily_change_pct": safe_pct(daily_change_pct),
        "volume": int(df["Volume"].dropna().iloc[-1]) if not df["Volume"].dropna().empty else None,
        "sma_20": safe_float(sma_20),
        "sma_50": safe_float(sma_50),
        "sma_100": safe_float(sma_100),
        "sma_200": safe_float(sma_200),
        "ema_20": safe_float(ema_20),
        "rsi_14": safe_float(rsi_14),
        "atr_14": safe_float(atr_14),
        "atr_14_pct_of_close": safe_pct((atr_14 / latest_close) * 100 if latest_close and not pd.isna(atr_14) else np.nan),
        "return_5d_pct": safe_pct(last_return(close, 5)),
        "return_21d_pct": safe_pct(last_return(close, 21)),
        "return_63d_pct": safe_pct(last_return(close, 63)),
        "pct_vs_sma_20": safe_pct(pct_vs(sma_20)),
        "pct_vs_sma_50": safe_pct(pct_vs(sma_50)),
        "pct_vs_sma_100": safe_pct(pct_vs(sma_100)),
        "pct_vs_sma_200": safe_pct(pct_vs(sma_200)),
        "technical_regime": technical_regime,
        "data_points": int(len(close)),
        "source": "yfinance",
    }


def add_relative_strength(metrics: dict, benchmark: str, label: str):
    bench = metrics.get(benchmark, {})
    for ticker, data in metrics.items():
        if data.get("status") != "OK" or bench.get("status") != "OK":
            data[f"rs_vs_{label}_21d_pct"] = None
            data[f"rs_vs_{label}_63d_pct"] = None
            continue
        r21 = data.get("return_21d_pct")
        b21 = bench.get("return_21d_pct")
        r63 = data.get("return_63d_pct")
        b63 = bench.get("return_63d_pct")
        data[f"rs_vs_{label}_21d_pct"] = safe_pct((r21 - b21) if r21 is not None and b21 is not None else None)
        data[f"rs_vs_{label}_63d_pct"] = safe_pct((r63 - b63) if r63 is not None and b63 is not None else None)


def classify_factor_groups(config: dict, metrics: dict) -> dict:
    groups = config.get("factor_adjacency", {}) or {}
    out = {}
    flat_rows = []
    for group, tickers in groups.items():
        rows = []
        for t in tickers:
            d = metrics.get(t, {})
            row = {
                "ticker": t,
                "group": group,
                "status": d.get("status", "MISSING"),
                "daily_change_pct": d.get("daily_change_pct"),
                "return_5d_pct": d.get("return_5d_pct"),
                "return_21d_pct": d.get("return_21d_pct"),
                "pct_vs_sma_50": d.get("pct_vs_sma_50"),
                "pct_vs_sma_200": d.get("pct_vs_sma_200"),
                "technical_regime": d.get("technical_regime"),
            }
            rows.append(row)
            flat_rows.append(row)
        valid = [r for r in rows if r.get("daily_change_pct") is not None]
        avg_1d = np.mean([r["daily_change_pct"] for r in valid]) if valid else None
        out[group] = {
            "average_daily_change_pct": safe_pct(avg_1d),
            "members": rows,
        }

    ranked = sorted([r for r in flat_rows if r.get("daily_change_pct") is not None], key=lambda r: r["daily_change_pct"], reverse=True)
    return {
        "groups": out,
        "top_daily_winners": ranked[:8],
        "top_daily_losers": ranked[-8:][::-1],
    }


def md_table(rows: list[dict], columns: list[tuple[str, str]]) -> str:
    if not rows:
        return "_No data._\n"
    header = "| " + " | ".join(label for _, label in columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, sep]
    for row in rows:
        vals = []
        for key, _ in columns:
            v = row.get(key)
            if v is None:
                vals.append("UNK")
            elif isinstance(v, float):
                vals.append(f"{v:.2f}")
            else:
                vals.append(str(v))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines) + "\n"


def render_market_packet(config: dict, manifest: dict, metrics: dict, factor_summary: dict) -> str:
    core = config.get("core_universe", [])
    macro = flatten_universe(config)["macros"]

    core_rows = [metrics.get(t, {"ticker": t, "status": "MISSING"}) for t in core]
    macro_rows = [metrics.get(t, {"ticker": t, "status": "MISSING"}) for t in macro]

    factor_rows = []
    for group, payload in factor_summary.get("groups", {}).items():
        factor_rows.append({
            "group": group,
            "average_daily_change_pct": payload.get("average_daily_change_pct"),
            "members": ", ".join([m.get("ticker", "") for m in payload.get("members", [])]),
        })

    stale = []
    run_as_of = manifest["run_date_local"][:10]
    for ticker, data in metrics.items():
        if data.get("status") != "OK":
            stale.append(f"{ticker}: {data.get('status')}")
        elif data.get("as_of") and data.get("as_of") > run_as_of:
            # futures / timezone edge; not an error
            pass

    lines = []
    lines.append(f"# Market Packet — {manifest['run_timestamp_local']}\n")
    lines.append("## Manifest\n")
    lines.append(f"- AS_OF policy: latest available market close per yfinance.\n")
    lines.append(f"- Run timezone: {manifest['timezone']}\n")
    lines.append(f"- Objective: public research packet only; no portfolio sizes, holdings, cost basis, or private notes.\n")
    lines.append(f"- Core universe: {', '.join(core)}\n")
    lines.append("- Data source: yfinance for market prices and OHLCV-derived indicators.\n")
    lines.append("- Interpretation layer: intended for downstream ChatGPT manager/supervisor review.\n")

    lines.append("\n## Data Status\n")
    if stale:
        lines.append("Potential issues:\n")
        for item in stale:
            lines.append(f"- {item}\n")
    else:
        lines.append("No missing ticker metrics detected in this run.\n")

    lines.append("\n## Core Universe Technical Evidence\n")
    lines.append(md_table(core_rows, [
        ("ticker", "Ticker"),
        ("as_of", "As Of"),
        ("close", "Close"),
        ("daily_change_pct", "1D %"),
        ("return_5d_pct", "5D %"),
        ("return_21d_pct", "21D %"),
        ("pct_vs_sma_50", "vs SMA50 %"),
        ("pct_vs_sma_200", "vs SMA200 %"),
        ("rsi_14", "RSI14"),
        ("atr_14_pct_of_close", "ATR14 %"),
        ("rs_vs_SPY_21d_pct", "RS vs SPY 21D"),
        ("rs_vs_QQQ_21d_pct", "RS vs QQQ 21D"),
        ("technical_regime", "Regime"),
    ]))

    lines.append("\n## Macro Proxy Evidence\n")
    lines.append(md_table(macro_rows, [
        ("ticker", "Proxy"),
        ("as_of", "As Of"),
        ("close", "Close"),
        ("daily_change_pct", "1D %"),
        ("return_5d_pct", "5D %"),
        ("return_21d_pct", "21D %"),
        ("pct_vs_sma_50", "vs SMA50 %"),
        ("technical_regime", "Regime"),
    ]))

    lines.append("\n## Factor Group Evidence\n")
    lines.append(md_table(factor_rows, [
        ("group", "Group"),
        ("average_daily_change_pct", "Avg 1D %"),
        ("members", "Members"),
    ]))

    lines.append("\n## Top Adjacent Daily Winners\n")
    lines.append(md_table(factor_summary.get("top_daily_winners", []), [
        ("ticker", "Ticker"),
        ("group", "Group"),
        ("daily_change_pct", "1D %"),
        ("return_21d_pct", "21D %"),
        ("pct_vs_sma_50", "vs SMA50 %"),
        ("technical_regime", "Regime"),
    ]))

    lines.append("\n## Top Adjacent Daily Losers\n")
    lines.append(md_table(factor_summary.get("top_daily_losers", []), [
        ("ticker", "Ticker"),
        ("group", "Group"),
        ("daily_change_pct", "1D %"),
        ("return_21d_pct", "21D %"),
        ("pct_vs_sma_50", "vs SMA50 %"),
        ("technical_regime", "Regime"),
    ]))

    lines.append("\n## Downstream Manager Prompt\n")
    lines.append("Use this packet as evidence only. Run ENUM, factor decomposition, current-universe analysis, adjacency scan, cross-impact map, asymmetry engine, red-team, supervisor QC, close loops, and final decision matrix. Mark stale/missing data as UNK. Do not infer portfolio sizes or holdings.\n")
    return "\n".join(lines)


def main():
    config = load_config()
    settings = config.get("settings", {})
    tz_name = settings.get("report_timezone", "Asia/Kuala_Lumpur")
    tz = ZoneInfo(tz_name)
    now_local = datetime.now(tz)
    run_slug = now_local.strftime("%Y-%m-%d_%H%M%S_%Z")
    run_archive = DOCS_ARCHIVE / run_slug
    run_archive.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST.mkdir(parents=True, exist_ok=True)

    universe = flatten_universe(config)
    period = settings.get("history_period", "18mo")
    metrics = {}

    for ticker in universe["all"]:
        df = download_history(ticker, period=period)
        metrics[ticker] = compute_ticker_metrics(ticker, df)

    add_relative_strength(metrics, settings.get("benchmark_primary", "SPY"), "SPY")
    add_relative_strength(metrics, settings.get("benchmark_growth", "QQQ"), "QQQ")

    factor_summary = classify_factor_groups(config, metrics)

    manifest = {
        "run_timestamp_local": now_local.isoformat(),
        "run_date_local": now_local.strftime("%Y-%m-%d"),
        "timezone": tz_name,
        "objective": "Public market research packet only; no portfolio sizes, holdings, cost basis, or private notes.",
        "core_universe": universe["core"],
        "factor_adjacency": config.get("factor_adjacency", {}),
        "macro_proxies": config.get("macro_proxies", {}),
        "data_source": "yfinance",
        "limitations": [
            "No OpenAI API or LLM analysis in GitHub workflow.",
            "No private portfolio data by design.",
            "News, filings, EPS revisions, and options data are not included in this MVP packet.",
            "Scheduled GitHub Actions are suitable for research automation, not execution timing."
        ],
    }

    evidence = {
        "manifest": manifest,
        "metrics": metrics,
        "factor_summary": factor_summary,
    }

    technicals = {
        "manifest": manifest,
        "metrics": metrics,
        "calculation_notes": {
            "sma": "Simple moving average over N daily closes.",
            "ema20": "20-day exponential moving average over daily closes.",
            "rsi14": "Wilder-style RSI approximation using exponential smoothing.",
            "atr14": "Average True Range using exponential smoothing.",
            "relative_strength": "Ticker return minus benchmark return over same window."
        }
    }

    packet_md = render_market_packet(config, manifest, metrics, factor_summary)

    # Write latest.
    (DOCS_LATEST / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (DOCS_LATEST / "evidence_ledger.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    (DOCS_LATEST / "technicals.json").write_text(json.dumps(technicals, indent=2), encoding="utf-8")
    (DOCS_LATEST / "market_packet.md").write_text(packet_md, encoding="utf-8")

    # Write archive.
    (run_archive / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (run_archive / "evidence_ledger.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    (run_archive / "technicals.json").write_text(json.dumps(technicals, indent=2), encoding="utf-8")
    (run_archive / "market_packet.md").write_text(packet_md, encoding="utf-8")

    print(packet_md)


if __name__ == "__main__":
    main()
