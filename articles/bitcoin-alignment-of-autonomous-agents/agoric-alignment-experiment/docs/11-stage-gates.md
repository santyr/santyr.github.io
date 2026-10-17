# 11 — Milestones S0–S6 and evidence-based promotion gates

Every stage has a working code deliverable, tests, empirical artifacts and a gate report. A coding agent may plan the next stage but must not silently execute a stage requiring new external permissions. Use [16 — Implementation backlog](16-implementation-backlog.md).

## S0 — Local reproducible skeleton (offline)

Deliver `pyproject.toml`, `src/agoric_alignment` with CLI, deterministic RNG, experiment-config loader and validation, JSONL event writers, schema checks, sample config, CI/test command docs and basic reporting. Demo: create two agents, post/accept/fund/deliver/settle one contract in simulated sats. Reject invalid state transitions; conservation holds; exact same seed/config/software gives byte-identical canonical output. **Gate:** tests green, README commands reproducible on another Linux machine; no network dependency.

## S1 — Core economy and agent baselines (offline)

Deliver 100-agent experiments with deterministic compute/forecast tasks, dynamic endowments, bid/offer market, budgets, scheduled events, reputation-free A and local-memory B arms, cooperative/opportunistic/newcomer strategies and oracle/evidence/belief separation. Fixtures: honest fulfillment, missed deadline, competent newcomer, incompetent incumbent, strategy endgame. **Gate:** 1,000+ contracts/run, no illicit oracle access, no negative balance or unexplained money creation, matched-arm seeded workload.

## S2 — Reputation and economic incentives (offline)

Add signed-endorsement C, private D and public-log E evidence visibility, independent evaluator interface, Bayesian baseline, false testimony and appeals, identity resets, collateral, policies conditioning on future reputational value. Deliver pilot seed matrix, effect-size variance, provisional parameter windows and frozen procedure for choosing confirmatory sample size. **Gate:** posterior calibration tests, E/B/C/D contrast reproducible, false allegations distinguishable from actual defaults, honest entrants retain access.

## S3 — Adversarial matrix and preregistration freeze (offline)

Implement all AT01–AT16 fixtures with permanent minimized regression traces and privacy/institutional capture measures. Prepare holdout seeds under digest and frozen config/software SHA. Produce machine-readable hypothesis/metric registry, confidence/multiplicity plan and preregistration commit. **Gate:** no known invariant violations, power plan approved, adversarial stress results labeled exploratory, owner approves freeze and/or adjustments before accessing holdouts.

## S4 — Archon and Bitcoin verification adapters (opt-in)

Pin upstream Archon commit SHA, run isolated Keymaster/Gatekeeper/IPFS, verify DID creation/update/key rotation/credential/revocation, multiple independent resolvers and historical state. First run local/mock anchor, then disposable Bitcoin signet only when explicitly approved; test missing data and reorg. Compare signature/anchor availability with non-Bitcoin transparency log using equivalent evidence, rate, retention and cost. **Gate:** no secret disclosure, no production systems, independent reconstruction after origin node disappears, no false-finality labels.

## S5 — Isolated payments and economic attestation (opt-in)

Connect sandbox LNbits, CLN and Archon mediator with bounded wallet identities; issue/verify BOLT11 invoices, L402 authorizations, simulate/payment receipt linking contract and DID, test replay/timeout/refund and closed channels. Keep payment-hash receipt proof separate from contractual outcome evidence. Every payment proposal goes through scoped external authorizer. **Gate:** no unauthorized spending, no default production configs or mainnet, replay evidence reproducible, all negative cases handled and teardown verified.

## S6 — Independent/heterogeneous evaluation (separately approved)

Bounded LLM-agent participants with logged model/version/prompts, structured actions, seeded task opportunities and strict token/monetary limits. Optional voluntary human study under separate ethics protocol; blinded substrate-label comparisons, matched capability histories and adverse event handling. Independent replication by a second agent/team; final report includes negative results, confounds, power and limitations. **Gate:** independent reviewer reruns specified fixtures, effect sizes and CIs reproduce, no overclaim of general AI safety.

## Gate report template

For each stage record (1) frozen requirements and version, (2) files changed, (3) exact commands and environment, (4) tests with pass/fail count, (5) artifact hashes and sample run IDs, (6) scientific interpretation, (7) deviations, (8) unresolved risks, (9) next stage decision and explicit authorization. A gate cannot be cleared solely by an agent claiming work is complete.

## Stop or change criteria

Unexpected leakage, inconsistent accounting, forged proof accepted, secret exposure, cross-run contamination or nondeterministic replay blocks stage promotion. If confirmatory tests falsify the hypothesis, publish and continue diagnostic studies under new preregistration; do not secretly redefine thresholds. If integration scope grows, document ADR and request approval instead of deleting baselines.
