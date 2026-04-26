#!/usr/bin/env python3
"""Validate the Phase 2 project identity and content vocabulary docs."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISION = ROOT / "docs/project/vision.md"
CONTENT_TYPES = ROOT / "docs/project/content-types.md"

REQUIRED_VISION_TERMS = [
    "Project name: **Multiverse Codex**",
    "Tone and visual direction",
    "Target audience",
    "Public/private split",
    "Minimum viable launch target",
    "Core content vocabulary",
]

REQUIRED_CONTENT_TYPES = [
    "# Multiverse Codex Content Types",
    "### World",
    "### Character",
    "### Artifact",
    "### Faction",
    "### Story",
    "### Chapter",
    "### Timeline event",
    "### Media asset",
    "### Entity relationship",
    "draft",
    "published",
    "archived",
    "canon",
    "variant",
    "legend",
    "retired",
    "non_canon",
]


def read_required(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"missing required identity document: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require_terms(label: str, text: str, terms: list[str]) -> list[str]:
    return [f"{label}: missing {term!r}" for term in terms if term not in text]


def main() -> int:
    failures: list[str] = []
    try:
        vision = read_required(VISION)
        content_types = read_required(CONTENT_TYPES)
    except FileNotFoundError as exc:
        print(f"[FAIL] {exc}", file=sys.stderr, flush=True)
        return 1

    failures.extend(require_terms("vision", vision, REQUIRED_VISION_TERMS))
    failures.extend(require_terms("content-types", content_types, REQUIRED_CONTENT_TYPES))

    if "placeholder" in vision.lower() or "placeholder" in content_types.lower():
        failures.append("identity docs must not contain placeholder language")
    if "todo" in vision.lower() or "todo" in content_types.lower():
        failures.append("identity docs must not contain TODO language")
    if "fixme" in vision.lower() or "fixme" in content_types.lower():
        failures.append("identity docs must not contain FIXME language")

    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}", file=sys.stderr, flush=True)
        return 1

    print("[PASS] Phase 2 identity and content vocabulary docs are locked", flush=True)
    return 0


if __name__ == "__main__":
    os._exit(main())
