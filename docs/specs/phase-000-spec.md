# Phase 000 Spec: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Implemented behavior

This phase currently implements the repository-side verification and bootstrap harness for the workstation bootstrap:

- `scripts/verify-workstation.sh` checks required command availability and version output.
- The probe checks PostgreSQL service availability through `systemctl is-active postgresql`.
- The probe exits nonzero when required tools or service checks fail.
- `MULTIVERSE_CODEX_DEBUG=1` enables gated command-level probe output for diagnosing failures.
- `scripts/bootstrap-workstation-kubuntu.sh` provides a Kubuntu/Ubuntu bootstrap helper with dry-run as the default behavior.
- `scripts/bootstrap-workstation-kubuntu.sh --install` installs the Phase 0 workstation tools, configures package repositories for Node and Caddy, enables pnpm, and starts/enables PostgreSQL.
- `docs/dev/workstation.md` documents required tools, the current target workstation state, bootstrap commands, verification commands, expected success behavior, expected failure behavior, and troubleshooting notes.
- `docs/progress.json` records the current machine-readable phase state.

## Repair note

The applied Phase 0 repo state referenced `scripts/bootstrap-workstation-kubuntu.sh` in the docs and progress log, but the uploaded `phase_000_kubuntu_bootstrap.patch` artifact did not contain the script file. This repair slice restores that missing implementation file and refreshes evidence so the docs again match the code.

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
- Bootstrap helper defaults to dry-run and requires `--install` before mutating the host.
- Bootstrap helper validates the requested Node major version.
- Bootstrap helper performs an Ubuntu-family host-shape check before install mode.
- Bootstrap helper exits on unknown arguments instead of guessing.

## Tests and smokes added

- `scripts/verify-workstation.sh`
- `scripts/bootstrap-workstation-kubuntu.sh --dry-run`
- `bash -n scripts/bootstrap-workstation-kubuntu.sh`

## Handoff notes for Phase 0 continuation

Phase 0 is not closed. The next Phase 0 slice should be based on the latest tar and should close only after the target workstation proves every required tool and PostgreSQL service check with a clean `scripts/verify-workstation.sh` run.
