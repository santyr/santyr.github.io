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
