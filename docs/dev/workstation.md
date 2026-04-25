# Phase 0 Workstation Bootstrap

## Purpose

Phase 0 proves that the local workstation can run the native toolchain required for Multiverse Codex development and deployment work.

## Target workstation snapshot

Current primary workstation reported by the project owner:

```txt
Operating System: Kubuntu 25.10
KDE Plasma Version: 6.4.5
KDE Frameworks Version: 6.17.0
Qt Version: 6.9.2
Kernel Version: 6.17.0-22-generic (64-bit)
Graphics Platform: Wayland
Processors: 16 x AMD Ryzen 7 5700X 8-Core Processor
Memory: 64 GiB RAM
Graphics Processor: AMD Radeon RX 7900 XT
Manufacturer: ASUS
```

Latest owner-run verification status:

```txt
PASS: git, systemctl, make, curl, jq, openssl
FAIL: node, pnpm, psql, caddy, postgresql service
```

Phase 0 remains open until the failing probes pass on this workstation.

## Patch repair note

The applied `phase-000-kubuntu-bootstrap` repo state referenced `scripts/bootstrap-workstation-kubuntu.sh` in docs and progress, but the uploaded patch artifact did not include that script file. The `phase-000-bootstrap-script-repair` slice restores the helper so the documentation matches the checked-in implementation.

## Required tools

The workstation must provide:

- Git
- Node LTS
- pnpm
- PostgreSQL server
- PostgreSQL client tools, including `psql`
- Caddy
- systemd and `systemctl`
- make
- curl
- jq
- openssl

Optional tools that can improve the local workflow:

- direnv
- nvm, fnm, or asdf
- VSCodium or another editor
- DBeaver or pgAdmin

## Kubuntu bootstrap helper

This repository includes a guarded helper for Kubuntu/Ubuntu hosts:

```bash
scripts/bootstrap-workstation-kubuntu.sh --dry-run
```

The default mode is dry-run and makes no host changes. It prints the exact commands it would run.

To install the missing Phase 0 tools on the target workstation:

```bash
scripts/bootstrap-workstation-kubuntu.sh --install
```

The helper installs or configures:

- base CLI tools through `apt-get`
- PostgreSQL server and client packages through `apt-get`
- Node LTS through NodeSource, defaulting to Node major `24`
- Caddy through the official Caddy/Cloudsmith apt repository
- pnpm through Corepack when available, with npm fallback
- PostgreSQL service activation through `systemctl enable --now postgresql`

To choose a different Node LTS major explicitly:

```bash
scripts/bootstrap-workstation-kubuntu.sh --install --node-major 22
```

## Manual package sketch

Use the checked-in helper when possible. These commands show the rough package groups for review before host mutation:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg git make jq openssl postgresql postgresql-client
```

After Node is installed, enable pnpm with Corepack when available:

```bash
sudo corepack enable
sudo corepack prepare pnpm@latest-10 --activate
```

If Corepack is unavailable or broken on the host:

```bash
sudo npm install -g pnpm@latest
```

## Verification commands

Run the checked-in probe from the repository root:

```bash
scripts/verify-workstation.sh
```

The script checks:

```bash
git --version
node --version
pnpm --version
psql --version
systemctl --version
caddy version
make --version
curl --version
jq --version
openssl version
systemctl is-active postgresql
```

For command-level probe output around failing checks, run:

```bash
MULTIVERSE_CODEX_DEBUG=1 scripts/verify-workstation.sh
```

## Expected success behavior

A complete Phase 0 workstation returns only `[PASS]` lines and exits with status `0`.

## Expected failure behavior

A missing command, failed version probe, or inactive PostgreSQL service returns at least one `[FAIL]` line and exits nonzero. This is intentional because Phase 0 must not count an unverified workstation as complete.

## Troubleshooting notes

- If `node` is missing, run the Kubuntu bootstrap helper or install Node LTS from a trusted package source.
- If `pnpm` is missing but Node is installed, enable Corepack or install pnpm from npm.
- If `psql` is missing, install PostgreSQL client tools.
- If `caddy` is missing, install Caddy from the official Caddy apt repository or another trusted operating system package source.
- If `systemctl is-active postgresql` reports `inactive`, run `sudo systemctl enable --now postgresql` and rerun the verifier.
- If `systemctl` fails inside a container, rerun the probe on the actual systemd-based workstation or VM target.

## Phase status

The repository now contains the verification harness, a guarded Kubuntu bootstrap helper, and documentation. Phase 0 remains open until the target workstation returns a clean verification run.
