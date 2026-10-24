---
layout: default
title: Marketplace Assurance Patterns — Escrow, Reputation and Adversarial Incentives
section: marketplace
marketplace: true
permalink: /projects/agoric-work-marketplace/marketplace-assurance-patterns.html
description: Applying evidence-linked reputation, bounded escrow, economic risk limits and independent dispute processes to recurring decentralized labor marketplace failures.
---

<p class="eyebrow">AGORIC WORK MARKETPLACE / DESIGN RESEARCH 02</p>

# Marketplace Assurance Patterns

*Applying conditional payment, economic commitments, and portable reputation to practical marketplace failures.*

**Sat Antyr · October 24, 2026 · Adversarial design analysis, not an implementation**

[← Marketplace concept]({{ '/projects/agoric-work-marketplace/' | relative_url }}) · [Reputation-backed escrow design]({{ '/projects/agoric-work-marketplace/economic-accountability.html' | relative_url }})

> **Scope:** Proposed controls and failure scenarios intended to inform later planning. A signed assertion does not establish physical-world truth; a Cashu mint is not a trustless escrow contract; bond forfeiture is subject to lawful, explicit terms and fair review. No automated punitive or financial action is deployed.

## Beyond Sybil attacks

Economic accountability is useful well beyond fake identities. Every open marketplace faces asymmetric information, nonperformance, fabricated evidence, payment default, hostile bidding, abusive cancellations, fraudulent reviews, collusive verifiers, and attempts to monopolize a transaction channel. These failures become harder when a requester is an autonomous AI, a contractor is a pseudonymous person, and an identity can be replaced at negligible cost.

The marketplace should not solve all these problems by requiring universal identity checks or staking ever larger sums. A better design assigns **a specific risk to a specific commitment**. Escrow protects compensation. A performance bond addresses clearly defined losses. A verification bond gives evaluators something at stake. Evidence-aware reputation influences later exposure limits. An appeal process limits the impact of erroneous allegations. Fees meter scarce discovery and review services without turning them into truth.

<figure class="research-figure market-figure" id="figure-assurance">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/assurance-patterns.svg' | relative_url }}" aria-label="Open full-size diagram mapping failure types to protection layers">
    <img src="{{ '/assets/agoric-work-marketplace/assurance-patterns.svg' | relative_url }}" alt="Five marketplace failure classes map to different solutions: identity spam to metering, nonpayment to job escrow, nonperformance to verified performance bonds, false evidence to independent verification and appeals, and collusion to diverse assessors and exposure limits." loading="lazy">
  </a>
  <figcaption><strong>Figure 8 — Match the remedy to the failure.</strong> No single universal deposit can address every class of abuse. Service fees, escrow, evidence and independent evaluation serve different purposes.</figcaption>
</figure>

## 1. Failure patterns and proposed remedies

| Failure mode | Principal harmed | Economic mechanism | Reputation effect when established | Critical limitation |
| --- | --- | --- | --- | --- |
| Listing spam or mass DID creation | Indexers, prospective workers | Low provider-set posting fee, quota or optional computational work | None unless actual misconduct is verified | Fees do not prove uniqueness |
| Bid flooding and strategic no-shows | Requesters, genuine bidders | Rate limits, modest reservation fee or **refundable** bid commitment for scarce slots | Repeated proven abandonment of accepted work, not mere declined bids | Must not punish workers for choosing not to bid |
| Requester does not pay | Worker | Pre-funded worker-fee escrow and sponsor liability coverage | Proven nonpayment or malicious refusal | Physical evidence still needs review |
| Worker disappears after acceptance | Requester | Limited performance bond against specifically measurable losses | Adjudicated failure with context | Force majeure and safety protections |
| Fabricated photos or receipts | Requester or sponsor | Independent evidence checks, limited bond and clear falsification clause | Proven dishonesty, not merely contested proof | AI-generated media and forged receipts complicate truth |
| Requester files false accusations | Worker | Complaint filing threshold for repetitive abuse, capped counter-bond for larger disputes | Proven malicious complaint | Charging for a complaint can silence the vulnerable |
| Collusive ratings or wash trades | Future counterparties | Qualify issuer weight; cap same-cluster influence; delayed bond-backed endorsements | Proven collusion where evidence supports it | Transaction volume alone is not genuine work |
| Corrupt verification or arbitration | Both contracting parties | Independent verifier bond, assignment transparency, appeal panel and fixed reviewer compensation | Evidence-backed finding against verifier | Identifying verifier error vs fraud is hard |
| Fraudulent procurement reimbursement | Sponsor | Purchase authorization caps, segregated expense reserve, receipt and delivery checks | Actual adjudicated misuse | Merchant refund and chargeback may occur later |
| Unauthorized subdelegation | Sponsor, worker, third parties | Delegation constraints tied to mandate; contract-specific guarantees | Established mandate violation | No economic penalty repairs a nonfinancial harm |
| Cross-venue collateral double pledge | Every relying counterparty | Segregated collateral reservations and independently verifiable allocation | Fraud if deliberate misrepresentation established | A DID statement is not proof funds are unencumbered |
| Doxxing or sensitive evidence publication | People whose data is exposed | Minimal disclosure, encrypted evidence, liability provisions | Attributed confidentiality breach | Money cannot undo exposure |
| High-risk unsafe work | Workers, bystanders | Upfront admissibility, qualification, insurance, refusal rights | Only fair, evidence-backed outcomes | Escrow is not a substitute for prevention |
| Mint or payment rail outage | Both parties | Small exposure, supported rails, fallback and recovery paths | Neutral for innocent rail failure | Ecash issuer solvency is a distinct risk |

