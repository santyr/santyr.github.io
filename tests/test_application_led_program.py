"""Regression checks for the unified publication; no marketplace code executes."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MARKET = ROOT / 'projects/agoric-work-marketplace'
RESEARCH = ROOT / 'articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment'


class ApplicationLedPublicationTests(unittest.TestCase):
    def test_charter_and_evidence_are_distinct_from_results(self):
        charter = (MARKET / 'application-led-research.md').read_text()
        evidence = (MARKET / 'evidence.md').read_text()
        self.assertIn('The Marketplace Is the Experiment', charter)
        self.assertIn('application-led research program', charter)
        self.assertIn('No experimental findings are claimed', evidence)
        self.assertIn('No pilot reported', evidence)
        self.assertIn('Not conducted', evidence)
        for name in ('M0', 'M1', 'M2', 'M3', 'M4', 'M5'):
            self.assertIn(name, charter)
            self.assertIn(name, evidence)

    def test_homepage_is_thesis_system_evidence(self):
        home = (ROOT / 'index.html').read_text()
        for label in ('01 / THE THESIS', '02 / THE WORKING SYSTEM', '03 / THE EVIDENCE'):
            self.assertIn(label, home)
        for url in ('application-led-research.html', 'evidence.html', 'agoric-alignment-experiment/'):
            self.assertIn(url, home)
        self.assertNotIn('02 / THE TEST', home)
        self.assertNotIn('03 / THE APPLICATION', home)

    def test_marketplace_no_longer_requires_separate_programs(self):
        paper = (MARKET / 'README.md').read_text()
        self.assertIn('One application-led Agoric Alignment program', paper)
        self.assertNotIn('remain organizationally separate', paper)
        self.assertNotIn('own versioning, repositories, service boundaries', paper)
        self.assertIn('14-why-this-is-a-separate-agoric-alignment-project', paper)
        self.assertIn('fund-flows.svg', paper)
        self.assertIn('feasibility', (MARKET / 'application-led-research.md').read_text().lower())

    def test_delivery_documents_use_application_led_gates(self):
        for name in ('README.md', 'AGENTS.md', 'docs/11-stage-gates.md',
                     'docs/16-implementation-backlog.md', 'docs/18-agent-handoff.md'):
            with self.subTest(name=name):
                text = (RESEARCH / name).read_text()
                self.assertIn('M0', text)
                self.assertIn('M2', text)
                self.assertIn('M5', text)
        gates = (RESEARCH / 'docs/11-stage-gates.md').read_text()
        self.assertNotIn('## S0', gates)
        self.assertIn('All gates are pending', gates)
        backlog = (RESEARCH / 'docs/16-implementation-backlog.md').read_text()
        for package in ('AA-001', 'AA-007', 'AA-012'):
            self.assertIn(package, backlog)
        self.assertNotIn('Tasks 016–018 depend on 015', backlog)

    def test_field_methods_preserve_protection_and_identification(self):
        design = (RESEARCH / 'docs/03-experimental-design.md').read_text().lower()
        metrics = (RESEARCH / 'docs/09-metrics-and-analysis.md').read_text().lower()
        ethics = (RESEARCH / 'docs/10-security-and-ethics.md').read_text().lower()
        for term in ('interference', 'selection', 'independent', 'consent', 'feasibility'):
            self.assertIn(term, design)
        for term in ('intention-to-treat', 'subsid', 'newcomer', 'uncertain'):
            self.assertIn(term, metrics)
        self.assertIn('no unprotected control group', ethics)
        self.assertIn('earned compensation', ethics)
        self.assertIn('research', ethics)

    def test_all_nine_figures_are_valid_and_referenced(self):
        texts = '\n'.join(p.read_text() for p in MARKET.glob('*.md'))
        figures = ('architecture', 'mission-graph', 'trust-graph', 'settlement',
                   'lifecycle', 'reputation-feedback', 'fund-flows',
                   'escrow-outcomes', 'assurance-patterns')
        for name in figures:
            with self.subTest(name=name):
                path = ROOT / 'assets/agoric-work-marketplace' / (name + '.svg')
                drawing = ET.parse(path).getroot()
                self.assertEqual(drawing.attrib.get('role'), 'img')
                self.assertIsNotNone(drawing.find('{http://www.w3.org/2000/svg}title'))
                self.assertIsNotNone(drawing.find('{http://www.w3.org/2000/svg}desc'))
                self.assertIn(name + '.svg', texts)

    def test_shared_navigation_and_revision(self):
        layout = (ROOT / '_layouts/default.html').read_text()
        guide = (ROOT / '_includes/research-guide.html').read_text()
        self.assertIn('agoric-unified-20261024-r1', layout)
        self.assertIn('consciousness-20261018-r2', layout)
        self.assertIn('application-led-research.html', guide)
        self.assertIn('evidence.html', guide)
        self.assertIn('One application-led research program', layout)


if __name__ == '__main__':
    unittest.main()
