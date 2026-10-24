# 16 — Application-led backlog and dependencies

**This backlog supersedes the former AAE-001–023 simulator-first dependency chain.** Read [AGENTS](../AGENTS.md), the [unified charter]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}), [gates](11-stage-gates.md), [data contracts](17-data-contracts.md) and [handoff](18-agent-handoff.md). All work packages are planned, not completed. No package grants live authority.

## M0 — Shared kernel

**AA-001 — Domain and scope.** Select the narrow useful task category, record implementation-location/architecture decisions and build a small versioned domain package. Define mandate, contract revision, evidence, review, dispute, reservation and settlement objects. Keep optional network dependencies out of offline setup. Acceptance: canonical codec/signature-domain and invalid-record fixtures; explicit environment and policy versions; no secrets or research permission inferred from a field.

**AA-002 — Accounting and authorization.** Implement state validation, budget ceilings, beneficiaries, idempotence, unique reservations, ambiguity reconciliation, cancellation, appeals and refund rules. Acceptance: conservation/property tests; no double allocation or duplicate payout; stale revisions and forged authority rejected; a negative reputation score cannot spend escrow.

**AA-003 — End-to-end offline job.** Use the same intended application domain with mock identity, money and evidence adapters. Include successful delivery, disagreement, refusal, cancellation and outage recovery. Acceptance: deterministic replay, clear synthetic labels and prohibited cross-environment/oracle access. No large economic tournament is required.

## M1 — Qualify a narrow pilot workflow

**AA-004 — Worker and bounded agent interfaces.** Provide minimal listing, negotiation, consent/scope display, acceptance/refusal, private evidence, review and appeal. Agents use structured authorized actions, not wallet-admin or arbitrary CLI access. Acceptance: user can identify purpose, compensation, risk and dispute route; tests cover scope changes and unsafe instructions.

**AA-005 — Required identity and payment adapters.** Qualify local Python `archon-keymaster` with https://4tress.org under [12](12-archon-integration.md), Nostr transport and the chosen supported settlement construction. Mock ports are not live escrow. Pin local dependencies separately from observed server capabilities; retain local signing, read/write/payment separation and no auto-pay on 402. Acceptance: independent identity/receipt checks, required condition enforcement, recovery and no accidental production credentials. Only approved network/value scopes may execute.

**AA-006 — Pilot safety and measurement case.** Specify genuine demand, responsible sponsor, task limits, compensation, custody, exposure, consent, data handling, independent review, incident response and appropriate legal/security/ethics review. Prepare operator drills and minimal research/operational separation. Acceptance: required recovery works and a decision maker approves a specific pilot; absent approval remains a block.

## M2 — Useful paid task

**AA-007 — Run the separately approved pilot.** Complete a genuine low-risk task with informed participants, real effort, protected compensation, independent outcome check and verified settlement. Include bounded AI-requester feasibility with supervision disclosed. Acceptance: honest report of outcome/remedy, consent and scope evidence, fees/subsidy/manual involvement and limitations. Publish feasibility only; no invented causal conclusion or synthetic reputation history.

## M3 — Repeated operation and study qualification

**AA-008 — Measurement and independent audit.** Develop repeat opportunities and independent counterparties. Instrument eligibility, offers, refusals, accepted work, completion, settlement, costs, loss, disputed/unknown outcomes and newcomer access under the approved data policy. Acceptance: calibrated outcome audits, separated research permissions, documented subsidy and no self-validating reputation labels.

**AA-009 — Safe comparison design and registration.** Select a precise fixed-versus-history-sensitive policy contrast. Preserve a common protection floor and isolate unrelated factors. Choose assignment/exposure mapping, independent units, follow-up, primary outcomes, missingness and cluster-aware power/precision. Acceptance: independent review and prospective registration; if inadequate, remain descriptive rather than manufacturing certainty.

## M4 — Field comparison

**AA-010 — Versioned policy execution.** Implement only the approved prospective assignment and policy variants. Freeze terms at contract acceptance, log deviations and ensure safety stops do not depend on statistical success. Acceptance: no unprotected arm, undisclosed experimental term or retrospective change; repeat participants and spillovers recorded as specified.

**AA-011 — Independent analysis and publication.** Analyze all specified outcomes at the defensible unit; report selection, intention-to-treat where appropriate, costs, uncertainty, harm, null/adverse results and protocol deviations. Acceptance: independently reproducible safe extracts and analysis, findings at their actual evidence level, no payment authority in the analyst pipeline.

## M5 — Replication and later mechanisms

**AA-012 — Replicate and test portability.** Add independent evaluators/operators and approved task contexts; verify export/recovery/provider exit; evaluate true demand and full costs with subsidy disclosed. Optional studies of pooled collateral, sponsors, insurance, settlement alternatives and Bitcoin anchoring require their own reviewed assumptions and safe comparisons. Acceptance: reproducible bounded findings and documented limits, not a predetermined claim of superiority.

## Dependencies

`AA-001 → AA-002 → AA-003 → AA-004/005 → AA-006 → approval → AA-007 → AA-008/009 → approval → AA-010 → AA-011 → AA-012`.

Some interface/design work can proceed in parallel after shared contracts are stable. Required safety tests cannot be deferred, but full A–F simulator runs, all optional AT scenarios, anchoring comparisons, global collateral and sponsorship are not blanket prerequisites to AA-007. Use controlled fixtures specifically needed for its safety case and maintain broader research in parallel/later.

## Delivery contract

Each package needs a scoped issue/ADR with purpose, assumptions, files, tests, artifacts, permission dependencies, rollback/recovery and acceptance evidence. Preserve original sources, alternative hypotheses and negative findings. Do not change frozen outcomes or conceal subsidy to make the thesis win. The [evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) distinguishes published plans from executed code and field results.
