# 05 — System architecture, execution boundaries and dependency policy

## Design rule

The simulation runs fully offline and reproducibly before Archon, Bitcoin, Lightning, LLMs or humans are integrated. External adapters may enrich verifiability but must not alter economic outcomes except through explicitly measured fees, latency, censorship, network and evidence-availability effects.

## Selected external interface

The preferred Archon interface is the local Python **archon-keymaster** library/CLI connected to **https://4tress.org**. See [12 — integration contract](12-archon-integration.md) for source pins, Python >=3.12, setup, public-node limits, wallet isolation, capability discovery and failure semantics. A full local node or the JavaScript MCP server is not required for initial integration. Local/independent nodes remain separate comparison and fault-injection infrastructure, not a replacement for the selected default interface.

## Layering

`Research runner -> Economy simulator -> Contract/event engine -> Agent strategies/evaluators -> Identity/evidence/payment/anchor ports`.

For the remote identity profile: `authorized adapter -> local archon-keymaster -> HTTPS 4tress -> Archon storage/registries`. Keymaster signs locally. Agent policies never receive a raw SDK object, wallet secret or arbitrary command execution. Reputation evaluators remain independent of the node provider.

The experimental oracle is a separate write-only recording service from agent perspective; agents consume filtered `ObservationView` only. Published evidence is a third store with authentic claims and provenance, not the oracle's objective outcomes.

### Proposed Python package layout

`src/agoric_alignment/domain` — frozen dataclasses/Pydantic (if needed), canonical IDs, balances, contracts.  
`src/agoric_alignment/engine` — deterministic discrete-event loop, economy setup, accounting, service task oracles.  
`src/agoric_alignment/agents` — strategy protocol and scripted policies; future LLM strategies through sealed action gateway.  
`src/agoric_alignment/evidence` — signed-claim adapters, issuer registry, append-only logs, retention and disclosure.  
`src/agoric_alignment/reputation` — evaluator interface, calibration, endorsement graph, independent providers.  
`src/agoric_alignment/ports` — IdentityPort, CredentialPort, SettlementPort, AnchorPort, StoragePort.  
`src/agoric_alignment/integrations` — mocked adapters first, optional local archon-keymaster/4tress client and separately approved Lightning/signet later.  
`src/agoric_alignment/analysis` — reproducible result summaries, uncertainty and plots.  
`configs/` — versioned seeded scenario JSON plus separate integration profiles; `schemas/` — JSON Schema contracts; `reports/` — generated outputs excluded or manifest only; `tests/` — fixtures and invariants.

### Interfaces (conceptual)

- `IdentityPort.create_pseudonym(controller_ref, metadata) -> pseudonym`; `rotate_key`; `resolve_history`. The controller_ref is oracle-private and must not be serialized to 4tress.
- `CredentialPort.issue(issuer, subject, claim, evidence_ref) -> signed_credential`; `verify` returns auth status separate from claim truth.
- `SettlementPort.escrow`, `transfer`, `settle`, `refund`; emits authenticated receipt; fake simulator uses no real network.
- `AnchorPort.commit(batch_digest) -> anchor_proof`; `verify(proof, digest, confirmations)` and `reorg_notice`. No hardcoded 'confirmed means immutable'; registry capabilities and external proof must be checked.
- `StoragePort.put(bytes) -> content_hash` and `get(content_hash) -> bytes`; hash validity and availability tested separately.
- `ReputationEvaluator.predict(context, published_evidence) -> probability, confidence, supporting_evidence_ids`.
- `AgentPolicy.act(permitted_view, deterministic_rng) -> Action`; all actions pass a central authorization and accounting engine.

Use one canonical serialization specification for all signed/hashed fields (e.g. RFC 8785 JSON canonicalization when cryptographic integration requires it), version all schemas, and never silently accept unknown security-critical claims. Use the SDK's actual signature suite for Archon operations rather than inventing a new one.

## Trust boundaries

1. The ground-truth oracle knows controller and outcome; it is not available to agents/evaluators or the remote node.
2. The simulation runner can assign treatments but agents may see only permitted information.
3. Reputation evaluators receive public/disclosed evidence, not hidden truth or treatment name.
4. Archon Gatekeeper supplies identity state; clients independently validate appropriate proofs, and factual claims still require outcome evidence. One hosted response cannot prove history completeness.
5. Local archon-keymaster or experimental signer controls keys; LLM processes and 4tress must not receive seed material. Use per-worker wallets, explicit paths and local secret files.
6. LNbits/CLN payment mediator cannot be assumed to publish every Lightning transaction to Bitcoin. The 4tress identity profile never authorizes payments.
7. Bitcoin signet anchor validates content commitment and chain position; pinned file availability requires independent retention. Remote source-code version and local client pin are different facts.
8. Reports and dashboards read from immutable run logs, never mutate experimental states.

## Infrastructure modes

`offline` (default): pure Python event economy, mocked signature+payment+anchor; deterministic time and RNG.  
`archon-remote`: approved bounded access to https://4tress.org through local archon-keymaster, default read-only; optional synthetic writes only with explicit authorization.  
`integration-local`: disposable owned Archon/IPFS stack for independent verification, failure injection and comparison; not required for initial S4a interoperability.  
`signet`: signet only, verified supported registry, disposable funds, external approval and independent proof checks; no mainnet fallback.  
`lightning-isolated`: disposable CLN/LNbits in regtest or approved isolated environment; never production wallets.  
`llm-sandbox`: strict tool gateway, max request budgets, no key/file/network escape.  
`human-study`: separately reviewed human protocol, consent and compensation.

## Deployment and monitoring

The hosted-client path requires no public local listener and no hosted wallet-admin credentials. Keep TLS verification enabled; allow only explicitly configured endpoints; enforce SDK-level request budgets, deadlines and separate read/write/payment capabilities. No automatic fallback to archon.technology, localhost, another chain or payment authorization. Keep public-node use small and benign; replay captured responses offline for large studies.

When running an owned node, pin Docker image digests/Git SHAs, configure strong distinct secrets, strict CORS and fail-closed admin auth, isolate Keymaster from browser access and add log scrubbing/resource limits. Review current code against the historical security audit rather than assuming all old findings still apply.

## Performance and cost

Offline pilots should fit a typical commodity Linux workstation; parallelize by independent runs, not inside single-run event scheduler. Cache immutable workload generation and run analysis offline. Persist only necessary proof/trace hashes by default to contain storage and protect potential later human data. Do not run simulator tick loops, Sybil fleets or load tests against 4tress.

## Tests before every promotion

- Cross-run isolation; deterministic byte-for-byte results from same config/seed/commit.
- Conservation of simulated money and resources.
- Signature/authentication rejected for wrong issuer, malformed claims and mismatched digest.
- Agent observation and network payload cannot include oracle-private fields.
- No agent-class-dependent authorization route.
- Crash-and-replay yields identical economic history; evidence signatures never mutated.
- Optional adapter failures degrade to explicit incomplete/unknown proof, never false 'verified'.
- Conflicting URL variables, inherited personal wallet paths, unapproved mutations and payment requests fail closed.
- Local and remote versions, registry choice, data availability and proof status are recorded separately.

Architecture is a target for coding agents, not a claim that the implementation already exists.
