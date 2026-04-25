# Phase 000 Closure: Workstation Bootstrap

## Closure status

Phase 0 is open and not closed.

## Scope completed in this patch

- Added a guarded Kubuntu/Ubuntu workstation bootstrap helper.
- Documented the current target workstation status from the owner-run verification transcript.
- Updated the Phase 0 spec to include the new bootstrap helper, its guard behavior, and its test surface.
- Updated the Phase 0 golden with the new commands and results.
- Appended progress for this Phase 0 continuation slice.

## Checklist status

- Workstation can run Node, pnpm, Git, PostgreSQL client tools, Caddy, and systemd commands: not yet proven by a passing target-workstation transcript.
- PostgreSQL native service can be checked with systemd: not yet proven by a passing target-workstation transcript.
- `docs/dev/workstation.md` exists and matches the Phase 0 scope: yes.
- `scripts/verify-workstation.sh` exists and fails closed: yes.
- `scripts/bootstrap-workstation-kubuntu.sh` exists, defaults to dry-run, and has shell syntax checked: yes.
- Global completion laws satisfied for this patch slice: yes.
- Phase 0 fully operational: no.

## Behavior proven

- The verification script exists and is executable.
- The verification script fails closed when required tools are missing.
- Gated debug output is available through `MULTIVERSE_CODEX_DEBUG=1`.
- The Kubuntu bootstrap helper defaults to dry-run.
- The Kubuntu bootstrap helper accepts explicit install mode only through `--install`.
- The Kubuntu bootstrap helper prints the host-mutating commands during dry-run.
- The Kubuntu bootstrap helper shell syntax passes `bash -n`.

## Commands and tests run

```bash
bash -n scripts/verify-workstation.sh
bash -n scripts/bootstrap-workstation-kubuntu.sh
scripts/bootstrap-workstation-kubuntu.sh --dry-run
scripts/verify-workstation.sh
git diff --check
for path in app scripts infra docs; do [ -d "$path" ] && find "$path" -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" \) -print0; done | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_000_kubuntu_bootstrap.patch
```

## Files changed

- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/dev/workstation.md`
- `docs/specs/phase-000-spec.md`
- `docs/closures/phase-000-closure.md`
- `docs/goldens/phase-000.md`
- `scripts/bootstrap-workstation-kubuntu.sh`

## Architecture findings

The file-size review found two pre-existing canonical control documents over 1,000 LOC:

- `docs/multiverse_codex_phase_plan.md`
- `docs/multiverse_codex_phase_completion_checklist.md`

This patch does not change those files. No changed file is over 1,000 LOC. Phase 0 remains open, so this patch does not use those oversized baseline docs to claim phase closure.

## Known limitations

- The current execution container does not have every required Phase 0 workstation tool installed.
- The current execution container does not expose a normal active PostgreSQL systemd service.
- The owner-run target workstation transcript still has missing tools and inactive PostgreSQL service before this bootstrap helper is applied.
- These limitations prevent Phase 0 closure, but they do not invalidate this bootstrap-helper patch slice.

## Deferral check

No work required for a closed Phase 0 is claimed as complete here. Phase 0 remains open until the workstation verification script passes on the target machine.

## Architecture law check

Architecture laws were checked for this patch slice:

- No changed file is over 1,000 LOC.
- No application logic/layout split exists yet because no app exists.
- The scripts have one purpose each and fail closed.
- The bootstrap helper defaults to dry-run before host mutation.
- No secrets, credentials, generated archives, or local machine files were added.
