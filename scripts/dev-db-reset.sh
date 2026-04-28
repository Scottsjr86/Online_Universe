#!/usr/bin/env bash
# Reset the native local PostgreSQL development database.

set -Eeuo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
# shellcheck source=scripts/dev-db-common.sh
source "$SCRIPT_DIR/dev-db-common.sh"

YES=0
DRY_RUN=0

usage() {
  cat <<USAGE
Usage: scripts/dev-db-reset.sh --yes [--dry-run]

Drops and recreates the local development database. This is destructive.
Required env:
  MULTIVERSE_CODEX_DB_PASSWORD  password to set on the app database role
USAGE
}

for arg in "$@"; do
  case "$arg" in
    --yes) YES=1 ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help) usage; exit 0 ;;
    *) mc_fail "unknown argument: $arg" 2 ;;
  esac
done

if [[ "$YES" -ne 1 ]]; then
  mc_fail "refusing destructive reset without --yes" 2
fi

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

mc_log INFO "dropping database $MC_DB_NAME"
mc_super_psql -c "drop database if exists \"$MC_DB_NAME\" with (force);" >/dev/null
mc_apply_role_and_database
mc_test_app_connection

mc_log PASS "native PostgreSQL dev database reset and verified"
