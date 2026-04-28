#!/usr/bin/env bash
# Report native local PostgreSQL development database status.

set -Eeuo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
# shellcheck source=scripts/dev-db-common.sh
source "$SCRIPT_DIR/dev-db-common.sh"

usage() {
  cat <<USAGE
Usage: scripts/dev-db-status.sh

Checks PostgreSQL service state, role/database existence, and app-user connection.
Connection check uses DATABASE_URL when set, otherwise MULTIVERSE_CODEX_DB_PASSWORD.
USAGE
}

for arg in "$@"; do
  case "$arg" in
    -h|--help) usage; exit 0 ;;
    *) mc_fail "unknown argument: $arg" 2 ;;
  esac
done

mc_validate_identifier "MULTIVERSE_CODEX_DB_NAME" "$MC_DB_NAME"
mc_validate_identifier "MULTIVERSE_CODEX_DB_USER" "$MC_DB_USER"
mc_need_command psql
mc_need_command sudo
mc_need_command systemctl

printf 'Multiverse Codex native PostgreSQL status\n'
printf '==========================================\n'

if mc_is_postgres_active; then
  mc_log PASS "service active: $MC_POSTGRES_SERVICE"
else
  mc_fail "service inactive: $MC_POSTGRES_SERVICE" 3
fi

if mc_role_exists; then
  mc_log PASS "role exists: $MC_DB_USER"
else
  mc_fail "role missing: $MC_DB_USER" 4
fi

if mc_database_exists; then
  mc_log PASS "database exists: $MC_DB_NAME"
else
  mc_fail "database missing: $MC_DB_NAME" 5
fi

if [[ -n "${DATABASE_URL:-}" ]]; then
  psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -c 'select 1;' >/dev/null
  mc_log PASS "DATABASE_URL connection ok"
elif [[ -n "${MULTIVERSE_CODEX_DB_PASSWORD:-}" ]]; then
  mc_test_app_connection
  mc_log PASS "app role connection ok: $(mc_masked_connection_url)"
else
  mc_fail "set DATABASE_URL or MULTIVERSE_CODEX_DB_PASSWORD for app-role connection check" 6
fi

mc_log PASS "native PostgreSQL status verified"
