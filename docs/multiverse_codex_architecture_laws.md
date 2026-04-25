# Multiverse Codex Architecture Laws

## Purpose

This document defines non-negotiable engineering laws for the Multiverse Codex codebase.

A phase, feature, patch, or refactor is not complete if it violates these laws.

---

# 1. Core Law: Separation Before Cleverness

The codebase must favor:

- small modules
- clear boundaries
- explicit contracts
- guarded seams
- testable logic
- replaceable layout
- boring data flow

The codebase must reject:

- god files
- mixed concerns
- hidden side effects
- implicit global state
- UI-driven business rules
- business logic inside layout components
- database calls inside visual components
- filesystem work inside route markup

If a shortcut makes the code harder to test or harder to replace later, it is debt wearing a fake mustache.

---

# 2. Module Size Law

## Hard Rule

No module should exceed:

```txt
1,000 LOC
```

This applies to:

- Svelte components
- server modules
- route loaders
- route actions
- utility modules
- database query modules
- schema files
- test files
- scripts
- CSS files
- Three.js scene modules
- admin modules
- media modules
- deployment scripts

## Preferred Range

```txt
50-300 LOC: ideal
300-500 LOC: acceptable
500-750 LOC: warning zone
750-999 LOC: split plan required
1,000+ LOC: violation unless explicitly justified
```

## Allowed Exception

A file may exceed 1,000 LOC only when all are true:

1. Splitting it would make the code less clear.
2. The excess is temporary.
3. The phase golden documents why.
4. A split plan exists.
5. The file is not mixing unrelated concerns.

Acceptable temporary exceptions:

- generated migration snapshot
- generated type file
- large static fixture
- vendor-generated output

Unacceptable exceptions:

- one huge admin page
- one giant media service
- one mega route action file
- one all-purpose utility file
- one massive Three.js component
- one route doing loading, validation, rendering, persistence, and styling

## Required Split Triggers

Split a module immediately when it contains more than one major role:

- rendering
- data loading
- validation
- persistence
- filesystem access
- authentication
- authorization
- media processing
- business rules
- formatting
- deployment logic
- testing helpers
- 3D scene orchestration
- 3D object construction

## File Review Gate

Before closing any phase, check file sizes.

```bash
find app scripts infra docs -type f \
  \( -name "*.ts" -o -name "*.svelte" -o -name "*.js" -o -name "*.css" -o -name "*.sh" -o -name "*.md" \) \
  -print0 | xargs -0 wc -l | sort -n
```

Any file near or over 750 LOC must be reviewed.

Any file over 1,000 LOC must be split or formally justified in that phase golden.

---

# 3. Hard Seam Law

A seam is a boundary where one part of the system talks to another.

Every important seam must be explicit, guarded, and testable.

## Required Seams

Maintain hard seams between:

- layout and logic
- public routes and admin routes
- server code and client code
- database queries and route handlers
- validation and persistence
- media validation and media storage
- filesystem paths and user input
- auth/session handling and page rendering
- business rules and UI components
- 3D scene data and 3D rendering
- deployment scripts and application code
- configuration and runtime behavior

## Seam Requirements

A seam must have:

- clear module boundary
- typed input
- typed output
- validation or guard when input crosses a trust boundary
- defined failure behavior
- tests or smoke coverage

## Bad Shape

```txt
+page.svelte
  loads form state
  validates data
  writes database rows
  formats business labels
  decides access rules
  renders UI
```

## Good Shape

```txt
+page.server.ts
  calls server functions

world.validation.ts
  validates world input

world.repository.ts
  reads/writes database

world.service.ts
  owns business rules

WorldForm.svelte
  renders the form

WorldDetailView.svelte
  renders display
```

---

# 4. Guard Placement Law

Guards belong at every trust boundary.

A trust boundary exists whenever data moves from:

- browser to server
- user input to validation
- validation to database
- request to filesystem
- database to public rendering
- admin action to mutation
- environment variable to runtime config
- upload to media processor
- slug to URL lookup
- auth cookie to session identity
- external command to script execution

## Required Guard Types

Use the right guard for the boundary:

- input validation
- auth check
- authorization check
- enum validation
- slug validation
- file MIME validation
- file size validation
- path traversal protection
- database constraint
- transaction boundary
- rate limit
- CSRF defense where applicable
- safe error handling
- environment validation
- output sanitization

## Guard Rules

Guards must be:

- server-side for security-critical behavior
- centralized when reused
- tested with valid and invalid cases
- written before persistence
- documented when they define domain behavior

## Forbidden Guard Patterns

Do not rely on:

- client-only validation
- hidden form fields
- disabled buttons
- CSS visibility
- route naming
- frontend-only redirects
- file extensions alone
- "admin won't do that"
- "only I use this"

Every exposed input can be hostile, malformed, oversized, stale, or cursed.

---

# 5. Logic/Layout Split Law

## Hard Rule

Logic must never know what it looks like.

Layout must never care what it does.

They must be separate modules whenever possible.

