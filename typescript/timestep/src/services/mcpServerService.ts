import {McpServer} from '../api/mcpServersApi.js';
import {Repository} from './backing/repository.js';
import {getBuiltinMcpServer} from '../config/defaultMcpServers.js';

/**
 * Service for managing MCP server operations.
 * Handles business logic for MCP server management and delegates persistence to repository.
 */
export class McpServerService {
	constructor(private repository: Repository<McpServer, string>) {}

	/**
	 * List all MCP servers
	 */
	async listMcpServers(): Promise<McpServer[]> {
		return await this.repository.list();
	}

	/**
	 * Get a specific MCP server by ID
	 */
	async getMcpServer(serverId: string): Promise<McpServer | null> {
		return await this.repository.load(serverId);
	}

	/**
	 * Check if an MCP server exists
	 */
	async isMcpServerAvailable(serverId: string): Promise<boolean> {
		return await this.repository.exists(serverId);
	}

	/**
	 * Save an MCP server
	 */
	async saveMcpServer(server: McpServer): Promise<void> {
		await this.repository.save(server);
	}

	/**
	 * Delete an MCP server
	 */
	async deleteMcpServer(serverId: string): Promise<void> {
		await this.repository.delete(serverId);
	}

	/**
	 * Handle MCP server requests - delegates to built-in server or proxies to remote server
	 */
	async handleMcpServerRequest(serverId: string, request: any): Promise<any> {
		const builtinServer = getBuiltinMcpServer();

		if (serverId === builtinServer.id) {
			// Handle built-in MCP server requests
			return await this.handleBuiltinMcpServerRequest(request);
		} else {
			// Proxy to remote MCP server
			return await this.proxyToRemoteMcpServer(serverId, request);
		}
	}

	/**
	 * Handle requests to the built-in MCP server
	 */
	private async handleBuiltinMcpServerRequest(request: any): Promise<any> {
		const {method, params, id} = request;

		switch (method) {
			case 'initialize':
				// Handle MCP initialization request
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						protocolVersion: '2024-11-05',
						capabilities: {
							tools: {},
							resources: {},
							prompts: {},
						},
						serverInfo: {
							name: 'timestep-builtin-mcp-server',
							version: '1.0.0',
						},
					},
				};

