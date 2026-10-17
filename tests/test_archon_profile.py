"""Documentation/configuration consistency only; no SDK import, network or signing."""
from pathlib import Path
import json
import unittest
ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / 'articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment'

class ArchonProfileTests(unittest.TestCase):
    def profile(self):
        return json.loads((EXPERIMENT / 'configs/archon-4tress.json').read_text())

    def test_selected_client_and_endpoint(self):
        p = self.profile()
        self.assertEqual(p['node_url'], 'https://4tress.org')
        self.assertEqual(p['adapter'], 'archon-keymaster')
        self.assertEqual(p['client_distribution'], 'archon-keymaster')
        self.assertEqual(p['python_requirement'], '>=3.12')
        self.assertEqual(p['client_source_revision'], '0a6ecf574a6a35175471a3342e30936336f37df6')
        self.assertEqual(p['client_source_subdirectory'], 'python/keymaster')

    def test_profile_is_disabled_bounded_and_not_a_bitcoin_claim(self):
        p = self.profile()
        for field in ['enabled', 'network_access', 'allow_writes', 'allow_payments']:
            self.assertIs(p[field], False)
        self.assertEqual(p['requested_registry'], 'hyperswarm')
        self.assertEqual(p['live_preflight_status'], 'not_verified')
        self.assertEqual(p['max_write_retries'], 0)
        self.assertEqual(p['max_concurrent_requests'], 1)
        self.assertLessEqual(p['max_total_requests'], 25)
        self.assertTrue(p['wallet_root'].startswith('runs/private/'))

    def test_execution_guides_use_selected_interface(self):
        paths = ['README.md', 'AGENTS.md', 'docs/05-architecture.md', 'docs/10-security-and-ethics.md', 'docs/11-stage-gates.md', 'docs/12-archon-integration.md', 'docs/13-operations.md', 'docs/16-implementation-backlog.md', 'docs/18-agent-handoff.md']
        for path in paths:
            with self.subTest(path=path):
                body = (EXPERIMENT / path).read_text()
                self.assertIn('4tress', body)
                self.assertIn('archon-keymaster', body)

    def test_schema_covers_profile_and_remote_manifest(self):
        p = self.profile()
        schema = json.loads((EXPERIMENT / 'schemas/archon-profile.schema.json').read_text())
        self.assertEqual(set(p), set(schema['required']))
        self.assertEqual(set(p), set(schema['properties']))
        self.assertEqual(schema['properties']['allow_payments']['const'], False)
        manifest = json.loads((EXPERIMENT / 'schemas/run-manifest.schema.json').read_text())
        self.assertIn('archon-remote', manifest['properties']['adapter_mode']['enum'])
        self.assertIn('1.1', manifest['properties']['manifest_version']['enum'])
        self.assertIn('archon_interface', manifest['properties'])
        self.assertTrue(manifest['allOf'])

    def test_original_offline_configs_stay_offline(self):
        for name in ['mini.json', 'pilot.json']:
            config = json.loads((EXPERIMENT / 'configs' / name).read_text())
            self.assertEqual(config['mode'], 'offline')
            self.assertIs(config['network_access'], False)
            self.assertIs(config['use_real_funds'], False)

if __name__ == '__main__':
    unittest.main()
