# 12 — Archon integration through 4tress and archon-keymaster

**Selected interface, 2026-10-17:** use [4tress](https://4tress.org/) as the preferred remote Archon node, with the **Python `archon-keymaster` package** as the local client/signing interface. Its executable is `keymaster`, and its import package is `keymaster`. This is distinct from the similarly named optional agent skill. The experiment remains a research specification; this document does not claim a successful connection or an executed study.

## 1. Architecture and what changes

The preferred integration path is `agent policy -> experiment authorization adapter -> local archon-keymaster -> HTTPS 4tress -> Archon registries/storage`. Private keys, encrypted wallets, passphrases and signing remain local. 4tress is a node endpoint, not the experiment's wallet custodian, ground-truth oracle or mandatory reputation evaluator. All human, artificial, institutional and unknown controllers use the same adapter and contract rules.

A full Docker Keymaster/Gatekeeper/IPFS deployment and the JavaScript MCP server are **not prerequisites** for the first real Archon integration. Keep an independent local node or second approved operator for later verification, availability and adversarial tests. Do not remove those tests: using one hosted gateway alone cannot establish censorship resistance or independence from that gateway.

S0–S3 remain offline and deterministic. This profile is disabled by default, and enabling network reads does not authorize creating public DIDs, issuing credentials, paying invoices, changing registries or sending money. Use [the configuration profile](../configs/archon-4tress.json) and [its schema](../schemas/archon-profile.schema.json).

## 2. Verified sources and pinning

The [official Archon agent guide](https://archetech.com/agents.html) identifies 4tress as the public reference node and documents Python `pip install archon-keymaster` plus `keymaster create-id`. The [Python package README](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/README.md) describes the local library/CLI and configuration. The [package metadata](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/pyproject.toml) declares package version **0.7.0**, **Python >=3.12**, and the `keymaster = keymaster.cli:main` console entry point.

Pin source revision **`0a6ecf574a6a35175471a3342e30936336f37df6`**, subdirectory `python/keymaster`. The source version is not proof that an identically numbered PyPI release has been published. The reproducible installation route below pins source; a release-wheel route needs independently verified package provenance and hashes. Lock all resolved dependencies, including build dependencies, before a confirmatory run. Record Python version, distribution version, source revision, dependency lock digest and adapter revision.

The local source pin does **not** pin 4tress's deployed server. Record its reported version/capabilities when available, actual observed registry list and response digests. Mark absent server revision as unknown, never substitute the local client SHA. At documentation time the public site's live status could not be independently confirmed from this environment; an actual bounded preflight is required.

## 3. Safe operator setup — not executed by this document

Use Python 3.12+ for the integration worker; the offline simulator may retain its Python 3.11 floor if it communicates through an isolated 3.12+ worker. Prefer 3.12+ for a new unified project. Archon dependencies must remain optional for offline tests.

After approval to install dependencies, from the experiment directory:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install 'archon-keymaster @ git+https://github.com/archetech/archon.git@0a6ecf574a6a35175471a3342e30936336f37df6#subdirectory=python/keymaster'
keymaster --help
```

Do not execute an unreviewed remote shell installer. The `keymaster` executable must come from this virtual environment, not another Python or Node installation; record its path and installed distribution metadata.

Use explicit configuration so inherited shell variables or an existing personal wallet cannot redirect the run:

```sh
export ARCHON_NODE_URL='https://4tress.org'
export ARCHON_GATEKEEPER_URL='https://4tress.org'
export ARCHON_DEFAULT_REGISTRY='hyperswarm'
export ARCHON_WALLET_TYPE='json'
export ARCHON_WALLET_PATH="$PWD/runs/private/archon/smoke/agent-01/wallet.json"
export ARCHON_PASSPHRASE_FILE="$PWD/runs/private/archon/smoke/agent-01/passphrase"
```

The adapter must reject conflicting node URL variables, refuse an inherited `ARCHON_PASSPHRASE` in favor of an approved local secret source, and refuse fallback to `~/.archon/wallet.json` or an unrelated `./wallet.json`. Provision the private directory with mode 0700 and its passphrase file with mode 0600, outside version control, using a local secret manager. Never print the secret or put it in a command argument. Give each concurrently controlled experimental identity its own wallet store/process or explicitly serialize access; do not share a mutable 'current ID' across workers.

After **separate permission to publish synthetic records**, operator smoke commands include `keymaster create-wallet`, `keymaster create-id aae-smoke-agent-01`, and `keymaster list-ids`. Confirm their current help and effects on the pinned CLI first. Wallet creation is a local mutation; DID creation publishes data. Do not use mnemonic export, personal-wallet recovery, Lightning wallet creation or payment commands as part of onboarding.

## 4. Read-only preflight and capability discovery

Use the package's [GatekeeperClient](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/src/keymaster/gatekeeper_client.py), which appends `/api/v1` itself: pass the origin `https://4tress.org`, **not** an origin already containing `/api/v1`. Its read methods include `is_ready()`, `list_registries()` and `resolve_did(did, options)`. Always close the client. Do not use its unbounded `connect(wait_until_ready=True)` retry loop in unattended experiments.

A bounded read-only probe after network approval can use:

```python
import asyncio
from keymaster.gatekeeper_client import GatekeeperClient

async def probe():
    client = GatekeeperClient('https://4tress.org')  # no remote admin credential
    try:
        async with asyncio.timeout(45):
            ready = await client.is_ready()
            registries = await client.list_registries()
            if not ready:
                raise RuntimeError('4tress is not ready; do not proceed')
            if not isinstance(registries, list) or not all(isinstance(r, str) for r in registries):
                raise RuntimeError('Unexpected registry response; do not proceed')
            return {'ready': ready, 'registries': registries}
    finally:
        await client.close()

# Invoke only from the runner after its network permission gate passes.
```

The profile proposes conservative smoke limits, not documented provider guarantees: one concurrent request, at most 0.5 requests/second and 25 requests total; at most two synthetic identities and six public claim assets when writes are explicitly enabled. Coordinate with the operator before larger work. Enforce the budget around every SDK HTTP operation, not just top-level CLI calls.

On timeout, TLS/DNS failure, malformed JSON, 401/403, 402 or 429, report an unavailable/unsupported/authorization/payment/rate-limit condition as appropriate. Retry idempotent reads at most once within the total budget; do not automatically retry writes. A timed-out write may already have been accepted: reconcile its deterministic operation ID/history before considering a resubmission. Never silently switch hosts, downgrade TLS, pay an L402 challenge, attach the user's admin key, or create a replacement identity.

## 5. Client adapter contract

Implement the existing IdentityPort and CredentialPort using `archon-keymaster`, not handwritten DID cryptography or calls to a hosted Keymaster wallet service. The [public import](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/src/keymaster/__init__.py) exports `Keymaster`. Its [constructor and logic](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/python/keymaster/src/keymaster/core.py) accept a Gatekeeper client, local wallet store, passphrase and registry. Audit the pinned methods and write contract tests before adapting operations.

- **Identity:** create pseudonyms only after approval; resolve current/historical versions; prove possession; rotate keys and revoke under explicit capabilities. The adapter returns DID, operation IDs, provenance and pending/confirmed status separately.
- **Credentials/evidence:** issue and verify signed, subject-bound claims, revoke, and append contesting evidence. Verify issuer authority at issuance time; a valid signature is not evidence that a claim is true.
- **Storage:** use the client's supported asset/content interfaces and retain the canonical signed bytes locally. A content hash or remote pin is not a permanent availability guarantee.
- **Anchoring:** submit signed operations through the client's selected registry. Do not implement a custom OP_RETURN broadcaster merely to use 4tress. Obtain and independently verify batch inclusion, Bitcoin chain/network, position, depth and reorg status. If the required proofs cannot be retrieved, the claim remains unverified.
- **Payments:** stay disabled for this identity profile. LightningSettlementPort and L402 belong to separately approved S5 tests; do not assume 4tress exposes or authorizes payment services.
- **Policy access:** expose only a narrow structured-action adapter to agent policies. Never give a model the raw Keymaster object, arbitrary CLI execution, passphrase file or wallet-export methods. The optional `archon-keymaster` agent skill and `@didcid/mcp-server` are not mandatory dependencies.

## 6. Registries and the limits of a hosted reference node

The SDK's default is Hyperswarm. Require the requested registry to appear in the actual preflight response before any write. Hyperswarm is unanchored; a connection to 4tress or `confirmed: true` does not make history Bitcoin-backed. Creation may be marked confirmed without an on-chain anchor.

For a Bitcoin experiment request `BTC:signet` explicitly and only if available and approved. If unavailable, mark that integration stage blocked; do not relabel Hyperswarm as arm F, switch to mainnet, or silently choose another chain. An approved independent node can supply missing capabilities in a separately declared profile/condition. Keep endpoint choice, storage replication, registry and reputation method distinct variables in paired comparisons.

A single TLS endpoint can filter, delay or omit evidence and correlate clients. Treat its responses as supplied data, validate signatures/content/chain proofs, retain response captures and use an independent verifier not wholly reliant on the same endpoint for the independence claim. Record unknown completeness and unavailable content honestly. No claims of anonymity against the gateway operator are made merely because DIDs are pseudonymous.

## 7. Acceptance tests and stage split

**S4a, interface:** offline SDK boundary mocks first; then approved bounded read-only preflight; then approved two-identity smoke test. Check local wallet isolation, no unexpected host or secrets in egress/logs, valid signatures, historical authority, create/resolve/rotate/revoke and false signed claims remaining distinguishable from truth. Demonstrate denial of unapproved writes/payments and proper handling of missing capabilities.

**S4b, historical verification:** independently reconstruct disclosed evidence when the original client is offline; test rotation/revocation, unavailable content and stale/contradictory responses. Separate a content-integrity proof from evidence completeness and availability.

**S4c, adversarial and Bitcoin:** use local fixtures or an owned isolated node for reorgs, forged responses, CID conflicts, partitions, storage loss, load and censorship. **Never fault-inject, flood or attack 4tress.** If signet is supported and approved, verify real anchor proofs and compare with an equally engineered transparency log. S4 is not complete merely because S4a can reach the hosted node.

The unchanged substantive requirements include independent signature checks, historical key validation, registry migration evidence, revocation without erasure, retained IPFS bytes, correct handling of reorgs and conditional convergence, and separation of invoice payment from service delivery.

## 8. Reproduction and provenance

Use manifest version 1.1 with `adapter_mode: archon-remote` for the hosted-client run and an `archon_interface` object recording profile digest, node URL, client distribution/version/source SHA and the digest of an observation artifact. Record actual server version when exposed, otherwise null; do not infer it from the client. Offline manifests continue to use `offline` and a null interface. Store dependency hashes, bounded request counts, sanitized public replies, registry list and relevant signed operations. Secrets and private wallet bytes must never appear in the exported artifacts.

Live responses/timestamps are not deterministic. Capture them for offline replay and distinguish replay reproducibility from repeating writes against a changing network. Keep bulk strategy tournaments and attacks offline; 4tress is the default interoperability target, not a per-tick simulator backend.

## 9. Further primary references

[Archon white paper](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/WHITEPAPER.md), [DID scheme](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/scheme.md), [Gatekeeper specification](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/gatekeeper/README.md), [Lightning mediator](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/mediators/lightning/README.md), [convergence proof scope](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/proofs/agent-convergence/README.md), and [historical security audit](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/SECURITY_AUDIT.md). Check current code rather than assuming old audit findings remain open. The [historical bibliography](14-references.md) and original thesis remain unchanged.
