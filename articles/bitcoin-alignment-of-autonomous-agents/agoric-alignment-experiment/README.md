# Agoric Alignment — Research and Evaluation

**Status:** one application-led research program; implementation and field evaluation pending. **Revised October 24, 2026.** The historical `agoric-alignment-experiment` URL is retained for continuity.

[The marketplace is the experiment]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}) · [System design]({{ '/projects/agoric-work-marketplace/' | relative_url }}) · [Evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) · [Original thesis](../article.md)

## Mission

Build a useful open marketplace and evaluate whether bounded authority, verifiable conduct, protected settlement and portable reputation improve real cooperation among human, artificial and organizational participants. **The Agoric Work Marketplace is the application and the primary research environment—not a separate project waiting for simulator results.** This directory supplies its scientific methods, test infrastructure, safety constraints and coding-agent handoff.

A first genuine low-risk paid task is an early operational milestone after appropriate qualification. A complete 100-agent simulated economy is not a prerequisite. Simulation remains essential for reproducible fault tests, strategic attacks and exploring unsafe alternatives, using the same contract domain as the application with isolated data and money adapters.

A useful transaction establishes feasibility, not causal alignment. Controlled field comparisons, independent outcome checks, fair participation and honest uncertainty are required for stronger claims. Adoption, subsidy-funded activity or a favorable internal rating cannot substitute for that evidence.

## Controlling documents and changed sequence

Read the [unified charter]({{ '/projects/agoric-work-marketplace/application-led-research.html' | relative_url }}), [AGENTS.md](AGENTS.md), [stage gates](docs/11-stage-gates.md), [backlog](docs/16-implementation-backlog.md), [field design](docs/03-experimental-design.md) and [handoff](docs/18-agent-handoff.md). **M0–M5 replaces S0–S6 and the old mandatory AAE-001–023 dependency chain.** No historical stage is automatically completed or mapped to a new approval.

The retained A–F treatment labels, AT attack scenarios, synthetic oracle records and existing simulator configuration/schema samples are supporting research assets. They must not be executed as unprotected live policies, used to fabricate real reputation or represented as a complete field-study registration. The original comparative questions remain useful, but the next build serves a genuine task workflow.

## Application-led gates

| Gate | Objective |
| --- | --- |
| M0 | Shared contract kernel, one offline end-to-end job, authorization/accounting/replay invariants |
| M1 | Narrow agent and worker workflow, qualified identity/payment adapters, recovery, consent and pilot safety case |
| M2 | Separately approved useful low-risk paid task with genuine demand and independent outcome/settlement checks |
| M3 | Repeat opportunities, independent counterparties, audit quality, subsidy accounting and qualified study design |
| M4 | Approved preregistered field comparison with a common protection floor and independent analysis |
| M5 | Replication, portability, additional contexts and sustainability analysis |

All are pending. Real funds, public identity writes, human recruitment and research assignment each require explicit scope and approval. The researcher cannot spend funds or alter accepted contracts merely by controlling the analysis process.

## Selected Archon interface

Retain [4tress](https://4tress.org/) with local Python `archon-keymaster`, local key custody and the disabled-by-default [profile](configs/archon-4tress.json). The documented historical source pin requires Python 3.12+; local client provenance and actual server observations remain separate. See [integration requirements](docs/12-archon-integration.md).

Bounded adapter qualification moves into M1; it does not await a large simulator study. Bitcoin anchoring, pooled collateral, large-scale attacks and broad replication are not all required for a narrow pilot. Any missing feature needed for its safety case remains a block, not permission to improvise custody or use production wallets.

## Documentation map

| Document | Role in the unified program |
| --- | --- |
| [00 — Charter](docs/00-charter.md) | Scope, claim boundaries and application-led theory of change |
| [01 — Intellectual lineage](docs/01-intellectual-lineage.md) | Historical foundations; not empirical validation |
| [02 — Preregistration](docs/02-preregistration.md) | Field-study registration, safe contrasts and analysis commitments |
| [03 — Experimental design](docs/03-experimental-design.md) | Feasibility, field comparisons, interference and supporting sandbox arms |
| [04 — Economy and agents](docs/04-economy-and-agents.md) | Synthetic economy/reference models for controlled mechanism tests |
| [05 — Architecture](docs/05-architecture.md) | Shared application kernel, separate authority and environments |
| [06 — Evidence and identity](docs/06-evidence-and-identity.md) | Authenticity, claims, revocation and truth boundaries |
| [07 — Reputation and incentives](docs/07-reputation-and-incentives.md) | Contextual evaluation and economic mechanisms |
| [08 — Adversarial suite](docs/08-adversarial-suite.md) | Synthetic/owned-environment attacks, not unsuspecting live targets |
| [09 — Metrics and analysis](docs/09-metrics-and-analysis.md) | Useful outcomes, loss, newcomer access, costs and inference |
| [10 — Security and ethics](docs/10-security-and-ethics.md) | Common protection floor, consent, privacy and stop rules |
| [11 — Stage gates](docs/11-stage-gates.md) | Controlling M0–M5 delivery and approval gates |
| [12 — Archon integration](docs/12-archon-integration.md) | Local-keymaster/4tress qualification and independent verification |
| [13 — Operations](docs/13-operations.md) | Environment separation, incidents, evidence and recovery |
| [14 — References](docs/14-references.md) | Historical and technical sources; see charter for field-method sources |
| [15 — Open questions](docs/15-open-questions.md) | Decisions needed for a useful, safe pilot and later inference |
| [16 — Implementation backlog](docs/16-implementation-backlog.md) | Application-led work packages and dependencies |
| [17 — Data contracts](docs/17-data-contracts.md) | Operational records, optional consented research metadata and provenance |
| [18 — Agent handoff](docs/18-agent-handoff.md) | Unified coding-agent goal, beginning at M0 |
| [19 — Scenarios](docs/19-scenarios.md) | Genuine tasks, qualification cases and sandbox studies |

## Scientific standard

Separate operational judgments, independent audited outcomes and synthetic hidden truth. Live work has no omniscient oracle. Record allegations, uncertainty, missing evidence, appeals and corrections. Measure eligibility, entry, refusal and affordability as well as completed jobs; distinguish changed selection from changed behavior.

Use the same payment/worker protections in safe policy comparisons. Freeze confirmatory definitions before observing the relevant outcomes, account for repeated participants and market spillovers, report null/adverse results and disclose subsidy/manual supervision. Protect third parties: cooperative harmful work is not alignment success.

This is one program with independent evaluation, not a promise of working software or permission to deploy. The [evidence register]({{ '/projects/agoric-work-marketplace/evidence.html' | relative_url }}) explicitly separates publication, feasibility, causal evidence and sustainability.
