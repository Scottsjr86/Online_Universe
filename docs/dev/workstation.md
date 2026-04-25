# Phase 0 Workstation Bootstrap

## Purpose

Phase 0 proves that the local workstation can run the native toolchain required for Multiverse Codex development and deployment work.

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

## Ubuntu package sketch

These commands are documentation only. Review package sources before running them on a real host.

```bash
sudo apt update
sudo apt install -y git postgresql postgresql-client caddy make curl jq openssl
```

Install Node LTS and pnpm using the workstation owner's preferred Node manager or trusted system package source. After Node is installed, enable pnpm with Corepack when available:

```bash
corepack enable
corepack prepare pnpm@latest --activate
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

- If `pnpm` is missing but Node is installed, enable Corepack or install pnpm from a trusted source.
- If `psql` is missing, install PostgreSQL client tools.
- If `caddy` is missing, install Caddy from the operating system package source or the official Caddy repository.
- If `systemctl is-active postgresql` fails on a desktop Linux host, start and enable the PostgreSQL service with the host's service manager.
- If `systemctl` fails inside a container, rerun the probe on the actual systemd-based workstation or VM target.

## Phase status

The repository now contains the verification harness and documentation, but Phase 0 remains open until the target workstation returns a clean verification run.
