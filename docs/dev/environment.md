# Environment Configuration

Phase 8 standardizes the required local environment variables for the SvelteKit app.
The canonical example file lives at the repository root:

```txt
.env.example
```

Copy it before running the app:

```bash
cp .env.example .env
```

Then edit `.env` and replace every example value.

## Required variables

| Name | Required shape | Purpose |
| --- | --- | --- |
| `DATABASE_URL` | `postgresql://` or `postgres://` URL with host and database name | Native PostgreSQL dev database from Phase 7. |
| `SESSION_SECRET` | At least 32 characters, generated with `openssl rand -hex 32` | Future server-side session signing material. |
| `PUBLIC_SITE_NAME` | Non-empty, 80 characters or fewer | Site name used by server config and later metadata. |
| `MEDIA_ROOT` | Absolute filesystem path with no `..` path traversal segments | Reserved media root for later media phases. |

## Generate safe local values

Use URL-safe hex for password and secret material:

```bash
export MULTIVERSE_CODEX_DB_PASSWORD="$(openssl rand -hex 32)"
scripts/dev-db-create.sh
```

Create `.env` with matching values:

```bash
cat > .env <<EOF_ENV
DATABASE_URL=postgresql://multiverse_codex_app:${MULTIVERSE_CODEX_DB_PASSWORD}@127.0.0.1:5432/multiverse_codex_dev
SESSION_SECRET=$(openssl rand -hex 32)
PUBLIC_SITE_NAME=Multiverse Codex
MEDIA_ROOT=/tmp/multiverse-codex-media
EOF_ENV
```

The app is configured with an absolute repo-root `envDir` in `app/vite.config.ts`, so SvelteKit commands run from `app/` read the root `.env` file.


`PUBLIC_SITE_NAME` intentionally uses the public prefix. The server validator reads it from `$env/dynamic/public`, while private values such as `DATABASE_URL`, `SESSION_SECRET`, and `MEDIA_ROOT` are read from `$env/dynamic/private`.

Copying `.env.example` unchanged is expected to fail. Replace `replace-with-url-safe-hex-password` and `replace-with-64-hex-character-session-secret` before treating the valid-env smoke as green.

## Validation behavior

Server-side code validates environment variables in:

```txt
app/src/lib/server/env.ts
app/src/hooks.server.ts
```

Validation runs at the server request boundary. Missing or malformed values fail closed with an `EnvironmentConfigError` message instead of letting later phases fail deep inside database, auth, or media code.

The validator checks:

- every required variable exists and is non-empty
- `DATABASE_URL` is a valid PostgreSQL URL
- `SESSION_SECRET` is long enough and no longer contains the example marker
- `PUBLIC_SITE_NAME` is bounded
- `MEDIA_ROOT` is absolute and does not contain traversal segments

## Smoke checks

Valid environment:

```bash
cd app
pnpm check
pnpm build
pnpm dev
```

Then browse `/` or run a local request against the dev server. The page should render normally.

Missing environment failure:

```bash
mv ../.env ../.env.phase8-smoke
pnpm dev
# Browse / and confirm the server fails clearly with a missing required environment variable message.
mv ../.env.phase8-smoke ../.env
```

Repo close gate:

```bash
cd ..
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

## Troubleshooting

- If `DATABASE_URL` parsing fails, regenerate URL-safe material with `openssl rand -hex 32`.
- If SvelteKit cannot see `.env`, confirm `app/vite.config.ts` still contains `envDir: '..'`.
- If `SESSION_SECRET` fails validation, replace the example value with a real generated value.
- If `MEDIA_ROOT` fails validation, use an absolute path such as `/tmp/multiverse-codex-media`.
