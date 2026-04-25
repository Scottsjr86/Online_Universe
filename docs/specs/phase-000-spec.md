# Phase 000 Spec: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Implemented behavior

Phase 0 provides and verifies the local workstation toolchain required to build Multiverse Codex through the next project phases.

Implemented repository-side behavior:

- `scripts/verify-workstation.sh` checks required command availability and version output.
- The verification probe checks PostgreSQL service availability through `systemctl is-active postgresql`.
- The verification probe exits nonzero when a required tool or service check fails.
- `MULTIVERSE_CODEX_DEBUG=1` enables gated command-level probe output for diagnosing failures.
- `scripts/bootstrap-workstation-kubuntu.sh` provides a Kubuntu/Ubuntu bootstrap helper with dry-run as the default behavior.
- `scripts/bootstrap-workstation-kubuntu.sh --install` installs Phase 0 workstation tools, configures package repositories for Node and Caddy, enables pnpm, and starts/enables PostgreSQL.
- The Caddy apt setup uses `/usr/share/keyrings/caddy-stable-archive-keyring.gpg` so the downloaded Caddy source list can verify the repository signature.
- `docs/dev/workstation.md` documents required tools, verification commands, expected success behavior, expected failure behavior, and troubleshooting notes.
- `docs/progress.json` records the machine-readable phase state.
- `docs/progress.jsonl` records append-only patch history.

## Verified workstation state

The primary Kubuntu 25.10 workstation returned a clean `scripts/verify-workstation.sh` transcript with passing probes for:

- Git 2.51.0
- Node v24.14.1
- pnpm 10.33.2
- PostgreSQL client 17.9
- systemd 257
- Caddy 2.6.2
- GNU Make 4.4.1
- curl 8.14.1
- jq 1.8.1
- OpenSSL 3.5.3
- active PostgreSQL service

## Public/admin routes touched

None. No app exists yet.

## Domain modules touched

None. No domain modules exist yet.

## Data models touched

None. No data models exist yet.

## Guards and seams added

- Workstation verification fails closed when a required command or service is missing.
- Debug output is gated by `MULTIVERSE_CODEX_DEBUG=1`.
- Bootstrap helper defaults to dry-run.
- Bootstrap helper requires explicit `--install` for host mutation.
- Bootstrap helper rejects unknown arguments instead of guessing.
- Bootstrap helper validates Ubuntu-family hosts before install mode.
- Caddy repository keyring setup removes stale keyring copies before installing the refreshed key.

## Tests and smokes added

- `scripts/verify-workstation.sh`
- `scripts/bootstrap-workstation-kubuntu.sh --dry-run`
- `bash -n scripts/verify-workstation.sh`
- `bash -n scripts/bootstrap-workstation-kubuntu.sh`

## Handoff notes for Phase 1

Phase 1 can begin from the next authoritative tar. The repo has proven workstation foundations and should next create the repository skeleton artifacts required by the phase plan: `app/`, `infra/`, `README.md`, `Makefile`, and project documentation.
