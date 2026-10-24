# 12 — Local-keymaster and 4tress integration within the application

**Revised scope, October 24, 2026:** retain [4tress](https://4tress.org/) and local Python `archon-keymaster` as the selected identity-integration path. Required adapter qualification belongs in M1 of the [application-led gates](11-stage-gates.md), not after a separate large simulator study. No connection, write or live study is claimed by this document.

## Pinned baseline and provenance

Preserve source revision `0a6ecf574a6a35175471a3342e30936336f37df6`, subdirectory `python/keymaster`, as the documented reproducibility baseline. Its [package metadata](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/pyproject.toml) declares version 0.7.0 and Python >=3.12; the [package README](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/README.md) describes the local CLI/library. These are historical pinned properties, not claims about the latest package or the deployed server. A reviewed upgrade needs source and dependency hashes plus renewed contract tests.

The executable is `keymaster`, import package `keymaster`. Do not confuse it with an optional agent skill or require a JavaScript MCP server merely to begin. Prefer Python 3.12+ for a new application domain; integrations remain optional for offline tests. Record source, distribution, Python, dependency lock and adapter revisions separately from independently observed remote capabilities. Unknown server revision stays unknown.

## Architecture and custody

The path is bounded agent action → application authorization adapter → local keymaster/signing → HTTPS 4tress → supported registry/storage. Local wallets, passphrases and private keys never leave their authorized host. 4tress is not the application's wallet custodian, real-world oracle or reputation authority.

Retain the disabled-by-default, read-only [profile](../configs/archon-4tress.json) and [profile schema](../schemas/archon-profile.schema.json). Enabling reads does not authorize DID creation, credential publication, fees, registry changes or payments. A full local stack is not required for first connectivity; independent verifiers/owned nodes remain important for historical reconstruction and adversarial work. Connectivity alone does not establish decentralized assurance.

## Safe setup and scoped identity tests

After explicit dependency/network approval, use an isolated Python environment and verified source installation, not a remote shell installer. Inspect the pinned CLI/help and SDK before invoking methods. Set both `ARCHON_NODE_URL` and `ARCHON_GATEKEEPER_URL` explicitly to `https://4tress.org`; reject conflicts. Use explicit private wallet and passphrase-file paths outside version control, with private directory/file permissions. Reject inherited personal-wallet paths, default-wallet fallback and unsafe secret environment values.

Provision independent stores/processes or serialized access for concurrent identities; do not share mutable current-identity state. Test and live keys/credentials remain isolated. Local wallet creation and public DID creation have different effects; both need their respective approvals. No mnemonic export, personal-wallet recovery or payment command belongs in routine agent onboarding.

## Bounded preflight

The pinned [GatekeeperClient](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/src/keymaster/gatekeeper_client.py) appends `/api/v1`: pass the origin, not a doubled API path. Audit `is_ready()`, `list_registries()` and `resolve_did()` against the pin, close the client and avoid an indefinite readiness retry. A proposed smoke budget remains one concurrent request, at most 0.5 requests/second, 25 requests total and a bounded overall deadline. These are local policy limits, not provider guarantees.

Inspect actual readiness, registries and permissions. Timeout, malformed JSON, TLS/DNS failure, 401/403, 402 or 429 must yield a specific blocked/unknown state. Retry safe idempotent reads at most once within the budget; do not blindly retry writes. Reconcile deterministic operation/history after ambiguous writes. Never auto-pay a challenge, switch hosts or registries, downgrade TLS or attach production credentials.

After separate synthetic-write approval, the profile permits a small smoke scope (at most two identities and six public claim assets). Enforce counts around underlying HTTP operations. Larger or live use requires separately reviewed scope, consent and identifiers; no synthetic work may bootstrap real reputation. Do not send oracle/controller mappings or private worker evidence to the hosted node.

## Adapter requirements

Expose narrow IdentityPort/CredentialPort-style interfaces, not raw Keymaster, arbitrary CLI or secret export. These port names are design interfaces, not a claim that application code already exists. Audit the pinned [Keymaster implementation](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/src/keymaster/core.py) before implementing supported methods.

Qualify possession proofs, current/historical resolution, rotation, revocation, issuer authority, credential signatures, content integrity and retention. Preserve pending, confirmed, unavailable and unverified states. Authentic false claims remain possible; signature validity never equals fulfillment. Retain canonical signed bytes and independently reconstruct disclosed history when the originating client is offline.

Payments are outside this identity profile. Cashu/Lightning settlement adapters require their own qualified scope and approvals. No node response is permission to create wallets or fund jobs. Evidence availability, completeness and privacy are separate from content integrity.

## Registry and anchoring limits

Require the requested registry to appear in actual capabilities. Hyperswarm is not Bitcoin anchoring; a generic confirmed flag does not prove a chain inclusion. For a specific anchoring study, request `BTC:signet` only when supported and approved, then independently verify chain/network, batch inclusion, depth and reorg status. Missing signet blocks that study, not necessarily a pilot that makes no anchoring claim and meets its other safety requirements.

Do not silently substitute mainnet or relabel unanchored records as a Bitcoin treatment. Endpoint, storage replication, registry and reputation method remain distinct experimental variables. A single gateway may omit evidence or correlate clients; independent verification cannot consist only of repeatedly asking that same gateway.

## Qualification groups and historical labels

Earlier S4a/S4b/S4c labels now describe capabilities, not a mandatory sequential program gate: bounded interface smoke tests; independent historical reconstruction; optional anchoring/adversarial verification. A narrow M1 pilot must demonstrate the capabilities its safety claims depend on. Broader anchoring comparisons and stress tests may be later research. Do not weaken a claimed guarantee simply to move a milestone.

Run malformed responses, malicious signatures, storage loss, reorgs, partitions, floods and censorship fixtures only on owned/isolated infrastructure. Never attack or load-test 4tress. Confirm that unapproved writes/payments are denied, secret egress is absent, historical authority is checked and unavailable evidence remains unknown.

## Manifests and reproducibility

Retain the existing manifest 1.1/profile examples as compatibility inputs: `adapter_mode: archon-remote`, profile digest, node URL, client distribution/version/source and observed remote-response digest. They are not a complete field-study manifest. The [data contract design](17-data-contracts.md) adds environment, consent, policy and assignment requirements through an explicitly versioned future schema migration.

Capture sanitized public responses and request counts for offline replay. A repeated live call is not deterministic historical replay. Separate permission logs, private stores and public artifacts. The [original pinned integration specification](https://github.com/santyr/santyr.github.io/blob/2faf058ec6f2c9e992f4a3139ba2c756256b3848/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/12-archon-integration.md) remains available for setup examples; its S-stage scheduling is superseded by this revision.
