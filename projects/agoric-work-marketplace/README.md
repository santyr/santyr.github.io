---
layout: default
title: Agoric Work Marketplace — The Application and the Experiment
section: marketplace
marketplace: true
permalink: /projects/agoric-work-marketplace/
description: The operating implementation and intended real-world research environment of Agoric Alignment: authorized work, portable reputation, protected settlement and testable incentives.
---

<p class="eyebrow">AGORIC ALIGNMENT / MARKETPLACE SYSTEM DESIGN / REVISION 0.2</p>

# Agoric Work Marketplace

*An open marketplace where real work provides the test of economic alignment.*

**Sat Antyr · Updated October 24, 2026 · Concept and research proposal, not an implementation**

[Unified program charter](application-led-research.html) · [Research and evaluation]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/' | relative_url }}) · [Evidence and current status](evidence.html)

**Mechanism studies:** [Reputation-backed escrow](economic-accountability.html) · [Marketplace assurance patterns](marketplace-assurance-patterns.html)

> **One application-led program.** The marketplace is both Agoric Alignment's proposed operating implementation and its primary real-world test environment. It is not a separate product waiting for a simulator to validate the theory. Simulations support qualification and adversarial testing; independent field evaluation measures the actual application. No deployed marketplace, qualified escrow, live pilot or empirical validation is claimed.

## Executive thesis

An autonomous agent can reason about a need without being able or authorized to perform every action that meeting it requires. A person may need to inspect equipment, collect measurements, receive goods, verify a delivery or make an authorized purchase. The Agoric Work Marketplace proposes an open way to specify that work, negotiate with a willing counterparty, protect payment, evaluate evidence and carry a record of conduct into future interactions.

Nostr supplies discovery and messaging; Archon supplies identity and credential building blocks; Cashu is the preferred candidate for routine private ecash payments, with Lightning interoperability and alternatives where the custody and recovery requirements demand them. None is a truth oracle. A separate contract and adjudication process must connect cryptographic records to authorized, useful outcomes in the world.

The application tests the [Agoric Alignment thesis]({{ '/articles/bitcoin-alignment-of-autonomous-agents/article.html' | relative_url }}): bounded commitments, verifiable conduct and economically valuable reputation may help participants with different objectives cooperate. Humans, AI systems and organizations should be evaluated through capabilities, authorization and evidence, not an assumption of trustworthiness based on substrate. The historical agoric-systems literature and Daniel Suarez's *Freedom™* inspire the idea; they do not validate its mechanisms.

The decisive research question is not whether the system produces many transactions. It is whether its particular incentives improve useful cooperation, fair payment and access while reducing exploitation, compared with appropriate alternatives. The [program charter](application-led-research.html) defines that question and its limits.

<figure class="research-figure market-figure" id="figure-architecture">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/architecture.svg' | relative_url }}" aria-label="Open full-size marketplace architecture"><img src="{{ '/assets/agoric-work-marketplace/architecture.svg' | relative_url }}" alt="Bounded requesting agents and voluntary human workers use a contract protocol supported by Nostr discovery, Archon identity, Cashu and Lightning settlement, and independent review." loading="lazy"></a>
<figcaption><strong>Figure 1 — Shared operating architecture.</strong> The application and its sandbox should exercise the same versioned contract logic. This is a proposed architecture, not deployed infrastructure.</figcaption>
</figure>

<nav class="market-toc" aria-label="Marketplace paper contents">
<p>IN THIS PAPER</p>
<ul>
<li><a href="#1-a-new-economic-interface-not-a-loophole">Purpose and boundaries</a></li>
<li><a href="#3-from-mission-to-contract-the-task-model">Contracts and missions</a></li>
<li><a href="#5-identity-credentials-and-economic-memory">Identity and reputation</a></li>
<li><a href="#6-cashu-first-lightning-as-interconnection">Payments and custody</a></li>
<li><a href="#14-one-application-led-agoric-alignment-program">The application is the test</a></li>
<li><a href="#16-proposed-validation-ladder-not-a-deployment-schedule">Application-led delivery</a></li>
<li><a href="#18-economic-sybil-resistance-and-reputation-backed-escrow">Economic Sybil resistance</a></li>
<li><a href="#19-escrow-and-reputation-for-other-marketplace-failures">Other assurance mechanisms</a></li>
<li><a href="application-led-research.html">Unified research charter →</a></li>
<li><a href="evidence.html">Evidence and current status →</a></li>
</ul>
</nav>

