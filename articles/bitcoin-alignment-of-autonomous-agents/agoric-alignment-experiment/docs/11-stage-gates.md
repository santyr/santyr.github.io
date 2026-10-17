# 11 — Milestones S0–S6 and evidence-based promotion gates

Every stage has a working code deliverable, tests, empirical artifacts and a gate report. A coding agent may plan the next stage but must not silently execute a stage requiring new external permissions. Use [16 — Implementation backlog](16-implementation-backlog.md).

## S0 — Local reproducible skeleton (offline)

Deliver `pyproject.toml`, `src/agoric_alignment` with CLI, deterministic RNG, experiment-config loader and validation, JSONL event writers, schema checks, sample config, CI/test command docs and basic reporting. Demo: create two agents, post/accept/fund/deliver/settle one contract in simulated sats. Reject invalid state transitions; conservation holds; exact same seed/config/software gives byte-identical canonical output. **Gate:** tests green, README commands reproducible on another Linux machine; no network dependency. Prefer Python 3.12+ for eventual archon-keymaster integration, or keep that optional worker in a separate compatible environment.

## S1 — Core economy and agent baselines (offline)

Deliver 100-agent experiments with deterministic compute/forecast tasks, dynamic endowments, bid/offer market, budgets, scheduled events, reputation-free A and local-memory B arms, cooperative/opportunistic/newcomer strategies and oracle/evidence/belief separation. Fixtures: honest fulfillment, missed deadline, competent newcomer, incompetent incumbent, strategy endgame. **Gate:** 1,000+ contracts/run, no illicit oracle access, no negative balance or unexplained money creation, matched-arm seeded workload.

## S2 — Reputation and economic incentives (offline)

Add signed-endorsement C, private D and public-log E evidence visibility, independent evaluator interface, Bayesian baseline, false testimony and appeals, identity resets, collateral, policies conditioning on future reputational value. Deliver pilot seed matrix, effect-size variance, provisional parameter windows and frozen procedure for choosing confirmatory sample size. **Gate:** posterior calibration tests, E/B/C/D contrast reproducible, false allegations distinguishable from actual defaults, honest entrants retain access.

## S3 — Adversarial matrix and preregistration freeze (offline)

Implement all AT01–AT16 fixtures with permanent minimized regression traces and privacy/institutional capture measures. Prepare holdout seeds under digest and frozen config/software SHA. Produce machine-readable hypothesis/metric registry, confidence/multiplicity plan and preregistration commit. **Gate:** no known invariant violations, power plan approved, adversarial stress results labeled exploratory, owner approves freeze and/or adjustments before accessing holdouts.

## S4 — 4tress / archon-keymaster and independent verification (opt-in)

**S4a — Client interoperability:** pin the Python archon-keymaster client and use https://4tress.org as the selected remote node. A local full stack and JavaScript MCP are not prerequisites. Begin with approved, rate-limited reads; record readiness, registries, missing capabilities and independently observed server metadata. After separate write approval, use no more than the configured small synthetic identity/credential budget. Demonstrate local signing, explicit wallet isolation, create/resolve/rotate/revoke and correct claim-versus-truth handling. **Gate:** no secrets/oracle metadata leave the adapter, no implicit payments or unsupported registry fallback, public interaction stays within scope.

**S4b — Reconstructible evidence:** independently check issuer authority, historical signatures, content hashes/availability, revocation and retained evidence with the original client offline. Use an independently operated verifier or approved owned node; repeated requests to 4tress alone are not independent verification. **Gate:** independent reconstruction succeeds or incomplete/unknown evidence is accurately reported.

**S4c — Bitcoin and faults:** explicitly discover and request BTC:signet only when supported and approved. If absent, mark this part blocked rather than substituting mainnet or relabeling Hyperswarm. Verify actual anchor chain/network, batch membership, depth and reorg status. Compare with a matched transparency log. Run partitions, deliberate data loss, reorgs, adversarial signatures and load tests only in owned/local environments, never against 4tress. **Gate:** no false-finality/availability claims; receipts reconstructible, costs and assumptions explicit.

See [12 — selected interface](12-archon-integration.md). S4 completes only when its applicable verification and adversarial requirements pass; a successful hosted smoke test is not a proof of decentralization or alignment.

## S5 — Isolated payments and economic attestation (opt-in)

Connect sandbox LNbits, CLN and Archon mediator with bounded wallet identities; issue/verify BOLT11 invoices, L402 authorizations, simulate/payment receipt linking contract and DID, test replay/timeout/refund and closed channels. Keep payment-hash receipt proof separate from contractual outcome evidence. Every payment proposal goes through scoped external authorizer. The 4tress identity profile does not authorize or imply payment support. **Gate:** no unauthorized spending, no production configs or mainnet, replay evidence reproducible, all negative cases handled and teardown verified.

## S6 — Independent/heterogeneous evaluation (separately approved)

Bounded LLM-agent participants with logged model/version/prompts, structured actions, seeded task opportunities and strict token/monetary limits. Optional voluntary human study under separate ethics protocol; blinded substrate-label comparisons, matched capability histories and adverse event handling. Independent replication by a second agent/team; final report includes negative results, confounds, power and limitations. **Gate:** independent reviewer reruns specified fixtures, effect sizes and CIs reproduce, no overclaim of general AI safety.

## Gate report template

For each stage record (1) frozen requirements and version, (2) files changed, (3) exact commands/environment, (4) test results, (5) artifact hashes/run IDs, (6) scientific interpretation, (7) deviations, (8) unresolved risks, (9) next-stage decision/authorization. For S4 include the local package pin, profile hash, observed remote version or unknown status, registry, request counts and separate read/write/payment scope. A gate cannot be cleared solely by an agent claiming completion.

## Stop or change criteria

Leakage, inconsistent accounting, forged proof accepted, secret exposure, cross-run contamination or nondeterministic replay blocks promotion. Missing public-node capability is a documented block, not license to change scientific conditions. If confirmatory tests falsify the hypothesis, publish and continue diagnostic studies under a new preregistration; do not secretly redefine thresholds. Document scope changes and request approval instead of deleting baselines.
