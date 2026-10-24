"""Check the generated or deployed unified Agoric Alignment publication."""
from __future__ import annotations
import argparse
import time
from pathlib import Path
import verify_publication as publication

REVISION = 'agoric-unified-20261024-r1'
MARKET = '/projects/agoric-work-marketplace/'
RESEARCH = '/articles/bitcoin-alignment-of-autonomous-agents/agoric-alignment-experiment/'


def verify(directory: Path | None) -> None:
    # Reuse the existing HTML/Liquid/HTTP checks, with a revision-specific request.
    publication.REVISION = REVISION
    audit = publication.Audit(directory)
    expected = {
        '/': ('01 / THE THESIS', '02 / THE WORKING SYSTEM', '03 / THE EVIDENCE'),
        MARKET: ('One application-led Agoric Alignment program', 'fund-flows.svg'),
        MARKET + 'application-led-research.html': ('The Marketplace Is the Experiment', 'M0', 'M5'),
        MARKET + 'evidence.html': ('No pilot reported', 'Not conducted', 'No experimental findings are claimed'),
        MARKET + 'economic-accountability.html': ('Reputation-Backed Escrow', 'unified charter'),
        MARKET + 'marketplace-assurance-patterns.html': ('Marketplace Assurance Patterns', 'unified charter'),
        RESEARCH: ('Research and Evaluation', 'M0', 'M5'),
        RESEARCH + 'AGENTS.html': ('Coding-agent instructions', 'M0', 'M2'),
        RESEARCH + 'docs/03-experimental-design.html': ('Real-world experimental design', 'spillovers'),
        RESEARCH + 'docs/11-stage-gates.html': ('M0', 'M5', 'All gates are pending'),
        RESEARCH + 'docs/16-implementation-backlog.html': ('AA-001', 'AA-007', 'AA-012'),
        RESEARCH + 'docs/18-agent-handoff.html': ('Unified application-led', 'M0', 'M2'),
    }
    for path, markers in expected.items():
        audit.read(path)
        html = audit.html[path][0]
        assert REVISION in html, f'Stale program revision: {path}'
        for marker in markers:
            assert marker in html, f'Missing {marker!r} at {path}'
        assert 'remain organizationally separate' not in html, f'Obsolete separation: {path}'
        print('VERIFIED AGORIC', path, flush=True)
    print(f'PASS: {len(expected)} unified-program pages and expected revision.', flush=True)
    print('Scope: publication integrity only; no market, payment or research claim is verified.', flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path)
    parser.add_argument('--attempts', type=int, default=1)
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error('--attempts must be positive')
    for attempt in range(args.attempts):
        try:
            verify(args.site)
            return
        except Exception as exc:
            print(f'Attempt {attempt + 1}/{args.attempts}: {type(exc).__name__}: {exc}', flush=True)
            if attempt + 1 == args.attempts:
                raise
            time.sleep(15)


if __name__ == '__main__':
    main()
