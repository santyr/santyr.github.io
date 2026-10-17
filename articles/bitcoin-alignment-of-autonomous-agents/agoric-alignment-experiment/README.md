# The Agoric Alignment Experiment

**Status:** research specification and coding-agent handoff; no experiment results claimed.  
**Date:** 2026-10-17  
**Canonical context:** [Bitcoin and the Alignment of Autonomous Agents](../article.md) · [Summary](../summary.md) · [original publication directory](../).

## Mission

Empirically test whether **persistent pseudonymous identity, independently verifiable economic history, and earned, decentralized reputation** promote cooperation among autonomous agents with heterogeneous objectives, without a central moral authority or special privileges based on substrate. An *agent* is any accountable actor capable of decisions and resource commitments: a person, AI system, organization, institution, or hybrid. The identity layer **must not require** the observer to know the agent's substrate.

This project takes inspiration from Leary and the Extropians' active construction of future institutions; Miller and Drexler's agoric markets for software agents; Finney's pseudonymous credentials; Sassaman's privacy-preserving communication; Szabo's reputation economics; and Bitcoin's public consensus history. These are intellectual precedents, **not proof of a historically coordinated plan or proof that Bitcoin solves all alignment**. See [intellectual lineage](docs/01-intellectual-lineage.md).

## Selected Archon interface

Use **[4tress](https://4tress.org/) with the local Python `archon-keymaster` package** for Archon identity and credential operations. Keys and signing remain local; the `keymaster` CLI is available for operator setup. Read [the full interface guide](docs/12-archon-integration.md) and [disabled-by-default configuration profile](configs/archon-4tress.json). The pinned client requires Python 3.12+; a full local node or JavaScript MCP server is not a prerequisite for initial interoperability.

4tress is not a reputation authority or proof of Bitcoin anchoring. Actual capabilities, registry support, fees, availability and version must be checked in a bounded preflight. Independent verification and owned-node adversarial tests remain part of the research. This update configures the plan; it does not claim a live connection or authorize publishing identities or sending payments.

## Starting instruction for an AI coding agent

**Read [AGENTS.md](AGENTS.md) in full.** Then read [the implementation backlog](docs/16-implementation-backlog.md), [scientific protocol](docs/03-experimental-design.md), [data contracts](docs/17-data-contracts.md), [Archon interface](docs/12-archon-integration.md) and [stage gates](docs/11-stage-gates.md). Begin with S0 (repository scaffolding and deterministic no-network experiment). Do not deploy or fund anything until the corresponding gate is explicitly approved.

## Documentation map

| Document | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Mandatory agent contract, workflow, safe boundaries and definition of done |
| [00 — Charter](docs/00-charter.md) | Research question, theory of change, definitions and what we will not claim |
| [01 — Intellectual lineage](docs/01-intellectual-lineage.md) | Historical antecedents and what each implies experimentally |
| [02 — Preregistration](docs/02-preregistration.md) | Falsifiable hypotheses and primary/secondary outcomes |
| [03 — Experimental design](docs/03-experimental-design.md) | Treatments, causal contrasts, confounds, sample unit and blinding |
| [04 — Economy and agents](docs/04-economy-and-agents.md) | Tasks, actors, markets, economics and substrate masking |
| [05 — Architecture](docs/05-architecture.md) | Components, trust boundaries, interfaces and deployment |
| [06 — Evidence and identity](docs/06-evidence-and-identity.md) | DIDs, signed observations, auditability and revocation |
| [07 — Reputation and incentives](docs/07-reputation-and-incentives.md) | Multiple evaluators, incentive modeling and cold start |
| [08 — Adversarial suite](docs/08-adversarial-suite.md) | Attacks, threats, privacy and economic capture |
| [09 — Metrics and analysis](docs/09-metrics-and-analysis.md) | Formulas, statistical methods and reporting |
| [10 — Security and ethics](docs/10-security-and-ethics.md) | Isolation, human trials, threat model and stop rules |
| [11 — Stage gates](docs/11-stage-gates.md) | S0–S6 deliverables, acceptance and promotion approvals |
| [12 — Archon integration](docs/12-archon-integration.md) | 4tress, local archon-keymaster, version pinning, preflight and independent verification |
| [13 — Operations](docs/13-operations.md) | Reproduction, data provenance, fault injection and runbook |
| [14 — References](docs/14-references.md) | Original historical, technical and methodological sources |
| [15 — Open questions](docs/15-open-questions.md) | Design decisions and falsification-sensitive unknowns |
| [16 — Implementation backlog](docs/16-implementation-backlog.md) | Work packages with acceptance tests and dependencies |
| [17 — Data contracts](docs/17-data-contracts.md) | Required record layouts, events, evidence and results |
| [18 — Agent handoff](docs/18-agent-handoff.md) | Complete launch prompt and reporting format |
| [Scenarios](docs/19-scenarios.md) | Controlled scenarios, seed families and adversarial fixtures |

## Evidence standard

The simulator possesses hidden ground truth, the protocol publishes a restricted authenticated evidence view, and each participant has only its own belief state. Those three **must never be conflated**. A signed credential proves who asserted something, not that the assertion is correct. Bitcoin anchoring attests to existence/ordering under chain assumptions; it does not ensure IPFS availability, wallet completeness, service quality or moral truth.

## Required research sequence

1. S0–S2: deterministic simulator, baselines, reproducible data and unit/invariant tests.
2. S3: adversarial fixtures, competing reputation services, preregistration freeze and holdout protocol.
3. S4: pinned local archon-keymaster connected to 4tress for bounded interoperability; independently verified history and optional supported/approved Bitcoin signet anchoring. Use owned nodes for fault injection.
4. S5: isolated Lightning/LNbits/CLN receipts and cross-verifier reconstruction; not enabled by the hosted identity profile.
5. S6: bounded LLM agents and voluntary human studies (separately approved).

The work is a research program: neither results nor real-world security claims are implied by the presence of these documents.

## GitHub location

Documentation lives beside the original article rather than introducing a separate repository because this preserves the historical context and existing publication. Executable software can later be extracted to a dedicated project if scale, licensing, or CI needs justify it; record that as an ADR and maintain links both ways.
