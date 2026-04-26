# Phase 003 Spec: SvelteKit App Scaffold

## Phase and title

Phase 3: SvelteKit App Scaffold

## Spec status

Phase 3 is complete.

## Implemented behavior

The `app/` root contains a SvelteKit TypeScript scaffold:

- `app/package.json` declares SvelteKit, TypeScript, Vite, Svelte, adapter-auto, svelte-check, pnpm, and dev/check/build/preview scripts.
- `app/pnpm-lock.yaml` locks the installed dependency graph.
- `app/svelte.config.js` configures adapter-auto and Vite preprocessing.
- `app/vite.config.ts` configures the SvelteKit Vite plugin.
- `app/tsconfig.json` extends SvelteKit's generated TypeScript config.
- `app/src/app.d.ts` defines the global App namespace seam.
- `app/src/app.html` defines the SvelteKit document shell.
- `app/src/routes/+page.svelte` renders a minimal default Multiverse Codex scaffold page.
- `scripts/check_phase_app_scaffold.py` validates the scaffold file shape and lockfile without requiring dependency execution.

## Public/admin routes touched

Public route scaffold added:

- `/` through `app/src/routes/+page.svelte`

No admin routes were added.

## Domain modules touched

None. Phase 3 is framework scaffolding only.

## Data models touched

None. No database schema, persistence, or seed data was added.

## Guards/seams added

- App-level TypeScript seam starts in `app/src/app.d.ts`.
- CI seam includes `scripts/check_phase_app_scaffold.py` and `ci/master_ci_runner.yaml`.
- Framework config remains in dedicated config files instead of route code.
- The pnpm lockfile is now required by professional CI before Phase 3 can remain closed.

## Tests/smokes added

- `scripts/check_phase_app_scaffold.py`
- Professional CI requires Phase 3 spec, closure, golden, pnpm lockfile, and scaffold shape.

## Closure evidence

Target workstation checks were run by the owner after applying the scaffold:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

Owner-reported result:

```txt
Vite booted and reported ready.
CI lanes pass cleanly.
```

## Handoff notes for next phase

Phase 4 should add TailwindCSS infrastructure only:

- TailwindCSS/PostCSS configuration
- global CSS entry
- base theme tokens
- `docs/design/theme.md`
- professional CI updates for Tailwind evidence

Do not build the layout shell, navigation, footer, or landing page polish in Phase 4.
