#!/usr/bin/env python3
"""Validate the Phase 6 static landing page shape and closure drift."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'app/src/routes/+page.svelte',
    'docs/specs/phase-006-spec.md',
    'docs/closures/phase-006-closure.md',
    'docs/goldens/phase-006.md',
]

REQUIRED_PAGE_MARKERS = [
    'Phase 6 landing signal online',
    'id="hero-title"',
    'Universe teaser',
    'Featured worlds placeholder',
    'Featured characters placeholder',
    'Call to action into the codex',
    'id="codex-preview"',
    'id="launch-path"',
    'featuredWorlds',
    'featuredCharacters',
    'signalPillars',
]

FORBIDDEN_MARKERS = [
    'Phase 5 public shell online',
    'Real landing content waits for Phase 6',
    'href="/worlds"',
    'href="/characters"',
    'href="/artifacts"',
    'href="/stories"',
    'href="/timeline"',
    '<main',
    '</main>',
]


def fail(message: str) -> int:
    print(f'[FAIL] {message}', file=sys.stderr)
    return 1


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def require_page_shape() -> int | None:
    page = read('app/src/routes/+page.svelte')
    for marker in REQUIRED_PAGE_MARKERS:
        if marker not in page:
            return fail(f'app/src/routes/+page.svelte missing {marker!r}')
    for marker in FORBIDDEN_MARKERS:
        if marker in page:
            return fail(f'app/src/routes/+page.svelte contains forbidden marker {marker!r}')
    if page.count('<section') < 5:
        return fail('landing page must expose at least five sections')
    if page.count('<h2') < 4:
        return fail('landing page must expose section headings for teaser/worlds/characters/CTA')
    if 'svelte:head' not in page or 'meta\n    name="description"' not in page:
        return fail('landing page must define title and description metadata')
    return None


def require_docs_shape() -> int | None:
    progress = json.loads(read('docs/progress.json'))
    if progress.get('last_completed_phase', -1) < 6:
        return fail('docs/progress.json must keep Phase 6 in the completed ladder')

    current_phase = progress.get('current_phase', 0)
    if current_phase <= 6:
        expected = {
            'current_phase': 6,
            'current_phase_title': 'Static Landing Page',
            'phase_status': 'complete',
            'last_completed_phase': 6,
            'next_candidate_phase': 7,
            'last_patch_id': 'phase-006-close-static-landing',
        }
        for key, value in expected.items():
            if progress.get(key) != value:
                return fail(f'docs/progress.json expected {key}={value!r}, got {progress.get(key)!r}')
    elif progress.get('current_phase', 0) > 6 and progress.get('next_candidate_phase', 0) < 7:
        return fail('docs/progress.json regressed below the Phase 7 handoff')

    closure = read('docs/closures/phase-006-closure.md')
    spec = read('docs/specs/phase-006-spec.md')
    golden = read('docs/goldens/phase-006.md')
    docs = '\n'.join([closure, spec, golden])
    required_doc_markers = [
        'hero',
        'universe teaser',
        'featured worlds placeholder',
        'featured characters placeholder',
        'call-to-action',
        'No database',
        'professional CI',
        'pnpm check',
        'pnpm build',
        'pnpm dev',
        'desktop/mobile `/` smoke',
    ]
    for marker in required_doc_markers:
        if marker not in docs:
            return fail(f'Phase 6 docs missing marker {marker!r}')

    for path, content in [
        ('docs/closures/phase-006-closure.md', closure),
        ('docs/specs/phase-006-spec.md', spec),
        ('docs/goldens/phase-006.md', golden),
    ]:
        if 'Complete.' not in content:
            return fail(f'{path} must record complete status after Phase 6 closes')
        for forbidden in ['In progress.', 'Not closed.', 'Phase 6 is open', 'pending owner run']:
            if forbidden in content:
                return fail(f'{path} still contains open-phase marker {forbidden!r}')
    return None


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        return fail('missing Phase 6 landing file(s): ' + ', '.join(missing))

    page_result = require_page_shape()
    if page_result is not None:
        return page_result
    docs_result = require_docs_shape()
    if docs_result is not None:
        return docs_result

    print('[PASS] Phase 6 static landing page artifacts verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
