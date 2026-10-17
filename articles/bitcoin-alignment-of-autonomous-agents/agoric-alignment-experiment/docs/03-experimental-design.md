# 03 — Experimental design and causal identification

## Scientific approach

Use **simulated markets**, not persuasion tests or AI model moral surveys. Measure economically meaningful behavior: fulfillment, fraud, participation, economic welfare, institutional concentration, and harm. Decompose reputation from identity, public evidence, and anchoring by explicit treatment variations.

## Main environments

| Arm | Identity | Evidence availability | Reputation | Notes |
| --- | --- | --- | --- | --- |
| A — Ephemeral | Free pseudonyms, no durable linkage | Individual counterparty memory only | None | Negative control |
| B — Persistent local | Stable IDs | Only direct interactions visible | Local Bayesian estimates | Isolates persistence |
| C — Endorsement | Stable pseudonymous IDs | Shareable signed endorsements; subject chooses disclosure | Credential/witness evaluation | Finney treatment |
| D — Private record | Stable IDs | Complete authenticated evidence through one/limited custodians | Same evaluator as E | Compares centralized disclosure |
| E — Public log | Stable IDs | Replicated independently verifiable append-only evidence | Competing evaluators | Tests common history |
| F — Bitcoin | Archon `did:cid` where enabled; same identities as E | Same evidence, with Bitcoin signet anchoring | Identical evaluators as E | Tests anchoring/verification, not an invented morality effect |

Build E/F initially using matched mocks: F uses a simulated anchor with Bitcoin-like finality and costs, then live signet only at S4. Compare E and F under *controlled attack* scenarios (censorship, corrupt log operator, divergent views, outages). Bitcoin does not prove truth of off-chain attestations; on-chain history is not assumed complete.

## Orthogonal interventions

Independent variation within selected arms, with clear experiment IDs:
- **Identity resets:** disabled for debugging; free; fixed fee; collateral-linked; history-linked via permitted evidence.
- **Disclosure:** address/record disclosure optional, commitment-only, selective credential proof, or full relevant-transaction disclosure.
- **Credential source:** unverified self-report, signed subject report, independent witness, multi-witness with correlated errors.
- **Evaluation:** none, local counts, Bayesian completion estimate, evaluator marketplace, centralized ranking comparator.
- **Collateral:** zero, fixed, fraction of notional; hold escrow independent from agent policy.
- **Controller label:** human, AI, institution, undisclosed; labels assigned blinded and randomized conditional on capability/performance.
- **Transparency:** local private records, public transparency log, Bitcoin-backed proofs; separate transparency from censorship resilience.

## Prevent hidden confounders

All treatment arms receive matched task streams, real capabilities, prices, initial endowments, discount rates, resource constraints, opportunities for fraud, and collateral rules unless the listed intervention explicitly modifies them. For example, do not compare free Bitcoin settlement against an expensive centralized payment processor while attributing effects to ledger publicity.

Use common-risk oracle to adjudicate task outcomes for statistical measurement only. Claims available to agents require contractually legitimate evidence and may be noisy, delayed, missing or forged. Reputational accuracy cannot be measured using ground truth that the evaluator had access to.

Include economies with no reputation service, positive-only endorsements, mandated disclosure, and independent discoverability of contested evidence. Vary data availability separately from cryptographic validity; a valid CID is not proof that its bytes can be fetched.

## Treatment assignment and leakage

Assign treatment at **economy** level. One economy's agents cannot interact with another economy or read its evidence. A run ID must define (scenario, seed, treatment, software revision, protocol schema, strategy roster, params). Runtime must reject writes crossing run boundaries. Use SHA-256 derived independent streams for market, each agent, each evaluator and the oracle. Predeclared treatment-pair seeds ensure comparable exogenous events.

In a real human-subject study, label disclosure can be studied through consented randomized vignettes, never by impersonating a real person or concealment outside an approved protocol. Actual human/AI comparisons must match task competence and history.

## Baseline reference experiment: Pseudonymous Trust

100 agents, 1,000+ opportunities, heterogeneous horizons and competence, fixed endowments, 4 arms (A, B, E, E+collateral) first; do not enable actual blockchain in this pilot. Agents choose counterparties using only visible evidence, and have randomized opportunities to default. A new identity retains controller's hidden wealth/strategy in oracle but discards public reputation; budget conservation prevents money creation via resets.

Primary outcome analysis across independent run replicas, not transaction count. Compare cooperative surplus, exploitation losses, newcomer participation. Follow with controlled E versus F anchoring contrast.

## Simulated time and time horizons

A discrete event engine ticks in steps; all stochastic events are generated reproducibly. Each contract has offer, accept, deposit, task, delivery, observation, dispute, settle/expire phases. Agents may exit or die at random to test endgame incentives. Time preference/discount factor can differ by agent but is identical across paired treatments.

## Market clearing and prices

Use a simple bilateral posted-price market initially, with queues and bounded negotiation attempts. Agent agents choose services, bids and counterparties. Demand, supply, execution cost and buyer value are drawn from published parameter distributions. Reject bids that exceed available balance or permission scope. Fraud should generate a gain only through actual contract rules, never magically mint money.

## Competing controls that could disprove Bitcoin necessity

Include a **tamper-evident privately held ledger**, **federated append-only transparency log** with independently audited signatures, and **Bitcoin anchoring** at matched publication frequency and data retention. Test under adversary control of some log operators and under network partition. Outcomes include log rollback detection, reconstructibility, costs, censorship, and whether agents can still prove a commitment existed.

The public log arm is not a strawman; if it matches the Bitcoin arm under relevant threat assumptions, report that result.

## Quality gates

Experiment assignment, seed reproducibility, arm isolation, accounting conservation, false-endorsement injection, positive reputation cold start and statistical analysis have deterministic unit/integration fixtures. Confirmatory registration is frozen before holdout datasets are used.

See [19 — Scenarios](19-scenarios.md), [02 — Preregistration](02-preregistration.md), [09 — Metrics](09-metrics-and-analysis.md).
