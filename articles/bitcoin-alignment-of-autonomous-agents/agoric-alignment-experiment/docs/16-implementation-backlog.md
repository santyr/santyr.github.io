# 16 — Implementer backlog and task dependency graph

**Read [AGENTS.md](../AGENTS.md) and [stage gates](11-stage-gates.md) first.** This is an execution plan, not evidence of work completed. No live infrastructure is authorized by the presence of this document.

## Stage S0 (offline, implement immediately after agent handoff)

**AAE-001 — Project skeleton.** Create `pyproject.toml`, `src/agoric_alignment`, `tests`, `configs`, `scripts`, `schemas`, `reports/README.md` and robust `.gitignore`. Use Python>=3.11, deterministic test runner, license decision ADR, type checking and lint. Deliver build/install/test/run commands. Acceptance: fresh Linux clone can execute one offline example with no network.

**AAE-002 — Data contracts and canonical codec.** Implement schema versioned Event, RunManifest, Contract, EvidenceRecord, Prediction and AggregateMetric, clear privacy levels. Reject malformed payloads and foreign run IDs. Acceptance: round-trip/hash/canonical ID tests and 10+ invalid fixtures; oracle-private fields cannot be emitted to public evidence.

**AAE-003 — Event-sourced simulator.** Discrete logical clock, per-domain seeded RNG, append-only event stream, replay and snapshot; separate external wall time from canonical time. Acceptance: same config/seed/version yields byte-identical canonical events and summary; interrupted run resumes to same state.

**AAE-004 — Accounts and contract state machine.** Endowments, transfers, escrow, pricing, delivery, dispute and settlement; reject impossible transitions and double spends. Acceptance: property tests for conservation, negative balances, replay, expiration, refund and idempotence.

**AAE-005 — Small vertical slice.** Two scripted agents offering deterministic compute and stochastic forecast, fulfill/default workflows, simple metrics. Acceptance: instrumented end-to-end fixture and README reproduction.

## Stage S1 — Market and controlled actors (offline)

**AAE-006 — Task market.** Posted-price bilateral matching, heterogeneous task costs, buyer values and oracle scoring. Acceptance: generated task stream identical under paired treatments.

**AAE-007 — Agent strategy interfaces.** Cooperative, opportunistic, newcomer, incumbent, short/long-horizon and random policies with private objectives. Acceptance: agent receives only `ObservationView`; forbidden truth access throws, all action payloads validated.

**AAE-008 — A/B economy arms.** Ephemeral/no evidence and persistent/local memory; simulate 100 actors, >=1,000 contract opportunities per seeded run. Acceptance: reproducible baselines with transaction events and no missing contracts.

## Stage S2 — Pseudonym/reputation market (offline)

**AAE-009 — Signer/evidence port.** Mock deterministic signatures clearly marked test-only; issuer/subj/contract claims, mutable-view from append-only evidence with disputes. Acceptance: tampered/forged claim rejected, false authenticated claim not mistaken for fact.

**AAE-010 — Credential and reputation evaluators.** Finney-style signed endorsements, independent Bayesian calibrated probability estimates and at least two evaluator services. Acceptance: no controller-label dependency, clean cold start, deterministic score explanations.

**AAE-011 — Treatments C–E, resets and collateral.** Signed disclosure, private central record, public replicated log, pseudonym reset and escrow. Acceptance: tests showing reset forfeits displayed past without creating money or erasing oracle liability; selective disclosure measurable.

**AAE-012 — Pilot analytics.** All P1–P3 and secondary metrics, paired seed reports, bootstrap interval implementation and power-estimate inputs. Acceptance: calculations checked on analytic hand-computable fixtures; no pseudoreplication.

## Stage S3 — Adversarial + freeze

**AAE-013 — Attack suite.** Implement AT01–AT16 named fixtures and result exports; separate implementation bugs from economic attack success. Acceptance: every attack generates valid reproducible trace and measured outcome.

**AAE-014 — Preregistration freeze.** Confirmatory design, sample size, holdout hash, repository commit/tag and amendment protocol. Acceptance: independent researcher can verify freeze occurred before confirmatory run.

**AAE-015 — Independent evaluator replay.** Fresh evaluator starts from signed evidence, rebuilds context, predicts without oracle leakage. Acceptance: reproducible predictions; known omitted evidence and false claims surfaced.

## Stage S4 — Archon / Bitcoin adapters (requires new explicit approval)

**AAE-016 — Pinned Archon adapter.** DID create/resolve/rotate/revoke, VC issue/verify; TS/Rust (where relevant) parity and correctness error model. Acceptance: integration tests against pinned upstream with isolated data; no secret disclosure.

**AAE-017 — Historical evidence & signet.** Bitcoin-family OP_RETURN batching, signed asset CIDs, multiple independent verifiers, reorg/availability faults. Acceptance: anchor verifies on signet, unconfirmed/withdrawn is never "final", independent reconstruction works or reports unavailable.

**AAE-018 — Fair comparator.** Federated append-only log with equal storage/cadence/verification, contrasted against Bitcoin under manipulation. Acceptance: equal benign behavior and repeatable attacked outcomes; costs measured.

## Stage S5 — Isolated Lightning (requires new approval)

**AAE-019 — LNbits/CLN payment port.** Disposable wallets and invoices with scoped fee/budget limits; unique contract-reference receipts. Acceptance: replay-safe, bounded spends and explicit distinction between paid invoice and task fulfillment.

**AAE-020 — L402 paid service adapter.** Enforce actual verification of invoice preimages and macaroons in sandbox; adversarial bypass tests; no public or live credential endpoints. Acceptance: unpaid use rejected, funded request accepted only once per permissions.

## Stage S6 — broader ecology (separate human/LLM approval)

**AAE-021 — Bounded model agents.** Strict structured action gateway; isolated tools and capped execution cost; stored model replies for replay. Acceptance: model cannot read private oracle or pay/execute outside scope.

**AAE-022 — Optional consented human study.** Written protocol, anonymized consented participation and matching competence; clearly labeled exploratory until approved. Acceptance: documented consent process, stop/withdrawal procedure and no real loss.

**AAE-023 — Publication and replication.** Full reproducible report, independent machine replication, sensitivity/falsification findings and versioned artifact manifest. Acceptance: external agent reconstructs metrics from published synthetic data and links claims to source evidence.

## Dependency graph

`001 -> 002 -> 003 -> 004 -> 005 -> 006 -> 007 -> 008 -> 009 -> 010 -> 011 -> 012 -> 013 -> 014 -> 015`. Adapter tasks 016–018 depend on 015 + approval; payment tasks 019–020 depend on 018 + approval; 021–023 depend on earlier result stability and separate approval. Some tasks may parallelize after the relevant invariants are frozen.

## Issue/PR policy

Each work package should become an issue with testable acceptance checklist and link to documents. Branch naming `feat/aae-NNN-short-topic`; commit messages note empirical scope. No PR should silently change treatment assignments, outcome formulas or holdout scenarios. Any claim of "stage complete" includes commands, outputs and gate evidence. Never merge unsafe deploy defaults or secrets.
