# 16 — Implementer backlog and task dependency graph

Read [AGENTS.md](../AGENTS.md), [stage gates](11-stage-gates.md) and [12 — 4tress/archon-keymaster interface](12-archon-integration.md) first. This is an execution plan, not evidence of completed work or permission for live deployments.

## Stage S0 — offline

**AAE-001 — Project skeleton.** Create `pyproject.toml`, `src/agoric_alignment`, `tests`, `configs`, `scripts`, `schemas`, `reports/README.md` and `.gitignore`. Offline floor Python >=3.11; prefer >=3.12 for the optional archon-keymaster integration, or use a separate >=3.12 worker. Add build/install/test/run commands, type/lint checks and license ADR. Acceptance: a fresh clone runs an offline example without network or installed Archon dependencies.

**AAE-002 — Data contracts and canonical codec.** Implement versioned Event, RunManifest, Contract, EvidenceRecord, Prediction and AggregateMetric. Add the separate Archon profile contract and manifest 1.1 remote provenance while retaining legacy manifest 1.0 validation. Reject malformed data and cross-run IDs. Acceptance: round-trip/hash tests, 10+ negative fixtures, no oracle fields in public records, no enabled network/payment in shipped profiles.

**AAE-003 — Event-sourced simulator.** Logical clock, independent RNG streams, append-only events, snapshots and replay. Acceptance: byte-identical canonical events/metrics for fixed inputs; resumed run matches uninterrupted run.

**AAE-004 — Accounting and contract states.** Endowments, transfers, escrow, prices, delivery, dispute, settle/refund; reject illegal transitions and double spends. Acceptance: conservation, replay, expiration, refund and idempotence properties.

**AAE-005 — Vertical slice.** Two scripted agents with compute/forecast and fulfill/default workflows plus metrics. Acceptance: instrumented offline fixture with a reproduction command.

## Stage S1 — market and controlled actors

**AAE-006 — Task market.** Posted-price bilateral matching, heterogeneous costs, buyer value and oracle scoring. Acceptance: identical generated exogenous task streams under paired treatments.

**AAE-007 — Strategy interfaces.** Cooperative, opportunistic, newcomer, incumbent, short/long horizon and random policies. Acceptance: ObservationView only, forbidden truth access rejected, actions validated.

**AAE-008 — A/B arms.** Ephemeral/no-evidence and persistent/local-memory economies with 100 actors and >=1,000 opportunities. Acceptance: reproducible matched baselines, no missing contract/accounting state.

## Stage S2 — reputation and identity economics

**AAE-009 — Signer/evidence port.** Clearly labeled simulated signatures, issuer/subject/contract claims, append-only contestation. Acceptance: tampering rejected; authenticated false assertion not treated as fact.

**AAE-010 — Credentials/evaluators.** Signed endorsements, contextual Bayesian estimates and multiple independent evaluator services. Acceptance: substrate blindness, uncertainty at cold start, reproducible explanations/calibration.

**AAE-011 — C–E, resets and collateral.** Subject-disclosed credentials, private authenticated records, public log, pseudonym resets and escrow. Acceptance: resets forfeit displayed reputation without creating money; omission and newcomer effects measurable.

**AAE-012 — Pilot analysis.** P1–P3 and secondary metrics, paired seeds, bootstrap intervals and pilot power inputs. Acceptance: hand-computable analytic fixtures pass and transactions are not treated as independent replicas.

## Stage S3 — adversarial tests and freeze

**AAE-013 — Attack suite.** AT01–AT16 reproducible fixtures with separate coding-defect and economic-attack outcomes. Acceptance: every attack has evidence, trace and measured result.

**AAE-014 — Preregister.** Freeze confirmatory design/sample size, code, holdout digest and amendment policy. Acceptance: independent reviewer can verify freeze preceded holdout results.

**AAE-015 — Independent evaluator replay.** Rebuild beliefs from permitted signed evidence, without oracle access. Acceptance: reproducible predictions, omissions and false claims reported honestly.

