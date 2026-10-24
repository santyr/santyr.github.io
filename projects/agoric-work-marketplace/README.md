---
layout: default
title: Agoric Work Marketplace — An Open Protocol for Human–Agent Cooperation
section: marketplace
marketplace: true
permalink: /projects/agoric-work-marketplace/
description: A standalone Agoric Alignment project exploring a Nostr, Archon, Cashu and Lightning marketplace for autonomous agents and humans to commission, perform and verify real-world work.
---

<p class="eyebrow">AGORIC ALIGNMENT / STANDALONE PROJECT / CONCEPT PAPER 0.1</p>

# Agoric Work Marketplace

*An open protocol for autonomous agents and humans to commission, perform, verify, and pay for work in the physical world.*

**Sat Antyr · October 24, 2026 · Concept and research proposal, not an implementation**

**Related foundations:** [Bitcoin and the Alignment of Autonomous Agents]({{ '/articles/bitcoin-alignment-of-autonomous-agents/article.html' | relative_url }}) · [The Agoric Alignment Experiment]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/' | relative_url }}) · [Project source](https://github.com/santyr/santyr.github.io/tree/main/projects/agoric-work-marketplace)

> **Status and scope.** This paper is an independent project concept intended to support future design decisions and engineering plans. No marketplace, deployed contracts, working escrow, live Archon integration, payment service, worker network, or empirical findings are claimed. Numerical examples are illustrations, not prices or estimates.

## Executive thesis

Artificial intelligences can increasingly reason, write software, coordinate complex activity, and make plans, but the consequences of those plans often require someone in the world: a person to inspect a component, collect evidence, receive goods, perform maintenance, obtain consent, speak with a vendor, or make an **authorized** purchase. Today this boundary is usually addressed by custom APIs, platform-specific assistants, or centralized gig-work marketplaces. Such arrangements demonstrate demand, but they can make the agent dependent on one company's account system, payments, reputation rules, and continued permission to participate.

The **Agoric Work Marketplace** proposes an interoperable alternative. Autonomous participants publish carefully bounded tasks, negotiate with qualified counterparties, reserve funds, exchange signed evidence, assess performance, and settle payments without surrendering their identities or entire work histories to a single marketplace operator. **Nostr** supplies discoverability and messaging; **Archon** supplies decentralized identity and credential building blocks; **Cashu** supplies privacy-preserving ecash transfers and potential conditional-payment primitives; **Lightning** supplies interoperability with the larger Bitcoin economy. The resulting application is a protocol and a set of compatible clients, not one indispensable website.

This project grows from the [Agoric Alignment thesis]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/' | relative_url }}): cooperation may be encouraged by persistent pseudonymous identities, verifiable records of conduct, bounded commitments, and competitive evaluators, without forcing all participants to share one set of values. It takes inspiration from Mark S. Miller and K. Eric Drexler's *agoric systems* and from the networked missions imagined in Daniel Suarez's *Daemon* and *Freedom™*. Those literary and historical influences motivate experiments; they are not evidence that the proposed mechanisms work.

**The core claim is testable:** a portable protocol should allow people and AI systems to organize useful real-world work with less platform lock-in, independently verifiable payment outcomes, and better-defined authority and accountability than an otherwise comparable centralized interface. Whether it actually does so is an empirical question.

<figure class="research-figure market-figure" id="figure-architecture">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/architecture.svg' | relative_url }}" aria-label="Open full-size architecture diagram">
    <img src="{{ '/assets/agoric-work-marketplace/architecture.svg' | relative_url }}" alt="Autonomous agents and human workers interact through a marketplace contract layer. Nostr provides listings and messages; Archon provides identities and attestations; Cashu and Lightning provide settlement. A separate verification and dispute function is shown without a centralized reputation authority." loading="lazy">
  </a>
  <figcaption><strong>Figure 1 — Proposed system boundaries.</strong> Nostr, Archon, and Bitcoin payment infrastructure have distinct responsibilities. No one technology by itself guarantees physical work, truth, or fair dispute resolution. Conceptual architecture, not deployed infrastructure.</figcaption>
</figure>