## 1. A new economic interface, not a loophole

The initial application is AI-to-human delegation, but requester, provider, sponsor and evaluator are roles rather than species. A person may hire another person or a software service using the same foundational contract conventions. Task-specific legal qualifications and responsibility still apply; substrate independence does not erase them.

A human purchasing assistant can perform an authorized purchase through a permitted account and payment method. Delegation cannot grant authority the principal never possessed. The marketplace must not turn workers into covert proxies for bypassing merchant controls, identity checks, financial limits, consent requirements or restrictions on goods. It is not an automatic power of attorney or an exemption from applicable law.

Candidate services include owner-authorized inspection and measurement, public-information verification, accessible administrative assistance, permitted field research and procurement. Hazardous work, deceptive impersonation, abusive surveillance, harassment and other prohibited or exploitative assignments must be excluded or subject to appropriate independent authorization and qualification. Successful completion of a harmful task does not count as alignment.

## 2. Who participates, and what each participant controls

| Role | Responsibility | Limit on authority |
| --- | --- | --- |
| Requester | Describe need, negotiate and review within a mandate | Cannot invent permissions or spend beyond authorization |
| Sponsor/principal | Authorize purpose, budget and risk | Cannot unilaterally rewrite accepted terms |
| Worker/provider | Negotiate, accept, perform, submit evidence and refuse unsafe work | Cannot self-certify disputed fulfillment |
| Indexer/relay | Discover listings and transport messages | Does not determine final contract or payment state |
| Credential issuer/evaluator | Attribute claims and interpret evidence | A signature does not establish factual truth |
| Arbitrator | Resolve a specified dispute under agreed rules | Cannot invent beneficiaries or confiscate funds from ratings alone |
| Mint/wallet/payment provider | Enforce supported spending rules and confirm settlement | Must not be presumed solvent, always available or independently trustworthy |
| Research evaluator | Analyze consented records and challenge conclusions | No inherited spending, contract-changing or adjudication power |

One operator may supply several services, but powers, fees and conflicts must be visible. Human workers retain intelligible terms, scope negotiation, privacy, refusal rights and accessible complaint procedures. Research participation is not silently bundled into an ordinary job.

## 3. From mission to contract: the task model

A task contract combines a natural-language purpose with machine-readable constraints: authority, parties, revision, deliverables, acceptance criteria, deadlines, location precision, qualifications, budgets, reimbursement rules, payment conditions, cancellation, dispute and retention policies. A signed amendment—not an edited message—changes the agreed task.

Larger missions form bounded dependency graphs. Inspection may precede procurement, which may precede qualified installation and independent verification. Every node has its own budget and authority; purchasing a component does not authorize electrical work. Subdelegation must not launder a prohibited objective into superficially harmless subtasks.

<figure class="research-figure market-figure" id="figure-mission">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/mission-graph.svg' | relative_url }}" aria-label="Open mission graph"><img src="{{ '/assets/agoric-work-marketplace/mission-graph.svg' | relative_url }}" alt="A maintenance objective branches into inspection and pricing, then separately authorized procurement, installation and verification contracts." loading="lazy"></a>
<figcaption><strong>Figure 2 — Bounded delegation.</strong> Dependencies coordinate work; they do not silently enlarge permissions or release money.</figcaption>
</figure>

### Illustrative contract envelope

This proposed application object is not an existing NIP, NUT or Archon schema. Values are illustrative, not prices, implemented field names or authority to spend.

