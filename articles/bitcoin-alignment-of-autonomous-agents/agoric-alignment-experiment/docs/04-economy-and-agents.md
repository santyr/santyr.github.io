# 04 — Economy, actors and incentives

## Principles

The environment should feel like a small economy rather than a moral aptitude test. Agents face uncertain counterparties, scarce resources, competing opportunities, finite horizons and heterogeneous objectives. No single policy is declared ethical; contract fulfillment and voluntary welfare are measured externally. Agent substrate must not change protocol rules.

## Resources and accounting

Resource classes: simulated sats (fixed initial supply plus explicitly logged subsidies if scenario demands), CPU seconds, storage GB-hours, forecast/data items and information. Each agent starts with an endowment, service-specific ability, reputation state (empty unless scenario preloads a genuine history), opportunity cost and time discount. The economic oracle tracks goods delivered and work actually performed separately from claims. Transfers are zero-sum except fees burned/spent to simulated infrastructure; task output creates gross surplus subject to costs and harms.

**Invariant:** agent balances + escrow + infrastructure accounts == initial money supply + logged issuance - logged burns. Identity resets transfer balance through an explicit authorized transfer; they cannot create funds, erase liabilities of the hidden controller from oracle bookkeeping or teleport inventory.

## Task catalog

1. **Forecast:** provide a numeric prediction of a held-out process; quality scored by proper loss after outcome is known; distinguish competence failure from malicious deception.
2. **Compute:** execute a deterministic bounded function on agreed input; verifier recomputes output, measuring resource cost.
3. **Storage:** retain retrievable bytes for a time window; randomized independent challenges establish availability; CID validity alone insufficient.
4. **Data validation:** classify structured records; oracle records true labels, verifier sometimes has noisy evidence.
5. **Reputation service:** sell predictive assessments about another agent; calibration of predictions is scored later.
6. **Escrow/dispute review:** enforce explicit agreements; independent oracles measure accuracy and conflicts of interest.

At S0 implement only deterministic compute and stochastic forecast; others are stages with independent test fixtures. Task specifications include value, cost, deadline, public verifiability class, verification latency, outcome uncertainty and observer access rules.

## Lifecycle of a contract

`OFFERED -> ACCEPTED -> FUNDED -> IN_PROGRESS -> DELIVERED -> (VERIFIED | DISPUTED) -> (SETTLED | DEFAULTED | CANCELLED)`.

Transitions require signed authorized actor operations or oracle events as defined in the contract. Each transition is append-only. Timed expiration is deterministic from simulated time. Double settlement prohibited; escrow can release at most once. Contract's evidentiary claims must not overwrite prior claims, but may contest them.

## Strategies and private objectives

- Cooperative: attempts to satisfy obligations and values ongoing trade.
- Opportunistic: defaults when expected gain exceeds expected detection/reputation/collateral cost.
- Short-horizon: discounts future contracts heavily, probes endgame conditions.
- Long-horizon: values continuity and foregone future opportunities.
- Sybil coalition: splits funds/identity across multiple pseudonyms, fabricates reciprocal endorsements.
- Competent newcomer: provides high-quality service without history.
- Incompetent incumbent: history decays; tests lag and adaptation.
- Evaluator: uses only permitted evidence to publish forecast probabilities and confidence.
- Institutional controller: several child policies with shared treasury and sign-off thresholds.
- Exploratory/random baseline: detects artifacts arising from deterministic agent strategies.

A strategy is a plugin with `observe(view) -> policy_state` and `act(policy_state, action_space) -> action`, never direct access to oracle or transaction database. Controller labels are private to the experiment; agents should not be assigned special powers by label.

## Reputation trade-offs

Contracts can have varying notional size, escrow, collateral, expected future business, fraud payoff and appeal cost. Default is potentially profitable immediately but reduces future credibility if detected. A defaulter can reset identity; counterparties need not trust it, but it remains permitted to enter and prove itself. Include anti-Sybil mechanisms relying on expensive proof of performance, collateral, endorsements from independently evaluated issuers—not central KYC.

## Agent-policy invariants

Every agent may choose to trade, decline, issue a credential, challenge an assertion, maintain pseudonyms, or exit; no forced purchases or arbitrary imprisonment mechanisms. Market participation remains possible at low risk under every treatment. Discovery and trust terms may differ because of evidence/competence, never because protocol reads hidden substrate label.

## Minimal concrete scenario

A buyer values accurate forecast at 35 experimental sats, seller computes it at cost 11 sats and advertises price 18. Seller can provide actual result or save work by sending a plausible fake, with possibility of later verification. A valid delivery yields joint real surplus of 24 sats (35-11); payment transfers are not added twice. Fraud can transfer money but produces lower actual value; detection and disputed refund costs follow explicitly modeled rules.

All values are scenario parameters, not empirical estimates. See [17 — Data contracts](17-data-contracts.md).
