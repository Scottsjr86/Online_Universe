#!/usr/bin/env python3
"""Local CI lane runner for Multiverse Codex.

This runner intentionally uses only the Python standard library. It is the
single local gate used before phase closure and grows as phases add tests.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]

CANONICAL_OVERSIZE_DOCS = {
    Path("docs/multiverse_codex_phase_plan.md"),
    Path("docs/multiverse_codex_phase_completion_checklist.md"),
}

TEXT_EXTENSIONS = {
    ".css",
    ".js",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".svelte",
    ".ts",
}

MAX_LINES = 1000
WARN_LINES = 750


@dataclass(frozen=True)
class Check:
    name: str
    run: Callable[[], None]


class CheckError(RuntimeError):
    """Raised when a CI check fails."""


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def command_exists(name: str) -> bool:
    path_env = os.environ.get("PATH", "")
    for raw_dir in path_env.split(os.pathsep):
        if raw_dir and (Path(raw_dir) / name).exists():
            return True
    return False


def run_command(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    printable = " ".join(args)
    print(f"[run] {printable}")
    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if check and result.returncode != 0:
        raise CheckError(f"command failed ({result.returncode}): {printable}")
    return result


def require_paths(paths: Iterable[str]) -> None:
    missing = [path for path in paths if not (REPO_ROOT / path).exists()]
    if missing:
        raise CheckError("missing required path(s): " + ", ".join(missing))


def check_required_skeleton() -> None:
    require_paths(
        [
            "README.md",
            "Makefile",
            "app/README.md",
            "infra/README.md",
            "docs/project/vision.md",
            "docs/project/phase-plan.md",
            "docs/progress.json",
            "docs/progress.jsonl",
            "docs/specs/phase-000-spec.md",
            "docs/specs/phase-001-spec.md",
            "docs/closures/phase-000-closure.md",
            "docs/closures/phase-001-closure.md",
            "docs/goldens/phase-000.md",
            "docs/goldens/phase-001.md",
        ]
    )


def check_no_gitkeep_sentinels() -> None:
    sentinels = sorted(path for path in REPO_ROOT.rglob(".gitkeep") if ".git" not in path.parts)
    if sentinels:
        raise CheckError(".gitkeep sentinel(s) are forbidden: " + ", ".join(rel(path) for path in sentinels))


def check_shell_syntax() -> None:
    scripts = sorted((REPO_ROOT / "scripts").glob("*.sh"))
    if not scripts:
        raise CheckError("no shell scripts found under scripts/")
    for script in scripts:
        run_command(["bash", "-n", rel(script)])


def check_python_syntax() -> None:
    run_command([sys.executable, "-m", "py_compile", "scripts/local_ci.py"])


def check_make_targets() -> None:
    run_command(["make", "help"])
    run_command(["make", "phase-docs"])


def check_git_diff_whitespace() -> None:
    run_command(["git", "diff", "--check"])


def load_progress() -> dict[str, object]:
    try:
        return json.loads((REPO_ROOT / "docs/progress.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CheckError(f"docs/progress.json is invalid JSON: {exc}") from exc


def check_progress_state() -> None:
    progress = load_progress()
    required = {
        "current_phase",
        "current_phase_title",
        "phase_status",
        "last_completed_phase",
        "next_candidate_phase",
        "last_patch_id",
        "updated_at",
    }
    missing = sorted(required.difference(progress))
    if missing:
        raise CheckError("docs/progress.json missing key(s): " + ", ".join(missing))

    current_phase = progress.get("current_phase")
    last_completed = progress.get("last_completed_phase")
    next_candidate = progress.get("next_candidate_phase")
    if not isinstance(current_phase, int) or not isinstance(last_completed, int) or not isinstance(next_candidate, int):
        raise CheckError("phase fields in docs/progress.json must be integers")
    if next_candidate < last_completed:
        raise CheckError("next_candidate_phase cannot be behind last_completed_phase")


def check_progress_log() -> None:
    log_path = REPO_ROOT / "docs/progress.jsonl"
    entries: list[dict[str, object]] = []
    with log_path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CheckError(f"docs/progress.jsonl line {line_number} is invalid JSON: {exc}") from exc
            entries.append(entry)
    if not entries:
        raise CheckError("docs/progress.jsonl has no entries")

    progress = load_progress()
    last_patch_id = progress.get("last_patch_id")
    if entries[-1].get("patch_id") != last_patch_id:
        raise CheckError("last progress log entry does not match docs/progress.json last_patch_id")


def check_phase_evidence() -> None:
    progress = load_progress()
    last_completed = progress.get("last_completed_phase")
    if not isinstance(last_completed, int):
        raise CheckError("last_completed_phase must be an integer")

    for phase in range(last_completed + 1):
        stem = f"phase-{phase:03d}"
        require_paths(
            [
                f"docs/specs/{stem}-spec.md",
                f"docs/closures/{stem}-closure.md",
                f"docs/goldens/{stem}.md",
            ]
        )


def check_checklist_local_ci_law() -> None:
    checklist = (REPO_ROOT / "docs/multiverse_codex_phase_completion_checklist.md").read_text(encoding="utf-8")
    required_phrases = [
        "Local CI Law",
        "scripts/local-ci.sh quick",
        "scripts/local-ci.sh professional",
        "scripts/local-ci.sh release",
        "No `.gitkeep` sentinels",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in checklist]
    if missing:
        raise CheckError("checklist missing local CI requirement(s): " + ", ".join(missing))


def iter_review_files() -> Iterable[Path]:
    roots = [REPO_ROOT / name for name in ("app", "scripts", "infra", "docs")]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in TEXT_EXTENSIONS:
                yield path


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="replace").splitlines())


def check_file_sizes() -> None:
    oversized: list[tuple[Path, int]] = []
    warnings: list[tuple[Path, int]] = []
    for path in iter_review_files():
        count = line_count(path)
        relative = path.relative_to(REPO_ROOT)
        if count > MAX_LINES and relative not in CANONICAL_OVERSIZE_DOCS:
            oversized.append((relative, count))
        elif count > WARN_LINES and relative not in CANONICAL_OVERSIZE_DOCS:
            warnings.append((relative, count))

    if warnings:
        print("[warn] files in 750-1000 LOC review zone:")
        for path, count in warnings:
            print(f"  {count:5d} {path}")

    if oversized:
        details = ", ".join(f"{path} ({count} LOC)" for path, count in oversized)
        raise CheckError("unknown file(s) over 1000 LOC: " + details)

    allowed = sorted(
        (path, line_count(REPO_ROOT / path))
        for path in CANONICAL_OVERSIZE_DOCS
        if (REPO_ROOT / path).exists()
    )
    if allowed:
        print("[info] documented canonical control-doc size exceptions:")
        for path, count in allowed:
            print(f"  {count:5d} {path}")


def lane_quick() -> list[Check]:
    return [
        Check("required skeleton paths", check_required_skeleton),
        Check("no .gitkeep sentinels", check_no_gitkeep_sentinels),
        Check("shell syntax", check_shell_syntax),
        Check("python syntax", check_python_syntax),
        Check("make targets", check_make_targets),
    ]


def lane_professional() -> list[Check]:
    return lane_quick() + [
        Check("git diff whitespace", check_git_diff_whitespace),
        Check("progress state", check_progress_state),
        Check("progress log", check_progress_log),
        Check("phase evidence", check_phase_evidence),
        Check("checklist local CI law", check_checklist_local_ci_law),
        Check("architecture file-size gate", check_file_sizes),
    ]


def lane_release() -> list[Check]:
    return lane_professional() + [
        Check("release phase-doc availability", lambda: require_paths([
            "docs/multiverse_codex_phase_plan.md",
            "docs/multiverse_codex_phase_completion_checklist.md",
            "docs/multiverse_codex_architecture_laws.md",
            "docs/multiverse_codex_fresh_chat_workflow_header.md",
        ])),
    ]


LANES: dict[str, Callable[[], list[Check]]] = {
    "quick": lane_quick,
    "professional": lane_professional,
    "release": lane_release,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Multiverse Codex local CI lanes.")
    parser.add_argument("lane", nargs="?", default="quick", choices=sorted(LANES), help="CI lane to run")
    args = parser.parse_args()

    print(f"Multiverse Codex local CI: {args.lane}")
    print("=" * 36)

    failures = 0
    for check in LANES[args.lane]():
        print(f"[check] {check.name}")
        try:
            check.run()
        except CheckError as exc:
            failures += 1
            print(f"[FAIL] {check.name}: {exc}")
        except Exception as exc:  # pragma: no cover - defensive CLI safety net.
            failures += 1
            print(f"[FAIL] {check.name}: unexpected {type(exc).__name__}: {exc}")
        else:
            print(f"[PASS] {check.name}")

    print("=" * 36)
    if failures:
        print(f"[FAIL] {args.lane} lane failed with {failures} failing check(s)")
        return 1

    print(f"[PASS] {args.lane} lane passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