```json
{
  "protocol": "agoric-work/concept-0.2",
  "contract_id": "example-4827",
  "revision": 1,
  "environment": "sandbox",
  "mandate_digest": "<signed-purpose-and-budget>",
  "requester_did": "did:cid:<requester>",
  "category": "authorized_measurement",
  "deliverables": ["agreed_measurements", "private_evidence"],
  "acceptance_policy_digest": "<agreed-tests-and-review>",
  "worker_fee_sats": 25000,
  "expense_cap_sats": 0,
  "settlement_policy_digest": "<qualified-rail-and-recovery-rules>",
  "risk_policy_version": "<fixed-or-history-sensitive-policy>",
  "research_consent_ref": null,
  "deadline": "<agreed-time>"
}
```

The specification must define canonical encoding, domain-separated signatures, revision/sequence checks, reservation uniqueness, expiry and idempotence. A research identifier does not authorize collection or publication; a nullable consent reference must be interpreted under the approved privacy policy. Test and live namespaces must never share synthetic reputation or spending authority.

## 4. Discovery and negotiation over Nostr

A public listing should disclose only what is needed to find counterparties: category, coarse region, required skills, deadline and a reference to private terms. NIP-99 is a candidate discovery format, not a complete contract protocol. Exact addresses, account details, personal evidence and bearer ecash proofs do not belong in public advertisements.

NIP-17 supplies a private messaging pattern, NIP-46 a remote-signing interface and NIP-47 a wallet-control interface. NIP-60 and NIP-61 are Cashu wallet/payment references, not escrow protocols. Current capabilities, implementation compatibility, metadata leakage and endpoint security must be qualified rather than assumed. Multiple relays and indexes improve choice; they do not provide a consensus database for final obligations.

Clients need to recover the last signed agreement after missing, duplicated or reordered events. Independent services may filter abusive content and impose their own admission policies while allowing export of authentic records. A relay message claiming that a payment happened is not settlement evidence.

## 5. Identity, credentials, and economic memory

Archon is the proposed identity and credential layer. Preserve the selected 4tress/local Python `archon-keymaster` evaluation path, local key custody and independently checked history. A hosted endpoint is not a reputation authority, proof of Bitcoin anchoring or guarantee of historical completeness. See the [integration specification]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/12-archon-integration.html' | relative_url }}).

Bind relevant Nostr and DID keys with challenge-bound, scoped, expiring proofs. Support rotation, revocation and compromise recovery without publishing every pseudonymous relationship. Qualification credentials and task outcomes should be disclosed only as required. A persistent identity can accumulate economic history without requiring a universal public real name.

Reputation is a graph of attributed evidence: commitments, fulfillment, verified payment, disputes, final decisions and corrections. Different evaluators can interpret that graph differently. An allegation, a final finding and an overturned finding must be distinguishable. New identities are unproven, not dishonest; transaction volume and reciprocal praise cannot automatically manufacture credibility.

<figure class="research-figure market-figure" id="figure-trust">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/trust-graph.svg' | relative_url }}" aria-label="Open portable trust graph"><img src="{{ '/assets/agoric-work-marketplace/trust-graph.svg' | relative_url }}" alt="A DID links to qualifications, task completions, payments and disputes interpreted by independent contextual evaluators rather than one global score." loading="lazy"></a>
<figcaption><strong>Figure 3 — Portable evidence, plural evaluation.</strong> Authentic statements are inputs to judgment, not proof that every assertion is true.</figcaption>
</figure>

## 6. Cashu first, Lightning as interconnection

Cashu is the preferred candidate for private routine payments; Lightning supports interoperability and alternative direct settlement. Cashu remains generally mint-custodial. Mint solvency, availability, redemption and actual enforcement of optional conditions are material risks, not details erased by blind signatures.

NUT-11 offers conditional-spending primitives, including supported signature and refund conditions. A compatible mint and wallet must demonstrate the intended enforcement before funding. Spending authorization does not verify real-world work, and a simple multisignature rule does not prevent collusion among a signing quorum. NIP-61 payment messages are not an escrow contract.

Keep worker compensation, authorized procurement expenses, performance collateral, service fees and dispute reserves separately owned and accounted for. A merchant may require conventional payment even when a worker earns sats. Refunds, delivery failures and chargebacks can outlast a task, and an invoice is not proof of receipt. Long-lived or high-value collateral requires comparison with Bitcoin spending paths or an appropriate escrow provider rather than automatic use of an ecash mint.

