# Multiverse Codex: High-Level Build Plan

## Goal

Build a self-hosted, futuristic, interactive fantasy multiverse website from scratch.

The final result should be a polished local/VM-tested site that is ready to migrate to a VPS and ready for the creator to begin adding real content: worlds, characters, artifacts, factions, stories, media, timelines, and eventually a 3D cosmic viewport.

## Chosen Baseline Stack

This plan assumes the following stack:

```txt
App Framework:     SvelteKit
Language:          TypeScript
Styling:           TailwindCSS
3D Engine:         Three.js
Database:          PostgreSQL
ORM:               Drizzle ORM
Auth:              Custom session auth
Reverse Proxy:     Caddy
Deployment:        Native systemd services
Process Manager:   systemd
OS Target:         Ubuntu Server
Local Dev OS:      Linux workstation
```

## Planning Rules

Each phase is single-purpose.

A phase should not mix unrelated objectives.  
If a phase starts touching too many systems, split it.

Each phase should end with:

```txt
- Code committed
- Tests or smoke checks added
- Basic documentation updated
- Known limitations written down
```

Recommended branch style:

```txt
phase/00-workstation-bootstrap
phase/01-repo-skeleton
phase/02-sveltekit-shell
...
```

Recommended commit style:

```txt
phase 00: bootstrap workstation tooling
phase 01: create repository skeleton
phase 02: scaffold sveltekit app shell
```

---

# Phase 0: Workstation Bootstrap

## Purpose

Prepare the local development machine with required tools.

## Scope

Install and verify:

```txt
git
node LTS
pnpm
postgresql server
postgres client tools
caddy
systemd
make
curl
jq
openssl
```

Optional but recommended:

```txt
direnv
nvm / fnm / asdf
VS Code / VSCodium
DBeaver / pgAdmin
```

## Deliverables

```txt
docs/dev/workstation.md
```

Include:

```txt
installed tools
versions
verification commands
troubleshooting notes
```

## Smoke Checks

```bash
node --version
pnpm --version
git --version
psql --version
systemctl --version
caddy version
```

## Done When

The workstation can run Node, pnpm, Git, PostgreSQL server/client tools, Caddy, and systemd service commands.

---

# Phase 1: Repository Skeleton

## Purpose

Create the empty project repository structure.

## Scope

Create top-level layout:

```txt
multiverse-codex/
  app/
  docs/
  infra/
  scripts/
  .gitignore
  README.md
  Makefile
```

## Deliverables

```txt
README.md
docs/project/vision.md
docs/project/phase-plan.md
.gitignore
Makefile
```

## Smoke Checks

```bash
git status
make help
```

## Done When

The repo exists, is committed, and has a clear starting structure.

---

# Phase 2: Project Vision and Naming Lock

## Purpose

Define the project identity before code sprawl begins.

## Scope

Document:

```txt
project name
tone and visual direction
core content types
target audience
public/private split
minimum viable launch target
```

## Deliverables

```txt
docs/project/vision.md
docs/project/content-types.md
```

## Done When

The project has a stable identity and agreed content model vocabulary.

---

# Phase 3: SvelteKit App Scaffold

## Purpose

Create the initial SvelteKit app.

## Scope

Inside `app/`, scaffold SvelteKit with TypeScript.

Add:

```txt
SvelteKit
TypeScript
pnpm lockfile
basic dev server
```

## Deliverables

```txt
app/package.json
app/src/
app/svelte.config.js
app/vite.config.ts
```

## Smoke Checks

```bash
cd app
pnpm install
pnpm dev
```

## Done When

The default app runs locally.

---

# Phase 4: TailwindCSS Setup

## Purpose

Add styling infrastructure.

## Scope

Install and configure:

```txt
TailwindCSS
PostCSS
global CSS entry
base theme tokens
```

Create initial design tokens:

```txt
background colors
foreground colors
accent colors
border colors
spacing conventions
radius conventions
shadow conventions
```

## Deliverables

```txt
app/tailwind.config.*
app/src/app.css
docs/design/theme.md
```

## Smoke Checks

Render a page with Tailwind utility classes.

## Done When

The app can render custom styled pages using Tailwind.

---

# Phase 5: Base Layout Shell

## Purpose

Create the public site frame.

## Scope

Build:

```txt
root layout
main navigation
footer
responsive container
dark futuristic baseline theme
```

Do not build content pages yet.

## Deliverables

```txt
app/src/routes/+layout.svelte
app/src/lib/components/site/SiteShell.svelte
app/src/lib/components/site/SiteNav.svelte
app/src/lib/components/site/SiteFooter.svelte
```

## Smoke Checks

Visit:

```txt
/
```

Confirm layout renders at desktop and mobile widths.

## Done When

The site has a clean reusable shell.

---

# Phase 6: Static Landing Page

## Purpose

Create the first polished public page.

## Scope

Build homepage sections:

```txt
hero
universe teaser
featured worlds placeholder
featured characters placeholder
call-to-action into codex
```

No database yet.

## Deliverables

```txt
app/src/routes/+page.svelte
```

## Smoke Checks

```bash
pnpm check
pnpm lint
```

## Done When

The homepage looks intentional, futuristic, and responsive.

---

# Phase 7: Local Native PostgreSQL Foundation

## Purpose

Create local database service orchestration without Docker.

## Scope

Install and configure host PostgreSQL for local development.

Create:

```txt
local database
local database user
local database lifecycle commands
optional init SQL directory
```

Do not containerize development or production.

## Deliverables

```txt
scripts/dev-db-create.sh
scripts/dev-db-reset.sh
scripts/dev-db-status.sh
docs/dev/postgres-native.md
```

## Smoke Checks

```bash
systemctl status postgresql
psql "$DATABASE_URL" -c 'select 1;'
scripts/dev-db-status.sh
```

## Done When

PostgreSQL runs locally as a native service and the app can reach the dev database without Docker.
---

# Phase 8: Environment Configuration

## Purpose

Standardize environment variables.

## Scope

Create:

```txt
.env.example
app/src/lib/server/env.ts
```

Define required variables:

