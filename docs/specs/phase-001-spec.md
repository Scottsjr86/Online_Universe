# Phase 001 Spec: Repository Skeleton

## Phase and title

Phase 1: Repository Skeleton

## Implemented behavior

Phase 1 establishes the tracked top-level repository skeleton required before application scaffolding begins.

Implemented repository behavior:

- `README.md` identifies the project, phase state, canonical control docs, repository layout, master CI lanes, and workstation verification entry point.
- `Makefile` provides stable developer entry points for `help`, `status`, `verify-workstation`, `phase-docs`, `ci-list`, `ci-quick`, `ci-professional`, `ci-release`, `ci-enterprise`, and `phase-close`.
- `app/` exists as the future application root and is tracked through `app/README.md`.
- `infra/` exists as the future native deployment root and is tracked through `infra/README.md`.
- `.gitkeep` sentinels are forbidden and absent.
- `ci/master_ci_runner.yaml` is the repo-owned CI manifest.
- `scripts/run_ci.py` is the repo-owned CI runner.
- The runner supports `--list` plus one lane argument.
- The manifest defines `quick`, `professional`, `release`, and `enterprise` lanes.
- Lane inheritance is manifest-defined and runs parent commands before child commands.
- `make phase-close` maps to the professional lane.
- `scripts/` continues to contain Phase 0 workstation scripts.
- `docs/project/vision.md` records the Phase 1 vision seed.
- `docs/project/phase-plan.md` indexes the canonical phase-control documents without duplicating the full plan.
- `.gitignore` protects patch artifacts, dependency output, build output, local environment files, logs, local media, and backups.
- `docs/progress.json` records Phase 1 as complete and Phase 2 as the next candidate phase.
- `docs/progress.jsonl` records the append-only Phase 1 CI redo entry.
- `docs/multiverse_codex_phase_completion_checklist.md` now describes the master CI runner law and Phase 1 CI requirements.

## CI lane behavior

The runner:

- reads `ci/master_ci_runner.yaml`
- accepts one lane argument
- supports `--list`
- rejects unknown lanes
- runs commands from the repository root
- runs commands in order
- prints numbered steps
- streams stdout and stderr
- stops on first failure
- returns the failed command's exit code
- avoids arbitrary command execution from user input
- avoids `shell=True`
- tokenizes manifest commands with `shlex`
- allowlists external command names used by the current manifest
- supports only simple repo-local YAML syntax needed by the manifest

The manifest does not invent npm, pnpm, lint, typecheck, test, e2e, audit, or build commands because no package/framework tooling exists yet.

## Public/admin routes touched

None. No app routes exist yet.

## Domain modules touched

None. No domain modules exist yet.

## Data models touched

None. No data models exist yet.

## Guards and seams added

- `Makefile` targets are thin command entry points and do not mutate host state by default.
- `ci/master_ci_runner.yaml` owns lane composition and command order.
- `scripts/run_ci.py` owns CI execution behavior and does not mutate host state.
- The professional lane checks golden/spec/closure evidence for completed phases to prevent drift.
- The professional lane rejects `.gitkeep` sentinels and legacy `scripts/local-ci.sh` / `scripts/local_ci.py` CI files.
- `.gitignore` guards against accidental commits of local environment files, generated archives, dependency folders, media, backups, and logs.

## Tests and smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py --list`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py quick`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py release`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py enterprise`
- `make ci-list`
- `make ci-quick`
- `make ci-professional`
- `make ci-release`
- `make ci-enterprise`
- `make phase-close`
- unknown lane rejection
- `git diff --check`

## Handoff notes for Phase 2

Phase 2 can begin from the next authoritative tar. The CI ladder is now the requested master-runner shape. Phase 2 should deepen `docs/project/vision.md`, create `docs/project/content-types.md`, update the checklist if the closure contract changes, and pass `make phase-close` before closure.
