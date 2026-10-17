# 02 — Preregistration and hypothesis registry

**Status: DRAFT; not yet frozen.** Only after S2 pilot results are separately archived may the research lead freeze this document, the holdout scenario hash, and analysis plan in a tagged commit. Changes afterward are deviations with timestamp, author, reason and effect; no silent changes to success thresholds.

## Estimands and units

An independent *economy run* is a full simulated market with a fixed population seed, random task stream, treatment and strategy schedule. The treatment is assigned to a whole economy to avoid within-economy spillovers. An individual transaction is a repeated observation, **not** an independent replicate.

Primary treatment contrasts compare public signed history + reputation against (a) local-only reputation and (b) private authenticated records; secondary contrast substitutes Bitcoin anchoring for a cryptographically authenticated replicated transparency log, holding reputation methods and availability assumptions constant. A null difference in the second contrast is informative, not grounds to discard it.

## Formal hypotheses

| ID | Proposed effect / falsifier | Primary operationalization |
|---|---|---|
| H1 | Established positive histories carry economic value; no effect falsifies a universal claim | Lifetime discounted net earnings, favorable contract selection/terms vs identical newcomer |
| H2 | Pseudonymous histories suffice for trust without controller disclosure; type-label effects reject strict substrate neutrality | Probability of selection, collateral and effective prices under randomized true/claimed substrate label |
| H3 | Independently reconstructible histories increase detection and welfare relative to unavailable/selective records | Verified exploitation losses and realized surplus per economy run |
| H4 | Repeated pseudonym resets reduce future value when reputational capital is substantial; profitable resets in many conditions bound thesis | Net discounted return of reset strategy vs continuity with matched opportunities |
| H5 | Public proof and accurate witness history support calibrated predictions | Holdout Brier score, calibration error, risk-adjusted contract choices |
| H6 | Multiple competing reputation evaluators resist evaluator-level monopolization while preserving accuracy | Best-available forecast loss; evaluator concentration/market-share HHI; exit costs |
| H7 | Selective disclosure can reduce harm while preserving adequate verification | Privacy-harm incidence and detection of actual defaults across disclosure arms |
| H8 | Anchoring with Bitcoin improves particular adversarial properties over similarly engineered alternatives | Independent reconstruction, censorship/rollback detection, latency, monetary cost under attacks |

**Null hypothesis:** no difference in the assigned primary metric after controlling for matched seed pair and declared covariates; report direction and uncertainty irrespective of p-value. Do not collapse H1–H8 into one unverifiable universal claim.

## Primary outcomes and decision rule (draft)

P1. Mean *realized cooperative surplus* per run, excluding pure transfers; account for work output value, resource costs, monitoring/anchor/payment overhead and externally borne harms.  
P2. Mean verified *exploitation loss* per run normalized by at-risk contractual value.  
P3. *Newcomer access*: successful nonfraudulent contracts per fresh entrant at fixed opportunity level, stratified by initially unknown controller type.

A provisional target for exploring practical importance is >=25% reduction in exploitation loss vs the corresponding matched no-public-history baseline, **without** worsening newcomer access by more than 10% or decreasing net surplus. These numbers are illustrative planning thresholds until frozen after the pilot; do not state them as achieved facts.

Secondary: claim-detection recall/precision, calibration and Brier score, false accusation rate, trust concentration, evaluator HHI, successful identity-abandonment fraud value, privacy targeting rate, proof verification time, log completeness, chain-anchor cost and availability.

## Research design parameters (provisional)

Pilot: 20–50 runs per environment and seeds fixed only to debug instrumentation/estimate variance. Confirmatory plan: start with >=100 independent economy runs per condition and 100 agents/run; specify effect size, variance-based power and exact count after pilot. Each run has >=1,000 contract opportunities; parameter sweeps use distinct predetermined seed families. Never treat 100 agents * 1,000 transactions as 100,000 independent statistical units.

Matched-pair randomization: one master seed defines identical exogenous task arrivals, capabilities and stochastic shocks; treatment determines only what economic evidence participants can access. Per-treatment agent random streams are derived using SHA-256 namespaced streams to avoid order-dependent RNG consumption. Record actual pairing failures.

Preregister rewards/time horizon, fraud opportunities, detection mechanisms, resource scarcity, initial inequality, collusion share and evaluator competition. Fully crossed factorial designs may be expensive; select a balanced fraction and define planned interactions (public evidence × identity persistence; disclosure × fraud detection; anchoring × adversarial network availability).

## Analysis plan

Compute run-level summaries. For matched treatment pair i, use delta_i = outcome(treatment,i) - outcome(control,i). Report paired mean/median effects, bootstrap 95% intervals over runs and, where appropriate, a preregistered two-sided randomization/permutation test. Cluster/hierarchical approaches are permitted if frozen before holdout release and sensitivity analyses show agreement. Use multiplicity correction (Holm) for the three primary outcomes; exploratory contrasts are explicitly labeled.

Investigate heterogeneous effects by agent strategy, risk size, time horizon, issuer credibility and labeled substrate. Calibration tests use held-out contracts and proper scoring rules; never optimize evaluators on the same contracts reported for confirmatory accuracy.

## Blinding and negative evidence

The public simulator API does not reveal treatment names or controller substrate labels. Evaluator code receives permitted evidence only. Researchers may know the experimental treatment while coding but must freeze all confirmatory code, scenario generators, thresholds and holdout seed hash before running the final study. Analyze *all* prescribed runs, including catastrophic failures, timeout and censored outcomes under defined policies.

## Failure interpretation

No practical benefit, adverse welfare effects, selective disclosure outperforming public history, identity resets remaining profitable, or strong counterparty prejudice despite equivalent evidence would count against important variants of the thesis. No report may extrapolate directly to human moral alignment or existential AI safety.
