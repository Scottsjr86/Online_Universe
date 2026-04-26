#!/usr/bin/env python3
"""Validate the Phase 3 SvelteKit TypeScript scaffold shape."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app"

REQUIRED_FILES = [
    APP / "package.json",
    APP / "svelte.config.js",
    APP / "vite.config.ts",
    APP / "tsconfig.json",
    APP / "src" / "app.d.ts",
    APP / "src" / "app.html",
    APP / "src" / "routes" / "+page.svelte",
]

REQUIRED_SCRIPTS = {"dev", "build", "preview", "check"}
REQUIRED_DEV_DEPENDENCIES = {
    "@sveltejs/adapter-auto",
    "@sveltejs/kit",
    "@sveltejs/vite-plugin-svelte",
    "svelte",
    "svelte-check",
    "typescript",
    "vite",
}


def fail(message: str) -> int:
    print(f"[FAIL] {message}", file=sys.stderr)
    return 1


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        return fail("missing Phase 3 scaffold files: " + ", ".join(str(path.relative_to(ROOT)) for path in missing))

    package_path = APP / "package.json"
    try:
        package = json.loads(package_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"app/package.json is invalid JSON: {exc}")

    if package.get("type") != "module":
        return fail("app/package.json must use ESM via type=module")
    if not str(package.get("packageManager", "")).startswith("pnpm@"):
        return fail("app/package.json must declare a pnpm packageManager")

    scripts = set(package.get("scripts", {}))
    missing_scripts = sorted(REQUIRED_SCRIPTS - scripts)
    if missing_scripts:
        return fail("missing package scripts: " + ", ".join(missing_scripts))

    dev_dependencies = set(package.get("devDependencies", {}))
    missing_deps = sorted(REQUIRED_DEV_DEPENDENCIES - dev_dependencies)
    if missing_deps:
        return fail("missing devDependencies: " + ", ".join(missing_deps))

    config = (APP / "svelte.config.js").read_text(encoding="utf-8")
    if "@sveltejs/adapter-auto" not in config or "vitePreprocess" not in config:
        return fail("svelte.config.js must use adapter-auto and vitePreprocess")

    vite_config = (APP / "vite.config.ts").read_text(encoding="utf-8")
    if "@sveltejs/kit/vite" not in vite_config or "sveltekit()" not in vite_config:
        return fail("vite.config.ts must load the SvelteKit Vite plugin")

    page = (APP / "src" / "routes" / "+page.svelte").read_text(encoding="utf-8")
    if "Multiverse Codex" not in page or "<svelte:head>" not in page:
        return fail("default route must render the Multiverse Codex scaffold page")

    if (APP / ".gitkeep").exists():
        return fail("app/.gitkeep must not return after scaffold creation")

    print("[PASS] Phase 3 SvelteKit scaffold files are present and coherent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
