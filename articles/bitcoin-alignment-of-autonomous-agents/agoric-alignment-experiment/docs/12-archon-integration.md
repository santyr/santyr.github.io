# 12 — Archon integration adapter contract (pinned)

## Upstream snapshot and version control

Primary repository: [archetech/archon](https://github.com/archetech/archon). The examined revision for planning is **`0a6ecf574a6a35175471a3342e30936336f37df6`** (main as observed 2026-10-17). All agent work must pin a concrete revision and record commit SHA, dependency lockfile, config digest, actual build artifacts and the changed interface if upgrading. Never rely on `latest` for confirmatory experiments.

Key specs:
- [Archon white paper](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/WHITEPAPER.md)
- [`did:cid` scheme](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/scheme.md)
- [Gatekeeper interface](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/gatekeeper/README.md)
- [MCP server](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/packages/mcp-server/README.md)
- [Lightning mediator](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/mediators/lightning/README.md)
- [Formal convergence proof scope](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/proofs/agent-convergence/README.md)
- [Historical security audit](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/SECURITY_AUDIT.md)

## Observed architecture

Agent DIDs identify cryptographic controllers; asset DIDs carry data/credentials and are controlled by agent DIDs. Gatekeeper validates and resolves signed `create/update/delete` operations with predecessor chains; Keymaster creates signatures, wallets and W3C-style credentials; mediators propagate operations over Hyperswarm or anchor batches to selected blockchains. Satoshi mediator writes a batch asset DID as `OP_RETURN`. Archon supports historical resolution, key rotation, revocation, Lightning service entries, L402 and agent-facing MCP.

**Crucial:** default registry in sample config is Hyperswarm, **not Bitcoin**. Registries differ in finality and trust assumptions. `didDocumentMetadata.confirmed` is not sufficient evidence of Bitcoin anchor; the spec notes creation counts as confirmed by definition. Confirm anchor chain name, block/tx position, chain depth and batch membership independently.

## Required ports implementation

`ArchonIdentityPort`: create ID, resolve DID at current/historical time, prove possession, rotate authorized key, revoke, list historical proofs. Return explicit provenance fields (registry, height, confirmations, verified).  
`ArchonCredentialPort`: issue VC, verify signature, verify subject binding, handle revocation, append contesting credential; validity as signed claim distinct from truth.  
`ArchonAnchorPort`: submit a batch commitment (safe sandbox), return CID, txid, block position and confirmation depth; verify data hash and reorg rollback; detect data unavailability.  
`LightningSettlementPort`: model adapter wraps LNbits/CLN mediator and produces receipts; must never interpret successful invoice payment as contract delivery.  
`ArchonMcpPort`: expose only explicitly authorized low-risk methods; read-only default, no unguarded `create_id` or wallet spend from LLM.

Adapter accepts `RunContext` (sandbox, registry, timeout, budget, signing provider, run_id). Fail on mismatched chain IDs and unexpected endpoints; no fallback to public archon.technology or mainnet.

## Concrete cross-check scenarios

1. Create two independent DIDs; resolve them from separate nodes and verify both key sets.
2. Sign contracts and endorsements; mutated data/issuer DID must fail verification.
3. Rotate DID's key; old historical evidence remains checkable at issuance version; stolen/retired key may not authenticate unauthorized successor under finalized registry history.
4. Revoke a credential; current resolver recognizes status; historical views still show prior evidence rather than falsely implying deletion from IPFS.
5. Write batch to local registry then to signet; verify only signet anchor carries external chain proof.
6. Disconnect origin IPFS node; show evidence availability depends on independent pinning even with valid CID/chain anchor.
7. Inject reorg/competing updates where possible; unconfirmed receipts become uncertain/withdrawn as specified.
8. Time-travel resolution on TS and Rust Gatekeepers with identical test vectors; document divergences rather than smoothing them.
9. Test Hyperswarm conflicting successors and convergence under evidence equality; do not infer availability or cryptographic safety solely from Lean proof.
10. Connect one test Lightning DID and create/pay BOLT11 inside sandbox; verify receipt and contract proof remain distinct.

## Deployment security prerequisites

Before network stage compare the historical audit to current code: require Keymaster/Gatekeeper fail-closed admin auth, safe login/password handling, explicit CORS origins, dependencies reviewed, strict proxy config and no exposed mnemonic endpoints. An old audit finding alone is not proof of current vulnerability; record the actual current state with tests. Use distinct disposable secrets, user namespaces, local firewall, isolated storage and cleanup.

The initial research must not fork/modify Archon's protocol or deploy against real keys. Open upstream issues only for reproduced defects, with appropriate private disclosure for security vulnerabilities.

## Independent verification claim

A successful Archon verification means "this signed operation/evidence is consistent with the resolver and specified registry at this confidence"—not "the issuer is reputable", "the service was performed", "all past conduct has been revealed", or "the transaction was voluntary". Document that limited claim in every API response and analysis report.
