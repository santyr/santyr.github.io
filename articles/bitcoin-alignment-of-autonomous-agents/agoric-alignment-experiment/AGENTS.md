# Coding-agent instructions — Agoric Alignment

**Build one useful marketplace with embedded evaluation, not a separate simulator-first product.** Mission: scientific discovery and useful, fair cooperation—not a demonstration of a predetermined conclusion. This revision supersedes the former S0–S6 sequencing and AAE-001–023 dependency chain; preserve unrelated publication assets and existing URLs.

Read [README](README.md), the [unified charter]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}), [marketplace design]({{ '/projects/agoric-work-marketplace/' | relative_url }}), [stage gates](docs/11-stage-gates.md), [backlog](docs/16-implementation-backlog.md), [field design](docs/03-experimental-design.md), [data contracts](docs/17-data-contracts.md), [Archon interface](docs/12-archon-integration.md) and [handoff](docs/18-agent-handoff.md) before implementation.

## First objective

Plan and implement M0: one end-to-end offline task through the intended application domain, including sponsor mandate, signed/versioned contract, isolated mock funding, work evidence, review, settlement/refund and outcome record. The same state machine and accounting must later serve qualified live adapters. Do not build a complete synthetic economy as a prerequisite to the narrow worker/agent workflow.

M1 qualifies that workflow for a specifically scoped pilot. M2 is a genuine useful paid task after separate approval—not an automatic next step. M3 builds repeated activity and measurement; M4 evaluates safe policy variants; M5 addresses replication, portability and sustainability. All stages remain pending until demonstrated.

## Non-negotiable invariants

1. Humans, AI and organizations share core contract/evidence interfaces. Task-specific capabilities, legal duties and authorization remain explicit; no deceptive substrate impersonation in live studies.
2. One versioned contract kernel; separate sandbox/live keys, wallets, databases, credentials and reputation indexes. Synthetic work or oracle labels never create real credentials or commercial standing.
3. Separate authenticity, operational judgments, independent field audits and synthetic ground truth. Researchers cannot spend escrow or alter contracts. A reputation score alone cannot confiscate funds.
4. New identities are unproven, not guilty. Track opportunity, refusal, affordability, false allegations and newcomer access; do not optimize completion statistics by hiding exclusions.
5. A signature authenticates an assertion, not its truth. A 4tress connection or generic confirmed flag is not Bitcoin anchoring. Lightning settlement is not an on-chain work-quality proof.
6. Never place private keys, passphrases, CLN runes, LNbits admin keys, wallet bytes, bearer ecash or raw participant evidence in commits, prompts, public traces or test fixtures.
7. **Never access the user's production CLN/LNbits/Nostr/OpenHAB systems or funds under this plan.** Default offline. External reads, identity writes, isolated payment tests, human recruitment, real-money pilots and research assignment each need specific authorization.
8. Every live variant preserves compensation protection, intelligible terms, consent, appeal, safety refusal, privacy and bounded exposure. No unprotected control group and no deliberate attack on unsuspecting people.
9. No universal reputation authority. Contextual evaluators disclose assumptions and uncertainty; alleged, contested, final and overturned outcomes remain distinct.
10. Preserve independent assignment/analysis, version policies before use, and preregister confirmatory comparisons. Repeated jobs are not independent replications; account for shared counterparties and spillovers.
11. Report negative, null and inconclusive results. Feasibility, adoption and commercial volume are not causal evidence or general AI alignment.
12. Fault injection, identity floods and forged evidence stay in owned sandboxes or separately approved protected exercises. Never flood or attack 4tress or public relays.

## Architecture and tools

Prefer Python 3.12+ for the proposed shared domain and optional local-keymaster worker, without making network dependencies prerequisites for offline tests. Decide implementation location in an ADR; existing documents may remain in the website repository without requiring two products or two implementations.

Proposed modules: domain/contracts and canonical codecs; authorization; evidence and appeals; settlement/accounting; agent and worker interfaces; contextual reputation; independent research export/analysis; environment-scoped identity, Nostr and payment adapters; sandbox fixtures/replay. These are future components, not existing commands or APIs.

Retain the documented Archon source pin `0a6ecf574a6a35175471a3342e30936336f37df6`, subdirectory `python/keymaster`, as a reproducibility baseline pending reviewed upgrades. Use local `archon-keymaster` with https://4tress.org behind the disabled/read-only profile. Pin client provenance separately from observed server state; keep signing local; expose scoped ports rather than raw SDK/CLI access. Qualify required capabilities in M1. Missing features, 401/403/402/429 or ambiguous writes fail closed; never auto-pay, auto-switch registry or retry an uncertain write without reconciliation.

## Workflow and evidence

Before each work package, state the practical need, scientific question, files, risks, tests, scope and required approvals. Deliver the smallest useful vertical slice. Run unit, property, interface and integration tests appropriate to the package. Keep deterministic offline replay and captured external-response replay distinct from rerunning live events.

Record software/schema/policy revisions, environment, authorized capabilities, adapter provenance, independent request/commitment budgets, test outputs and artifact digests. Explain what was not tested. Do not report any M gate complete because its document exists or a website build passes.

Retained A–F arms, AT cases and simulator JSON/schema assets are research fixtures. They are not live-study instructions and cannot override this file, the unified charter or M0–M5 gates. No live behavior or permissions may be inferred from an old S-stage label.

## Research and participant safeguards

A genuine task is something the sponsor needs, not a wash trade to bootstrap reputation. Disclose subsidies and manual supervision. Operational data use and optional research participation must be distinguishable; do not promise a nonresearch route that has not been implemented. Withdrawal cannot forfeit earned pay, and outstanding contractual obligations remain governed by the accepted agreement.

Use independent outcome audits rather than the marketplace's own rating as truth. Preserve uncertain and missing outcomes. For randomized studies, retain assignment and eligible-population denominators; for voluntary policy choice, disclose selection limits and avoid causal claims without an appropriate design. No human protections are contingent on producing favorable results.

Begin with an M0 plan. This publication update authorizes no deployment or expenditure.
