import { error, type Handle } from '@sveltejs/kit';

import { EnvironmentConfigError, getServerEnv } from '$lib/server/env';

export const handle: Handle = async ({ event, resolve }) => {
  try {
    event.locals.env = getServerEnv();
  } catch (caught) {
    if (caught instanceof EnvironmentConfigError) {
      throw error(500, caught.message);
    }
    throw caught;
  }

  return resolve(event);
};
