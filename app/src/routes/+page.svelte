<svelte:head>
  <title>Multiverse Codex</title>
  <meta
    name="description"
    content="A creator-owned fantasy multiverse codex and admin system."
  />
</svelte:head>

<main>
  <section aria-labelledby="welcome-title">
    <p>Phase 3 scaffold online</p>
    <h1 id="welcome-title">Multiverse Codex</h1>
    <p>
      The SvelteKit shell is ready for the cosmic machinery that starts landing in
      the next phases.
    </p>
  </section>
</main>

<style>
  :global(body) {
    margin: 0;
    min-width: 320px;
    min-height: 100vh;
    color: #f5f7fb;
    background:
      radial-gradient(circle at top left, rgba(110, 231, 255, 0.18), transparent 32rem),
      linear-gradient(135deg, #070914 0%, #111827 48%, #020617 100%);
    font-family:
      Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
      sans-serif;
  }

  main {
    display: grid;
    min-height: 100vh;
    place-items: center;
    padding: 2rem;
  }

  section {
    max-width: 42rem;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 1.5rem;
    padding: clamp(2rem, 6vw, 4rem);
    background: rgba(15, 23, 42, 0.72);
    box-shadow: 0 1.5rem 4rem rgba(2, 6, 23, 0.38);
  }

  p:first-child {
    margin: 0 0 0.75rem;
    color: #67e8f9;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }

  h1 {
    margin: 0;
    font-size: clamp(2.5rem, 9vw, 5.5rem);
    line-height: 0.95;
  }

  p:last-child {
    margin: 1.25rem 0 0;
    color: #cbd5e1;
    font-size: clamp(1rem, 2vw, 1.2rem);
    line-height: 1.7;
  }
</style>
