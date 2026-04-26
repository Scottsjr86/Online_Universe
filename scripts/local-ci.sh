#!/usr/bin/env bash
set -euo pipefail

# Master entry point for local CI lanes.
# Lanes:
#   quick         fast static checks for every patch loop
#   professional phase-close gate; includes quick plus drift/file-size checks
#   release      deepest local gate currently available before handoff

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON:-/usr/bin/python3}"
exec "$python_bin" scripts/local_ci.py "$@"
