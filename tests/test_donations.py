"""Donation destination / layout regressions; no requests or payments."""
from pathlib import Path
import hashlib
import unittest
import yaml
ROOT = Path(__file__).resolve().parents[1]
ADDRESS = 'sat@lightning-goats.com'
ENDPOINT = 'https://lightning-goats.com/.well-known/lnurlp/sat'

class DonationTests(unittest.TestCase):
    def read(self, name):
        self.assertTrue((ROOT / name).is_file(), f'Missing donation asset: {name}')
        return (ROOT / name).read_text()

    def config(self):
        return yaml.safe_load(self.read('_data/donations.yml'))

    def test_recipient_and_lnurl_checksum(self):
        data = self.config()
        self.assertEqual(data['address'], ADDRESS)
        self.assertEqual(data['endpoint'], ENDPOINT)
        encoded = data['lnurl'].lower()
        self.assertTrue(encoded.startswith('lnurl1'))
        charset = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'
        words = [charset.index(c) for c in encoded[6:]]
        values = [ord(c) >> 5 for c in 'lnurl'] + [0] + [ord(c) & 31 for c in 'lnurl'] + words
        check = 1
        for value in values:
            top = check >> 25
            check = ((check & 0x1ffffff) << 5) ^ value
            for i, generator in enumerate([0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3]):
                if (top >> i) & 1:
                    check ^= generator
        self.assertEqual(check, 1, 'Invalid bech32 checksum')
        bits = ''.join(f'{word:05b}' for word in words[:-6])
        padding = len(bits) % 8
        if padding:
            self.assertEqual(set(bits[-padding:]), {'0'})
        decoded = bytes(int(bits[i:i+8],2) for i in range(0,len(bits)-7,8)).decode()
        self.assertEqual(decoded, ENDPOINT)

    def test_donation_links_and_qr_share_configured_destination(self):
        body = self.read('_includes/donations.html')
        self.assertGreaterEqual(body.count('href="lightning:{{ donation.lnurl | escape }}"'), 3)
        self.assertIn('data-donation-link', body)
        self.assertIn('{{ donation.address | escape }}', body)
        self.assertIn('{{ donation.qr_path | relative_url }}', body)
        self.assertIn('aria-label=', body)
        self.assertIn('role="status"', body)
        self.assertNotIn('mailto:', body)
        self.assertNotIn('bolverker.com', body)

    def test_qr_file_is_pinned_to_verified_asset(self):
        data = self.config()
        path = ROOT / data['qr_path'].lstrip('/')
        self.assertTrue(path.is_file())
        self.assertTrue(path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), data['qr_sha256'])

    def test_sitewide_support_follows_content(self):
        layout = self.read('_layouts/default.html')
        self.assertEqual(layout.count('include donations.html'), 1)
        self.assertLess(layout.index('include related-work.html'),layout.index('include donations.html'))
        self.assertLess(layout.index('include donations.html'),layout.index('<footer'))
        self.assertIn('href="#support"', layout)
        self.assertIn('name="lightning" content="lnurlp:{{ site.data.donations.address | escape }}"', layout)
        self.assertIn("'/assets/donations.js' | relative_url", layout)
        self.assertIn('defer', layout)
        self.assertNotIn('hero-band', layout)

    def test_wallet_integration_is_local_and_user_initiated(self):
        body = self.read('assets/donations.js')
        for forbidden in ['fetch(', 'localStorage', 'sessionStorage', 'sendPayment(', 'makeInvoice(', 'innerHTML', 'console.log']:
            self.assertNotIn(forbidden, body)
        self.assertIn('provider.enable()', body)
        self.assertIn('provider.lnurl(', body)

if __name__ == '__main__':
    unittest.main()
