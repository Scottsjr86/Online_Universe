# Multiverse Codex Phase Plan Index

## Canonical plan source

The authoritative high-level build plan lives at:

```txt
docs/multiverse_codex_phase_plan.md
```

The authoritative completion checklist lives at:

```txt
docs/multiverse_codex_phase_completion_checklist.md
```

The architecture laws live at:

```txt
docs/multiverse_codex_architecture_laws.md
```

## Current status

Phase 0 is complete. Phase 1 creates the repository skeleton and records the first stable project layout.

## Near-term sequence

```txt
Phase 1: Repository Skeleton
Phase 2: Project Vision and Naming Lock
Phase 3: SvelteKit App Scaffold
Phase 4: TailwindCSS Setup
Phase 5: Base Layout Shell
Phase 6: Static Landing Page
```

## Patch discipline

Every phase must ship with:

- implementation or documentation artifacts matching that phase scope
- progress state update
- append-only progress log entry
- spec file
- closure file
- golden evidence
- smoke checks
- `git apply --check` proof for the generated patch
