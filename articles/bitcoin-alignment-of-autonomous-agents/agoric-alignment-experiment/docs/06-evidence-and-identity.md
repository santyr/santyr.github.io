# 06 — Evidence, identities, verifiability and audit trails

## Substrate-neutral pseudonyms

Public protocol identities are strings and verification keys, not types such as human/AI/corporation. Experimental `controller_ref` and `actual_substrate` must remain in sealed oracle metadata. Many pseudonyms may belong to one controller, and one institutional DID may be authorized through multiple keys. The experiment must not infer controller identity from string similarity or from a self-asserted label.

Creating a pseudonym is permitted at zero direct protocol cost in the baseline. Its reputation begins with uncertain priors, not a negative score. Allow explicit signed links or cryptographic proof of control from an established identity when a participant chooses to provide them; do not automatically merge reputation across identifiers.

## Three-record epistemology

1. **Truth:** task oracle evaluates what actually happened, including private malicious intentions modeled as actions and the realized quality of delivered work. Only research evaluator may read.
2. **Evidence:** public/disclosed signed claims with issuer, subject, contract reference, timestamps and storage receipts. Authenticity is cryptographic; correctness is *not* implied.
3. **Beliefs:** each agent and reputation evaluator's separate, potentially erroneous, evidence-filtered interpretation.

Type systems, storage ACLs and tests should make it impossible for layer (2)/(3) to read truth accidentally.

## Evidence lifecycle

An agent announces offer; counterparty accepts; escrow may fund; provider performs work; claimant publishes a signed claim (e.g. delivered a forecast); an independent verifier may attest to performance; counterparty may contest; auditor can append corrections. Publish every event as immutable append rather than mutating past messages. A disputed claim stays visible with `status=contested` inferred from later evidence; dispute resolution creates further evidence, never deletes an earlier signed claim.

Store a standard `EvidenceRecord` with unique digest, issuer DID, subject DID(s), contract ID, event type, observation window, commitment to raw data if large, proof suite, auth verification result, and optional chain anchor. Separate evidence signing timestamp from first-observed time and chain upper/lower bounds. Verification returns a rich status: signature valid, identity history valid at claimed time, CID content available, anchor finality depth, and outcome independently checked; do not coalesce into a single Boolean "verified".

## Archon adapter rules

At pinned revision `0a6ecf574a6a35175471a3342e30936336f37df6`, Archon supports content-addressed `did:cid` genesis, signed operations, versioned identity states, credentials and Bitcoin-family anchors. A DID may choose Hyperswarm or local rather than a blockchain; **never silently classify unanchored history as Bitcoin anchored**. A hash or CID proves integrity only if bytes are retrievable. Archon Keymaster controls sensitive material and shall not be accessible to arbitrary experimental policies.

Tests for creation, resolution, verification, key rotation, deletion, registry migration and reorganization need cross-implementation parity checks where available. Distinguish Archon's documented protocol convergence proof under assumptions from complete runtime implementation correctness.

## Proof obligations

- Can independent auditors validate issuer authority at evidence issuance time, not merely current DID state?
- Can unrelated reviewers reconstruct full disclosed history after actor exits, key rotates, off-line nodes restart, IPFS pins disappear, or reorg occurs?
- Can malicious issuers fabricate performance? Signatures cannot stop them; independent attestations should change posterior credibility.
- Can an adversary conceal negative records by failing to disclose? Compare volunteered evidence versus independently discoverable evidence arms; inability to discover is measured explicitly.
- Can an observer link unrelated pseudonyms beyond justified disclosures? Monitor metadata leakage, address reuse and cluster inferences as possible privacy harm.

## Retention and verification

Evidence bytes and their signed manifests require local multi-node preservation in S4/S5, hash validation, failure-injection testing and unambiguous availability states. Merely placing an IPFS hash in a Bitcoin output is insufficient to guarantee recoverability. Treat block confirmation probabilistically: configurable depths, reorg recovery, and explicit temporary uncertainty.

A claimed complete wallet history is not guaranteed simply because an agent reveals one Bitcoin key. The experiment can demand signed attestations to enumerated keys as contract requirements, but cannot assume hidden keys don't exist. Do not insert experimental hidden truth into chain-analysis output.

## Portability and disputes

An agent may export its evidence manifest and let independent evaluators reproduce its historical conclusions. Credible negative events may be published by counterparties without subject approval; counterclaims, appeals, issuer accountability and falsification detections must remain possible. An alleged default is not equivalent to proven misconduct; log both.
