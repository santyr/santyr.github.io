# 18 — Complete coding-agent kickoff handoff

Copy the section below as the initial goal for an AI coding agent with GitHub access and a local development machine. This is an execution order, not authorization for real-world deployments.

## Goal

Implement **The Agoric Alignment Experiment** inside `santyr/santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment` as a research-grade, reproducible, substrate-independent agent economy. The guiding thesis and historical rationale are in [the original essay](../../article.md), [01 — intellectual lineage](01-intellectual-lineage.md) and [14 — references](14-references.md). Historical intent (Finney/Sassaman as Satoshi, future AI motive) is a hypothesis and **cannot be used as evidence of scientific success**.

Read `AGENTS.md`, README, all `docs/` files, available schemas and config templates first. Produce a concise stage S0 implementation plan with files, tests, risks and expected run artifacts. Begin only S0, then progress within authorized offline S1–S3 after stage checks. Do not touch production Bitcoin/Lightning wallets, public networks, real identities, paid AI APIs or humans without separate approval at S4–S6.

## Required scientific invariants

- All agents use identical protocol interfaces irrespective of human/AI/institutional labels; controller substrate metadata belongs in blind ground-truth store.
- Distinguish signed claim/authenticity, fact/outcome truth, and each observer's uncertain beliefs in separate schemas and physical data paths.
- Treat fresh pseudonyms as unproven, not negatively ranked; open entry remains possible.
- No mandatory global morality/reputation score. Multiple evaluator models can disagree over common evidence.
- Free identity resets are permitted in appropriate arms; simulated balances and liabilities follow controller in the hidden oracle, while public reputation does not.
- Bitcoin anchoring is a tested competing durability/verifiability mechanism, not asserted to prove contract truth or reveal all controller wallets.
- Maintain preregistered paired-seed causal controls and per-run independent statistical inference.
- Preserve negative results and benchmark strong private/federated transparency-log alternatives.

## Implementation order

1. Create deterministic simulator project, schema contracts, append-only event engine and tests (AAE-001–005).
2. Add 100-agent market, contract tasks, policy interface and arm A/B matched experiments (AAE-006–008).
3. Add endorsement records, public/private history, evaluators, identity abandonment, collateral and pilot analysis (AAE-009–012).
4. Add adversarial tests and freeze preregistration before any confirmatory holdout runs (AAE-013–015).
5. Only after owner permission: pinned Archon integration, signet and comparison transparency log (AAE-016–018).
6. Only after further permission: isolated CLN/LNbits and L402 (AAE-019–020).
7. Only after additional approval: bounded LLM/human trials and independent replication (AAE-021–023).

## Acceptance

At S0: a fresh clone with Python 3.11+ can run a 2-agent offline test in an environment without network or secrets; produced run manifest and canonical event history are bit-identical for identical inputs; all balances conserve and no oracle field leaks to market agent. CI or local test instructions must be explicit. No success claims without test output.

At S1–S3: show reproducible paired treatment comparisons, signed assertions distinguished from truth, false allegations distinguished from defaults, sensitivity sweeps for reset profitability, honest newcomer access, independent evaluator quality, complete adversarial fixtures, preregistered analysis. Do not choose thresholds to force the hypothesized outcome.

At S4+: independent DID and chain verification, reorg/availability handling, strict key isolation and scoped monetary authorizations.

## Reporting format after every stage

**Stage:** / **Git SHA & modified files:** / **Scientific questions:** / **Commands and test results:** / **Sample run IDs and manifest digests:** / **Measured outcomes (if any):** / **Invariants and fault injections:** / **Differences from plan:** / **Risks/open decisions:** / **Gate passed? evidence:** / **Next action requiring approval:**.

Report only observed outputs. If any document contradicts a code implementation, use the stricter fail-closed scientific/safety interpretation, raise an issue, and seek decision rather than guessing. Never silently change normative contracts once preregistration is frozen.

## Source policy

Primary sources and pinned upstream Archon URLs are in [14 — References](14-references.md) and [12 — Archon integration](12-archon-integration.md). Keep historical authorship and universal alignment claims explicitly speculative. No fabricated quotes or citations. Read actual source files when implementing, not just this handoff.
