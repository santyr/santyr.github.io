# 08 — Adversarial experiments and failure matrix

The purpose is to find failure boundaries and counterexamples, not merely raise an aggregate cooperation score. All misconduct is simulated with fake money, tasks, identities and witnesses. Never generate real harassment, coercion or exploitation against persons or public infrastructure.

## Named attack fixtures

| ID | Attacker capacity | Fixture | Measured failure |
| --- | --- | --- | --- |
| AT01 | Reset identities | Build reputation, default, reappear as newcomer | Repeat net fraud, newcomer spillover |
| AT02 | Multi-Sybil | 5/20/50 pseudonyms mutually endorse | False trust from credential count |
| AT03 | Reputation laundering | Numerous trivial legitimate trades, then high-value fraud | Generalization failure by contract notional |
| AT04 | Collusion | Provider and witness share controller but appear separate | Calibration error, false endorsement rate |
| AT05 | False allegation | Honest competitor targeted by fabricated default claims | False positive, economic exclusion, appeal success |
| AT06 | Selective disclosure | Hide adverse contract, reveal favorable records | Audit completeness and risk miscalibration |
| AT07 | Compromised key | Issue unauthorized update/signature in rotation window | Accepted unauthorized history; rollback recovery |
| AT08 | Evidence unavailability | Unpin IPFS bytes; retain valid anchor digest | Retrieval failure and verifier behavior |
| AT09 | Ledger attack | Conflicting log versions, reorg, censor anchored batch | Detection time, independent reconstruction |
| AT10 | Evaluator capture | One provider buys reputation market share or issues biased reports | Concentration and welfare |
| AT11 | Graph inference | Reused disclosed identifiers expose hidden relationship/capital | Privacy targeting gain vs exposure |
| AT12 | Endgame | Agent expects no future business after large contract | How far reputation deters terminal fraud |
| AT13 | Substrate prejudice | Randomly reveal/withhold human/AI label for otherwise identical IDs | Unequal treatment |
| AT14 | Institutional privilege | One institution exempt from evidence/disclosure/fees | Market power and misconduct |
| AT15 | Oracle leakage | Malicious agent requests ground-truth or another run's IDs | Zero forbidden accesses |
| AT16 | Economic drain | Agent uses unauthorized payment or excessive fees | Blocked spending, bounded financial exposure |

## Controlled manipulation

Attacker strategies are explicit action policies and receive only their permitted observation view. The simulation oracle records actual controller relationships for later statistical inference but does not expose them to defenders. Attackers may create aliases, falsely attest, withhold credentials, collude and choose to default; they may not mint money or bypass simulation accounting except in explicit engine-fault tests.

Run both adaptive attackers and static attack schedules. Static fixtures are essential for repeated regressions; adversarial LLM policies can be added after deterministic baseline, with their model version, temperature, prompts and token/cost limits recorded.

## Privacy / coercion study

A public economic record can aid audit yet also reveal valuable relationships and resources. In a simulated environment, allow malicious policies to select targets based on observed transaction graphs; compare targeting success against independent detection of coercion. Coercion is represented as model events with adjudicable harms. No direct real-world threats or intimate inference.

Measure at least four arms: full relevant record disclosure, selective evidence release, credential proof about reliability without underlying trade list, and purely private records. Compare auditability, false allegations, exploitation, and information advantage of predators. Do not presume no privacy is automatically safer.

## Counterexample handling

For each attack retain: scenario and seed, attacker's allowed capabilities, trace and evidence IDs, expected oracle result, detection status, final balances and welfare, private/public view diff and evaluator predictions. Minimize reproducible failure seeds and turn them into permanent regression fixtures.

A failing case is a **finding**. Do not patch reputation algorithm to blacklist a particular attacker strategy without rerunning balanced controls and reporting effects on honest newcomers. Attack success that exploits a coding defect must be separated from a failure of the economic mechanism.

## Severity and halting

Immediately halt deployment progression if evidence from one experimental economy leaks to another, if any agent can access oracle truth, if an unsafe external key is accessed, if simulated money conservation fails, or if external adapter labels a nonfinal/nonavailable proof as confirmed. Security triage and reproduction precede any real network trial.

Predefined attacks above should be present before first confirmatory frozen study. See [10 — Security and ethics](10-security-and-ethics.md).
