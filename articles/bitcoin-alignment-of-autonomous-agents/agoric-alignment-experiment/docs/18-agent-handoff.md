# 18 — Unified application-led coding-agent handoff

Use this as the project goal after reading the linked documents. It authorizes planning and scoped implementation work, **not deployment, production-wallet access, human recruitment or spending**. All M gates remain pending.

## Goal

Develop **Agoric Alignment as one application-led research program**. Its first operating implementation is the Agoric Work Marketplace, and the marketplace is the primary real-world environment for testing its incentive mechanisms. Build useful work and the means to evaluate it together. Do not implement a separate simulator-first economy and postpone the application until it produces favorable results.

Read [AGENTS](../AGENTS.md), [program charter]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}), [marketplace design]({{ '/projects/agoric-work-marketplace/' | relative_url }}), [escrow study]({{ '/projects/agoric-work-marketplace/economic-accountability.html' | relative_url }}), [assurance patterns]({{ '/projects/agoric-work-marketplace/marketplace-assurance-patterns.html' | relative_url }}), [field design](03-experimental-design.md), [gates](11-stage-gates.md), [backlog](16-implementation-backlog.md), [data contracts](17-data-contracts.md) and [integration requirements](12-archon-integration.md).

## First deliverable: M0, not a full simulated market

Produce an M0 implementation plan identifying the smallest useful low-risk task category, domain objects, application interfaces, environment boundaries, threats, tests, files and unresolved decisions. Select an implementation location through an ADR without splitting the program into two contract engines. Preserve all existing website/essay assets and publication URLs.

Then implement one offline vertical slice through the actual intended contract domain: sponsor mandate, task/offer, signed revision, simulated protected funding, work evidence, review/dispute, settlement/refund and outcome attestation. Demonstrate deterministic replay, conservation, idempotence, unique reservation, refusal/cancellation, missing evidence and outage recovery. Use fake keys/value visibly marked as synthetic. The same transition/accounting implementation must later support qualified live adapters.

A 100-agent tournament, all A–F treatments, sophisticated reputation marketplace, pooled collateral and a complete anchoring comparison are not prerequisites. Retained synthetic scenarios are test fixtures and research extensions, never sources of real reputation.

## Subsequent work and permissions

M1 adds the narrow worker UI and bounded agent tools; qualifies required identity/payment/evidence adapters; and completes the pilot safety case, recovery drills, compensation/consent/data policies and appropriate review. M2 runs a separately approved genuinely useful paid task. M3 establishes repeat opportunities, independent counterparties and credible measurement. M4 executes an approved safe field comparison and independent analysis. M5 addresses replication, portability and sustainable demand.

Use AA-001–012 from the [new backlog](16-implementation-backlog.md). M0–M5 supersedes S0–S6 and the old mandatory AAE dependency chain. Old S labels in preserved references do not grant authority or block the new path except where a concrete safety requirement remains applicable.

Never access production CLN/LNbits/Nostr/OpenHAB or personal wallets. Remote reads, public writes, integration value, real money, participants and research assignment have distinct approval scopes. Missing safe escrow or consent blocks the pilot. If a required feature is absent, document the block or propose a reviewed alternative; do not silently substitute custody, keys, host, chain or funding rail.

## Required integration constraints

Retain https://4tress.org with local Python `archon-keymaster` as the selected identity interface. The documented source baseline is `0a6ecf574a6a35175471a3342e30936336f37df6`, subdirectory `python/keymaster`, declared 0.7.0/Python >=3.12. It is a historical pin, not a claim about current server software. Review any upgrade and lock dependencies. Start with mocks and separately approved bounded preflight using the disabled/read-only profile.

Keep signing and wallet secrets local; reject inherited personal-wallet paths and conflicting node variables. Pass the origin to the pinned Gatekeeper client, which appends its API path. Enforce request/deadline/write budgets; handle 401/403/402/429, missing registry, ambiguous writes and unknown server state explicitly. No automatic payment of challenges or blind write retries. Independent verification is not repeated queries to the same endpoint. Do not attack public infrastructure.

Cashu is the preferred routine payment candidate with Lightning interoperability, not a presumed working escrow. Demonstrate actual optional-condition enforcement, verified funding, redemption/custody assumptions, authorized destinations, fees, timeout/dispute recovery and no double pledging. Separate job pay, expenses, bonds and service fees. Reputation can affect future risk terms; it is not a signing key for confiscation.

## Research built into the product

Version operational contracts and policy models from the start. Separate service records, optional consented research enrollment/assignment and independent outcome audits. Research components have no production signing or contract-changing authority. Keep synthetic/live identities, keys, databases, credentials and reputation indexes isolated.

First prove a useful task can work. Later compare a precise fixed-versus-history-sensitive economic policy with the same safety/payment floor and comparable unrelated factors. Account for shared counterparties, persistent reputation, selection and independent sample units. Preregister confirmatory outcomes and analysis before examining them. Track refusals, entry barriers, affordability and newcomers, not only completed jobs. Audit outcomes independently rather than using the reputation score as ground truth.

Protect third parties, consent and earned compensation in every arm. No deliberate fraud against unsuspecting participants or fabricated public history. Declare subsidy and manual supervision. Feasibility is not causal validation, adoption is not alignment, and simulated scores are not field evidence. Publish negative and uncertain results.

## Report format and definition of done

After each package report: gate/package; design and code/schema/policy revisions; touched files; actual commands and outputs; tested invariants; artifact digests; observed result; environment and permission scope; incidents; unknowns and deviations; remaining risks; next action requiring approval. Qualify claims rather than presenting unexecuted commands as evidence.

M0 is done only when the shared-domain offline workflow and relevant tests reproduce without external dependencies or secrets. M1 needs actual qualified adapters and a reviewed pilot case. M2 needs real authorized work and verified fair settlement. Later gates need their specified evidence, not favorable anecdotes. The [evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) records those distinctions.
