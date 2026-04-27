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

Phase 0, Phase 1, Phase 2, and Phase 3 are complete. Phase 4 is in progress and must stay scoped to TailwindCSS infrastructure until the Tailwind runtime proof is locked.

## Near-term sequence

```txt
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
- professional local CI lane with all new phase tests and golden checks wired before closure
- `git apply --check` proof for the generated patch
