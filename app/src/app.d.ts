// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces.
declare global {
  namespace App {
    // interface Error {}
    interface Locals {
      env: Readonly<{
        databaseUrl: string;
        sessionSecret: string;
        publicSiteName: string;
        mediaRoot: string;
      }>;
    }
    // interface PageData {}
    // interface PageState {}
    // interface Platform {}
  }
}

export {};