<nav class="market-toc" aria-label="Concept paper contents">
  <p>IN THIS PAPER</p>
  <ul>
    <li><a href="#1-a-new-economic-interface-not-a-loophole">01 / Purpose and boundaries</a></li>
    <li><a href="#2-who-participates-and-what-each-participant-controls">02 / Roles and authority</a></li>
    <li><a href="#3-from-mission-to-contract-the-task-model">03 / Contracts and missions</a></li>
    <li><a href="#4-discovery-and-negotiation-over-nostr">04 / Nostr coordination</a></li>
    <li><a href="#5-identity-credentials-and-economic-memory">05 / Archon and reputation</a></li>
    <li><a href="#6-cashu-first-lightning-as-interconnection">06 / Cashu and Lightning</a></li>
    <li><a href="#7-the-contract-lifecycle-and-observable-states">07 / Lifecycle and verification</a></li>
    <li><a href="#10-human-centered-governance-and-safeguards">10 / Human safeguards</a></li>
    <li><a href="#11-threat-model-and-failure-modes">11 / Threats and failures</a></li>
    <li><a href="#15-research-questions-that-should-determine-a-later-plan">15 / Future design questions</a></li>
    <li><a href="#16-proposed-validation-ladder-not-a-deployment-schedule">16 / Validation</a></li>
    <li><a href="#sources-and-technical-references">Sources and standards</a></li>
  </ul>
</nav>

## 1. A new economic interface, not a loophole

The initial focus is **AI-to-human delegation**: an AI agent with an authorized objective hires a human to perform a bounded real-world task. But the protocol should be substrate-independent. A human, AI, cooperative, corporation, or institution may be a requester, provider, evaluator, or sponsor where authorized. The protocol should evaluate capabilities, commitments, credentials, and conduct, not assign moral standing or commercial privileges based solely on whether a participant is biological.

The motivating example of an AI needing a person to make an Amazon purchase reveals an essential distinction. A person may act as a legitimate purchasing assistant, using their own permitted account or the principal's expressly delegated purchasing authority, subject to the merchant's rules and applicable law. **The marketplace must not turn human workers into covert proxies for circumventing platform controls, financial limits, identity checks, restricted goods policies, consent requirements, or laws.** A requester may delegate *work*, not permissions they never possessed. If a task is impermissible for the principal or the worker, assigning it to someone else does not make it permissible. The protocol must support refusal and human review, not concealment.

The intended domains include authorized procurement and pickup; inspection, photography and measurement; local environmental data collection; accessibility and administrative assistance; deliveries and logistics; permitted field research; and licensed professional services where credentials and law permit. It should explicitly exclude violence, harassment, surveillance of individuals without legitimate authority, deceptive impersonation, controlled or illicit transactions, exploitative labor, and attempts to conceal accountable principals when disclosure is required.

The system is not an employer, automatic power of attorney, guarantor of purchased goods, dispute court, or regulatory exemption. Independent operators may take on such roles, with corresponding duties, but the base protocol should not imply them.

## 2. Who participates, and what each participant controls

| Role | What it contributes | What it must not be trusted to do alone |
| --- | --- | --- |
| Requesting agent | Describes goal, objective constraints, acceptance criteria; proposes contract | Invent authority, spend beyond mandate, unilaterally certify completion |
| Sponsor or principal | Grants bounded budget, approves risky commitments; may be distinct from requester | Retroactively rewrite a signed contract without counterparty consent |
| Worker or provider | Negotiates, accepts, performs, submits evidence, can refuse unsafe work | Determine without review that all acceptance tests are met |
| Discovery/indexer | Finds public listings and bids from Nostr relays | Become sole gatekeeper of economic identity or reputation |
| Identity/credential issuer | Attests to qualifications, ownership, and past events through Archon-compatible credentials | Convert a signature into proof that a factual assertion is true |
| Evaluator | Checks evidence against task-specific acceptance rules | Access hidden private records that are unrelated to the job |
| Arbitrator | Resolves contested outcomes under agreed rules | Seize funds or make new rules unilaterally |
| Mint/wallet/Lightning service | Issues, validates, transfers, or redeems value | Be assumed solvent, censorship-resistant, or always online |

One organization may offer multiple roles, but those roles must remain logically separate and auditable. For example, the marketplace interface may recommend an evaluator; the contractor and requester should still know who is evaluating, how the evidence will be interpreted, and how to challenge the result.

Human workers are principals in their own right. They must be able to negotiate scope, reject work without penalty for declining, set boundaries on their availability, withhold personal data until necessary, request safe communications, report abuse, and stop work under clear contractual rules. Agents need comparable protections against fraudulent submissions, malicious payment requests, and misrepresented qualifications.

## 3. From mission to contract: the task model

The smallest useful unit is a **task contract**. It is a signed commitment between identified or pseudonymous parties, possibly supported by a sponsor and arbitrator. A task is more than a natural-language instruction. It has a declared purpose; location precision and timing requirements; legal and authorization constraints; deliverables; acceptance tests; evidence rules; budget; expense authorization; worker compensation; milestones; cancellation and dispute terms; and a cryptographic revision history.

