# Phase 000 Spec: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Implemented behavior

This phase currently implements the repository-side verification harness for the workstation bootstrap:

- `scripts/verify-workstation.sh` checks required command availability and version output.
- The probe checks PostgreSQL service availability through `systemctl is-active postgresql`.
- The probe exits nonzero when required tools or service checks fail.
- `MULTIVERSE_CODEX_DEBUG=1` enables gated command-level probe output for diagnosing failures.
- `docs/dev/workstation.md` documents required tools, verification commands, expected success behavior, expected failure behavior, and troubleshooting notes.
- `docs/progress.json` restores the required machine-readable progress state.

## Public/admin routes touched

None. No application routes exist in Phase 0.

## Domain modules touched

None. No application domain modules exist in Phase 0.

## Data models touched

None. No database schema exists in Phase 0.

## Guards and seams added

- Shell probe uses explicit command checks before version probes.
- Shell probe fails closed when commands are missing or service checks fail.
- Gated debug output is controlled by `MULTIVERSE_CODEX_DEBUG` and is silent by default.

## Tests and smokes added

- `scripts/verify-workstation.sh`

## Handoff notes for Phase 0 continuation

Phase 0 is not closed. The next Phase 0 slice should be based on the latest tar and should close only after the target workstation or VM proves every required tool and PostgreSQL service check with a clean `scripts/verify-workstation.sh` run.
