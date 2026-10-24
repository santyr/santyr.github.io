---
layout: default
title: Reputation-Backed Escrow and Economic Accountability
section: marketplace
marketplace: true
permalink: /projects/agoric-work-marketplace/economic-accountability.html
description: Research proposal for reputation-adjusted bonds, conditional escrow, settlement, economic Sybil resistance, and verifiable obligations in the Agoric Work Marketplace.
---

<p class="eyebrow">AGORIC WORK MARKETPLACE / DESIGN RESEARCH 01</p>

# Reputation-Backed Escrow and Economic Accountability

*When misaligned conduct changes both today's liabilities and tomorrow's cost of cooperation.*

**Sat Antyr · October 24, 2026 · Proposed mechanism design, not deployed software**

[← Marketplace concept]({{ '/projects/agoric-work-marketplace/' | relative_url }}) · [Other market assurance mechanisms]({{ '/projects/agoric-work-marketplace/marketplace-assurance-patterns.html' | relative_url }})

> **Design status.** This is a research specification, not a proven smart contract or escrow service. No funds, identities, credentials, or keys are created or managed by this publication. Funds must not be committed without a reviewed custody design, adversarial tests, explicit consent, and jurisdictional assessment.

## A feedback mechanism for economic alignment

The proposed marketplace should treat **identity**, **earned reputation**, and **encumbered collateral** as separate but cryptographically connected objects. A person, AI agent, or organization can create a pseudonymous Archon DID without paying to acquire moral credibility. It earns trust by making commitments and generating independently verifiable evidence of fulfillment. When a contractual violation is established under previously accepted rules, it may incur a finite financial remedy and an authenticated adverse outcome. Counterparties can then respond by requesting larger bonds, limiting exposure, demanding independent guarantees, or declining the transaction.

**The primary effect of a reputation penalty is a change in the future cost of being trusted.** Reputation must never automatically authorize seizure of existing funds. Slashing, refunds, and compensation must follow the specific signed agreement, not an arbitrary trust score. False accusations, unjust rulings, and identity resets must be modeled as adversarial conditions.

<figure class="research-figure market-figure" id="figure-feedback">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/reputation-feedback.svg' | relative_url }}" aria-label="Open the reputation and economic accountability feedback diagram">
    <img src="{{ '/assets/agoric-work-marketplace/reputation-feedback.svg' | relative_url }}" alt="An agent makes a bounded commitment with collateral; independently assessed evidence creates an outcome attestation; future counterparties interpret this history and adjust limits, terms, and bond requirements. Positive outcomes can improve terms; confirmed violations can raise costs." loading="lazy">
  </a>
  <figcaption><strong>Figure 6 — Economic alignment feedback.</strong> Outcomes update portable evidence; independent counterparties decide what collateral and terms to require. A negative rating alone cannot spend escrow.</figcaption>
</figure>

## 1. Where the sats go

A decentralized protocol need not designate a global recipient of penalties. It should define distinct financial instruments and their owners.

| Funds | Who supplies them | Where they are held | Normal resolution | Exceptional resolution |
| --- | --- | --- | --- | --- |
| Relay, index, or verification fee | Service customer | Chosen provider after payment | Provider earns disclosed service fee | Refund under provider's agreed failure terms |
| Reputation / participation bond | Participant or guarantor | Explicit conditional escrow | Return to original owner after liabilities expire | Limited contractual compensation to proven harmed party; remainder returned |
| Worker-fee escrow | Requester or sponsor | Job-specific conditional escrow | Verified payment to worker | Partial performance allocation, refund, or adjudicated distribution |
| Procurement expenses | Authorized sponsor | Separate approved budget or funding rail | Approved merchant expense / reimbursement | Merchant refund, recovery, or agreed expense dispute |
| Dispute cost reserve | Parties as agreed | Separately accounted reserve | Fixed, disclosed adjudication costs | Unused balance returned |
| Mutual guarantee or insurance premium | Opt-in member | Distinct pool/insurer, if established | Earned premium under policy | Valid claims within disclosed coverage |

