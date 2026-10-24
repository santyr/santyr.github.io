# 11 — M0–M5: application-led delivery and evidence gates

**Controlling sequence, revised October 24, 2026. All gates are pending.** The former S0–S6 simulator-first sequence is superseded. Historical labels and documents are not evidence of completion or approval. The [unified charter]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}), [AGENTS](../AGENTS.md) and [backlog](16-implementation-backlog.md) govern the one marketplace program.

## M0 — Shared contract kernel and offline vertical slice

Implement one genuine-task-shaped workflow in the intended application domain: sponsor mandate, listing/offer, signed versioned agreement, isolated simulated funding, evidence, review, payment/refund and outcome attestation. Use explicit environment boundaries and deterministic replay. Reject unapproved action, stale revisions, duplicate settlement, double allocation, forged authority and accidental oracle/public-data mixing.

**Gate:** reproducible tests demonstrate conservation, idempotence, refusal/cancellation, dispute and recovery behavior for the narrow workflow. The sandbox and proposed live ports use the same transition/accounting implementation. No external network, funds or personal credentials are needed. A complete 100-agent economy, A–F tournament or sophisticated evaluator is not required.

## M1 — Qualify the narrow real-work pilot

Build the minimal worker interface and bounded agent interface around that kernel. Qualify actual required identity, evidence, signing and payment adapters under explicitly scoped permissions. Preserve local-keymaster/4tress constraints and independent credential verification. A mock funding check must never be displayed as live escrow. Cashu preference does not waive enforcement, redemption, custody or recovery requirements.

Choose a genuinely needed, low-risk task and a responsible sponsor. Document task admissibility, exact permitted action, participants, contract/acceptance policy, worker compensation and expenses, custody and permitted beneficiaries, individual/aggregate exposure, maximum pending duration, incident contacts, consent, retention, independent review and dispute/appeal. Obtain appropriate legal/security/ethics review for the actual pilot; this specification cannot supply it.

**Gate:** relevant failure/recovery drills pass, required evidence can be independently reconstructed, no production-wallet access or secret leakage exists, participants can understand/refuse terms, and an authorized decision maker approves the specific pilot scope. Missing safe settlement, recovery or consent is a block. Publication, a passing sandbox or an available mint is not pilot approval.

Optional Bitcoin-anchoring research, global pooled collateral, sponsorship/insurance and large strategic tournaments are not all M1 requirements. Qualify only what the narrow safety case actually depends on, without omitting required controls.

## M2 — First genuine useful paid task

After separate permission for participants and real value, execute a small task someone actually needs. The requester operates within a sponsor mandate; the human provider can negotiate and decline; evidence is independently reviewed; actual funding and settlement are verified; an attributed outcome record follows. A bounded AI requester should be represented in the early feasibility program, with supervision disclosed.

**Gate:** the accepted task produced a useful verified result and fair payment, or the report honestly documents failure and remedy. Retain consent, scope, incident and rail evidence privately; publish only appropriate aggregates and provenance. Declare subsidy, project-origin demand, manual assistance and whether actions were automated. A failed pilot is a finding to investigate, not a reason to fabricate completion.

**Claim limit:** operational feasibility under stated conditions. No causal proof of reputation's effect, durable market demand or general AI alignment.

## M3 — Repeated activity and measurement qualification

Develop repeat opportunities and independent counterparties without manufacturing work histories. Measure the recruitment/eligibility/offer/refusal/acceptance/completion/settlement flow, compensation, loss, disputes, affordability, newcomer access, operator cost and subsidy. Establish task-specific independent audit procedures and calibration, including uncertain and adverse outcomes.

Define a feasible safe policy comparison, assignment/exposure map, follow-up, sample and cluster-aware power or precision rationale, outcomes and analysis. Freeze a confirmatory registration before the relevant data are inspected. If independent units are too few or evidence unreliable, stay with exploratory/descriptive findings rather than lowering evidentiary standards.

**Gate:** measurement is credible, permissions and privacy are reviewed, the proposed comparison is independently scrutinized, and registration/analysis plans are approved. Genuine participation rather than staged wash trades supports the study population.

## M4 — Approved field comparison

Compare fixed and history-sensitive terms, or another specifically approved contrast, inside the same application. Retain the protection floor in every arm and keep unrelated factors comparable. Account for repeat identities, shared counterparties, carryover, selection and spillovers. Assignment, policy versions and consent remain auditable; frozen terms cannot be changed retroactively.

**Gate:** independent analysis reports every specified outcome, uncertainty, inclusion and exclusion, attrition, unresolved cases, harm, costs, subsidy, deviations and limitations. Show intention-to-treat and selection-sensitive analyses as appropriate. Pause unsafe variants and disclose any design break. Report null/adverse findings as fully as improvements.

**Claim limit:** bounded causal evidence only if the actual design and execution support it. A dashboard, large transaction count or internal reputation score is insufficient.

## M5 — Replication, portability and sustainability

Seek replication across independent evaluators/operators and additional approved task contexts. Test identity/evidence export, key recovery and provider exit without synthetic reputation contamination. Compare full operating costs and subsidies with genuine repeat demand. Qualified later work can examine sponsorship, pooled reservation schemes, alternative settlement or Bitcoin anchoring without declaring them necessary conclusions.

**Gate:** independently reproducible artifacts, context-specific findings, documented failure limits and honest sustainability analysis. Do not generalize beyond the evidence or erase unsuccessful replications.

## Permission model and stop rules

Every stage report records requirements, software/schema/policy revisions, files, executed commands/tests, artifacts, actual observations, limitations, incidents, approvals and the next blocked action. Permissions are scoped capabilities, not inherited from an earlier stage number. Remote reads do not authorize writes; identity writes do not authorize money; payment tests do not authorize recruitment or experimentation.

Stop new commitments on accounting corruption, duplicate payment, forged authority, consent/privacy failure, unsafe tasks or material unexpected harm. Preserve earned pay and existing claims during containment. Missing upstream capabilities block the relevant function; no silent host/chain/mint substitution or production credential reuse. A safety amendment requires transparent requalification and treatment of affected research data.

The [evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) must separate publication, software tests, feasibility, exploratory activity, causal evidence, replication and sustainable operation. A gate is not passed by an agent asserting success.
