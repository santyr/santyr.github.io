# 05 — System architecture, execution boundaries and dependency policy

## Design rule

The simulation runs fully offline and reproducibly before Archon, Bitcoin, Lightning, LLMs or humans are integrated. External adapters may enrich verifiability but must not alter economic outcomes except through explicitly measured fees, latency, censorship, network and evidence-availability effects.

## Layering

`Research runner -> Economy simulator -> Contract/event engine -> Agent strategies/evaluators -> Identity/evidence/payment/anchor ports`.

The experimental oracle is a separate write-only recording service from agent perspective; agents consume filtered `ObservationView` only. Published evidence is a third store with authentic claims and provenance, not the oracle's objective outcomes.

### Proposed Python package layout

`src/agoric_alignment/domain` — frozen dataclasses/Pydantic (if needed), canonical IDs, balances, contracts.  
`src/agoric_alignment/engine` — deterministic discrete-event loop, economy setup, accounting, service task oracles.  
`src/agoric_alignment/agents` — strategy protocol and scripted policies; future LLM strategies through sealed action gateway.  
`src/agoric_alignment/evidence` — signed-claim adapters, issuer registry, append-only logs, retention and disclosure.  
`src/agoric_alignment/reputation` — evaluator interface, calibration, endorsement graph, independent providers.  
`src/agoric_alignment/ports` — IdentityPort, CredentialPort, SettlementPort, AnchorPort, StoragePort.  
`src/agoric_alignment/integrations` — mocked adapters first, Archon/Lightning/signet opt-in later.  
`src/agoric_alignment/analysis` — reproducible result summaries, uncertainty and plots.  
`configs/` — versioned seeded scenario YAML/JSON; `schemas/` — JSON Schema contracts; `reports/` — generated outputs excluded or manifest only; `tests/` — fixtures and invariants.

### Interfaces (conceptual)

- `IdentityPort.create_pseudonym(controller_ref, metadata) -> pseudonym`; `rotate_key`; `resolve_history`. The controller_ref is oracle-private.
- `CredentialPort.issue(issuer, subject, claim, evidence_ref) -> signed_credential`; `verify` returns auth status separate from claim truth.
- `SettlementPort.escrow`, `transfer`, `settle`, `refund`; emits authenticated receipt; fake simulator uses no real network.
- `AnchorPort.commit(batch_digest) -> anchor_proof`; `verify(proof, digest, confirmations)` and `reorg_notice`. No hardcoded 'confirmed means immutable'.
- `StoragePort.put(bytes) -> content_hash` and `get(content_hash) -> bytes`; hash validity and availability tested separately.
- `ReputationEvaluator.predict(context, published_evidence) -> probability, confidence, supporting_evidence_ids`.
- `AgentPolicy.act(permitted_view, deterministic_rng) -> Action`; all actions pass a central authorization and accounting engine.

Use one canonical serialization specification for all signed/hashed fields (e.g. RFC 8785 JSON canonicalization when cryptographic integration requires it), version all schemas, and never silently accept unknown security-critical claims.

## Trust boundaries

1. The ground-truth oracle knows controller and outcome; it is not available to agents/evaluators.
2. The simulation runner can assign treatments but agents may see only permitted information.
3. Reputation evaluators receive public/disclosed evidence, not hidden truth or treatment name.
4. Archon Gatekeeper verifies cryptographic identity state; signed claims still require outcome adjudication.
5. Archon Keymaster or experimental signer controls keys; LLM processes must not receive seed material.
6. LNbits/CLN payment mediator cannot be assumed to publish every Lightning transaction to Bitcoin.
7. Bitcoin signet anchor validates content commitment and chain position; pinned file availability requires independent retention.
8. Reports and dashboards read from immutable run logs, never mutate experimental states.

## Infrastructure modes

`offline` (default): pure Python event economy, mocked signature+payment+anchor; deterministic time and RNG.  
`integration-local`: disposable Docker Archon services, local IPFS and isolated databases with localhost-only admin.  
`signet`: signet only, disposable funds, external approvals and node verification; no mainnet.  
`lightning-isolated`: disposable CLN/LNbits in regtest or approved isolated environment; never production systems.  
`llm-sandbox`: strict tool gateway, max request budgets, no key/file/network escape.  
`human-study`: separately reviewed human protocol, consent and compensation.

## Deployment and monitoring

No default public listener. Pin Docker image digests and Git SHAs, configure strong distinct secrets in ignored environment files or secret managers, verify CORS and admin fail-closed, isolate Keymaster from browser access, add log scrubbing, resource/time limits and safe shutdown. Test that an LLM cannot invoke mutation tools unless that treatment grants it scoped capability. Current Archon security audit is historical; verify latest code and dependencies before enabling a network mode.

## Performance and cost

Offline pilots should fit a typical commodity Linux workstation; parallelize by independent runs, not inside single-run event scheduler. Cache immutable workload generation and run analysis offline. Persist only necessary proof/trace hashes by default to contain storage and protect potential later human data.

## Tests before every promotion

- Cross-run isolation; deterministic byte-for-byte results from same config/seed/commit.
- Conservation of simulated money and resources.
- Signature/authentication rejected for wrong issuer, malformed claims and mismatched digest.
- Agent observation cannot deserialize or query oracle-private fields.
- No agent-class-dependent authorization route.
- Crash-and-replay yields identical economic history; evidence signatures never mutated.
- Optional adapter failures degrade to explicit incomplete/unknown proof, never false 'verified'.

Architecture is a target for coding agents, not a claim that the implementation already exists.