## Logic Modules May Know

Logic modules may know:

- domain rules
- database schemas
- query shapes
- validation rules
- auth rules
- status transitions
- media storage rules
- filesystem constraints
- relationship rules
- publishing rules
- sorting rules
- search behavior

Logic modules must not know:

- CSS classes
- Tailwind classes
- DOM layout
- animation timing
- component hierarchy
- button placement
- responsive breakpoints
- visual icons
- theme colors

## Layout Modules May Know

Layout modules may know:

- HTML structure
- CSS classes
- Tailwind utilities
- visual hierarchy
- responsive layout
- animation
- slots
- component composition
- icons
- empty-state presentation

Layout modules must not know:

- database queries
- password hashing
- session lookup
- filesystem writes
- media validation internals
- business rule enforcement
- publishing authorization
- relationship mutation rules
- raw environment variables
- backup/restore logic

## Approved Flow

```txt
Route
  -> loader/action
    -> validation
    -> service
    -> repository
    -> database/filesystem

Route
  -> view model
    -> layout component
      -> UI components
```

## Example Directory Shape

```txt
app/src/lib/domain/worlds/
  world.types.ts
  world.validation.ts
  world.service.ts
  world.repository.ts
  world.view-model.ts

app/src/lib/components/worlds/
  WorldCard.svelte
  WorldDetailView.svelte
  WorldForm.svelte
  WorldRelationshipList.svelte
```

The domain folder owns behavior.

The component folder owns appearance.

No cross-contamination.

---

# 6. Route File Law

Route files must stay thin.

## `+page.server.ts`

Allowed:

- read route params
- call auth helper
- call validation helper
- call service/repository
- return data
- handle redirect/error

Not allowed:

- large SQL blocks
- complex business decisions
- inline media processing
- long validation schemas
- HTML/layout assumptions
- large helper functions

## `+page.svelte`

Allowed:

- compose visual components
- pass data into components
- handle local UI state
- dispatch user intent

Not allowed:

- database access
- server-only imports
- business authorization
- raw mutation logic
- media filesystem logic
- password/session logic
- publishing rules

If a route file grows beyond 300-500 LOC, review it for splitting.

---

# 7. Service and Repository Law

## Services

Services own business behavior.

Examples:

- `createWorld()`
- `publishStory()`
- `attachMediaToEntity()`
- `createRelationship()`
- `validateDraftVisibility()`
- `buildCosmosNodeModel()`

Services may call repositories.

Services must not render UI.

## Repositories

Repositories own persistence.

Examples:

- `insertWorld()`
- `findWorldBySlug()`
- `listPublishedStories()`
- `findEntityRelationships()`
- `saveMediaAsset()`

Repositories must not contain UI decisions.

Repositories should not contain high-level business policy unless the policy is strictly database-level.

## Validation

Validation should happen before service mutation and before persistence.

Preferred shape:

```txt
route action
  -> parse form data
  -> validate input
  -> call service
  -> service calls repository
```

---

# 8. View Model Law

When raw data is not ready for layout, create a view model.

View models translate domain data into render-ready shape without owning appearance.

Allowed:

- format relationship groups
- sort timeline display groups
- prepare card summaries
- derive labels
- prepare hrefs
- normalize optional fields

Not allowed:

- choose CSS classes
- choose icons based on visual theme
- perform database calls
- mutate records
- enforce auth

Example:

```txt
world.view-model.ts
  buildWorldDetailViewModel(world, relationships, media)

WorldDetailView.svelte
  renders the view model
```

---

# 9. Media Boundary Law

Media is a hazardous subsystem and must be guarded hard.

## Required Upload Flow

```txt
browser upload
  -> server action
  -> auth guard
  -> size guard
  -> MIME/content guard
  -> safe filename generation
  -> safe path resolution
  -> storage write
  -> metadata write
  -> derivative generation if needed
```

## Required Media Modules

- `media.validation.ts`
- `media.storage.ts`
- `media.repository.ts`
- `media.processor.ts`
- `media.service.ts`
- `media.routes.ts`

Do not put upload validation, filesystem writing, metadata persistence, and UI rendering in one file.

## Hard No

Never derive a filesystem path directly from user input.

Never trust original filenames.

Never expose media roots through unchecked path joining.

---

# 10. Auth Boundary Law

Auth must be server-owned.

## Required Split

- `auth.password.ts`
- `auth.session.ts`
- `auth.guard.ts`
- `auth.repository.ts`
- `auth.service.ts`

## Forbidden

- client-only auth checks
- layout-only admin protection
- plaintext passwords
- session parsing inside UI components
- admin permissions inferred from route names

All admin mutations must run through server-side auth and authorization checks.

---

# 11. Database Boundary Law

Database access must be centralized.

## Allowed

- repository modules
- migration files
- seed scripts
- test fixtures

## Discouraged

- inline queries inside route files
- queries inside Svelte components
- queries duplicated across features
- business logic hidden inside arbitrary SQL fragments

## Required

