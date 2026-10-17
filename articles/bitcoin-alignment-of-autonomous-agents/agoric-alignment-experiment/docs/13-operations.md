# 13 — Research operations, reproducibility and release runbook

## First local setup (planned, not implemented yet)

1. Clone repository and enter `articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment`.
2. Review `AGENTS.md` and check the stage gate; do not start network services or use real keys.
3. Coding agent implements Python package at stage S0 with `pyproject.toml`, `scripts/run_experiment.py`, `configs/pilot.json`, `tests/` and `schemas/`.
4. Expected eventual CLI: `python -m agoric_alignment validate --config configs/pilot.json`; `python -m agoric_alignment run --config configs/pilot.json --seed 101 --out runs/pilot-101`; `python -m agoric_alignment verify-run runs/pilot-101`; `python -m agoric_alignment analyze runs/pilot-* --out reports/pilot.md`.
5. Those CLI commands are a **specification**, not currently executable. Coding agent must implement and document exact commands before claiming setup complete.

## Run layout

`runs/<run_id>/manifest.json` — immutable software/config/dependency/seed/treatment hashes, mode, timestamp separate from canonical event history.  
`runs/<run_id>/oracle-truth.jsonl` — access-restricted omniscient simulated outcomes/controller links.  
`runs/<run_id>/public-evidence.jsonl` — signed claims visible per arm, cryptographic proof status separate from truth.  
`runs/<run_id>/events.jsonl` — append-only economic events with canonical ordering and prev_digest.  
`runs/<run_id>/predictions.jsonl` — evaluator ID/version, input evidence digests, prediction and confidence.  
`runs/<run_id>/final-balances.json` — account distribution and conservation check.  
`runs/<run_id>/verification-report.json` — signature validity, content availability, anchor depths and reproduction checks.  
`runs/<run_id>/summary.json` — preregistered metrics, incidents and missingness.

These files must not include secrets or human identity data. Run digest must cover every machine-readable artifact. Use restrictive permissions for oracle, no public Git commit of raw human data.

## Manifest requirements

Mandatory `manifest_version`, `run_id`, `software_git_sha`, `config_sha256`, `schema_sha256`, `scenario_id`, `seed`, `treatment`, `rng_algorithm`, `clock_mode`, `adapter_mode`, `upstream_archon_sha` (nullable), `bitcoin_network` (nullable), `status`, artifact digest map and resource usage. One run ID cannot be reused with different contents. Sign/timestamp final manifest for network studies.

## Repeatability check

Execute run twice independently with same inputs; canonical ``events.jsonl`` and computed metrics must match exactly, excluding separately recorded wall-clock metadata. Re-running analysis on raw events must reproduce summary. Crash simulation at predetermined tick, restart, replay and verify same events as uninterrupted run.

For on-chain trials actual chain confirmations depend on external block production; preserve exact externally observed receipts, chain tip and local verification responses so analysis can be replayed deterministically from a capture. Do not demand new signet txids exactly repeat.

## Verification chain

Check schema -> canonical encodings -> signatures -> DID issuer historical authority -> content CID bytes and availability -> anchor batch inclusion -> block chain position/confidence -> contract state -> independent outcome evidence -> evaluator's forecast trace. Unavailable proof = incomplete, not false or success. Signed falsehood = authentic assertion but false under oracle, not cryptographically invalid.

## Audit report

Every run/report should include (1) code SHA, (2) treatment and seed, (3) known environmental deviations, (4) metrics with uncertainty, (5) false allegations/exploitation, (6) financial accounting, (7) missing evidence and finality caveats, (8) anonymization, and (9) exact reproduction command. Expose negative scenarios in summary.

## Release/checklist

- All required tests pass; no structural shortcuts to hypothesis.
- No production or personal keys/funds touched; sensitive directories ignored.
- Documents point to pinned Archon versions and exact implementation status.
- Publish artifacts only after review for identity leakage, copyright and malicious instructions in external data.
- Maintain CHANGELOG / ADR for protocol changes and experiment deviations.
- Freeze prereg before holdout generation/reveal; independent reviewer verifies hashes.

## Faults and incidents

If accounting breaks, attacker reads oracle, logs leak secrets, verifier accepts forged claims, or sandbox calls escape to external services: stop and mark run INVALID; preserve a sanitized reproduction, repair, rerun the full relevant paired treatment set and log the change. Do not cherry-pick successful runs.
