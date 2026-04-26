# Multiverse Codex App

This directory now contains the Phase 3 SvelteKit TypeScript scaffold.

## Package manager

The app is configured for `pnpm` and declares its package manager in `package.json`.

## Expected local commands

Run these from the repo root after applying the Phase 3 scaffold patch:

```bash
cd app
pnpm install
pnpm check
pnpm build
pnpm dev
```

`pnpm install` creates `app/pnpm-lock.yaml`, which is required before Phase 3 can be truthfully closed.

## Scope boundary

This phase creates the default app shell only. TailwindCSS, reusable layout components, and the polished landing page begin in later phases.
