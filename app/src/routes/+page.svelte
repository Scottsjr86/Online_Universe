<svelte:head>
  <title>Multiverse Codex</title>
  <meta
    name="description"
    content="A creator-owned fantasy multiverse codex and admin system."
  />
</svelte:head>

<main class="grid min-h-screen place-items-center px-6 py-12">
  <section
    aria-labelledby="welcome-title"
    class="w-full max-w-2xl rounded-codex border border-slate-400/30 bg-codex-panel/75 p-8 shadow-codex backdrop-blur md:p-14"
  >
    <p class="mb-3 text-xs font-bold uppercase tracking-[0.18em] text-codex-cyan">
      Phase 4 styling spine online
    </p>
    <h1 id="welcome-title" class="text-5xl font-black leading-none tracking-tight md:text-7xl">
      Multiverse Codex
    </h1>
    <p class="mt-6 max-w-xl text-base leading-8 text-codex-mute md:text-lg">
      TailwindCSS is now wired into the SvelteKit shell so the next phases can build the
      public frame without smuggling design tokens through component-local styles.
    </p>
  </section>
</main>
