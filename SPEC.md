# THE ORACLE — Owner config
- Owner: Byron Teasley · timezone America/New_York (report all times in ET)
- Niches (equal priority): (1) AI — agents, decentralized compute/inference, AI data; (2) Quantum / post-quantum cryptography — PQC-secured chains, quantum-resistant tokens
- Window: last ~2 weeks + upcoming launches
- HIGH PRIORITY threshold: score >= 75 AND >= 2 independent quality sources
- Daily HIGH PRIORITY alert cap: 3 (count resets midnight ET)
- Delivery: Grok Bot chat (desk Page "ORACLE Desk" updated in place; see desk/PUBLISH.md)
- Research only: never connect a wallet, sign, trade, or handle keys. Not financial advice.
- Verdict labels on the desk: HIGH PRIORITY / WATCH (incl. PROVISIONAL = tokenomics unpublished) / REJECT (one-line reason)

# THE ORACLE — Score Spec v1.0 (2026-11-01)

Scope: AI-crypto and quantum / post-quantum (PQ) crypto token launches & pre-launch projects. Equal coverage of both niches.
Research only. Never connect a wallet, sign, handle keys, or trade. Not financial advice.

## Oracle Score (0–100)
| # | Factor | Max | What earns points |
|---|---|---|---|
| 1 | Team doxxed / track record | 15 | Named founders on official pages + verifiable history (prior companies, papers, exits) |
| 2 | Credible backers | 10 | Named tier-1/2 funds or angels confirmed by ≥1 independent outlet (not only a paid PR wire) |
| 3 | Real product / GitHub activity | 15 | Live mainnet/app with usage; public repos with recent commits |
| 4 | Audit | 10 | Public report from a recognised auditor covering the core code (not just a token contract) |
| 5 | Official channels consistency | 10 | Site, X, docs, CoinGecko, contract all point at each other; no conflicting claims |
| 6 | Tokenomics sanity | 15 | Published allocation/vesting; insider cliff ≥12 mo; float & FDV not extreme; no hidden mint |
| 7 | Liquidity / venue quality | 15 | Tier-1 CEX (Coinbase/Binance/Kraken/Upbit/OKX/KuCoin/Bitget) or deep DEX; real volume |
| 8 | Red-flag deduction pool | 10 | Start at 10, subtract for each soft red flag (insider dumps, sybil drama, paid-PR-only coverage, anon dev, etc.) |

Pre-launch items: factor 7 is scored 0–5 on announced venues only. If tokenomics are unpublished, the score is **PROVISIONAL** (tracked, not alerted).

## Verdicts
- **HIGH PRIORITY** = 75+ AND ≥2 independent quality sources (e.g. tier-1 exchange notice + reputable outlet + official docs).
- **WATCH** = 55–74.
- **REJECT** = <55, OR any hard red flag regardless of score.

Hard red flags (auto-REJECT): honeypot/mint/blacklist in contract; team-controlled unlocked supply >30% at TGE without disclosure; presale-only via website with KOL shilling; impersonation of another project; pump.fun/anon meme dressed as infra; official channel suspended/hijacked without an official replacement; fake audits.

## Impostor check (mandatory on every alert)
1. Contract address must match the project's own docs AND CoinGecko/explorer. 2. X handle must be linked from the official site (and vice-versa). 3. Claim/airdrop URLs must be on the official domain (subdomain OK). 4. Flag lookalike domains & handles seen in the sweep.

## Alert format
```
[VERDICT] NAME (TICKER) — niche — stage — Oracle Score NN
Breakdown: Team a/15 · Backers b/10 · Product c/15 · Audit d/10 · Consistency e/10 · Tokenomics f/15 · Liquidity g/15 · Red-flag pool h/10
Evidence: …
Risks: …
Links (official only): site · X · docs · contract
Impostor check: PASS/FAIL + notes
```
