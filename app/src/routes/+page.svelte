<script>
  const signalPillars = [
    {
      title: 'Worlds',
      summary: 'Cosmic domains, kingdoms, realms, planets, ruins, dream layers, and impossible homes.',
    },
    {
      title: 'Characters',
      summary: 'Heroes, monsters, monarchs, rivals, wanderers, and reality-bent legends with room to grow.',
    },
    {
      title: 'Artifacts',
      summary: 'Relics, weapons, books, vessels, machines, curses, keys, and mythic debris with a paper trail.',
    },
  ];

  const featuredWorlds = [
    {
      name: 'Aurelian Rift',
      label: 'placeholder world',
      summary: 'A shattered celestial borderland where floating city-states anchor themselves to dead stars.',
    },
    {
      name: 'Nocturne Archive',
      label: 'placeholder world',
      summary: 'A moonlit library-realm that stores forbidden histories inside living constellations.',
    },
    {
      name: 'Ironroot Expanse',
      label: 'placeholder world',
      summary: 'An ancient forest of metal-barked giants grown around buried engines and old royal crimes.',
    },
  ];

  const featuredCharacters = [
    {
      name: 'Veyra Ash-Marked',
      role: 'rift cartographer',
      summary: 'Maps unstable realities by listening to the static between worlds.',
    },
    {
      name: 'Saint Orbitus',
      role: 'retired moon-saint',
      summary: 'Carries a broken halo that still remembers every oath it failed to keep.',
    },
    {
      name: 'Korrin of the Ninth Gate',
      role: 'doorbreaker prince',
      summary: 'Opens sealed realms with a crown forged from stolen threshold magic.',
    },
  ];
</script>

<svelte:head>
  <title>Multiverse Codex | Worlds, Characters, Stories, and Canon</title>
  <meta
    name="description"
    content="A creator-owned fantasy multiverse codex for worlds, characters, artifacts, factions, stories, timelines, media, and canon relationships."
  />
</svelte:head>

<section aria-labelledby="hero-title" class="overflow-hidden py-8 sm:py-14 lg:py-20">
  <div class="grid items-center gap-10 lg:grid-cols-[1.08fr_0.92fr]">
    <div>
      <p class="mb-4 text-xs font-black uppercase tracking-[0.24em] text-codex-cyan">
        Phase 6 landing signal online
      </p>
      <h1 id="hero-title" class="max-w-4xl text-5xl font-black leading-[0.92] tracking-tight sm:text-6xl lg:text-7xl">
        A living map for a fantasy multiverse that refuses to rot.
      </h1>
      <p class="mt-6 max-w-2xl text-lg leading-8 text-codex-mute sm:text-xl">
        Multiverse Codex is the future home for linked worlds, characters, artifacts,
        factions, stories, timelines, media, and canon rules. This landing page is static
        for now, but the foundation is already humming under the deck plating.
      </p>
      <div class="mt-8 flex flex-col gap-3 sm:flex-row">
        <a
          class="inline-flex items-center justify-center rounded-full bg-codex-cyan px-6 py-3 text-sm font-black uppercase tracking-[0.18em] text-codex-void shadow-codex transition hover:bg-codex-ink focus:outline-none focus:ring-2 focus:ring-codex-cyan focus:ring-offset-2 focus:ring-offset-codex-void"
          href="#codex-preview"
        >
          Enter the codex preview
        </a>
        <a
          class="inline-flex items-center justify-center rounded-full border border-white/15 bg-white/5 px-6 py-3 text-sm font-black uppercase tracking-[0.18em] text-codex-ink transition hover:border-codex-violet/70 hover:bg-codex-violet/10 focus:outline-none focus:ring-2 focus:ring-codex-violet focus:ring-offset-2 focus:ring-offset-codex-void"
          href="#launch-path"
        >
          See the launch path
        </a>
      </div>
    </div>

    <aside
      aria-label="Codex status panel"
      class="rounded-[2rem] border border-codex-cyan/20 bg-codex-panel/70 p-6 shadow-codex backdrop-blur"
    >
      <div class="rounded-[1.5rem] border border-white/10 bg-codex-void/70 p-5">
        <p class="text-xs font-black uppercase tracking-[0.22em] text-codex-violet">
          Current system shape
        </p>
        <dl class="mt-6 grid gap-4">
          <div class="rounded-codex border border-white/10 bg-white/[0.03] p-4">
            <dt class="text-sm font-bold text-codex-mute">Public shell</dt>
            <dd class="mt-1 text-2xl font-black text-codex-cyan">Online</dd>
          </div>
          <div class="rounded-codex border border-white/10 bg-white/[0.03] p-4">
            <dt class="text-sm font-bold text-codex-mute">Landing content</dt>
            <dd class="mt-1 text-2xl font-black text-codex-ink">Static</dd>
          </div>
          <div class="rounded-codex border border-white/10 bg-white/[0.03] p-4">
            <dt class="text-sm font-bold text-codex-mute">Database content</dt>
            <dd class="mt-1 text-2xl font-black text-codex-ember">Future phase</dd>
          </div>
        </dl>
      </div>
    </aside>
  </div>
