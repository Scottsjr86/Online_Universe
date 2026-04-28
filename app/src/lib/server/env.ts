import { env as privateEnv } from '$env/dynamic/private';

export type RequiredEnvName = 'DATABASE_URL' | 'SESSION_SECRET' | 'PUBLIC_SITE_NAME' | 'MEDIA_ROOT';

export type ServerEnv = Readonly<{
  databaseUrl: string;
  sessionSecret: string;
  publicSiteName: string;
  mediaRoot: string;
}>;

type EnvSource = Partial<Record<RequiredEnvName, string | undefined>>;

export class EnvironmentConfigError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'EnvironmentConfigError';
  }
}

const REQUIRED_ENV_NAMES: RequiredEnvName[] = [
  'DATABASE_URL',
  'SESSION_SECRET',
  'PUBLIC_SITE_NAME',
  'MEDIA_ROOT',
];

let cachedServerEnv: ServerEnv | null = null;

export function clearServerEnvCacheForTests(): void {
  cachedServerEnv = null;
}

export function getServerEnv(source: EnvSource = privateEnv): ServerEnv {
  if (source === privateEnv && cachedServerEnv) {
    return cachedServerEnv;
  }

  const parsed = validateServerEnv(source);
  if (source === privateEnv) {
    cachedServerEnv = parsed;
  }
  return parsed;
}

export function validateServerEnv(source: EnvSource = privateEnv): ServerEnv {
  const values = readRequiredEnv(source);
  validateDatabaseUrl(values.DATABASE_URL);
  validateSessionSecret(values.SESSION_SECRET);
  validatePublicSiteName(values.PUBLIC_SITE_NAME);
  validateMediaRoot(values.MEDIA_ROOT);

  return Object.freeze({
    databaseUrl: values.DATABASE_URL,
    sessionSecret: values.SESSION_SECRET,
    publicSiteName: values.PUBLIC_SITE_NAME,
    mediaRoot: values.MEDIA_ROOT,
  });
}

function readRequiredEnv(source: EnvSource): Record<RequiredEnvName, string> {
  const missing = REQUIRED_ENV_NAMES.filter((name) => !source[name]?.trim());
  if (missing.length > 0) {
    throw new EnvironmentConfigError(
      `Missing required environment variable${missing.length === 1 ? '' : 's'}: ${missing.join(', ')}`,
    );
  }

  return {
    DATABASE_URL: source.DATABASE_URL?.trim() ?? '',
    SESSION_SECRET: source.SESSION_SECRET?.trim() ?? '',
    PUBLIC_SITE_NAME: source.PUBLIC_SITE_NAME?.trim() ?? '',
    MEDIA_ROOT: source.MEDIA_ROOT?.trim() ?? '',
  };
}

function validateDatabaseUrl(value: string): void {
  let url: URL;
  try {
    url = new URL(value);
  } catch {
    throw new EnvironmentConfigError('DATABASE_URL must be a valid PostgreSQL connection URL.');
  }

  if (!['postgres:', 'postgresql:'].includes(url.protocol)) {
    throw new EnvironmentConfigError('DATABASE_URL must use the postgres:// or postgresql:// protocol.');
  }
  if (!url.hostname) {
    throw new EnvironmentConfigError('DATABASE_URL must include a database host.');
  }
  if (!url.pathname || url.pathname === '/') {
    throw new EnvironmentConfigError('DATABASE_URL must include a database name.');
  }
}

function validateSessionSecret(value: string): void {
  if (value.length < 32) {
    throw new EnvironmentConfigError('SESSION_SECRET must be at least 32 characters long.');
  }
  if (value.includes('replace-with')) {
    throw new EnvironmentConfigError('SESSION_SECRET still contains the example placeholder value.');
  }
}

function validatePublicSiteName(value: string): void {
  if (value.length > 80) {
    throw new EnvironmentConfigError('PUBLIC_SITE_NAME must be 80 characters or fewer.');
  }
}

function validateMediaRoot(value: string): void {
  if (!value.startsWith('/')) {
    throw new EnvironmentConfigError('MEDIA_ROOT must be an absolute filesystem path.');
  }
  if (value.includes('..')) {
    throw new EnvironmentConfigError('MEDIA_ROOT must not contain path traversal segments.');
  }
}
