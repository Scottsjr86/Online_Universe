# Phase 7 Closure: Local Native PostgreSQL Foundation

## Status

Not closed.

## Scope completed in this patch

- Added native PostgreSQL create/reset/status scripts.
- Added shared PostgreSQL shell helpers.
- Added Phase 7 native PostgreSQL documentation.
- Added Phase 7 source validator.
- Wired Phase 7 shell syntax checks and source validator into professional CI.
- Repaired the prior truth gap where docs, CI, and progress referenced missing Phase 7 scripts.

## Checklist status

Open. The source artifacts exist and CI source-shape checks pass, but Phase 7 cannot close until owner workstation PostgreSQL smokes are run against the real native PostgreSQL service.

## Behavior proven

Proven in source/CI:

- scripts exist
- scripts parse with `bash -n`
- destructive reset requires `--yes`
- create/reset support dry-run
- identifier validation exists
- stale app-role password repair exists
- Phase 7 validator exists and passes

Not yet proven in this closure:

- owner workstation `scripts/dev-db-create.sh`
- owner workstation `psql "$DATABASE_URL" -c 'select 1;'`
- owner workstation `scripts/dev-db-status.sh`

## Commands/tests run

```bash
bash -n scripts/dev-db-common.sh
bash -n scripts/dev-db-create.sh
bash -n scripts/dev-db-reset.sh
bash -n scripts/dev-db-status.sh
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/check_phase_postgres_native.py
PYTHONDONTWRITEBYTECODE=1 python3 -S scripts/run_ci.py professional
git diff --check
git apply --check /mnt/data/phase_007_native_postgres_repair.patch
```

## Files changed

- `scripts/dev-db-common.sh`
- `scripts/dev-db-create.sh`
- `scripts/dev-db-reset.sh`
- `scripts/dev-db-status.sh`
- `scripts/check_phase_postgres_native.py`
- `docs/dev/postgres-native.md`
- `docs/specs/phase-007-spec.md`
- `docs/closures/phase-007-closure.md`
- `docs/goldens/phase-007.md`
- `docs/progress.json`
- `docs/progress.jsonl`

## Known limitations

Phase 7 is not closed until owner workstation database create/status/select smokes pass.

## Deferral check

No Phase 7-required source artifact is deferred. Runtime closure remains open because the required workstation PostgreSQL proof has not been captured in this patch. The no work is deferred rule is satisfied for source artifacts while the phase honestly remains not closed.

## Architecture laws checked

Architecture laws were checked for this slice. No route, UI, media, auth, schema, or application database client code was added.
