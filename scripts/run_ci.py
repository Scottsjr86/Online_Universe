#!/usr/bin/env python3
"""Repo-owned local CI lane runner for Multiverse Codex."""

from __future__ import annotations

import argparse
import os
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


MANIFEST_PATH = Path("ci/master_ci_runner.yaml")
ALLOWED_EXTERNAL_COMMANDS = {
    "bash",
    "git",
    "make",
    "pnpm",
    "python3",
    "test",
}


class ManifestError(ValueError):
    """Raised when the CI manifest is missing or malformed."""


@dataclass(frozen=True)
class CiCommand:
    name: str
    run: str


@dataclass
class Lane:
    name: str
    description: str = ""
    extends: str | None = None
    commands: list[CiCommand] = field(default_factory=list)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_manifest(path: Path) -> dict[str, Lane]:
    if not path.exists():
        raise ManifestError(f"missing CI manifest: {path}")

    lanes: dict[str, Lane] = {}
    current_lane: Lane | None = None
    current_command: dict[str, str] | None = None
    in_lanes = False
    in_commands = False

    def flush_command(line_number: int) -> None:
        nonlocal current_command
        if current_command is None:
            return
        if current_lane is None:
            raise ManifestError(f"line {line_number}: command defined outside a lane")
        name = current_command.get("name")
        run = current_command.get("run")
        if not name or not run:
            raise ManifestError(
                f"line {line_number}: every command must define both name and run"
            )
        current_lane.commands.append(CiCommand(name=name, run=run))
        current_command = None

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0 and line == "lanes:":
            in_lanes = True
            continue
        if not in_lanes:
            raise ManifestError(f"line {line_number}: expected top-level 'lanes:'")

        if indent == 2 and line.endswith(":"):
            flush_command(line_number)
            lane_name = line[:-1]
            if not lane_name or " " in lane_name:
                raise ManifestError(f"line {line_number}: invalid lane name {lane_name!r}")
            if lane_name in lanes:
                raise ManifestError(f"line {line_number}: duplicate lane {lane_name!r}")
            current_lane = Lane(name=lane_name)
            lanes[lane_name] = current_lane
            in_commands = False
            continue

        if current_lane is None:
            raise ManifestError(f"line {line_number}: lane field without lane")

        if indent == 4 and line.startswith("description:"):
            current_lane.description = line.split(":", 1)[1].strip().strip('"')
            continue
        if indent == 4 and line.startswith("extends:"):
            parent = line.split(":", 1)[1].strip()
            current_lane.extends = parent or None
            continue
        if indent == 4 and line == "commands:":
            in_commands = True
            continue

        if not in_commands:
            raise ManifestError(f"line {line_number}: unexpected lane field {line!r}")

        if indent == 6 and line.startswith("- name:"):
            flush_command(line_number)
            current_command = {"name": line.split(":", 1)[1].strip().strip('"')}
            continue
        if indent == 8 and line.startswith("run:"):
            if current_command is None:
                raise ManifestError(f"line {line_number}: run defined before command name")
            current_command["run"] = line.split(":", 1)[1].strip().strip('"')
            continue

        raise ManifestError(f"line {line_number}: unsupported manifest syntax {line!r}")

    flush_command(line_number if 'line_number' in locals() else 0)

    if not lanes:
        raise ManifestError("CI manifest has no lanes")
    for lane in lanes.values():
        if lane.extends and lane.extends not in lanes:
            raise ManifestError(f"lane {lane.name!r} extends unknown lane {lane.extends!r}")
    return lanes


def resolve_lane_commands(lanes: dict[str, Lane], lane_name: str) -> list[CiCommand]:
    resolved: list[CiCommand] = []
    seen: set[str] = set()

    def visit(name: str) -> None:
        if name in seen:
            raise ManifestError(f"cyclic lane inheritance involving {name!r}")
        seen.add(name)
        lane = lanes[name]
        if lane.extends:
            visit(lane.extends)
        resolved.extend(lane.commands)
        seen.remove(name)

    visit(lane_name)
    return resolved


