#!/usr/bin/env bash
# Create or verify the native local PostgreSQL development database.

set -Eeuo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
# shellcheck source=scripts/dev-db-common.sh
source "$SCRIPT_DIR/dev-db-common.sh"

usage() {
  cat <<USAGE
Usage: scripts/dev-db-create.sh [--dry-run]

Creates or verifies the native PostgreSQL development role/database.
Required env:
  MULTIVERSE_CODEX_DB_PASSWORD  password for the app database role
Optional env:
  MULTIVERSE_CODEX_DB_NAME      default: multiverse_codex_dev
  MULTIVERSE_CODEX_DB_USER      default: multiverse_codex_app
  MULTIVERSE_CODEX_DB_HOST      default: 127.0.0.1
  MULTIVERSE_CODEX_DB_PORT      default: 5432
USAGE
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) ;;
    -h|--help) usage; exit 0 ;;
    *) mc_fail "unknown argument: $arg" 2 ;;
  esac
done

mc_parse_dry_run_flag "$@"
mc_validate_identifier "MULTIVERSE_CODEX_DB_NAME" "$MC_DB_NAME"
mc_validate_identifier "MULTIVERSE_CODEX_DB_USER" "$MC_DB_USER"
mc_require_password
mc_need_command psql
mc_need_command sudo
mc_need_command systemctl
mc_require_postgres_active

mc_log INFO "target database: $MC_DB_NAME"
mc_log INFO "target role: $MC_DB_USER"
mc_log INFO "target connection: $(mc_masked_connection_url)"

if [[ "$DRY_RUN" -eq 1 ]]; then
  mc_log PASS "dry run complete; no PostgreSQL changes were made"
  exit 0
fi

mc_apply_role_and_database
mc_test_app_connection

mc_log PASS "native PostgreSQL dev database verified"
mc_log INFO "export DATABASE_URL=\"$(mc_masked_connection_url)\""
if [[ "${MULTIVERSE_CODEX_PRINT_DATABASE_URL:-0}" == "1" ]]; then
  printf 'DATABASE_URL=%s\n' "$(mc_connection_url)"
fi
