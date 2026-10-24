# 17 — Shared operational and research data contracts

These are proposed requirements for one application domain, not implemented schemas or published NIPs/NUTs. Existing JSON schemas/configurations remain simulator and integration-profile examples until a tested, explicit migration is delivered. Do not relabel manifest 1.0/1.1 or synthetic oracle records as a complete field-study protocol.

## Common envelope

Every relevant record needs a stable object ID, schema version, environment/namespace, issuer/authority reference, timestamp semantics, canonical digest and signature-domain binding where applicable. Contracts and actions reference exact revisions and predecessor state. Separate synthetic logical time from external observation time and evidence availability. Idempotency and replay protection must survive relay duplication, process restarts and ambiguous writes.

Environment labels alone are insufficient: separate keys, wallet scopes, databases, credentials and allowed adapters must enforce the boundary. Test events and synthetic signatures cannot create live commercial history. A field study uses actual consented operational events, not an oracle-filled copy of the simulator model.

## Operational objects

| Proposed object | Required meaning |
| --- | --- |
| EconomicMandate | Accountable principal, authorized requester, purpose/categories, budgets, expiry, delegation and revocation handling |
| TaskContract | Parties, scope, exact revision, evidence/acceptance tests, qualifications, deadlines, compensation/expenses, settlement/dispute policy and data terms |
| CollateralLock/Reservation | Rail/network/mint, verified funded locator, ownership/spend rules, unique per-obligation allocation, amount/duration, pending claims and recovery |
| EvidenceRecord | Issuer, contract, content digest, collection/provenance limits, access/retention, assertion versus independently assessed fact |
| Review/AppealDecision | Decision authority, contract rules, available evidence, uncertainty, allegation/finality state and superseding links |
| SettlementReceipt | Actual rail-confirmed inputs/outputs/fees or payment state, contract binding, independent checks, ambiguity and remaining liabilities |
| OutcomeAttestation | Attributed fulfillment/payment/dispute statements with issuer and finality; not automatic truth or reputation points |
| ReputationAssessment | Contextual evaluator, policy/model version, permitted evidence, uncertainty and prospective recommendation; no spend authority |

Private bearer proofs, wallet bytes, passphrases and raw personal evidence are not public fields. A collateral credential is a claim; actual allocation must be checked. A rail receipt does not prove physical delivery. An analyst cannot create an authorized remedy by writing a score into an object.

## Research and consent objects

Maintain separate access-controlled records for operational terms, research enrollment/consent, approved intervention policy, assignment/exposure, independent outcome audit, analysis extract and evidence report. A research ID is not consent. Record what uses are permitted, version/date, withdrawal and retention constraints, and whether policy experimentation affects terms. Do not promise deletion of already public material or erase outstanding obligations.

For a study, store study/protocol registration and amendment references; eligible population and recruitment criteria; assignment unit/method and any randomization provenance; cluster/participant linkage under authorized access; policy and contract versions; follow-up, attrition and missingness; audit sampling probabilities and disagreements; subsidies/manual intervention; monitoring, stops and unblinding. Analysts receive minimized authorized extracts, not production keys or unrestricted identity graphs.

Unenrolled ordinary users must not silently become experimental subjects. Any operational aggregation outside optional research must have a separately justified and disclosed policy. Where collecting refusal/eligibility data is necessary for valid inference, obtain the appropriate permissions rather than quietly expanding telemetry.

## Manifest migration

A future application/study manifest should identify environment, domain/schema/software/policy/model revisions, authorized capabilities, budgets, actual adapter provenance, consent/approval references, dataset digests and analysis scope. Fields and validation rules require an explicit new version with compatibility tests; this document does not pretend existing example schemas already enforce them.

Retain existing archon-remote provenance: local source/distribution/dependencies, selected endpoint/profile, observed server version or unknown state, registry/capabilities and captured-response digest. Client pin and server revision are not interchangeable. Synthetic manifests retain seeds/oracle references privately; field manifests cannot invent ground truth or deterministic outside-world replay.

## Invariants and verification

Conservation, beneficiary authority, unique reservations, immutable accepted revisions, idempotence, safe retry, privacy and environment separation apply to every adapter. Independently replay permitted evidence without granting the replayer payment authority. Refuse incompatible schema/policy/environment mixtures unless an approved analysis explicitly stratifies them.

Outcome states must include contested, unknown and overturned, not just success/failure. Test malformed signatures, missing data, stale keys, misleading confirmed flags, secret fields, mismatched contract digests and cross-run/research-consent leakage. Safe aggregate export and full private evidence have different audiences and retention rules.

The [architecture](05-architecture.md), [field design](03-experimental-design.md), [operations](13-operations.md) and [backlog](16-implementation-backlog.md) determine when these requirements must become tested code.
