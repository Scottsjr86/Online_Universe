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

Phase 0 and Phase 1 are complete. Phase 2 locks the project identity, public/private product split, content vocabulary, and minimum launch target.

## Near-term sequence

```txt
Phase 2: Project Vision and Naming Lock
Phase 3: SvelteKit App Scaffold
Phase 4: TailwindCSS Setup
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
