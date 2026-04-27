# Multiverse Codex Phase Completion Checklist

This is the closure contract for the Multiverse Codex build. A phase is complete only when intent, behavior, tests, documentation, and golden evidence all lock together.

## Global Completion Laws

- [ ] Every phase is single-purpose. If the work braids unrelated objectives together, split the phase.
- [ ] No module, component, route file, server utility, script, or test file may exceed 1,000 LOC. Split before crossing the ceiling.
- [ ] Logic and layout never mix. Keep data loading, validation, persistence, filesystem work, auth, media processing, deployment logic, and rendering in separate modules whenever possible.
- [ ] No deferred work ever. No TODO, FIXME, placeholder, stub, mocked success, or later note may be used to call a phase complete.
- [ ] Every phase ends with code committed, tests or smoke checks run, docs updated, and a golden file created or updated.
- [ ] Validation must be reproducible from a clean checkout, clean database, or clean VM depending on the phase.
- [ ] A phase cannot close if it breaks any previously locked golden unless the current phase intentionally updates that golden with a justified behavior change.
- [ ] When a test fails, add or use gated debugging around the failure area, fix the issue, keep useful gated debug hooks, and remove noisy debug-only execution paths.

## Local CI Law

Every phase closure must run through the repo-owned master CI runner before it can close.

- [ ] `ci/master_ci_runner.yaml` exists and defines `quick`, `professional`, `release`, and `enterprise` lanes.
- [ ] `scripts/run_ci.py` reads `ci/master_ci_runner.yaml`, supports `--list`, accepts one lane argument, rejects unknown lanes, and runs commands from the repo root.
- [ ] CI commands run in manifest order, print numbered steps, stream stdout/stderr, stop on first failure, and return the failed command's exit code.
- [ ] The runner avoids arbitrary command execution from user input; user input may select only a manifest-defined lane.
- [ ] The runner avoids `shell=True`; manifest commands are tokenized and run directly.
- [ ] Manifest commands must reflect real repo tooling. Do not invent lint, typecheck, test, e2e, audit, or build commands before those tools exist.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py quick` passes for fast patch-loop checks.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional` passes before any phase is marked complete.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py release` passes when preparing a release-grade handoff.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py enterprise` passes for the deepest local verification currently available.
- [ ] `make ci-list`, `make ci-quick`, `make ci-professional`, `make ci-release`, `make ci-enterprise`, and `make phase-close` route to the master CI runner.
- [ ] New tests, smokes, drift checks, or golden checks added by a phase are wired into the professional lane before closure.
- [ ] Golden evidence records the CI lane output used to close the phase.
- [ ] No `.gitkeep` sentinels are used to preserve directories; use explicit README notes or real tracked files.

## Required Golden Format

Each phase locks evidence in `docs/goldens/phase-###.md`.

- [ ] Phase number and title
- [ ] Exact scope completed
- [ ] Files changed
- [ ] Commands run
- [ ] Test/smoke output summary
- [ ] Screenshots, Playwright traces, schema/query snapshots, logs, or terminal snippets where relevant
- [ ] Known limitations, with none allowed if they violate phase intent
- [ ] Final commit hash
- [ ] Hard no's reviewed and clean

## Phase Checklist

### Phase 0: Workstation Bootstrap

**Intent:** Prepare the local development machine with required tools.

**Scope lock:** Install and verify: `git; node LTS; pnpm; postgresql server; postgres client tools; caddy; systemd; make; curl; jq; openssl` Optional but recommended: `direnv; nvm / fnm / asdf; VS Code / VSCodium; DBeaver / pgAdmin`

**Expected artifacts:** `docs/dev/workstation.md` Include: `installed tools; versions; verification commands; troubleshooting notes`

**What must be true to call this phase fully complete:**

- [ ] The workstation can run Node, pnpm, Git, PostgreSQL server/client tools, Caddy, and systemd service commands.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `node --version; pnpm --version; git --version; psql --version; systemctl --version; caddy version`
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-000.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for `pnpm install`, `pnpm check`, `pnpm build`, `pnpm dev`, and professional CI.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No `.gitkeep` sentinels; tracked empty roots must use explicit README notes or real purpose-owned files.

### Phase 1: Repository Skeleton

**Intent:** Create the empty project repository structure.

**Scope lock:** Create top-level layout: `multiverse-codex/; app/; docs/; infra/; scripts/; .gitignore; README.md; Makefile`

**Expected artifacts:** `README.md; docs/project/vision.md; docs/project/phase-plan.md; .gitignore; Makefile; app/README.md; infra/README.md; ci/master_ci_runner.yaml; scripts/run_ci.py`

**What must be true to call this phase fully complete:**

