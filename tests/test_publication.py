"""Checks for the publication site; no experiment or payment code is executed."""
from pathlib import Path
import unittest
import yaml
ROOT = Path(__file__).resolve().parents[1]

class PublicationTests(unittest.TestCase):
    def test_pages_configuration(self):
        path = ROOT / '_config.yml'
        self.assertTrue(path.is_file())
        config = yaml.safe_load(path.read_text())
        self.assertEqual(config['url'], 'https://santyr.github.io')
        self.assertTrue({'jekyll-relative-links','jekyll-optional-front-matter','jekyll-readme-index'} <= set(config['plugins']))
        self.assertIn('.config.key', config['exclude'])

    def test_homepage_has_both_publications(self):
        path = ROOT / 'index.html'
        self.assertTrue(path.is_file())
        body = path.read_text()
        self.assertIn('article.html', body)
        self.assertIn('agoric-alignment-experiment/', body)
        self.assertNotIn('Hello World', body)

    def test_related_projects_follow_content(self):
        path = ROOT / '_layouts/default.html'
        self.assertTrue(path.is_file())
        body = path.read_text()
        self.assertLess(body.index('{{ content }}'), body.index('include related-work.html'))
        self.assertIn('id="main-content"', body)
        self.assertIn('name="viewport"', body)
        self.assertNotIn('ajax.googleapis.com', body)

    def test_requested_work_is_linked(self):
        path = ROOT / '_data/projects.yml'
        self.assertTrue(path.is_file())
        groups = yaml.safe_load(path.read_text())
        urls = [item['url'] for group in groups for item in group['items']]
        for url in ['https://lightning-goats.com', 'https://github.com/lightning-goats/lnbits-extensions', 'https://github.com/lightning-goats/lightning_goats_extension']:
            self.assertIn(url, urls)
        self.assertEqual(len(urls), len(set(urls)))

    def test_consciousness_exploration_is_published(self):
        essay = ROOT / 'explorations/consciousness/the-unreadable-language-of-perception.md'
        landing = ROOT / 'explorations/consciousness/README.md'
        diagram = ROOT / 'assets/consciousness/perceptual-model.svg'
        self.assertTrue(essay.is_file())
        self.assertTrue(landing.is_file())
        self.assertTrue(diagram.is_file())
        text = essay.read_text()
        self.assertIn('Constrained Generative Perception Hypothesis', text)
        self.assertIn('## Summary', text)
        self.assertIn('References and further reading', text)
        self.assertIn("perceptual-model.svg", text)
        self.assertIn("The Unreadable Language of Perception", landing.read_text())
        self.assertIn('<svg', diagram.read_text())
        groups = yaml.safe_load((ROOT / '_data/projects.yml').read_text())
        category = next(g for g in groups if g['title'] == 'Explorations of consciousness')
        self.assertIn('explorations/consciousness/', category['url'])
        self.assertTrue(any('the-unreadable-language-of-perception.html' in item['url'] for item in category['items']))


    def test_agoric_work_marketplace_is_independent_and_illustrated(self):
        import xml.etree.ElementTree as ET
        project = ROOT / 'projects/agoric-work-marketplace/README.md'
        self.assertTrue(project.is_file())
        paper = project.read_text()
        self.assertIn('permalink: /projects/agoric-work-marketplace/', paper)
        self.assertIn('Concept and research proposal, not an implementation', paper)
        self.assertIn('Cashu', paper)
        self.assertIn('Archon', paper)
        self.assertIn('Nostr', paper)
        figure_paths = [
            'architecture.svg',
            'mission-graph.svg',
            'trust-graph.svg',
            'settlement.svg',
            'lifecycle.svg',
        ]
        for name in figure_paths:
            asset = ROOT / 'assets/agoric-work-marketplace' / name
            self.assertTrue(asset.is_file(), name)
            root = ET.parse(asset).getroot()
            self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg')
            self.assertEqual(root.attrib.get('role'), 'img')
            self.assertIn(name, paper)
        home = (ROOT / 'index.html').read_text()
        layout = (ROOT / '_layouts/default.html').read_text()
        self.assertIn('/projects/agoric-work-marketplace/', home)
        self.assertIn('/projects/agoric-work-marketplace/', layout)
        self.assertTrue((ROOT / 'assets/agoric-work-marketplace.css').is_file())
        self.assertIn('page.marketplace', layout)

    def test_marketplace_reputation_escrow_publication(self):
        import xml.etree.ElementTree as ET
        root = ROOT / 'projects/agoric-work-marketplace'
        paper = (root / 'README.md').read_text()
        escrow = (root / 'economic-accountability.md').read_text()
        assurance = (root / 'marketplace-assurance-patterns.md').read_text()
        self.assertIn('## 18. Economic Sybil resistance', paper)
        self.assertIn('## 19. Escrow and reputation', paper)
        self.assertIn('permalink: /projects/agoric-work-marketplace/economic-accountability.html', escrow)
        self.assertIn('permalink: /projects/agoric-work-marketplace/marketplace-assurance-patterns.html', assurance)
        self.assertIn('reputation', escrow.lower())
        self.assertIn('independent', assurance.lower())
        self.assertIn('reputation must never automatically', escrow.lower())
        self.assertIn('funds', assurance.lower())
        for name in (
            'reputation-feedback.svg',
            'fund-flows.svg',
            'escrow-outcomes.svg',
            'assurance-patterns.svg',
        ):
            path = ROOT / 'assets/agoric-work-marketplace' / name
            self.assertTrue(path.is_file(), name)
            drawing = ET.parse(path).getroot()
            self.assertEqual(drawing.tag, '{http://www.w3.org/2000/svg}svg')
            self.assertEqual(drawing.attrib.get('role'), 'img')
            self.assertTrue(any(name in source for source in (paper, escrow, assurance)))
        home = (ROOT / 'index.html').read_text()
        self.assertIn('economic-accountability.html', home)
        self.assertIn('marketplace-assurance-patterns.html', home)
        for name in ('economic-accountability.md', 'marketplace-assurance-patterns.md'):
            self.assertTrue((root / name).is_file())
        self.assertTrue((ROOT / 'PUBLISHING.md').is_file())

    def test_header_graphic_is_not_rendered(self):
        body = (ROOT / '_layouts/default.html').read_text()
        self.assertNotIn('class="hero-band"', body)
        self.assertNotIn('/hero.svg', body)
        self.assertIn('<header class="site-header">', body)
        self.assertIn('aria-label="Main navigation"', body)

    def test_lightning_goats_points_to_public_website(self):
        groups = yaml.safe_load((ROOT / '_data/projects.yml').read_text())
        projects = [item for group in groups for item in group['items']]
        goats = [item for item in projects if item['title'] == 'Lightning Goats']
        self.assertEqual(len(goats), 1)
        self.assertEqual(goats[0]['url'], 'https://lightning-goats.com')

    def test_nsec_oracle_is_listed_with_lnbits_work(self):
        groups = yaml.safe_load((ROOT / '_data/projects.yml').read_text())
        lnbits = next(group for group in groups if group['title'] == 'LNbits-related work')
        oracle = [item for item in lnbits['items'] if item['title'] == 'Nsec Oracle']
        self.assertEqual(len(oracle), 1)
        self.assertEqual(oracle[0]['url'], 'https://github.com/lightning-goats/nsec_oracle')
        self.assertTrue(oracle[0]['description'].strip())

    def test_original_twenty_research_documents(self):
        path = ROOT / '_data/research.yml'
        self.assertTrue(path.is_file())
        docs = yaml.safe_load(path.read_text())
        self.assertEqual(len(docs), 20)
        self.assertEqual(len({doc['file'] for doc in docs}), 20)
        self.assertTrue(all(doc['file'].endswith('.html') for doc in docs))

    def test_research_status_and_source_access(self):
        path = ROOT / '_layouts/default.html'
        self.assertTrue(path.is_file())
        body = path.read_text()
        self.assertIn('No experimental findings are claimed', body)
        self.assertIn('page.path', body)
        self.assertIn('research-guide.html', body)

if __name__ == '__main__': unittest.main()
