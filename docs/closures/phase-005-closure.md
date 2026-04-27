# Phase 005 Closure: Base Layout Shell

## Phase and title

Phase 5: Base Layout Shell

## Closure status

Complete.

## Scope completed

- Added reusable public shell components for site frame, navigation, and footer.
- Updated the root layout to wrap route content with `SiteShell`.
- Kept navigation route-safe by avoiding links to unbuilt public routes.
- Converted the root page into slot-friendly placeholder content inside the shell.
- Added a skip link and a single shell-owned `main` landmark.
- Added a responsive content container and dark futuristic baseline shell using Phase 4 Tailwind tokens.
- Added a Phase 5 shell validator and wired it into the professional CI lane.
- Strengthened the Phase 5 validator to check closure/progress/golden state after the phase closes.
- Updated spec, golden, progress state, progress log, README, phase index, and checklist evidence.

## Checklist status

Complete.

- The site has a clean reusable shell.
- The root layout composes `SiteShell` and does not own page content.
- The page route does not create a competing `main` landmark after the shell owns it.
- Navigation exists and does not link to unbuilt routes.
- Footer exists and stays layout-only.
- All expected artifacts exist and match the Phase 5 scope.
- The Phase 5 source-shape and closure drift check is wired into the professional CI lane.
- Owner workstation runtime/browser proof was reported green before closure.
- Global completion laws are satisfied.
- Prior locked behavior still passes.

## Behavior proven

- `scripts/check_phase_site_shell.py` validates the shell file shape, landmark ownership, route-safe navigation, footer boundary, Phase 5 placeholder boundary, and closed Phase 5 progress/docs state.
- The professional CI lane validates Phase 0 through Phase 5 artifacts and the Phase 5 shell validator.
- Owner workstation proof reported green for `pnpm check`, `pnpm build`, Vite dev readiness, desktop/mobile `/` smoke, and professional CI.

## Commands/tests run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/check_phase_site_shell.py
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py quick
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py professional
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py release
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py enterprise
node --check app/svelte.config.js
python3 -S -m json.tool app/package.json
git diff --check
find app scripts infra docs -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" -o -name "*.py" \) -not -path "app/node_modules/*" -not -path "app/.svelte-kit/*" -print0 | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_005_close_site_shell.patch
```

Owner workstation proof reported before closure:

```bash
cd app
pnpm check
pnpm build
pnpm dev
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

Result: green and ready for next slice.

## Files changed

- `README.md`
- `docs/project/phase-plan.md`
- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/specs/phase-005-spec.md`
- `docs/closures/phase-005-closure.md`
- `docs/goldens/phase-005.md`
- `scripts/check_phase_site_shell.py`

## Known limitations

None for Phase 5.

## Architecture laws checked

- Components own appearance only.
- No database, auth, media, filesystem, route action, or persistence behavior was added.
- Route files stay thin; `+layout.svelte` only composes shell and imports CSS.
- Navigation avoids broken links to unbuilt routes.
- New implementation files stay under 1,000 LOC.
- Logic/layout boundaries remain clean.

## Deferred work confirmation

No Phase 5 work is deferred. Phase 6 static landing content is a future phase item and is not required by the Phase 5 checklist.
