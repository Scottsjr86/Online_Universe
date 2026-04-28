#!/usr/bin/env python3
"""Validate Phase 7 native PostgreSQL foundation source artifacts."""

from __future__ import annotations

import json
import os
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "scripts/dev-db-common.sh",
    "scripts/dev-db-create.sh",
    "scripts/dev-db-reset.sh",
    "scripts/dev-db-status.sh",
    "docs/dev/postgres-native.md",
    "docs/specs/phase-007-spec.md",
    "docs/closures/phase-007-closure.md",
    "docs/goldens/phase-007.md",
]

EXECUTABLE_FILES = [
    "scripts/dev-db-create.sh",
    "scripts/dev-db-reset.sh",
    "scripts/dev-db-status.sh",
]

SCRIPT_MARKERS = {
    "scripts/dev-db-common.sh": [
        "mc_validate_identifier",
        "mc_require_url_safe_password",
        "openssl rand -hex 32",
        "mc_apply_role_and_database",
        "alter role",
        "mc_test_app_connection",
    ],
    "scripts/dev-db-create.sh": [
        "MULTIVERSE_CODEX_DB_PASSWORD",
        "--dry-run",
        "mc_apply_role_and_database",
        "mc_test_app_connection",
    ],
    "scripts/dev-db-reset.sh": [
        "--yes",
        "drop database if exists",
        "with (force)",
        "mc_apply_role_and_database",
    ],
    "scripts/dev-db-status.sh": [
        "DATABASE_URL",
        "mc_role_exists",
        "mc_database_exists",
        "native PostgreSQL status verified",
    ],
}

DOC_MARKERS = {
    "docs/dev/postgres-native.md": [
        "Native PostgreSQL",
        "scripts/dev-db-create.sh",
        "scripts/dev-db-reset.sh --dry-run --yes",
        "scripts/dev-db-status.sh",
        "openssl rand -hex 32",
        "updates the password for an existing role",
    ],
    "docs/specs/phase-007-spec.md": [
        "Phase 7",
        "Local Native PostgreSQL Foundation",
        "Implemented behavior",
        "scripts/dev-db-create.sh",
    ],
    "docs/closures/phase-007-closure.md": [
        "Phase 7",
        "Closed",
        "owner workstation",
        "no work is deferred",
    ],
    "docs/goldens/phase-007.md": [
        "Phase 7",
        "Commands run",
        "Known limitations",
        "closed",
    ],
}

CI_MARKERS = [
    "bash -n scripts/dev-db-common.sh",
    "bash -n scripts/dev-db-create.sh",
    "bash -n scripts/dev-db-reset.sh",
    "bash -n scripts/dev-db-status.sh",
    "python3 -S scripts/check_phase_postgres_native.py",
]

CHECKLIST_MARKERS = [
    "scripts/dev-db-common.sh",
    "scripts/dev-db-create.sh",
    "scripts/dev-db-reset.sh",
    "scripts/dev-db-status.sh",
    "scripts/check_phase_postgres_native.py",
    "Run `scripts/dev-db-create.sh`",
    "URL-safe",
]


def fail(message: str) -> int:
    print(f"[FAIL] {message}", file=sys.stderr)
    return 1


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    for path in REQUIRED_FILES:
        if not (ROOT / path).is_file():
            return fail(f"missing required Phase 7 artifact: {path}")

    for path in EXECUTABLE_FILES:
        mode = (ROOT / path).stat().st_mode
        if not (mode & stat.S_IXUSR):
            return fail(f"script is not executable: {path}")

    for path, markers in SCRIPT_MARKERS.items():
        text = read(path)
        if not text.startswith("#!/usr/bin/env bash"):
            return fail(f"missing bash shebang: {path}")
        for marker in markers:
            if marker not in text:
                return fail(f"{path} missing marker: {marker}")

    for path, markers in DOC_MARKERS.items():
        text = read(path)
        for marker in markers:
            if marker not in text:
                return fail(f"{path} missing marker: {marker}")

    ci_text = read("ci/master_ci_runner.yaml")
    for marker in CI_MARKERS:
        if marker not in ci_text:
            return fail(f"CI manifest missing Phase 7 command: {marker}")

    checklist_text = read("docs/multiverse_codex_phase_completion_checklist.md")
    for marker in CHECKLIST_MARKERS:
        if marker not in checklist_text:
            return fail(f"checklist missing Phase 7 marker: {marker}")

    progress = json.loads(read("docs/progress.json"))
    if progress.get("current_phase") != 7:
        return fail("progress current_phase is not 7")
    if progress.get("phase_status") != "complete":
        return fail("Phase 7 must be complete after owner PostgreSQL smoke passes")
    if progress.get("last_completed_phase") != 7:
        return fail("last_completed_phase must be 7 after Phase 7 closure")
    if progress.get("next_candidate_phase") != 8:
        return fail("next_candidate_phase must be 8 after Phase 7 closure")

    print("[PASS] Phase 7 native PostgreSQL foundation closure artifacts verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
