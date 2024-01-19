import Agent, {
  type Task
} from 'agent-protocol'

export interface Env {
  agents: Agent[];
  metadata: {
    [key: string]: any;
  }
}
