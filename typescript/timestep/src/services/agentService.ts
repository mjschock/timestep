import { Agent } from '../api/agentsApi.js';
import { Repository } from './backing/repository.js';

/**
 * Service for managing agent operations.
 * Handles business logic for agent management and delegates persistence to repository.
 */
export class AgentService {
    constructor(private repository: Repository<Agent, string>) {}

    /**
     * List all agents
     */
    async listAgents(): Promise<Agent[]> {
        return await this.repository.list();
    }

    /**
     * Get a specific agent by ID
     */
    async getAgent(agentId: string): Promise<Agent | null> {
        return await this.repository.load(agentId);
    }

    /**
     * Check if an agent is available
     */
    async isAgentAvailable(agentId: string): Promise<boolean> {
        return await this.repository.exists(agentId);
    }

    /**
     * Save an agent
     */
    async saveAgent(agent: Agent): Promise<void> {
        await this.repository.save(agent);
    }

    /**
     * Delete an agent
     */
    async deleteAgent(agentId: string): Promise<void> {
        await this.repository.delete(agentId);
    }
}