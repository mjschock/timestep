import { spawn, ChildProcess } from 'child_process';
import { getTimestepPaths } from '../utils.js';

/**
 * Wrapper for the A2A client to be used from the React CLI
 */
export class A2AClientWrapper {
  private process: ChildProcess | null = null;

  /**
   * Start an interactive chat session with an agent
   */
  async startChat(options: {
    agentId?: string;
    autoApprove?: boolean;
  } = {}): Promise<{ success: boolean; error?: string }> {
    try {
      const timestepPaths = getTimestepPaths();

      // Build arguments for the a2a_client
      const args = ['src/api/a2a_client.ts'];

      if (options.agentId) {
        args.push('--agentId', options.agentId);
      }

      if (options.autoApprove) {
        args.push('--auto-approve');
      }

      // Check if agents config exists
      const fs = await import('node:fs');
      if (!fs.existsSync(timestepPaths.agentsConfig)) {
        return {
          success: false,
          error: `Agents configuration not found at: ${timestepPaths.agentsConfig}`
        };
      }

      // Start the a2a_client process using tsx (TypeScript runner)
      this.process = spawn('npx', ['tsx', ...args], {
        stdio: 'inherit',
        cwd: process.cwd()
      });

      return new Promise((resolve) => {
        this.process!.on('error', (error) => {
          resolve({
            success: false,
            error: `Failed to start A2A client: ${error.message}`
          });
        });

        this.process!.on('spawn', () => {
          resolve({ success: true });
        });

        this.process!.on('exit', (code) => {
          if (code !== 0) {
            resolve({
              success: false,
              error: `A2A client exited with code ${code}`
            });
          }
        });
      });
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error'
      };
    }
  }

  /**
   * Check if agents are available by trying to load the config
   */
  async getAvailableAgents(): Promise<{ success: boolean; agents?: any[]; error?: string }> {
    try {
      const timestepPaths = getTimestepPaths();
      const fs = await import('node:fs');

      if (!fs.existsSync(timestepPaths.agentsConfig)) {
        return {
          success: false,
          error: `Agents configuration not found at: ${timestepPaths.agentsConfig}`
        };
      }

      const content = fs.readFileSync(timestepPaths.agentsConfig, 'utf8');
      const lines = content.split('\n').filter(line => line.trim());

      const agents = lines.map(line => {
        try {
          return JSON.parse(line);
        } catch {
          return null;
        }
      }).filter(Boolean);

      return { success: true, agents };
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error'
      };
    }
  }

  /**
   * Stop the current chat session
   */
  stop(): void {
    if (this.process) {
      this.process.kill();
      this.process = null;
    }
  }
}