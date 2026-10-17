# 15 — Open questions, competing explanations and future ADRs

## Fundamental uncertainties

1. **Necessity vs sufficiency:** Does persistent reputation require Bitcoin, a generic public transparency log, or merely contractual enforcement and persistent identity? The study must measure alternatives.
2. **Disclosure completeness:** One known public key is not proof of all wallets controlled by an agent. Which contractual scope disclosures can be verified, and how do we measure strategic omissions?
3. **Subjective versus objective claims:** Some services have objectively scoreable outputs (compute, forecasts); some (trust, fairness, consent) cannot be adjudicated by a blockchain. How far do conclusions generalize?
4. **Definition of agent:** Operational controllers can be humans, models, corporations and multi-party organizations. Does one DID map to one economic agent or many? Avoid using substrate as a privileged protocol input.
5. **Reputation transfer and recovery:** How should confidence transfer on key rotation, merger of identities, splits, expiring organizations or lost keys without enabling laundering?
6. **Sybil defense:** Can collateral, paid history and independent witnesses deter coordinated self-endorsement without punishing poor/new participants?
7. **Economics of endgame betrayal:** At which discount factors or value-at-risk does cheating become rational even for highly reputable agents?
8. **Negative reputation privacy:** Does public allegation evidence improve accuracy or enable censorship, false accusations and persistent inequitable exclusion?
9. **Markets for reputation:** Will independent evaluators compete on prediction quality or converge toward incumbents and concentrated power?
10. **Public vs selectively disclosed evidence:** Does full visibility create net accountability or targeting harms? Which partial disclosures preserve essential auditability?
11. **Bitcoin-specific guarantees:** What exactly changes when operations are anchored to proof-of-work compared with independent signed transparency log or alternative consensus registry?
12. **Temporal ordering:** Is inclusion timestamp sufficient for an economic promise that depends on precise events, or are trusted task timestamps/third-party witnesses unavoidable?
13. **Data availability:** Who stores signed records after publishers disappear, and can auditors prove they obtained all relevant disclosed history?
14. **Coercion and off-ledger acts:** Which harmful actions never create observable financial evidence, and which additional witnesses are needed?
15. **Human decision biases:** Do substrate labels affect trust when reputation and abilities are otherwise held constant?
16. **Simulation realism:** Does scripted-agent advantage extrapolate to bounded LLM agents or real people? Which capacities are missing from artificial economies?

## Decision register (pending ADR)

D01 Choose Python versions and lockfile manager; candidate Python 3.11+ with stdlib-first deps; S0 decision.  
D02 Fix signed event canonical encoding and codec; must interoperate only when using Archon's actual suite.  
D03 Specify bilateral price clearing and disputes policy; choose simple deterministic implementation for S1.  
D04 Pick exact fixed-size signet test resources and separate permissions; gate S4.  
D05 Decide whether opt-in Archon DID aliases can link to existing Nostr identities via dual-control signatures.  
D06 Define referee oracle for cases not objectively verifiable and apply double-blind evidence availability.  
D07 Define retention/independent pinning architecture and reimbursement of infrastructure costs.  
D08 Establish preregistered thresholds, power, holdout seeds and test families from S2 pilot.  
D09 Separate LLM exploratory variation from scripted confirmatory trial; gate S6.  
D10 Establish license if/when software is extracted to a standalone project.

Every ADR records context, alternatives, decision, trade-offs, tests, impact on inference and approval. No coding agent should silently pick assumptions that could determine research outcome.