```txt
DATABASE_URL
SESSION_SECRET
PUBLIC_SITE_NAME
MEDIA_ROOT
```

Add validation.

## Deliverables

```txt
.env.example
docs/dev/environment.md
```

## Smoke Checks

Run app with valid `.env`.

Run app with missing env and confirm it fails clearly.

## Done When

Environment config is explicit, validated, and documented.

---

# Phase 9: Database Connection

## Purpose

Connect SvelteKit server code to PostgreSQL.

## Scope

Install and configure:

```txt
pg driver
Drizzle ORM
database client module
```

No tables yet.

## Deliverables

```txt
app/src/lib/server/db/client.ts
app/drizzle.config.ts
```

## Smoke Checks

Create a temporary health query:

```sql
select 1
```

## Done When

The app can connect to PostgreSQL.

---

# Phase 10: Database Migration System

## Purpose

Add repeatable schema migration workflow.

## Scope

Configure:

```txt
Drizzle schema folder
migration generation
migration apply command
migration documentation
```

## Deliverables

```txt
app/src/lib/server/db/schema/
app/drizzle/
docs/dev/migrations.md
```

## Smoke Checks

```bash
pnpm db:generate
pnpm db:migrate
```

## Done When

Schema changes can be generated and applied repeatably.

---

# Phase 11: Core Entity Base Schema

## Purpose

Create a shared entity foundation.

## Scope

Add base table design for common canon entities.

Create:

```txt
entities
```

Fields:

```txt
id
slug
type
name
summary
description
status
created_at
updated_at
published_at
```

Do not add specialized tables yet.

## Deliverables

```txt
schema entity base
migration
docs/data/entities.md
```

## Smoke Checks

Run migration and inspect table.

## Done When

The database has a generic entity foundation.

---

# Phase 12: World Schema

## Purpose

Add worlds as the first real content type.

## Scope

Create:

```txt
worlds
```

Fields:

```txt
entity_id
cosmology_notes
climate_notes
culture_notes
magic_or_tech_notes
```

## Deliverables

```txt
world schema
migration
world type docs
```

## Smoke Checks

Insert one test world through a seed script.

## Done When

A world can exist in the database.

---

# Phase 13: Character Schema

## Purpose

Add character data model.

## Scope

Create:

```txt
characters
```

Fields:

```txt
entity_id
alias
species
origin_world_id
status_in_story
power_notes
biography
```

## Deliverables

```txt
character schema
migration
character type docs
```

## Smoke Checks

Insert one test character linked to a world.

## Done When

A character can exist and optionally reference an origin world.

---

# Phase 14: Artifact Schema

## Purpose

Add artifact data model.

## Scope

Create:

```txt
artifacts
```

Fields:

```txt
entity_id
origin_world_id
current_location
power_notes
curse_notes
history
```

## Deliverables

```txt
artifact schema
migration
artifact type docs
```

## Smoke Checks

Insert one test artifact.

## Done When

An artifact can exist and optionally reference a world.

---

# Phase 15: Faction Schema

## Purpose

Add faction data model.

## Scope

Create:

```txt
factions
```

Fields:

```txt
entity_id
home_world_id
ideology
leader_notes
influence_notes
```

## Deliverables

```txt
faction schema
migration
faction type docs
```

## Smoke Checks

Insert one test faction.

## Done When

A faction can exist and optionally reference a world.

---

# Phase 16: Story Schema

## Purpose

Add story-level content.

## Scope

Create:

```txt
stories
```

Fields:

```txt
entity_id
title
subtitle
summary
body
canon_status
release_status
```

Do not add chapters yet.

## Deliverables

```txt
story schema
migration
story type docs
```

## Smoke Checks

Insert one test story.

## Done When

A story can exist as a long-form written entry.

---

# Phase 17: Chapter Schema

## Purpose

Add chapter-level story structure.

## Scope

Create:

```txt
chapters
```

Fields:

```txt
story_id
chapter_number
slug
title
summary
body
status
published_at
```

## Deliverables

```txt
chapter schema
migration
chapter docs
```

## Smoke Checks

Insert one story with two chapters.

## Done When

Stories can contain ordered chapters.

---

# Phase 18: Timeline Event Schema

## Purpose

Add timeline support.

## Scope

Create:

```txt
timeline_events
```

Fields:

```txt
entity_id
era
year_label
sort_order
event_date_text
event_summary
event_body
```

Do not build UI yet.

## Deliverables

```txt
timeline schema
migration
timeline docs
```

## Smoke Checks

Insert timeline events and query sorted order.

## Done When

Timeline events can be stored and sorted.

---

# Phase 19: Entity Relationship Schema

## Purpose

Create the canon graph.

## Scope

Create:

```txt
entity_relationships
```

Fields:

```txt
id
source_entity_id
target_entity_id
relation_type
description
sort_order
created_at
updated_at
```

Example relation types:

```txt
appears_in
belongs_to
owns
created_by
enemy_of
ally_of
located_in
connected_to
caused
descended_from
```

## Deliverables

```txt
relationship schema
migration
relationship docs
```

## Smoke Checks

Link character to world, artifact, faction, and story.

## Done When

Any entity can relate to any other entity.

---

# Phase 20: Seed Data System

## Purpose

Create repeatable demo data.

## Scope

Build seed script for:

```txt
one world
two characters
one artifact
one faction
one story
two chapters
three relationships
three timeline events
```

## Deliverables

```txt
app/scripts/seed.ts
docs/dev/seeding.md
```

## Smoke Checks

```bash
pnpm db:seed
```

## Done When

A fresh database can be populated with demo universe content.

---

# Phase 21: Public World List Page

## Purpose

Render worlds from the database.

## Scope

Build:

```txt
/worlds
```

Show:

```txt
name
summary
status
published date
```

No detail page yet.

## Deliverables

```txt
app/src/routes/worlds/+page.server.ts
app/src/routes/worlds/+page.svelte
```

## Smoke Checks

Seed data appears on `/worlds`.

## Done When

Worlds render publicly from PostgreSQL.

---

# Phase 22: Public World Detail Page

## Purpose

Render one world from the database.

## Scope

Build:

```txt
/worlds/[slug]
```