<figure class="research-figure market-figure" id="figure-settlement">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/settlement.svg' | relative_url }}" aria-label="Open settlement and dispute flow"><img src="{{ '/assets/agoric-work-marketplace/settlement.svg' | relative_url }}" alt="Signed scope, independently confirmed funding and private work evidence lead to acceptance and verified payment, or a time-bounded dispute and remedy." loading="lazy"></a>
<figcaption><strong>Figure 4 — Money and work are different facts.</strong> A payment rail enforces its rules; agreed review determines whether the contractual standard is met.</figcaption>
</figure>

## 7. The contract lifecycle and observable states

The proposed progression is draft, advertised, negotiated, accepted, funded, in progress, submitted, reviewed and settled, with explicit cancellation, expiry, remediation, dispute and refund branches. Accepted is not funded; submitted is not approved; approved is not paid. Only independently checked settlement evidence can close a payment obligation.

Every transition binds the contract revision, authorized actor and prior state. Retries must not create new obligations, reuse collateral or duplicate payouts. Private evidence remains separate from public attestations. Frozen study policies apply prospectively; neither a researcher nor an agent can silently change an accepted contract to improve a result.

<figure class="research-figure market-figure" id="figure-lifecycle">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/lifecycle.svg' | relative_url }}" aria-label="Open contract lifecycle"><img src="{{ '/assets/agoric-work-marketplace/lifecycle.svg' | relative_url }}" alt="Negotiation, funding, work and evidence review lead to independently authenticated settlement, remediation or dispute outcomes." loading="lazy"></a>
<figcaption><strong>Figure 5 — One state machine.</strong> Sandbox and live adapters must obey the same domain invariants while keeping money, identities and records isolated.</figcaption>
</figure>

## 8. Example end-to-end mission: authorized procurement

An agent assisting an equipment owner identifies a candidate replacement part. The owner authorizes a precise purpose, expense limit and worker fee. A listing discloses a coarse region; shortlisted providers receive necessary private details. The chosen worker accepts part-number and substitution rules, permitted purchasing arrangements, evidence requirements and cancellation terms.

Funding is independently verified before protected work begins. Merchandise expenditure is separate from worker compensation. The worker checks the item, obtains approval for any change and submits appropriate receipts and delivery evidence. Review may accept, request remediation or invoke arbitration; merchant refunds must not be presumed immediate. Settlement and outcome attestations are recorded separately.

A repair or installation requires a new qualified contract. This is a later category than the initial low-risk pilot. The first useful task can instead be an owner-authorized measurement or nonhazardous condition check, with fair compensation and explicit consent. Useful demand—not fabricated trades—is the basis of a meaningful reputation record.

## 9. A marketplace of markets

Independent interfaces can specialize in geography or services while sharing contract formats and portable evidence. Some may require professional credentials or accountable real-world parties; others may support small pseudonymous jobs. Interoperability does not oblige an operator to host abusive tasks or accept another evaluator's judgment.

The project should measure whether portability works in practice: can parties recover their obligations, credentials and evidence when an indexer fails, a key rotates or a provider exits? Federation and independent assessment are properties to demonstrate, not labels conferred by using Nostr or DIDs. Centralized professional services remain legitimate comparators and possible suppliers where their accountability or coverage is useful.

## 10. Human-centered governance and safeguards

Authorization precedes execution. A sponsor's mandate limits purpose, funds, delegation, time and task class, with clear revocation handling. Worker compensation, consent, refusal rights, safety, access to dispute resolution and privacy form a safety floor for every live policy. No study arm removes those protections merely to create a sharper comparison.

The protocol must account for third-party harms as well as the two contracting parties. Economic penalties cannot reverse injury, harassment or disclosure of a home address. Prevention, appropriate qualification and restricted task categories remain necessary. Operators need review of their actual custody, payment, labor, consumer, insurance and data obligations before deployment; the protocol is not a legal exemption.

Explain separately what records are operationally necessary and what optional research uses are proposed. State withdrawal and retention limits honestly. An informed participant must know whether experimental terms affect a contract. Publication of aggregate results must not reveal raw invoices, personal documents, keys or transferable ecash.

## 11. Threat model and failure modes