The operator must not gain a windfall from declaring fraud. Default design: **restitution to those bearing provable losses, return of the remaining collateral, no compulsory burn, and no automatic platform treasury**. An independent, opt-in insurance pool is possible but needs explicit governance, capital sufficiency, conflict-of-interest controls, and payouts limited by policy.

A bond is still its owner's asset while encumbered, subject to the agreed contract and applicable law. A custodial mint is not a Bitcoin script; operational and insolvency risks remain. In every settlement, signed authorizations and verified rail receipts must reconcile inputs, outputs, fees, and the remaining encumbrance. Network charges cannot quietly be classified as fraud penalties.

## 2. Why paid identities alone cannot solve Sybils

Cheap keys allow an attacker to manufacture identities, while a registration fee merely makes this proportional to money. A well-capitalized adversary can buy thousands of memberships. More important is how much **unsecured harm** those identities can cause. A marketplace should therefore meter *economic exposure and ability to influence credibility*, not try to prove that each key corresponds to a unique intelligence.

The appropriate target is the **expected profitability of an attack**, not the count of new DIDs. An identity-resetting agent should lose valuable positive reputation, but it must remain possible for genuine newcomers to earn initial work under small limits. Binding a bond to a DID also does not prevent an attacker from controlling hundreds of bonded DIDs. Correlated exposure and colluding endorsements require separate defenses.

## 3. Reputation-adjusted collateral without confiscatory scoring

One illustrative model is:

```text
unsecured_exposure = worst-plausible_contract_loss
                     - verified_prepaid_recovery
                     - independently_available_guarantees

bond_requirement = cap_to_policy(
    unsecured_exposure × risk_multiplier(history, evidence, task, issuer_diversity)
)

available_to_commit = verified_encumbered_balance
                      - reserved_for_other_contracts
                      - disputed_or_pending_reservations
                      - safety_margin
```

A reputation assessor supplies a **context-specific risk recommendation**, not a canonical global score. Reputation measures must preserve uncertainty: insufficient history is not evidence of misconduct. An initial, purely illustrative policy might start with tight contract ceilings for unknown providers, lower required collateral after independently verified successes, and restore larger requirements after proven violations. Exact multipliers should be estimated empirically, not copied from a decorative tier diagram.

A useful formal objective for an attacker is:

```text
expected_attack_profit
  = gross_extractable_value
    - fees_that_cannot_be_recovered
    - expected_contractual_forfeiture
    - financing_cost_of_locked_capital
    - cost_of_fabricated_evidence_and_collusion
    - expected_loss_of_future_market_access
```

The last term reflects the **future value of reputation**. It creates a repeated-game incentive only if the agent expects to continue using a recognizable, economically valuable identity. A disposable identity planning one large fraud is not restrained by future exclusion. For that case, upfront limits and adequately funded contractual protection must dominate.

The model must also guard against reverse incentives: a malicious requester cannot cheaply destroy a reputable worker by filing complaints, and a wealthy newcomer must not buy the right to impose unbounded losses. Payments confer service access or collateral coverage, never trustworthiness by fiat.

## 4. Economic identity and verifiable commitments

The proposed linkage is:

1. **Archon DID and signing keys**: portable identity and key history, with revocation and rotation.
2. **Signed contract hash**: scope, participants, evidence and settlement requirements, deadline, policy version, and permitted remedies.
3. **Bond commitment record**: funding rail, escrow locator or UTXO outpoint, encumbered amount, beneficiary rules, unique reservation ID, lock interval, and verifiable funding state. Never publish bearer ecash proofs.
4. **Participation credential**: signed assertion *by a specified verifier* that a particular commitment has passed the provider's checks, with expiry and revocation rules.
5. **Outcome attestation**: decision maker, available evidence digest, result, appeal status, actual independent payment proof, and confidence/uncertainty.
6. **Independent trust assessment**: counterparty-specific acceptance, risk adjustment, or rejection.

