# Phase 0 Workstation Bootstrap

## Purpose

Phase 0 proves that the local workstation can run the native toolchain required for Multiverse Codex development and deployment work.

## Target workstation snapshot

Primary workstation reported by the project owner:

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

## Verified success transcript

The primary workstation returned a clean Phase 0 verification run:

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

## Kubuntu bootstrap helper

This repository includes a guarded helper for Kubuntu/Ubuntu hosts:

```bash
scripts/bootstrap-workstation-kubuntu.sh --dry-run
```

The default mode is dry-run and makes no host changes. It prints the exact commands it would run.

To install the missing Phase 0 tools on a Kubuntu/Ubuntu workstation:

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

## Caddy keyring repair note

An earlier install attempt hit an apt signature failure for the Caddy repository because the repository key was not available to apt at the expected keyring path. The bootstrap helper now writes the Caddy keyring to:

```txt
/usr/share/keyrings/caddy-stable-archive-keyring.gpg
```

It also removes the stale earlier copy at:

```txt
/etc/apt/keyrings/caddy-stable-archive-keyring.gpg
```

After that repair, `caddy version` passed on the target workstation.

## Expected success behavior

A complete Phase 0 workstation returns only `[PASS]` lines and exits with status `0`.

## Expected failure behavior

A missing command, failed version probe, or inactive PostgreSQL service returns at least one `[FAIL]` line and exits nonzero. This is intentional because Phase 0 must not count an unverified workstation as complete.

## Troubleshooting notes

- If `node` is missing, run the Kubuntu bootstrap helper or install Node LTS from a trusted package source.
- If `pnpm` is missing but Node is installed, enable Corepack or install pnpm from npm.
- If `psql` is missing, install PostgreSQL client tools.
- If `caddy` is missing or apt reports `NO_PUBKEY`, rerun the updated bootstrap helper or refresh the Caddy keyring at `/usr/share/keyrings/caddy-stable-archive-keyring.gpg`.
- If `systemctl is-active postgresql` reports `inactive`, run `sudo systemctl enable --now postgresql` and rerun the verifier.
- If `systemctl` fails inside a container, rerun the probe on the actual systemd-based workstation or VM target.

## Phase status

Phase 0 is complete. The workstation bootstrap is verified on the primary workstation.
