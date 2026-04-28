# Phase 7 Spec: Local Native PostgreSQL Foundation

## Phase

Phase 7: Local Native PostgreSQL Foundation

## Implemented behavior

Phase 7 adds source-controlled native PostgreSQL development database rails:

- `scripts/dev-db-common.sh` provides shared validation, service checks, superuser `psql` helpers, role/database existence checks, idempotent role/database creation, stale password repair, and app-user connection validation.
- `scripts/dev-db-create.sh` creates or verifies the configured local development database and role.
- `scripts/dev-db-reset.sh` requires `--yes`, drops only the configured development database, recreates it, repairs the app role password, and validates the app connection.
- `scripts/dev-db-status.sh` proves the PostgreSQL service, role, database, and app-user connection are usable.
- `docs/dev/postgres-native.md` documents the native workflow.
- `scripts/check_phase_postgres_native.py` verifies Phase 7 source artifacts and CI wiring.

## Public/admin routes touched

None.

## Domain modules touched

None.

## Data models touched

None. Phase 7 creates no schema tables and no migrations.

## Guards/seams added

- Docker is not used.
- Destructive reset requires `--yes`.
- Dry-run mode is available for create/reset checks.
- Database and role identifiers are validated before SQL execution.
- Existing role passwords are updated by the create/reset path so stale credentials fail less mysteriously.
- App-user connection is validated after create/reset.
- Phase 7 checks are wired into the professional CI lane.

## Tests/smokes added

- `bash -n scripts/dev-db-common.sh`
- `bash -n scripts/dev-db-create.sh`
- `bash -n scripts/dev-db-reset.sh`
- `bash -n scripts/dev-db-status.sh`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_postgres_native.py`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional`

## Handoff notes for next phase

Phase 7 remains open until the owner workstation proves:

```bash
export MULTIVERSE_CODEX_DB_PASSWORD="$(openssl rand -base64 32)"
scripts/dev-db-create.sh
export DATABASE_URL="postgresql://multiverse_codex_app:${MULTIVERSE_CODEX_DB_PASSWORD}@127.0.0.1:5432/multiverse_codex_dev"
psql "$DATABASE_URL" -c 'select 1;'
scripts/dev-db-status.sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

Phase 8 owns environment variable standardization. Phase 9 owns SvelteKit database connection code.
