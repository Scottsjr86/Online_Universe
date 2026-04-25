#!/usr/bin/env bash
set -u

# Verifies the Phase 0 workstation toolchain without installing or mutating the host.
# Enable MULTIVERSE_CODEX_DEBUG=1 for command trace output around failing probes.

failures=0
probe_timeout_seconds="${MULTIVERSE_CODEX_TIMEOUT_SECONDS:-10}"
probe_output=''
probe_status=0

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

run_probe_shell() {
  probe_command="$1"

  if command -v timeout >/dev/null 2>&1; then
    log_debug "running with timeout ${probe_timeout_seconds}s: $probe_command"
    probe_output=$(timeout "${probe_timeout_seconds}s" bash -lc "$probe_command" 2>&1)
    probe_status=$?
    if [ "$probe_status" -eq 124 ]; then
      probe_output="probe timed out after ${probe_timeout_seconds}s"
    fi
    return
  fi

  log_debug "running: $probe_command"
  probe_output=$(bash -lc "$probe_command" 2>&1)
  probe_status=$?
}

require_command() {
  name="$1"
  version_command="$2"
  probe_command="$version_command"

  if ! command -v "$name" >/dev/null 2>&1; then
    mark_fail "$name" "command not found"
    return
  fi

  # Corepack-backed pnpm shims may attempt a download on first use.
  # Disable that during verification so the probe stays read-only and fails fast.
  if [ "$name" = "pnpm" ]; then
    probe_command="COREPACK_ENABLE_NETWORK=0 $version_command"
  fi

  run_probe_shell "$probe_command"
  if [ "$probe_status" -eq 124 ]; then
    mark_fail "$name" "$probe_output: $version_command"
    return
  fi

  if [ "$probe_status" -ne 0 ]; then
    mark_fail "$name" "version probe failed: $probe_output"
    return
  fi

  mark_pass "$name" "$(printf '%s\n' "$probe_output" | first_line)"
}

require_service_probe() {
  service_name="$1"

  if ! command -v systemctl >/dev/null 2>&1; then
    mark_fail "postgresql service" "systemctl command not found"
    return
  fi

  run_probe_shell "systemctl is-active $service_name"
  if [ "$probe_status" -eq 124 ]; then
    mark_fail "postgresql service" "$probe_output: systemctl is-active $service_name"
    return
  fi

  if [ "$probe_status" -ne 0 ]; then
    mark_fail "postgresql service" "not active or unavailable: $probe_output"
    return
  fi

  mark_pass "postgresql service" "$probe_output"
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
