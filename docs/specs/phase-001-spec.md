# Phase 001 Spec: Repository Skeleton

## Phase and title

Phase 1: Repository Skeleton

## Implemented behavior

Phase 1 establishes the tracked top-level repository skeleton required before application scaffolding begins.

Implemented repository behavior:

- `README.md` identifies the project, current phase state, canonical control docs, top-level layout, and initial smoke checks.
- `Makefile` provides stable developer entry points for `help`, `status`, `verify-workstation`, and `phase-docs`.
- `app/` exists as the future application root and is tracked through `app/.gitkeep`.
- `infra/` exists as the future native deployment root and is tracked through `infra/.gitkeep`.
- `scripts/` continues to contain Phase 0 workstation scripts.
- `docs/project/vision.md` records the Phase 1 vision seed.
- `docs/project/phase-plan.md` indexes the canonical phase-control documents without duplicating the full plan.
- `.gitignore` protects patch artifacts, dependency output, build output, local environment files, logs, local media, and backups.
- `docs/progress.json` records Phase 1 as complete and Phase 2 as the next candidate phase.
- `docs/progress.jsonl` records the append-only Phase 1 patch entry.

## Public/admin routes touched

None. No app routes exist yet.

## Domain modules touched

None. No domain modules exist yet.

## Data models touched

None. No data models exist yet.

## Guards and seams added

- `Makefile` targets are thin command entry points and do not mutate host state by default.
- `.gitignore` guards against accidental commits of local environment files, generated archives, dependency folders, media, backups, and logs.
- Empty top-level roots are tracked with sentinels so Git preserves the intended structure.

## Tests and smokes added

- `make help`
- `make phase-docs`
- `git status --short`
- `git diff --check`
- Architecture file-size review

## Handoff notes for Phase 2

Phase 2 can begin from the next authoritative tar. The repository skeleton is present, Phase 0 remains closed, and the next phase should deepen `docs/project/vision.md` and add the content vocabulary document required by the canonical plan.
