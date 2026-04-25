# Phase 000 Closure: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Closure status

Phase 0 is complete.

## Scope completed

The primary workstation now satisfies the Phase 0 toolchain requirements:

- Git is available.
- Node LTS is available.
- pnpm is available.
- PostgreSQL client tools are available.
- PostgreSQL native service is active under systemd.
- Caddy is available.
- systemd and `systemctl` are available.
- make is available.
- curl is available.
- jq is available.
- openssl is available.

This closure patch also hardens `scripts/bootstrap-workstation-kubuntu.sh` after the observed Caddy apt key failure. The helper now places the Caddy keyring at `/usr/share/keyrings/caddy-stable-archive-keyring.gpg`, removes the earlier `/etc/apt/keyrings` copy, and refreshes the Caddy source list before install.

## Checklist status

- Workstation can run Node, pnpm, Git, PostgreSQL client tools, Caddy, and systemd commands: yes.
- PostgreSQL native service is active: yes.
- `docs/dev/workstation.md` exists and matches Phase 0 scope: yes.
- `scripts/verify-workstation.sh` exists and fails closed: yes.
- `scripts/bootstrap-workstation-kubuntu.sh` exists, defaults to dry-run, and has shell syntax checked: yes.
- Golden evidence exists: yes.
- Spec exists: yes.
- Progress state and append-only log entry exist: yes.
- Architecture laws checked: yes.
- Phase 0 fully operational: yes.

## Behavior proven

Owner-run workstation verification returned a clean pass on the target Kubuntu workstation:

```txt
Multiverse Codex Phase 0 workstation verification
==================================================
[PASS] git: git version 2.51.0
[PASS] node: v24.14.1
[PASS] pnpm: 10.33.2
[PASS] psql: psql (PostgreSQL) 17.9 (Ubuntu 17.9-0ubuntu0.25.10.1)
[PASS] systemctl: systemd 257 (257.9-0ubuntu2.4)
[PASS] caddy: 2.6.2
[PASS] make: GNU Make 4.4.1
[PASS] curl: curl 8.14.1 (x86_64-pc-linux-gnu) libcurl/8.14.1 OpenSSL/3.5.3 zlib/1.3.1 brotli/1.1.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.2 libssh2/1.11.1 nghttp2/1.64.0 librtmp/2.3 OpenLDAP/2.6.10
[PASS] jq: jq-1.8.1
[PASS] openssl: OpenSSL 3.5.3 16 Sep 2025 (Library: OpenSSL 3.5.3 16 Sep 2025)
[PASS] postgresql service: active
==================================================
[PASS] workstation bootstrap verified
```

Repository-side checks in the patch container verified the shell scripts and patch quality.

## Commands and tests run

Owner-run on the target workstation:

```bash
bash scripts/verify-workstation.sh
```

Patch-container checks:

```bash
bash -n scripts/verify-workstation.sh
bash -n scripts/bootstrap-workstation-kubuntu.sh
scripts/bootstrap-workstation-kubuntu.sh --dry-run
git diff --check
for path in app scripts infra docs; do [ -d "$path" ] && find "$path" -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" \) -print0; done | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_000_close_workstation_bootstrap.patch
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

Architecture laws were checked for this closure patch:

- No changed file exceeds 1,000 LOC.
- No route files exist yet.
- No layout/application logic split exists yet because no app exists.
- Scripts are purpose-scoped and fail closed.
- Bootstrap install mode remains explicit and guarded.
- No secrets, credentials, generated archives, or local machine files were added.

The file-size review still reports two pre-existing canonical control documents over 1,000 LOC:

- `docs/multiverse_codex_phase_plan.md`
- `docs/multiverse_codex_phase_completion_checklist.md`

Those documents are project-control inputs and were not changed by this closure patch.

## Known limitations

None for Phase 0.

## No deferred work confirmation

No required Phase 0 work is outstanding. The workstation bootstrap behavior is operational and verified on the primary workstation.

## Architecture law confirmation

The architecture laws were checked. This phase closes without changed-file size violations, unguarded host mutation, secrets, mixed application concerns, or fabricated completion.
