# Multiverse Codex Phase Explainer

## Estimate Model

A **turn** means one complete implementation cycle with full repo context: inspect relevant code/docs, make the patch, run the phase checks, update docs/goldens, and provide verified results.

Difficulty is scored from **1 to 10**:

- **1-3:** light setup or documentation
- **4-6:** normal feature, schema, UI, or test work
- **7-8:** complex integration, media, E2E, VM, or 3D work
- **9-10:** release-candidate or multi-system verification work

## Summary

- **Phases covered:** 110
- **Phase range:** 0 through 109
- **Estimated total implementation turns:** 132
- **Average difficulty:** 5.3/10
- **Max difficulty:** 9/10

## Phase Matrix

| Phase | Purpose | Dev Difficulty | Estimated Turns |
|---:|---|---:|---:|
| Phase 0: Workstation Bootstrap | Prepare the local development machine with required tools. | 2/10 | 1 |
| Phase 1: Repository Skeleton | Create the empty project repository structure. | 2/10 | 1 |
| Phase 2: Project Vision and Naming Lock | Define the project identity before code sprawl begins. | 2/10 | 1 |
| Phase 3: SvelteKit App Scaffold | Create the initial SvelteKit app. | 3/10 | 1 |
| Phase 4: TailwindCSS Setup | Add styling infrastructure. | 3/10 | 1 |
| Phase 5: Base Layout Shell | Create the public site frame. | 4/10 | 1 |
| Phase 6: Static Landing Page | Create the first polished public page. | 4/10 | 1 |
| Phase 7: Local Docker Compose Foundation | Create local service orchestration. | 5/10 | 1 |
| Phase 8: Environment Configuration | Standardize environment variables. | 5/10 | 1 |
| Phase 9: Database Connection | Connect SvelteKit server code to PostgreSQL. | 5/10 | 1 |
| Phase 10: Database Migration System | Add repeatable schema migration workflow. | 5/10 | 1 |
| Phase 11: Core Entity Base Schema | Create a shared entity foundation. | 5/10 | 1 |
| Phase 12: World Schema | Add worlds as the first real content type. | 5/10 | 1 |
| Phase 13: Character Schema | Add character data model. | 5/10 | 1 |
| Phase 14: Artifact Schema | Add artifact data model. | 5/10 | 1 |
| Phase 15: Faction Schema | Add faction data model. | 5/10 | 1 |
| Phase 16: Story Schema | Add story-level content. | 5/10 | 1 |
| Phase 17: Chapter Schema | Add chapter-level story structure. | 5/10 | 1 |
| Phase 18: Timeline Event Schema | Add timeline support. | 5/10 | 1 |
| Phase 19: Entity Relationship Schema | Create the canon graph. | 5/10 | 1 |
| Phase 20: Seed Data System | Create repeatable demo data. | 4/10 | 1 |
| Phase 21: Public World List Page | Render worlds from the database. | 5/10 | 1 |
| Phase 22: Public World Detail Page | Render one world from the database. | 5/10 | 1 |
| Phase 23: Public Character List Page | Render characters from the database. | 5/10 | 1 |
| Phase 24: Public Character Detail Page | Render one character from the database. | 5/10 | 1 |
| Phase 25: Public Artifact List Page | Render artifacts from the database. | 5/10 | 1 |
| Phase 26: Public Artifact Detail Page | Render one artifact from the database. | 5/10 | 1 |
| Phase 27: Public Story List Page | Render stories from the database. | 5/10 | 1 |
| Phase 28: Public Story Detail Page | Render one story and chapter list. | 5/10 | 1 |
| Phase 29: Public Chapter Reader | Render individual chapters. | 5/10 | 1 |
| Phase 30: Public Timeline Page | Render the universe timeline. | 5/10 | 1 |
| Phase 31: Public Search Page | Add basic search across published content. | 6/10 | 1 |
| Phase 32: Admin Auth Schema | Create database support for creator login. | 5/10 | 1 |
| Phase 33: Password Hashing | Add secure password storage. | 6/10 | 1 |
| Phase 34: Login Route | Create admin login. | 6/10 | 1 |
| Phase 35: Logout Route | Create admin logout. | 4/10 | 1 |
| Phase 36: Admin Route Guard | Protect admin pages. | 6/10 | 1 |
| Phase 37: Admin Dashboard Shell | Create the admin interface frame. | 4/10 | 1 |
| Phase 38: Admin World Create | Create worlds from the admin UI. | 6/10 | 1 |
| Phase 39: Admin World Edit | Edit existing worlds. | 6/10 | 1 |
| Phase 40: Admin Character Create | Create characters from the admin UI. | 6/10 | 1 |
| Phase 41: Admin Character Edit | Edit existing characters. | 6/10 | 1 |
| Phase 42: Admin Artifact Create | Create artifacts from the admin UI. | 6/10 | 1 |
| Phase 43: Admin Artifact Edit | Edit existing artifacts. | 6/10 | 1 |
| Phase 44: Admin Story Create | Create stories from the admin UI. | 6/10 | 1 |
| Phase 45: Admin Story Edit | Edit existing stories. | 6/10 | 1 |
| Phase 46: Admin Chapter Create | Create chapters from the admin UI. | 6/10 | 1 |
| Phase 47: Admin Chapter Edit | Edit existing chapters. | 6/10 | 1 |
| Phase 48: Admin Relationship Manager | Manage canon graph links. | 7/10 | 2 |
| Phase 49: Admin Timeline Event Create | Create timeline events from admin UI. | 6/10 | 1 |
| Phase 50: Admin Timeline Event Edit | Edit existing timeline events. | 6/10 | 1 |
| Phase 51: Media Asset Schema | Create database support for media. | 5/10 | 1 |
| Phase 52: Local Media Storage Directories | Create safe filesystem layout for uploaded media. | 4/10 | 1 |
| Phase 53: Image Upload Backend | Support image uploads. | 7/10 | 2 |
| Phase 54: Admin Media Library | Browse uploaded media. | 4/10 | 1 |
| Phase 55: Image Thumbnail Generation | Generate optimized thumbnails. | 6/10 | 1 |
| Phase 56: Public Media Serving | Serve media files safely. | 6/10 | 1 |
| Phase 57: Entity Featured Image | Attach images to entities. | 6/10 | 1 |
| Phase 58: Story Cover Image | Attach cover images to stories. | 6/10 | 1 |
| Phase 59: Image Gallery Relationship | Allow multiple images per entity. | 6/10 | 1 |
| Phase 60: Public Entity Galleries | Render image galleries on public entity pages. | 4/10 | 1 |
| Phase 61: Video Upload Backend | Support basic video uploads. | 7/10 | 2 |
| Phase 62: Public Video Display | Display uploaded videos. | 4/10 | 1 |
| Phase 63: Markdown Rendering | Allow rich written lore/story content. | 6/10 | 1 |
| Phase 64: Slug Validation and Collision Handling | Prevent broken URLs. | 4/10 | 1 |
| Phase 65: Draft and Published Filtering | Separate private drafts from public content. | 6/10 | 1 |
| Phase 66: Canon Status System | Track canon state. | 4/10 | 1 |
| Phase 67: UI Component Pass | Consolidate reusable visual components. | 6/10 | 2 |
| Phase 68: Public Visual Polish Pass | Make the public site feel premium. | 7/10 | 2 |
| Phase 69: Admin Visual Polish Pass | Make admin pleasant to use. | 7/10 | 2 |
| Phase 70: Form Validation Standardization | Unify validation behavior. | 4/10 | 1 |
| Phase 71: Error Page System | Handle failures cleanly. | 4/10 | 1 |
| Phase 72: Loading and Empty States | Improve perceived polish. | 4/10 | 1 |
| Phase 73: Accessibility Pass | Make the site usable and structurally sane. | 7/10 | 2 |
| Phase 74: SEO Metadata | Prepare public pages for indexing and sharing. | 4/10 | 1 |
| Phase 75: Sitemap | Generate sitemap for published content. | 4/10 | 1 |
| Phase 76: Robots.txt | Control crawler basics. | 4/10 | 1 |
| Phase 77: RSS Feed | Expose updates for new stories/content. | 4/10 | 1 |
| Phase 78: Basic Analytics Logging | Track site usage without third-party dependency. | 4/10 | 1 |
| Phase 79: Test Framework Setup | Add automated test foundation. | 4/10 | 1 |
| Phase 80: Unit Tests for Core Utilities | Protect core logic. | 4/10 | 1 |
| Phase 81: Database Query Tests | Protect data access behavior. | 7/10 | 2 |
| Phase 82: Public E2E Smoke Tests | Verify public browsing flows. | 7/10 | 2 |
| Phase 83: Admin E2E Smoke Tests | Verify admin creation flows. | 7/10 | 2 |
| Phase 84: Backup Script | Protect database and media. | 6/10 | 1 |
| Phase 85: Restore Script | Verify backups are useful. | 7/10 | 2 |
| Phase 86: Production Dockerfile | Containerize the app for deployment. | 6/10 | 1 |
| Phase 87: Production Docker Compose | Define production service layout. | 7/10 | 2 |
| Phase 88: Caddy Reverse Proxy | Serve the app through a reverse proxy. | 5/10 | 1 |
| Phase 89: Health Check Endpoint | Expose deploy readiness signal. | 5/10 | 1 |
| Phase 90: Structured Logging | Make production failures debuggable. | 5/10 | 1 |
| Phase 91: Security Headers | Add baseline browser security hardening. | 5/10 | 1 |
| Phase 92: Rate Limiting for Auth | Protect login route from brute force. | 6/10 | 1 |
| Phase 93: Media Upload Limits | Prevent accidental server abuse. | 5/10 | 1 |
| Phase 94: VM Provisioning Notes | Prepare local VM test environment. | 4/10 | 1 |
| Phase 95: VM Deployment Dry Run | Deploy to a clean VM. | 8/10 | 2 |
| Phase 96: VM Backup/Restore Test | Prove operational recovery on VM. | 8/10 | 2 |
| Phase 97: VM Public Flow Test | Verify public user experience on production-like deployment. | 4/10 | 1 |
| Phase 98: VM Admin Flow Test | Verify creator workflow on production-like deployment. | 7/10 | 2 |
| Phase 99: Performance Baseline | Measure current performance before VPS launch. | 6/10 | 1 |
| Phase 100: Production Content Empty-State Pass | Make the site ready before real content exists. | 4/10 | 1 |
| Phase 101: Final Design Polish Pass | Finish the first-launch visual layer. | 7/10 | 2 |
| Phase 102: Basic Three.js Scene Setup | Create the foundation for the future 3D viewport. | 7/10 | 2 |
| Phase 103: Database-Driven Cosmos Nodes | Connect worlds to the 3D viewport. | 8/10 | 2 |
| Phase 104: Cosmos Visual Polish | Make the 3D viewport feel intentional. | 8/10 | 3 |
| Phase 105: Deployment Documentation | Prepare VPS migration instructions. | 4/10 | 1 |
| Phase 106: Domain and DNS Checklist | Prepare domain launch. | 3/10 | 1 |
| Phase 107: VPS Readiness Checklist | Confirm the project is ready to leave the VM nest. | 5/10 | 1 |
| Phase 108: Content Authoring Guide | Prepare creator workflow for adding real content. | 4/10 | 1 |
| Phase 109: Final VM Release Candidate | Freeze the VPS-ready version. | 9/10 | 3 |

## Notes

- Estimates assume the phase checklist must be fully satisfied, including tests/smokes, docs, goldens, hard no's, and regression checks.
- Estimates assume full repo context is available at implementation time.
- If a phase reveals broken prior architecture, missing fixtures, dependency conflicts, or VM instability, add one extra turn rather than cramming scope.
- No phase should be treated as complete without its matching checklist section fully closed.