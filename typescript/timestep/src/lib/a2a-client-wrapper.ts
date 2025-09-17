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
    userInput?: string;
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

      if (options.userInput) {
        args.push('--user-input', options.userInput);
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
   * Get available agents using the API endpoint
   */
  async getAvailableAgents(): Promise<{ success: boolean; agents?: any[]; error?: string }> {
    try {
      const { listAgents } = await import('../api/agentsApi.js');
      const response = await listAgents();
      return { success: true, agents: response.data };
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Failed to load agents'
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