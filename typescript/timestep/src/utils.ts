import { homedir } from 'node:os';
import { join } from 'node:path';

function posixify(appName: string): string {
  return appName.toLowerCase().replace(/\s+/g, '-');
}

/**
 * Returns the config folder for the application. The default behavior
 * is to return whatever is most appropriate for the operating system.
 *
 * Based on Python Click's get_app_dir function:
 * https://github.com/pallets/click/blob/2a0e3ba907927ade6951d5732b775f11b54cb766/src/click/utils.py#L449
 *
 * @param appName - the application name. This should be properly capitalized and can contain whitespace.
 * @param roaming - controls if the folder should be roaming or not on Windows. Has no effect otherwise.
 * @param forcePosix - if this is set to true then on any POSIX system the folder will be stored in the home folder with a leading dot instead of the XDG config home or darwin's application support folder.
 */
export function getAppDir(
  appName: string,
  roaming: boolean = true,
  forcePosix: boolean = false
): string {
  const platform = process.platform;

  if (platform === 'win32') {
    const key = roaming ? 'APPDATA' : 'LOCALAPPDATA';
    const folder = process.env[key] || homedir();
    return join(folder, appName);
  }

  if (forcePosix) {
    return join(homedir(), `.${posixify(appName)}`);
  }

  if (platform === 'darwin') {
    return join(homedir(), 'Library', 'Application Support', appName);
  }

  // Unix/Linux
  const xdgConfigHome = process.env.XDG_CONFIG_HOME || join(homedir(), '.config');
  return join(xdgConfigHome, posixify(appName));
}

/**
 * Get configuration paths for the timestep application
 */
export function getTimestepPaths() {
  const configDir = getAppDir('timestep');

  return {
    configDir,
    appConfig: join(configDir, 'app.json'),
    agentsConfig: join(configDir, 'agents.jsonl'),
    modelProviders: join(configDir, 'model_providers.jsonl'),
    mcpServers: join(configDir, 'mcp_servers.jsonl'),
    dataDir: join(configDir, 'data'),
  };
}