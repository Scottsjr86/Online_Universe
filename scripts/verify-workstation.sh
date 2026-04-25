#!/usr/bin/env bash
set -u

# Verifies the Phase 0 workstation toolchain without installing or mutating the host.
# Enable MULTIVERSE_CODEX_DEBUG=1 for command trace output around failing probes.

failures=0

log_debug() {
  if [ "${MULTIVERSE_CODEX_DEBUG:-0}" = "1" ]; then
    printf '[debug] %s\n' "$*" >&2
  fi
}

mark_pass() {
  printf '[PASS] %s: %s\n' "$1" "$2"
}

mark_fail() {
  printf '[FAIL] %s: %s\n' "$1" "$2"
  failures=$((failures + 1))
}

first_line() {
  sed -n '1p'
}

require_command() {
  name="$1"
  version_command="$2"

  if ! command -v "$name" >/dev/null 2>&1; then
    mark_fail "$name" "command not found"
    return
  fi

  log_debug "running: $version_command"
  output=$(bash -lc "$version_command" 2>&1)
  status=$?
  if [ "$status" -ne 0 ]; then
    mark_fail "$name" "version probe failed: $output"
    return
  fi

  mark_pass "$name" "$(printf '%s\n' "$output" | first_line)"
}

require_service_probe() {
  service_name="$1"

  if ! command -v systemctl >/dev/null 2>&1; then
    mark_fail "postgresql service" "systemctl command not found"
    return
  fi

  log_debug "running: systemctl is-active $service_name"
  output=$(systemctl is-active "$service_name" 2>&1)
  status=$?
  if [ "$status" -ne 0 ]; then
    mark_fail "postgresql service" "not active or unavailable: $output"
    return
  fi

  mark_pass "postgresql service" "$output"
}

printf 'Multiverse Codex Phase 0 workstation verification\n'
printf '==================================================\n'

require_command git 'git --version'
require_command node 'node --version'
require_command pnpm 'pnpm --version'
require_command psql 'psql --version'
require_command systemctl 'systemctl --version'
require_command caddy 'caddy version'
require_command make 'make --version'
require_command curl 'curl --version'
require_command jq 'jq --version'
require_command openssl 'openssl version'
require_service_probe postgresql

printf '==================================================\n'
if [ "$failures" -eq 0 ]; then
  printf '[PASS] workstation bootstrap verified\n'
  exit 0
fi

printf '[FAIL] workstation bootstrap has %s failing probe(s)\n' "$failures"
printf 'Set MULTIVERSE_CODEX_DEBUG=1 for command-level probe output.\n'
exit 1
