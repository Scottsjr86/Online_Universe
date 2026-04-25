# Phase 000 Golden: Workstation Bootstrap

## Phase and title

Phase 0: Workstation Bootstrap

## Scope completed

This patch repairs the Phase 0 workstation bootstrap slice:

- Restores `scripts/bootstrap-workstation-kubuntu.sh`, which the applied repo docs and progress log referenced but the uploaded `phase_000_kubuntu_bootstrap.patch` artifact did not include.
- Preserves `scripts/verify-workstation.sh` as the workstation proof probe.
- Keeps the bootstrap helper dry-run-first, with `--install` required for host mutation.
- Updates Phase 0 progress, spec, closure evidence, and golden evidence to match the actual repository state.
- Keeps Phase 0 open until the target workstation returns a clean verification transcript.

## Files changed

- `docs/progress.json`
- `docs/progress.jsonl`
- `docs/specs/phase-000-spec.md`
- `docs/closures/phase-000-closure.md`
- `docs/goldens/phase-000.md`
- `scripts/bootstrap-workstation-kubuntu.sh`

## Commands run

```bash
bash -n scripts/verify-workstation.sh
bash -n scripts/bootstrap-workstation-kubuntu.sh
scripts/bootstrap-workstation-kubuntu.sh --dry-run
scripts/verify-workstation.sh
git diff --check
for path in app scripts infra docs; do [ -d "$path" ] && find "$path" -type f \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" \) -print0; done | xargs -0 wc -l | sort -n
git apply --check /mnt/data/phase_000_bootstrap_script_repair.patch
```

## Test and smoke output summary

`bash -n scripts/verify-workstation.sh` passed.

`bash -n scripts/bootstrap-workstation-kubuntu.sh` passed.

`./scripts/bootstrap-workstation-kubuntu.sh --dry-run` passed and printed host-mutating commands without running them.

Dry-run excerpt:

```txt
Multiverse Codex Kubuntu Phase 0 bootstrap
==========================================
Mode: dry-run
NodeSource major: 24.x
+ sudo apt-get update
+ sudo apt-get install -y ca-certificates curl gnupg git make jq openssl postgresql postgresql-client debian-keyring debian-archive-keyring apt-transport-https
+ curl -fsSL https://deb.nodesource.com/setup_24.x -o /tmp/multiverse-codex-nodesource-setup.sh
+ sudo bash /tmp/multiverse-codex-nodesource-setup.sh
+ sudo apt-get install -y nodejs
+ sudo install -d -m 0755 /etc/apt/keyrings
+ curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/caddy-stable-archive-keyring.gpg
+ curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt | sudo tee /etc/apt/sources.list.d/caddy-stable.list >/dev/null
+ sudo apt-get update
+ sudo apt-get install -y caddy
+ sudo systemctl enable --now postgresql
+ if command -v corepack >/dev/null 2>&1; then sudo corepack enable && sudo corepack prepare pnpm@latest-10 --activate; else sudo npm install -g pnpm@latest; fi
[PASS] dry-run complete; no host changes were made. Re-run with --install to apply.
```

`./scripts/verify-workstation.sh` failed closed in the patch container because the container is not the target workstation and does not expose the full host toolchain/service state.

Container verification excerpt:

```txt
[PASS] git: git version 2.47.3
[PASS] node: v22.16.0
[FAIL] pnpm: command not found
[FAIL] psql: command not found
[FAIL] caddy: command not found
[FAIL] postgresql service: not active or unavailable: System has not been booted with systemd as init system (PID 1). Can't operate.
[FAIL] workstation bootstrap has 4 failing probe(s)
```

`git diff --check` passed.

Architecture file-size review passed for changed files. Two pre-existing canonical docs remain over 1,000 LOC:

```txt
4495 docs/multiverse_codex_phase_plan.md
4496 docs/multiverse_codex_phase_completion_checklist.md
```

No changed file is over 1,000 LOC.

`git apply --check /mnt/data/phase_000_bootstrap_script_repair.patch` passed.

## Known limitations

- Phase 0 is not closed.
- The owner-reported target workstation still needs Node, pnpm, PostgreSQL client/server activation, and Caddy before the verifier can pass.
- The patch container cannot prove the workstation service state.
- The bootstrap helper was verified in dry-run mode only in the patch container; install mode must be run on the target Kubuntu workstation.

## Final commit hash

Baseline commit in the temporary work repo before this patch: `bb23bc3`.

No final project commit exists in the source tar workflow because patches are generated from a temporary git repo and delivered as unified diffs.

## Hard no review

- No changed module exceeds 1,000 LOC.
- No logic/layout mixing was introduced.
- No route files exist yet.
- No application data models exist yet.
- No secrets, private keys, credentials, generated archives, or local machine files were added.
- No Phase 0 closure is claimed without a passing target workstation verification transcript.