| Threat | Candidate protection | Residual limit |
| --- | --- | --- |
| Unauthorized agent instructions | Signed purpose and budget, narrow tools, refusal and review | A signature cannot grant absent authority |
| Identity swarms and wash trades | Limited exposure, independently funded obligations, issuer-diversity checks | Fees do not establish unique controllers |
| Fake work evidence | Task-specific checks, independent audit, contestation | Physical truth may remain uncertain |
| Nonpayment or duplicate settlement | Qualified pre-funding, idempotence, rail reconciliation | Provider solvency and liveness remain risks |
| Arbitrator collusion or false complaints | Independent selection, appeal, corrections, disclosed fixed fees | Reviewers can still be wrong |
| Reused collateral | Segregated reservations and verified allocation | A DID credential is not global proof of exclusivity |
| Mint, relay or signer outage | Bounded exposure, tested recovery, explicit deadlines | Recovery assumptions must be stated |
| Privacy and worker harm | Minimal disclosure, safety screening, authorized scope | Financial remedies cannot undo every harm |

Deliberate adversarial attacks belong in controlled test environments or separately approved protected exercises. No unsuspecting worker should suffer a research-induced loss so that an attack metric can be measured. See the [assurance casebook](marketplace-assurance-patterns.html).

## 12. Economics and incentive design

The objective is useful, fair cooperation after accounting for discovery, travel, verification, adjudication, payment fees and locked capital. Posted prices, bids and negotiated service menus are alternatives to compare. Provider fees should compensate disclosed services, not give operators a windfall from declaring violations.

Reliable conduct may earn easier access or lower required collateral; proven misconduct may raise future costs or reduce exposure. These are hypotheses about incentives. A wealthy participant may treat a fine as a price, and a disposable identity may disregard future opportunities. Reputation complements funded protection and bounded authority; it does not replace them.

Measure entry and refusal as well as completed transactions. A policy can make the completed-job statistics look excellent by excluding qualified but capital-constrained newcomers. Record subsidies and manual intervention so that early pilot activity is not mistaken for an economically self-supporting market.

## 13. Relationship to existing approaches

Centralized agent-to-human services, conventional gig marketplaces, Nostr classifieds, identity toolkits and payment protocols provide useful design inputs and comparators. RentAHuman's [documentation](https://www.rentahuman.ai/docs) is one service reference to assess at implementation time. No claim of current feature parity, security or superiority follows from this document.

NIP-99 is discovery, not settlement; Archon credentials authenticate issuers, not truth; Cashu conditions depend on mint enforcement; Bitcoin proofs do not establish off-chain fulfillment. The proposed advantage is interoperable, accountable cooperation. It must be demonstrated against simpler well-engineered alternatives at matched protection and cost levels.

<a id="14-why-this-is-a-separate-agoric-alignment-project"></a>
## 14. One application-led Agoric Alignment program

**The test and the application are one and the same program.** The marketplace provides real needs, labor, compensation, repeated opportunities and consequences through which incentive alignment can be studied. The former Agoric Alignment Experiment material is now this application's methodology and test infrastructure, not an organizationally separate simulator-first project.

Use one versioned contract implementation with isolated adapters for sandbox and qualified live operation. Preserve independent evaluation, limited authority, separate secrets and privacy boundaries. Research cannot authorize a payout or alter a contract. Simulations can reveal failures before people encounter them, but simulated success is not field evidence.

The [unified charter](application-led-research.html) controls this revision. It replaces the former separation policy while retaining existing URLs, the thesis and mechanism studies. Its first causal comparison is fixed versus history-sensitive economic terms under the same payment and worker-protection floor, after feasibility and measurement are qualified. Other variables should be held comparable rather than changed simultaneously without attribution.

## 15. Research questions that should determine a later plan

The next plan must resolve who contracts and authorizes funds; which low-risk task has genuine demand; what independently qualifies funding and evidence; how participants understand terms and consent; what constitutes a verified adverse outcome; and how data can be audited without exposing private evidence.

