# Phase 000 Golden: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Scope completed

Phase 0 is complete. The primary Kubuntu workstation has the required native development toolchain available and the PostgreSQL service active.

This closure patch also hardens the Kubuntu bootstrap helper after an observed Caddy apt key failure:

- Caddy keyring path now uses `/usr/share/keyrings/caddy-stable-archive-keyring.gpg`.
- The helper removes stale Caddy keyring copies before installing the refreshed key.
- Dry-run remains the default.
- `--install` remains required for host mutation.

## Files changed

- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/dev/workstation.md`
- `docs/specs/phase-000-spec.md`
- `docs/closures/phase-000-closure.md`
- `docs/goldens/phase-000.md`
- `scripts/bootstrap-workstation-kubuntu.sh`

## Commands run

Owner-run on the primary workstation:

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

## Test and smoke output summary

Target workstation verification passed:

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

Patch-container syntax checks passed:

```txt
bash -n scripts/verify-workstation.sh
bash -n scripts/bootstrap-workstation-kubuntu.sh
```

Dry-run excerpt after Caddy keyring hardening:

```txt
+ sudo install -d -m 0755 /usr/share/keyrings
+ sudo rm -f /etc/apt/keyrings/caddy-stable-archive-keyring.gpg
+ sudo rm -f /usr/share/keyrings/caddy-stable-archive-keyring.gpg
+ curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
+ curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt | sudo tee /etc/apt/sources.list.d/caddy-stable.list >/dev/null
```

`git diff --check` passed.

Architecture file-size review passed for changed files. Two pre-existing canonical docs remain over 1,000 LOC:

```txt
docs/multiverse_codex_phase_plan.md
docs/multiverse_codex_phase_completion_checklist.md
```

No changed file is over 1,000 LOC.

`git apply --check /mnt/data/phase_000_close_workstation_bootstrap.patch` passed.

## Known limitations

None for Phase 0.

## Final commit hash

Baseline commit in the temporary work repo before this patch: `4cc5302`.

No final project commit exists in the source tar workflow because patches are generated from a temporary git repo and delivered as unified diffs.

## Hard no review

- No changed module exceeds 1,000 LOC.
- No logic/layout mixing was introduced.
- No route files exist yet.
- No application data models exist yet.
- No secrets, private keys, credentials, generated archives, or local machine files were added.
- No Phase 0 closure is claimed without a passing target workstation verification transcript.
- No required Phase 0 work remains outstanding.
