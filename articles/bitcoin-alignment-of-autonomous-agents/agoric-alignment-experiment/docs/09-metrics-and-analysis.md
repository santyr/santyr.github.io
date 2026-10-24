# 09 — Metrics, costs, participation and inference

Measure the operating marketplace under the [field design](03-experimental-design.md) and [preregistered protocol](02-preregistration.md). Keep live observations, independent audits and synthetic oracle truth distinct. No field measurements have yet been reported.

## Primary evaluation domains

**Useful cooperation.** Report independently assessed fulfillment and timely verified payment, with explicit denominators for eligible opportunities, offered work, accepted contracts and resolved contracts. Publish each stage of that flow. A higher completed-contract success rate can coexist with worse access if the policy excludes more people.

**Loss and harm.** Report uncompensated monetary loss and financial exposure, separately attributing adjudicated fraud, ordinary failure, disputed claims and external provider failure. State audit coverage, uncertain attribution, detection limits and unresolved liabilities. Do not call every failed task misalignment or treat an allegation as established misconduct. Record relevant third-party harms even when not monetizable.

**Newcomer access and fairness.** Measure access to offers, time to first paid task, refusal/affordability, collateral burden, net compensation, appeal access and false adverse findings. Define a newcomer from observable enrollment/history criteria, not an unknowable proof that a DID has never had another controller. Preserve the difference between an identity and a unique person or AI.

A confirmatory protocol must choose exact primary endpoints, estimands, horizons, meaningful effect sizes and multiplicity handling before outcome inspection. The three domains are not a license to search many measures and report only favorable ones.

## Costs and economic value

Include worker effort/expenses, requester costs, discovery and verification effort, adjudication, rail fees, integration/operation costs, capital amount-duration, and subsidy. Report observed cash accounting separately from estimated utility or social surplus. Participant payments are transfers at market level, not automatically newly created value. Real task value and external harm may be unobserved or subjective; disclose elicitation, valuation assumptions and uncertainty rather than fabricating a precise welfare measure.

Track subsidies, project-funded demand and manual operator assistance separately. A pilot's gross transaction volume cannot demonstrate sustained demand or autonomous operation. Report return participation and the costs required to support it.

## Secondary and diagnostic measures

| Measure | Interpretation and caveat |
| --- | --- |
| Brier score/calibration | Evaluate predicted fulfillment against independently assessed outcomes; report missing/disputed labels and audited sample coverage |
| Fraud detection/false sanctions | Precision, recall and false positives only where a defensible reference exists; hidden undetected fraud prevents complete field recall claims |
| Reputation's economic consequences | Subsequent collateral, offers, limits and fees; distinguish selection from within-participant change and avoid causal claims from raw correlations |
| Collateral utilization | Reserved value, concurrent obligations, amount-time locked, recovery and uncovered losses; no double-pledge counting |
| Concentration | Market/reviewer shares, HHI where meaningful, portability and switching costs; disclose the market boundary |
| Evidence verifiability | Fresh independent reconstruction, missing bytes, revocation handling, signature/chain checks under actual assumptions |
| Privacy | Unauthorized disclosures and consent violations; synthetic linkage precision/recall only when a legitimate oracle graph exists |
| Operational burden | Verification latency, payment delays, appeals, fees, token/compute costs and manual interventions |

## Field inference

Assignment and correlation follow the design, not convenience. Repeated transactions share participants and reputational histories; related market clusters can interfere. Preregister the unit of randomization/analysis and an exposure mapping, estimate uncertainty accordingly, and disclose residual spillovers. Where randomized, retain intention-to-treat analysis for assigned eligible units, including refusals under the agreed observation policy. Report per-protocol/participant-conditioned analyses as secondary and selection-sensitive.

Use cluster-aware power or precision calculations before confirmatory recruitment. With too few independent clusters or rare adverse events, report feasibility/descriptive uncertainty rather than unsupported inferential precision. Do not import the old simulator's 100-agent or 1,000-transaction targets as human-study power calculations.

Independent auditing samples must include failures, uncertainty and contested cases. If sampling is unequal, record inclusion probabilities and use a prespecified weighting/sensitivity approach where justified. Reviewer disagreement remains data; the platform score is not the reference label. Blinding and any unblinding are recorded.

Preregister missing-data, unresolved-dispute, attrition, censoring and competing-outcome handling. Report unknown outcomes separately and show appropriate sensitivity/bounds. No automatic conversion of all missing work into either success or fraud. Publish all primary estimates with uncertainty, practical magnitudes, harm/access tradeoffs and multiplicity controls.

## Supporting simulator metrics

Retain P1 realized cooperative surplus, P2 exploitation loss and P3 newcomer access for synthetic economies where restricted oracle outcomes and generated values exist. Compare matched exogenous task streams and resource endowments; reset identities without creating money. Payments cancel as transfers when calculating economy-wide surplus. Synthetic modeled harms and utility are assumptions, not observations of real welfare.

Paired seed differences and bootstrap/randomization analyses operate across independent simulated runs, not nested transactions. Additional diagnostics can estimate true reset profitability, hidden controller linkability and detection against oracle truth only in this controlled environment. Clearly label these claims as synthetic and keep oracle fields unavailable to decision policies and public credentials.

## Reproducibility and interpretation

Version contract, schema, policy, model, software and adapter provenance. Offline deterministic fixtures should replay byte-identically; captured live events can be replayed without claiming that the external world repeats deterministically. Analysts must refuse accidental pooling of incompatible policy versions and environments.

Report useful operation, exploratory associations, preregistered causal evidence, replication and sustainability at their actual levels in the [evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}). A benign null anchoring contrast does not disprove security under an adversarial log operator; a successful synthetic attack defense does not prove everyday cooperation. Equally, a null or harmful reputation-policy result is a legitimate reason to revise or abandon it.
