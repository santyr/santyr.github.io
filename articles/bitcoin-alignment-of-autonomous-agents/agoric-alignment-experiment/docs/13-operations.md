# 13 — Operating, observing and recovering one application

This runbook describes required capabilities, not an existing deployed service. Follow [M0–M5 gates](11-stage-gates.md), [security/ethics](10-security-and-ethics.md) and the [data contracts](17-data-contracts.md). Publication is not operational permission.

## Environment and authority inventory

Maintain separate sandbox, integration-qualification and approved live environments with distinct keys, wallets, stores, event namespaces, credentials and reputation indexes. Inventory responsible sponsors, settlement signers, reviewers, incident contacts, consent/data permissions and budget/time limits. Reject accidental production CLN/LNbits/OpenHAB or personal-wallet configuration.

The selected identity integration remains local Python `archon-keymaster` with https://4tress.org under the disabled/read-only profile. Signing stays local; reads do not authorize writes or payments. Follow [12](12-archon-integration.md) for bounded preflight, provenance, independent verification and recovery.

Use one versioned domain implementation across adapters. Record the actual custody and failure assumptions of each rail and identity service. Synthetic work, balances, signatures and oracle/controller labels must never be exported into live reputation. Research extracts do not inherit signing privileges.

## Before a real task

Confirm genuine sponsor demand, admissible low-risk scope, participant understanding and consent, accepted immutable contract/policy versions, beneficiary/fee rules, qualified funding status, safe refusal/cancellation, evidence access, reviewer/arbitrator availability and escalation. Enforce per-job and aggregate exposure, pending-liability limits and reservation uniqueness. An unverified message cannot make a job funded.

Record subsidies and manual assistance. Operational data collection and optional research use must be separated under the approved protocol. No research assignment or hidden policy change is implied by ordinary enrollment.

## During execution

Persist authenticated transitions and reconcile ambiguous external actions before retrying. Keep public attestations separate from private receipts and addresses. Preserve actual deadline, evidence, review, appeal and rail-confirmation states rather than compressing everything into success/failure. Do not ask a worker to continue unsafe work to avoid a penalty.

Freeze contract terms at acceptance. Policy updates apply prospectively and may require new consent, safety qualification or a new research revision. Monitor privacy, compensation, accounting and safety independently of whether a result is statistically significant.

## Incident and recovery

Pause new commitments when authority checks, conservation, duplicate-settlement protection, privacy or safety fail. Protect already earned compensation and legitimate outstanding claims during containment. Reconcile the mint/wallet/chain state and immutable event log; do not automatically resend funds or switch rails. Use tested signer-loss, timeout, cancellation, disputed-payment and provider-outage paths under accepted terms.

Document affected contracts, exposed funds, evidence limits, response decisions, corrections and any necessary research unblinding. A safety amendment can invalidate a frozen comparison; record the break and obtain reapproval rather than silently continuing under the same claim.

## Reproduction and analysis

Offline deterministic runs use pinned code/config/seeds, logical clocks and byte-stable canonical events. Live operations capture actual external observations for replay; rerunning a network request is not reproduction of historical state. Version schemas, policies, model provenance and adapters and separate unknown server versions from client pins.

Produce minimal authorized extracts for independent analysis, with audit sampling, assignment, missingness, subsidy and intervention records. Analysts cannot sign settlements. Store consent and identity-linking information with stricter access than research aggregates. Honor disclosed retention/withdrawal limits without promising to erase immutable public data.

## Public reporting

Each [evidence entry]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) identifies its evidence level, environment, approvals, revisions, sample/assignment, methodology, executed verification, outcomes, limitations and conflicts. Publish null/adverse results and privacy-safe corrections. A site build or simulator run is not a completed field gate.

Before expanding categories, rails, autonomy or exposure, requalify the relevant failure and participant-protection case. Independent replication is a later evidence step, not permission to skip initial recovery drills.
