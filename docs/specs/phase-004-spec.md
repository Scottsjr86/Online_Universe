# Phase 004 Spec: TailwindCSS Setup

## Phase and title

Phase 4: TailwindCSS Setup

## Status

Complete.

## Implemented behavior

- `app/package.json` declares TailwindCSS, the Tailwind Vite plugin, and PostCSS as dev dependencies.
- `app/pnpm-lock.yaml` records those dependencies after workstation install.
- `app/vite.config.ts` loads `tailwindcss()` before `sveltekit()`.
- `app/src/app.css` imports Tailwind and defines the initial Codex theme tokens.
- `app/src/routes/+layout.svelte` imports the global CSS entry.
- `app/src/routes/+page.svelte` proves Tailwind utilities render on the existing scaffold page.
- `app/tailwind.config.js` records source scanning and initial theme extension.
- `app/postcss.config.js` creates the PostCSS seam.
- `docs/design/theme.md` documents the token contract.
- `scripts/check_phase_tailwind_setup.py` validates Phase 4 artifacts and lockfile drift.
- The professional CI lane runs the Phase 4 validator.

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
- Professional CI lane includes the Phase 4 validator.
- Workstation app smoke covers `pnpm install`, `pnpm check`, `pnpm build`, and `pnpm dev` readiness.

## Handoff notes for next phase

Phase 5 may build the public site frame on top of the Tailwind tokens. Keep Phase 5 scoped to root layout shell, main navigation, footer, responsive container, and baseline futuristic theme. Do not build content pages in Phase 5.
