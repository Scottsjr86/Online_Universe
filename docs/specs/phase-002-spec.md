# Phase 002 Spec: Project Vision and Naming Lock

## Phase and title

Phase 2: Project Vision and Naming Lock

## Implemented behavior

Phase 2 locks the project's identity and content vocabulary before application scaffolding begins.

Implemented documentation behavior:

- `docs/project/vision.md` now records the product name, product promise, tone and visual direction, target audience, public/private split, core vocabulary pointer, minimum launch target, and technical posture.
- `docs/project/content-types.md` defines the canonical Phase 2 vocabulary for worlds, characters, artifacts, factions, stories, chapters, timeline events, media assets, and entity relationships.
- `docs/project/phase-plan.md` now reflects Phase 2 as the current completed ladder rung and keeps Phase 3 as the next implementation candidate.
- `README.md` now points developers at the Phase 2 identity docs and the identity smoke command.
- `scripts/check_phase_identity.py` validates the Phase 2 identity and content vocabulary docs.
- `ci/master_ci_runner.yaml` wires Phase 2 documentation artifacts, golden evidence, and the identity smoke into the professional lane.
- `docs/multiverse_codex_phase_completion_checklist.md` explicitly records the Phase 2 identity smoke and professional CI gate.
- `docs/progress.json` records Phase 2 as complete and Phase 3 as the next candidate phase.
- `docs/progress.jsonl` records the append-only Phase 2 entry.

## Public/admin routes touched

None. No application routes exist yet.

## Domain modules touched

None. Phase 2 defines vocabulary only. Domain implementation begins in later data and route phases.

## Data models touched

None. Phase 2 defines content vocabulary only. Database schema work begins after app and database foundations exist.

## Guards and seams added

- `scripts/check_phase_identity.py` guards against identity doc drift by checking required Phase 2 terms and rejecting placeholder, TODO, and FIXME language in the identity docs.
- The professional CI lane now checks Phase 2 artifacts before closure.
- The content vocabulary separates canon concepts from media and relationship boundaries before implementation starts.

## Tests and smokes added

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_phase_identity.py`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_ci.py professional`
- `make phase-close`

The professional lane remains the canonical phase-close gate.

## Handoff notes for Phase 3

Phase 3 can scaffold the SvelteKit app under `app/` using the locked project name, public/private split, and content vocabulary from Phase 2. Phase 3 should add real package/framework commands to `ci/master_ci_runner.yaml` only after the corresponding tooling exists in the repo.