Show:

```txt
name
summary
description
related characters
related artifacts
related stories
```

## Deliverables

```txt
app/src/routes/worlds/[slug]/+page.server.ts
app/src/routes/worlds/[slug]/+page.svelte
```

## Smoke Checks

Click world from list to detail.

## Done When

A world page can show connected canon data.

---

# Phase 23: Public Character List Page

## Purpose

Render characters from the database.

## Scope

Build:

```txt
/characters
```

Show:

```txt
name
alias
origin world
summary
```

## Deliverables

```txt
character list route
character card component
```

## Smoke Checks

Seed characters appear on `/characters`.

## Done When

Characters render publicly from PostgreSQL.

---

# Phase 24: Public Character Detail Page

## Purpose

Render one character from the database.

## Scope

Build:

```txt
/characters/[slug]
```

Show:

```txt
name
alias
biography
origin world
related artifacts
related factions
related stories
```

## Deliverables

```txt
character detail route
relationship display component
```

## Smoke Checks

Click character from list to detail.

## Done When

A character page can show connected canon data.

---

# Phase 25: Public Artifact List Page

## Purpose

Render artifacts from the database.

## Scope

Build:

```txt
/artifacts
```

Show:

```txt
name
origin world
summary
```

## Deliverables

```txt
artifact list route
artifact card component
```

## Smoke Checks

Seed artifacts appear on `/artifacts`.

## Done When

Artifacts render publicly from PostgreSQL.

---

# Phase 26: Public Artifact Detail Page

## Purpose

Render one artifact from the database.

## Scope

Build:

```txt
/artifacts/[slug]
```

Show:

```txt
name
history
power notes
curse notes
related characters
related worlds
related stories
```

## Deliverables

```txt
artifact detail route
```

## Smoke Checks

Click artifact from list to detail.

## Done When

An artifact page can show connected canon data.

---

# Phase 27: Public Story List Page

## Purpose

Render stories from the database.

## Scope

Build:

```txt
/stories
```

Show:

```txt
title
summary
canon status
release status
```

## Deliverables

```txt
story list route
story card component
```

## Smoke Checks

Seed stories appear on `/stories`.

## Done When

Stories render publicly from PostgreSQL.

---

# Phase 28: Public Story Detail Page

## Purpose

Render one story and chapter list.

## Scope

Build:

```txt
/stories/[slug]
```

Show:

```txt
title
summary
body
chapter list
related worlds
related characters
```

## Deliverables

```txt
story detail route
chapter list component
```

## Smoke Checks

Click story from list to detail.

## Done When

A story page can show metadata and chapters.

---

# Phase 29: Public Chapter Reader

## Purpose

Render individual chapters.

## Scope

Build:

```txt
/stories/[storySlug]/chapters/[chapterSlug]
```

Show:

```txt
story title
chapter title
body
previous chapter
next chapter
```

## Deliverables

```txt
chapter reader route
reader layout component
```

## Smoke Checks

Navigate between chapters.

## Done When

Chapters can be read cleanly on desktop and mobile.

---

# Phase 30: Public Timeline Page

## Purpose

Render the universe timeline.

## Scope

Build:

```txt
/timeline
```

Show timeline events sorted by:

```txt
era
sort_order
year_label
```

## Deliverables

```txt
timeline route
timeline event component
```

## Smoke Checks

Seed timeline appears in correct order.

## Done When

Timeline data renders publicly.

---

# Phase 31: Public Search Page

## Purpose

Add basic search across published content.

## Scope

Build search over:

```txt
entities.name
entities.summary
entities.description
stories.body
chapters.body
```

Use PostgreSQL search or simple query matching initially.

## Deliverables

```txt
/search
server-side search query
search result component
```

## Smoke Checks

Search can find seeded worlds, characters, artifacts, and stories.

## Done When

Users can search the codex.

---

# Phase 32: Admin Auth Schema

## Purpose

Create database support for creator login.

## Scope

Create:

```txt
users
sessions
```

Fields:

```txt
email
password_hash
role
created_at
updated_at
expires_at
```

## Deliverables

```txt
auth schema
migration
auth docs
```

## Smoke Checks

Create local admin user through script.

## Done When

Admin identity can exist in database.

---

# Phase 33: Password Hashing

## Purpose

Add secure password storage.

## Scope

Install password hashing library.

Create utilities for:

```txt
hash password
verify password
```

## Deliverables

```txt
app/src/lib/server/auth/password.ts
tests for hash/verify
```

## Smoke Checks

Correct password verifies.

Wrong password fails.

## Done When

Passwords are never stored in plain text.

---

# Phase 34: Login Route

## Purpose

Create admin login.

## Scope

Build:

```txt
/admin/login
```

Includes:

```txt
login form
server action
session creation
error states
```

## Deliverables

```txt
login route
session cookie logic
```

## Smoke Checks

Valid admin can log in.

Invalid login fails.

## Done When

Admin login works locally.

---

# Phase 35: Logout Route

## Purpose

Create admin logout.

## Scope

Build:

```txt
/admin/logout
```

Includes:

```txt
session deletion
cookie clearing
redirect
```

## Deliverables

```txt
logout route
```

## Smoke Checks

Logged-in admin can log out.

## Done When

Session can be terminated cleanly.

---

# Phase 36: Admin Route Guard

## Purpose

Protect admin pages.

## Scope

Add server-side auth check for:

```txt
/admin/*
```

Redirect unauthenticated users to login.

## Deliverables

```txt
admin layout server guard
auth helper
```

## Smoke Checks

Unauthenticated users cannot access `/admin`.

## Done When

Admin area is protected.

---

# Phase 37: Admin Dashboard Shell

## Purpose

Create the admin interface frame.

## Scope

Build:

```txt
/admin
```

Includes:

```txt
sidebar
topbar
content area
logout control
quick stats placeholders
```

## Deliverables

```txt
admin layout components
admin dashboard route
```

## Smoke Checks

Logged-in admin sees dashboard.

## Done When

Admin area has a reusable layout.

---

# Phase 38: Admin World Create

## Purpose

Create worlds from the admin UI.

## Scope

Build:

