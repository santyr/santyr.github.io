"""Regression tests for directory routing and the illustrated essay."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ESSAY = ROOT / 'explorations/consciousness/the-unreadable-language-of-perception.md'

class ConsciousnessRepairTests(unittest.TestCase):
    def test_collection_has_explicit_directory_permalink(self):
        text = (ROOT / 'explorations/consciousness/README.md').read_text()
        self.assertIn('permalink: /explorations/consciousness/', text)

    def test_ascii_diagrams_are_replaced_by_four_accessible_graphics(self):
        text = ESSAY.read_text()
        self.assertNotRegex(text, r'(?m)^```')
        self.assertEqual(text.count('<figure '), 4)
        for name in ['perceptual-model','surface-anchoring','object-texture-repetition','symbol-meaning']:
            self.assertIn(name + '.svg', text)
            file = ROOT / 'assets/consciousness' / (name + '.svg')
            self.assertTrue(file.is_file(), str(file))
            svg = ET.parse(file).getroot()
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}title'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}desc'))

    def test_hypothesis_summary_precede_body_and_references_are_linked(self):
        text = ESSAY.read_text()
        self.assertLess(text.index('## Working hypothesis'), text.index('## Summary'))
        self.assertLess(text.index('## Summary'), text.index('## 1.'))
        for n in range(1,15):
            self.assertIn(f'id="ref-{n}"', text)
            self.assertIn(f'](#ref-{n})', text)
        self.assertIn('id="references-and-further-reading"', text)

if __name__ == '__main__':
    unittest.main()
