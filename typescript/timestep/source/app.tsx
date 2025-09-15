import React, {useState, useEffect} from 'react';
import {Text, Box} from 'ink';
import {spawn} from 'child_process';

type Props = {
	name: string | undefined;
	command?: string;
};

type Agent = {
	id: string;
	name: string;
	instructions: string;
	handoffIds?: string[];
	handoffDescription?: string;
	toolIds: string[];
	model: string;
	modelSettings: {
		temperature: number;
	};
};

type Chat = {
	id: string;
	title: string;
	participants: string[];
	lastMessage: string;
	timestamp: string;
};

type Model = {
	id: string;
	name: string;
	provider: string;
	type: string;
	status: string;
	capabilities: string[];
	maxTokens: number;
	cost: number;
};

type Tool = {
	id: string;
	name: string;
	category: string;
	description: string;
	status: string;
	usage: number;
	lastUsed: string;
};

type Trace = {
	id: string;
	sessionId: string;
	agentId: string;
	action: string;
	input: string;
	output: string;
	duration: number;
	timestamp: string;
	status: string;
};

export default function App({name = 'Stranger', command}: Props) {
	const [agents, setAgents] = useState<Agent[]>([]);
	const [chats, setChats] = useState<Chat[]>([]);
	const [models, setModels] = useState<Model[]>([]);
	const [tools, setTools] = useState<Tool[]>([]);
	const [traces, setTraces] = useState<Trace[]>([]);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState<string | null>(null);
	const [serverStarted, setServerStarted] = useState(false);

	useEffect(() => {
		if (command === 'list-agents') {
			fetchAgents();
		} else if (command === 'list-chats') {
			fetchChats();
		} else if (command === 'list-models') {
			fetchModels();
		} else if (command === 'list-tools') {
			fetchTools();
		} else if (command === 'list-traces') {
			fetchTraces();
		} else if (command === 'server') {
			startServer();
		}
	}, [command]);

	const startServer = () => {
		try {
			// Check if Deno is available
			const denoCheck = spawn('deno', ['--version'], { stdio: 'pipe' });
			
			denoCheck.on('error', () => {
				setError('Deno is not installed. Please install Deno from https://deno.land/');
			});
			
			denoCheck.on('close', (code) => {
				if (code === 0) {
					// Start the server
					const server = spawn('deno', ['run', '--allow-net', 'server.ts'], {
						stdio: 'inherit',
						detached: true
					});
					
					server.unref(); // Allow the parent process to exit
					setServerStarted(true);
				} else {
					setError('Deno is not installed. Please install Deno from https://deno.land/');
				}
			});
		} catch (err) {
			setError('Failed to start server');
		}
	};

	const fetchAgents = async () => {
		setLoading(true);
		setError(null);
		
		try {
			const response = await fetch('http://localhost:8000/agents');
			if (!response.ok) {
				throw new Error(`Server responded with ${response.status}`);
			}
			const data = await response.json();
			setAgents(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : 'Failed to fetch agents');
		} finally {
			setLoading(false);
		}
	};

	const fetchChats = async () => {
		setLoading(true);
		setError(null);
		
		try {
			const response = await fetch('http://localhost:8000/chats');
			if (!response.ok) {
				throw new Error(`Server responded with ${response.status}`);
			}
			const data = await response.json();
			setChats(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : 'Failed to fetch chats');
		} finally {
			setLoading(false);
		}
	};

	const fetchModels = async () => {
		setLoading(true);
		setError(null);
		
		try {
			const response = await fetch('http://localhost:8000/models');
			if (!response.ok) {
				throw new Error(`Server responded with ${response.status}`);
			}
			const data = await response.json();
			setModels(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : 'Failed to fetch models');
		} finally {
			setLoading(false);
		}
	};

	const fetchTools = async () => {
		setLoading(true);
		setError(null);
		
		try {
			const response = await fetch('http://localhost:8000/tools');
			if (!response.ok) {
				throw new Error(`Server responded with ${response.status}`);
			}
			const data = await response.json();
			setTools(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : 'Failed to fetch tools');
		} finally {
			setLoading(false);
		}
	};

	const fetchTraces = async () => {
		setLoading(true);
		setError(null);
		
		try {
			const response = await fetch('http://localhost:8000/traces');
			if (!response.ok) {
				throw new Error(`Server responded with ${response.status}`);
			}
			const data = await response.json();
			setTraces(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : 'Failed to fetch traces');
		} finally {
			setLoading(false);
		}
	};

	if (command === 'server') {
		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
				</Box>
			);
		}
		
		if (serverStarted) {
			return (
				<Box flexDirection="column">
					<Text color="green">✅ Timestep Agents Server started!</Text>
					<Text>Server is available at: http://localhost:8000</Text>
					<Text>Agents endpoint: http://localhost:8000/agents</Text>
					<Text color="blue">Use 'timestep list-agents' to fetch agents</Text>
				</Box>
			);
		}
		
		return (
			<Box flexDirection="column">
				<Text color="green">🚀 Starting Timestep Agents Server...</Text>
				<Text>Checking for Deno...</Text>
			</Box>
		);
	}

	if (command === 'list-agents') {
		if (loading) {
			return <Text color="blue">Loading agents...</Text>;
		}

		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
					<Text color="yellow">Make sure the server is running with: timestep server</Text>
				</Box>
			);
		}

		return (
			<Box flexDirection="column">
				<Text color="green">🤖 Available Agents:</Text>
				{agents.map((agent) => (
					<Box key={agent.id} flexDirection="column" marginLeft={2}>
						<Text>
							<Text color="blue">•</Text> <Text color="cyan">{agent.name}</Text>
							<Text color="gray"> (ID: {agent.id.slice(0, 8)}...)</Text>
						</Text>
						<Box marginLeft={2}>
							<Text color="gray">
								Model: {agent.model} | Temperature: {agent.modelSettings.temperature}
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Tools: {agent.toolIds.length} available
							</Text>
						</Box>
						{agent.handoffDescription && (
							<Box marginLeft={2}>
								<Text color="gray">
									{agent.handoffDescription}
								</Text>
							</Box>
						)}
						{agent.handoffIds && agent.handoffIds.length > 0 && (
							<Box marginLeft={2}>
								<Text color="gray">
									Can handoff to: {agent.handoffIds.length} other agents
								</Text>
							</Box>
						)}
					</Box>
				))}
			</Box>
		);
	}

	if (command === 'list-chats') {
		if (loading) {
			return <Text color="blue">Loading chats...</Text>;
		}

		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
					<Text color="yellow">Make sure the server is running with: timestep server</Text>
				</Box>
			);
		}

		return (
			<Box flexDirection="column">
				<Text color="green">💬 Available Chats:</Text>
				{chats.map((chat) => (
					<Box key={chat.id} flexDirection="column" marginLeft={2}>
						<Text>
							<Text color="blue">•</Text> <Text color="cyan">{chat.title}</Text>
						</Text>
						<Box marginLeft={2}>
							<Text color="gray">
								Participants: {chat.participants.join(', ')}
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Last message: "{chat.lastMessage}"
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Time: {new Date(chat.timestamp).toLocaleString()}
							</Text>
						</Box>
					</Box>
				))}
			</Box>
		);
	}

	if (command === 'list-models') {
		if (loading) {
			return <Text color="blue">Loading models...</Text>;
		}

		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
					<Text color="yellow">Make sure the server is running with: timestep server</Text>
				</Box>
			);
		}

		return (
			<Box flexDirection="column">
				<Text color="green">🤖 Available Models:</Text>
				{models.map((model) => (
					<Box key={model.id} flexDirection="column" marginLeft={2}>
						<Text>
							<Text color="blue">•</Text> <Text color="cyan">{model.name}</Text>
							<Text color="gray"> ({model.provider})</Text>
						</Text>
						<Box marginLeft={2}>
							<Text color="gray">
								Type: {model.type} | Status: <Text color={model.status === 'active' ? 'green' : 'yellow'}>{model.status}</Text>
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Capabilities: {model.capabilities.join(', ')}
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Max Tokens: {model.maxTokens.toLocaleString()} | Cost: ${model.cost}/1K tokens
							</Text>
						</Box>
					</Box>
				))}
			</Box>
		);
	}

	if (command === 'list-tools') {
		if (loading) {
			return <Text color="blue">Loading tools...</Text>;
		}

		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
					<Text color="yellow">Make sure the server is running with: timestep server</Text>
				</Box>
			);
		}

		return (
			<Box flexDirection="column">
				<Text color="green">🔧 Available Tools:</Text>
				{tools.map((tool) => (
					<Box key={tool.id} flexDirection="column" marginLeft={2}>
						<Text>
							<Text color="blue">•</Text> <Text color="cyan">{tool.name}</Text>
							<Text color="gray"> ({tool.category})</Text>
						</Text>
						<Box marginLeft={2}>
							<Text color="gray">
								{tool.description}
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Status: <Text color={tool.status === 'active' ? 'green' : 'yellow'}>{tool.status}</Text> | 
								Usage: {tool.usage.toLocaleString()} times | 
								Last used: {new Date(tool.lastUsed).toLocaleString()}
							</Text>
						</Box>
					</Box>
				))}
			</Box>
		);
	}

	if (command === 'list-traces') {
		if (loading) {
			return <Text color="blue">Loading traces...</Text>;
		}

		if (error) {
			return (
				<Box flexDirection="column">
					<Text color="red">❌ Error: {error}</Text>
					<Text color="yellow">Make sure the server is running with: timestep server</Text>
				</Box>
			);
		}

		return (
			<Box flexDirection="column">
				<Text color="green">📊 Recent Traces:</Text>
				{traces.map((trace) => (
					<Box key={trace.id} flexDirection="column" marginLeft={2}>
						<Text>
							<Text color="blue">•</Text> <Text color="cyan">{trace.action}</Text>
							<Text color="gray"> (Agent {trace.agentId}, Session {trace.sessionId})</Text>
						</Text>
						<Box marginLeft={2}>
							<Text color="gray">
								Input: "{trace.input}"
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Output: "{trace.output}"
							</Text>
						</Box>
						<Box marginLeft={2}>
							<Text color="gray">
								Status: <Text color={trace.status === 'completed' ? 'green' : 'red'}>{trace.status}</Text> | 
								Duration: {trace.duration}s | 
								Time: {new Date(trace.timestamp).toLocaleString()}
							</Text>
						</Box>
					</Box>
				))}
			</Box>
		);
	}

	// Default greeting
	return (
		<Text>
			Hello, <Text color="green">{name}</Text>
		</Text>
	);
}
