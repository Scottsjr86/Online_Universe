#!/usr/bin/env python3
"""Validate Phase 8 environment configuration artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    '.env.example',
    'app/src/lib/server/env.ts',
    'app/src/hooks.server.ts',
    'app/src/app.d.ts',
    'app/vite.config.ts',
    'docs/dev/environment.md',
    'docs/specs/phase-008-spec.md',
    'docs/closures/phase-008-closure.md',
    'docs/goldens/phase-008.md',
]

REQUIRED_ENV_NAMES = [
    'DATABASE_URL',
    'SESSION_SECRET',
    'PUBLIC_SITE_NAME',
    'MEDIA_ROOT',
]


def fail(message: str) -> int:
    print(f'[FAIL] {message}', file=sys.stderr)
    return 1


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def require_env_example() -> int | None:
    text = read('.env.example')
    for name in REQUIRED_ENV_NAMES:
        if f'{name}=' not in text:
            return fail(f'.env.example missing {name}')
    if 'openssl rand -hex 32' not in text:
        return fail('.env.example must document URL-safe hex secret generation')
    if 'replace-with-url-safe-hex-password' not in text:
        return fail('.env.example must avoid real database credentials')
    if 'SESSION_SECRET=replace-with-64-hex-character-session-secret' not in text:
        return fail('.env.example must use an example session secret marker')
    if 'MEDIA_ROOT=/tmp/multiverse-codex-media' not in text:
        return fail('.env.example must include an absolute MEDIA_ROOT example')
    return None


def require_server_env_module() -> int | None:
    text = read('app/src/lib/server/env.ts')
    markers = [
        "import { env as privateEnv } from '$env/dynamic/private'",
        'EnvironmentConfigError',
        'RequiredEnvName',
        'ServerEnv',
        'getServerEnv',
        'validateServerEnv',
        'clearServerEnvCacheForTests',
        'DATABASE_URL',
        'SESSION_SECRET',
        'PUBLIC_SITE_NAME',
        'MEDIA_ROOT',
        'new URL(value)',
        'postgres:',
        'postgresql:',
        'SESSION_SECRET must be at least 32 characters long',
        'MEDIA_ROOT must be an absolute filesystem path',
        'path traversal',
    ]
    for marker in markers:
        if marker not in text:
            return fail(f'app/src/lib/server/env.ts missing marker {marker!r}')
    forbidden = ['process.env', 'TODO', 'FIXME']
    for marker in forbidden:
        if marker in text:
            return fail(f'app/src/lib/server/env.ts contains forbidden marker {marker!r}')
    return None


def require_hook_and_types() -> int | None:
    hook = read('app/src/hooks.server.ts')
    for marker in ['getServerEnv', 'EnvironmentConfigError', 'event.locals.env', 'throw error(500']:
        if marker not in hook:
            return fail(f'app/src/hooks.server.ts missing marker {marker!r}')
    app_types = read('app/src/app.d.ts')
    for marker in ['interface Locals', 'env: Readonly<{', 'databaseUrl: string', 'sessionSecret: string', 'publicSiteName: string', 'mediaRoot: string']:
        if marker not in app_types:
            return fail(f'app/src/app.d.ts missing marker {marker!r}')
    return None


def require_vite_env_dir() -> int | None:
    vite = read('app/vite.config.ts')
    if "envDir: '..'" not in vite:
        return fail("app/vite.config.ts must keep envDir: '..' so app commands read root .env")
    if 'plugins: [tailwindcss(), sveltekit()]' not in vite:
        return fail('app/vite.config.ts must preserve Tailwind before SvelteKit plugin order')
    return None


def require_docs_shape() -> int | None:
    docs = '\n'.join(
        read(path)
        for path in [
            'docs/dev/environment.md',
            'docs/specs/phase-008-spec.md',
            'docs/closures/phase-008-closure.md',
            'docs/goldens/phase-008.md',
        ]
    )
    for marker in [
        '.env.example',
        'app/src/lib/server/env.ts',
        'app/src/hooks.server.ts',
        'DATABASE_URL',
        'SESSION_SECRET',
        'PUBLIC_SITE_NAME',
        'MEDIA_ROOT',
        'openssl rand -hex 32',
        'pnpm check',
        'pnpm build',
        'pnpm dev',
        'professional CI',
    ]:
        if marker not in docs:
            return fail(f'Phase 8 docs missing marker {marker!r}')
    return None


def require_progress_state() -> int | None:
    progress = json.loads(read('docs/progress.json'))
    if progress.get('last_completed_phase') != 7:
        return fail('docs/progress.json must keep Phase 7 as last completed while Phase 8 is open')
    expected = {
        'current_phase': 8,
        'current_phase_title': 'Environment Configuration',
        'phase_status': 'in_progress',
        'next_candidate_phase': 8,
        'last_patch_id': 'phase-008-environment-config-start',
    }
    for key, value in expected.items():
        if progress.get(key) != value:
            return fail(f'docs/progress.json expected {key}={value!r}, got {progress.get(key)!r}')
    return None


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        return fail('missing Phase 8 environment file(s): ' + ', '.join(missing))

    checks = [
        require_env_example,
        require_server_env_module,
        require_hook_and_types,
        require_vite_env_dir,
        require_docs_shape,
        require_progress_state,
    ]
    for check in checks:
        result = check()
        if result is not None:
            return result

    print('[PASS] Phase 8 environment configuration artifacts verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
