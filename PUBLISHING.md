# Publishing and maintaining the site

This repository publishes a static website. It does not deploy Agoric Alignment, operate escrow, access wallets or connect to Archon merely because documentation is changed.

## Program and page structure

- Homepage: https://santyr.github.io/
- Thesis: https://santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/article.html
- Marketplace system: https://santyr.github.io/projects/agoric-work-marketplace/
- Unified program charter: https://santyr.github.io/projects/agoric-work-marketplace/application-led-research.html
- Evidence register: https://santyr.github.io/projects/agoric-work-marketplace/evidence.html
- Methods and evaluation (existing URL retained): https://santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/
- Escrow research: https://santyr.github.io/projects/agoric-work-marketplace/economic-accountability.html
- Assurance patterns: https://santyr.github.io/projects/agoric-work-marketplace/marketplace-assurance-patterns.html
- Consciousness collection: https://santyr.github.io/explorations/consciousness/

The homepage uses **the thesis / the working system / the evidence**. The working system is explicitly a proposed design, not deployed software. There is one application-led research program: the marketplace is its real-world test environment, and the former experiment material is its methodology and supporting test infrastructure. Do not reintroduce organizational separation or a requirement to finish a large simulated economy before qualifying a narrow live pilot.

## Source of truth and compatibility

Edit Markdown in `projects/agoric-work-marketplace/` and `articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/`. Preserve existing URLs and the original essay. M0–M5 is the controlling delivery sequence. Older A–F treatments, AT cases and simulator config/schema examples remain sandbox/reference assets, not a field-study approval or evidence of completion. Add explicit scope notes when extending those assets.

The escrow and assurance chapters remain useful mechanism studies within the unified program. Their mechanism qualification gates do not supersede the program's M0–M5 gates. External calls, identity writes, funds and participants require separate approvals. The evidence page must distinguish document publication, software verification, feasibility, exploratory observations, causal evidence, replication and sustainability.

Jekyll's optional-front-matter, relative-links, readme-index and titles-from-headings plugins render source documents and rewrite relative Markdown links. README pages become directory indexes. `_data/research.yml` retains the original twenty research document paths, while `_includes/research-guide.html` links the unified charter and evidence register. The nine existing conceptual SVGs use local styles; no external fonts or trackers are introduced.

## Verification

Run `python -m pip install -r publication-requirements.txt` and `python -m unittest discover -s tests -v`. Run the Jekyll build and `python tests/verify_publication.py --site _site`, then `python tests/verify_application_led.py --site _site` for the unified-program checks. The existing verifier preserves unrelated consciousness, donation and navigation checks. These are publication tests only, not economic evidence.

For live checks use `python tests/verify_publication.py --attempts 10` and `python tests/verify_application_led.py --attempts 10`. A source commit is not proof of deployment: verify the Pages build and the expected revision on the public pages. Inspect wide and narrow layouts, local links, fragment anchors, figures and printing where tooling permits. Never report a visual inspection that was not performed.

The shared layout retains the older publication marker for existing regressions and adds `agoric-unified-20261024-r1` for this revision. No secrets, raw participant data, synthetic reputation passed off as real, or unsupported empirical claims belong in the public artifacts. Sensitive legacy filenames and tests remain excluded from the generated site; repository history is not rewritten.
