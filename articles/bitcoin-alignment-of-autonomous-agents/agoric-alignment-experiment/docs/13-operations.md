# 13 — Research operations, reproducibility and release runbook

## First local setup (planned, not implemented yet)

1. Clone repository and enter `articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment`.
2. Review `AGENTS.md` and check the stage gate; do not start network services or use real keys.
3. Implement the Python package at S0 with `pyproject.toml`, `scripts/run_experiment.py`, `configs/pilot.json`, `tests/` and `schemas/`. Prefer Python 3.12+; isolate the optional archon-keymaster worker if keeping a Python 3.11 simulator.
4. Expected eventual CLI: `python -m agoric_alignment validate --config configs/pilot.json`; `python -m agoric_alignment run --config configs/pilot.json --seed 101 --out runs/pilot-101`; `python -m agoric_alignment verify-run runs/pilot-101`; `python -m agoric_alignment analyze runs/pilot-* --out reports/pilot.md`.
5. Those CLI commands are a specification, not currently executable. Implement and document them before claiming setup complete.

## Hosted Archon setup at S4

Use **https://4tress.org** through local **archon-keymaster**, following the pinned-source installation and preflight in [12 — Archon integration](12-archon-integration.md). [configs/archon-4tress.json](../configs/archon-4tress.json) is a separate disabled-by-default integration profile, not a simulator scenario and not executable authorization. Validate it against [archon-profile.schema.json](../schemas/archon-profile.schema.json), not experiment-config.schema.json.

After network approval, perform a bounded read-only check and save sanitized observations. Do not provision public identities until write scope is separately approved. No wallet-admin service runs on 4tress on behalf of this client: signing and secrets remain local. Set both node URL variables explicitly, prevent personal wallet autodiscovery and isolate each wallet under ignored private storage. Capture local client dependencies, remote capabilities and actual registry support independently.

Use captured replies for bulk deterministic studies. Hosted DNS/TLS failures, missing registry support, 401/403, 402 and rate limits are diagnostic outcomes, not reasons to switch hosts or authorize spending. No automatic write retry; reconcile an uncertain submission. Run destructive faults and load tests on owned/local infrastructure only.

## Run layout

`runs/<run_id>/manifest.json` — immutable software/config/dependency/seed/treatment hashes and mode.  
`runs/<run_id>/oracle-truth.jsonl` — restricted omniscient outcomes/controller links.  
`runs/<run_id>/public-evidence.jsonl` — signed claims visible per arm, proof status separate from truth.  
`runs/<run_id>/events.jsonl` — append-only canonical economic events.  
`runs/<run_id>/predictions.jsonl` — evaluator/model version, evidence digests and probability.  
`runs/<run_id>/final-balances.json` — account distribution and conservation check.  
`runs/<run_id>/verification-report.json` — signatures, availability, anchor depth and reproduction.  
`runs/<run_id>/summary.json` — preregistered metrics, incidents and missingness.  
`runs/<run_id>/archon-observations.json` — remote status/version when exposed, registry list, sanitized request observations and proof provenance; used by hosted profiles.  
`runs/private/archon/<run_id>/<pseudonym>/` — local wallet and passphrase files; never included in exported artifact maps or publications.

No exported artifact may contain secrets or real identities. Use restrictive permissions for private/oracle files and never publicly commit raw human data.

## Manifest requirements

Keep existing identity, software/config/schema hashes, scenario, seed, treatment, RNG, logical clock, mode, source SHA, Bitcoin network (`none`, `regtest` or `signet`), status, artifact digests and resource usage. One run ID cannot be reused with changed contents.

Manifest **1.1** adds `archon-remote` and a required non-null `archon_interface` for that mode: local distribution/version/source, node URL, interface profile digest and remote observation-artifact digest. The observation digest must match the `archon-observations.json` entry in `artifact_sha256`; validate that semantic condition in the runner. A local client revision never stands in for an unknown remote server revision. Manifest 1.0 remains accepted for legacy modes without interface fields. Event, evidence and prediction schema versions remain unchanged.

## Repeatability check

Run twice with the same inputs; canonical events and metrics must match byte-for-byte excluding wall-clock metadata. Re-analyze raw events to reproduce summary. Interrupt at a fixed tick, resume/replay and compare with uninterrupted execution.

Live service responses and chain confirmations change externally. Preserve captured replies/receipts, server/version observation, tip and proofs for deterministic replay; do not require repeated public DID writes or signet transactions to produce identical external IDs. Keep live interoperability and scientific simulator result claims separate.

## Verification chain

Check schema -> canonical encoding -> signature -> historical issuer authority -> content hash/availability -> registry/batch/chain proof -> contract state -> independent outcome evidence -> evaluator prediction trace. An unavailable proof is incomplete, not false or successful. An authentic falsehood is a validly signed claim contradicted by outcome evidence, not an invalid signature.

## Audit report and release

Report code/profile/dependency pins, treatment/seed, remote observation provenance, environmental deviations, metrics/uncertainty, false allegations/exploitation, money accounting, evidence gaps, privacy protections and reproduction commands. Publish negative scenarios. Check all tests; review artifacts for secrets, identity leakage and untrusted instructions; freeze preregistration before holdout access; record ADRs and deviations. Do not assert success from a source pin, hosted marketing claim or HTTP 200 alone.

## Incidents

Accounting failure, oracle access, secret leakage, forged proof acceptance or unapproved network escape invalidates the run. Freeze a sanitized trace, repair, rerun relevant paired conditions and record the change. A hosted write timeout pauses further writes until its state is reconciled. Preserve failures without cherry-picking.
