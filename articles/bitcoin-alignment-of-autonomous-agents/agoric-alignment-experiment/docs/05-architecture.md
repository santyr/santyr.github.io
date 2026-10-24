# 05 — One application architecture with independent evaluation

The [marketplace]({{ '/projects/agoric-work-marketplace/' | relative_url }}) is Agoric Alignment's operating implementation and primary field-research environment. This is a proposed architecture, not existing software. [M0–M5](11-stage-gates.md) controls delivery; the full simulator is not a separate prerequisite product.

## Shared domain, isolated adapters

Use a versioned contract kernel for mandate checks, canonical contract revisions, offers/acceptance, funding verification, evidence submission, review, dispute, settlement/refund and outcome records. The same authorization and accounting rules serve offline fixtures and qualified live adapters. Sandbox clocks, identities, tasks and money are substituted at explicit ports; they must not hide a different escrow implementation.

Candidate ports cover identity/credentials, Nostr messaging/discovery, evidence storage, settlement rails, reviewer/arbitrator decisions, consent and research export. Nostr transports claims, Archon binds attributed identity/credentials, and the chosen wallet/mint/chain supplies financial facts. No transport event alone closes a payment obligation.

## Authority boundaries

| Component | Allowed authority | Prohibited inheritance |
| --- | --- | --- |
| Agent interface | Structured actions inside a sponsor mandate | Raw wallet admin, arbitrary CLI, secret export, unbounded subdelegation |
| Worker interface | Negotiation, acceptance/refusal, private evidence, appeals | Changing counterparties' signed terms |
| Settlement/accounting | Verify funds and authorized transfers; enforce reservation uniqueness | Executing a reputational rating as confiscation |
| Adjudication | Decide specified cases under accepted rules | Inventing retrospective penalties or overriding laws/consent |
| Reputation evaluator | Contextual risk assessment over permitted evidence | Universal truth or legal authority |
| Research pipeline | Read authorized minimized records; assign approved prospective policies through a separate control | Spending, changing existing contracts, accessing unrelated private evidence |

Keep test and live wallets, keys, databases, event namespaces, credentials and reputation indexes separate. Reject synthetic signatures or oracle labels in live paths. Agent observations, operational decisions, independent audited outcomes and hidden synthetic truth are distinct types. Logs and prompts cannot contain bearer ecash, wallet bytes, private keys or raw personal documents.

## First useful vertical slice

M0 implements one complete task offline with conservation, replay, cancellation, ambiguity and refusal tests. M1 adds a narrow human interface and bounded AI tool interface, qualified identity/settlement adapters, recovery and consent. M2 performs a separately approved useful low-risk task. Each subsequent research mechanism uses that same domain rather than a second application.

Candidate implementation is a small Python 3.12+ domain package with optional integration workers, accompanied by a minimal worker UI and agent API. Repository layout, frontend choices and exact APIs require a documented implementation decision; the publication does not assert those components exist. A large market simulator, global collateral pool or sophisticated reputation engine is not needed to begin.

## Research built in, not unrestricted telemetry

Record environment and contract/policy/schema/software revisions in operational events. Include research enrollment/assignment references only under the approved data policy, preserving a distinction between service and research. Minimize linkage and retain withdrawal/retention limits. Analysis consumes immutable extracts, not production signing capabilities.

Use independent outcome audits and a versioned evidence register. Capture external responses for replay, recognizing that repeating live calls cannot reproduce a past network state. Frozen confirmatory policy versions cannot be retuned against the holdout under the same study identifier. Safety changes pause or amend the study transparently.

## Infrastructure assumptions

Retain local Python `archon-keymaster` with https://4tress.org and the qualification and independent verification requirements in [12](12-archon-integration.md). Cashu/Lightning remains the preferred routine payment design direction subject to actual custody and recovery qualification; use a reviewed alternative or stop if required conditions are absent. Payment, identity and research permissions are separate. Production CLN/LNbits/OpenHAB and personal wallets are not authorized dependencies.

Detailed objects and manifests are in [17](17-data-contracts.md); failure and incident procedures are in [13](13-operations.md). No architectural diagram or successful website build establishes financial safety or alignment.
