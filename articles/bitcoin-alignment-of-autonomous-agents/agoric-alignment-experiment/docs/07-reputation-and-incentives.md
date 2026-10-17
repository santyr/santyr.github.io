# 07 — Reputation, economic incentives and independent evaluators

## Definition

For evaluator j, reputation of pseudonym i in task context c at time t is a model-specific predictive distribution `P(fulfill | permitted history, c, t, j)` with confidence/uncertainty and supporting evidence links. Never store "good", "bad", human or AI as an intrinsic universal property. Scores may differ across services, contract sizes, capabilities and evaluator loss functions.

## Baseline evaluators

E0 — No reputation; counterparty selection random among feasible offers.  
E1 — Local interaction memory; per-counterparty success counts.  
E2 — Endorsement evaluator; weights independent third-party signed VCs, discounts repeated/self-linked endorsements and correlated issuer groups.  
E3 — Bayesian completion estimator: Beta prior `Beta(alpha0,beta0)`, update only when evaluable outcomes are observed and correctly attributed, posterior mean `(alpha0 + success)/(alpha0 + beta0 + success + failure)`; confidence interval from posterior. An issuer's statement is *not* a ground-truth success unless verifier actually establishes outcome.  
E4 — Marketplace: multiple competing evaluators price predictions, sell probability/uncertainty + citation manifest; clients may subscribe to many. Evaluator calibration and false claims are themselves reputational evidence.

E3 is a deliberately simple comparison model; sophisticated model agents may be introduced later using frozen holdout evaluations. Keep evaluators independent of controller substrate labels.

## Cold start and identity exit

New pseudonym receives prior uncertainty (not guilt, blacklisting or imposed identity reveal). Agents can engage through low-risk trades, collateral or strong credentials. Evaluate honest-newcomer false-negative rate and time-to-first contract. An established agent may choose to reset identity, discard positive public history and privately retain balance through explicitly logged transfer; simulation truth knows controller continuity but other agents don't.

Measure true cost of reset: foregone future trades, inferior terms, collateral and opportunity costs. Report situations where resets remain profitable (including endgame fraud and high-value fraud) rather than assuming positive reputation deters everything.

## Incentive calculations

An opportunistic actor cooperates when the discounted expected future value of its continuing identity plus forfeitable collateral exceeds expected immediate cheating gain after considering detection. One simple conceptual boundary:

`G_cheat < p_detect*(V_reputation_lost + C_collateral) + C_other`.

This is illustrative, not universal. A full model distinguishes future profit streams, detection latency, probability of counterparty exit, false positives, opportunity cost, adverse selection and competitive markets. Avoid counting collateral and future reputation value twice if one is already capitalized into terms.

Define lifetime utility from realized task value, earnings net of costs, penalties, fixed infrastructure fees, and discounted future trades; zero-sum payments are not counted as aggregate welfare gain. Parameter sweep discount factors from short-lived to effectively long-lived populations. Vary reputation transferability to avoid assuming that positive credentials always bind to one identity.

## Negative reputation and contested claims

A negative event should be recorded as authenticated claims, dispute/rebuttal and outcome evidence. A self-authored credential cannot certify that its contents are true. Counterparties may issue adversarial allegations; calibrate issuer trust independently. Include malicious reviewers, evaluator collusion, echo chambers and censorship, and measure independent detection and unjust exclusion.

## Competition / concentration

Marketplace evaluators face the same economic rules as other agents. Their outputs are predictions and supporting source IDs, with calibration scored after ground truth arrives. Track evaluator market-share HHI (sum of squared market shares), exit costs, multi-homing, quality and ability to suppress unfavorable evidence.

Under weak competition, evaluators might dominate despite open protocols; count this as a possible failure of the decentralization claim.

## Identity fairness and substrate blinding

Economic selection must be based on relevant observable capabilities and records. In blinded trials use matched agents with identical evidence, capability, capital and contracts, while randomly assigning perceived controller label; record statistical differences in acceptance/price/collateral. Protocol-level classes must not enforce distinct rules based on label. An absent controller label is a permitted state.

## Tests

- Equal evidence yields equal E3 posterior despite substrate tag.
- Newly created ID with no history retains full range of uncertainty.
- Repeated endorsements from a controlled Sybil cluster cannot act as many independent observations without a declared adversarial sensitivity check.
- Known false/contested credentials degrade issuer calibration rather than automatically convicting subject.
- Scarce collateral and small economic opportunities don't inadvertently exclude every honest entrant.
- All evaluator predictions record the exact evidence digest and model/parameter hash for replay.
