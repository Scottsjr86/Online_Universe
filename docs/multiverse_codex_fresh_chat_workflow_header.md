# Multiverse Codex Fresh-Chat Patch Workflow Header

Use this header at the top of a fresh chat to define the workflow for Multiverse Codex patch work.

This header is an instruction contract for the assistant.

The user will upload a current repository tar for each patch cycle. The newest uploaded tar is always the authoritative base.

---

# Mission

You are helping build the Multiverse Codex project through small, verified, phase-aligned patches.

Each patch must:

- use only the latest uploaded tar as the base
- ignore all prior extracted repos and stale working directories
- inspect the repo before deciding what to do
- verify docs against code instead of trusting docs blindly
- choose the next logical slice from the project plan/checklist/laws
- implement only that slice
- update progress, closure, spec, and golden docs
- generate a downloadable unified git diff patch
- verify that patch with `git apply --check`
- never print inline diffs unless explicitly requested

No phase is complete until the checklist is complete and the described behavior is fully operational.

No work required by the current phase may be deferred to a later phase.

---

# Authoritative Base Law

The latest uploaded tar is the only authoritative base.

For every patch cycle:

```txt
1. Ignore all previous extractions.
2. Delete/nuke prior temp work directories.
3. Extract the newest uploaded tar fresh.
4. Create a temporary git repo from that extraction.
5. Commit the untouched extracted base as the baseline.
6. Make all changes against that baseline only.
```

Never patch against memory.

Never patch against a prior extraction.

Never patch against a stale repo copy.

Never assume previous generated files exist unless they exist inside the newest uploaded tar.

---

# Required Start Procedure

When the user uploads a fresh current tar and asks for a patch:

```txt
1. Extract the newest tar into a clean temp work directory.
2. Extract the same tar into a second clean temp check directory.
3. Find the repo root in both extractions.
4. Initialize a git repo in the work extraction.
5. Commit the untouched work extraction as baseline.
6. Initialize a git repo in the check extraction.
7. Commit the untouched check extraction as baseline.
8. Read the required repo docs.
9. Audit docs against code.
10. Choose the next logical slice.
11. Implement the slice.
12. Update required docs.
13. Generate a unified git diff patch from the work repo.
14. Run `git apply --check` against the clean check repo.
15. Deliver the patch artifact only if verification passes.
```

---

# Required Docs to Read Before Work

Before choosing any implementation slice, read:

```txt
docs/progress.json
docs/specs/
docs/closures/
docs/multiverse_codex_phase_plan.md
docs/multiverse_codex_phase_completion_checklist.md
docs/multiverse_codex_architecture_laws.md
```

If one of these files is missing:

```txt
1. Inspect nearby docs for a renamed equivalent.
2. If a clear replacement exists, use it and document the assumption.
3. If no replacement exists and the missing file is required for safe progress, patch the missing project-control doc first.
4. Do not silently invent progress.
5. Do not advance to implementation while blind.
```

---

# Progress State Law

`docs/progress.json` is the machine-readable build state.

It should identify, at minimum:

```txt
current_phase
current_phase_title
phase_status
last_completed_phase
next_candidate_phase
last_patch_id
updated_at
```

If the repo uses an established alternate file such as:

```txt
docs/progress.jsonl
docs/changelog.jsonl
docs/build_log.jsonl
docs/roadmap.jsonl
```

then preserve the existing convention unless the current patch explicitly migrates it.

Do not create a second progress system if one already exists.

---

# Append-Only Step Log Law

Every patch must add a brief append-only progress entry.

Preferred file:

```txt
docs/progress.jsonl
```

Acceptable alternate names if already established:

```txt
docs/changelog.jsonl
docs/build_log.jsonl
docs/roadmap.jsonl
```

Each entry should record:

```json
{
  "timestamp": "ISO-8601 timestamp",
  "patch_id": "phase-###-short-name",
  "phase": 0,
  "slice": "short description",
  "status": "complete",
  "summary": "brief explanation of what changed",
  "files_changed": [],
  "tests": [],
  "golden": "docs/goldens/phase-###.md",
  "closure": "docs/closures/phase-###-closure.md",
  "spec": "docs/specs/phase-###-spec.md"
}
```

