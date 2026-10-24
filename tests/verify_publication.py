"""Audit generated HTML, or the deployed Pages site, without third-party packages."""
from __future__ import annotations
import argparse
import mimetypes
import re
import time
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen

ORIGIN = 'https://santyr.github.io'
REVISION = 'consciousness-20261018-r2'
COLLECTION = '/explorations/consciousness/'
ESSAY = COLLECTION + 'the-unreadable-language-of-perception.html'
FIGURES = ['perceptual-model', 'surface-anchoring', 'object-texture-repetition', 'symbol-meaning']

class Document(HTMLParser):
    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.refs: list[str] = []
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag in ('a', 'link') and attrs.get('href'):
            self.refs.append(attrs['href'])
        if tag in ('img', 'script', 'source') and attrs.get('src'):
            self.refs.append(attrs['src'])

class Audit:
    def __init__(self, directory: Path | None):
        self.directory = directory
        self.cache = {}
        self.html = {}
    def read(self, path: str):
        path = unquote(urlsplit(path).path) or '/'
        if path in self.cache:
            return self.cache[path]
        if self.directory:
            root = self.directory.resolve()
            file = (root / path.lstrip('/')).resolve()
            assert file.is_relative_to(root), f'Path leaves site root: {path}'
            if file.is_dir():
                file /= 'index.html'
            assert file.is_file(), f'Missing generated target: {path}'
            data = file.read_bytes()
            content_type = mimetypes.guess_type(str(file))[0] or ''
        else:
            req = Request(ORIGIN + path + '?publication-check=' + REVISION,
                          headers={'User-Agent': 'SatAntyr-Publication-Check/1.0', 'Cache-Control': 'no-cache'})
            with urlopen(req, timeout=25) as response:
                assert response.status == 200, f'HTTP {response.status}: {path}'
                data = response.read()
                content_type = response.headers.get_content_type()
        self.cache[path] = data, content_type
        if 'text/html' in content_type or path.endswith('.html') or path.endswith('/'):
            text = data.decode('utf-8')
            assert '<html' in text.lower(), f'Not an HTML page: {path}'
            assert 'Liquid Exception' not in text, f'Liquid error in {path}'
            assert not re.search(r'\{[{%]', text), f'Unrendered Liquid in {path}'
            self.html[path] = (text, Document(text))
        return self.cache[path]
    def run(self):
        for path in ['/', '/index.html', COLLECTION, COLLECTION + 'index.html', ESSAY]:
            self.read(path)
            assert REVISION in self.html[path][0], f'Stale or wrong page: {path}'
            print('VERIFIED', path, flush=True)
        if not self.directory:
            self.read(COLLECTION.rstrip('/'))
            print('VERIFIED slashless collection redirects/serves successfully', flush=True)
        home, home_doc = self.html['/']
        assert 'consciousness' in home_doc.ids, 'Homepage lacks consciousness section'
        assert home.index('class="all-projects"') < home.index('id="consciousness"'), 'Consciousness must follow all coding links'
        home_paths = {urlsplit(urljoin(ORIGIN, p)).path for p in home_doc.refs}
        assert COLLECTION in home_paths and ESSAY in home_paths, 'Homepage must link to collection AND essay'
        essay, essay_doc = self.html[ESSAY]
        assert '```' not in essay, 'ASCII/code fences remain in the essay'
        assert not any(tag == 'pre' for tag, _ in essay_doc.tags), 'Preformatted ASCII block remains'
        figures = [a for tag, a in essay_doc.tags if tag == 'figure' and 'research-figure' in a.get('class', '').split()]
        assert len(figures) == 4, f'Expected four figures, got {len(figures)}'
        for n in range(1,15):
            assert f'ref-{n}' in essay_doc.ids, f'Missing reference {n}'
        assert 'references-and-further-reading' in essay_doc.ids
        for name in FIGURES:
            path = '/assets/consciousness/' + name + '.svg'
            data, _ = self.read(path)
            svg = ET.fromstring(data)
            assert svg.find('{http://www.w3.org/2000/svg}title') is not None
            assert svg.find('{http://www.w3.org/2000/svg}desc') is not None
            print('VERIFIED GRAPHIC', path, flush=True)
        visited = set()
        edges = []
        while True:
            pending = [p for p in self.html if p not in visited]
            if not pending:
                break
            assert len(visited) < 500, 'Unexpected crawl size'
            for path in pending:
                visited.add(path)
                for ref in self.html[path][1].refs:
                    target = urlsplit(urljoin(ORIGIN + path, ref))
                    if target.scheme not in ('http','https') or target.netloc != urlsplit(ORIGIN).netloc:
                        continue
                    target_path = unquote(target.path) or '/'
                    self.read(target_path)
                    if target.fragment:
                        edges.append((path, target_path, unquote(target.fragment)))
        for source, target, fragment in edges:
            if target in self.html:
                assert fragment in self.html[target][1].ids, f'Broken anchor: {source} -> {target}#{fragment}'
        print(f'PASS: {len(visited)} HTML pages, {len(self.cache)} local resources, {len(edges)} fragment links; all reachable targets resolve.', flush=True)
        print('PASS: homepage -> consciousness collection -> essay, four SVG graphics, all 14 reference anchors, and code-first section order.', flush=True)
        print('Scope: external publisher and repository availability is not asserted by this internal-link audit.', flush=True)
        # The existing workflow calls this verifier for both built and public pages.
        # Import only after core checks; the extra audit reads but never recurses into run().
        from verify_application_led import verify
        verify(self.directory)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, help='Generated Jekyll directory; omit for live checks')
    parser.add_argument('--attempts', type=int, default=1)
    args = parser.parse_args()
    for attempt in range(args.attempts):
        try:
            Audit(args.site).run()
            return
        except Exception as exc:
            print(f'Attempt {attempt+1}/{args.attempts}: {type(exc).__name__}: {exc}', flush=True)
            if attempt + 1 == args.attempts:
                raise
            time.sleep(15)
if __name__ == '__main__':
    main()
