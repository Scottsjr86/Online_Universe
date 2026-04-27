# Phase 004 Golden: TailwindCSS Setup

## Phase and title

Phase 4: TailwindCSS Setup

## Golden status

In progress. This golden records the Tailwind setup slice and must be updated with
workstation runtime proof before Phase 4 closes.

## Exact scope completed

- Declared TailwindCSS, `@tailwindcss/vite`, and PostCSS dev dependencies.
- Wired `tailwindcss()` into Vite before `sveltekit()`.
- Added global CSS entry and root layout import.
- Added initial Codex design tokens.
- Added theme documentation.
- Converted the scaffold page to Tailwind utility classes.
- Added and wired a Phase 4 setup validator into professional CI.

## Files changed

- `README.md`
- `Makefile`
- `app/package.json`
- `app/postcss.config.js`
- `app/tailwind.config.js`
- `app/vite.config.ts`
- `app/src/app.css`
- `app/src/routes/+layout.svelte`
- `app/src/routes/+page.svelte`
- `ci/master_ci_runner.yaml`
- `docs/design/theme.md`
- `docs/multiverse_codex_phase_completion_checklist.md`
- `docs/project/phase-plan.md`
- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/specs/phase-004-spec.md`
- `docs/closures/phase-004-closure.md`
- `docs/goldens/phase-004.md`
- `scripts/check_phase_tailwind_setup.py`

## Commands run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/check_phase_tailwind_setup.py
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py quick
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py professional
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py release
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py enterprise
node --check app/svelte.config.js
python3 -m json.tool app/package.json
git diff --check
find app scripts infra docs -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" -o -name "*.py" \) -not -path "app/node_modules/*" -not -path "app/.svelte-kit/*" -print0 | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_004_tailwind_setup_repair.patch
```

## Test/smoke output summary

- Phase 4 setup validator passed in the patch environment.
- All repo-owned CI lanes passed in the patch environment.
- App runtime checks are not yet locked for this phase in the authoritative base.

## Evidence snippets

```txt
[PASS] Phase 4 Tailwind setup artifacts verified
```

## Known limitations

- `app/pnpm-lock.yaml` still needs to be refreshed on the workstation after dependency installation.
- `pnpm check`, `pnpm build`, Vite dev readiness, and professional CI output still need to be
  recorded before closing Phase 4.

## Final commit hash

Patch workflow baseline only. Final project commit hash must be recorded after applying the
verified patch in the real repository.

## Hard no review

- No new implementation file added by this patch exceeds 1,000 LOC. The canonical phase plan and checklist remain pre-existing oversized control documents and are recorded as review exceptions while the phase remains open.
- No logic/layout mixing was introduced.
- No Tailwind setup is counted as a layout shell.
- No Phase 5 or Phase 6 scope was started.
- No secrets, production media, database changes, or auth changes were added.
- No `.gitkeep` sentinels were reintroduced.
