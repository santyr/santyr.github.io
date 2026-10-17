# 18 — Complete coding-agent kickoff handoff

Use this as the initial goal for an AI coding agent with GitHub access and a local development machine. It describes the implementation order, not permission to deploy public experiments or spend money.

## Goal

Implement **The Agoric Alignment Experiment** inside `santyr/santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment` as a reproducible, substrate-independent economic research system. Read [the original essay](../../article.md), [intellectual lineage](01-intellectual-lineage.md) and [references](14-references.md). Historical intent and proposed Finney/Sassaman authorship are hypotheses, not evidence of scientific success.

**Use https://4tress.org with local Python archon-keymaster as the Archon interface.** Read [12 — complete interface specification](12-archon-integration.md) and [configs/archon-4tress.json](../configs/archon-4tress.json). The `keymaster` executable comes from that package; this requirement is not an instruction to install a similarly named third-party skill. Source pin: `0a6ecf574a6a35175471a3342e30936336f37df6`, `python/keymaster`, declared version 0.7.0, Python >=3.12. Prefer Python 3.12+ for the project or isolate the integration worker from a retained 3.11 offline core.

Key custody/signing stay local. Agents receive only a scoped adapter, not private keys, the raw SDK, arbitrary CLI execution or a hosted wallet-admin API. A full local Archon stack and JavaScript MCP are not prerequisites for initial interoperability; local/independent nodes remain essential for suitable adversarial and independent-verification tests.

Read AGENTS.md, README, all docs, schemas and profiles first. Produce an S0 plan with files/tests/risks/artifacts; begin with offline S0 and progress through authorized S1–S3 gates. No public-node traffic until scoped network approval; no identity/credential publishing until write approval; no payments or human participants without their separate gates.

## Scientific invariants

- Identical protocol standards across human, AI and institutional controllers; labels stay in blinded oracle metadata.
- Separate authenticity, outcome truth and partial beliefs in types and storage; never upload oracle/controller links to 4tress.
- Fresh identities are unproven, not guilty; preserve participation and measure exclusion.
- No universal reputation/moral score; independent evaluators can disagree over authentic evidence.
- Identity reset may discard public reputation but cannot create money or silently erase oracle liabilities.
- Bitcoin is a tested history/ordering mechanism, not proof of contract truth or complete wallet attribution.
- Match exogenous workloads/seeds and use independent runs for inference; preserve negative results and strong alternatives.
- A hosted API success does not prove independence, privacy against the operator, archival availability or Bitcoin anchoring.

## Execution sequence

1. AAE-001–005: deterministic offline simulator, schemas, accounting and two-agent vertical slice.
2. AAE-006–008: 100-agent market, task/policy interfaces, paired A/B baselines.
3. AAE-009–012: endorsements/evaluators, public/private histories, resets/collateral and pilot analysis.
4. AAE-013–015: adversarial fixtures, independent evaluator replay and preregistration before holdouts.
5. AAE-016–018: optional client adapter with mocked SDK tests; approved bounded reads from 4tress; separately approved tiny synthetic writes; independent retained-history/chain verification and matched log comparison. BTC:signet only if supported and approved. Conduct deliberate faults/load only locally or on owned infrastructure.
6. AAE-019–020: separately approved isolated CLN/LNbits/L402. A 402 during preflight is a block, not automatic spending authorization.
7. AAE-021–023: separately approved bounded LLM/human trials and independent replication.

## Runtime requirements for the selected interface

Use the disabled-by-default profile. Set both ARCHON_NODE_URL and ARCHON_GATEKEEPER_URL to https://4tress.org and reject conflicts. Use an explicit local wallet/passphrase-file path under private run storage; reject inherited personal wallet or secret environment values. Pass only the origin to GatekeeperClient: it appends /api/v1 itself. Do not use its indefinite readiness retry loop.

Check readiness, registry list and actual permissions under the profile's request/deadline limits. Treat unknown server revision as unknown, record it separately from the local client pin, and capture sanitized responses for offline replay. Missing registry, 401/403, 402, 429, DNS/TLS failure or malformed evidence must fail closed without automatic host/chain switching. A write timeout requires reconciliation before retry. Hyperswarm and a generic confirmed flag cannot qualify as Bitcoin evidence.

## Acceptance

S0: a fresh compatible environment runs two agents offline with byte-identical canonical history and metrics, correct conservation and zero oracle leakage. Archon dependencies are optional. Document executable commands rather than claiming the proposed CLI already exists.

S1–S3: reproducible contrasts and adversarial traces, uncertainty/calibration, meaningful newcomer access and preregistered analysis; no threshold selection to force the thesis.

S4a: scoped hosted interoperability and local key custody verified. S4b/c: independent reconstruction, content availability and actual chain proofs validated under explicit assumptions, with approved local failure tests. Missing remote capabilities remain blocked/unknown; reaching the endpoint is not stage completion.

Use manifest 1.1 for archon-remote, including profile digest, local package/source provenance and remote observation digest. Preserve source server identity/capability uncertainty. Do not publish raw private wallet/secret files or actual participant data.

## Report after every stage

Stage; software and dependency revisions; files changed; scientific questions; commands/test results; artifact digests; observed outcomes; scope limits/request counts; client versus server provenance; fault tests; deviations; unresolved risks; evidence for gate completion; next action requiring approval. Report only actual outputs.

## Source policy

Primary historical sources remain in [14 — references](14-references.md); the official 4tress announcement, package README/metadata and pinned client implementation are linked in [12 — integration](12-archon-integration.md). Read the actual pinned API before adapting it. No fabricated signatures, method names, source quotations, remote availability claims or experimental findings.
