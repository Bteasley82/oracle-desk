# ORACLE Desk

Live desk: **https://bteasley82.github.io/oracle-desk/**

Research on new and upcoming **AI** and **quantum / post-quantum** crypto launches, scored 0–100 and
filtered for scams (method in [SPEC.md](SPEC.md)). Verdicts: HIGH PRIORITY / WATCH (incl. PROVISIONAL) / REJECT.

**Research only, not financial advice.** Nothing here connects a wallet, signs, trades or handles keys.

## Files
- `index.html` / `oracle-desk.html` – the shared ORACLE desk page (RockoDevelopment/oracle-desk-shared, `oracle-desk-for-others.html`), unmodified except for its `SYNC_URL` line. Loads `./oracle-feed.json` at runtime.
- `oracle-feed.json` – the feed, maintained by the Oracle sweep and pushed here.
- `update_prices.py` – shared CoinGecko price refresher; updates watchlist items that have `cg_id` and `price` in `oracle-feed.json` (same folder).
- `.github/workflows/prices.yml` – runs `update_prices.py` every hour (and on demand) and commits the feed only if it changed.

## Run locally
```
python3 update_prices.py              # refresh prices
python3 -m http.server                # then open http://localhost:8000
```