			case 'tools/list':
				// Return the original tools from the previous version
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						tools: [
							{
								name: 'get-alerts',
								description: 'Get weather alerts for a US state',
								inputSchema: {
									type: 'object',
									properties: {
										state: {
											type: 'string',
											description: 'Two-letter state code (e.g. CA, NY)',
											minLength: 2,
											maxLength: 2,
										},
									},
									required: ['state'],
								},
							},
							{
								name: 'get-forecast',
								description:
									'Get NWS forecast for latitude/longitude (US only)',
								inputSchema: {
									type: 'object',
									properties: {
										latitude: {
											type: 'number',
											description: 'Latitude of the location',
											minimum: -90,
											maximum: 90,
										},
										longitude: {
											type: 'number',
											description: 'Longitude of the location',
											minimum: -180,
											maximum: 180,
										},
									},
									required: ['latitude', 'longitude'],
								},
							},
							{
								name: 'markdownToPdf',
								description: 'Convert markdown content to PDF using pandoc',
								inputSchema: {
									type: 'object',
									properties: {
										markdownContent: {
											type: 'string',
											description: 'Markdown content to convert to PDF',
										},
										markdownFile: {
											type: 'string',
											description:
												'Path to markdown file to convert (alternative to markdownContent)',
										},
										outputPath: {
											type: 'string',
											description:
												'Output path for the PDF file (default: output.pdf)',
										},
										template: {
											type: 'string',
											description: 'Pandoc template to use for PDF generation',
										},
										variables: {
											type: 'object',
											description: 'Variables to pass to pandoc template',
											additionalProperties: {
												type: 'string',
											},
										},
										additionalArgs: {
											type: 'array',
											items: {
												type: 'string',
											},
											description: 'Additional arguments to pass to pandoc',
										},
									},
								},
							},
							{
								name: 'think',
								description:
									'Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log.',
								inputSchema: {
									type: 'object',
									properties: {
										thought: {
											type: 'string',
											description: 'A thought to think about.',
										},
									},
									required: ['thought'],
								},
							},
						],
					},
				};

			case 'tools/call':
				return await this.handleToolCall(params, id);

			case 'resources/list':
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						resources: [
							{
								uri: 'greeting://{name}',
								name: 'Dynamic Greeting Resource',
								description: 'Get a personalized greeting',
								mimeType: 'text/plain',
							},
						],
					},
				};

			case 'resources/read':
				return await this.handleResourceRead(params, id);

			case 'prompts/list':
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						prompts: [
							{
								name: 'greet_user',
								description: 'Generate a greeting prompt',
								arguments: [
									{
										name: 'name',
										description: 'Name of the person to greet',
										required: true,
									},
									{
										name: 'style',
										description: 'Style of greeting (friendly, formal, casual)',
										required: false,
									},
								],
							},
						],
					},
				};

			case 'prompts/get':
				return await this.handlePromptGet(params, id);

			default:
				return {
					jsonrpc: '2.0',
					id: id,
					error: {
						code: -32601,
						message: `Unsupported method: ${method}`,
					},
				};
		}
	}

	private async handleToolCall(params: any, id: any): Promise<any> {
		const {name, arguments: args} = params || {};

		if (name === 'get-alerts') {
			return await this.handleGetAlerts(args, id);
		}

		if (name === 'get-forecast') {
			return await this.handleGetForecast(args, id);
		}

		if (name === 'markdownToPdf') {
			return await this.handleMarkdownToPdf(args, id);
		}

		if (name === 'think') {
			return await this.handleThink(args, id);
		}

		return {
			jsonrpc: '2.0',
			id: id,
			error: {
				code: -32601,
				message: `Unknown tool: ${name}`,
			},
		};
	}

	private async handleGetAlerts(args: any, id: any): Promise<any> {
		const stateArg = (args?.['state'] as string | undefined) || '';
		const state = stateArg.toUpperCase();
		if (!/^[A-Z]{2}$/.test(state)) {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{
							type: 'text',
							text: 'Invalid state code. Use two letters, e.g., CA or NY.',
						},
					],
				},
			};
		}

		const NWS_API_BASE = 'https://api.weather.gov';
		const USER_AGENT = 'weather-app/1.0';

		const alertsUrl = `${NWS_API_BASE}/alerts/active/area/${state}`;

		try {
			const response = await fetch(alertsUrl, {
				headers: {
					'User-Agent': USER_AGENT,
					Accept: 'application/geo+json',
				},
			});

			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}

			const alertsData = await response.json();
			const features = alertsData.features || [];

			if (features.length === 0) {
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						content: [{type: 'text', text: `No active alerts for ${state}`}],
					},
				};
			}

			const formatAlert = (feature: any) => {
				const props = feature.properties;
				return [
					`Event: ${props.event || 'Unknown'}`,
					`Area: ${props.areaDesc || 'Unknown'}`,
					`Severity: ${props.severity || 'Unknown'}`,
					`Description: ${props.description || 'No description available'}`,
					`Instructions: ${
						props.instruction || 'No specific instructions provided'
					}`,
					'---',
				].join('\n');
			};

			const formattedAlerts = features.map(formatAlert);
			const alertsText = `Active alerts for ${state}:\n\n${formattedAlerts.join(
				'\n',
			)}`;

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [{type: 'text', text: alertsText}],
				},
			};
		} catch (error) {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [{type: 'text', text: 'Failed to retrieve alerts data'}],
				},
			};
		}
	}

	private async handleGetForecast(args: any, id: any): Promise<any> {
		const latitude = Number(args?.['latitude']);
		const longitude = Number(args?.['longitude']);

		if (
			Number.isNaN(latitude) ||
			Number.isNaN(longitude) ||
			latitude < -90 ||
			latitude > 90 ||
			longitude < -180 ||
			longitude > 180
		) {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{
							type: 'text',
							text: 'Invalid coordinates. Provide latitude [-90,90] and longitude [-180,180].',
						},
					],
				},
			};
		}

		const NWS_API_BASE = 'https://api.weather.gov';
		const USER_AGENT = 'weather-app/1.0';

		try {
			const pointsUrl = `${NWS_API_BASE}/points/${latitude.toFixed(
				4,
			)},${longitude.toFixed(4)}`;

			const pointsResponse = await fetch(pointsUrl, {
				headers: {
					'User-Agent': USER_AGENT,
					Accept: 'application/geo+json',
				},
			});

			if (!pointsResponse.ok) {
				throw new Error(`HTTP error! status: ${pointsResponse.status}`);
			}

			const pointsData = await pointsResponse.json();
			const forecastUrl = pointsData.properties?.forecast;

			if (!forecastUrl) {
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						content: [
							{
								type: 'text',
								text: 'Failed to get forecast URL from grid point data',
							},
						],
					},
				};
			}

			const forecastResponse = await fetch(forecastUrl, {
				headers: {
					'User-Agent': USER_AGENT,
					Accept: 'application/geo+json',
				},
			});

			if (!forecastResponse.ok) {
				throw new Error(`HTTP error! status: ${forecastResponse.status}`);
			}

			const forecastData = await forecastResponse.json();
			const periods = forecastData.properties?.periods || [];

			if (periods.length === 0) {
				return {
					jsonrpc: '2.0',
					id: id,
					result: {
						content: [{type: 'text', text: 'No forecast periods available'}],
					},
				};
			}

			const formattedForecast = periods
				.slice(0, 5)
				.map((period: any) =>
					[
						`${period.name || 'Unknown'}:`,
						`Temperature: ${period.temperature ?? 'Unknown'}°${
							period.temperatureUnit || 'F'
						}`,
						`Wind: ${period.windSpeed || 'Unknown'} ${
							period.windDirection || ''
						}`,
						`Forecast: ${
							period.detailedForecast ||
							period.shortForecast ||
							'No forecast available'
						}`,
						'---',
					].join('\n'),
				);

			const forecastText = `Forecast for ${latitude}, ${longitude}:\n\n${formattedForecast.join(
				'\n',
			)}`;

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [{type: 'text', text: forecastText}],
				},
			};
		} catch (error) {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{
							type: 'text',
							text: `Failed to retrieve forecast data for coordinates: ${latitude}, ${longitude}. This location may not be supported by the NWS API (only US locations are supported).`,
						},
					],
				},
			};
		}
	}

	private async handleMarkdownToPdf(args: any, id: any): Promise<any> {
		const markdownContent = args?.['markdownContent'] as string | undefined;
		const markdownFile = args?.['markdownFile'] as string | undefined;
		const outputPath =
			(args?.['outputPath'] as string | undefined) || 'output.pdf';
		const template = args?.['template'] as string | undefined;
		const variables = args?.['variables'] as Record<string, string> | undefined;
		const additionalArgs =
			(args?.['additionalArgs'] as string[] | undefined) || [];

		if (!markdownContent && !markdownFile) {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{
							type: 'text',
							text: 'Either markdownContent or markdownFile must be provided',
						},
					],
				},
			};
		}

		try {
			const {exec} = await import('node:child_process');
			const {promisify} = await import('node:util');
			const fs = await import('node:fs/promises');

			const execAsync = promisify(exec);

			// Build pandoc command
			const cmd = ['pandoc'];
			let tempFile: string | null = null;

			// Input handling
			if (markdownContent) {
				// Write content to temp file
				tempFile = 'temp_markdown.md';
				await fs.writeFile(tempFile, markdownContent, 'utf8');
				cmd.push(tempFile);
			} else if (markdownFile) {
				try {
					await fs.access(markdownFile);
					cmd.push(markdownFile);
				} catch {
					throw new Error(`Markdown file not found: ${markdownFile}`);
				}
			}

			// Output format and file
			cmd.push('-o', outputPath);

			// Template
			if (template) {
				cmd.push('--template', template);
			}

			// Variables
			if (variables) {
				Object.entries(variables).forEach(([key, value]) => {
					cmd.push('-V', `${key}=${value}`);
				});
			}

			// Additional arguments
			cmd.push(...additionalArgs);

			// Default PDF engine and options for better output
			cmd.push(
				'--pdf-engine=xelatex', // Better Unicode support
				'--variable',
				'geometry:margin=1in', // Reasonable margins
				'--variable',
				'fontsize=11pt', // Good readable size
			);

			// Execute pandoc
			console.log(`Running: ${cmd.join(' ')}`);
			await execAsync(cmd.join(' '));

			// Clean up temp file if created
			if (tempFile) {
				try {
					await fs.unlink(tempFile);
				} catch {
					// Ignore cleanup errors
				}
			}

			console.log(`✅ PDF generated successfully: ${outputPath}`);

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{type: 'text', text: `PDF generated successfully: ${outputPath}`},
					],
				},
			};
		} catch (error: any) {
			console.error(`❌ Error: ${error.message}`);
			if (error.stderr) {
				console.error(`Pandoc stderr: ${error.stderr}`);
			}

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [
						{type: 'text', text: `Error generating PDF: ${error.message}`},
					],
				},
			};
		}
	}

	private async handleThink(args: any, id: any): Promise<any> {
		const thought = args?.['thought'] as string | undefined;

		if (!thought || typeof thought !== 'string') {
			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					content: [{type: 'text', text: 'A thought string is required'}],
				},
			};
		}

		// Log the thought (this is the main functionality - append to log)
		console.log(`💭 Think tool: ${thought}`);

		// Return confirmation that the thought was processed
		return {
			jsonrpc: '2.0',
			id: id,
			result: {
				content: [{type: 'text', text: `Thought recorded: ${thought}`}],
			},
		};
	}

	private async handleResourceRead(params: any, id: any): Promise<any> {
		const {uri} = params || {};

		if (uri.startsWith('greeting://')) {
			// Extract name from URI like "greeting://John"
			const name = uri.replace('greeting://', '');

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					contents: [
						{
							uri,
							mimeType: 'text/plain',
							text: `Hello, ${name}!`,
						},
					],
				},
			};
		}

		return {
			jsonrpc: '2.0',
			id: id,
			error: {
				code: -32601,
				message: `Unknown resource: ${uri}`,
			},
		};
	}

	private async handlePromptGet(params: any, id: any): Promise<any> {
		const {name, arguments: args} = params || {};

		if (name === 'greet_user') {
			const userName = args?.['name'] as string;
			const style = (args?.['style'] as string) || 'friendly';

			if (!userName) {
				return {
					jsonrpc: '2.0',
					id: id,
					error: {
						code: -32602,
						message: 'Name parameter is required',
					},
				};
			}

			const styles: Record<string, string> = {
				friendly: 'Please write a warm, friendly greeting',
				formal: 'Please write a formal, professional greeting',
				casual: 'Please write a casual, relaxed greeting',
			};

			const styleText = styles[style] || styles['friendly'];

			return {
				jsonrpc: '2.0',
				id: id,
				result: {
					messages: [
						{
							role: 'user',
							content: {
								type: 'text',
								text: `${styleText} for someone named ${userName}.`,
							},
						},
					],
				},
			};
		}

		return {
			jsonrpc: '2.0',
			id: id,
			error: {
				code: -32601,
				message: `Unknown prompt: ${name}`,
			},
		};
	}

	/**
	 * Proxy requests to remote MCP servers
	 */
	private async proxyToRemoteMcpServer(
		serverId: string,
		request: any,
	): Promise<any> {
		const server = await this.getMcpServer(serverId);

		if (!server || !server.enabled) {
			throw new Error(`MCP server ${serverId} not found or disabled`);
		}

		try {
			const headers: Record<string, string> = {
				'Content-Type': 'application/json',
				Accept: 'application/json, text/event-stream',
			};

			if (server.authToken) {
				headers['Authorization'] = `Bearer ${server.authToken}`;
			}

			const response = await fetch(server.serverUrl, {
				method: 'POST',
				headers,
				body: JSON.stringify(request),
			});

			if (!response.ok) {
				throw new Error(`HTTP ${response.status}: ${response.statusText}`);
			}

			const responseText = await response.text();

			// Check if response is Server-Sent Events (SSE) format
			if (
				responseText.startsWith('event:') ||
				responseText.includes('data: {')
			) {
				// Parse SSE format: extract JSON from data: field
				const lines = responseText.split('\n');
				for (const line of lines) {
					if (line.startsWith('data: ')) {
						const jsonData = line.substring(6); // Remove 'data: ' prefix
						return JSON.parse(jsonData);
					}
				}
				throw new Error('No valid JSON data found in SSE response');
			} else {
				// Regular JSON response
				return JSON.parse(responseText);
			}
		} catch (error) {
			throw new Error(
				`Failed to proxy to MCP server ${serverId}: ${
					error instanceof Error ? error.message : String(error)
				}`,
			);
		}
	}
}
