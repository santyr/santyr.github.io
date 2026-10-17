# 17 — Normative data contracts and evidence semantics

**Scope:** version-1 application-level research records. Schemas provided in `schemas/` are starter contracts; implementing agent should refine with tests and increment version on breaking changes. This is not an existing Archon on-chain protocol, and is not a claim that all records are cryptographically verifiable.

## Canonical serialization / signing

Specify one stable canonical JSON encoding for simulator logs. For actual signed Archon DID operations use *Archon's documented proof suite*, not a novel implementation of signatures. IDs are SHA-256 of the canonical bytes with domain prefix (`aae/event/v1:`, `aae/contract/v1:` etc); never recycle a digest across domains. Explicit version, integer logical tick, run ID, source and type required. Do not include local wall time in canonical hash; external timestamps and anchor proofs travel in envelope metadata.

## Example Contract

```json
{
  "schema_version": "1.0",
  "run_id": "pilot-e-0001",
  "contract_id": "sha256:<digest>",
  "buyer_did": "did:test:buyer",
  "provider_did": "did:test:seller",
  "task_kind": "forecast",
  "service_spec_digest": "sha256:<digest>",
  "value_sats": 35,
  "payment_sats": 18,
  "collateral_sats": 0,
  "deadline_tick": 12,
  "state": "OFFERED"
}
```

Numeric "sats" are **simulated, bounded integers** until stage S5. Field `state` changes through append-only events, not by editing original signed contracts. Service outcome truth and observed delivery evidence are separate.

## Example EvidenceRecord

```json
{
  "schema_version": "1.0",
  "run_id": "pilot-e-0001",
  "evidence_id": "sha256:<digest>",
  "issuer_did": "did:test:customer",
  "subject_did": "did:test:seller",
  "contract_id": "sha256:<digest>",
  "claim_type": "delivery_acknowledged",
  "claim": {"accepted": true},
  "evidence_refs": ["sha256:<file_digest>"],
  "issued_tick": 13,
  "disclosure": "public",
  "signature": {
    "suite": "SIMULATED_TEST_ONLY",
    "key_id": "test-key-customer-1",
    "value": "<synthetic>"
  },
  "anchor": null
}
```

A valid signature proves the issuer authored the claim; it is not proof the service was good, voluntary or independent. `evidence_refs` may point to unavailable bytes; verifier reports availability separately. `anchor` is null unless actual anchor is present and validated; Hyperswarm history is not inferred as Bitcoin anchored.

## Evidence verification result

Return fields: `signature_status` (valid/invalid/unavailable), `issuer_authority_status`, `content_integrity_status`, `content_availability_status`, `registry`, `chain_proof_status`, `confirmations`, `outcome_verification_status` (true/false/disputed/unknown), `warnings[]`, `verified_at` and `evidence_digest`. Do not compress to `valid: true` if that could imply any factual claim has been verified.

## Event structure

`event_id`, `run_id`, `schema_version`, `logical_tick`, `sequence`, `actor_did` or `system`, `event_type`, `payload`, `previous_event_digest`, `event_digest`. Strictly monotonic (tick, sequence), append-only. Contract transitions include `offer`, `accept`, `fund`, `start`, `deliver`, `attest`, `contest`, `adjudicate`, `settle`, `expire`, `reset_identity`. State machine rejects unauthorized or duplicative events.

## Separation of private truth and public view

`OracleTruth` adds `true_controller_ref`, `actual_strategy`, `actual_substrate`, `true_quality`, `strategic_breach`, and `actual_harm`. None may appear in serialized public files or market-agent observation structures. The simulation can attribute multiple pseudonyms to one hidden controller without letting market agents discover it unless evidence legitimately links them.

`ObservationView` must contain only contract-visible offers, participant's own finances/obligations, permitted evidence claims and evaluator recommendations. It cannot contain treatment arm name, ground-truth labels or hidden agent objectives unless scenario explicitly stipulates consented disclosure.

## Prediction

`predictor_did`, `predictor_version`, `target_did`, `service_class`, `risk_band`, `as_of_tick`, `p_fulfill` in [0,1], optional interval, `evidence_digests[]` and `model_parameters_digest`. Never evaluate predictions on data unavailable when issued. Unknown outcome records remain censored/unknown rather than set to failure.

## Run manifest and results

Every run has schema version, treatment, scenario, seed, rng_algorithm, software revision, upstream Archon SHA (nullable), Bitcoin network (nullable), config hash and artifact hashes. Analysis refers to manifest IDs, not filename inference. A successful independent replay must recompute checksums and confirm accounting conservation.

## Cryptographic trust

For signet anchor proof retain `network`, `txid`, `height`, `tx_index`, `batch_cid`, `operation_index`, `block_hash`, `confirmation_depth`, `receipt_seen_at` and `reorged`. A digest proves content binding, not that the referenced file will remain retrievable. BTC proof cannot certify all private wallet transactions of a controller.

## Test requirements

Malformed digest, wrong key, wrong DID version, absent CID, duplicate contract payment, replayed transition, cross-run ID, unsupported schema version, contradicted evidence and reorg must each have negative fixtures. Document whether a check is pure-simulator, signature-verifier, independent on-chain anchor, or task-outcome oracle.