```txt
/admin/worlds/new
```

Fields:

```txt
name
slug
summary
description
status
world-specific fields
```

## Deliverables

```txt
world create form
server action
validation
```

## Smoke Checks

Create a world through UI.

## Done When

Admin can create worlds without scripts.

---

# Phase 39: Admin World Edit

## Purpose

Edit existing worlds.

## Scope

Build:

```txt
/admin/worlds
/admin/worlds/[id]/edit
```

Includes:

```txt
list
edit form
update action
validation
```

## Deliverables

```txt
world admin list
world edit route
```

## Smoke Checks

Edit a world and confirm public page updates.

## Done When

Admin can manage worlds.

---

# Phase 40: Admin Character Create

## Purpose

Create characters from the admin UI.

## Scope

Build:

```txt
/admin/characters/new
```

Fields:

```txt
name
slug
alias
summary
biography
origin world
status
power notes
```

## Deliverables

```txt
character create form
validation
```

## Smoke Checks

Create character through UI.

## Done When

Admin can create characters.

---

# Phase 41: Admin Character Edit

## Purpose

Edit existing characters.

## Scope

Build:

```txt
/admin/characters
/admin/characters/[id]/edit
```

## Deliverables

```txt
character admin list
character edit route
```

## Smoke Checks

Edit character and confirm public page updates.

## Done When

Admin can manage characters.

---

# Phase 42: Admin Artifact Create

## Purpose

Create artifacts from the admin UI.

## Scope

Build:

```txt
/admin/artifacts/new
```

Fields:

```txt
name
slug
summary
history
origin world
power notes
curse notes
status
```

## Deliverables

```txt
artifact create form
validation
```

## Smoke Checks

Create artifact through UI.

## Done When

Admin can create artifacts.

---

# Phase 43: Admin Artifact Edit

## Purpose

Edit existing artifacts.

## Scope

Build:

```txt
/admin/artifacts
/admin/artifacts/[id]/edit
```

## Deliverables

```txt
artifact admin list
artifact edit route
```

## Smoke Checks

Edit artifact and confirm public page updates.

## Done When

Admin can manage artifacts.

---

# Phase 44: Admin Story Create

## Purpose

Create stories from the admin UI.

## Scope

Build:

```txt
/admin/stories/new
```

Fields:

```txt
title
slug
summary
body
canon status
release status
```

## Deliverables

```txt
story create form
validation
```

## Smoke Checks

Create story through UI.

## Done When

Admin can create stories.

---

# Phase 45: Admin Story Edit

## Purpose

Edit existing stories.

## Scope

Build:

```txt
/admin/stories
/admin/stories/[id]/edit
```

## Deliverables

```txt
story admin list
story edit route
```

## Smoke Checks

Edit story and confirm public page updates.

## Done When

Admin can manage stories.

---

# Phase 46: Admin Chapter Create

## Purpose

Create chapters from the admin UI.

## Scope

Build:

```txt
/admin/stories/[storyId]/chapters/new
```

Fields:

```txt
chapter number
slug
title
summary
body
status
```

## Deliverables

```txt
chapter create form
validation
```

## Smoke Checks

Create chapter through UI.

## Done When

Admin can create chapters.

---

# Phase 47: Admin Chapter Edit

## Purpose

Edit existing chapters.

## Scope

Build:

```txt
/admin/stories/[storyId]/chapters/[chapterId]/edit
```

## Deliverables

```txt
chapter edit form
```

## Smoke Checks

Edit chapter and confirm reader updates.

## Done When

Admin can manage chapters.

---

# Phase 48: Admin Relationship Manager

## Purpose

Manage canon graph links.

## Scope

Build UI to create relationships:

```txt
source entity
relation type
target entity
description
sort order
```

## Deliverables

```txt
/admin/relationships
relationship create form
relationship delete action
```

## Smoke Checks

Create relation through UI and confirm public detail page shows it.

## Done When

Admin can connect entities without database scripts.

---

# Phase 49: Admin Timeline Event Create

## Purpose

Create timeline events from admin UI.

## Scope

Build:

```txt
/admin/timeline/new
```

Fields:

```txt
name
era
year label
sort order
summary
body
status
```

## Deliverables

```txt
timeline create form
```

## Smoke Checks

Create timeline event through UI.

## Done When

Admin can create timeline events.

---

# Phase 50: Admin Timeline Event Edit

## Purpose

Edit existing timeline events.

## Scope

Build:

```txt
/admin/timeline
/admin/timeline/[id]/edit
```

## Deliverables

```txt
timeline admin list
timeline edit route
```

## Smoke Checks

Edit timeline event and confirm public page updates.

## Done When

Admin can manage timeline events.

---

# Phase 51: Media Asset Schema

## Purpose

Create database support for media.

## Scope

Create:

```txt
media_assets
```

Fields:

```txt
id
slug
original_filename
stored_filename
relative_path
mime_type
media_kind
size_bytes
width
height
duration_seconds
alt_text
caption
created_at
updated_at
```

## Deliverables

```txt
media schema
migration
media docs
```

## Smoke Checks

Insert media metadata manually or through seed.

## Done When

Media metadata can be stored.

---

# Phase 52: Local Media Storage Directories

## Purpose

Create safe filesystem layout for uploaded media.

## Scope

Define directories:

```txt
media/originals
media/images
media/videos
media/thumbnails
media/models
media/tmp
```

Add `.gitignore` rules.

## Deliverables

```txt
media directory docs
filesystem helper
```

## Smoke Checks

App can resolve media root safely.

## Done When

Media storage location is deterministic and outside source control.

---

# Phase 53: Image Upload Backend

## Purpose

Support image uploads.

## Scope

Build server logic for:

```txt
accept image upload
validate MIME type
limit file size
generate safe filename
store original image
write media_assets row
```

No thumbnails yet.

## Deliverables

```txt
image upload server action
media validation utilities
```

## Smoke Checks

Upload PNG/JPG/WebP from admin.

Reject invalid file.

## Done When

Images can be uploaded safely.

---

# Phase 54: Admin Media Library

## Purpose

Browse uploaded media.

## Scope

Build:

```txt
/admin/media
```

