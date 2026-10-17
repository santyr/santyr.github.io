# Donation integration checks

The site receives at `sat@lightning-goats.com`. The address, clickable QR and primary donation button all resolve the same LNURL-pay endpoint: `https://lightning-goats.com/.well-known/lnurlp/sat`.

`_data/donations.yml` contains public receiving details only. Its uppercase Bech32 LNURL is encoded in `assets/donation-qr.png`; it is not an expiring invoice. QR changes require independently decoding the image, checking the Bech32 checksum and exact endpoint, and updating the pinned image SHA-256. The uploaded QR was replaced with the user's approval because it identified a different receiving domain. No private keys or wallet API credentials are needed or stored by this site.

## Progressive enhancement

Ordinary `lightning:` links and the QR work without JavaScript. The Lightning meta tag advertises the recipient to Alby. When available, WebLN `enable()` followed by optional `lnurl(address)` lets the wallet handle the amount, invoice verification and payment confirmation. Without that optional API the real wallet link remains active. The separate "Open another wallet" link always remains a native link.

Permission denial or an ambiguous result never triggers automatic retries or an unqualified payment-success message. Duplicate clicks are guarded. Copy-to-clipboard has a manual-copy fallback, and the address remains selectable. No provider is contacted on page load; no third-party scripts, invoice proxies, trackers, payment logs or stored payer identifiers are used.

## Tests

```sh
python -m unittest discover -s tests -v
node --test tests/test_donations.cjs
```

Python tests use the existing PyYAML publication dependency. JavaScript tests use Node's standard library and mocked wallet/DOM boundaries: they execute the real script but cannot send money. A payment result is a wallet report, not server-side receipt verification. Also independently decode the QR and inspect desktop/mobile layouts. A live end-to-end payment is a manual test by an authorized payer; no live donation was sent during development.

References: [WebLN lnurl](https://www.webln.guide/building-lightning-apps/webln-reference/webln.lnurl), [LUD-01](https://github.com/lnurl/luds/blob/luds/01.md), [LUD-16](https://github.com/lnurl/luds/blob/luds/16.md).
