<script>
  import SiteFooter from './SiteFooter.svelte';
  import SiteNav from './SiteNav.svelte';
</script>

<div class="min-h-screen bg-codex-void text-codex-ink">
  <a
    class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-full focus:bg-codex-cyan focus:px-4 focus:py-2 focus:font-black focus:text-codex-void"
    href="#main-content"
  >
    Skip to main content
  </a>

  <div class="flex min-h-screen flex-col">
    <SiteNav />
    <main id="main-content" class="mx-auto w-full max-w-6xl flex-1 px-4 py-10 sm:px-6 lg:px-8">
      <slot />
    </main>
    <SiteFooter />
  </div>
</div>