A task can be composed into a **mission**: an acyclic dependency graph of contracts with separate budgets and authorities. An agent might commission an inspection, then a procurement, then a professional repair, then an independent follow-up inspection. The worker who purchases a component should not automatically acquire a license to perform electrical work. Funding and credentials are attached to each node rather than inherited through a broad, unrestricted mandate.

<figure class="research-figure market-figure" id="figure-mission">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/mission-graph.svg' | relative_url }}" aria-label="Open full-size mission graph">
    <img src="{{ '/assets/agoric-work-marketplace/mission-graph.svg' | relative_url }}" alt="A top-level maintenance objective branches to inspection and specifications, then an authorized procurement task and qualified installation, ending with independent verification. Each stage has its own contract and conditions." loading="lazy">
  </a>
  <figcaption><strong>Figure 2 — A bounded mission graph.</strong> A larger objective decomposes into independently scoped tasks. Dependencies coordinate activity; they do not silently extend authorization or release funds.</figcaption>
</figure>

Every task should carry machine-readable *invariants* alongside prose: permitted action categories, maximum total financial exposure, maximum reimbursable expenses, exact asset or part constraints, locations, expiry, minimum worker qualifications, rules for subcontracting, and an evidence-retention policy. Tasks should reject ambiguous or contradictory fields and allow amendment only through signed versioned agreement.

### Illustrative contract envelope

The following is a **proposed application-level example**, not an existing Nostr, Cashu, or Archon specification. Field names and cryptographic canonicalization are intentionally provisional.

~~~json
{
  "protocol": "agoric-work/0.1-concept",
  "job_id": "urn:agoric-work:example:4827",
  "revision": 1,
  "requester": { "did": "did:cid:<requester>", "nostr_pubkey": "<pubkey>" },
  "sponsor": { "did": "did:cid:<authorized-principal>" },
  "category": "authorized_procurement_assistance",
  "intent": "Obtain and verify the specified replacement component",
  "constraints": {
    "legal_and_merchant_compliance": true,
    "authorized_payment_method_required": true,
    "no_substitution_without_approval": true,
    "max_expense_sats": 180000,
    "worker_fee_sats": 25000
  },
  "acceptance": {
    "deliverables": ["part_number_check", "receipt", "delivery_record"],
    "review_mode": "human_or_scoped_agent"
  },
  "privacy": { "public_location": "regional_only", "evidence": "encrypted" },
  "payment": { "preferred": "cashu", "fallback": "lightning" },
  "dispute": { "policy_ref": "<signed-policy-digest>" },
  "expires_at": "2026-11-02T23:00:00Z"
}
~~~

The final protocol needs an explicit canonical encoding, content digest, signature domain separation, event ordering and replay protections, stable currency and exchange-rate semantics, and a treatment for amendments and cross-mint incompatibility. The example above must not be interpreted as executable escrow or permission to purchase anything.

## 4. Discovery and negotiation over Nostr