## Stage S4 — 4tress / archon-keymaster (explicit approval)

**AAE-016 — Preferred client adapter.** Wrap the local Python archon-keymaster SDK pinned to source `0a6ecf574a6a35175471a3342e30936336f37df6`, subdirectory `python/keymaster` (source version 0.7.0, Python >=3.12). Use https://4tress.org as the selected remote node. Validate configs/archon-4tress.json, reject unsafe inherited configuration, isolate wallets, enforce capabilities/request budgets and expose structured ports rather than arbitrary wallet commands. No full local stack or MCP installation is required to begin.

Start with mocked SDK boundary tests, then approved bounded read-only readiness/registry checks, then separately approved two-identity synthetic smoke tests for create/resolve/rotate/revoke and credential issue/verify. Acceptance: local signing, no secrets/oracle fields sent remotely, no auto-pay on 402, no unsafe retry on ambiguous writes, no silent host/registry fallback, captured client/server provenance. Missing endpoint capabilities produce a documented block, not fabricated success.

**AAE-017 — Independent history and signet.** Verify signatures and issuer history independently, retain CID bytes and reconstruct with the original client offline. Use an independently operated verifier. Request BTC:signet only if advertised, approved and independently provable; a Hyperswarm `confirmed` flag does not qualify. Acceptance: valid batch/chain/depth proofs, unavailable data stays unknown, reorg handling correct. Reorgs, partitions, malicious responses and load tests run only on local fixtures or owned isolated nodes, never on 4tress. Distinguish S4a connectivity from S4b/c security evidence.

**AAE-018 — Fair comparator.** Equalize log storage/cadence/verification, economic workload and costs; compare Bitcoin anchoring with an independent transparency log under declared threats. Acceptance: repeatable benign/attacked outcomes and costs; record hosted versus local infrastructure as a separate factor.

## Stage S5 — isolated Lightning (separate approval)

**AAE-019 — LNbits/CLN payment port.** Disposable wallets, scoped budgets/fees and contract-bound receipts. Acceptance: replay-safe bounded spends, paid invoice distinguished from fulfillment. The 4tress identity profile does not authorize wallet creation or payments; check any selected payment backend separately.

**AAE-020 — L402 service adapter.** Verify preimages/macaroons in the sandbox with bypass tests. Acceptance: unpaid requests rejected; funded requests accepted only within explicit scope. Never automatically satisfy a challenge received during the hosted identity preflight.

## Stage S6 — broader ecology (separate approval)

**AAE-021 — Bounded model agents.** Structured authorized actions, no raw Keymaster/CLI or secrets, isolated tools and token/cost limits; capture model replies for replay. Acceptance: no oracle or out-of-scope payment/execution access.

**AAE-022 — Consented human study.** Written consent, withdrawal, compensation and competence-matching protocol. Acceptance: reviewed scope and no involuntary disclosure or real losses.

**AAE-023 — Replication/publication.** Reproducible full report, independent replication, sensitivity/negative findings and versioned artifacts. Acceptance: external agent reconstructs reported metrics and limited proof claims from published synthetic evidence.

## Dependencies

`001 -> 002 -> 003 -> 004 -> 005 -> 006 -> 007 -> 008 -> 009 -> 010 -> 011 -> 012 -> 013 -> 014 -> 015`. Tasks 016–018 depend on 015 plus scoped approval; tasks 019–020 on 018 plus payment approval; tasks 021–023 on stable prior results and separate authorization. Parallel work is permitted only after relevant invariants are fixed.

## Issue/PR policy

Use task issues with linked acceptance tests and `feat/aae-NNN-short-topic` branches. Never silently change treatment assignments, outcome formulas, disclosure assumptions or frozen holdouts. A stage completion includes commands, artifacts and gate evidence. Do not merge unsafe defaults or secrets. Preserve historical sources, alternative treatments and meaningful falsification criteria.
