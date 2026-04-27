# Phase 004 Spec: TailwindCSS Setup

## Phase and title

Phase 4: TailwindCSS Setup

## Status

Phase 4 is in progress. This patch installs the Tailwind/PostCSS source contract and CI
shape checks. It does not close the phase until the workstation lockfile, `pnpm check`,
`pnpm build`, Vite dev-server proof, and professional CI output are recorded.

## Implemented behavior

- `app/package.json` declares TailwindCSS, the Tailwind Vite plugin, and PostCSS as dev dependencies.
- `app/vite.config.ts` loads `tailwindcss()` before `sveltekit()`.
- `app/src/app.css` imports Tailwind and defines the initial Codex theme tokens.
- `app/src/routes/+layout.svelte` imports the global CSS entry.
- `app/src/routes/+page.svelte` proves Tailwind utilities render on the existing scaffold page.
- `app/tailwind.config.js` records source scanning and initial theme extension.
- `app/postcss.config.js` creates the PostCSS seam.
- `docs/design/theme.md` documents the token contract.
- `scripts/check_phase_tailwind_setup.py` validates Phase 4 artifacts.
- The professional CI lane runs the Phase 4 Tailwind setup validator.

## Public/admin routes touched

- `app/src/routes/+layout.svelte`
- `app/src/routes/+page.svelte`

No admin routes exist yet.

## Domain modules touched

None. Phase 4 is styling infrastructure only.

## Data models touched

None.

## Guards/seams added

- Global CSS entry seam: `app/src/app.css`
- Tailwind/Vite plugin seam: `app/vite.config.ts`
- PostCSS seam: `app/postcss.config.js`
- Theme documentation seam: `docs/design/theme.md`
- CI validation seam: `scripts/check_phase_tailwind_setup.py`

## Tests/smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_tailwind_setup.py`
- Professional CI lane now includes the Phase 4 validator.

## Handoff notes for next patch

The next Phase 4 patch must come from a tar that includes the refreshed `app/pnpm-lock.yaml`
after `pnpm install`, plus workstation proof for `pnpm check`, `pnpm build`, Vite dev server
readiness, and `scripts/run_ci.py professional`. Only then can Phase 4 close.
