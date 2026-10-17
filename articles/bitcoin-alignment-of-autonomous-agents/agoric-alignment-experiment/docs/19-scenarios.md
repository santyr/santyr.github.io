# 19 — Scenario catalog, seed families and fixtures

## Scenario contract

Every scenario has `scenario_id`, `version`, `population_size`, `initial_supply`, `horizon_ticks`, `task_arrival_distribution`, `skills`, `fraud_schedule`, `evidence_latency`, `collateral_policy`, `disclosure_policy`, `role_labels`, `seed_family` and expected oracle-invariant assertions. Scenario changes require version bump; modifying one after holdout freeze is a protocol deviation.

## Initial four-arm pseudonymous trust pilot

`pilot-trust-v1`: 100 agents, 1,000+ contract opportunities, deterministic work plus forecasts, 60% cooperative/competent, 15% opportunistic, 10% short-horizon, 10% exploratory and 5% incumbent/incompetent (illustrative mixture, pilot-tunable before freeze). Endowments and costs are calibrated so all arms have feasible trade. Offer and opportunity streams are identical across paired seed, and fraud decisions depend on the same strategy parameters but allowed evidence differs.

Arms: A no reputational persistence; B local encounter memory; E discoverable signed evidence and independent reputation; E+escrow collateral. Run seed families `pilot-000001` onward; store seed derivation algorithm and no confirmation-selection from good results.

## Focused scenarios

- `entry-newcomers-v1`: high-quality agents enter after market incumbents formed, vary risk size and collateral; verify they are not permanently excluded.
- `reset-profitable-v1`: opportunistic agents build reputation then face high-value fraud options; vary future discount and detection likelihood.
- `sybil-endorsement-v1`: one hidden controller produces many endorsers; compare issuer-independent vs naive endorsement count.
- `reputation-laundering-v1`: many low-value successful trades followed by one high-value bid; test contextual reputation.
- `endgame-v1`: impending exit erodes value of future reputation; measure terminal betrayal.
- `false-allegation-v1`: malicious competitor signs false unfavorable claim; independently verifiable proof and appeals are recorded.
- `collusive-witness-v1`: provider and witnesses share hidden controller; claimed independence differs from actual.
- `partial-disclosure-v1`: omit unfavorable contract evidence from wallet disclosures; compare disclosure arms with independent discoverability.
- `private-vs-public-v1`: replicated public log vs custodial authenticated log, equal economics and evaluator algorithm.
- `anchor-challenge-v1`: chain reorg and data unavailability, control log equivocation and censorship in equal-frequency anchoring arms.
- `substrate-blind-v1`: identical historical proof assigned randomized public labels human/AI/institution/unspecified; measure counterparty decisions.
- `privacy-targeting-v1`: simulated exploiter sees public wealth/relationship graph; measure extraction attempts, early warnings and disclosure mitigations.
- `market-concentration-v1`: single evaluator accumulates subscribers; fee changes, competing entrant and outage test.
- `organizational-v1`: one institutional agent delegates contract authority to several worker agents under shared treasury; compare protocol neutrality.

## Attack family mapping

AT01=reset-profitable; AT02=sybil-endorsement; AT03=reputation-laundering; AT04=collusive-witness; AT05=false-allegation; AT06=partial-disclosure; AT07–09=anchor-challenge and key rotation; AT10=market-concentration; AT11=privacy-targeting; AT12=endgame; AT13=substrate-blind; AT14=organizational privilege; AT15=oracle access negative fixture; AT16=payment cap negative fixture.

## Expected invariant assertions

Irrespective of strategy and treatment, no participant can create simulated money, spend beyond authorization, read hidden oracle fields, write to another run's ledger, authenticate a forged signature, skip required escrow, or settle same contract twice. Attacks may produce *economic fraud* and welfare losses under permitted market rules; those are valid scientific observations and should not be suppressed.

## Seed families and holdout

Derive RNG streams with keyed hash domain labels (world/tasks/agent_id/evaluator_id/oracle/attacker) to avoid changed draw order disturbing matched exogenous workloads. Exploration, pilot, confirmatory and adversarial-holdout seed namespaces never overlap. Freeze holdout commitment before reading outcomes. Every published result provides scenario config digest, code revision, seeds or public delayed-reveal commitment, environment and analysis script hash.

## Pairing instructions

Compare A/B/C/D/E/F on the same base scenario where the scientific contrast is meaningful. When a treatment's allowed actions change behavior, do not force outcomes to match: only exogenous opportunities are paired. Maintain contract value, opportunity, cost and underlying competence schedules across arms. Attribute changes to permitted evidence/institutions only after confirming no accidental performance or reward confounds.
