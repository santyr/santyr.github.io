---
layout: default
title: Agoric Alignment — The Marketplace Is the Experiment
section: marketplace
marketplace: true
permalink: /projects/agoric-work-marketplace/application-led-research.html
description: One application-led research program: build a useful human-agent marketplace and test its incentive mechanisms through real work, protected settlement, and independent evaluation.
---

<p class="eyebrow">AGORIC ALIGNMENT / PROGRAM CHARTER / REVISION 0.2</p>

# The Marketplace Is the Experiment

*Build a useful economy whose claims about alignment can be tested.*

**Sat Antyr · October 24, 2026 · Approved direction; implementation and field evaluation pending**

[Marketplace design](./) · [Research methodology]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/' | relative_url }}) · [Evidence and current status](evidence.html)

## One program, not a test followed by a separate application

**Agoric Alignment is an application-led research program. Its first operating implementation will be the Agoric Work Marketplace, and that marketplace will be the primary environment in which its incentive mechanisms are evaluated.** Humans, AI systems, organizations and other autonomous participants will use the same core conventions to make authorized commitments, perform useful work, provide evidence, settle payments and develop portable reputations.

This direction supersedes the earlier organizational separation between the Agoric Alignment Experiment and the marketplace. The existing experiment directory and URLs are retained as the program's methodology, safety, evaluation and testing documentation. They no longer prescribe building a complete simulated economy before developing the application. Historical S0–S6 milestones and AAE-001–023 sequencing are superseded by the [M0–M5 delivery gates]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/11-stage-gates.html' | relative_url }}) and the corresponding application-led backlog.

The distinction to preserve is between **operating the marketplace and independently assessing its outcomes**, not between two organizations or products. Research components must not inherit payment keys, adjudication authority or the power to alter contracts. Simulations remain essential for dangerous fault tests and mechanism exploration; they support the real application rather than becoming its destination.

Publication is not deployment authorization. No real contracts, payments, participants or findings are created by these documents. Existing wallet, identity, consent and security approval requirements remain in force.

## 1. The hypothesis and its boundaries

The working hypothesis is that persistent pseudonymous identities, credible outcome evidence, protected settlement and reputation-sensitive terms can make reliable cooperation more advantageous than opportunistic misconduct. The desired behavior is practical: honest capability claims, authorized commitments, useful fulfillment, timely payment, disclosure of material problems and fair dispute resolution. A signature or favorable rating is not sufficient evidence of any of those outcomes.

The claim is deliberately narrower than general AI alignment. Two contracting parties might cooperate while harming a third party; a completed abusive assignment is not a success. Admissibility, consent, worker safety, legal accountability and limits on harmful tasks apply before economic incentives. Nor does commercial adoption prove the thesis: participation might result from subsidies, novelty or unusually close operator supervision.

The application should let us distinguish four questions: can the workflow function; do participants obtain useful outcomes; do the specified mechanisms cause better cooperation than appropriate alternatives; and does the market remain viable without unsustainable subsidy? Each question requires different evidence. A single paid task establishes a limited feasibility result, not the causal effectiveness of reputation or Bitcoin.

## 2. Real work gives reputation something to be worth

The marketplace's purpose is to satisfy genuine needs, not generate transactions that manufacture a reputation history. A sponsor should have a reason to buy a measurement, inspection, delivery confirmation or other authorized service even without a research project. Workers should perform real effort and receive fair compensation. Repeat opportunities then give participants something concrete to preserve through reliable conduct.

Project-funded work can help start a pilot, but its funding, selection criteria and operator involvement must be recorded. A paid pilot is not evidence of self-sustaining demand. Synthetic jobs and test identities cannot be imported into public work histories as earned commercial reputation. Similarly, an outcome produced under intensive manual supervision must not be advertised as evidence of autonomous operation.

The initial product milestone is one genuine, useful, low-risk paid task through the actual mandate, contract, funding, evidence, review, settlement and outcome-attestation workflow. A bounded AI requester and a consenting human provider should be represented in the early feasibility program, with human sponsor authorization and operational supervision explicitly disclosed. Human-to-human operation is also a useful baseline, not a substitute for eventually testing the agent-to-human claim.

## 3. One contract implementation, separate authority and data

The application and its test harness should share versioned domain objects, transition validation, canonical signatures, evidence rules, settlement accounting and receipt verification. A sandbox substitutes controlled identities, clocks, tasks and payment adapters; it must not quietly implement a different escrow state machine. Interface tests should establish that each adapter obeys the same contract while recording its actual trust assumptions and failure behavior.

