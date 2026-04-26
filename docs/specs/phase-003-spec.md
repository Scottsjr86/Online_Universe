# Phase 003 Spec: SvelteKit App Scaffold

## Phase and title

Phase 3: SvelteKit App Scaffold

## Spec status

Phase 3 is started but not closed in this patch.

The scaffold files exist and the repo-owned professional CI lane verifies their shape. The phase cannot close until the target workstation generates and commits `app/pnpm-lock.yaml`, runs dependency install, runs SvelteKit check/build, and proves the dev server starts.

## Implemented behavior

The `app/` root now contains a SvelteKit TypeScript scaffold:

- `app/package.json` declares SvelteKit, TypeScript, Vite, Svelte, adapter-auto, svelte-check, and pnpm.
- `app/svelte.config.js` configures adapter-auto and Vite preprocessing.
- `app/vite.config.ts` configures the SvelteKit Vite plugin.
- `app/tsconfig.json` extends SvelteKit's generated TypeScript config.
- `app/src/app.d.ts` defines the global App namespace seam.
- `app/src/app.html` defines the SvelteKit document shell.
- `app/src/routes/+page.svelte` renders a minimal default Multiverse Codex scaffold page.
- `scripts/check_phase_app_scaffold.py` validates the scaffold file shape without requiring installed dependencies.

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
- CI seam added through `scripts/check_phase_app_scaffold.py` and `ci/master_ci_runner.yaml`.
- Framework config remains in dedicated config files instead of route code.

## Tests/smokes added

- `scripts/check_phase_app_scaffold.py`
- Professional CI now requires Phase 3 spec/golden evidence and runs the scaffold shape check.

## Required checks before closure

Phase 3 cannot be called complete until these commands pass on the target workstation and their evidence is added to the golden:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
```

The generated `app/pnpm-lock.yaml` must be committed before closure.

## Handoff notes for next patch

Stay in Phase 3. The next patch should consume a new tar that includes the generated lockfile and owner-run SvelteKit smoke evidence, then close Phase 3 only after the professional lane and app checks pass.
