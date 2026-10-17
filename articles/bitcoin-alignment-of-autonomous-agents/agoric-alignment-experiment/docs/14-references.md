# 14 — Annotated bibliography, source provenance and assumptions

**Purpose:** primary context required for coding agents; distinguish original sources from later retrospective interpretation. Use links at source access time; preserve URL, retrieval date and content digest if basing a formal claim on quoted passages. The historical hypothesis that Finney and Sassaman jointly created Bitcoin remains disputed and unproven and is not used to assign economic outcomes.

## Philosophical and historical foundations

1. **Timothy Leary** (1970s–80s), SMI²LE (Space Migration, Intelligence Increase, Life Extension) and `Info-Psychology` (1987). Historical context through W. Patrick McCray (2016), [`Timothy Leary's Transhumanist SMI²LE`](https://academic.oup.com/chicago-scholarship-online/book/18660/chapter-abstract/176873141), in *Groovy Science*. Relevant idea: deliberate future-building and cognitive enhancement. **Limitation:** no direct evidence that Leary specified Bitcoin's mechanisms or designed a reputation economy.
2. **Max T. O'Connor (Max More) and Tom W. Bell** (1988), [`Extropy` issue 1 introduction](https://extropy.agoraops.org/issues/01/introduction/). Speculates on AI, decentralization, autonomy and institutional evolution. Read original context rather than extracting a single slogan.
3. **Max More** (1998), [`The Extropian Principles v3.0`](https://www.mrob.com/pub/religion/extro_prin.html). Active technological improvement, spontaneous order, open societies and voluntary cooperation. Philosophical motivation, **not a measured theorem**.

## The agoric research lineage

4. **Mark S. Miller and K. Eric Drexler** (1988), [`Markets and Computation: Agoric Open Systems`](https://papers.agoric.com/papers/markets-and-computation-agoric-open-systems/full-text/). Central operational predecessor; read computational market construction and reputation service discussion, especially section 5.3.3 on positive reputation with inexpensive pseudonyms. Replicate mechanism as positive-credential/newcomer experiment rather than claiming its efficacy in all conditions.
5. **Miller and Drexler** (1988), [`Incentive Engineering for Computational Resource Management`](https://papers.agoric.com/papers/incentive-engineering-for-computational-resource-management/full-text/). Markets allocate computational resources through decentralized incentives. Motivates scarce goods, prices and service contracts.

## Cryptographic identity, privacy and reputation

6. **Hal Finney** (1993), [`Protecting Privacy with Electronic Cash`](https://nakamotoinstitute.org/library/protecting-privacy-with-electronic-cash/), originally *Extropy #10*. Public-key pseudonyms, e-cash and unlinkability. Privacy is part of the lineage; avoid falsely attributing a universal transparency preference to Finney.
7. **Hal Finney** (April 6, 1994), [`Pseudonyms and Reputations`](https://cypherpunks.samuelshadrach.com/archive/1994/04/cfeb0cb66eb2788fbbd2d653516bd3b0a3b889350733185ddf792ba0bb4ad412/), Cypherpunks mailing list. Signed credentials, portable reputation and linkability considerations. Follow-up discussion covers negative reputation and resetting pseudonyms.
8. **Nick Szabo** (1997), [`Formalizing and Securing Relationships on Public Networks`](https://nakamotoinstitute.org/library/formalizing-securing-relationships/). Contract formalization, reputational value, identity abandonment and credit; motivates horizon/cheating/collateral test.
9. **Mark Grant** (1995), [`Introduction to Digital Cash`](https://extropy.agoraops.org/issues/15/introduction-to-digital-cash/), *Extropy #15*. E-cash plus escrow, endorsements and decentralized commerce.
10. **Len Sassaman, Bram Cohen and Nick Mathewson** (2005), [`The Pynchon Gate: A Secure Method of Pseudonymous Mail Retrieval`](https://www.freehaven.net/anonbib/cache/sassaman%3Awpes2005.pdf). Persistent anonymous identity and distribution of trust. A communication privacy design, not evidence that Sassaman advocated publicly traceable finance.
11. **Len Sassaman** (2002), [`The Promise of Privacy`](https://www.usenix.org/conference/lisa-02/promise-privacy). Adoption obstacles and cryptographic privacy.

## Bitcoin and transaction attribution

12. **Satoshi Nakamoto** (2008), [`Bitcoin: A Peer-to-Peer Electronic Cash System`](https://bitcoin.org/bitcoin.pdf). Validation, proof-of-work, public transactions and pseudonymous privacy (`10). Consensus rules validate transactions, **not legality, consent or beneficial intent**. Mining reorganizations and data availability remain relevant assumptions.
13. **Sarah Meiklejohn et al.** (2013), [`A Fistful of Bitcoins: Characterizing Payments Among Men with No Names`](https://www.usenix.org/conference/imc13/technical-sessions/presentation/meiklejohn). Empirical address clustering; the inferred controller graph is neither complete nor always certain.
14. **Hal Finney** (2004), [`RPOW — Reusable Proofs of Work`](https://nakamotoinstitute.org/library/rpow/). Pre-Bitcoin cryptographic monetary experiment; not identical trust model to Bitcoin.
15. **Finding Satoshi documentary hypothesis** (2026): see [contemporaneous report](https://www.theblock.co/news/ecosystems/2026-04-22-finding-satoshi-documentary-makes-case-hal-finney-len-sassaman-bitcoins-co-creators-398423) and [Steven Levy's critical examination](https://www.wired.com/story/you-found-satoshi-lets-see-the-receipts). These are contrasting **secondary** accounts, not proof of joint authorship.

## Archon identity integration

16. **archetech/archon**, [white paper pinned to `0a6ecf5`](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/WHITEPAPER.md), `did:cid` registries, identity version histories, VCs and Lightning.
17. [Archon scheme](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/scheme.md); [Gatekeeper spec](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/gatekeeper/README.md); [MCP server](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/packages/mcp-server/README.md); [Lightning mediator](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/docs/services/mediators/lightning/README.md).
18. [Archon convergence proofs](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/proofs/agent-convergence/README.md). Formal model's convergence is conditional on proof assumptions, and does not prove every implementation or economic outcome correct.
19. [Archon Aug 2026 security audit](https://github.com/archetech/archon/blob/0a6ecf574a6a35175471a3342e30936336f37df6/SECURITY_AUDIT.md). Historical findings must be retested on currently pinned code.

## Methodological and standards references

20. [W3C DID Core Recommendation](https://www.w3.org/TR/did-core/) and [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/). A signature proves authorized assertion, not assertion truth.
21. [RFC 8785 — JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785) for interoperable signed and hashed JSON messages if selecting JSON. Ensure Archon's native suite is matched exactly; do not reserialize its signatures under an incompatible scheme.
22. [NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md) for the companion essay's Nostr long-form publication, not the primary experiment identity layer.
23. Bayesian Beta-Bernoulli completion modeling and proper scoring rules: standard quantitative methods; implement and validate formulas in [07 — Reputation](07-reputation-and-incentives.md) and [09 — Metrics](09-metrics-and-analysis.md). Document all package versions and the chosen confidence interval method.
24. [Original essay](../../article.md) and [its standalone summary](../../summary.md). Interpret as thesis and motivation, not established scientific evidence.

## Provenance instructions

Before publication of an external research paper, independently verify links, exact historical quotations and dates against originals or stable archival copies. Distinguish archival texts from documentary speculation. When unable to locate a referenced page, flag missing provenance rather than inventing passages or silently substituting adjacent sources. Record any correction in `docs/14-references.md` and downstream thesis claims.