The log is the roadmap of every step.

No patch ships without a progress/log entry.

---

# Closure and Spec Law

Every completed phase must have:

```txt
docs/closures/phase-###-closure.md
docs/specs/phase-###-spec.md
```

## Closure File

The closure file records what was actually completed.

It must include:

```txt
phase number and title
scope completed
checklist status
behavior proven
commands/tests run
files changed
known limitations
confirmation that no work is deferred
confirmation that architecture laws were checked
```

No closure file may overstate completion.

If behavior is not operational, the phase is not closed.

## Spec File

The spec file records what was built and how future work should hand off from it.

It must include:

```txt
phase number and title
implemented behavior
public/admin routes touched
domain modules touched
data models touched
guards/seams added
tests/smokes added
handoff notes for next phase
```

Spec files are not wishlists.

They describe implementation reality.

---

# Truth Audit Law

Before choosing the next slice, compare docs against code.

Required checks:

```txt
1. Read latest closure docs.
2. Read latest specs.
3. Read progress state.
4. Inspect relevant code/modules/routes/tests.
5. Verify claimed behavior exists.
6. Verify claimed tests/smokes exist or are recorded.
7. Verify architecture laws were not violated.
8. Verify no phase is overstated as complete.
```

If docs claim something is complete but code proves otherwise:

```txt
1. Treat the docs as suspect.
2. Do not advance blindly.
3. Patch the truth gap first if needed.
4. Update progress/closure/spec docs honestly.
```

Docs do not outrank reality.

The code and passing checks are ground truth.

---

# Next Slice Selection Law

After the truth audit, choose the next logical slice by reading:

```txt
docs/progress.json
latest docs/closures/*
latest docs/specs/*
docs/multiverse_codex_phase_plan.md
docs/multiverse_codex_phase_completion_checklist.md
docs/multiverse_codex_architecture_laws.md
actual repo state
```

The next slice must be:

```txt
single-purpose
phase-aligned
small enough to complete correctly
large enough to move the build forward
fully testable
fully closeable
```

Do not mash objectives together.

Do not skip ahead because a later phase is more interesting.

Do not start polish before foundations are real.

Do not start a new phase if the previous phase is not truthfully closed.

---

# No Deferred Work Law

No work may be deferred to the next phase if it is required for the current phase checklist.

Forbidden closure language:

```txt
will do later
left for next phase
temporary stub
placeholder for now
not wired yet
manual verification only when automated check is required
TODO before completion
FIXME before completion
```

Allowed only when explicitly outside the current phase:

```txt
out of scope for this phase
future phase item
not required by current checklist
```

Even then, closure must make clear that the current phase is fully operational within its defined scope.

---

# Architecture Law Enforcement

Every patch must obey:

```txt
docs/multiverse_codex_architecture_laws.md
```

Especially:

```txt
modules should stay below 1,000 LOC
logic/layout must be split
hard seams must be guarded
route files must stay thin
services own behavior
repositories own persistence
components own appearance
media/auth/database/3D/ops boundaries must be explicit
```

Before closing a patch, check for:

```txt
oversized files
logic/layout mixing
unguarded trust boundaries
client-only security
manual-only database changes
unchecked media paths
missing tests
missing golden
missing closure
missing spec
missing progress entry
```

Any violation blocks closure.

---

# Patch Generation Law

Every implementation patch must be generated from the temporary git repo.

Required process from the work repo:

```bash
git status --short
git diff -- . > /mnt/data/<patch_name>.patch
```

The patch must be a unified git diff.

Prefer downloadable patch files.

Do not print inline diffs unless explicitly requested.

Patch names should be descriptive:

```txt
phase_000_workstation_bootstrap.patch
phase_001_repo_skeleton.patch
phase_007_native_postgres_foundation.patch
```

---

# Patch Verification Law

Every patch must be checked before delivery.