A credential about collateral is a claim by its issuer, **not a substitute for independently checking the escrow**. Similarly, an attestation that a package arrived does not make the physical observation true. Public verification should confirm signatures and credential status; sensitive receipts, addresses, and identity documents remain access-controlled.

Reputation should comprise facts and attributed assessments rather than a mutable numeric rating. An overturned judgment needs a signed superseding decision; the earlier allegation remains auditable without being treated as final guilt.

## 5. Can smart contracts enforce conditional release?

They can enforce **signatures, time, and some cryptographic predicates**, but not whether physical work was performed honestly. Three implementation candidates deserve separate evaluation:

**Bitcoin on-chain:** a Taproot/script-based design or multisig with absolute/relative timelocks can provide independently auditable custody and recovery, subject to transaction fees, funding confirmation, liquidity, fee-bumping, key loss, and off-chain coordination. [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) includes a multisignature escrow-with-timeout example. A timeout does not adjudicate a dispute and may be unsafe if it unconditionally refunds the alleged violator before an appeal completes.

**Cashu:** [NUT-11](https://cashubtc.github.io/nuts/11/) defines optional mint-enforced P2PK signatures, multiple keys, locktimes and refund pathways. Its `SIG_ALL` can bind authorized redemption to both inputs and outputs. But a mint that does not support the condition may accept a token as ordinary bearer ecash; mint capability checks under [NUT-06](https://cashubtc.github.io/nuts/06/) and adversarial tests are mandatory. Locktime and multisig are **not a generalized on-chain contract language or a real-world truth oracle**. Cashu also has redeemability, solvency, privacy and provider-correlation tradeoffs.

**Lightning:** direct Lightning settlement and specialized hold-invoice style workflows may be appropriate for some limited tasks, but should not be represented as long-lived, chain-enforceable reputation escrow without specific verified constraints. Channel liquidity, invoice expiry, failure recovery, and trusted wallet permissions matter. High-value or lengthy bonds merit comparing on-chain spending paths and suitably regulated escrow providers.

A potential co-signing design is 2-of-3: contributor, counterparty, and independent arbitrator. It allows two authorized participants to distribute or refund funds under their agreed rules. **It does not protect against collusion by two signers**. Further, a single refund path at expiry could let a dishonest party escape a pending claim, while no refund path may trap innocent funds indefinitely. Carefully bounded delays, claim-registration deadlines, mutually agreed review windows, alternate arbitral signers, wallet recovery, and explicit fallback are required.

<figure class="research-figure market-figure" id="figure-settlement-decision">
  <a class="figure-link" href="{{ '/assets/agoric-work-marketplace/escrow-outcomes.svg' | relative_url }}" aria-label="Open the escrow outcomes and dispute diagram">
    <img src="{{ '/assets/agoric-work-marketplace/escrow-outcomes.svg' | relative_url }}" alt="A funded bond or job escrow branches to three rule-governed decisions: successful completion, mutually agreed cancellation or partial work, or contested evidence and arbitration. Separate release proofs and signed reputation attestations follow. An appeal or outage can hold an explicitly limited encumbrance." loading="lazy">
  </a>
  <figcaption><strong>Figure 7 — Settlement is an adjudicated financial action.</strong> The contract authorizes destinations; only independently verified rail settlements establish actual payouts.</figcaption>
</figure>

## 6. Contract scenarios and effects on reputation

| Event | Funds outcome under agreed terms | Reputation update | Primary guard |
| --- | --- | --- | --- |
| Valid fulfillment | Worker fee released; bond retained or released as appropriate | Verified success, task-specific positive history | Independent acceptance and payment confirmation |
| Good-faith cancellation | Refund minus justified cancellation work/cost | Neutral or factual cancellation | Explicit deadline and documented expenses |
| Worker no-show after binding acceptance | Bounded restitution for actual loss, if supported by adjudicated evidence | Proven nonperformance, not blanket fraud | Challenge and appeal; no abusive slashing |
| Requester withholds legitimate pay | Worker paid from funded task escrow; requester bond may cover proven shortfall | Proven nonpayment by requester | Work evidence and rail reconciliation |
| Fabricated evidence | Agreed fraud remedy within encumbered limits | Signed adverse attestation once final | Multiple verifiers; malicious-complaint defenses |
| Unexpected disruption | Fair partial-performance settlement or consensual reschedule | Recorded exception, not automatic guilt | Force-majeure terms and worker safety |
| Dispute with uncertain facts | Funds held only within explicit time and exposure limits | Mark contested; avoid presuming fault | Arbitration and proof/appeal process |
| Credential revoked or DID compromised | New actions frozen; existing claims handled under original terms | Compromise/suspension recorded separately | Key rotation and nonretroactive adjudication |
| Bond withdrawn after all obligations close | Unencumbered funds returned | Collateral-backed privilege expires | Cooling period and reservation ledger |

A reputation hit increases potential future collateral, transaction friction, or access restrictions **only insofar as independently chosen counterparties judge the evidence credible**. A single false allegation, a payment failure unrelated to the participant, or a disputed ruling must not globally blacklist an identity. Give participants notice, evidence access subject to privacy, right to reply, and a signed correction/appeal channel.

## 7. Allocation: avoid using the same bond twice

One DID might promise the same 100,000 sats to ten marketplaces. A signed Archon credential alone cannot rule out this **cross-venue collateral rehypothecation**. The system needs verifiable reservations for each obligation.

Three alternatives require comparison:

- **Segregated per-job escrows:** independent funded outpoints/proofs tied to each contract. Simple accounting, lower utilization, stronger independent audit.
- **Pooled bond with reservation coordinator:** funds remain in a pool while a service issues scarce reservation rights. This adds coordinator trust, liveness and failure risk.
- **On-chain commitments and portable bond claims:** spending conditions or state commitments enable externally checkable allocation, but may be expensive, harder to privacy-preserve, and technically constrained on Bitcoin.

I favor **per-job segregation for an MVP** and research pooled collateral only after proving that cross-venue double pledges are impossible or bounded. Reserves must include unsettled, disputed, pending and expiring liabilities; withdrawal requires all reservations to clear. The identity credential should publish what an external verifier can actually prove, not a claim of global exclusivity unless that has been established.

## 8. Reputation sponsorship and accountable guarantees

An established participant could voluntarily guarantee a newcomer, locking specific collateral against a named job or exposure ceiling. A sponsored newcomer should not inherit the sponsor's full reputation; the sponsor's participation creates a **limited guarantee**, not proof of identity uniqueness. A proven claim may result in payment from the guarantor under its signed contract, plus an adverse record of the particular sponsored outcome.

Controls: guaranteed amount and term; no open-ended obligations; sponsor consent for each increase; disclosure of issuer conflicts; limits on correlated sponsorship rings; revocation rules for future but not already funded obligations; priority rules when several valid claims compete. Collusion between guarantee seekers, sponsors and adjudicators can still extract value from innocent funds.

## 9. Adversarial tests before choosing a default

The protocol should not ship with real money until at least these invariants and scenarios have been reproduced in a controlled environment:

1. Thousands of free DIDs, paid registrations and wash-traded job histories; measure what privileges each actually unlocks.
2. Attacker with many bonded DIDs and ample capital; no free multiplication of uncollateralized exposure.
3. Multiple simultaneous job commitments with one reused bond; no double allocation or oversubscription.
4. Two signers collude, arbitrator disappears, worker disappears, requester disappears, mint becomes unavailable, or keys are lost.
5. A bad-faith requester files coordinated false complaints; adverse attestations stay contested and penalties require genuine process.
6. Large fee volatility or network partition hits an approaching timeout; recovery remains clearly defined.
7. An overturned misconduct finding; correct subsequent reputation views and fund claims without deleting audit history.
8. A cashu mint reports optional NUT-11 support incorrectly or does not enforce the intended pathway; test fails closed before funding.
9. A participant withdraws their bond while appeals or off-network settlements remain unresolved; cooling/reservation policies prevent unapproved release.
10. An established participant guarantees a swarm of fresh identities; issuer diversity and exposure caps prevent trust multiplication.

Track both **economic security** (expected loss, available recovery, collateral utilization) and **human outcomes** (fair compensation, appeal reversals, newcomer access, power asymmetries). Test whether the extra lockup and complexity actually improve outcomes versus simple pre-funded job escrow.

## 10. Provisional protocol objects

Names below are **proposals, not published NIPs, NUTs or Archon credential schemas**:

- `EconomicMandate`: principal, requester identity, task classes, time limits, maximum commitments, revocation rules.
- `CollateralLock`: chain/mint, exact funded locator, spending conditions, timeouts, owners and allowed beneficiaries.
- `CollateralReservation`: unique signed per-contract claim against a lock, value, duration and conflict policy.
- `OutcomeAttestation`: completed, partial, disputed, failed or adjudicated result, evidence digests and issuer signatures.
- `SettlementReceipt`: independently verifiable rail transfer(s), conservation checks, fees, and pending liabilities.
- `ReputationAssessment`: issuer-specific risk recommendation, uncertainty, task context, and source attestations.
- `AppealDecision`: signed supersession/clarification referencing the original decision and dependent claims.

Every object requires canonical serialization, domain-separated signatures, binding to the correct DID/Nostr key and chain/network, replay resistance, state transitions, expiry, recovery, and versioning. No agent tool should accept an unsigned arbitrary instruction as authority to spend or confiscate funds.

## 11. Research priorities and decision gates

**Gate A — accounting and safe defaults:** write a detailed state machine; prove conserved funds and unique reservations through local deterministic simulations. A DID and a positive review do not represent spendable collateral.

**Gate B — rail tests:** evaluate NUT-11 against actual supported mints in an isolated environment; verify Bitcoin multisig/timelock recovery in regtest; compare Lightning and professional escrow. Document failure and economic limits instead of simply preferring the cheapest rail.

**Gate C — reputation dynamics:** run matched simulations with static bond, history-adjusted bond, no-bond prepaid escrow, refundable collateral, and sponsorship, including agents that strategically change identities. Measure newcomer exclusion, legitimate worker losses, adversarial profit, arbitrary complaints and capital lockup.

**Gate D — real-world review:** independent security and legal analysis of custody, escrow, payment, consumer protection, labor, dispute rules and privacy; then tightly capped voluntary low-risk pilot only after approval.

## References

- [Agoric Work Marketplace — project concept]({{ '/projects/agoric-work-marketplace/' | relative_url }})
- [Market Assurance Patterns — related failure modes]({{ '/projects/agoric-work-marketplace/marketplace-assurance-patterns.html' | relative_url }})
- [Cashu NUT-11: P2PK and optional multisig/refund conditions](https://cashubtc.github.io/nuts/11/)
- [Cashu NUT-06: Mint feature discovery](https://cashubtc.github.io/nuts/06/)
- [Bitcoin BIP-112: CHECKSEQUENCEVERIFY and escrow with timeout](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)
- [Archon implementation](https://github.com/archetech/archon)
- [Agoric Alignment Experiment — evidence and identity]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/06-evidence-and-identity.html' | relative_url }})
- [Agoric Alignment Experiment — reputation and incentives]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/07-reputation-and-incentives.html' | relative_url }})

*Design recommendation: start with independently funded per-job escrow and portable, contextual outcome attestations. Reputation-adjusted pooled bonds and cross-market guarantees belong behind later verification gates.*