</section>

<section id="codex-preview" aria-labelledby="preview-title" class="py-12 sm:py-16">
  <div class="max-w-3xl">
    <p class="text-xs font-black uppercase tracking-[0.24em] text-codex-cyan">Universe teaser</p>
    <h2 id="preview-title" class="mt-3 text-3xl font-black tracking-tight sm:text-5xl">
      Built to keep canon sharp while the universe gets wonderfully huge.
    </h2>
    <p class="mt-5 text-lg leading-8 text-codex-mute">
      The codex will eventually connect published lore, private drafts, relationship graphs,
      timelines, images, videos, and story chapters. Phase 6 only proves the public landing
      surface: a polished static page that hints at the system without pretending the later
      machinery already exists.
    </p>
  </div>

  <div class="mt-8 grid gap-4 md:grid-cols-3">
    {#each signalPillars as pillar}
      <article class="rounded-codex border border-white/10 bg-codex-panel/65 p-5 shadow-codex">
        <h3 class="text-xl font-black text-codex-ink">{pillar.title}</h3>
        <p class="mt-3 text-sm leading-6 text-codex-mute">{pillar.summary}</p>
      </article>
    {/each}
  </div>
</section>

<section aria-labelledby="worlds-title" class="py-12 sm:py-16">
  <div class="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
    <div>
      <p class="text-xs font-black uppercase tracking-[0.24em] text-codex-cyan">Featured worlds placeholder</p>
      <h2 id="worlds-title" class="mt-3 text-3xl font-black tracking-tight sm:text-5xl">
        First worlds waiting in the launch bay.
      </h2>
    </div>
    <p class="max-w-xl text-sm leading-6 text-codex-mute">
      These cards are static placeholders. Database-backed world lists begin later, after schema,
      seed data, and public routes exist.
    </p>
  </div>

  <div class="mt-8 grid gap-5 lg:grid-cols-3">
    {#each featuredWorlds as world}
      <article class="group rounded-[1.75rem] border border-white/10 bg-white/[0.04] p-6 shadow-codex transition hover:border-codex-cyan/50 hover:bg-codex-panel/75">
        <p class="text-xs font-black uppercase tracking-[0.2em] text-codex-violet">{world.label}</p>
        <h3 class="mt-4 text-2xl font-black text-codex-ink">{world.name}</h3>
        <p class="mt-4 text-sm leading-7 text-codex-mute">{world.summary}</p>
      </article>
    {/each}
  </div>
</section>

<section aria-labelledby="characters-title" class="py-12 sm:py-16">
  <div class="rounded-[2rem] border border-codex-violet/20 bg-codex-panel/70 p-6 shadow-codex sm:p-8">
    <div class="max-w-3xl">
      <p class="text-xs font-black uppercase tracking-[0.24em] text-codex-cyan">Featured characters placeholder</p>
      <h2 id="characters-title" class="mt-3 text-3xl font-black tracking-tight sm:text-5xl">
        Characters with enough gravity to bend the map.
      </h2>
    </div>

    <div class="mt-8 grid gap-5 md:grid-cols-3">
      {#each featuredCharacters as character}
        <article class="rounded-codex border border-white/10 bg-codex-void/60 p-5">
          <p class="text-xs font-black uppercase tracking-[0.2em] text-codex-ember">{character.role}</p>
          <h3 class="mt-4 text-xl font-black text-codex-ink">{character.name}</h3>
          <p class="mt-3 text-sm leading-6 text-codex-mute">{character.summary}</p>
        </article>
      {/each}
    </div>
  </div>
</section>

<section id="launch-path" aria-labelledby="launch-title" class="py-12 sm:py-16">
  <div class="rounded-[2rem] border border-codex-cyan/20 bg-gradient-to-br from-codex-cyan/15 via-codex-panel/80 to-codex-violet/15 p-8 shadow-codex sm:p-10">
    <p class="text-xs font-black uppercase tracking-[0.24em] text-codex-cyan">Call to action into the codex</p>
    <h2 id="launch-title" class="mt-3 max-w-3xl text-3xl font-black tracking-tight sm:text-5xl">
      The landing beacon is live. Next comes the machinery that makes the codex real.
    </h2>
    <p class="mt-5 max-w-3xl text-lg leading-8 text-codex-mute">
      Phase 7 moves the project into native PostgreSQL foundations. After that, environment
      validation, database connections, schemas, seed data, public pages, admin tools, media,
      search, and the cosmic viewport start locking into place one proven slice at a time.
    </p>
    <a
      class="mt-8 inline-flex items-center justify-center rounded-full bg-codex-ink px-6 py-3 text-sm font-black uppercase tracking-[0.18em] text-codex-void shadow-codex transition hover:bg-codex-cyan focus:outline-none focus:ring-2 focus:ring-codex-ink focus:ring-offset-2 focus:ring-offset-codex-void"
      href="#main-content"
    >
      Back to the top of the codex
    </a>
  </div>
</section>
