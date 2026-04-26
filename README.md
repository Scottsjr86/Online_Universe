# Multiverse Codex

Multiverse Codex is a self-hosted fantasy universe codex built through small, verified, phase-aligned patches.

The finished project will become a public lore site and creator-owned admin tool for worlds, characters, artifacts, factions, stories, timelines, media, relationships, and a later 3D cosmic viewport.

## Current phase state

- Last completed phase: Phase 0, Workstation Bootstrap
- Current phase after this patch: Phase 1, Repository Skeleton
- Next candidate phase: Phase 2, Project Vision and Naming Lock

Machine-readable state lives in `docs/progress.json`.
Append-only patch history lives in `docs/progress.jsonl`.

## Repository layout

```txt
multiverse-codex/
  app/      Application source root, beginning in Phase 3.
  docs/     Project control docs, specs, closures, goldens, and design notes.
  infra/    Native deployment, Caddy, systemd, and ops configuration.
  scripts/  Workstation, dev, build, database, and ops scripts.
```

## Canonical project-control docs

```txt
docs/multiverse_codex_phase_plan.md
docs/multiverse_codex_phase_completion_checklist.md
docs/multiverse_codex_architecture_laws.md
docs/multiverse_codex_fresh_chat_workflow_header.md
```

These documents define the build order, closure contract, architecture laws, and patch workflow.

## Phase 1 smoke checks

```bash
git status --short
make help
```

## Workstation verification

Phase 0 added the workstation verifier:

```bash
scripts/verify-workstation.sh
```

Run it on the primary workstation when host-tool drift is suspected.