Show:

```txt
preview
filename
kind
size
created date
```

## Deliverables

```txt
media library route
media grid component
```

## Smoke Checks

Uploaded images appear in admin media library.

## Done When

Admin can view uploaded media.

---

# Phase 55: Image Thumbnail Generation

## Purpose

Generate optimized thumbnails.

## Scope

Add image processing for:

```txt
small thumbnail
medium preview
public optimized image
```

Use a server-side image library.

## Deliverables

```txt
image processor
thumbnail paths
metadata update
```

## Smoke Checks

Upload image and confirm generated derivatives exist.

## Done When

Uploaded images have optimized variants.

---

# Phase 56: Public Media Serving

## Purpose

Serve media files safely.

## Scope

Add route or static serving config for public media.

Requirements:

```txt
no directory traversal
cache headers
correct MIME type
404 handling
```

## Deliverables

```txt
media serving route or Caddy config
docs/media/serving.md
```

## Smoke Checks

Public pages can display uploaded images.

## Done When

Media displays publicly through stable URLs.

---

# Phase 57: Entity Featured Image

## Purpose

Attach images to entities.

## Scope

Add featured image fields:

```txt
entities.featured_media_id
```

Update public pages to show featured images.

## Deliverables

```txt
schema migration
admin image selector
public image rendering
```

## Smoke Checks

Assign character portrait and confirm it appears publicly.

## Done When

Entities can have featured images.

---

# Phase 58: Story Cover Image

## Purpose

Attach cover images to stories.

## Scope

Add:

```txt
stories.cover_media_id
```

Update admin and public story pages.

## Deliverables

```txt
story cover schema
admin selector
public cover rendering
```

## Smoke Checks

Assign story cover and confirm it appears publicly.

## Done When

Stories can have cover images.

---

# Phase 59: Image Gallery Relationship

## Purpose

Allow multiple images per entity.

## Scope

Create:

```txt
entity_media
```

Fields:

```txt
entity_id
media_asset_id
role
sort_order
caption_override
```

## Deliverables

```txt
entity media schema
migration
gallery docs
```

## Smoke Checks

Attach multiple images to one world.

## Done When

Entities can have media galleries.

---

# Phase 60: Public Entity Galleries

## Purpose

Render image galleries on public entity pages.

## Scope

Add gallery display to:

```txt
world detail
character detail
artifact detail
story detail
```

## Deliverables

```txt
gallery component
public gallery integration
```

## Smoke Checks

Attached images appear in gallery.

## Done When

Public pages can show multiple images per entity.

---

# Phase 61: Video Upload Backend

## Purpose

Support basic video uploads.

## Scope

Build server logic for:

```txt
accept MP4/WebM
validate MIME type
limit file size
store original video
write media_assets row
```

No transcoding yet.

## Deliverables

```txt
video upload support
video validation docs
```

## Smoke Checks

Upload small MP4.

Reject invalid file.

## Done When

Videos can be uploaded safely.

---

# Phase 62: Public Video Display

## Purpose

Display uploaded videos.

## Scope

Create reusable video component using native HTML video.

Support:

```txt
poster image
controls
caption
responsive sizing
```

## Deliverables

```txt
VideoPlayer.svelte
public media integration
```

## Smoke Checks

A video plays on a public page.

## Done When

Videos are visible and playable.

---

# Phase 63: Markdown Rendering

## Purpose

Allow rich written lore/story content.

## Scope

Add safe Markdown rendering for:

```txt
entity descriptions
story body
chapter body
timeline body
```

Requirements:

```txt
sanitize output
support headings
support links
support lists
support blockquotes
support code blocks
```

## Deliverables

```txt
markdown renderer
markdown docs
```

## Smoke Checks

Markdown renders correctly and unsafe HTML is blocked.

## Done When

Long-form text can be written cleanly.

---

# Phase 64: Slug Validation and Collision Handling

## Purpose

Prevent broken URLs.

## Scope

Add utilities for:

```txt
slug generation
slug validation
duplicate slug detection
reserved slug blocking
```

## Deliverables

```txt
slug utility
tests
admin validation integration
```

## Smoke Checks

Duplicate slug fails cleanly.

Invalid slug fails cleanly.

## Done When

Public URLs are stable and protected.

---

# Phase 65: Draft and Published Filtering

## Purpose

Separate private drafts from public content.

## Scope

Enforce public queries to show only:

```txt
status = published
```

Admin can see:

```txt
draft
published
archived
```

## Deliverables

```txt
status helper
public query updates
tests
```

## Smoke Checks

Draft content is hidden publicly.

Published content is visible.

## Done When

Public site does not leak drafts.

---

# Phase 66: Canon Status System

## Purpose

Track canon state.

## Scope

Define canon statuses:

```txt
canon
variant
legend
retired
non_canon
```

Expose on admin forms and public pages.

## Deliverables

```txt
canon status docs
UI badges
query support
```

## Smoke Checks

Set canon status and confirm badge renders.

## Done When

Canon state is visible and manageable.

---

# Phase 67: UI Component Pass

## Purpose

Consolidate reusable visual components.

## Scope

Create components:

```txt
Button
Card
Badge
Panel
PageHeader
SectionHeader
EntityCard
MediaFrame
EmptyState
FormField
```

Do not redesign full pages yet.

## Deliverables

```txt
app/src/lib/components/ui/*
docs/design/components.md
```

## Smoke Checks

Existing pages use shared components.

## Done When

UI is no longer one-off page sludge.

---

# Phase 68: Public Visual Polish Pass

## Purpose

Make the public site feel premium.

## Scope

Polish:

```txt
homepage
world list/detail
character list/detail
artifact list/detail
story list/detail
timeline
search
```

Focus:

```txt
spacing
typography
card design
hover states
empty states
responsive behavior
visual consistency
```

## Deliverables

```txt
updated public routes
design notes
```

## Smoke Checks

Desktop/mobile visual pass.

## Done When

Public pages feel cohesive and intentional.

---

# Phase 69: Admin Visual Polish Pass

## Purpose

Make admin pleasant to use.

## Scope

Polish:

