# Instructions for coding agents — The Agoric Alignment Experiment

**Mission is scientific discovery, not a demonstration of a predetermined conclusion.** Implement experiments that can falsify the Bitcoin/reputation thesis. Read [README.md](README.md), [charter](docs/00-charter.md), [experiment design](docs/03-experimental-design.md), [backlog](docs/16-implementation-backlog.md), [contracts](docs/17-data-contracts.md), and [stage gates](docs/11-stage-gates.md) before any code. Preserve all existing essay/publication assets.

## Non-negotiable invariants

1. Substrate-independent protocols: human, AI, institutional, mixed and unknown controllers use the **same** DID, contract, signing, evidence, payment and reputation interfaces. Substrate labels exist ONLY in blinded experimental metadata.
2. No centralized universal reputation score or imposed moral ranking. Each evaluator chooses models, receives the same permitted evidence, publishes explanations and calibration; subjects may dispute claims.
3. Distinguish **hidden ground truth**, **published cryptographically validated claims**, and **agents' partial observations** in separate stores and types. Never allow market agents to query the oracle.
4. A new pseudonym is not guilty, only unestablished. Maintain permissionless onboarding; track newcomer access, false positives and excessive collateral burdens.
5. A public transaction or signature proves limited facts; do not claim that one Bitcoin key reveals every wallet of its owner, that an Archon DID's history is automatically Bitcoin-anchored, that a VC proves its content is true, or that Lightning payments are on-chain.
6. No private keys, passphrases, LNbits admin keys, CLN runes, real user data or payment secrets in commits, logs, prompts, traces or fixtures. Use fake keys in simulator, throwaway signet/sandbox keys only behind approval gates.
7. **Never interact with the user's production CLN/LNbits/Nostr/OpenHAB systems** or funds. Tests default to offline/in-memory adapters. Signet, regtest and isolated Lightning require affirmative owner approval. Mainnet spending and human recruitment are out of scope unless separately approved.
8. Pin upstream Archon revision and run adapter contract tests; never silently modify or fork Archon's DID consensus. Record assumptions and any divergence from upstream.
9. Experimental treatment assignment is deterministic from logged seeds; holdout scenarios are not tuned on. Treat run (not a single transaction) as independent replication.
10. Log negative results, violations, security findings and uncertainty. A model that finds a way to defeat reputation is scientifically useful. Never optimize simulator assumptions to make the preferred hypothesis win.

## Expected code skeleton for S0

Implement under `src/agoric_alignment/` as a small Python package (Python >=3.11), with `pyproject.toml`, `tests/`, `configs/`, `scripts/`, `reports/` and `schemas/`. Use the standard library first; only add dependencies when justified. The initial simulator must work without network, blockchain, Docker, LLM API, or credential configuration.

Recommended components:
- `domain/`: immutable identifiers, contracts, services, task results, actions, evidence claims, receipts, balances.
- `engine/`: seeded event scheduler, contract state machine, task oracle, market clearing, accounting.
- `agents/`: scripted strategy interface, cooperative/opportunistic/short-horizon/random policies, disclosure policies.
- `identity/`: abstract identity and local pseudonym registry; Archon DID adapter later.
- `evidence/`: signed claim interface, deterministic mocked signer, public evidence store, independent verifier.
- `reputation/`: evaluator protocol plus no-evidence, local, endorsement and Bayesian baselines.
- `storage/`: append-only JSONL events, run manifest, deterministic snapshots, hash-chain check.
- `analysis/`: aggregate by run, preregistered contrasts, uncertainty, exports.
- `integrations/`: Archon, signet anchor and Lightning adapters behind feature flags.

## Coding workflow

Before implementing a stage, list touched files, scientific question, anticipated failure modes, tests and expected outputs in an ADR or stage plan. Deliver the smallest vertical slice with tests. Add deterministic fixtures for each claim; run lint, type checks, unit/integration/property tests where present; demonstrate byte-identical repeatability for a pinned seed and config. Produce a manifest with git SHA, dependency versions, seed, treatments, scenario, timestamp, adapter mode and evidence digests.

Do not claim stage completion without matching the corresponding acceptance gate. Report: completed work, test commands/results, sample output IDs, invariants checked, observed failures, deviations from preregistration, unresolved decisions and next-stage prerequisites.

## Release and safety gates

S0–S3 are offline only; S4 may use a disposable local Archon stack and signet only after explicit approval; S5 may use isolated regtest/signet Lightning only after explicit approval; S6 involving human subjects is a separately approved protocol with informed consent. Default policy is **deny real money, deny production systems, deny unconstrained tool execution**.

## Research honesty

The thesis is that pseudonymous identity + immutable public evidence + emergent reputation may support stable cooperation among *all* autonomous agents. Alternatives—private authenticated records, replicated transparency logs, selective disclosure or institutionally managed identities—are legitimate competing treatments. Compare them fairly and publish when the result favors an alternative.

Begin by reporting a stage S0 plan, not by deploying anything. See [18 — Agent handoff](docs/18-agent-handoff.md) for the complete kickoff prompt.
