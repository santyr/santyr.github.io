"""Fail early on malformed YAML that Jekyll otherwise warns about and ignores."""
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


class FrontMatterTests(unittest.TestCase):
    def test_publication_frontmatter_is_valid_yaml(self):
        paths = list(ROOT.glob('*.html')) + list(ROOT.glob('*.md'))
        for directory in ('projects', 'articles', 'explorations'):
            paths.extend((ROOT / directory).rglob('*.md'))
        for path in paths:
            text = path.read_text(encoding='utf-8')
            if not text.startswith('---\n'):
                continue
            with self.subTest(path=str(path.relative_to(ROOT))):
                parts = text.split('\n---', 1)
                self.assertEqual(len(parts), 2, 'Unterminated front matter')
                metadata = yaml.safe_load(parts[0][4:])
                self.assertIsInstance(metadata, dict)
                if 'description' in metadata:
                    self.assertIsInstance(metadata['description'], str)


if __name__ == '__main__':
    unittest.main()