```txt
dashboard
forms
lists
media library
relationship manager
timeline manager
```

Focus:

```txt
dense but readable layout
clear save feedback
validation messages
navigation clarity
```

## Deliverables

```txt
updated admin routes
admin UX notes
```

## Smoke Checks

Create/edit content flows are usable without confusion.

## Done When

Admin feels like a real tool, not a basement wiring panel.

---

# Phase 70: Form Validation Standardization

## Purpose

Unify validation behavior.

## Scope

Add shared validation patterns for:

```txt
required fields
slug fields
enum fields
text length
file uploads
relationship selections
```

## Deliverables

```txt
validation helpers
form error components
tests
```

## Smoke Checks

Invalid forms fail with useful messages.

## Done When

Forms behave consistently.

---

# Phase 71: Error Page System

## Purpose

Handle failures cleanly.

## Scope

Create:

```txt
404 page
500 page
admin error states
not found helpers
```

## Deliverables

```txt
error routes
error components
```

## Smoke Checks

Visit missing slug and confirm polished 404.

## Done When

Errors look intentional.

---

# Phase 72: Loading and Empty States

## Purpose

Improve perceived polish.

## Scope

Add:

```txt
loading states
empty states
skeleton cards where useful
no-results states
```

## Deliverables

```txt
loading components
empty state components
route integrations
```

## Smoke Checks

Empty database does not look broken.

## Done When

Blank states feel designed.

---

# Phase 73: Accessibility Pass

## Purpose

Make the site usable and structurally sane.

## Scope

Review:

```txt
semantic HTML
keyboard navigation
focus states
color contrast
alt text
form labels
button names
heading order
```

## Deliverables

```txt
docs/quality/accessibility.md
accessibility fixes
```

## Smoke Checks

Keyboard navigate major routes.

Run browser accessibility audit.

## Done When

Core flows are accessible.

---

# Phase 74: SEO Metadata

## Purpose

Prepare public pages for indexing and sharing.

## Scope

Add metadata for:

```txt
title
description
canonical URL
Open Graph image
Open Graph type
Twitter card metadata
```

## Deliverables

```txt
SEO helper
route metadata integration
```

## Smoke Checks

Inspect rendered page head.

## Done When

Public pages have clean metadata.

---

# Phase 75: Sitemap

## Purpose

Generate sitemap for published content.

## Scope

Build:

```txt
/sitemap.xml
```

Include:

```txt
homepage
worlds
characters
artifacts
stories
chapters
timeline
```

## Deliverables

```txt
sitemap route
```

## Smoke Checks

Visit `/sitemap.xml`.

## Done When

Published pages are discoverable.

---

# Phase 76: Robots.txt

## Purpose

Control crawler basics.

## Scope

Build:

```txt
/robots.txt
```

Rules:

```txt
allow public site
disallow admin
link sitemap
```

## Deliverables

```txt
robots route
```

## Smoke Checks

Visit `/robots.txt`.

## Done When

Crawler rules are explicit.

---

# Phase 77: RSS Feed

## Purpose

Expose updates for new stories/content.

## Scope

Build:

```txt
/rss.xml
```

Include latest published:

```txt
stories
chapters
timeline events
```

## Deliverables

```txt
RSS route
feed docs
```

## Smoke Checks

Validate feed XML.

## Done When

Public updates can be subscribed to.

---

# Phase 78: Basic Analytics Logging

## Purpose

Track site usage without third-party dependency.

## Scope

Add privacy-friendly server logs for:

```txt
route hits
referer
user agent
timestamp
status code
```

Avoid invasive tracking.

## Deliverables

```txt
access log docs
optional DB table or Caddy log config
```

## Smoke Checks

Request pages and verify logs.

## Done When

Basic traffic visibility exists.

---

# Phase 79: Test Framework Setup

## Purpose

Add automated test foundation.

## Scope

Install and configure:

```txt
unit test runner
Svelte component testing if needed
Playwright for browser tests
```

## Deliverables

```txt
test config
test scripts
docs/dev/testing.md
```

## Smoke Checks

```bash
pnpm test
pnpm test:e2e
```

## Done When

Test commands run successfully.

---

# Phase 80: Unit Tests for Core Utilities

## Purpose

Protect core logic.

## Scope

Test:

```txt
slug utilities
env validation
password helpers
media validation
relationship helpers
status filters
```

## Deliverables

```txt
unit tests
```

## Smoke Checks

All unit tests pass.

## Done When

Core utility behavior is covered.

---

# Phase 81: Database Query Tests

## Purpose

Protect data access behavior.

## Scope

Test:

```txt
published filtering
entity loading
relationship loading
story/chapter loading
timeline sorting
search queries
```

## Deliverables

```txt
database tests
test database setup docs
```

## Smoke Checks

Run tests against disposable test database.

## Done When

Important query behavior is verified.

---

# Phase 82: Public E2E Smoke Tests

## Purpose

Verify public browsing flows.

## Scope

Test:

```txt
homepage loads
world list loads
world detail loads
character detail loads
story reader loads
timeline loads
search works
404 works
```

## Deliverables

```txt
Playwright public smoke tests
```

## Smoke Checks

```bash
pnpm test:e2e
```

## Done When

Public site flows are covered.

---

# Phase 83: Admin E2E Smoke Tests

## Purpose

Verify admin creation flows.

## Scope

Test:

```txt
login
create world
create character
create artifact
create story
create chapter
create relationship
upload image
logout
```

## Deliverables

```txt
Playwright admin smoke tests
```

## Smoke Checks

Admin E2E suite passes.

## Done When

Admin flows are covered by browser tests.

---

# Phase 84: Backup Script

## Purpose

Protect database and media.

## Scope

Create script to backup:

```txt
PostgreSQL dump
media directory archive
.env exclusion confirmation
```

## Deliverables

```txt
scripts/backup.sh
docs/ops/backups.md
```

## Smoke Checks

Run backup locally and inspect output.

## Done When

A full local backup can be generated.

---

# Phase 85: Restore Script

## Purpose

Verify backups are useful.

## Scope

Create restore script for:

```txt
database dump
media archive
```

Use only in local/VM environment first.

## Deliverables

