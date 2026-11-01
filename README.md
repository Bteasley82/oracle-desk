# ORACLE Desk

Live desk: **https://bteasley82.github.io/oracle-desk/**

Research on new and upcoming **AI** and **quantum / post-quantum** crypto launches, scored 0–100 and
filtered for scams (method in [SPEC.md](SPEC.md)). Verdicts: HIGH PRIORITY / WATCH (incl. PROVISIONAL) / REJECT.

**Research only, not financial advice.** Nothing here connects a wallet, signs, trades or handles keys.

## Files
- `index.html` – static, dependency-free page; fetches `oracle-feed.json` (and `breakdowns.json`) at load. Times shown in ET.
- `oracle-feed.json` – the feed (source of truth is maintained by the Oracle sweep and pushed here).
- `breakdowns.json` – per-factor Oracle Score breakdown by ticker (from the latest sweep).
- `scripts/update_prices.py` – refreshes price, market cap and 24h volume from CoinGecko's free API (stdlib only; exits 1 and leaves the feed untouched on failure).
- `.github/workflows/prices.yml` – runs the price refresh every 2 hours (and on demand) and commits the feed only if it changed.

## Run locally
```
python3 scripts/update_prices.py      # refresh prices
python3 -m http.server                # then open http://localhost:8000
```
