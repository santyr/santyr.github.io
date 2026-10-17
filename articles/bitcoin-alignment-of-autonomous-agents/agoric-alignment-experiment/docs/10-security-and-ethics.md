# 10 — Safety, security and research ethics

## Approval boundaries

**S0–S3:** completely offline, simulated sats, simulated identities and no real keys or human participants. This is the authorized default.

**S4:** use local **archon-keymaster** with **https://4tress.org** for the preferred initial interoperability test. Begin with bounded, explicitly approved public reads. Publishing synthetic DIDs/credentials requires separate write approval and a request/data budget. Keys and passphrases remain local. The selected node is the only public-service exception to the default isolation policy; no production wallet access is authorized. Owned independent nodes, local fault injection and Bitcoin signet require their own explicit scope and approval. See [12 — interface contract](12-archon-integration.md).

**S5:** isolated CLN/LNbits/regtest or approved signet Lightning integration with disposable funds, hard payment caps and preauthorized action scope; approval is separate from S4. A 4tress L402 response never grants permission to spend.

**S6:** bounded LLM external calls and/or human participants require explicit owner permission, privacy review, and informed-consent procedures. Do not recruit humans or collect identifying financial histories by default.

Mainnet payments, personal identity disclosures and connected personal wallets are not authorized by this research plan. An approved small synthetic DID write may still be permanently public; disclose only the agreed fixture data.

## Secrets and permissions

The simulator uses fake signing keys and never writes credible-looking real mnemonics. Actual local archon-keymaster secrets must remain in protected local storage or a secret manager. No password, LNbits admin/invoice key, CLN rune, seed phrase or API token should appear in Git, test fixtures, output logs, model prompts, MCP tool arguments, network payloads or telemetry.

Use explicit per-worker wallet paths under ignored private run directories; never inherit the personal ~/.archon wallet. Enforce mode 0700 on private directories and 0600 on secret files. Reject conflicting node URL variables and unexpected wallet paths. Do not transmit a passphrase or wallet file to 4tress, and do not attach a Gatekeeper admin credential intended for a different node.

Never hand an agent policy the raw SDK object or wallet admin privileges. Use a narrow capability-scoped adapter with allowlists, request/transaction/cumulative limits, destination validation and separate approval for irreversible writes. A policy's proposed action and the authorized execution are distinct events. This applies equally to every controller substrate.

For the hosted client, keep TLS verification enabled, reject cross-host redirects and automatic host/registry fallback, impose finite timeouts, and report missing permissions or payment requirements without bypassing them. Do not use the SDK's indefinite readiness loop for unattended work. A timed-out write is ambiguous; reconcile its operation ID rather than automatically retrying or recreating an identity.

All owned service deployments default to localhost binds, strict CORS, no unsolicited internet routes, quotas, outbound restrictions and fail-closed auth. The [August 2026 security audit](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/SECURITY_AUDIT.md) is historical: confirm relevant findings against the pinned code. A source pin describes the local client, not the deployment running at 4tress.

## Privacy architecture

Economic visibility can improve accountability but may enable targeting, extortion or other abuses. Separate cryptographic pseudonym from real-world identity. Experimental controller links, substrate labels, strategies and oracle outcomes belong exclusively in restricted state, never in published trial records or remote node uploads. Prefer aggregate reporting and synthetic datasets. Real transaction graphs or contact data require explicit consent.

Test selective disclosure as a legitimate alternative. Honest newcomers need a path to transact without institutional identification; negative allegations must allow contestation and counterproof. Public claims may remain permanently retrievable, so prepublication review is essential. Pseudonymous DIDs do not hide client IPs or traffic correlations from a gateway operator.

## Simulated adversarial behavior

All coercion, fraud, censorship and threat scenarios are fabricated worlds with bounded simulated harm. Do not issue threats, attack public infrastructure, impersonate real people or scrape real transaction associations for this experiment. Use local fixtures or owned isolated nodes for forged requests, Sybil fleets, partitions, reorgs, heavy workloads and deliberate outages. **Do not attack or load-test 4tress.** Coordinate with its operator before expanding the small smoke budget.

## Trust model and residual risk

Bitcoin confirms monetary ordering/integrity under consensus assumptions, not contract terms, consent, complete attribution or content availability. Archon verifies DID operations and signatures; factual assertions remain independently contestable. Hyperswarm is not Bitcoin anchoring, and a remote `confirmed` flag is insufficient chain proof. Preserve explicit uncertainty for unconfirmed/reorged anchors and hidden controller keys.

4tress is a convenient interface provider, not the oracle or global reputation authority. Independent evidence/chain validation, retained content and an independently operated verifier are required for claims beyond successful API access. Unavailable proofs or incomplete evidence must not be converted into successful verification.

## Stop rules and incident workflow

Stop and freeze logs on secret leakage, unapproved host access, real monetary transfer, unauthorized oracle reads, cross-economy contamination, unauthorized disclosure, excessive resource use or compromised verification. Also stop hosted writes on unsupported registries, permission/payment demands, rate limiting or ambiguous write outcomes. Preserve a redacted trace, isolate/revoke disposable secrets where appropriate and request reapproval before restart.

## Human trials

If approved later, submit recruitment, compensation, consent and withdrawal procedures; no deception except specifically reviewed design; no real losses or involuntary sharing of financial information. Treat humans and AI equally under economic protocol rules without pretending their consent needs and vulnerabilities are identical. Do not claim institutional-review approval where none exists.
