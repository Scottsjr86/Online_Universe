# Phase 004 Theme Tokens

## Phase and title

Phase 4: TailwindCSS Setup

## Purpose

This document records the first styling infrastructure contract for Multiverse Codex.
It defines the initial token vocabulary used by TailwindCSS without building the Phase 5
layout shell or Phase 6 landing page.

## Styling stack

- TailwindCSS is loaded through the SvelteKit Vite pipeline with `@tailwindcss/vite`.
- `app/src/app.css` is the global CSS entry imported by `app/src/routes/+layout.svelte`.
- `app/tailwind.config.js` records the source scan path and initial theme extension.
- `app/postcss.config.js` is present as the PostCSS configuration seam for future CSS tooling.

## Initial tokens

| Token family | Values |
| --- | --- |
| Background | `codex.void`, global radial/linear dark field |
| Panel | `codex.panel` |
| Foreground | `codex.ink`, `codex.mute` |
| Accents | `codex.cyan`, `codex.violet`, `codex.ember` |
| Border | `border-slate-400/30` for the initial scaffold card |
| Radius | `rounded-codex` |
| Shadow | `shadow-codex` |
| Spacing | Tailwind spacing utilities only, no component-local spacing system |

## Scope boundary

Phase 4 establishes infrastructure and proves Tailwind utility rendering on the existing
scaffold page. It does not create the reusable site shell, navigation, footer, content
sections, or public landing page polish. Those begin in later phases.

## Verification

Required checks before Phase 4 can close:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional
```

The professional lane must include `scripts/check_phase_tailwind_setup.py` and the Phase 4
spec, closure, and golden artifacts before the phase can be closed.
