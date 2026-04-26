# Phase 001 Spec: Repository Skeleton

## Phase and title

Phase 1: Repository Skeleton

## Implemented behavior

Phase 1 establishes the tracked top-level repository skeleton required before application scaffolding begins.

Implemented repository behavior:

- `README.md` identifies the project, phase state, canonical control docs, repository layout, local CI lanes, and workstation verification entry point.
- `Makefile` provides stable developer entry points for `help`, `status`, `verify-workstation`, `phase-docs`, `ci-quick`, `ci-professional`, `ci-release`, and `phase-close`.
- `app/` exists as the future application root and is tracked through `app/README.md`.
- `infra/` exists as the future native deployment root and is tracked through `infra/README.md`.
- `.gitkeep` sentinels are forbidden and absent.
- `scripts/local-ci.sh` is the local CI master entry point.
- `scripts/local_ci.py` owns the local CI runner and supports `quick`, `professional`, and `release` lanes.
- `make phase-close` maps to the professional lane.
- `scripts/` continues to contain Phase 0 workstation scripts.
- `docs/project/vision.md` records the Phase 1 vision seed.
- `docs/project/phase-plan.md` indexes the canonical phase-control documents without duplicating the full plan.
- `.gitignore` protects patch artifacts, dependency output, build output, local environment files, logs, local media, and backups.
- `docs/progress.json` records Phase 1 as complete and Phase 2 as the next candidate phase.
- `docs/progress.jsonl` records the append-only Phase 1 repair entry.
- `docs/multiverse_codex_phase_completion_checklist.md` now includes the Local CI Law and Phase 1 local CI requirements.

## Public/admin routes touched

None. No app routes exist yet.

## Domain modules touched

None. No domain modules exist yet.

## Data models touched

None. No data models exist yet.

## Guards and seams added

- `Makefile` targets are thin command entry points and do not mutate host state by default.
- `scripts/local-ci.sh` delegates local CI behavior to `scripts/local_ci.py` and stays shell-thin.
- `scripts/local_ci.py` centralizes local CI checks and uses only the Python standard library.
- The professional lane checks golden/spec/closure evidence for all completed phases to prevent drift.
- The professional lane rejects `.gitkeep` sentinels and unknown files over 1,000 LOC.
- The file-size gate allows only the documented canonical control-doc size exceptions already present in the repo.
- `.gitignore` guards against accidental commits of local environment files, generated archives, dependency folders, media, backups, and logs.

## Tests and smokes added

- `scripts/local-ci.sh quick`
- `scripts/local-ci.sh professional`
- `scripts/local-ci.sh release`
- `make ci-quick`
- `make ci-professional`
- `make ci-release`
- `make phase-close`
- `git diff --check`
- Architecture file-size review through the professional lane

## Handoff notes for Phase 2

Phase 2 can begin from the next authoritative tar. The ladder was re-audited and repaired before Phase 2 so phase closure now has a local CI gate and drift checks. Phase 2 should deepen `docs/project/vision.md`, create `docs/project/content-types.md`, update the checklist if the phase changes the closure standard, and pass `make phase-close` before closure.
