#!/usr/bin/env bash
# Shared helpers for Multiverse Codex native PostgreSQL dev database scripts.

set -Eeuo pipefail

MC_DB_NAME="${MULTIVERSE_CODEX_DB_NAME:-multiverse_codex_dev}"
MC_DB_USER="${MULTIVERSE_CODEX_DB_USER:-multiverse_codex_app}"
MC_DB_HOST="${MULTIVERSE_CODEX_DB_HOST:-127.0.0.1}"
MC_DB_PORT="${MULTIVERSE_CODEX_DB_PORT:-5432}"
MC_POSTGRES_SERVICE="${MULTIVERSE_CODEX_POSTGRES_SERVICE:-postgresql}"

mc_log() {
  printf '[%s] %s\n' "$1" "$2"
}

mc_fail() {
  mc_log FAIL "$1" >&2
  exit "${2:-1}"
}

mc_need_command() {
  command -v "$1" >/dev/null 2>&1 || mc_fail "required command not found: $1" 127
}

mc_validate_identifier() {
  local label="$1"
  local value="$2"
  if [[ ! "$value" =~ ^[a-z_][a-z0-9_]{0,62}$ ]]; then
    mc_fail "$label must match ^[a-z_][a-z0-9_]{0,62}$, got: $value" 2
  fi
}

mc_require_url_safe_password() {
  if [[ ! "${MULTIVERSE_CODEX_DB_PASSWORD}" =~ ^[A-Za-z0-9._~-]+$ ]]; then
    mc_fail "MULTIVERSE_CODEX_DB_PASSWORD must be URL-safe for DATABASE_URL usage; generate one with: openssl rand -hex 32" 2
  fi
}

mc_require_password() {
  if [[ -z "${MULTIVERSE_CODEX_DB_PASSWORD:-}" ]]; then
    mc_fail "set MULTIVERSE_CODEX_DB_PASSWORD before running this command" 2
  fi
  mc_require_url_safe_password
}

mc_sql_literal() {
  local value="$1"
  value=${value//\'/\'\'}
  printf "'%s'" "$value"
}

mc_super_psql() {
  mc_need_command sudo
  mc_need_command psql
  sudo -u postgres psql -v ON_ERROR_STOP=1 "$@"
}

mc_is_postgres_active() {
  systemctl is-active --quiet "$MC_POSTGRES_SERVICE"
}

mc_require_postgres_active() {
  mc_need_command systemctl
  if ! mc_is_postgres_active; then
    mc_fail "PostgreSQL service is not active: $MC_POSTGRES_SERVICE" 3
  fi
}

mc_connection_url() {
  printf 'postgresql://%s:%s@%s:%s/%s' \
    "$MC_DB_USER" \
    "$MULTIVERSE_CODEX_DB_PASSWORD" \
    "$MC_DB_HOST" \
    "$MC_DB_PORT" \
    "$MC_DB_NAME"
}

mc_masked_connection_url() {
  printf 'postgresql://%s:***@%s:%s/%s' \
    "$MC_DB_USER" \
    "$MC_DB_HOST" \
    "$MC_DB_PORT" \
    "$MC_DB_NAME"
}

mc_role_exists() {
  local role_literal
  role_literal=$(mc_sql_literal "$MC_DB_USER")
  [[ "$(mc_super_psql -At -c "select 1 from pg_roles where rolname = $role_literal;")" == "1" ]]
}

mc_database_exists() {
  local db_literal
  db_literal=$(mc_sql_literal "$MC_DB_NAME")
  [[ "$(mc_super_psql -At -c "select 1 from pg_database where datname = $db_literal;")" == "1" ]]
}

mc_apply_role_and_database() {
  local password_literal
  password_literal=$(mc_sql_literal "$MULTIVERSE_CODEX_DB_PASSWORD")

  if mc_role_exists; then
    mc_log INFO "updating password for existing role $MC_DB_USER"
    mc_super_psql -c "alter role \"$MC_DB_USER\" with login password $password_literal;" >/dev/null
  else
    mc_log INFO "creating role $MC_DB_USER"
    mc_super_psql -c "create role \"$MC_DB_USER\" with login password $password_literal;" >/dev/null
  fi

  if mc_database_exists; then
    mc_log INFO "database exists: $MC_DB_NAME"
    mc_super_psql -c "alter database \"$MC_DB_NAME\" owner to \"$MC_DB_USER\";" >/dev/null
  else
    mc_log INFO "creating database $MC_DB_NAME owned by $MC_DB_USER"
    mc_super_psql -c "create database \"$MC_DB_NAME\" owner \"$MC_DB_USER\";" >/dev/null
  fi

  mc_super_psql -d "$MC_DB_NAME" -c "grant all privileges on database \"$MC_DB_NAME\" to \"$MC_DB_USER\";" >/dev/null
  mc_super_psql -d "$MC_DB_NAME" -c "grant usage, create on schema public to \"$MC_DB_USER\";" >/dev/null
}

mc_test_app_connection() {
  local url
  url="$(mc_connection_url)"
  psql "$url" -v ON_ERROR_STOP=1 -c 'select 1;' >/dev/null
}

mc_parse_dry_run_flag() {
  DRY_RUN=0
  for arg in "$@"; do
    case "$arg" in
      --dry-run) DRY_RUN=1 ;;
      *) ;;
    esac
  done
}
