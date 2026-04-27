# Phase 005 Closure: Base Layout Shell

## Phase and title

Phase 5: Base Layout Shell

## Closure status

Open. This patch implements the source shell and CI validator, but Phase 5 is not complete until runtime/browser proof is captured from the owner workstation.

## Scope completed in this patch

- Added reusable public shell components for site frame, navigation, and footer.
- Updated the root layout to wrap route content with `SiteShell`.
- Kept navigation route-safe by avoiding links to unbuilt public routes.
- Converted the root page into slot-friendly placeholder content inside the shell.
- Added a Phase 5 shell validator and wired it into the professional CI lane.
- Updated spec, golden, progress state, progress log, README, phase index, and checklist evidence.

## Checklist status

Complete in source shape:

- Root layout exists and composes the shell.
- Navigation component exists.
- Footer component exists.
- Responsive main container exists.
- Dark futuristic baseline uses the existing Phase 4 Tailwind tokens.
- Professional CI validates Phase 5 source artifacts.

Still required before closure:

- Owner workstation `pnpm check` proof.
- Owner workstation `pnpm build` proof.
- Owner workstation `pnpm dev` readiness proof.
- Browser smoke for `/` at desktop and mobile widths.
- Owner workstation professional CI proof after the app smokes.

## Behavior proven

- Patch environment validates source shape through `scripts/check_phase_site_shell.py`.
- Patch environment validates prior phase gates through the professional CI lane.
- Runtime/browser behavior has not been claimed yet.

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
git apply --check /mnt/data/phase_005_site_shell_start.patch
```

## Files changed

- `README.md`
- `app/src/routes/+layout.svelte`
- `app/src/routes/+page.svelte`
- `app/src/lib/components/site/SiteShell.svelte`
- `app/src/lib/components/site/SiteNav.svelte`
- `app/src/lib/components/site/SiteFooter.svelte`
- `ci/master_ci_runner.yaml`
- `docs/multiverse_codex_phase_completion_checklist.md`
- `docs/project/phase-plan.md`
- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/specs/phase-005-spec.md`
- `docs/closures/phase-005-closure.md`
- `docs/goldens/phase-005.md`
- `scripts/check_phase_site_shell.py`

## Known limitations

Phase 5 is open. Runtime/browser proof must be captured before this phase can close.

## Architecture laws checked

- Components own appearance only.
- No database, auth, media, filesystem, route action, or persistence behavior was added.
- Route files stay thin; `+layout.svelte` only composes shell and imports CSS.
- Navigation avoids broken links to unbuilt routes.
- New implementation files stay under 1,000 LOC.

## Deferred work confirmation

No Phase 5 source-scope work is deferred by this patch. Phase closure is withheld because required runtime/browser proof has not been captured yet.