Verification process:

```txt
1. Use the second clean extraction of the same uploaded tar.
2. Initialize and baseline commit if not already done.
3. Run `git apply --check` against the generated patch.
4. Only deliver the patch if `git apply --check` passes.
```

Required command:

```bash
git apply --check /mnt/data/<patch_name>.patch
```

If `git apply --check` fails:

```txt
1. Do not deliver the broken patch.
2. Fix the patch.
3. Re-run `git apply --check`.
4. Deliver only after it passes.
```

---

# Testing and Smoke Law

Run the tests/smokes required by the current phase checklist.

Minimum expected checks may include:

```txt
git diff --check
lint
typecheck
unit tests
database migration check
route smoke
browser smoke
upload smoke
backup/restore smoke
VM smoke
```

Use the current phase checklist to determine what must pass.

If a test cannot run due to environment limitations, document that honestly in the closure and do not overstate completion.

If the test is required for phase completion and cannot be run, the phase is not complete.

---

# Golden Law

Every phase must create/update:

```txt
docs/goldens/phase-###.md
```

Golden must include:

```txt
phase number and title
scope completed
files changed
commands run
test/smoke output summary
screenshots/log snippets/schema snapshots where useful
known limitations
final commit hash if available
hard no review
```

No golden, no closure.

---

# Latest Tar Reset Procedure

For every new uploaded tar:

```bash
rm -rf /tmp/multiverse-codex-work
rm -rf /tmp/multiverse-codex-check

mkdir -p /tmp/multiverse-codex-work
mkdir -p /tmp/multiverse-codex-check

tar -xf /mnt/data/<latest_tar>.tar -C /tmp/multiverse-codex-work
tar -xf /mnt/data/<latest_tar>.tar -C /tmp/multiverse-codex-check
```

Find the repo root in both extractions.

Initialize the work base:

```bash
cd /tmp/multiverse-codex-work/<repo-root>
git init
git add .
git commit -m "baseline from latest tar"
```

Initialize the check base:

```bash
cd /tmp/multiverse-codex-check/<repo-root>
git init
git add .
git commit -m "baseline from latest tar"
```

After implementing in the work repo:

```bash
cd /tmp/multiverse-codex-work/<repo-root>
git diff -- . > /mnt/data/<patch_name>.patch
```

Verify in the check repo:

```bash
cd /tmp/multiverse-codex-check/<repo-root>
git apply --check /mnt/data/<patch_name>.patch
```

Only send the patch if verification passes.

---

# Phase Completion Definition

A phase is complete only when:

```txt
the implementation exists
the behavior is operational
the checklist is satisfied
tests/smokes pass
golden is created/updated
closure is created/updated
spec is created/updated
progress/log entry is appended
architecture laws are satisfied
git apply --check passes for the patch
no work is deferred
```

If any item is missing, the phase is not done.

---

# Patch Response Format

When delivering a patch, respond with:

```txt
- brief summary of what changed
- tests/smokes run
- git apply --check result
- downloadable patch link
- any honest limitations
```

Do not paste the full diff inline unless requested.

Preferred final response:

```txt
Done.

Changed:
- ...

Verified:
- git apply --check passed
- ...

Patch:
[Download patch](sandbox:/mnt/data/<patch_name>.patch)
```

---

# Failure Handling

If the repo state blocks safe progress:

```txt
1. Do not guess.
2. Do not fabricate completion.
3. Report the blocker clearly.
4. Patch the blocker first if it is the next logical slice.
5. Otherwise provide a truthful partial result.
```

Examples of blockers:

```txt
missing docs/progress.json
missing phase plan/checklist/laws
closures contradict code
specs overstate completion
tests cannot run
repo cannot build
tar has unexpected nesting
patch cannot apply cleanly
required phase scope is too large for one safe patch
```

---

# Final Commandment

The newest tar is the map.

The code is the terrain.

The docs are sworn testimony.

The tests are the lie detector.

The patch is the artifact.

The golden is the receipt.

No phase advances on hope.
