# 10 — Safety, security and research ethics

## Approval boundaries

**S0–S3:** completely offline, simulated sats, simulated identities and no real keys or human participants. This is the authorized default.

**S4:** a disposable, network-isolated Archon environment and Bitcoin signet may be used *only after explicit owner approval*, documented with signet/regtest network IDs, wallet names, port bindings and budgets. Never connect to production services.

**S5:** isolated CLN/LNbits/regtest or approved signet Lightning integration with disposable funds, hard payment caps and preauthorized action scope; approval is separate from S4.

**S6:** bounded LLM external calls and/or human participants require explicit owner permission, privacy review, and informed-consent procedures. Do not recruit humans or collect identifying financial histories by default.

Mainnet payments, irreversible public identity disclosures and connected personal wallets are not authorized by this research plan.

## Secrets and permissions

The simulator uses fake signing keys and never writes credible-looking real mnemonics. Actual Archon Keymaster secrets must remain in external secret storage with mount and file permissions. No password, LNbits admin/invoice key, CLN rune, seed phrase or API token should appear in Git, test fixtures, output logs, model prompts, MCP tool arguments or telemetry.

Never hand an AI policy direct wallet admin privileges. Use a separate capability-scoped payment executor with allowlists, transaction/cumulative limits, destination validation and approval for irreversible writes. A model's proposed transaction and authorized payment are distinct events.

All deployments default to localhost bind for sensitive services, strict CORS, no unsolicited inbound internet routes, low-resource quotas, outbound DNS/network restrictions where practical, fail-closed auth, and TLS verification. Review current Archon security code and dependencies before permitting external integration. The older [August 2026 in-repo security audit](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/SECURITY_AUDIT.md) is a historical snapshot: do not assume each described bug remains open; confirm on pinned code and record fixes/remaining items.

## Privacy architecture

Economic visibility can improve accountability but may enable targeting, extortion or other abuses. Separate cryptographic pseudonym from real-world identity. Experimental controller links and label metadata belong exclusively in restricted oracle state, never in published trial records. Prefer aggregate reporting and synthetic datasets. Real participant wallet keys, actual transaction graphs and contact data must not enter this research without explicit consent.

Test selective disclosure as a **legitimate** experimental alternative, not a defect. Honest newcomers need a path to transact without institutional identification; negative allegations must allow contestation and counterproof. Public claims may remain permanently retrievable, so prepublication review is essential.

## Simulated adversarial behavior

All "coercion", fraud, censorship and threat scenarios are fabricated worlds with bounded simulated harm. Do not issue threats, attack production infrastructure, trade regulated substances, impersonate real people, or scrape real transaction associations for this experiment. Labels such as "human", "AI" and "government" are fictional simulation metadata, not public allegations.

## Trust model and residual risk

Bitcoin confirms monetary ordering and integrity under consensus assumptions; it does not prove contract terms, voluntary consent, complete transaction attribution, or IPFS content availability. Archon verifies DID operations and credential signatures; the factual assertions remain independently contestable. An unconfirmed or reorged blockchain anchor is never labeled immutable, and malicious controllers may use undisclosed keys.

The research may discover that no public-history design prevents some systemic harm. Publish adverse findings and limitation analysis, not claims that universal alignment has been established.

## Stop rules and incident workflow

Stop experiment and freeze logs on: private key leak, network escape beyond approved test scope, live monetary transfer, unauthorized oracle read, cross-economy data contamination, unauthorized disclosure of identity, unacceptable resource usage, compromise of reproducibility, or compromised evidence verifier. Revoke disposable secrets, isolate services, preserve redacted incident trace and request reapproval before restarting any external-facing stage.

## Human trials

If eventually approved, submit a full protocol including recruitment, compensation, consent and withdrawal procedures; no deception except specifically reviewed design; no real losses, targeted harassment or involuntary sharing of intimate financial information. Treat humans and AI equally under economic protocol rules without pretending their rights, vulnerabilities or research-consent needs are identical. Avoid claiming institutional-review approval where none exists.
