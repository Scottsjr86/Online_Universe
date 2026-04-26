# Multiverse Codex Content Types

## Purpose

This document locks the Phase 2 content vocabulary. Later schema, route, admin, media, search, and 3D work should use these names unless a later phase deliberately changes the vocabulary with updated docs, tests, and golden evidence.

## Vocabulary rules

- Use singular names for one record and plural names for collections.
- Use **entity** as the shared base concept for canon objects that can be related to one another.
- Use **published** only for content safe to show publicly.
- Use **draft** for creator-private work.
- Use **archived** for content retained but not active.
- Relationship labels should describe the connection, not the visual layout.
- Media metadata and media files stay behind explicit media boundaries.

## Core content types

### World

A world is a major setting body in the multiverse.

Examples of world data:

- name
- slug
- summary
- description
- cosmology notes
- climate notes
- culture notes
- magic or technology notes
- status
- published date

Worlds can relate to characters, artifacts, factions, stories, timeline events, media assets, and other worlds.

### Character

A character is a person, creature, construct, or sentient force with narrative identity.

Examples of character data:

- name
- slug
- alias
- species
- origin world
- summary
- biography
- status in story
- power notes
- status

Characters can relate to worlds, artifacts, factions, stories, chapters, timeline events, media assets, and other characters.

### Artifact

An artifact is an object, relic, device, weapon, text, tool, or material thing with canon significance.

Examples of artifact data:

- name
- slug
- origin world
- current location
- summary
- history
- power notes
- curse notes
- status

Artifacts can relate to worlds, characters, factions, stories, timeline events, media assets, and other artifacts.

### Faction

A faction is an organized group, nation, order, cult, guild, house, fleet, or institution.

Examples of faction data:

- name
- slug
- home world
- summary
- ideology
- leader notes
- influence notes
- status

Factions can relate to worlds, characters, artifacts, stories, timeline events, media assets, and other factions.

### Story

A story is a long-form written canon or non-canon work.

Examples of story data:

- title
- slug
- subtitle
- summary
- body
- canon status
- release status
- chapters
- cover media

Stories can relate to worlds, characters, artifacts, factions, timeline events, media assets, and chapters.

### Chapter

A chapter is an ordered part of a story.

Examples of chapter data:

- story
- chapter number
- slug
- title
- summary
- body
- status
- published date

Chapters belong to stories and may reference related entities through story-level or direct relationships when later phases require it.

### Timeline event

A timeline event is a dated or ordered lore occurrence.

Examples of timeline event data:

- linked entity
- era
- year label
- sort order
- event date text
- event summary
- event body
- status

Timeline events can relate to worlds, characters, artifacts, factions, stories, chapters, and media assets.

### Media asset

A media asset is stored visual, audio, video, model, or document media with metadata.

Examples of media asset data:

- slug
- original filename
- stored filename
- relative path
- MIME type
- media kind
- size
- dimensions or duration
- alt text
- caption

Media assets can become featured images, covers, galleries, thumbnails, videos, or later 3D model references. The media boundary must guard filenames, paths, MIME types, sizes, and public serving behavior.

### Entity relationship

An entity relationship is a typed connection between two canon entities.

Example relationship labels:

- appears_in
- belongs_to
- owns
- created_by
- enemy_of
- ally_of
- located_in
- connected_to
- caused
- descended_from

Relationships should include source entity, target entity, relation type, description, sort order, created date, and updated date.

## Status vocabulary

### Publication status

Use this status family for public visibility:

- draft
- published
- archived

Public routes may show only published records unless a later phase defines a more specific public rule.

### Canon status

Use this status family for story truth state:

- canon
- variant
- legend
- retired
- non_canon

Canon status is not the same as publication status. A private draft can still be canon, and a published story can identify itself as legend or variant.

## Minimum launch content model

The minimum launch content model must support:

- at least one world
- multiple characters
- at least one artifact
- at least one faction
- at least one story
- multiple chapters
- timeline events
- relationships between entities
- media assets attached to public content

## Naming lock

Use **Multiverse Codex** as the project and product name in user-facing project documentation. Code package names, service names, and database names may use lowercase hyphenated or underscored variants where required by tooling, but the product name remains **Multiverse Codex**.
