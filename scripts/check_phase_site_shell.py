#!/usr/bin/env python3
"""Validate the Phase 5 reusable public site shell shape."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'app/src/routes/+layout.svelte',
    'app/src/routes/+page.svelte',
    'app/src/lib/components/site/SiteShell.svelte',
    'app/src/lib/components/site/SiteNav.svelte',
    'app/src/lib/components/site/SiteFooter.svelte',
    'docs/specs/phase-005-spec.md',
    'docs/closures/phase-005-closure.md',
    'docs/goldens/phase-005.md',
]

FORBIDDEN_ROUTE_LINKS = [
    'href="/worlds"',
    'href="/characters"',
    'href="/artifacts"',
    'href="/stories"',
    'href="/timeline"',
]


def fail(message: str) -> int:
    print(f'[FAIL] {message}', file=sys.stderr)
    return 1


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def require_contains(path: str, needles: list[str]) -> int | None:
    content = read(path)
    for needle in needles:
        if needle not in content:
            return fail(f'{path} missing {needle!r}')
    return None



def require_phase_closed() -> int | None:
    progress = json.loads(read('docs/progress.json'))
    expected = {
        'last_completed_phase': 5,
        'next_candidate_phase': 6,
        'last_patch_id': 'phase-005-close-site-shell',
    }
    for key, value in expected.items():
        if progress.get(key) != value:
            return fail(f'docs/progress.json expected {key}={value!r}, got {progress.get(key)!r}')
    if progress.get('phase_status') not in {'ready', 'complete'}:
        return fail('docs/progress.json must mark the next phase ready after Phase 5 closes')

    closure = read('docs/closures/phase-005-closure.md')
    spec = read('docs/specs/phase-005-spec.md')
    golden = read('docs/goldens/phase-005.md')
    for path, content in [
        ('docs/closures/phase-005-closure.md', closure),
        ('docs/specs/phase-005-spec.md', spec),
        ('docs/goldens/phase-005.md', golden),
    ]:
        if 'Complete.' not in content:
            return fail(f'{path} must record complete status after Phase 5 closes')
        for forbidden in ['In progress.', 'Open.', 'Phase 5 is not closed yet']:
            if forbidden in content:
                return fail(f'{path} still contains open-phase marker {forbidden!r}')

    required_evidence = [
        'pnpm check',
        'pnpm build',
        'pnpm dev',
        'desktop/mobile `/` smoke',
        'professional CI',
    ]
    for needle in required_evidence:
        if needle not in closure and needle not in golden:
            return fail(f'Phase 5 closure/golden missing evidence marker {needle!r}')
    return None

def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        return fail('missing Phase 5 shell file(s): ' + ', '.join(missing))

    layout_result = require_contains(
        'app/src/routes/+layout.svelte',
        [
            "import '../app.css';",
            "import SiteShell from '$lib/components/site/SiteShell.svelte';",
            '<SiteShell>',
            '<slot />',
        ],
    )
    if layout_result is not None:
        return layout_result

    shell_result = require_contains(
        'app/src/lib/components/site/SiteShell.svelte',
        [
            "import SiteFooter from './SiteFooter.svelte';",
            "import SiteNav from './SiteNav.svelte';",
            '<SiteNav />',
            '<SiteFooter />',
            'id="main-content"',
            'Skip to main content',
            '<slot />',
            'max-w-6xl',
        ],
    )
    if shell_result is not None:
        return shell_result

    nav_result = require_contains(
        'app/src/lib/components/site/SiteNav.svelte',
        [
            'aria-label="Main navigation"',
            'href="/"',
            'aria-current="page"',
            'aria-disabled="true"',
            'plannedSections',
        ],
    )
    if nav_result is not None:
        return nav_result

    nav = read('app/src/lib/components/site/SiteNav.svelte')
    forbidden = [link for link in FORBIDDEN_ROUTE_LINKS if link in nav]
    if forbidden:
        return fail('Phase 5 nav must not link to unbuilt routes: ' + ', '.join(forbidden))

    footer_result = require_contains(
        'app/src/lib/components/site/SiteFooter.svelte',
        ['<footer', 'Public shell online', 'later phases'],
    )
    if footer_result is not None:
        return footer_result

    page = read('app/src/routes/+page.svelte')
    if '<main' in page or '</main>' in page:
        return fail('+page.svelte must not own the main landmark after Phase 5 shell')
    for needle in ['Phase 5 public shell online', 'Real landing content waits for Phase 6']:
        if needle not in page:
            return fail(f'+page.svelte missing shell placeholder proof {needle!r}')

    closed_result = require_phase_closed()
    if closed_result is not None:
        return closed_result

    print('[PASS] Phase 5 site shell artifacts verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
