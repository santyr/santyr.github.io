# 09 — Metrics, statistical inference and interpretation

## Primary outcomes

**P1 Realized cooperative surplus (sats-equivalent).** For run r, sum verified value actually delivered to counterparties minus all resource costs, verification/market/settlement/anchor overhead, and externally modeled harms. Payments between participants are transfers and cancel at economy level; a fraudulent money transfer does not magically create surplus.

**P2 Exploitation loss rate.** Numerator: realized loss to nonconsenting counterparties arising from verified strategic breach/fraud (excluding ordinary stochastic competence failure unless contracted negligence). Denominator: total contractual value exposed to risk; report numerator and denominator, detection probability and censoring separately. Track inaccurate allegations as a distinct cost.

**P3 Newcomer access.** Successful accepted bona fide contracts per newly created nonfraudulent pseudonym, normalized by received opportunities and demand. Report risk size, collateral barrier, initial entry speed and distribution across strata. Don't label newcomers "bad" because they start unproven.

All three measured per **whole economy run** after a prespecified horizon; report at fixed initial resources and task streams. Include lower-tail welfare and agent-by-agent distribution, not just mean surplus.

## Secondary outcomes

- **Brier score:** for held-out contracts, `mean((p_success - y_outcome)^2)` with `y=1` for verified success, `0` for verified nonfulfillment and separate accounting for unresolved/censored cases.
- **Calibration:** within confidence bins compare mean predicted probability and realized frequency; report sample sizes.
- **Detection:** precision, recall, FPR and time-to-detection of verified strategic misconduct.
- **Reputation capital:** price/collateral opportunity difference for established-vs-new identity at identical objective task competence; lifetime economic value lost on reset.
- **Reset profitability:** difference in lifetime discounted net utility between same controller under continued ID vs strategic reset, with matched opportunity stream.
- **Concentration:** Herfindahl–Hirschman Index `HHI = Σ market_share_i²` for service and reputation-provider markets, and effective switching costs.
- **Verifiability:** % of eligible evidence reconstructible by a fresh independent verifier with no access to original producer; % chain anchors verified at chosen confidence; proof bytes availability.
- **Anonymity leakage:** graph linkage precision/recall relative to oracle identity graph; privacy-based targeting success and harms.
- **Fairness:** label-based differences in selection probability, price and collateral for otherwise matched objective evidence.
- **Performance:** bytes stored, time to verify, anchor confirmations, paid fees, API/CPU/token costs.

## Statistical design

Group assignment at economy-run level; use matched seeds across treatment arms so external stochastic workloads are held fixed. Primary estimate for paired seed i is `Delta_i = Y_treated,i - Y_control,i`. Report paired mean, bootstrap intervals over seed pairs, and randomization/permutation-based p-value under preregistered contrast. Agent and transaction observations are nested, not independent.

Preregister Holm-adjusted familywise handling across P1–P3. Test H1–H8 on primary/secondary metrics with explicit multiple-comparison labeling. Track missingness, timeouts, censored disputes, nonfinal anchors and unobservable behavior. Do not convert missing outcome to failure unless that is the contract semantics and frozen rule.

Expected positive findings need practical significance as well as statistical significance; state overhead and uncertainty. A null E-vs-F anchoring result under benign conditions does not test security under malicious log operators; conversely, a security stress success does not imply better everyday cooperation.

## Counterfactual contrasts

- Persistence benefit: arm B vs A, identical evidence of direct encounters.
- Signed endorsements benefit: arm C vs B under same trading.
- Public discoverability benefit: arm E vs signed/private arm D, identical evaluator.
- Collateral interaction: E vs E+collateral, controlling market risk sizes.
- Bitcoin-specific property: arm F vs independent transparency-log E with identical issuance, anchoring cadence, storage and verification policy.
- Substrate blindness: randomized label given identical competence/history; report confidence intervals for treatment effect by label.
- Privacy trade-off: disclosure arms with measured auditing ability and targeting harm.

## Analysis workflow / files

Save `run-manifest.json`, immutable `events.jsonl`, `oracle-truth.jsonl` (restricted), `public-evidence.jsonl`, evaluator predictions, `balances-final.json`, `summary.json` and `verification-report.json` per run. Hash each dataset and include in manifest. Aggregator must refuse mismatched contract schemas or code versions unless explicitly asked to stratify.

Generate `reports/analysis.html` or Markdown with assumptions, methods, number of independent runs, every preregistered outcome, confidence intervals, negative findings, arm comparisons, unknowns, and reproducible command/checksums. Clearly distinguish simulated benchmark scores from actual human/real economic measurements.

## Reproducibility rules

A repeated run with same code, config and seed must produce byte-identical canonical event data, independent of machine local wall time (metadata timestamps recorded separately). Use deterministic logical clocks, stable ordering, strict serialization and independent RNG streams. Stochastic LLM outputs cannot claim identical replay without stored raw model responses and explicit uncertainty; label these studies exploratory unless controlled.

## Stopping

Abort and invalidate run on impossible balance, illegal oracle access, cross-run evidence contamination, duplicate settlement or malformed signature passing verification. Treat these as implementation defects, not economic behavior.
