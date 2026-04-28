# Phase 006 Spec: Static Landing Page

## Phase and title

Phase 6: Static Landing Page

## Status

In progress.

## Implemented behavior

- `app/src/routes/+page.svelte` now renders the first polished static public landing page inside the Phase 5 shell.
- The page includes the required Phase 6 sections:
  - hero
  - universe teaser
  - featured worlds placeholder
  - featured characters placeholder
  - call-to-action into the codex
- The landing page uses static arrays inside the page component for teaser card content only.
- The call-to-action points to in-page anchors instead of unbuilt public routes.
- Page metadata is defined through `<svelte:head>`.
- No database, admin, auth, media, search, or content-route behavior was added.

## Public/admin routes touched

- `app/src/routes/+page.svelte`

No admin routes exist yet.

## Domain modules touched

None. Phase 6 is static public presentation only.

## Data models touched

None.

## Guards/seams added

- Landing-page scope seam: `scripts/check_phase_landing_page.py` validates required static sections, rejects Phase 5 placeholder residue, rejects links to unbuilt public routes, and confirms Phase 6 remains open until workstation proof is recorded.
- Phase 5 regression seam: `scripts/check_phase_site_shell.py` now allows later phases to replace homepage content while still requiring the shell wrapper and prior Phase 5 closure proof.
- Professional CI seam: `ci/master_ci_runner.yaml` requires Phase 6 spec, closure evidence, golden evidence, and the landing-page validator.

## Tests/smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_landing_page.py`
- Professional CI lane includes Phase 6 artifacts and the Phase 6 landing-page validator.

## Handoff notes for next slice

Phase 6 must stay open until the owner runs `pnpm check`, `pnpm build`, `pnpm dev`, desktop/mobile `/` browser smoke, and professional CI from the workstation. Once that proof exists in the next authoritative tar, close Phase 6 by updating progress, closure, golden, and the validator closure drift check.