def split_command(command: str) -> list[str]:
    try:
        parts = shlex.split(command)
    except ValueError as exc:
        raise ManifestError(f"cannot parse command {command!r}: {exc}") from exc
    if not parts:
        raise ManifestError("empty command in CI manifest")
    return parts


def validate_command(parts: list[str], root: Path) -> None:
    executable = parts[0]

    if any(token in {"|", ";", "&&", "||", ">", ">>", "<"} for token in parts):
        raise ManifestError(
            "shell operators are not supported; split the check into explicit commands"
        )

    if "/" in executable:
        candidate = (root / executable).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise ManifestError(f"command escapes repo root: {executable}") from exc
        if not candidate.exists():
            raise ManifestError(f"repo command does not exist: {executable}")
        if candidate.is_dir():
            raise ManifestError(f"repo command is a directory: {executable}")
        return

    if executable not in ALLOWED_EXTERNAL_COMMANDS:
        raise ManifestError(f"external command is not allowlisted: {executable}")
    if shutil.which(executable) is None:
        raise ManifestError(f"command not found on PATH: {executable}")



def run_internal_test(parts: list[str], root: Path) -> int | None:
    if not parts or parts[0] != "test":
        return None
    if len(parts) == 3 and parts[1] == "-f":
        return 0 if (root / parts[2]).is_file() else 1
    if len(parts) == 4 and parts[1] == "!" and parts[2] == "-e":
        return 0 if not (root / parts[3]).exists() else 1
    raise ManifestError(f"unsupported test command: {' '.join(parts)}")

def run_lane(lane_name: str, lanes: dict[str, Lane], root: Path) -> int:
    commands = resolve_lane_commands(lanes, lane_name)
    total = len(commands)
    if total == 0:
        print(f"[FAIL] lane {lane_name!r} has no commands", file=sys.stderr, flush=True)
        return 2

    print(f"Multiverse Codex local CI: {lane_name}", flush=True)
    print("=" * 40, flush=True)
    for index, command in enumerate(commands, 1):
        parts = split_command(command.run)
        validate_command(parts, root)
        print(f"[{index}/{total}] {command.name}", flush=True)
        print(f"$ {command.run}", flush=True)
        internal_returncode = run_internal_test(parts, root)
        if internal_returncode is None:
            env = os.environ.copy()
            env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
            completed = subprocess.run(parts, cwd=root, env=env, shell=False)
            returncode = completed.returncode
        else:
            returncode = internal_returncode
        if returncode != 0:
            print(
                f"[FAIL] step {index} failed with exit code {returncode}: {command.name}",
                file=sys.stderr,
                flush=True,
            )
            return returncode
        print(f"[ok] step {index} completed", flush=True)
    print(f"[PASS] {lane_name} lane passed", flush=True)
    return 0


def print_lanes(lanes: dict[str, Lane]) -> None:
    width = max(len(name) for name in lanes)
    print("Available CI lanes:", flush=True)
    for name in lanes:
        lane = lanes[name]
        inheritance = f" extends {lane.extends}" if lane.extends else ""
        print(f"  {name:<{width}}  {lane.description}{inheritance}", flush=True)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Multiverse Codex local CI lanes.")
    parser.add_argument("lane", nargs="?", help="CI lane to run")
    parser.add_argument("--list", action="store_true", help="List available CI lanes")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    root = repo_root()
    manifest = root / MANIFEST_PATH

    try:
        lanes = parse_manifest(manifest)
        if args.list:
            print_lanes(lanes)
            return 0
        if not args.lane:
            print("[FAIL] missing lane argument; use --list to inspect lanes", file=sys.stderr, flush=True)
            return 2
        if args.lane not in lanes:
            print(f"[FAIL] unknown CI lane: {args.lane}", file=sys.stderr, flush=True)
            print_lanes(lanes)
            return 2
        return run_lane(args.lane, lanes, root)
    except ManifestError as exc:
        print(f"[FAIL] {exc}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    os._exit(main())
