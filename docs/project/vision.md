# Multiverse Codex Project Vision

## Identity lock

Project name: **Multiverse Codex**

Multiverse Codex is a creator-owned fantasy multiverse website and admin system. It is built to become the canonical public face and private operating console for an expanding universe of worlds, characters, artifacts, factions, stories, timelines, media, relationships, and a later 3D cosmic viewport.

The project should feel like a living atlas, archive, observatory, and control room for an original speculative universe. It is not a generic blog, wiki clone, campaign notebook, or social platform.

## Product promise

Multiverse Codex gives readers a polished public lore surface and gives the creator a durable private system for managing canon without depending on third-party lore tools.

The public side should answer:

- What is this universe?
- Which worlds exist?
- Who matters?
- What artifacts, factions, and stories shape the canon?
- How do events and relationships connect?
- Where can a reader begin?

The private side should answer:

- What content exists?
- What is draft, published, archived, canon, variant, or retired?
- Which entities are connected?
- Which stories, media, and timeline events are ready to publish?
- What needs attention before public release?

## Tone and visual direction

The site direction is futuristic fantasy with a controlled mythic edge:

- dark cosmic foundation
- luminous interface accents
- readable long-form typography
- premium codex panels and cards
- clear hierarchy over visual noise
- restrained motion, used for meaning rather than decoration
- admin UI that is dense, precise, and calm
- public UI that feels cinematic without sacrificing speed or clarity

The design should avoid toy-like fantasy styling, cluttered RPG dashboard noise, and generic SaaS beige panels. It should feel like an instrument panel for a universe with secrets under glass.

## Target audience

Primary audience:

- readers exploring the creator's fictional multiverse
- the creator maintaining canon and publishing content

Secondary audience:

- collaborators or reviewers who may later need a clear read-only view of lore structure
- future operators responsible for deployment, backups, and maintenance

This project is creator-first. Public features exist to present the universe cleanly. Admin features exist to keep the creator's canon accurate and shippable.

## Public/private split

Public surface:

- published worlds
- published characters
- published artifacts
- published factions
- published stories and chapters
- published timeline events
- public search
- safe media display
- relationship views that reveal only public content
- later 3D cosmic exploration of public canon

Private creator surface:

- draft, published, and archived content management
- admin-only create/edit flows
- media upload and library management
- relationship management
- timeline management
- publishing controls
- backup, restore, and operational visibility where appropriate

Security-critical behavior is server-owned. Public pages must not leak drafts or private admin data.

## Core content vocabulary

The canonical Phase 2 vocabulary is defined in:

```txt
docs/project/content-types.md
```

The short vocabulary is:

- world
- character
- artifact
- faction
- story
- chapter
- timeline event
- media asset
- entity relationship

These terms should stay stable unless a later phase intentionally updates the vocabulary and golden evidence.

## Minimum viable launch target

The minimum viable launch is a self-hosted public codex and admin tool that can:

- run on a Linux workstation and production-like Ubuntu server path
- store content in PostgreSQL
- manage worlds, characters, artifacts, factions, stories, chapters, timeline events, media, and relationships
- publish only approved public content
- render public list/detail pages for major content types
- provide search and timeline browsing
- support safe media storage and display
- build and run through native Node, Caddy, systemd, PostgreSQL, and scripted local verification
- pass the professional local CI lane before each phase close

## Technical posture

The chosen baseline stack remains:

```txt
SvelteKit
TypeScript
TailwindCSS
Three.js
PostgreSQL
Drizzle ORM
Custom session auth
Caddy
systemd
Ubuntu Server style native deployment
```

Implementation must continue to follow the architecture laws: thin routes, explicit seams, server-owned security, repository-owned persistence, service-owned behavior, component-owned appearance, and phase-locked proof.