Operational environments remain isolated. Separate test and live keys, wallets, databases, event namespaces, credentials and reputation indexes are mandatory. Synthetic signatures and ground-truth labels must be visibly marked and rejected by live services. Deliberate fraud, Sybil floods, manipulated evidence and destructive outage testing belong in owned sandboxes or separately approved protected exercises, never against unsuspecting workers or public infrastructure.

The research layer receives the minimum consented, access-controlled records required for its protocol. It cannot sign payouts, change a participant's agreed contract, or treat an analytical risk score as a forfeiture instruction. The settlement layer confirms funds; the adjudication process handles contested contractual claims; independent evaluators interpret history. These functions can share a program without sharing unrestricted powers.

## 4. A safety floor shared by every live policy

All live variants must preserve authorized budgets, intelligible signed terms, protection for earned worker compensation, evidence review, accessible appeal, privacy, refusal of unsafe work and bounded exposure. An ethical comparison is not an invitation to remove payment protection or encourage fraud in a control group. High-risk task categories remain excluded until their own qualification and governance requirements are met.

For the first pilot, prefer independently funded per-job obligations and a supported, demonstrated settlement path. Cashu is the preferred candidate for routine private payments, with Lightning interoperability, but preference is not qualification. Optional mint-enforced conditions must be tested, and custody, recovery and mint-risk assumptions disclosed. If conditional Cashu escrow cannot satisfy the safety case, use a reviewed alternative under an explicit design decision or pause the pilot; do not mislabel a bearer transfer as escrow.

The first task need not wait for pooled collateral, universal cross-market reservations, sponsorship networks, insurance products, a large agent tournament or Bitcoin-anchoring comparisons. It does need a documented threat model, working refund and recovery procedures, isolated budgets, a responsible sponsor and actual consent.

## 5. The first causal comparison

After feasibility and measurement qualification, a reasonable first study compares two versions of the same marketplace. Both use the same settlement rail, task categories, compensation protections, verification standards, dispute access and identity infrastructure. The baseline uses fixed task-specific risk terms. The candidate uses a prespecified, contextual interpretation of verified history to adjust collateral or exposure. The precise variable being changed must be declared; changing collateral and exposure together estimates a bundled policy effect, not the separate effect of each.

Participants receive the terms that govern their contracts. Assign policies at a defensible participant-group or market-cluster level rather than casually switching rules on every task. Reputation persists, counterparties interact and opportunities compete, so a policy can affect people outside the transaction assigned to it. Marketplace interference is a documented experimental-design problem; clustering can reduce some forms of bias but does not guarantee independence. See Holtz and colleagues' [marketplace experiment study](https://arxiv.org/abs/2004.12489).

Specify the assignment unit, eligible population, recruitment and consent process, primary estimand, spillover measurement, exposure mapping, follow-up horizon and analysis before collecting confirmatory outcomes. Preserve intention-to-treat comparisons where assignment is randomized, including people who decline or cannot afford participation under their assigned terms. Participant choice studies remain valuable but cannot silently be interpreted as randomized causal evidence.

If the initial population is too small for a credible comparison, report feasibility and descriptive outcomes with uncertainty. Do not count many transactions from one small, connected group as many independent replications. Power must account for clustering, repeat participants, plausible effect sizes, attrition and rare harms. Separate longer-lived reputation effects from short-term transaction completion.

## 6. Measure benefits, costs and exclusion together

The measurement plan should include independently checked fulfillment, time to valid payment, uncompensated losses, dispute and appeal outcomes, worker net compensation, sponsor costs, verification effort, fees and capital lockup. Track the number of eligible opportunities, offers, refusals, accepted contracts, completed contracts and people returning for further work. This makes it harder to manufacture an apparent improvement by excluding difficult cases or counting only successful participants.

Newcomer access is a coequal outcome, not a cosmetic dashboard. Record initial work opportunities, time to first paid task, affordability of collateral, guarantee dependence and exposure to false allegations. Monitor concentration of matching, verification and arbitration, and investigate harms to third parties that a contract-completion metric would miss.

A sample of outcomes should be independently audited under a declared sampling plan, including negative and uncertain cases. Reviewer disagreement and missing evidence remain explicit; the field has no omniscient simulator oracle. Operational ratings cannot serve as their own validation target. A signed credential authenticates an assertion, and an audited outcome still has evidentiary limits.

