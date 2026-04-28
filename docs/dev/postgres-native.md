# Native PostgreSQL development database

Phase 7 establishes the local PostgreSQL service path without Docker.

The scripts in this phase manage only the development database and role on the owner workstation. App environment files, SvelteKit database clients, ORM wiring, migrations, and schema tables belong to later phases.

## Defaults

```txt
Database: multiverse_codex_dev
Role:     multiverse_codex_app
Host:     127.0.0.1
Port:     5432
Service:  postgresql
```

Override with:

```bash
export MULTIVERSE_CODEX_DB_NAME=multiverse_codex_dev
export MULTIVERSE_CODEX_DB_USER=multiverse_codex_app
export MULTIVERSE_CODEX_DB_HOST=127.0.0.1
export MULTIVERSE_CODEX_DB_PORT=5432
export MULTIVERSE_CODEX_POSTGRES_SERVICE=postgresql
```

## Create or verify the local database

```bash
export MULTIVERSE_CODEX_DB_PASSWORD="$(openssl rand -base64 32)"
scripts/dev-db-create.sh
export DATABASE_URL="postgresql://multiverse_codex_app:${MULTIVERSE_CODEX_DB_PASSWORD}@127.0.0.1:5432/multiverse_codex_dev"
psql "$DATABASE_URL" -c 'select 1;'
scripts/dev-db-status.sh
```

`dev-db-create.sh` is idempotent for this phase. If the role already exists, the script updates the password for an existing role before validating the app-user connection. This fixes stale credential failures without requiring manual SQL.

## Dry runs

```bash
scripts/dev-db-create.sh --dry-run
scripts/dev-db-reset.sh --dry-run --yes
```

Dry runs validate arguments, required commands, identifier shape, password presence, and service state without mutating PostgreSQL.

## Reset the local database

Reset is destructive and requires `--yes`:

```bash
export MULTIVERSE_CODEX_DB_PASSWORD="$(openssl rand -base64 32)"
scripts/dev-db-reset.sh --yes
export DATABASE_URL="postgresql://multiverse_codex_app:${MULTIVERSE_CODEX_DB_PASSWORD}@127.0.0.1:5432/multiverse_codex_dev"
psql "$DATABASE_URL" -c 'select 1;'
scripts/dev-db-status.sh
```

The reset script drops only the configured development database, recreates it, updates or creates the configured app role, grants the public schema permissions needed for later migrations, and validates the app-user connection.

## Status

```bash
scripts/dev-db-status.sh
```

Status checks:

- PostgreSQL service is active
- app role exists
- database exists
- app-user connection works through `DATABASE_URL` or `MULTIVERSE_CODEX_DB_PASSWORD`

## Required privileges

The scripts use:

```txt
sudo -u postgres psql
```

On Kubuntu/Ubuntu, this matches the default native PostgreSQL administration path. If sudo prompts for your password, that is expected.

## Failure behavior

The scripts fail closed when:

- required commands are missing
- PostgreSQL service is inactive
- database or role names are invalid
- destructive reset lacks `--yes`
- app-user connection fails

No Docker, containers, app database client code, migrations, or `.env.example` files are created in Phase 7.
