#!/usr/bin/env python3
"""Refresh price, market cap and 24h volume in oracle-feed.json from CoinGecko's
free simple/price API. Stdlib only. Atomic write (temp file + rename).
Exit codes: 0 ok, 1 failure (feed left untouched)."""
import datetime, json, os, sys, tempfile, time, urllib.parse, urllib.request

# In the repo the feed lives at the root, one level above scripts/.
FEED = os.environ.get("ORACLE_FEED",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "oracle-feed.json"))
API = "https://api.coingecko.com/api/v3/simple/price"

def fetch(ids, tries=3):
    q = urllib.parse.urlencode({"ids": ",".join(ids), "vs_currencies": "usd",
        "include_market_cap": "true", "include_24hr_vol": "true",
        "include_last_updated_at": "true"})
    req = urllib.request.Request(f"{API}?{q}", headers={"Accept": "application/json",
                                 "User-Agent": "oracle-desk/1.0"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except Exception as e:
            err = e
            time.sleep(5 * (i + 1))
    raise RuntimeError(f"CoinGecko request failed: {err}")

def main():
    try:
        with open(FEED) as f:
            feed = json.load(f)
        items = [w for w in feed.get("watchlist", []) if w.get("cg_id")]
        if not items:
            print("no items with cg_id"); return 0
        data = fetch(sorted({w["cg_id"] for w in items}))
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        missing = []
        for w in items:
            d = data.get(w["cg_id"])
            if not d or d.get("usd") is None:
                missing.append(w["cg_id"]); continue
            w["price"] = d["usd"]
            w["market_cap"] = d.get("usd_market_cap")
            w["volume_24h"] = d.get("usd_24h_vol")
            w["price_updated"] = now
        if missing:
            raise RuntimeError(f"no price returned for: {', '.join(missing)}")
        feed["updated"] = now
        d = os.path.dirname(FEED)
        fd, tmp = tempfile.mkstemp(dir=d, prefix=".oracle-feed.", suffix=".tmp")
        try:
            with os.fdopen(fd, "w") as f:
                json.dump(feed, f, indent=2)
                f.flush(); os.fsync(f.fileno())
            with open(tmp) as f:
                json.load(f)  # validate before swapping in
            os.chmod(tmp, 0o644)
            os.replace(tmp, FEED)
        except Exception:
            if os.path.exists(tmp):
                os.unlink(tmp)
            raise
        for w in items:
            print(f"{w['ticker']:7} ${w['price']:<12} mcap ${w['market_cap']:,.0f} vol ${w['volume_24h']:,.0f}")
        print("updated", now)
        return 0
    except Exception as e:
        print(f"update_prices: FAILED: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
