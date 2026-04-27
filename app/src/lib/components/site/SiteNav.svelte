<script>
  const plannedSections = ['Worlds', 'Characters', 'Artifacts', 'Stories', 'Timeline'];
</script>

<header class="border-b border-white/10 bg-codex-void/80 backdrop-blur-xl">
  <nav
    aria-label="Main navigation"
    class="mx-auto flex w-full max-w-6xl flex-col gap-4 px-4 py-4 sm:px-6 md:flex-row md:items-center md:justify-between lg:px-8"
  >
    <a class="group inline-flex items-center gap-3 text-codex-ink" href="/" aria-label="Multiverse Codex home">
      <span
        aria-hidden="true"
        class="grid size-10 place-items-center rounded-codex border border-codex-cyan/30 bg-codex-panel text-sm font-black text-codex-cyan shadow-codex transition group-hover:border-codex-violet/70"
      >
        MC
      </span>
      <span class="flex flex-col leading-none">
        <span class="text-sm font-black uppercase tracking-[0.22em]">Multiverse</span>
        <span class="mt-1 text-xs font-semibold uppercase tracking-[0.28em] text-codex-mute">Codex</span>
      </span>
    </a>

    <div class="flex flex-wrap items-center gap-2 text-sm font-bold uppercase tracking-[0.14em]">
      <a
        class="rounded-full border border-codex-cyan/40 bg-codex-cyan/10 px-4 py-2 text-codex-cyan shadow-codex"
        href="/"
        aria-current="page"
      >
        Home
      </a>
      {#each plannedSections as section}
        <span
          class="rounded-full border border-white/10 px-4 py-2 text-codex-mute/70"
          aria-disabled="true"
          title="Unlocks in a later phase"
        >
          {section}
        </span>
      {/each}
    </div>
  </nav>
</header>