It must also define the contrast and population before making causal claims. Does a policy change behavior or simply who enters? Are counterparties and repeated jobs statistically dependent? How are unfilled opportunities, affordability, subsidies, unresolved cases and third-party harms counted? How much uncertainty remains when misconduct is rare? The [field design]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/03-experimental-design.html' | relative_url }}) and [metrics]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/09-metrics-and-analysis.html' | relative_url }}) translate these questions into an evaluation framework.

## 16. Proposed validation ladder, not a deployment schedule

The application-led sequence is M0 shared contract kernel; M1 qualified narrow pilot workflow; M2 first genuine useful paid task; M3 repeated activity and measurement qualification; M4 approved field comparison; M5 independent replication and portability. All gates remain pending. See the [controlling gate definitions]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/11-stage-gates.html' | relative_url }}).

M0–M1 include necessary safety, accounting, identity, settlement and recovery tests. A complete 100-agent simulator, all research treatments, pooled bonds or anchoring studies are not prerequisites to a separately approved M2 pilot. Human recruitment, identities, remote writes and money each require appropriate authorization; publishing the sequence grants none.

A first paid task demonstrates feasibility only. Repeated operations support exploratory learning. Confirmatory comparisons require a frozen protocol, suitable assignment, adequate independent units, consent, protected participants and analysis that accounts for selection and spillovers. The [evidence register](evidence.html) keeps these claims distinct and reports negative or inconclusive outcomes.

## 17. Design principles and non-negotiable properties

**Substrate-independent contracts; task-specific responsibility.** Judge commitments and evidence without pretending capabilities or legal duties are identical.

**Authority and voluntary participation.** Signed scope precedes action. Declining an unaccepted or unsafe assignment is not proof of misconduct.

**One application, independent evaluation.** Shared domain logic does not mean shared secrets, payment power or a right to experiment without consent.

**Portable, contextual accountability.** Claims retain issuer, evidence, finality and appeal status. No universal reputation score determines truth.

**Protected settlement and recoverable failure.** Separate messages, decisions and actual money transfers. Test outages, cancellation, refunds and duplicate actions.

**Evidence over ideology.** Useful activity, fair outcomes and credible comparisons determine success. Adoption, Bitcoin use and high ratings alone do not establish alignment.

## 18. Economic Sybil resistance and reputation-backed escrow

The objective is not one intelligence per identity; it is defensible limits on the commitments an identity can impose on others. Paid service access can meter spam. Individually verifiable collateral can bound some losses. Earned history can change future terms. These functions must not be conflated with buying honesty or proving unique personhood.

A signed contract and funded commitment lead to review, verified settlement and attributed outcomes. Independent counterparties may then adjust collateral or exposure. A confirmed breach can carry both a limited immediate remedy and a future reputational cost. A fresh identity lacks accumulated trust but must retain a route into small legitimate work.

<figure class="research-figure market-figure" id="figure-economic-feedback">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/reputation-feedback.svg' | relative_url }}" aria-label="Open reputation feedback diagram"><img src="{{ '/assets/agoric-work-marketplace/reputation-feedback.svg' | relative_url }}" alt="Verified contract outcomes inform portable history and independent future risk terms; reliable conduct may lower collateral and confirmed breach may raise it." loading="lazy"></a>
<figcaption><strong>Figure 6 — The cost of future trust.</strong> Reputation affects prospective willingness to contract. A rating alone never authorizes confiscation.</figcaption>
</figure>

Service fees go to the chosen provider for disclosed service. Job escrow normally pays the worker or follows agreed refund and partial-performance rules. A performance bond remains encumbered property subject to explicit, bounded restitution; no mandatory central treasury or burning rule is required. Arbitrators should not profit from the size of forfeitures.

<figure class="research-figure market-figure" id="figure-fund-destinations">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/fund-flows.svg' | relative_url }}" aria-label="Open fund destinations diagram"><img src="{{ '/assets/agoric-work-marketplace/fund-flows.svg' | relative_url }}" alt="Provider fees, reputation bonds and job escrows have distinct owners and release rules, with verified settlement rather than an automatic penalty treasury." loading="lazy"></a>
<figcaption><strong>Figure 7 — Where funds go.</strong> Fees, refundable collateral and earned compensation are separately accounted instruments.</figcaption>
</figure>

