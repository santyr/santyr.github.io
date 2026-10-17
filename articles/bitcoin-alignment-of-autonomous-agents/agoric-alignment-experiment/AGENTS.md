# Instructions for coding agents — The Agoric Alignment Experiment

**Mission is scientific discovery, not a demonstration of a predetermined conclusion.** Implement experiments that can falsify the Bitcoin/reputation thesis. Read [README.md](README.md), [charter](docs/00-charter.md), [experiment design](docs/03-experimental-design.md), [backlog](docs/16-implementation-backlog.md), [contracts](docs/17-data-contracts.md), [Archon interface](docs/12-archon-integration.md) and [stage gates](docs/11-stage-gates.md) before any code. Preserve all existing essay/publication assets.

## Selected Archon interface

Use **https://4tress.org with the local Python `archon-keymaster` package** for the preferred S4 integration. Its `keymaster` CLI is an operator interface; agent policies use a narrow authorized adapter around the SDK. Keys and signing stay local; never send passphrases, wallet files or private keys to 4tress. A full local Archon stack and JavaScript MCP server are not prerequisites for initial interoperability, but independent/local nodes remain necessary for appropriate adversarial and independent-verification tests.

Read [12 — Archon integration](docs/12-archon-integration.md) and [configs/archon-4tress.json](configs/archon-4tress.json). The profile is disabled and read-only by default. Source revision `0a6ecf574a6a35175471a3342e30936336f37df6` declares client version 0.7.0 and requires Python >=3.12. Use a separate 3.12+ worker if retaining a 3.11 offline simulator. Pin the local client separately from the hosted server's observed version. These documentation changes do not authorize public identity writes, load tests or payments.

## Non-negotiable invariants

1. Substrate-independent protocols: human, AI, institutional, mixed and unknown controllers use the **same** DID, contract, signing, evidence, payment and reputation interfaces. Substrate labels exist ONLY in blinded experimental metadata.
2. No centralized universal reputation score or imposed moral ranking. Each evaluator chooses models, receives the same permitted evidence, publishes explanations and calibration; subjects may dispute claims.
3. Distinguish **hidden ground truth**, **published cryptographically validated claims**, and **agents' partial observations** in separate stores and types. Never allow market agents to query the oracle.
4. A new pseudonym is not guilty, only unestablished. Maintain permissionless onboarding; track newcomer access, false positives and excessive collateral burdens.
5. A public transaction or signature proves limited facts; do not claim that one Bitcoin key reveals every wallet of its owner, that an Archon DID's history is automatically Bitcoin-anchored, that a VC proves its content is true, or that Lightning payments are on-chain.
6. No private keys, passphrases, LNbits admin keys, CLN runes, real user data or payment secrets in commits, logs, prompts, traces or fixtures. Use fake keys in simulator, disposable local integration wallets only behind approval gates.
7. **Never interact with the user's production CLN/LNbits/Nostr/OpenHAB systems** or funds. Tests default to offline/in-memory adapters. Network integration, signet, regtest and isolated Lightning require affirmative owner approval. Mainnet spending and human recruitment remain separately gated.
8. Pin upstream Archon revision and run adapter contract tests; never silently modify or fork Archon's DID consensus. Validate remote responses and record unknown server version/capabilities rather than assuming a source pin describes the server.
9. Experimental treatment assignment is deterministic from logged seeds; holdout scenarios are not tuned on. Treat run (not a single transaction) as independent replication.
10. Log negative results, violations, security findings and uncertainty. A model that finds a way to defeat reputation is scientifically useful. Never optimize simulator assumptions to make the preferred hypothesis win.
11. Do not send bulk tournaments, fault injection, Sybil attacks or privacy-sensitive ground truth to 4tress. Missing registry support, authentication challenges, rate limits and payment requests fail closed; no automatic host, registry or payment fallback.

## Expected code skeleton for S0

Implement under `src/agoric_alignment/` as a small Python package (offline floor Python >=3.11; prefer >=3.12 for SDK integration), with `pyproject.toml`, `tests/`, `configs/`, `scripts/`, `reports/` and `schemas/`. Use the standard library first; add `archon-keymaster` as an optional integration dependency, not an offline prerequisite. The initial simulator must work without network, blockchain, Docker, LLM API or credential configuration.

Recommended components:
- `domain/`: immutable identifiers, contracts, services, task results, actions, evidence claims, receipts, balances.
- `engine/`: seeded event scheduler, contract state machine, task oracle, market clearing, accounting.
- `agents/`: scripted strategy interface, cooperative/opportunistic/short-horizon/random policies, disclosure policies.
- `identity/`: abstract identity and local pseudonym registry; authorized Keymaster adapter later.
- `evidence/`: signed claim interface, deterministic mocked signer, public evidence store, independent verifier.
- `reputation/`: evaluator protocol plus no-evidence, local, endorsement and Bayesian baselines.
- `storage/`: append-only JSONL events, run manifest, deterministic snapshots, hash-chain check.
- `analysis/`: aggregate by run, preregistered contrasts, uncertainty, exports.
- `integrations/`: local archon-keymaster/4tress adapter, signet proof verification and isolated Lightning behind separate capability gates.

## Coding workflow

Before implementing a stage, list touched files, scientific question, anticipated failure modes, tests and expected outputs in an ADR or stage plan. Deliver the smallest vertical slice with tests. Add deterministic fixtures for each claim; run lint, type checks, unit/integration/property tests where present; demonstrate byte-identical repeatability for a pinned seed and config. Produce a manifest with git SHA, dependency versions, seed, treatments, scenario, timestamp, adapter mode and evidence digests. Hosted runs additionally record the versioned interface profile and captured remote observation digest under manifest 1.1.

Do not claim stage completion without matching the corresponding acceptance gate. Report: completed work, test commands/results, sample output IDs, invariants checked, observed failures, deviations from preregistration, unresolved decisions and next-stage prerequisites.

## Release and safety gates

S0–S3 are offline only. S4 begins with approved bounded reads from 4tress via local archon-keymaster; publishing synthetic records needs separate explicit write approval. Signet and independent-node tests remain separately authorized. S5 may use isolated regtest/signet Lightning only after explicit approval; S6 involving human subjects is a separately approved consented protocol. Default policy is **deny real money, deny production wallet access, deny unconstrained tool execution**.

## Research honesty

The thesis is that pseudonymous identity + immutable public evidence + emergent reputation may support stable cooperation among *all* autonomous agents. Alternatives—private authenticated records, replicated transparency logs, selective disclosure or institutionally managed identities—are legitimate competing treatments. Compare them fairly and publish when the result favors an alternative. A hosted node is an integration convenience, not proof of decentralized trust or economic alignment.

Begin by reporting a stage S0 plan, not by deploying anything. See [18 — Agent handoff](docs/18-agent-handoff.md) for the complete kickoff prompt.
