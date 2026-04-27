# Phase 005 Spec: Base Layout Shell

## Phase and title

Phase 5: Base Layout Shell

## Status

In progress. The source shell is implemented and wired into professional CI shape checks. Runtime/browser proof is still required before closure.

## Implemented behavior

- `app/src/routes/+layout.svelte` imports the global Tailwind CSS entry and wraps all routes with `SiteShell`.
- `app/src/lib/components/site/SiteShell.svelte` owns the reusable public frame, skip link, responsive main landmark, and page structure.
- `app/src/lib/components/site/SiteNav.svelte` owns the main navigation region and only links to currently available routes.
- `app/src/lib/components/site/SiteFooter.svelte` owns the public footer region.
- `app/src/routes/+page.svelte` no longer owns the `main` landmark; it renders a small slot-friendly placeholder inside the shell.
- `scripts/check_phase_site_shell.py` validates the shell file shape, landmark split, route-safe navigation, and Phase 5 placeholder boundary.
- The professional CI lane now requires Phase 5 shell artifacts and runs the shell validator.

## Public/admin routes touched

- `app/src/routes/+layout.svelte`
- `app/src/routes/+page.svelte`

No admin routes exist yet.

## Domain modules touched

None. Phase 5 is layout shell only.

## Data models touched

None.

## Guards/seams added

- Layout shell seam: `app/src/lib/components/site/SiteShell.svelte`
- Navigation seam: `app/src/lib/components/site/SiteNav.svelte`
- Footer seam: `app/src/lib/components/site/SiteFooter.svelte`
- Accessibility seam: skip link plus single route-level `main` landmark in the shell
- CI validation seam: `scripts/check_phase_site_shell.py`

## Tests/smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_site_shell.py`
- Professional CI lane includes Phase 5 artifact requirements and the Phase 5 shell validator.

## Handoff notes for next phase

Phase 5 must not close until the owner workstation proves `pnpm check`, `pnpm build`, Vite dev readiness, desktop/mobile route smoke for `/`, and professional CI. Phase 6 remains the first static landing page phase and should build content sections only after this shell is closed.
