# Multiverse Codex

Multiverse Codex is a self-hosted fantasy universe codex built through small, verified, phase-aligned patches.

The finished project will become a public lore site and creator-owned admin tool for worlds, characters, artifacts, factions, stories, timelines, media, relationships, and a later 3D cosmic viewport.

## Current phase state

- Last completed phase: Phase 5, Base Layout Shell
- Current phase after this patch: Phase 6, Static Landing Page in progress
- Next candidate phase: Phase 6, Static Landing Page closure after workstation proof

Machine-readable state lives in `docs/progress.json`.
Append-only patch history lives in `docs/progress.jsonl`.

## Repository layout

```txt
multiverse-codex/
  app/      Application source root, beginning in Phase 3.
  ci/       Repo-owned local CI manifest.
  docs/     Project control docs, specs, closures, goldens, and design notes.
  infra/    Native deployment, Caddy, systemd, and ops configuration.
  scripts/  Workstation, dev, build, database, ops, and CI runner scripts.
```

`app/` and `infra/` are tracked with explicit README notes instead of `.gitkeep` sentinels.

## Canonical project-control docs

```txt
docs/multiverse_codex_phase_plan.md
docs/multiverse_codex_phase_completion_checklist.md
docs/multiverse_codex_architecture_laws.md
docs/multiverse_codex_fresh_chat_workflow_header.md
```

These documents define the build order, closure contract, architecture laws, and patch workflow.

## Local CI lanes

The repo-owned local CI system is defined by:

```txt
ci/master_ci_runner.yaml
scripts/run_ci.py
```

Run lanes from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py --list
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py quick
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py release
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py enterprise
```

Make wrappers are also available:

```bash
make ci-list
make ci-quick
make ci-professional
make ci-release
make ci-enterprise
make phase-close
```

The professional lane is the phase-close gate. New tests, smokes, drift checks, and golden checks must be wired into the manifest before a phase is marked complete. Phase 2 adds the identity/content vocabulary check through `scripts/check_phase_identity.py`. Phase 3 adds the scaffold shape and pnpm lockfile check through `scripts/check_phase_app_scaffold.py`. Phase 4 adds the Tailwind setup and lockfile drift check through `scripts/check_phase_tailwind_setup.py`. Phase 5 adds the site shell shape and closure drift check through `scripts/check_phase_site_shell.py`. Phase 6 adds the static landing page source-shape check through `scripts/check_phase_landing_page.py`.

## Project identity docs

Phase 2 locks the project identity and content vocabulary:

```txt
docs/project/vision.md
docs/project/content-types.md
```

Run the targeted identity smoke directly with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_identity.py
```

## Workstation verification

Phase 0 added the workstation verifier:

```bash
scripts/verify-workstation.sh
```

Run it on the primary workstation when host-tool drift is suspected.


## Phase 3 SvelteKit scaffold

The application scaffold lives in `app/` and currently includes SvelteKit, TypeScript, Vite, adapter-auto, and the default route shell.

Run from the repo root when app scaffold drift is suspected:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
```

`app/pnpm-lock.yaml` is committed and required by the professional CI lane before Phase 3 can remain closed.


## Phase 4 Tailwind setup

TailwindCSS is wired through the SvelteKit Vite pipeline. The current Phase 4 source artifacts are:

```txt
app/src/app.css
app/src/routes/+layout.svelte
app/tailwind.config.js
app/postcss.config.js
docs/design/theme.md
scripts/check_phase_tailwind_setup.py
```

Run the Phase 4 shape check from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_tailwind_setup.py
```

Phase 4 closure proof was captured with the workstation app path:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
```

Then run the canonical close gate from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```


## Phase 5 base layout shell

The public site shell is split into layout-owned components:

```txt
app/src/routes/+layout.svelte
app/src/lib/components/site/SiteShell.svelte
app/src/lib/components/site/SiteNav.svelte
app/src/lib/components/site/SiteFooter.svelte
scripts/check_phase_site_shell.py
```

Run the Phase 5 source-shape check from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_site_shell.py
```

Phase 5 closure proof was captured with the workstation app path:

```bash
cd app
pnpm check
pnpm build
pnpm dev
```

Then the canonical close gate passed from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

## Phase 6 static landing page

The homepage now contains the required static landing-page sections:

```txt
app/src/routes/+page.svelte
scripts/check_phase_landing_page.py
```

Run the Phase 6 source-shape check from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_landing_page.py
```

Phase 6 is in progress until the workstation app path is proven:

```bash
cd app
pnpm check
pnpm build
pnpm dev
```

Then run the canonical close gate from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

The page must stay static. Database content, public content routes, admin tools, media, auth, and search remain later-phase work.