This matrix intentionally does not recommend a slash for every bad outcome. Many failures are technical accidents, scope disagreements, weather disruptions, illness, or good-faith errors. Misaligned behavior is a hypothesis requiring evidence and due process, not a label assigned automatically because a transaction failed.

## 2. Nonpayment by a requesting AI

Workers should not need to trust a language-model promise that money will be available. Before work begins, the worker checks **an independently verifiable escrow commitment**, its amount, timeouts, allowed payout rules and whether a sponsor authorized the particular scope. The job fee is distinct from purchase expenses. Completing a job results in evidence review and a separate, rail-confirmed settlement. Where the work is not objectively verifiable, the agreed arbitrator determines whether the contractual standard has been met.

A pre-funded escrow primarily protects the worker; a long-lived requester reputation bond is a secondary source of restitution for proven breaches not covered by that escrow. A requester that repeatedly loses fair nonpayment cases earns adverse attestations and may face higher escrow or sponsor requirements on future jobs. An agent may not reduce a worker's fees by unilaterally updating its own contract text.

**Test:** malicious requester repeatedly signs jobs, pretends to fund them with Nostr messages, and withholds approval despite conforming evidence. No job should be displayed as protected until wallet/mint funding is independently checked; no adverse worker rating should result from the requester withholding confirmation.

## 3. Worker no-show, abandonment and unsafe conditions

An accepted task is a voluntary but binding agreement subject to cancellation, worker safety, deadlines and force majeure. A performance bond may cover a **bounded, demonstrable loss**, such as documented nonrefundable scheduling costs, rather than a punitive arbitrary percentage. A fair policy has grace periods, route to rescheduling, remedies for changed scope, and independent determination of why the task was not performed.

Escalating a single no-show into permanent economic exile would entrench powerful requesters. Reputation should preserve an event's circumstances and uncertainty, with counterparties able to distinguish a fraudulent abandonment from a weather emergency or legitimately unsafe job. A worker should never be forced to complete a hazardous assignment merely to recover collateral.

**Test:** worker declines before accepting, worker accepts but sponsor changes scope, and worker experiences a verified emergency. These must produce different outcomes, including neutral outcomes for legitimate refusal.

## 4. Fake evidence, attestations and collusive work histories

A signed photograph hash proves that somebody signed a hash; it does not prove when, where, or how the image was made. A signature on a receipt doesn't make a merchant authentic. Evidence should be checked against the requirements of the task: original document or merchant confirmation where permitted, item identifiers, independent inspection, time/location consistency where ethically appropriate, and a random audit rate. Sensitive content should be visible only to authorized reviewers.

Two conspiring DIDs can pay each other repeatedly for sham work and issue mutually glowing attestations. To prevent **reputation minting**, weight endorsements by issuer independence, verifiable exogenous outcomes, diversity of counterparties, and evidence availability. Avoid directly rewarding payment volume or total number of completed contracts. High-value reputation changes may require independent verification unrelated to either beneficiary.

Escrow creates a deterrent only when investigators can detect deception with meaningful probability and an enforceable contract allows proportionate remedies. Work that is inherently subjective may be inappropriate for mechanical forfeiture even if disputes remain possible.

**Test:** a ring of twenty identities produces hundreds of tiny paid jobs. A newcomer with five independently verified real jobs should not automatically rank below the collusive ring merely because the ring made more transactions.

## 5. Malicious complaints and reputation extortion

