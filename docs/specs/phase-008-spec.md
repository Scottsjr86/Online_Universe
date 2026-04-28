# Phase 8 Spec: Environment Configuration

## Phase

Phase 8: Environment Configuration

## Implemented behavior

Phase 8 starts environment standardization for the SvelteKit app:

- `.env.example` defines the required variables: `DATABASE_URL`, `SESSION_SECRET`, `PUBLIC_SITE_NAME`, and `MEDIA_ROOT`.
- `app/vite.config.ts` sets `envDir: '..'` so app commands run from `app/` read the repository-root `.env` file.
- `app/src/lib/server/env.ts` centralizes server-only environment parsing and validation.
- `app/src/hooks.server.ts` validates environment configuration at the request boundary and stores the parsed config on `event.locals.env`.
- `app/src/app.d.ts` types `event.locals.env` with a read-only parsed environment shape.
- `docs/dev/environment.md` documents valid local values, root `.env` loading, missing-env failure checks, and troubleshooting.
- `scripts/check_phase_environment.py` verifies Phase 8 source artifacts and CI wiring.

Phase 8 is currently open until owner workstation proof records valid `.env`, missing-env failure, app check/build/dev, and professional CI.

## Public/admin routes touched

No public or admin route files were added. Existing routes now run behind the server hook environment guard.

## Domain modules touched

None.

## Data models touched

None. Phase 8 creates no database client, no schema tables, and no migrations.

## Guards/seams added

- Environment validation is server-owned in `app/src/lib/server/env.ts`.
- Required variables fail closed when missing or empty.
- `DATABASE_URL` must parse as a PostgreSQL URL with host and database name.
- `SESSION_SECRET` must be at least 32 characters and cannot keep the example marker.
- `PUBLIC_SITE_NAME` is bounded to 80 characters.
- `MEDIA_ROOT` must be an absolute path and must not contain traversal segments.
- `hooks.server.ts` performs the request-boundary guard before route rendering.
- `event.locals.env` is typed for later server code handoff.

## Tests/smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_environment.py`
- Professional CI now requires Phase 8 environment artifacts and runs the Phase 8 validator.

## Handoff notes for next phase

Phase 9 owns the real SvelteKit database connection, pg driver, Drizzle ORM, and database client module. Phase 8 only validates and exposes environment configuration.
