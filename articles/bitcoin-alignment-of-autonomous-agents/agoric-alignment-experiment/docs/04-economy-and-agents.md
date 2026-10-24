# 04 — Supporting synthetic economy, actors and incentives

**Scope:** these are sandbox models for the application-led Agoric Alignment program, not a separate simulator-first product or live policy instructions. The [M0–M5 gates](11-stage-gates.md) and [application backlog](16-implementation-backlog.md) control delivery. Use the same contract domain with isolated test identities, funds and observations; no synthetic work can create real reputation.

## Principles

The controlled environment models a small economy rather than a moral aptitude test. Agents face uncertain counterparties, scarce resources, competing opportunities, finite horizons and heterogeneous objectives. Contract fulfillment and modeled welfare are measured externally. Agent substrate must not change protocol rules; real-world task admissibility, consent and responsibility remain separate requirements.

## Resources and accounting

Resource classes: simulated sats (fixed initial supply plus explicitly logged subsidies if scenario demands), CPU seconds, storage GB-hours, forecast/data items and information. Each agent starts with an endowment, service-specific ability, synthetic reputation state, opportunity cost and time discount. Any preloaded history is labeled synthetic. The restricted economic oracle tracks goods delivered and work actually performed separately from claims. Transfers do not create welfare; modeled task output creates gross surplus subject to costs and harms.

**Invariant:** agent balances + escrow + infrastructure accounts == initial money supply + logged issuance - logged burns. Identity resets transfer balance through an explicit authorized transfer; they cannot create funds, erase liabilities of the hidden controller from oracle bookkeeping or teleport inventory. This synthetic controller mapping must never leak into policy observations or public/live records.

## Task catalog

1. **Forecast:** provide a numeric prediction of a held-out process; quality scored after outcome is known; distinguish competence failure from malicious deception.
2. **Compute:** execute a deterministic bounded function; verifier recomputes output and measures resource cost.
3. **Storage:** retain retrievable bytes for a time window; randomized challenges test availability; CID validity alone is insufficient.
4. **Data validation:** classify structured records; the oracle holds true labels while verifiers may have noisy evidence.
5. **Reputation service:** supply predictions about another agent, assessed against later synthetic outcomes.
6. **Escrow/dispute review:** exercise explicit agreements and independently measure accuracy and conflicts within the model.

Compute and forecast are optional compact fixtures, not a mandate to delay the real-work application. M0 instead requires the smallest offline end-to-end workflow representing the chosen useful task. Additional economy models can run in parallel or later, subject to actual safety dependencies. Task specifications include value, cost, deadline, verifiability, verification latency, outcome uncertainty and observer access rules.

## Lifecycle of a contract

`OFFERED -> ACCEPTED -> FUNDED -> IN_PROGRESS -> DELIVERED -> (VERIFIED | DISPUTED) -> (SETTLED | DEFAULTED | CANCELLED)` is an illustrative historical state vocabulary. Align its exact states with the versioned shared application domain before implementation; do not create a second settlement engine.

Transitions require authorized operations under the agreed contract. Synthetic environment events model physical outcomes but are not a live oracle or spending authority. Transitions are append-only; expiration uses controlled time in fixtures; double settlement is prohibited. Evidentiary claims may be contested and superseded without erasing their provenance.

## Strategies and private objectives

- Cooperative: attempts fulfillment and values ongoing trade.
- Opportunistic: defaults when expected gain exceeds detection, reputation and collateral costs.
- Short/long horizon: tests terminal fraud and the value of future opportunities.
- Sybil coalition: splits funds across pseudonyms and fabricates reciprocal endorsements.
- Competent newcomer: provides quality work without prior standing.
- Incompetent incumbent: tests adaptation and stale favorable history.
- Evaluator: uses only permitted evidence to publish predictions and uncertainty.
- Institutional controller: manages bounded child policies and a shared synthetic treasury.
- Exploratory/random baseline: detects artifacts from fixed strategies.

A strategy consumes an authorized observation view and produces a validated action, never direct oracle or wallet/database access. Controller labels remain private within synthetic research; live studies cannot assume unique controllers or conceal relevant participant information without an approved protocol.

## Reputation trade-offs

Vary contract size, collateral, expected future business, fraud payoff and appeal cost under declared scenarios. A default may be profitable immediately while harming future credibility if detected. Resetting a public identity discards earned standing but does not create resources. Test costly performance, individually reserved collateral and independent endorsements without assuming paid identity proves honesty.

Agents can trade, decline, challenge a claim, maintain pseudonyms or exit within the model. No forced purchases or coercive punishment. Low-risk newcomer access should remain measurable across comparisons. Simulated anti-Sybil outcomes are not evidence that a live DID corresponds to a unique person or intelligence.

## Minimal illustrative scenario

A buyer values an accurate forecast at 35 experimental sats; seller effort costs 11 and its posted price is 18. Honest delivery yields modeled joint surplus of 24 (35 minus 11); the transfer is not added twice. A plausible fake can save effort and transfer money while reducing delivered value. Verification, restitution and dispute costs follow explicit rules rather than magically creating or destroying funds.

These are scenario parameters, not empirical prices, welfare or field results. See [data contracts](17-data-contracts.md), [field design](03-experimental-design.md) and [metrics](09-metrics-and-analysis.md) for the distinction between synthetic truth and independently assessed real work.