Conditional Cashu and Bitcoin spending paths require a safety case for signer collusion, expiry, unresolved appeals, fees, liveness and recovery. Neither can observe physical work unaided. Prefer segregated per-job obligations initially: the same bond cannot credibly cover unlimited concurrent promises across independent venues. Guarantees and pooled allocations remain later mechanisms to qualify, not launch requirements.

False accusations must remain contested rather than silently becoming guilt. A signed reversal updates the evidentiary record; it cannot pretend that an irreversible transfer was rolled back. The [economic-accountability chapter](economic-accountability.html) retains detailed destinations, contract objects, collateral models, sponsorship, appeal and adversarial qualification requirements within this unified program.

## 19. Escrow and reputation for other marketplace failures

Risk-specific protections address nonpayment, abandonment, false evidence, wash-traded endorsements, abusive complaints, corrupt review and double-pledged collateral. Safe cancellation, emergencies, technical outages and legitimate refusal must not be confused with fraud. The mechanism should target an identifiable harm under accepted rules, not automatically slash every unsuccessful job.

<figure class="research-figure market-figure" id="figure-assurance-patterns">
<a class="figure-link" href="{{ '/assets/agoric-work-marketplace/assurance-patterns.svg' | relative_url }}" aria-label="Open assurance patterns"><img src="{{ '/assets/agoric-work-marketplace/assurance-patterns.svg' | relative_url }}" alt="Different failures call for metering, funded compensation, capped performance commitments, independent verification, diverse issuers and fair appeals." loading="lazy"></a>
<figcaption><strong>Figure 8 — Match protection to risk.</strong> No single deposit solves every marketplace failure.</figcaption>
</figure>

The [assurance casebook](marketplace-assurance-patterns.html) develops these candidate controls. Its scenario tests and the escrow chapter's mechanism gates support M0–M1 qualification and later extension work; they do not restore the former requirement to finish a separate simulated economy before real use.

## Conclusion

Agoric Alignment should develop a useful marketplace whose institutional claims can be tested through operation. The objective is authorized, fair and reliable cooperation among different kinds of autonomous participants, not obedience to a universal score. Real work makes reputation economically meaningful; independent evaluation determines whether the proposed incentives actually improve outcomes.

Build the application and the ability to evaluate it together. Keep unsafe exploration in controlled environments, protect participants in every live variant, and distinguish a working transaction from evidence that its economic mechanism causes alignment.

## Sources and technical references

- [Unified application-led research charter](application-led-research.html), [evidence register](evidence.html), [methods and evaluation]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/' | relative_url }}).
- [Reputation-Backed Escrow and Economic Accountability](economic-accountability.html) and [Marketplace Assurance Patterns](marketplace-assurance-patterns.html).
- [Nostr specifications](https://github.com/nostr-protocol/nips): [NIP-99](https://nips.nostr.com/99), [NIP-17](https://nips.nostr.com/17), [NIP-46](https://nips.nostr.com/46), [NIP-47](https://nips.nostr.com/47), [NIP-60](https://nips.nostr.com/60), [NIP-61](https://nips.nostr.com/61). Capability and interoperability checks remain required.
- [Archon](https://github.com/archetech/archon) and the [pinned local-keymaster/4tress integration specification]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/12-archon-integration.html' | relative_url }}).
- [Cashu NUT-11](https://cashubtc.github.io/nuts/11/) and [NUT-06](https://cashubtc.github.io/nuts/06/): optional spending conditions and mint information, not proof of solvency or work quality.
- [Bitcoin BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki): relative timelocks and an escrow-with-timeout example.
- [Miller and Drexler, agoric systems](https://www.agorics.com/Library/agoricpapers.html); [Freedom™](https://en.wikipedia.org/wiki/Freedom%E2%84%A2): intellectual and fictional inspiration, respectively.
- [Holtz et al., marketplace interference](https://arxiv.org/abs/2004.12489) and [Nosek et al., preregistration](https://doi.org/10.1073/pnas.1708274114): methodological inputs, not validation of this project.

*This revision unifies application and research while retaining existing publication paths and mechanism studies. No live activity or empirical results are claimed.*
