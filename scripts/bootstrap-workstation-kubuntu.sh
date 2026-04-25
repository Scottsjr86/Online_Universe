#!/usr/bin/env bash
set -euo pipefail

# Bootstraps the Phase 0 workstation toolchain for Kubuntu/Ubuntu hosts.
# Default mode is dry-run. Use --install before any host mutation happens.

mode="dry-run"
node_major="24"

usage() {
  cat <<'USAGE'
Usage: scripts/bootstrap-workstation-kubuntu.sh [--dry-run] [--install] [--node-major <major>]

Defaults to --dry-run and prints the commands that would run.
Use --install to apply changes to the host.

Options:
  --dry-run             Print commands without running them. Default.
  --install             Install required Phase 0 packages and start PostgreSQL.
  --node-major <major>  NodeSource major version to configure. Default: 24.
  -h, --help            Show this help text.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run)
      mode="dry-run"
      shift
      ;;
    --install)
      mode="install"
      shift
      ;;
    --node-major)
      if [ "$#" -lt 2 ]; then
        printf '[FAIL] --node-major requires a value.\n' >&2
        exit 2
      fi
      node_major="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf '[FAIL] unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if ! printf '%s' "$node_major" | grep -Eq '^[0-9]+$'; then
  printf '[FAIL] --node-major must be numeric, got: %s\n' "$node_major" >&2
  exit 2
fi

run() {
  printf '+ %s\n' "$*"
  if [ "$mode" = "install" ]; then
    "$@"
  fi
}

run_shell() {
  printf '+ %s\n' "$*"
  if [ "$mode" = "install" ]; then
    bash -lc "$*"
  fi
}

require_install_host() {
  if ! command -v apt-get >/dev/null 2>&1; then
    printf '[FAIL] apt-get is required for install mode.\n' >&2
    exit 1
  fi

  if ! command -v sudo >/dev/null 2>&1; then
    printf '[FAIL] sudo is required for install mode.\n' >&2
    exit 1
  fi

  if [ -r /etc/os-release ]; then
    # shellcheck disable=SC1091
    . /etc/os-release
    case "${ID:-}" in
      ubuntu|kubuntu|neon|pop|linuxmint)
        ;;
      *)
        printf '[FAIL] install mode expected an Ubuntu-family host, found ID=%s.\n' "${ID:-unknown}" >&2
        exit 1
        ;;
    esac
  else
    printf '[FAIL] /etc/os-release is missing; refusing install mode.\n' >&2
    exit 1
  fi
}

print_header() {
  printf 'Multiverse Codex Kubuntu Phase 0 bootstrap\n'
  printf '==========================================\n'
  printf 'Mode: %s\n' "$mode"
  printf 'NodeSource major: %s.x\n' "$node_major"
}

print_header

if [ "$mode" = "install" ]; then
  require_install_host
fi

base_packages=(
  ca-certificates
  curl
  gnupg
  git
  make
  jq
  openssl
  postgresql
  postgresql-client
  debian-keyring
  debian-archive-keyring
  apt-transport-https
)

run sudo apt-get update
run sudo apt-get install -y "${base_packages[@]}"

nodesource_setup="/tmp/multiverse-codex-nodesource-setup.sh"
run curl -fsSL "https://deb.nodesource.com/setup_${node_major}.x" -o "$nodesource_setup"
run sudo bash "$nodesource_setup"
run sudo apt-get install -y nodejs

run sudo install -d -m 0755 /etc/apt/keyrings
run_shell 'curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/caddy-stable-archive-keyring.gpg'
run_shell 'curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt | sudo tee /etc/apt/sources.list.d/caddy-stable.list >/dev/null'
run sudo apt-get update
run sudo apt-get install -y caddy

run sudo systemctl enable --now postgresql

run_shell 'if command -v corepack >/dev/null 2>&1; then sudo corepack enable && sudo corepack prepare pnpm@latest-10 --activate; else sudo npm install -g pnpm@latest; fi'

if [ "$mode" = "dry-run" ]; then
  printf '[PASS] dry-run complete; no host changes were made. Re-run with --install to apply.\n'
else
  printf '[PASS] install complete. Run scripts/verify-workstation.sh next.\n'
fi
