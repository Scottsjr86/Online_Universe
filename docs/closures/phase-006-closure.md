# Phase 006 Closure: Static Landing Page

## Phase and title

Phase 6: Static Landing Page

## Status

In progress.

## Scope completed in this patch

- Replaced the Phase 5 placeholder homepage with a polished static landing page.
- Added the required hero section.
- Added the required universe teaser section.
- Added the required featured worlds placeholder section.
- Added the required featured characters placeholder section.
- Added the required call-to-action into the codex section.
- Kept CTA links route-safe by using in-page anchors until future public content routes exist.
- Added a Phase 6 targeted validator and wired it into professional CI.
- Updated Phase 6 checklist, spec, golden evidence, progress state, and progress log.

## Checklist status

- Landing implementation exists: complete for source shape.
- Required sections exist: complete for source shape.
- No database, admin, media, auth, search, or content-route behavior added: complete.
- Targeted validator added: complete.
- Professional CI lane wired: complete.
- Workstation `pnpm check`, `pnpm build`, `pnpm dev`, desktop/mobile `/` smoke: pending owner run.
- Phase 6 closure: not complete until workstation runtime proof is recorded.

## Behavior proven

The source-level landing page shape is proven by `scripts/check_phase_landing_page.py`. Runtime SvelteKit behavior must be proven on the owner workstation before closure.

## Commands/tests run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/check_phase_landing_page.py
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py quick
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py professional
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py release
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py enterprise
node --check app/svelte.config.js
python3 -S -m json.tool app/package.json
git diff --check
find app scripts infra docs -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" -o -name "*.py" \) -not -path "app/node_modules/*" -not -path "app/.svelte-kit/*" -print0 | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_006_static_landing_start.patch
```

## Files changed

- `README.md`
- `app/src/routes/+page.svelte`
- `ci/master_ci_runner.yaml`
- `docs/multiverse_codex_phase_completion_checklist.md`
- `docs/project/phase-plan.md`
- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/specs/phase-006-spec.md`
- `docs/closures/phase-006-closure.md`
- `docs/goldens/phase-006.md`
- `scripts/check_phase_landing_page.py`
- `scripts/check_phase_site_shell.py`

## Known limitations

Phase 6 is not closed in this patch because workstation runtime proof has not been recorded in the authoritative tar yet. This does not defer Phase 6 scope; it blocks closure until the required smoke evidence exists.

## Architecture laws checked

- Pre-existing canonical control docs over 1,000 LOC were reviewed. `docs/multiverse_codex_phase_completion_checklist.md` remains intentionally canonical until a future project-control split is explicitly planned; this patch only updates the Phase 6 checklist contract inside it.

- The page is static presentation only.
- No persistence, validation, auth, admin, media, database, filesystem, or route action logic was added.
- CTA links avoid unbuilt route targets.
- New implementation files stay under 1,000 LOC.
- The Phase 5 shell remains the only owner of the `main` landmark.

## Deferred work confirmation

No required Phase 6 implementation scope is deferred. Closure is blocked only by missing workstation runtime proof, which is required evidence for this phase.