- [ ] The repo exists, is committed, and has a clear starting structure.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `git status; make help`
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py --list` lists all lanes.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py quick` passes.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional` passes before closure.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py release` passes for release-grade handoff confidence.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py enterprise` passes for deepest local confidence.
- [ ] `make phase-close` passes and maps to the professional lane.
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-001.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 2: Project Vision and Naming Lock

**Intent:** Define the project identity before code sprawl begins.

**Scope lock:** Document: `project name; tone and visual direction; core content types; target audience; public/private split; minimum viable launch target`

**Expected artifacts:** `docs/project/vision.md; docs/project/content-types.md; scripts/check_phase_identity.py; CI professional lane checks for Phase 2 spec/closure/golden and identity smoke`

**What must be true to call this phase fully complete:**

- [ ] The project has a stable identity and agreed content model vocabulary.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run targeted identity smoke: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_identity.py`.
- [ ] Run the canonical phase-close gate: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional`.
- [ ] Run `make phase-close` and confirm it maps to the professional lane.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-002.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include the identity smoke and professional CI lane output summary.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 3: SvelteKit App Scaffold

**Intent:** Create the initial SvelteKit app.

**Scope lock:** Inside `app/`, scaffold SvelteKit with TypeScript. Add: `SvelteKit; TypeScript; pnpm lockfile; basic dev server`

**Expected artifacts:** `app/package.json; app/pnpm-lock.yaml; app/src/; app/svelte.config.js; app/vite.config.ts; app/tsconfig.json`

**What must be true to call this phase fully complete:**

- [ ] The default app runs locally.
- [ ] `app/package.json` declares SvelteKit, TypeScript, Vite, pnpm, and dev/check/build/preview scripts.
- [ ] `app/pnpm-lock.yaml` exists after `pnpm install` and is committed before closure.
- [ ] Professional CI includes and passes `scripts/check_phase_app_scaffold.py`, the committed `app/pnpm-lock.yaml` requirement, and all Phase 3 golden/spec evidence checks.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `cd app; pnpm install; pnpm dev`
- [ ] Run `cd app; pnpm check` and `cd app; pnpm build` after dependencies are installed.
- [ ] Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_app_scaffold.py` from repo root.
- [ ] Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional` before closure.
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-003.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 4: TailwindCSS Setup

**Intent:** Add styling infrastructure.

**Scope lock:** Install and configure: `TailwindCSS; PostCSS; global CSS entry; base theme tokens` Create initial design tokens: `background colors; foreground colors; accent colors; border colors; spacing conventions; radius conventions; shadow conventions`

**Expected artifacts:** `app/tailwind.config.*; app/postcss.config.*; app/src/app.css; app/src/routes/+layout.svelte; docs/design/theme.md; scripts/check_phase_tailwind_setup.py`

**What must be true to call this phase fully complete:**

- [ ] The app can render custom styled pages using Tailwind.
- [ ] TailwindCSS, `@tailwindcss/vite`, and PostCSS are declared in `app/package.json` and reflected in `app/pnpm-lock.yaml` after workstation install.
- [ ] `app/src/app.css` is imported from `app/src/routes/+layout.svelte` and defines the base theme tokens.
- [ ] `scripts/check_phase_tailwind_setup.py` is wired into the professional CI lane before closure and checks both source artifacts and lockfile drift.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Render a page with Tailwind utility classes.
- [ ] Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_tailwind_setup.py` and confirm it validates package and lockfile state.
- [ ] Run `cd app; pnpm install; pnpm check; pnpm build; pnpm dev` and record Vite readiness.
- [ ] Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional` after the Phase 4 validator and golden checks are wired in.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-004.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No Phase 5 shell/navigation/footer work counted as Phase 4.
- [ ] No component-local CSS counted as Tailwind proof when a utility-class proof is required.

### Phase 5: Base Layout Shell

**Intent:** Create the public site frame.

**Scope lock:** Build: `root layout; main navigation; footer; responsive container; dark futuristic baseline theme` Do not build content pages yet.

**Expected artifacts:** `app/src/routes/+layout.svelte; app/src/lib/components/site/SiteShell.svelte; app/src/lib/components/site/SiteNav.svelte; app/src/lib/components/site/SiteFooter.svelte`

**What must be true to call this phase fully complete:**

- [ ] The site has a clean reusable shell.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit: `/` Confirm layout renders at desktop and mobile widths.
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-005.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 6: Static Landing Page

**Intent:** Create the first polished public page.

**Scope lock:** Build homepage sections: `hero; universe teaser; featured worlds placeholder; featured characters placeholder; call-to-action into codex` No database yet.

**Expected artifacts:** `app/src/routes/+page.svelte`

**What must be true to call this phase fully complete:**

- [ ] The homepage looks intentional, futuristic, and responsive.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `pnpm check; pnpm lint`
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-006.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 7: Local Native PostgreSQL Foundation

**Intent:** Create local database service orchestration without Docker.

**Scope lock:** Install and configure host PostgreSQL for local development. Create: `local database; local database user; local database lifecycle commands; optional init SQL directory` Do not containerize development or production.

**Expected artifacts:** `scripts/dev-db-create.sh; scripts/dev-db-reset.sh; scripts/dev-db-status.sh; docs/dev/postgres-native.md`

**What must be true to call this phase fully complete:**

- [ ] PostgreSQL runs locally as a native service and the app can reach the dev database without Docker.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `systemctl status postgresql; psql "$DATABASE_URL" -c 'select 1;'; scripts/dev-db-status.sh`
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-007.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 8: Environment Configuration

**Intent:** Standardize environment variables.

**Scope lock:** Create: `.env.example; app/src/lib/server/env.ts` Define required variables: `DATABASE_URL; SESSION_SECRET; PUBLIC_SITE_NAME; MEDIA_ROOT` Add validation.

**Expected artifacts:** `.env.example; docs/dev/environment.md`

**What must be true to call this phase fully complete:**

- [ ] Environment config is explicit, validated, and documented.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Run app with valid `.env`. Run app with missing env and confirm it fails clearly.
- [ ] Run setup/build/check commands from a clean shell and verify the documented happy path works without hidden local state.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-008.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 9: Database Connection

**Intent:** Connect SvelteKit server code to PostgreSQL.

**Scope lock:** Install and configure: `pg driver; Drizzle ORM; database client module` No tables yet.

**Expected artifacts:** `app/src/lib/server/db/client.ts; app/drizzle.config.ts`

**What must be true to call this phase fully complete:**

- [ ] The app can connect to PostgreSQL.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create a temporary health query: `select 1`
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-009.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 10: Database Migration System

**Intent:** Add repeatable schema migration workflow.

**Scope lock:** Configure: `Drizzle schema folder; migration generation; migration apply command; migration documentation`

**Expected artifacts:** `app/src/lib/server/db/schema/; app/drizzle/; docs/dev/migrations.md`

**What must be true to call this phase fully complete:**

- [ ] Schema changes can be generated and applied repeatably.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `pnpm db:generate; pnpm db:migrate`
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-010.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 11: Core Entity Base Schema

**Intent:** Create a shared entity foundation.

**Scope lock:** Add base table design for common canon entities. Create: `entities` Fields: `id; slug; type; name; summary; description; status; created_at; updated_at; published_at` Do not add specialized tables yet.

**Expected artifacts:** `schema entity base; migration; docs/data/entities.md`

**What must be true to call this phase fully complete:**

- [ ] The database has a generic entity foundation.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Run migration and inspect table.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-011.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 12: World Schema

**Intent:** Add worlds as the first real content type.

**Scope lock:** Create: `worlds` Fields: `entity_id; cosmology_notes; climate_notes; culture_notes; magic_or_tech_notes`

**Expected artifacts:** `world schema; migration; world type docs`

**What must be true to call this phase fully complete:**

- [ ] A world can exist in the database.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one test world through a seed script.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-012.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 13: Character Schema

**Intent:** Add character data model.

**Scope lock:** Create: `characters` Fields: `entity_id; alias; species; origin_world_id; status_in_story; power_notes; biography`

**Expected artifacts:** `character schema; migration; character type docs`

**What must be true to call this phase fully complete:**

- [ ] A character can exist and optionally reference an origin world.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one test character linked to a world.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-013.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 14: Artifact Schema

**Intent:** Add artifact data model.

**Scope lock:** Create: `artifacts` Fields: `entity_id; origin_world_id; current_location; power_notes; curse_notes; history`

**Expected artifacts:** `artifact schema; migration; artifact type docs`

**What must be true to call this phase fully complete:**

- [ ] An artifact can exist and optionally reference a world.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one test artifact.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-014.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 15: Faction Schema

**Intent:** Add faction data model.

**Scope lock:** Create: `factions` Fields: `entity_id; home_world_id; ideology; leader_notes; influence_notes`

**Expected artifacts:** `faction schema; migration; faction type docs`

**What must be true to call this phase fully complete:**

- [ ] A faction can exist and optionally reference a world.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one test faction.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-015.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 16: Story Schema

**Intent:** Add story-level content.

**Scope lock:** Create: `stories` Fields: `entity_id; title; subtitle; summary; body; canon_status; release_status` Do not add chapters yet.

**Expected artifacts:** `story schema; migration; story type docs`

**What must be true to call this phase fully complete:**

- [ ] A story can exist as a long-form written entry.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one test story.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-016.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 17: Chapter Schema

**Intent:** Add chapter-level story structure.

**Scope lock:** Create: `chapters` Fields: `story_id; chapter_number; slug; title; summary; body; status; published_at`

**Expected artifacts:** `chapter schema; migration; chapter docs`

**What must be true to call this phase fully complete:**

- [ ] Stories can contain ordered chapters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert one story with two chapters.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-017.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 18: Timeline Event Schema

**Intent:** Add timeline support.

**Scope lock:** Create: `timeline_events` Fields: `entity_id; era; year_label; sort_order; event_date_text; event_summary; event_body` Do not build UI yet.

**Expected artifacts:** `timeline schema; migration; timeline docs`

**What must be true to call this phase fully complete:**

- [ ] Timeline events can be stored and sorted.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert timeline events and query sorted order.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-018.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 19: Entity Relationship Schema

**Intent:** Create the canon graph.

**Scope lock:** Create: `entity_relationships` Fields: `id; source_entity_id; target_entity_id; relation_type; description; sort_order; created_at; updated_at` Example relation types: `appears_in; belongs_to; owns; created_by; enemy_of; ally_of; located_in; connected_to; caused; descended_from`

**Expected artifacts:** `relationship schema; migration; relationship docs`

**What must be true to call this phase fully complete:**

- [ ] Any entity can relate to any other entity.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Link character to world, artifact, faction, and story.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-019.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 20: Seed Data System

**Intent:** Create repeatable demo data.

**Scope lock:** Build seed script for: `one world; two characters; one artifact; one faction; one story; two chapters; three relationships; three timeline events`

**Expected artifacts:** `app/scripts/seed.ts; docs/dev/seeding.md`

**What must be true to call this phase fully complete:**

- [ ] A fresh database can be populated with demo universe content.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `pnpm db:seed`
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-020.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 21: Public World List Page

**Intent:** Render worlds from the database.

**Scope lock:** Build: `/worlds` Show: `name; summary; status; published date` No detail page yet.

**Expected artifacts:** `app/src/routes/worlds/+page.server.ts; app/src/routes/worlds/+page.svelte`

**What must be true to call this phase fully complete:**

- [ ] Worlds render publicly from PostgreSQL.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed data appears on `/worlds`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-021.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 22: Public World Detail Page

**Intent:** Render one world from the database.

**Scope lock:** Build: `/worlds/[slug]` Show: `name; summary; description; related characters; related artifacts; related stories`

**Expected artifacts:** `app/src/routes/worlds/[slug]/+page.server.ts; app/src/routes/worlds/[slug]/+page.svelte`

**What must be true to call this phase fully complete:**

- [ ] A world page can show connected canon data.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Click world from list to detail.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-022.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 23: Public Character List Page

**Intent:** Render characters from the database.

**Scope lock:** Build: `/characters` Show: `name; alias; origin world; summary`

**Expected artifacts:** `character list route; character card component`

**What must be true to call this phase fully complete:**

- [ ] Characters render publicly from PostgreSQL.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed characters appear on `/characters`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-023.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 24: Public Character Detail Page

**Intent:** Render one character from the database.

**Scope lock:** Build: `/characters/[slug]` Show: `name; alias; biography; origin world; related artifacts; related factions; related stories`

**Expected artifacts:** `character detail route; relationship display component`

**What must be true to call this phase fully complete:**

- [ ] A character page can show connected canon data.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Click character from list to detail.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-024.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 25: Public Artifact List Page

**Intent:** Render artifacts from the database.

**Scope lock:** Build: `/artifacts` Show: `name; origin world; summary`

**Expected artifacts:** `artifact list route; artifact card component`

**What must be true to call this phase fully complete:**

- [ ] Artifacts render publicly from PostgreSQL.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed artifacts appear on `/artifacts`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-025.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 26: Public Artifact Detail Page

**Intent:** Render one artifact from the database.

**Scope lock:** Build: `/artifacts/[slug]` Show: `name; history; power notes; curse notes; related characters; related worlds; related stories`

**Expected artifacts:** `artifact detail route`

**What must be true to call this phase fully complete:**

- [ ] An artifact page can show connected canon data.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Click artifact from list to detail.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-026.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 27: Public Story List Page

**Intent:** Render stories from the database.

**Scope lock:** Build: `/stories` Show: `title; summary; canon status; release status`

**Expected artifacts:** `story list route; story card component`

**What must be true to call this phase fully complete:**

- [ ] Stories render publicly from PostgreSQL.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed stories appear on `/stories`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-027.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 28: Public Story Detail Page

**Intent:** Render one story and chapter list.

**Scope lock:** Build: `/stories/[slug]` Show: `title; summary; body; chapter list; related worlds; related characters`

**Expected artifacts:** `story detail route; chapter list component`

**What must be true to call this phase fully complete:**

- [ ] A story page can show metadata and chapters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Click story from list to detail.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-028.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 29: Public Chapter Reader

**Intent:** Render individual chapters.

**Scope lock:** Build: `/stories/[storySlug]/chapters/[chapterSlug]` Show: `story title; chapter title; body; previous chapter; next chapter`

**Expected artifacts:** `chapter reader route; reader layout component`

**What must be true to call this phase fully complete:**

- [ ] Chapters can be read cleanly on desktop and mobile.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Navigate between chapters.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-029.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 30: Public Timeline Page

**Intent:** Render the universe timeline.

**Scope lock:** Build: `/timeline` Show timeline events sorted by: `era; sort_order; year_label`

**Expected artifacts:** `timeline route; timeline event component`

**What must be true to call this phase fully complete:**

- [ ] Timeline data renders publicly.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed timeline appears in correct order.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-030.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 31: Public Search Page

**Intent:** Add basic search across published content.

**Scope lock:** Build search over: `entities.name; entities.summary; entities.description; stories.body; chapters.body` Use PostgreSQL search or simple query matching initially.

**Expected artifacts:** `/search; server-side search query; search result component`

**What must be true to call this phase fully complete:**

- [ ] Users can search the codex.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Search can find seeded worlds, characters, artifacts, and stories.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-031.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 32: Admin Auth Schema

**Intent:** Create database support for creator login.

**Scope lock:** Create: `users; sessions` Fields: `email; password_hash; role; created_at; updated_at; expires_at`

**Expected artifacts:** `auth schema; migration; auth docs`

**What must be true to call this phase fully complete:**

- [ ] Admin identity can exist in database.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create local admin user through script.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-032.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 33: Password Hashing

**Intent:** Add secure password storage.

**Scope lock:** Install password hashing library. Create utilities for: `hash password; verify password`

**Expected artifacts:** `app/src/lib/server/auth/password.ts; tests for hash/verify`

**What must be true to call this phase fully complete:**

- [ ] Passwords are never stored in plain text.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Correct password verifies. Wrong password fails.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-033.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 34: Login Route

**Intent:** Create admin login.

**Scope lock:** Build: `/admin/login` Includes: `login form; server action; session creation; error states`

**Expected artifacts:** `login route; session cookie logic`

**What must be true to call this phase fully complete:**

- [ ] Admin login works locally.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Valid admin can log in. Invalid login fails.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-034.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 35: Logout Route

**Intent:** Create admin logout.

**Scope lock:** Build: `/admin/logout` Includes: `session deletion; cookie clearing; redirect`

**Expected artifacts:** `logout route`

**What must be true to call this phase fully complete:**

- [ ] Session can be terminated cleanly.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Logged-in admin can log out.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-035.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 36: Admin Route Guard

**Intent:** Protect admin pages.

**Scope lock:** Add server-side auth check for: `/admin/*` Redirect unauthenticated users to login.

**Expected artifacts:** `admin layout server guard; auth helper`

**What must be true to call this phase fully complete:**

- [ ] Admin area is protected.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Unauthenticated users cannot access `/admin`.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-036.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 37: Admin Dashboard Shell

**Intent:** Create the admin interface frame.

**Scope lock:** Build: `/admin` Includes: `sidebar; topbar; content area; logout control; quick stats placeholders`

**Expected artifacts:** `admin layout components; admin dashboard route`

**What must be true to call this phase fully complete:**

- [ ] Admin area has a reusable layout.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Logged-in admin sees dashboard.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-037.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 38: Admin World Create

**Intent:** Create worlds from the admin UI.

**Scope lock:** Build: `/admin/worlds/new` Fields: `name; slug; summary; description; status; world-specific fields`

**Expected artifacts:** `world create form; server action; validation`

**What must be true to call this phase fully complete:**

- [ ] Admin can create worlds without scripts.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create a world through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-038.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 39: Admin World Edit

**Intent:** Edit existing worlds.

**Scope lock:** Build: `/admin/worlds; /admin/worlds/[id]/edit` Includes: `list; edit form; update action; validation`

**Expected artifacts:** `world admin list; world edit route`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage worlds.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit a world and confirm public page updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-039.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 40: Admin Character Create

**Intent:** Create characters from the admin UI.

**Scope lock:** Build: `/admin/characters/new` Fields: `name; slug; alias; summary; biography; origin world; status; power notes`

**Expected artifacts:** `character create form; validation`

**What must be true to call this phase fully complete:**

- [ ] Admin can create characters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create character through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-040.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 41: Admin Character Edit

**Intent:** Edit existing characters.

**Scope lock:** Build: `/admin/characters; /admin/characters/[id]/edit`

**Expected artifacts:** `character admin list; character edit route`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage characters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit character and confirm public page updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-041.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 42: Admin Artifact Create

**Intent:** Create artifacts from the admin UI.

**Scope lock:** Build: `/admin/artifacts/new` Fields: `name; slug; summary; history; origin world; power notes; curse notes; status`

**Expected artifacts:** `artifact create form; validation`

**What must be true to call this phase fully complete:**

- [ ] Admin can create artifacts.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create artifact through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-042.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 43: Admin Artifact Edit

**Intent:** Edit existing artifacts.

**Scope lock:** Build: `/admin/artifacts; /admin/artifacts/[id]/edit`

**Expected artifacts:** `artifact admin list; artifact edit route`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage artifacts.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit artifact and confirm public page updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-043.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 44: Admin Story Create

**Intent:** Create stories from the admin UI.

**Scope lock:** Build: `/admin/stories/new` Fields: `title; slug; summary; body; canon status; release status`

**Expected artifacts:** `story create form; validation`

**What must be true to call this phase fully complete:**

- [ ] Admin can create stories.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create story through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-044.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 45: Admin Story Edit

**Intent:** Edit existing stories.

**Scope lock:** Build: `/admin/stories; /admin/stories/[id]/edit`

**Expected artifacts:** `story admin list; story edit route`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage stories.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit story and confirm public page updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-045.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 46: Admin Chapter Create

**Intent:** Create chapters from the admin UI.

**Scope lock:** Build: `/admin/stories/[storyId]/chapters/new` Fields: `chapter number; slug; title; summary; body; status`

**Expected artifacts:** `chapter create form; validation`

**What must be true to call this phase fully complete:**

- [ ] Admin can create chapters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create chapter through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-046.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 47: Admin Chapter Edit

**Intent:** Edit existing chapters.

**Scope lock:** Build: `/admin/stories/[storyId]/chapters/[chapterId]/edit`

**Expected artifacts:** `chapter edit form`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage chapters.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit chapter and confirm reader updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-047.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 48: Admin Relationship Manager

**Intent:** Manage canon graph links.

**Scope lock:** Build UI to create relationships: `source entity; relation type; target entity; description; sort order`

**Expected artifacts:** `/admin/relationships; relationship create form; relationship delete action`

**What must be true to call this phase fully complete:**

- [ ] Admin can connect entities without database scripts.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create relation through UI and confirm public detail page shows it.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-048.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 49: Admin Timeline Event Create

**Intent:** Create timeline events from admin UI.

**Scope lock:** Build: `/admin/timeline/new` Fields: `name; era; year label; sort order; summary; body; status`

**Expected artifacts:** `timeline create form`

**What must be true to call this phase fully complete:**

- [ ] Admin can create timeline events.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create timeline event through UI.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-049.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 50: Admin Timeline Event Edit

**Intent:** Edit existing timeline events.

**Scope lock:** Build: `/admin/timeline; /admin/timeline/[id]/edit`

**Expected artifacts:** `timeline admin list; timeline edit route`

**What must be true to call this phase fully complete:**

- [ ] Admin can manage timeline events.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Edit timeline event and confirm public page updates.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-050.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 51: Media Asset Schema

**Intent:** Create database support for media.

**Scope lock:** Create: `media_assets` Fields: `id; slug; original_filename; stored_filename; relative_path; mime_type; media_kind; size_bytes; width; height; duration_seconds; alt_text; caption; created_at; updated_at`

**Expected artifacts:** `media schema; migration; media docs`

**What must be true to call this phase fully complete:**

- [ ] Media metadata can be stored.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Insert media metadata manually or through seed.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-051.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 52: Local Media Storage Directories

**Intent:** Create safe filesystem layout for uploaded media.

**Scope lock:** Define directories: `media/originals; media/images; media/videos; media/thumbnails; media/models; media/tmp` Add `.gitignore` rules.

**Expected artifacts:** `media directory docs; filesystem helper`

**What must be true to call this phase fully complete:**

- [ ] Media storage location is deterministic and outside source control.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: App can resolve media root safely.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-052.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 53: Image Upload Backend

**Intent:** Support image uploads.

**Scope lock:** Build server logic for: `accept image upload; validate MIME type; limit file size; generate safe filename; store original image; write media_assets row` No thumbnails yet.

**Expected artifacts:** `image upload server action; media validation utilities`

**What must be true to call this phase fully complete:**

- [ ] Images can be uploaded safely.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Upload PNG/JPG/WebP from admin. Reject invalid file.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-053.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 54: Admin Media Library

**Intent:** Browse uploaded media.

**Scope lock:** Build: `/admin/media` Show: `preview; filename; kind; size; created date`

**Expected artifacts:** `media library route; media grid component`

**What must be true to call this phase fully complete:**

- [ ] Admin can view uploaded media.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Uploaded images appear in admin media library.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-054.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 55: Image Thumbnail Generation

**Intent:** Generate optimized thumbnails.

**Scope lock:** Add image processing for: `small thumbnail; medium preview; public optimized image` Use a server-side image library.

**Expected artifacts:** `image processor; thumbnail paths; metadata update`

**What must be true to call this phase fully complete:**

- [ ] Uploaded images have optimized variants.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Upload image and confirm generated derivatives exist.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-055.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 56: Public Media Serving

**Intent:** Serve media files safely.

**Scope lock:** Add route or static serving config for public media. Requirements: `no directory traversal; cache headers; correct MIME type; 404 handling`

**Expected artifacts:** `media serving route or Caddy config; docs/media/serving.md`

**What must be true to call this phase fully complete:**

- [ ] Media displays publicly through stable URLs.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Public pages can display uploaded images.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-056.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 57: Entity Featured Image

**Intent:** Attach images to entities.

**Scope lock:** Add featured image fields: `entities.featured_media_id` Update public pages to show featured images.

**Expected artifacts:** `schema migration; admin image selector; public image rendering`

**What must be true to call this phase fully complete:**

- [ ] Entities can have featured images.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Assign character portrait and confirm it appears publicly.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-057.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 58: Story Cover Image

**Intent:** Attach cover images to stories.

**Scope lock:** Add: `stories.cover_media_id` Update admin and public story pages.

**Expected artifacts:** `story cover schema; admin selector; public cover rendering`

**What must be true to call this phase fully complete:**

- [ ] Stories can have cover images.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Assign story cover and confirm it appears publicly.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-058.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 59: Image Gallery Relationship

**Intent:** Allow multiple images per entity.

**Scope lock:** Create: `entity_media` Fields: `entity_id; media_asset_id; role; sort_order; caption_override`

**Expected artifacts:** `entity media schema; migration; gallery docs`

**What must be true to call this phase fully complete:**

- [ ] Entities can have media galleries.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Attach multiple images to one world.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-059.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 60: Public Entity Galleries

**Intent:** Render image galleries on public entity pages.

**Scope lock:** Add gallery display to: `world detail; character detail; artifact detail; story detail`

**Expected artifacts:** `gallery component; public gallery integration`

**What must be true to call this phase fully complete:**

- [ ] Public pages can show multiple images per entity.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Attached images appear in gallery.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-060.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 61: Video Upload Backend

**Intent:** Support basic video uploads.

**Scope lock:** Build server logic for: `accept MP4/WebM; validate MIME type; limit file size; store original video; write media_assets row` No transcoding yet.

**Expected artifacts:** `video upload support; video validation docs`

**What must be true to call this phase fully complete:**

- [ ] Videos can be uploaded safely.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Upload small MP4. Reject invalid file.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-061.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 62: Public Video Display

**Intent:** Display uploaded videos.

**Scope lock:** Create reusable video component using native HTML video. Support: `poster image; controls; caption; responsive sizing`

**Expected artifacts:** `VideoPlayer.svelte; public media integration`

**What must be true to call this phase fully complete:**

- [ ] Videos are visible and playable.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: A video plays on a public page.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-062.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 63: Markdown Rendering

**Intent:** Allow rich written lore/story content.

**Scope lock:** Add safe Markdown rendering for: `entity descriptions; story body; chapter body; timeline body` Requirements: `sanitize output; support headings; support links; support lists; support blockquotes; support code blocks`

**Expected artifacts:** `markdown renderer; markdown docs`

**What must be true to call this phase fully complete:**

- [ ] Long-form text can be written cleanly.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Markdown renders correctly and unsafe HTML is blocked.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-063.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 64: Slug Validation and Collision Handling

**Intent:** Prevent broken URLs.

**Scope lock:** Add utilities for: `slug generation; slug validation; duplicate slug detection; reserved slug blocking`

**Expected artifacts:** `slug utility; tests; admin validation integration`

**What must be true to call this phase fully complete:**

- [ ] Public URLs are stable and protected.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Duplicate slug fails cleanly. Invalid slug fails cleanly.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-064.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 65: Draft and Published Filtering

**Intent:** Separate private drafts from public content.

**Scope lock:** Enforce public queries to show only: `status = published` Admin can see: `draft; published; archived`

**Expected artifacts:** `status helper; public query updates; tests`

**What must be true to call this phase fully complete:**

- [ ] Public site does not leak drafts.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Draft content is hidden publicly. Published content is visible.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-065.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 66: Canon Status System

**Intent:** Track canon state.

**Scope lock:** Define canon statuses: `canon; variant; legend; retired; non_canon` Expose on admin forms and public pages.

**Expected artifacts:** `canon status docs; UI badges; query support`

**What must be true to call this phase fully complete:**

- [ ] Canon state is visible and manageable.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Set canon status and confirm badge renders.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-066.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 67: UI Component Pass

**Intent:** Consolidate reusable visual components.

**Scope lock:** Create components: `Button; Card; Badge; Panel; PageHeader; SectionHeader; EntityCard; MediaFrame; EmptyState; FormField` Do not redesign full pages yet.

**Expected artifacts:** `app/src/lib/components/ui/*; docs/design/components.md`

**What must be true to call this phase fully complete:**

- [ ] UI is no longer one-off page sludge.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Existing pages use shared components.
- [ ] Run a targeted smoke test proving the phase intent works from a clean checkout.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-067.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 68: Public Visual Polish Pass

**Intent:** Make the public site feel premium.

**Scope lock:** Polish: `homepage; world list/detail; character list/detail; artifact list/detail; story list/detail; timeline; search` Focus: `spacing; typography; card design; hover states; empty states; responsive behavior; visual consistency`

**Expected artifacts:** `updated public routes; design notes`

**What must be true to call this phase fully complete:**

- [ ] Public pages feel cohesive and intentional.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Desktop/mobile visual pass.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-068.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 69: Admin Visual Polish Pass

**Intent:** Make admin pleasant to use.

**Scope lock:** Polish: `dashboard; forms; lists; media library; relationship manager; timeline manager` Focus: `dense but readable layout; clear save feedback; validation messages; navigation clarity`

**Expected artifacts:** `updated admin routes; admin UX notes`

**What must be true to call this phase fully complete:**

- [ ] Admin feels like a real tool, not a basement wiring panel.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Create/edit content flows are usable without confusion.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-069.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 70: Form Validation Standardization

**Intent:** Unify validation behavior.

**Scope lock:** Add shared validation patterns for: `required fields; slug fields; enum fields; text length; file uploads; relationship selections`

**Expected artifacts:** `validation helpers; form error components; tests`

**What must be true to call this phase fully complete:**

- [ ] Forms behave consistently.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Invalid forms fail with useful messages.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-070.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 71: Error Page System

**Intent:** Handle failures cleanly.

**Scope lock:** Create: `404 page; 500 page; admin error states; not found helpers`

**Expected artifacts:** `error routes; error components`

**What must be true to call this phase fully complete:**

- [ ] Errors look intentional.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit missing slug and confirm polished 404.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-071.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 72: Loading and Empty States

**Intent:** Improve perceived polish.

**Scope lock:** Add: `loading states; empty states; skeleton cards where useful; no-results states`

**Expected artifacts:** `loading components; empty state components; route integrations`

**What must be true to call this phase fully complete:**

- [ ] Blank states feel designed.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Empty database does not look broken.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-072.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 73: Accessibility Pass

**Intent:** Make the site usable and structurally sane.

**Scope lock:** Review: `semantic HTML; keyboard navigation; focus states; color contrast; alt text; form labels; button names; heading order`

**Expected artifacts:** `docs/quality/accessibility.md; accessibility fixes`

**What must be true to call this phase fully complete:**

- [ ] Core flows are accessible.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Keyboard navigate major routes. Run browser accessibility audit.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-073.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 74: SEO Metadata

**Intent:** Prepare public pages for indexing and sharing.

**Scope lock:** Add metadata for: `title; description; canonical URL; Open Graph image; Open Graph type; Twitter card metadata`

**Expected artifacts:** `SEO helper; route metadata integration`

**What must be true to call this phase fully complete:**

- [ ] Public pages have clean metadata.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Inspect rendered page head.
- [ ] Run a targeted smoke test proving the phase intent works from a clean checkout.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-074.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 75: Sitemap

**Intent:** Generate sitemap for published content.

**Scope lock:** Build: `/sitemap.xml` Include: `homepage; worlds; characters; artifacts; stories; chapters; timeline`

**Expected artifacts:** `sitemap route`

**What must be true to call this phase fully complete:**

- [ ] Published pages are discoverable.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit `/sitemap.xml`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-075.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 76: Robots.txt

**Intent:** Control crawler basics.

**Scope lock:** Build: `/robots.txt` Rules: `allow public site; disallow admin; link sitemap`

**Expected artifacts:** `robots route`

**What must be true to call this phase fully complete:**

- [ ] Crawler rules are explicit.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit `/robots.txt`.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-076.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 77: RSS Feed

**Intent:** Expose updates for new stories/content.

**Scope lock:** Build: `/rss.xml` Include latest published: `stories; chapters; timeline events`

**Expected artifacts:** `RSS route; feed docs`

**What must be true to call this phase fully complete:**

- [ ] Public updates can be subscribed to.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Validate feed XML.
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-077.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 78: Basic Analytics Logging

**Intent:** Track site usage without third-party dependency.

**Scope lock:** Add privacy-friendly server logs for: `route hits; referer; user agent; timestamp; status code` Avoid invasive tracking.

**Expected artifacts:** `access log docs; optional DB table or Caddy log config`

**What must be true to call this phase fully complete:**

- [ ] Basic traffic visibility exists.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Request pages and verify logs.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-078.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 79: Test Framework Setup

**Intent:** Add automated test foundation.

**Scope lock:** Install and configure: `unit test runner; Svelte component testing if needed; Playwright for browser tests`

**Expected artifacts:** `test config; test scripts; docs/dev/testing.md`

**What must be true to call this phase fully complete:**

- [ ] Test commands run successfully.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `pnpm test; pnpm test:e2e`
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-079.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 80: Unit Tests for Core Utilities

**Intent:** Protect core logic.

**Scope lock:** Test: `slug utilities; env validation; password helpers; media validation; relationship helpers; status filters`

**Expected artifacts:** `unit tests`

**What must be true to call this phase fully complete:**

- [ ] Core utility behavior is covered.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: All unit tests pass.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-080.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 81: Database Query Tests

**Intent:** Protect data access behavior.

**Scope lock:** Test: `published filtering; entity loading; relationship loading; story/chapter loading; timeline sorting; search queries`

**Expected artifacts:** `database tests; test database setup docs`

**What must be true to call this phase fully complete:**

- [ ] Important query behavior is verified.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Run tests against disposable test database.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-081.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.

### Phase 82: Public E2E Smoke Tests

**Intent:** Verify public browsing flows.

**Scope lock:** Test: `homepage loads; world list loads; world detail loads; character detail loads; story reader loads; timeline loads; search works; 404 works`

**Expected artifacts:** `Playwright public smoke tests`

**What must be true to call this phase fully complete:**

- [ ] Public site flows are covered.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `pnpm test:e2e`
- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-082.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.

### Phase 83: Admin E2E Smoke Tests

**Intent:** Verify admin creation flows.

**Scope lock:** Test: `login; create world; create character; create artifact; create story; create chapter; create relationship; upload image; logout`

**Expected artifacts:** `Playwright admin smoke tests`

**What must be true to call this phase fully complete:**

- [ ] Admin flows are covered by browser tests.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Admin E2E suite passes.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-083.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 84: Backup Script

**Intent:** Protect database and media.

**Scope lock:** Create script to backup: `PostgreSQL dump; media directory archive; .env exclusion confirmation`

**Expected artifacts:** `scripts/backup.sh; docs/ops/backups.md`

**What must be true to call this phase fully complete:**

- [ ] A full local backup can be generated.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Run backup locally and inspect output.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-084.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 85: Restore Script

**Intent:** Verify backups are useful.

**Scope lock:** Create restore script for: `database dump; media archive` Use only in local/VM environment first.

**Expected artifacts:** `scripts/restore.sh; docs/ops/restore.md`

**What must be true to call this phase fully complete:**

- [ ] Backup/restore loop is proven.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Restore into fresh local database and media directory.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-085.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 86: Production Build Script

**Intent:** Create a reproducible native production build path without Docker.

**Scope lock:** Create scripts and documentation for: `installing production dependencies; building the SvelteKit app; verifying the build output; running the built Node server locally; checking required environment variables`

**Expected artifacts:** `scripts/build-prod.sh; scripts/run-prod-local.sh; docs/ops/native-production-build.md`

**What must be true to call this phase fully complete:**

- [ ] The app can be built and run with native Node commands from a clean checkout without Docker.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `scripts/build-prod.sh; scripts/run-prod-local.sh; curl -f http://127.0.0.1:3000/health`
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-086.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 87: Native Service Layout

**Intent:** Define production services using host-installed Linux services instead of Docker Compose.

**Scope lock:** Create native service layout for: `app systemd service; postgresql system service; caddy system service; media directory; backup directory; environment file; release directory`

**Expected artifacts:** `infra/systemd/multiverse-codex.service; infra/caddy/Caddyfile; docs/ops/native-service-layout.md; docs/ops/systemd.md`

**What must be true to call this phase fully complete:**

- [ ] Production-like services are defined as native Linux services and can be validated without Docker.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: `systemd-analyze verify infra/systemd/multiverse-codex.service; caddy validate --config infra/caddy/Caddyfile`
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-087.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 88: Caddy Reverse Proxy

**Intent:** Serve the app through a reverse proxy.

**Scope lock:** Configure Caddy for: `domain placeholder; HTTPS-ready config; reverse proxy to native app service; static/media route if needed; security headers; compression`

**Expected artifacts:** `infra/caddy/Caddyfile; docs/ops/caddy.md`

**What must be true to call this phase fully complete:**

- [ ] Caddy can route traffic to the app.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit app through Caddy locally or VM.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-088.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 89: Health Check Endpoint

**Intent:** Expose deploy readiness signal.

**Scope lock:** Build: `/health` Return: `app status; database connectivity; timestamp` Do not expose secrets.

**Expected artifacts:** `health route; health docs`

**What must be true to call this phase fully complete:**

- [ ] Deployment can check app health.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit `/health`. Stop database and confirm degraded response.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-089.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 90: Structured Logging

**Intent:** Make production failures debuggable.

**Scope lock:** Standardize logs for: `startup; database errors; auth errors; media upload errors; request failures`

**Expected artifacts:** `logger utility; logging docs`

**What must be true to call this phase fully complete:**

- [ ] The app emits useful logs.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Trigger controlled error and inspect logs.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-090.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 91: Security Headers

**Intent:** Add baseline browser security hardening.

**Scope lock:** Configure headers: `Content-Security-Policy; X-Frame-Options or frame-ancestors; X-Content-Type-Options; Referrer-Policy; Permissions-Policy`

**Expected artifacts:** `Caddy header config; docs/ops/security-headers.md`

**What must be true to call this phase fully complete:**

- [ ] Security headers are present.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Inspect headers in browser devtools or curl.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-091.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 92: Rate Limiting for Auth

**Intent:** Protect login route from brute force.

**Scope lock:** Add rate limit for: `/admin/login` Could be in app code or reverse proxy.

**Expected artifacts:** `rate limit utility/config; auth security docs`

**What must be true to call this phase fully complete:**

- [ ] Login endpoint is not wide open.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Repeated failed login attempts get throttled.
- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-092.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 93: Media Upload Limits

**Intent:** Prevent accidental server abuse.

**Scope lock:** Enforce: `max image size; max video size; allowed MIME types; per-upload validation; clear error messages`

**Expected artifacts:** `upload limit config; docs/media/limits.md`

**What must be true to call this phase fully complete:**

- [ ] Media upload limits are enforced.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Oversized upload fails cleanly.
- [ ] Run valid/invalid content cases, boundary-size cases, persistence checks, public-render checks, and safety checks for uploads/markdown/URLs.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-093.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No directory traversal risk.
- [ ] No trusting file extensions without MIME/content validation.
- [ ] No source-controlled user media except tiny intentional fixtures.

### Phase 94: VM Provisioning Notes

**Intent:** Prepare local VM test environment.

**Scope lock:** Document VM setup: `Ubuntu Server install; Node and pnpm install; PostgreSQL install; Caddy install; application system user; user permissions; firewall basics; SSH access; project clone; env setup; systemd service setup`

**Expected artifacts:** `docs/ops/vm-setup.md`

**What must be true to call this phase fully complete:**

- [ ] VM setup is repeatable.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: A clean VM can be prepared from docs.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-094.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 95: VM Deployment Dry Run

**Intent:** Deploy to a clean VM.

**Scope lock:** On a local VM: `clone repo; create env file; install native service files; start PostgreSQL; start Caddy; start app systemd service; run migrations; create admin user; seed optional demo data`

**Expected artifacts:** `deployment notes; updated docs`

**What must be true to call this phase fully complete:**

- [ ] The full stack runs on a clean VM.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Visit the site from host browser.
- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-095.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 96: VM Backup/Restore Test

**Intent:** Prove operational recovery on VM.

**Scope lock:** On VM: `create content; upload media; run backup; wipe app data; restore backup; verify content/media returned`

**Expected artifacts:** `docs/ops/vm-backup-restore-report.md`

**What must be true to call this phase fully complete:**

- [ ] Backup/restore works outside local dev machine.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Restored site matches pre-wipe state.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-096.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 97: VM Public Flow Test

**Intent:** Verify public user experience on production-like deployment.

**Scope lock:** Test on VM: `homepage; worlds; characters; artifacts; stories; chapters; timeline; search; media display; mobile viewport`

**Expected artifacts:** `docs/quality/public-vm-smoke.md`

**What must be true to call this phase fully complete:**

- [ ] Public experience works cleanly on VM.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run browser smoke for the target public route, desktop/mobile viewport checks, empty-state or 404 checks where relevant, and verify draft/private data does not leak.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-097.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No public leakage of draft/private records.
- [ ] No broken internal links accepted as complete.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 98: VM Admin Flow Test

**Intent:** Verify creator workflow on production-like deployment.

**Scope lock:** Test on VM: `login; create/edit all core entities; upload image; upload video; attach media; create relationship; create timeline event; publish draft; logout`

**Expected artifacts:** `docs/quality/admin-vm-smoke.md`

**What must be true to call this phase fully complete:**

- [ ] Admin workflow is proven on VM.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-098.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 99: Performance Baseline

**Intent:** Measure current performance before VPS launch.

**Scope lock:** Measure: `homepage load; entity list load; entity detail load; story reader load; media-heavy page load; database query timings; bundle size`

**Expected artifacts:** `docs/quality/performance-baseline.md`

**What must be true to call this phase fully complete:**

- [ ] Performance baseline exists and major issues are documented.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Run Lighthouse or equivalent local browser audit.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-099.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 100: Production Content Empty-State Pass

**Intent:** Make the site ready before real content exists.

**Scope lock:** Review empty and low-content cases: `no worlds; no characters; no artifacts; no stories; no media; no timeline events; no search results`

**Expected artifacts:** `empty-state copy and UI updates`

**What must be true to call this phase fully complete:**

- [ ] A fresh site does not look broken before content is added.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-100.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 101: Final Design Polish Pass

**Intent:** Finish the first-launch visual layer.

**Scope lock:** Polish: `animation timing; hover states; focus states; mobile spacing; typography scale; card consistency; background effects; 3D placeholders if 3D is not active yet`

**Expected artifacts:** `final UI polish commits; docs/design/final-polish-notes.md`

**What must be true to call this phase fully complete:**

- [ ] The site feels clean, smooth, futuristic, and coherent.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-101.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 102: Basic Three.js Scene Setup

**Intent:** Create the foundation for the future 3D viewport.

**Scope lock:** Build: `/cosmos` Add: `Three.js canvas; camera; controls; basic starfield; placeholder world nodes; click handling scaffold` Do not connect database yet.

**Expected artifacts:** `CosmosViewport.svelte; /cosmos route`

**What must be true to call this phase fully complete:**

- [ ] The 3D viewport foundation exists.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: 3D scene renders and does not crash on mobile.
- [ ] Run `/cosmos` in browser, verify no console errors, click/selection behavior, mobile/reduced-motion fallback, and animation cleanup after navigation.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-102.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No WebGL-only failure cliff without fallback.
- [ ] No animation loop/resource leaks after route changes.

### Phase 103: Database-Driven Cosmos Nodes

**Intent:** Connect worlds to the 3D viewport.

**Scope lock:** Load published worlds into `/cosmos`. Represent each world as: `node; label; click target; summary panel; link to world page`

**Expected artifacts:** `cosmos data loader; world node component/logic`

**What must be true to call this phase fully complete:**

- [ ] The 3D viewport reflects database content.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Seed worlds appear as clickable nodes.
- [ ] Run migrations against a disposable database, inspect the resulting schema, run seed/query checks where relevant, and verify re-run behavior does not corrupt data.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-103.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include schema, fixture, query, media, or rendered-output snapshot proving persisted behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No manual-only database changes.
- [ ] No schema drift outside tracked migrations.
- [ ] No destructive migration without restore/rollback proof.
- [ ] No WebGL-only failure cliff without fallback.
- [ ] No animation loop/resource leaks after route changes.

### Phase 104: Cosmos Visual Polish

**Intent:** Make the 3D viewport feel intentional.

**Scope lock:** Polish: `starfield; node hover states; selection panel; transitions; camera movement; mobile fallback; reduced motion fallback`

**Expected artifacts:** `cosmos polish updates; docs/design/cosmos.md`

**What must be true to call this phase fully complete:**

- [ ] The 3D viewport feels like a real feature, not a tech demo glued to a wall.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Source smoke check: Clicking nodes feels smooth and does not wreck performance.
- [ ] Run the exact quality command introduced or affected by the phase, verify useful failure output, and confirm the fix is regression-safe.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-104.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No WebGL-only failure cliff without fallback.
- [ ] No animation loop/resource leaks after route changes.

### Phase 105: Deployment Documentation

**Intent:** Prepare VPS migration instructions.

**Scope lock:** Write complete deployment guide: `buy domain; point DNS; provision VPS; install Node, pnpm, PostgreSQL, and Caddy; create application system user; clone repo; configure env; install systemd service; start native services; run migrations; create admin user; verify health; enable backups`

**Expected artifacts:** `docs/ops/vps-deployment.md`

**What must be true to call this phase fully complete:**

- [ ] A VPS migration can be followed step-by-step.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-105.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 106: Domain and DNS Checklist

**Intent:** Prepare domain launch.

**Scope lock:** Document: `A record; AAAA record optional; www handling; HTTPS expectation; DNS propagation check; mail records optional`

**Expected artifacts:** `docs/ops/domain-dns.md`

**What must be true to call this phase fully complete:**

- [ ] Domain setup steps are clear.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-106.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.

### Phase 107: VPS Readiness Checklist

**Intent:** Confirm the project is ready to leave the VM nest.

**Scope lock:** Create checklist: `tests pass; E2E passes; VM deploy passes; backup/restore passes; admin login works; media upload works; health endpoint works; Caddy proxy works; systemd app service works; native PostgreSQL service works; domain docs complete; secrets not committed; .env.example current`

**Expected artifacts:** `docs/ops/vps-readiness-checklist.md`

**What must be true to call this phase fully complete:**

- [ ] Every launch gate has a clear pass/fail status.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-107.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

### Phase 108: Content Authoring Guide

**Intent:** Prepare creator workflow for adding real content.

**Scope lock:** Write guide for: `creating a world; creating a character; creating an artifact; creating a story; creating chapters; uploading media; attaching media; linking relationships; publishing content; draft workflow; canon status usage`

**Expected artifacts:** `docs/content/authoring-guide.md`

**What must be true to call this phase fully complete:**

- [ ] The creator can start adding real universe content without digging through code.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run authenticated and unauthenticated browser flows, validation-failure cases, persistence-after-reload checks, and public-page reflection checks where relevant.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-108.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include screenshot, Playwright trace, or UI snapshot for the visible behavior.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No client-only protection for secured behavior.
- [ ] No plaintext password storage.
- [ ] No auth bypass path left open.

### Phase 109: Final VM Release Candidate

**Intent:** Freeze the VPS-ready version.

**Scope lock:** Run final checks: `unit tests; database tests; E2E tests; lint; typecheck; native production build; VM deployment; VM backup/restore; public smoke test; admin smoke test` Tag: `v0.1.0-vps-ready`

**Expected artifacts:** `release notes; git tag; final checklist`

**What must be true to call this phase fully complete:**

- [ ] The site is polished, VM-tested, and ready to migrate to VPS.
- [ ] All expected artifacts exist, are committed, and match the phase scope.
- [ ] Global completion laws are satisfied.
- [ ] Documentation for this phase is updated.
- [ ] Prior locked behavior still passes.

**Tests that validate behavior matches intent:**

- [ ] Run the operation in a clean environment or disposable VM where applicable, then verify logs, health, rollback, backup, restore, or systemd behavior as appropriate.
- [ ] Run `git diff --check` and project lint/typecheck/build commands where applicable.
- [ ] Verify failure cases fail cleanly instead of silently succeeding.

**Golden to lock it:**

- [ ] Create/update `docs/goldens/phase-109.md`.
- [ ] Record commands run, outputs summarized, files changed, and final commit hash.
- [ ] Include terminal transcript snippets for install, deploy, ops, or environment commands.
- [ ] Golden states any limitations and confirms none violate phase intent.

**Hard no's:**

- [ ] No module/file over 1,000 LOC.
- [ ] No mixing logic and layout; split rendering from data, validation, persistence, auth, media, and ops logic whenever possible.
- [ ] No deferred work ever: no TODO/FIXME/stub/placeholder/mocked-success may count as completion.
- [ ] No unrelated objectives, surprise refactors, or scope braid.
- [ ] No secrets, private keys, real credentials, production media, or accidental local files committed.
- [ ] No workstation-only deployment assumptions.
- [ ] No hardcoded environment-specific paths or domains.
- [ ] No backup marked complete without restore proof where applicable.
- [ ] No Docker-only requirement or container-only deployment path.

---

## Final Rule

A phase is not done when the happy path works once. It is done when happy path, failure path, regression path, documentation, and golden all line up without cheats.