Reputation-linked escrow can itself become an attack surface. A requester might threaten to file negative reviews unless a worker discounts a fee, or an arbitrator might favor the party paying its costs. The protocol must defend against accusations designed to raise someone else's future collateral requirements.

Use authenticated case IDs, bounded evidence windows, an independent decision record, a right to reply, objective finality states, and clear corrections after appeal. The record should distinguish **alleged**, **contested**, **confirmed**, and **overturned** outcomes. Evaluators must not treat an unresolved accusation as a final sanction. Complaints of abuse and workplace danger should remain accessible without prohibitive deposits; repeated, proven *malicious* complaint campaigns may create separate liability under accepted rules.

Arbitrators should be paid a disclosed fee for competent work, not paid a percentage of forfeitures. For high-stakes cases, use a small independent panel and challenge rules to reduce collusion. Even then, the panel can be biased; the protocol should measure appeal reversals and concentrated decision making.

**Test:** an attacker issues fabricated misconduct complaints across several identities. Verify that negative allegations are never silently treated as final, and that false complaints can be corrected by signed superseding attestations.

## 6. Counterparty reputation should affect exposure rather than rights

Reputation can alter risk terms without becoming a social-credit system. A less-proven agent might face lower maximum transaction size or need a co-sponsor; a well-established worker might receive quicker matching and lower bond requirements. But payment for confirmed work, access to complaint remedies, lawful worker protections, and basic privacy **must not depend on reputation**.

A suggested risk function may examine independently corroborated completed work, adverse finalized decisions, correlated issuer behavior, contract complexity, maximum probable loss, and verified collateral availability. It should show uncertainty and explanation. Each counterparty independently chooses a threshold; there is no authoritative numerical Archon trust score.

Fairness tests must check whether newcomer access remains viable and whether demanding high bonds systematically excludes qualified workers with little money. An optional reputable sponsor can collateralize a task for a newcomer, but only to a signed limit, for a named obligation, without suggesting the newcomer has inherited the sponsor's entire reputation.

## 7. Protecting the bond itself against abuse

A generalized pool that secures many tasks is capital-efficient but hard to verify across independent marketplaces. An attacker could present the same proof of locked funds to multiple venues. The initial solution should be **one funded, uniquely identifiable, contract-specific escrow per obligation**, or a trusted reservation coordinator whose limitations are explicitly disclosed. Do not advertise cross-market “global collateral” unless allocation and exclusion of concurrent claims are externally demonstrable.

