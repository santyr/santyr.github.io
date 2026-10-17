# Publishing and maintaining the site

This is a static publication layer. It does not implement or execute the Agoric Alignment Experiment, access wallets, or deploy Archon.

## Published pages

- Home: https://santyr.github.io/
- Essay: https://santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/article.html
- Experiment: https://santyr.github.io/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/

## Single-source content

Edit the existing article.md, summary.md, experiment README.md, AGENTS.md, and docs/*.md. They remain usable on GitHub and for separate Nostr publication. Do not copy article text into HTML. GitHub Pages uses Jekyll's supported optional-front-matter, relative-links, readme-index, and titles-from-headings plugins. README pages become directory indexes; other Markdown documents become .html pages. Relative Markdown links are rewritten during the build.

Edit _data/projects.yml for related projects and _data/research.yml for the research navigation. The latter lists the original twenty documents. Update its entries when deliberately adding or renaming research documents. Related work appears after each page's primary content via _includes/related-work.html.

## Build and verify

The existing GitHub Pages branch deployment runs on main from the repository root. Check the repository's pages build and deployment workflow after a commit; a source commit alone is not proof that deployment succeeded. Inspect the generated artifact for unresolved Liquid tags, missing documents, broken local links and unwanted files. Test desktop and narrow mobile layouts and browser printing.

For source checks: python -m pip install -r publication-requirements.txt; python -m unittest discover -s tests -v. These tests validate the publication layer only, not scientific hypotheses or experimental software.

The site uses local styles and the existing hero.svg; there are no external fonts, client-side trackers, wallet integrations, or required JavaScript. Sensitive legacy filenames, test files, and build notes are excluded from the generated website. They are not removed from repository history.
