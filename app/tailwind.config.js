/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        codex: {
          void: '#050711',
          panel: '#0f172a',
          ink: '#f8fafc',
          mute: '#cbd5e1',
          cyan: '#67e8f9',
          violet: '#a78bfa',
          ember: '#f97316'
        }
      },
      borderRadius: {
        codex: '1.5rem'
      },
      boxShadow: {
        codex: '0 1.5rem 4rem rgba(2, 6, 23, 0.38)'
      }
    }
  }
};
