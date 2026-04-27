#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'app/package.json',
    'app/vite.config.ts',
    'app/postcss.config.js',
    'app/tailwind.config.js',
    'app/src/app.css',
    'app/src/routes/+layout.svelte',
    'app/src/routes/+page.svelte',
    'docs/design/theme.md',
    'app/pnpm-lock.yaml',
]

REQUIRED_DEV_DEPS = ['@tailwindcss/vite', 'postcss', 'tailwindcss']


def fail(message: str) -> int:
    print(f'[FAIL] {message}', file=sys.stderr)
    return 1


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        return fail('missing required Phase 4 file(s): ' + ', '.join(missing))

    package = json.loads(read('app/package.json'))
    dev_deps = package.get('devDependencies', {})
    missing_deps = [dep for dep in REQUIRED_DEV_DEPS if dep not in dev_deps]
    if missing_deps:
        return fail('missing Tailwind/PostCSS dev dependency/dependencies: ' + ', '.join(missing_deps))

    lockfile = read('app/pnpm-lock.yaml')
    missing_locked_deps = [dep for dep in REQUIRED_DEV_DEPS if dep not in lockfile]
    if missing_locked_deps:
        return fail('app/pnpm-lock.yaml missing Tailwind/PostCSS dependency/dependencies: ' + ', '.join(missing_locked_deps))

    vite_config = read('app/vite.config.ts')
    if "@tailwindcss/vite" not in vite_config or 'tailwindcss()' not in vite_config:
        return fail('Vite config does not load the TailwindCSS Vite plugin')
    if 'plugins: [tailwindcss(), sveltekit()]' not in vite_config.replace('\n', ' '):
        return fail('Vite plugin order must keep tailwindcss() before sveltekit()')

    app_css = read('app/src/app.css')
    for needle in ['@import', 'tailwindcss', '@theme', '--color-codex-void', '@layer base']:
        if needle not in app_css:
            return fail(f'app/src/app.css missing {needle!r}')

    layout = read('app/src/routes/+layout.svelte')
    if "import '../app.css';" not in layout:
        return fail('+layout.svelte must import ../app.css')
    if '<slot />' not in layout:
        return fail('+layout.svelte must render the route slot')

    page = read('app/src/routes/+page.svelte')
    if '<style' in page:
        return fail('Phase 4 scaffold page must use Tailwind utilities, not component-local CSS')
    for needle in ['class=', 'text-codex-cyan', 'rounded-codex', 'shadow-codex']:
        if needle not in page:
            return fail(f'+page.svelte missing Tailwind proof token {needle!r}')

    theme_doc = read('docs/design/theme.md')
    for needle in ['TailwindCSS', 'PostCSS', 'Initial tokens', 'Scope boundary']:
        if needle not in theme_doc:
            return fail(f'theme doc missing {needle!r}')

    print('[PASS] Phase 4 Tailwind setup artifacts verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