```txt
scripts/restore.sh
docs/ops/restore.md
```

## Smoke Checks

Restore into fresh local database and media directory.

## Done When

Backup/restore loop is proven.

---

# Phase 86: Production Build Script

## Purpose

Create a reproducible native production build path without Docker.

## Scope

Create scripts and documentation for:

```txt
installing production dependencies
building the SvelteKit app
verifying the build output
running the built Node server locally
checking required environment variables
```

## Deliverables

```txt
scripts/build-prod.sh
scripts/run-prod-local.sh
docs/ops/native-production-build.md
```

## Smoke Checks

```bash
scripts/build-prod.sh
scripts/run-prod-local.sh
curl -f http://127.0.0.1:3000/health
```

## Done When

The app can be built and run with native Node commands from a clean checkout without Docker.
---

# Phase 87: Native Service Layout

## Purpose

Define production services using host-installed Linux services instead of Docker Compose.

## Scope

Create native service layout for:

```txt
app systemd service
postgresql system service
caddy system service
media directory
backup directory
environment file
release directory
```

## Deliverables

```txt
infra/systemd/multiverse-codex.service
infra/caddy/Caddyfile
docs/ops/native-service-layout.md
docs/ops/systemd.md
```

## Smoke Checks

```bash
systemd-analyze verify infra/systemd/multiverse-codex.service
caddy validate --config infra/caddy/Caddyfile
```

## Done When

Production-like services are defined as native Linux services and can be validated without Docker.
---

# Phase 88: Caddy Reverse Proxy

## Purpose

Serve the app through a reverse proxy.

## Scope

Configure Caddy for:

```txt
domain placeholder
HTTPS-ready config
reverse proxy to native app service
static/media route if needed
security headers
compression
```

## Deliverables

```txt
infra/caddy/Caddyfile
docs/ops/caddy.md
```

## Smoke Checks

Visit app through Caddy locally or VM.

## Done When

Caddy can route traffic to the app.

---

# Phase 89: Health Check Endpoint

## Purpose

Expose deploy readiness signal.

## Scope

Build:

```txt
/health
```

Return:

```txt
app status
database connectivity
timestamp
```

Do not expose secrets.

## Deliverables

```txt
health route
health docs
```

## Smoke Checks

Visit `/health`.

Stop database and confirm degraded response.

## Done When

Deployment can check app health.

---

# Phase 90: Structured Logging

## Purpose

Make production failures debuggable.

## Scope

Standardize logs for:

```txt
startup
database errors
auth errors
media upload errors
request failures
```

## Deliverables

```txt
logger utility
logging docs
```

## Smoke Checks

Trigger controlled error and inspect logs.

## Done When

The app emits useful logs.

---

# Phase 91: Security Headers

## Purpose

Add baseline browser security hardening.

## Scope

Configure headers:

```txt
Content-Security-Policy
X-Frame-Options or frame-ancestors
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

## Deliverables

```txt
Caddy header config
docs/ops/security-headers.md
```

## Smoke Checks

Inspect headers in browser devtools or curl.

## Done When

Security headers are present.

---

# Phase 92: Rate Limiting for Auth

## Purpose

Protect login route from brute force.

## Scope

Add rate limit for:

```txt
/admin/login
```

Could be in app code or reverse proxy.

## Deliverables

```txt
rate limit utility/config
auth security docs
```

## Smoke Checks

Repeated failed login attempts get throttled.

## Done When

Login endpoint is not wide open.

---

# Phase 93: Media Upload Limits

## Purpose

Prevent accidental server abuse.

## Scope

Enforce:

```txt
max image size
max video size
allowed MIME types
per-upload validation
clear error messages
```

## Deliverables

```txt
upload limit config
docs/media/limits.md
```

## Smoke Checks

Oversized upload fails cleanly.

## Done When

Media upload limits are enforced.

---

# Phase 94: VM Provisioning Notes

## Purpose

Prepare local VM test environment.

## Scope

Document VM setup:

```txt
Ubuntu Server install
Node and pnpm install
PostgreSQL install
Caddy install
application system user
user permissions
firewall basics
SSH access
project clone
env setup
systemd service setup
```

## Deliverables

```txt
docs/ops/vm-setup.md
```

## Smoke Checks

A clean VM can be prepared from docs.

## Done When

VM setup is repeatable.

---

# Phase 95: VM Deployment Dry Run

## Purpose

Deploy to a clean VM.

## Scope

On a local VM:

```txt
clone repo
create env file
install native service files
start PostgreSQL
start Caddy
start app systemd service
run migrations
create admin user
seed optional demo data
```

## Deliverables

```txt
deployment notes
updated docs
```

## Smoke Checks

Visit the site from host browser.

## Done When

The full stack runs on a clean VM.

---

# Phase 96: VM Backup/Restore Test

## Purpose

Prove operational recovery on VM.

## Scope

On VM:

```txt
create content
upload media
run backup
wipe app data
restore backup
verify content/media returned
```

## Deliverables

```txt
docs/ops/vm-backup-restore-report.md
```

## Smoke Checks

Restored site matches pre-wipe state.

## Done When

Backup/restore works outside local dev machine.

---

# Phase 97: VM Public Flow Test

## Purpose

Verify public user experience on production-like deployment.

## Scope

Test on VM:

```txt
homepage
worlds
characters
artifacts
stories
chapters
timeline
search
media display
mobile viewport
```

## Deliverables

```txt
docs/quality/public-vm-smoke.md
```

## Done When

Public experience works cleanly on VM.

---

# Phase 98: VM Admin Flow Test

## Purpose

Verify creator workflow on production-like deployment.

## Scope

Test on VM:

```txt
login
create/edit all core entities
upload image
upload video
attach media
create relationship
create timeline event
publish draft
logout
```

## Deliverables

```txt
docs/quality/admin-vm-smoke.md
```

## Done When

Admin workflow is proven on VM.

---

# Phase 99: Performance Baseline

## Purpose

Measure current performance before VPS launch.

## Scope

Measure:

```txt
homepage load
entity list load
entity detail load
story reader load
media-heavy page load
database query timings
bundle size
```

## Deliverables

```txt
docs/quality/performance-baseline.md
```

## Smoke Checks

Run Lighthouse or equivalent local browser audit.

## Done When

Performance baseline exists and major issues are documented.

---

# Phase 100: Production Content Empty-State Pass

## Purpose

Make the site ready before real content exists.

## Scope

Review empty and low-content cases:

```txt
no worlds
no characters
no artifacts
no stories
no media
no timeline events
no search results
```

## Deliverables

```txt
empty-state copy and UI updates
```

## Done When

A fresh site does not look broken before content is added.

---

# Phase 101: Final Design Polish Pass

## Purpose

Finish the first-launch visual layer.

## Scope

Polish:

```txt
animation timing
hover states
focus states
mobile spacing
typography scale
card consistency
background effects
3D placeholders if 3D is not active yet
```

## Deliverables

```txt
final UI polish commits
docs/design/final-polish-notes.md
```

## Done When

The site feels clean, smooth, futuristic, and coherent.

---

# Phase 102: Basic Three.js Scene Setup

## Purpose

Create the foundation for the future 3D viewport.

## Scope

Build:

```txt
/cosmos
```

Add:

```txt
Three.js canvas
camera
controls
basic starfield
placeholder world nodes
click handling scaffold
```

Do not connect database yet.

## Deliverables

```txt
CosmosViewport.svelte
/cosmos route
```

## Smoke Checks

3D scene renders and does not crash on mobile.

## Done When

The 3D viewport foundation exists.

---

# Phase 103: Database-Driven Cosmos Nodes

## Purpose

Connect worlds to the 3D viewport.

## Scope

Load published worlds into `/cosmos`.

Represent each world as:

```txt
node
label
click target
summary panel
link to world page
```

## Deliverables

```txt
cosmos data loader
world node component/logic
```

## Smoke Checks

Seed worlds appear as clickable nodes.

## Done When

The 3D viewport reflects database content.

---

# Phase 104: Cosmos Visual Polish

## Purpose

Make the 3D viewport feel intentional.

## Scope

Polish:

```txt
starfield
node hover states
selection panel
transitions
camera movement
mobile fallback
reduced motion fallback
```

## Deliverables

```txt
cosmos polish updates
docs/design/cosmos.md
```

## Smoke Checks

Clicking nodes feels smooth and does not wreck performance.

## Done When

The 3D viewport feels like a real feature, not a tech demo glued to a wall.

---

# Phase 105: Deployment Documentation

## Purpose

Prepare VPS migration instructions.

## Scope

Write complete deployment guide:

```txt
buy domain
point DNS
provision VPS
install Node, pnpm, PostgreSQL, and Caddy
create application system user
clone repo
configure env
install systemd service
start native services
run migrations
create admin user
verify health
enable backups
```

## Deliverables

```txt
docs/ops/vps-deployment.md
```

## Done When

A VPS migration can be followed step-by-step.

---

# Phase 106: Domain and DNS Checklist

## Purpose

Prepare domain launch.

## Scope

Document:

```txt
A record
AAAA record optional
www handling
HTTPS expectation
DNS propagation check
mail records optional
```

## Deliverables

```txt
docs/ops/domain-dns.md
```

## Done When

Domain setup steps are clear.

---

# Phase 107: VPS Readiness Checklist

## Purpose

Confirm the project is ready to leave the VM nest.

## Scope

Create checklist:

```txt
tests pass
E2E passes
VM deploy passes
backup/restore passes
admin login works
media upload works
health endpoint works
Caddy proxy works
systemd app service works
native PostgreSQL service works
domain docs complete
secrets not committed
.env.example current
```

## Deliverables

```txt
docs/ops/vps-readiness-checklist.md
```

## Done When

Every launch gate has a clear pass/fail status.

---

# Phase 108: Content Authoring Guide

## Purpose

Prepare creator workflow for adding real content.

## Scope

Write guide for:

```txt
creating a world
creating a character
creating an artifact
creating a story
creating chapters
uploading media
attaching media
linking relationships
publishing content
draft workflow
canon status usage
```

## Deliverables

```txt
docs/content/authoring-guide.md
```

## Done When

The creator can start adding real universe content without digging through code.

---

# Phase 109: Final VM Release Candidate

## Purpose

Freeze the VPS-ready version.

## Scope

Run final checks:

```txt
unit tests
database tests
E2E tests
lint
typecheck
native production build
VM deployment
VM backup/restore
public smoke test
admin smoke test
```

Tag:

```txt
v0.1.0-vps-ready
```

## Deliverables

```txt
release notes
git tag
final checklist
```

## Done When

The site is polished, VM-tested, and ready to migrate to VPS.

---

# First Real Content Milestone

After Phase 109, the build machine is ready.

The first real creator milestone should be:

```txt
1 published world
3 published characters
1 published faction
1 published artifact
1 published story
2 published chapters
5 uploaded images
1 uploaded video
5 relationships
5 timeline events
```

If that content can be added entirely through the admin UI and viewed cleanly on the public site, the engine is alive.

---

# Future Expansion Phases

These are intentionally not part of the first VPS-ready launch.

## Future Phase: Advanced 3D World Maps

Add deeper maps inside each world.

## Future Phase: Object Storage

Move media from VPS disk to S3-compatible storage.

## Future Phase: CDN

Add CDN for image/video delivery.

## Future Phase: Video Transcoding

Generate adaptive streaming formats.

## Future Phase: Public Accounts

Allow readers to create accounts.

## Future Phase: Favorites and Reading Progress

Track reader engagement.

## Future Phase: Comments

Allow moderated discussion.

## Future Phase: Lore Graph Visualization

Render entity relationships as an interactive graph.

## Future Phase: In-Universe Search Modes

Search by faction, era, world, species, power type, canon status.

## Future Phase: Multi-Timeline Support

Support alternate timelines and variant canons.

## Future Phase: API

Expose public read-only API for published content.

---

# Guiding Principle

Build the content engine first.

Then the polish.

Then the 3D.

Then the scale.

A multiverse does not need to explode into existence.  
It needs a forge that can keep producing worlds without collapsing under its own gravity.