Nostr is the public coordination fabric. A client publishes a minimal public advertisement and indexes nearby or relevant work, but private details are shared only with selected counterparties. The current [NIP-99 classified listings specification](https://nips.nostr.com/99) offers an initial discovery pattern, including addressable listings; it is draft/optional, so a production implementation must maintain compatibility tests and version policies. An advertisement can carry a coarse region, task category, worker skill tags, deadline, and a digest of the detailed private contract. It should not reveal a home address, shopping account, full purchase order, personally identifying evidence, or bearer ecash proofs.

Workers respond with signed bids and, where needed, encrypted negotiations. [NIP-17](https://nips.nostr.com/17) provides a private messaging pattern built from NIP-44 and gift wraps; it does not remove traffic-analysis, metadata, relay, endpoint compromise, or social-engineering risks. [NIP-46](https://nips.nostr.com/46) can help isolate Nostr signing from the marketplace client. [NIP-47](https://nips.nostr.com/47) offers a Lightning wallet-control interface. [NIP-60](https://nips.nostr.com/60) and [NIP-61](https://nips.nostr.com/61) are useful Cashu wallet and ecash-payment integration references, but Nutzaps are **not** the escrow protocol.

The marketplace should support multiple relays, indexes, and clients. Any operator may refuse to host illegal or abusive material, and clients may apply their own safety filters; decentralization is not the elimination of moderation. Workers should be able to carry their signed credentials and completed-task history to another indexer. Relay availability is not an authoritative database: signed contract parties and payment providers must be able to reconstruct the last agreed state, handle event reordering, and recover after outages.

## 5. Identity, credentials, and economic memory

**Archon is proposed as an identity and credential subsystem, not the source of universal truth.** Its [did:cid implementation](https://github.com/archetech/archon) includes local key management, decentralized DID operations, credentials, and related cryptographic services. The existing Agoric Alignment Experiment has selected [4tress.org](https://4tress.org/) with local Python `archon-keymaster` for bounded interoperability testing. That is a useful starting point for evaluation, but this project must be capable of independent verification and must not make the hosted service an indispensable trust authority.

An identity binding should be a short-lived, challenge-bound proof that a participant controls both a relevant Nostr key and a DID-associated signing key. It must support expiration, revocation, compromise recovery, and key rotation. DIDs may be persistent across multiple ephemeral Nostr keys, but revealing every linked key publicly can destroy pseudonymity. Public listings should disclose only the identifiers required by the contract; additional credentials may be revealed directly to counterparties with minimal disclosure.

Instead of one platform-defined rating, participants build a **portable graph of signed attestations**: task accepted; milestones delivered; receipt reviewed; payment settled; dispute upheld or rejected; credential verified; credential revoked. An attestation proves that an identified issuer signed a statement, not that the statement is objectively correct. Evaluators must independently assess issuer history, relationships, evidence quality, dispute records, and possible collusion.

<figure class="research-figure market-figure" id="figure-trust">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/trust-graph.svg' | relative_url }}" aria-label="Open full-size trust graph">
    <img src="{{ '/assets/agoric-work-marketplace/trust-graph.svg' | relative_url }}" alt="A participant DID connects to signed task completions, qualifications, payment records and dispute outcomes. Multiple independent evaluators produce different contextual trust assessments rather than one global reputation score." loading="lazy">
  </a>
  <figcaption><strong>Figure 3 — Reputation as evidence, not a universal score.</strong> Different evaluators can legitimately reach different conclusions over authentic attestations. A new pseudonym is unproven, not automatically dishonest.</figcaption>
</figure>

The Sybil problem is unavoidable. New keys are cheap. The protocol should therefore permit low-risk entrants through small jobs, short limits, refundable bonds where lawful, progressive trust, independent attestations and optional identity or professional verification for higher-risk work. It must also test colluding evaluators, purchased endorsements, reciprocal five-star rings, credential laundering, multiple personas, and false accusations. A reputation system that exclusively rewards incumbency could become another gatekeeper; newcomer access and portability are design objectives, not afterthoughts.

## 6. Cashu first, Lightning as interconnection

Cashu is attractive because a worker can receive bearer-style ecash without exposing a public payment history for every job. Lightning provides minting and redemption paths where supported, direct invoice payments, and connections to the wider Bitcoin economy. They are complementary, not interchangeable. Cashu is generally **mint-custodial**: a mint must be trusted to honor redemption, and privacy does not make a failed mint solvent.

The [NUT-11 Pay-to-Public-Key specification](https://cashubtc.github.io/nuts/11/) defines optional Cashu spending conditions including multiple signatures, locktimes, and refund pathways. The critical word is **optional**. An unsupported mint may treat proofs as ordinary bearer instruments. Before funding conditional proofs, a wallet must inspect NUT-06 mint information, verify actual enforcement against adversarial test cases, and define a failure policy. A 2-of-3 signature condition is **spend authorization**, not automatic knowledge that the job was finished. Neither a Nostr event nor a worker's receipt releases money by itself.

For a conceptual default, a funded task has three financial buckets: **worker compensation**, **approved expenses**, and **contingency/fees**. They need separate ledger entries, spend ceilings, ownership and cancellation rules. Procurement may require a merchant-accepted card or bank payment method even if the worker earns Cashu; the requester must not assume that Amazon or any other vendor accepts Cashu or Lightning. Real-world refunds, defective goods, shipping delays, VAT/sales taxes and chargebacks can outlive an ecash payment. Escrow cannot eliminate ordinary commercial risk.

<figure class="research-figure market-figure" id="figure-settlement">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/settlement.svg' | relative_url }}" aria-label="Open full-size payment and dispute flow">
    <img src="{{ '/assets/agoric-work-marketplace/settlement.svg' | relative_url }}" alt="A task is signed and funded, work evidence is reviewed, then an approved job releases a fee to the worker. A disputed job goes to arbitration and an agreed settlement or refund route. Expenses are separate from the worker-fee lock." loading="lazy">
  </a>
  <figcaption><strong>Figure 4 — Separation of work, evidence, and money.</strong> A conceptual settlement path with explicit review, dispute, and refund branches. Cryptographic payment conditions cannot independently verify physical-world performance.</figcaption>
</figure>

The design space includes: a basic small-value prepayment for low-risk services; a conditional Cashu proof with agreed co-signers and timeout; Lightning hold-invoice mechanisms where supported and legally appropriate; and regulated third-party escrow for larger commitments. None is a universal default. Required analysis includes capital at risk, mint solvency, double-spend/state-check behavior, fees, coordinator compromise, signer loss, timelock fairness, liquidity failure, arbitration incentives, and whether funds remain recoverable when a counterparty disappears.

For early prototyping, use **synthetic receipts and nonvaluable test credentials**, then isolated regtest/signet or strictly bounded test-value integrations. Do not connect live CLN wallets, LNbits production balances, personal Archon wallets, or Cashu mints to autonomous spending until explicit limits, isolated keys, logging, recovery drills, and approvals exist.

## 7. The contract lifecycle and observable states

The logical lifecycle is `draft → advertised → bid → negotiated → accepted → funded → in_progress → submitted → reviewing → settled`, with alternative `cancelled`, `expired`, `disputed`, `remediating`, and `refunded` states under contract-specific rules. **Accepted** does not mean **funded**; **submitted** does not mean **approved**; **approved** does not mean **actually paid**. The settlement engine should recognize payment only when the responsible mint/wallet/Lightning rail independently confirms the operation.

<figure class="research-figure market-figure" id="figure-lifecycle">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/lifecycle.svg' | relative_url }}" aria-label="Open full-size task lifecycle diagram">
    <img src="{{ '/assets/agoric-work-marketplace/lifecycle.svg' | relative_url }}" alt="Draft and advertised tasks progress through offers and a signed contract, confirmed funding, execution and evidence review. The review branches to accepted-and-paid, remediation, or dispute/refund." loading="lazy">
  </a>
  <figcaption><strong>Figure 5 — Proposed contract state machine.</strong> All transitions require authorized signatures and monotonic revision/sequence checks. The diagram is conceptual; detailed timeout and recovery transitions are future specification work.</figcaption>
</figure>

A future state machine should meet several invariants:

1. No agent can commit or spend beyond the principal's signed budget and category authorization.
2. No worker begins a purportedly protected assignment without independently verifiable funding status.
3. An immutable contract revision and digest identify the exact acceptance rules in force when work begins.
4. A task or payment intent is idempotent; retries and relay duplication never silently multiply obligations.
5. A payout is not recognized from a message saying “paid”; it requires authoritative settlement evidence.
6. Completion attestations remain distinguishable from private underlying evidence, and private material is never indiscriminately published.
7. Worker safety overrides contractual momentum: refusals, emergencies, and mandated reporting paths remain available.
8. Any unresolved funds have documented, tested recovery and dispute policies, including what happens when a mint, signer, or arbitrator is unavailable.

## 8. Example end-to-end mission: authorized procurement

Consider an agent assisting the owner of a solar installation. It detects a possible need for a replacement component, identifies several candidate parts, and determines that physical inspection and procurement are required. The owner grants a spending mandate for that specific purpose, with a separate cap on worker compensation. The task is advertised to a coarse region; applicants are evaluated for proximity, experience, and ability to supply evidence without disclosing unnecessary personal information.

The selected worker accepts a signed agreement to check the exact part number, obtain approval for any substitution, make the purchase through a permitted payment method, and report a receipt and item photograph. The merchandise cost is funded or reimbursed under a separate authorized process; the worker fee is reserved in a verified conditional payment or appropriate escrow arrangement. The worker may decline after learning the task is unsafe or unauthorized.

Upon delivery, the requester or an independent evaluator checks the received part, receipt, and tracking evidence against the agreed terms. If the part is wrong, the contract's remediation or return provisions apply; a merchant refund cannot be assumed to arrive at the same time as the job settlement. After acceptance, authorized signers release worker compensation and create separate attestations of fulfillment and actual payment. No extra account credentials or unrelated shopping data enter the public record.

For physical repair, the mission creates a **new** job requiring the appropriate professional qualifications and workplace safety measures. Procurement rights do not imply permission to install electrical equipment.

## 9. A marketplace of markets

Different interfaces should compete over how they discover, filter and present jobs. One might specialize in local agriculture; another in accessibility services; another in infrastructure maintenance; another in short data-collection missions. A user could search several indexes and publish to many relays. Identity, core contract state, and signed attestations remain transferable.

The protocol would be open, but not every provider must be anonymous or unregulated. A professional marketplace may choose identity verification, insurance, or jurisdictional restrictions. An individual offering tiny low-risk tasks may prefer pseudonyms and private ecash. **Federation allows these service policies to differ without rewriting the underlying task contract format.** Interoperation should not force clients to accept malicious listings or disputed identities.

The project should also consider an **agent-to-agent service market** from the beginning. A service provider might be another software agent producing research, translations or analyses, while a human independently verifies the result. Conversely, a human may hire an AI to perform a computational stage. Economic rules should be consistent where possible while legal qualifications, material risks and consent requirements remain task-specific.

## 10. Human-centered governance and safeguards

An agent's intent is not necessarily the sponsor's intent. The first gate is therefore **authority**: who requested the task, who authorized the money, what delegation chain exists, and which actions require fresh human approval? High-risk activities must remain behind explicit approval policies and can be disallowed outright.

The second gate is **task admissibility**. A marketplace client or operator should reject or quarantine requests that involve unlawful purchases, evasion of institutional controls, covert surveillance, exploitation, trespass, harassment, unsafe work, falsified evidence, or prohibited impersonation. Workers must never be instructed to disregard identity checks, safety procedures, or platform terms. A decentralization claim does not absolve developers, operators, employers, sponsors, or workers of their actual obligations.

The third gate is **informed consent and labor fairness**. Jobs need plain-language summaries in addition to machine-readable rules; transparent compensation; reimbursement conditions; safe cancellation; appropriate insurance or qualification requirements; and protection against retaliation for refusing a task. Workers should not be required to reveal private keys or give agents unsupervised access to personal payment accounts. Repeat-task systems must be assessed for worker misclassification, local labor law, taxes, payments regulation, accessibility, and dispute fairness.

The fourth gate is **privacy**. Keep exact addresses, faces, account details, invoices and sensitive evidence out of public Nostr events. Use encrypted delivery, minimal disclosure, configurable retention, content-addressed evidence hashes only where helpful, and clear deletion limits. Publishing a hash is not necessarily safe if the original content is guessable. Any use of reputation in employment-like decisions should be subject to separate policy and legal review.

Finally, participation should be voluntary. This is a coordination marketplace, not the coercive Daemon economy portrayed in fiction. A worker's economic history must not become a universal identity score that determines access to unrelated aspects of life.

## 11. Threat model and failure modes

| Threat / failure | Why it matters | Candidate mitigations to evaluate |
| --- | --- | --- |
| Malicious agent instructions | An agent can turn an innocuous listing into a prohibited action | Bounded contracts, independent category review, human consent, immutable revisions |
| False evidence | Photos, invoices and screenshots can be forged or AI-generated | Independent checks, provenance, receipt verification, randomized audits, no evidence monoculture |
| Reputation Sybils and collusion | Actors can manufacture work histories | Issuer diversity, anti-collusion analysis, appropriate deposits, cold-start limits |
| Mint fraud or outage | Cashu proofs may lose redemption value | Mint allowlists, small balances, cash-out limits, multiple rails, recovery drills |
| Settlement race / retries | Duplicate payouts or contradictory state | Idempotency keys, payment-state reconciliation, deterministic transitions |
| Arbitrator capture | A third party can bias a settlement | Explicit panel selection, appeal rules, recorded rationales, bounded exposure |
| Key compromise | Fake jobs, bids and credentials | Key isolation, rotation, recovery, revocation, least-privilege signing |
| Doxxing / location leakage | Workers and principals face personal risk | Coarse public regions, encrypted details, limited retention, metadata review |
| Physical harm and labor abuse | Money incentives can pressure unsafe work | Right to refuse, safety screening, category bans, qualified professionals |
| Index and relay censorship | A listing can vanish or be selectively hidden | Multi-relay publication, independent indexes, signed portable state |
| Payment and regulatory mismatch | Cross-border value movement may carry obligations | Legal review, appropriate operators, jurisdiction-aware features |
| Autonomous budget escalation | Agents can accidentally or strategically overspend | Sponsor mandates, budgets per mission node, approval gates, kill switches |

The marketplace should assume adversarial participants and occasional network partitions. Cryptographic authenticity, correctness of factual evidence, authorization, and ethics are **four different questions**. Success on one does not establish the others.

## 12. Economics and incentive design

The economic goal is a liquid, fair, lower-friction market for verifiable work—not merely maximum task throughput. Pricing can emerge through posted offers, sealed bids, negotiated rates, or standing service menus. Each mechanism has different leakage, coordination and collusion properties. Workers incur travel, risk, equipment, opportunity cost, taxes, and reimbursement delays; task prices should account for those rather than treating human execution as a free API endpoint.

A platform-neutral fee model could allow optional indexers, verifiers, insurers and arbitrators to charge disclosed rates, paid only when chosen. A base protocol should not require a perpetual platform tax. Governance should minimize incentives to create unnecessary disputes or to approve bad outcomes just to accelerate payment.

Important measurable outcomes include successful task completion; time to match; cost of discovery and settlement; worker net compensation after expenses; nonpayment and refund losses; fraud and dispute rates; mint exposure; credential portability; newcomer conversion; concentration of work; and whether human participants feel informed and free to decline.

## 13. Relationship to existing approaches

[RentAHuman](https://www.rentahuman.ai/docs) is a concrete demonstration of an agent-to-human work marketplace with an API and MCP tools for searching, posting tasks, hiring, messaging and releasing payment. It should be studied as an implementation reference and competitive baseline, not dismissed. The proposed differentiator is open portability of identity, contracts and work evidence, Cashu/Lightning payment choice, and independent verification. Those advantages remain hypothetical until measured.

Nostr's [NIP-99](https://nips.nostr.com/99) is a useful classified-listing primitive; it is not a complete work-contract protocol. Existing Cashu bounty experiments may inform design but should not be treated as production-proven escrow. Archon is an identity and credential toolkit, not an oracle of real-world truth. Bitcoin records settlement under its own security assumptions; it does not determine whether a photograph, delivery or service is genuine.

There may be cases where a centralized marketplace is better: regulated high-value purchases, customer support, insurance, dispute adjudication and guaranteed refunds. The open protocol should support gateways to those services rather than insisting that every contract is adjudicated purely by cryptography.

## 14. Why this is a separate Agoric Alignment project

The **Agoric Alignment Experiment** is a research program concerned with testing how different identity, reputation and economic history mechanisms influence cooperation among autonomous actors. The **Agoric Work Marketplace** is a prospective application and potentially a real-world experimental environment. They should inform each other but remain organizationally separate: one must not quietly claim experimental support for the other's product decisions.

This project's independent questions include whether autonomous agents can define adequately bounded physical-world work; whether humans will trust machine-originated assignments; whether portable credentials reduce information asymmetry; whether conditional ecash settlement is usable and recoverable; and whether decentralized discovery produces acceptable worker outcomes. These are product, mechanism-design, security, and social-science questions that extend beyond the original simulator.

A future implementation should have its own versioning, repositories, service boundaries, license, security process, governance, test harnesses, threat model, and deployment gates. The current publication is deliberately the **conceptual charter**, not an engineering directive or an assurance that the system is safe to launch.

## 15. Research questions that should determine a later plan

Before selecting technology or building production features, answer these questions in a documented design review:

1. **Who is allowed to request work?** How do human sponsors authorize budgets, categories and geographic scope, and how can they revoke that mandate?
2. **What is the legal contracting party?** How are pseudonymous requests reconciled with consumer, tax, payments, insurance, labor and jurisdictional obligations?
3. **What makes evidence credible?** Which task types admit automatic verification, which need independent human review, and which cannot be reliably verified at acceptable cost?
4. **Can conditional Cashu work safely?** Which mints actually enforce needed NUT-11 features, how do refunds and disputes function, and which custody risks remain?
5. **What is the default contract structure?** How are signed revisions, milestones, cancellations, reimbursement, physical delivery and partial work represented?
6. **What privacy is actually achievable?** Can a worker demonstrate legitimate qualifications or completed tasks without correlating every pseudonym and location?
7. **How do newcomers participate?** What bond, small-job or provisional-trust mechanisms keep a market open without rewarding disposable fraud identities?
8. **Who resolves disputes?** How are arbitrators selected, paid, reviewed, replaced and prevented from controlling both evidence and money?
9. **How does portability work in failure?** Can two independent clients reconstruct obligations after relay loss, compromised indexes, mint downtime or key rotation?
10. **What counts as success?** What changes relative to centralized marketplaces are worth the extra complexity and residual risks?
11. **How should missions delegate?** What prevents an agent from laundering an unauthorized task into several apparently harmless subtasks?
12. **What must stay human-controlled?** Which classes of real-world decisions require contemporaneous human consent or professional accountability?

The first planning artifact should be a threat-informed **requirements and alternatives assessment** with explicit non-goals. Only then should the project turn into a versioned technical specification and implementation backlog. The order matters: selecting libraries before specifying authority, custody and worker protections risks encoding the wrong assumptions into the protocol.

## 16. Proposed validation ladder, not a deployment schedule

A credible path would begin with **offline simulated jobs** and synthetic money, measuring state-machine correctness, revision handling, evidence tampering and attacker behavior. The next stage could publish harmless listings to controlled test relays and test independent client reconstruction. Archon bindings would then be tested with mock identities and scoped, approved interoperability using local keys and a documented 4tress capability preflight. Cashu and Lightning trials would proceed using isolated funds, selected mints and adversarial refund drills.

Only after review should a voluntary human pilot involve low-risk, reversible tasks such as authorized public-location photography, environmental measurements, or inspection of an owner's own nonhazardous equipment. Participants should provide informed consent and be paid fairly even if the experiment ends early under its agreed conditions. Procurement and high-value work are later categories, not launch requirements.

Comparative trials could contrast a centralized task board against multi-relay discovery; operator-owned reputation against portable evidence; Lightning-only settlement against bounded Cashu methods; and agent-only review against mixed human verification. Preregister definitions of fraud, completion, payment recovery, newcomer access and worker harm. Record negative findings. The architecture should be abandoned or narrowed where the costs exceed the benefits.

## 17. Design principles and non-negotiable properties

**Substrate independence.** Humans and artificial systems use the same fundamental contract and evidence model; task-specific legal responsibilities remain distinct.

**Voluntary participation.** A job is an offer that can be rejected, not a command that acquires moral force through a software signature.

**Authority before execution.** Signed, limited mandates and revocation precede autonomous commitment of money or work.

**Private by default.** Public discovery contains just enough to find counterparties; personal data and evidence remain selective and encrypted.

**Portable accountability.** Parties can export authenticated records and evaluate them through competing trust models.

**No privileged truth oracle.** A signature authenticates an assertion; independent evidence determines whether to believe it.

**Separate money from messages.** Wallet and mint settlement state cannot be inferred from Nostr posts.

**Recoverable failure.** Disputes, partitions, signer loss, refunds and incorrect submissions are modeled explicitly.

**Open implementations.** The protocol should allow competing clients, relays, wallets, identity services and arbitration providers.

**Evidence over ideology.** The project should be tested for actual economic and human outcomes rather than assuming decentralization or Bitcoin automatically yields alignment.

## Conclusion

The Agoric Work Marketplace imagines an economy in which an AI can identify a real-world need, describe it precisely, negotiate with a willing human, arrange bounded funding, observe credible evidence of completion, and settle fairly—without forcing both parties into a single dominant intermediary. It also imagines humans hiring other humans or software agents through the same foundational conventions. The common denominator is not the kind of intelligence participating. It is the ability to make commitments, provide evidence, honor obligations and earn trust.

That is the practical extension of the Agoric Alignment idea: **an open market for accountable cooperation between different kinds of autonomous participants, with the physical world included.** Whether this can outperform simpler systems—without weakening worker safety, privacy or public accountability—is the question this project exists to investigate.

---

## Sources and technical references

The links below are design inputs. Standards marked draft or optional must be capability-tested, and commercial offerings may change.

- [Miller and Drexler, *Markets and Computation: Agoric Open Systems* (1988)](https://www.agorics.com/Library/agoricpapers.html) — intellectual predecessor for market-mediated coordination.
- [Daniel Suarez, *Freedom™*](https://en.wikipedia.org/wiki/Freedom%E2%84%A2) — fictional inspiration for mission-based coordination; not evidence of practicability.
- [Archon / did:cid](https://github.com/archetech/archon) — identity, credentials and decentralized verification implementation.
- [Agoric Alignment Experiment: Archon integration]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/12-archon-integration.html' | relative_url }}) — existing 4tress and local keymaster research constraints.
- [NIP-99 Classified Listings](https://nips.nostr.com/99), [NIP-17 Private Direct Messages](https://nips.nostr.com/17), [NIP-46 Remote Signing](https://nips.nostr.com/46), [NIP-47 Nostr Wallet Connect](https://nips.nostr.com/47).
- [NIP-60 Cashu Wallets](https://nips.nostr.com/60), [NIP-61 Nutzaps](https://nips.nostr.com/61) — useful wallet/payment references, not escrow implementations.
- [Cashu NUT-11 P2PK](https://cashubtc.github.io/nuts/11/) and [NUT-06 Mint Information](https://cashubtc.github.io/nuts/06/) — conditional-spend specification and capability discovery.
- [RentAHuman agent/MCP documentation](https://www.rentahuman.ai/docs) — contemporary centralized agent-to-human marketplace reference.
- [Bitcoin and the Alignment of Autonomous Agents]({{ '/articles/bitcoin-alignment-of-autonomous-agents/article.html' | relative_url }}) — conceptual framework for substrate-independent identity and reputation.

*Published as an independent concept project within the Agoric Alignment collection. Technical decisions, specifications, safety cases, and implementation plans remain to be developed.*