All schema changes must be represented by tracked migrations.

No manual-only database changes count as complete.

---

# 12. 3D Viewport Boundary Law

The 3D cosmos must be split into layers.

## Required Split

- `cosmos.types.ts`
- `cosmos.data.ts`
- `cosmos.view-model.ts`
- `cosmos.scene.ts`
- `cosmos.objects.ts`
- `cosmos.interaction.ts`
- `CosmosViewport.svelte`

## Responsibilities

```txt
cosmos.data.ts
  loads published world/cosmos data

cosmos.view-model.ts
  prepares node positions and labels

cosmos.scene.ts
  manages scene/camera/renderer lifecycle

cosmos.objects.ts
  builds Three.js objects

cosmos.interaction.ts
  handles raycast/click/hover behavior

CosmosViewport.svelte
  mounts canvas and renders panels
```

## Hard No

No database calls inside Three.js scene code.

No Three.js object construction inside database loaders.

No long-running animation loop without cleanup on unmount.

---

# 13. Script and Ops Boundary Law

Deployment and ops scripts must be boring, explicit, and guarded.

## Scripts Must

- fail fast
- print useful errors
- avoid hidden assumptions
- check required commands
- check required environment variables
- support dry-run where destructive
- avoid hardcoded secrets
- document expected host paths

## Scripts Must Not

- silently continue after failure
- delete data without confirmation or dry-run
- depend on the original workstation
- hide errors with broad redirects
- mix backup, restore, deploy, and provisioning in one mega-script

Split scripts by purpose.

---

# 14. Testing Law

Tests must follow the seam structure.

## Unit Tests

Use for:

- validation
- slug rules
- status filters
- view models
- relationship grouping
- media path helpers
- auth helpers
- formatting utilities

## Integration Tests

Use for:

- repositories
- database queries
- migration behavior
- media metadata flow
- session persistence
- draft/published filtering

## E2E Tests

Use for:

- public browsing
- admin creation flows
- login/logout
- media upload
- relationship creation
- publishing flow

## Smoke Tests

Use for:

- ops scripts
- VM deployment
- backup/restore
- Caddy/systemd behavior
- health checks

No phase closes without tests or smoke checks matching the phase checklist.

---

# 15. Golden Law

Every phase must lock proof.

Each phase golden must include:

- phase number and title
- scope completed
- files changed
- commands run
- test/smoke output
- screenshots/log snippets/schema snapshots where useful
- known limitations
- final commit hash
- hard no review

A golden is not decoration. It is the receipt from the forge.

---

# 16. Professional-Grade Review Checklist

Before any phase closes, answer:

- Is every changed module under 1,000 LOC?
- Did any file enter the warning zone above 750 LOC?
- Are logic and layout separate?
- Are all trust boundaries guarded?
- Are route files thin?
- Are services free of UI assumptions?
- Are components free of persistence/business logic?
- Are repositories free of visual decisions?
- Are media paths safe?
- Are auth checks server-side?
- Are migrations tracked?
- Are tests or smoke checks present?
- Did failure cases fail safely?
- Was a golden created or updated?
- Was deferred work avoided completely?

If any answer is no, the phase is not done.

---

# 17. Naming Law

Name modules by responsibility.

Good:

- `world.repository.ts`
- `world.service.ts`
- `world.validation.ts`
- `world.view-model.ts`
- `WorldCard.svelte`
- `WorldDetailView.svelte`
- `media.storage.ts`
- `media.validation.ts`
- `auth.guard.ts`

Bad:

- `helpers.ts`
- `utils.ts`
- `stuff.ts`
- `manager.ts`
- `common.ts`
- `misc.ts`
- `all.ts`
- `adminThings.ts`
- `doWorlds.ts`

Generic names are allowed only for tiny, obvious, localized helpers.

If a module name cannot explain what belongs inside it, the module is already suspicious.

---

# 18. Dependency Direction Law

Dependencies should flow inward toward logic, not outward toward layout.

Preferred:

```txt
UI component
  -> view model type

route server
  -> service
    -> repository
      -> database
```

Forbidden:

```txt
repository imports Svelte component
service imports CSS
validation imports route component
database module imports layout
Three.js scene imports admin form
```

If dependency direction feels cursed, stop and split the seam.

---

# 19. Completion Failure Conditions

A phase automatically fails closure if it contains:

- module over 1,000 LOC without documented exception
- logic/layout mixing
- unguarded trust boundary
- client-only security
- manual-only database change
- unchecked media path
- unvalidated upload
- route file doing too many jobs
- missing tests/smoke checks
- missing golden
- placeholder counted as done
- deferred TODO/FIXME counted as done
- silent failure behavior
- broken prior golden

No vibes. No handwaving. No "probably fine."

---

# 20. Final Law

The codebase must grow like a city with roads, districts, gates, and maps.

Not like a junk drawer with a login button.

Every module needs a job.

Every seam needs a guard.

Every phase needs proof.

Every violation gets fixed before the next phase begins.