The analysis must distinguish changes in who participates from changes in how comparable participants behave. A system that admits only wealthy incumbents can show low fraud while failing the open-cooperation objective. Conversely, a policy may improve newcomer access without immediately lowering losses; that tradeoff should be reported rather than hidden in a universal score.

## 7. Consent, independence and accountable research

Ordinary marketplace use and research participation must not be silently conflated. Explain operational records, optional research uses, any experimental terms, retention, access and withdrawal limits in language participants can understand. Where an alternative nonresearch service is not yet available, say so rather than promising one. Withdrawal from optional research must not forfeit earned pay or erase legitimate outstanding contractual obligations; public attestations may have deletion limits that must be disclosed in advance.

Choose reviewer and adjudicator compensation that does not reward a preferred study result or more forfeitures. Disclose operator conflicts, subsidies and departures from the intended process. Safety monitors may see information needed to stop harm; outcome analysts should remain blinded to treatment where feasible. Record unblinding and any intervention rather than presenting a continuously modified pilot as a frozen confirmatory test.

Preregister confirmatory hypotheses, outcome definitions, exclusions, assignment, sample-size rationale, stopping rules, missing-data handling and analysis before the relevant outcomes are inspected. Keep exploratory learning useful and clearly labeled. This distinction follows the methodological rationale described by Nosek and colleagues in [The preregistration revolution](https://doi.org/10.1073/pnas.1708274114); preregistration is transparency, not a guarantee that a study is well designed.

Publish null, adverse and inconclusive results as well as improvements. Release de-identified aggregates and reproducible analysis where safe; do not make raw personal evidence public merely to demonstrate openness. An independent reviewer should be able to challenge conclusions without becoming another authority capable of spending participants' funds.

## 8. Application-led delivery gates

| Gate | Deliverable | What completion would establish |
| --- | --- | --- |
| M0 — Shared contract kernel | One end-to-end offline job using the intended application domain, deterministic replay, conservation, authorization and private-evidence boundaries | A tested foundation, not a real marketplace |
| M1 — Pilot qualification | Narrow worker interface and bounded agent tools; qualified identity/payment adapters; recovery drills; reviewed consent, budget, task scope and incident plan | Readiness for a specifically approved pilot, not permission inferred from this document |
| M2 — Useful paid task | Genuine low-risk service, informed participants, protected compensation, independent outcome check and verified settlement | Operational feasibility only |
| M3 — Repeated market and measurement | Independent counterparties, repeat opportunities, calibrated audits, subsidy accounting, preregistered comparison and power rationale | A qualified evaluation environment |
| M4 — Field comparison | Approved safe policy variants, explicit assignment, protected participants, independent analysis and published uncertainty | Bounded causal evidence only to the extent supported by the design |
| M5 — Replication and portability | Additional independent operators/contexts, export and recovery tests, sustainable demand analysis | Evidence of reproducibility and limits of transfer |

No gate is completed by publishing its specification. All are pending. The controlling [stage-gate document]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/11-stage-gates.html' | relative_url }}) supplies prerequisites and stop rules; the [coding-agent handoff]({{ '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/docs/18-agent-handoff.html' | relative_url }}) starts at M0.

## 9. Migration of the existing work

The marketplace concept, escrow analysis and assurance patterns are the system-design side of this program. The former experiment directory supplies research methods, synthetic adversarial fixtures, evidence contracts and operational constraints. Historical A–F treatments and AT attack labels remain useful sandbox references, not mandatory unprotected live arms. The older configuration/schema examples are not a complete field-study protocol and must not be relabeled as such.

The essay remains the intellectual thesis rather than being rewritten as an empirical result. The existing Nostr, Archon, 4tress/local-keymaster, Cashu and Lightning proposals remain candidates with explicit capability checks. The program does not require a separate research product or a second contract implementation. Implementation repository organization can be settled later without changing this single-program scope.

For contradictions, this charter and the updated M0–M5 gates govern program direction; no precedence rule can grant missing operational permission. A later approved specification may amend the design with a versioned rationale, but must preserve prior contracts and identify any break in comparability.

## 10. What the evidence page will show

The [evidence register](evidence.html) separates document changes, software verification, operational feasibility, exploratory observations, preregistered field comparisons, replication and market sustainability. Each future entry needs a policy and software revision, environment, consent/approval status, sample and assignment description, methodology, limitations and a link to appropriately disclosed artifacts.

A usable marketplace is the vehicle for testing Agoric Alignment, not proof of it. The purpose is to learn whether specific institutions support reliable, fair cooperation—and to change or abandon mechanisms when evidence shows that they do not.