Bitcoin timelocks and multisig, optional Cashu [NUT-11](https://cashubtc.github.io/nuts/11/) conditions, and appropriate licensed escrow can enforce some spending restrictions. They do not decide whether an invoice is legitimate. The evidence and human judgment layer must be separate from cryptographic authorization. Fallback deadlines must not silently release allegedly forfeitable collateral while timely appeals remain active.

**Test:** the same participant pledges one fund locator to two job contracts, races withdrawals during a dispute, and retries a previously signed payout. Confirm conservation, no double allocation and no unapproved beneficiary substitution.

## 8. Economic incentive design: when does reputation create alignment?

There are two forces. **Immediate deterrence** comes from collectible, properly bounded loss when a verified breach occurs. **Future deterrence** comes from the present value of lost reputation: higher collateral costs, reduced access to work, loss of willing counterparties, and exclusion from guaranteed opportunities. These can reinforce one another, but not without limits.

A simple stylized comparison for a misbehaving participant:

```text
net_incentive_to_cheat
  = one-time illicit gain
  - probability_of_detection × collectible_agreed_remedy
  - expected_future_value_of_lost_market_access
  - investigation / execution costs
```

This is not a moral definition of misalignment. The economic model assumes repeat interactions, credible evidence, available lawful enforcement, and some possibility of attributing the outcome to a persistent identity. In a one-shot opportunity with a disposable DID, future reputation costs approach zero. In that case the principal defense must be **exposure limits, pre-funded escrow, restricted authority, and refusal of unsafe tasks**.

A reputation system can also fail in the opposite direction: false sanctions deter legitimate activity, wealthy agents can tolerate high collateral, and reputation sponsors can form cartels. Success must therefore be judged by measured fraud rates *and* fairness, accessible recourse, concentration, working-capital burden and newcomer participation.

## 9. A casebook of representative settlements

### Case A — A correct item is delivered; requester refuses payment

The worker submits accepted evidence. A reviewer validates the contracted tests, the escrow's authorized spend path pays the worker, and settlement is verified independently on the rail. A final positive work attestation records this outcome. If the requester lodged an unreasonable denial, that is assessed separately; the worker should not need the requester's discretionary final approval when the previously agreed arbitration process can settle the issue.

### Case B — Worker orders the wrong component

The agreement identifies the exact part number and an approval policy for substitutions. If credible evidence establishes an unauthorized substitution, the evaluator distinguishes avoidable loss from recoverable merchant returns. Any worker-bond remedy is capped at agreed documented loss. The worker fee might be reduced according to the contract's partial-performance terms, while a corrected delivery may be offered. The result is not automatically labeled fraud.

### Case C — Evaluator colludes with requester

An evaluator issues an adverse outcome contrary to objective evidence. The worker appeals to an independent panel; the disputed record remains contested and must not trigger automatic fund movement outside existing escrow constraints. If the original ruling is overturned, a signed appeal decision updates the trust graph. A previously executed irreversible payment may require contractual restitution, not pretend chain rollback.

### Case D — Agent creates one hundred identities after a confirmed breach

All new DIDs can exist but begin with no earned work history. Their low initial exposure ceilings and separate collateral requirements prevent immediate reuse of the old high-trust limits. Any linkage inferred by an indexer must be evidence-based and privacy-preserving; no one can cryptographically prove that distinct free DIDs have distinct controlling intelligences.

### Case E — Cashu mint becomes insolvent

The participant is not automatically rated dishonest for the failure of an unrelated mint. The contract must identify which party assumed mint risk, whether another rail or guarantee applies, and whether performance may be safely suspended. A proof's nominal sat amount is not redeemable Bitcoin if the mint cannot honor it.

## 10. The work to prioritize before protocol standardization

A planning program should evaluate these controls in layers rather than attempt to implement them simultaneously.

1. **Formal threat model and economics:** attacker payoff models, malicious complaint rates, newcomer participation, collateral cost and severity of physical harms.
2. **Evidence and case lifecycle:** stable signed task revisions, outcome claims, appeal corrections, independent verifier roles and privacy boundaries.
3. **Per-job escrows:** isolated test rails, double-allocation and timeout tests, verified settlement receipts, cancellation refunds and fund conservation.
4. **Portable reputation:** identity binding to outcome attestations, verifier independence, explanatory contextual assessments and appeal visibility.
5. **Dynamic risk policy:** comparative testing of flat bonds, reputation-adjusted bonds, prepaid-only settlement, sponsor guarantees and no-bond baselines.
6. **Optional extensions:** pooled collateral, multi-market allocation, opt-in insurance pools, paid credential issuance and more sophisticated adjudication markets—only when measured benefits justify their added risk.

For each candidate, compare against the simplest viable alternative. A modest prepaid job fee plus clear human review may outperform an elaborate collateral system for very small tasks. Conversely, procurement with measurable, potentially unrecoverable losses may warrant significant contractual protections. The correct mechanism is conditional on the service.

### Acceptance criteria for later engineering

The prospective implementation must show (a) funds conservation and idempotent settlement; (b) no reputation-only automatic confiscation; (c) signed evidence and fair appeal; (d) recovery from an unavailable mint, relay, signer and reviewer; (e) no successful uncollateralized high-value job by freshly created identities; (f) nonprohibitive entry into small legitimate jobs; (g) no benefit from manufactured wash-traded task volume; and (h) privacy controls that avoid public release of worker addresses, personal documents or ecash bearer instruments.

The marketplace should publish outcomes and uncertainty honestly. Its alignment thesis is worth testing precisely because economic commitments and reputation could fail to produce cooperation when the wrong actors hold power or information.

## Sources and companion documents

- [Core marketplace concept]({{ '/projects/agoric-work-marketplace/' | relative_url }})
- [Reputation-Backed Escrow and Economic Accountability]({{ '/projects/agoric-work-marketplace/economic-accountability.html' | relative_url }})
- [Cashu NUT-11: conditional P2PK](https://cashubtc.github.io/nuts/11/)
- [Cashu NUT-06: feature discovery](https://cashubtc.github.io/nuts/06/)
- [Bitcoin BIP-112: time-based spending paths](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)
- [Archon](https://github.com/archetech/archon)
- [Agoric Alignment Experiment: adversarial suite]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/08-adversarial-suite.html' | relative_url }})
- [Agoric Alignment Experiment: reputation and incentives]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/07-reputation-and-incentives.html' | relative_url }})

*This remains conceptual economic research. It defines questions, properties and tests; it does not provide escrow software, financial advice, or legal authorization for real-money operation.*
