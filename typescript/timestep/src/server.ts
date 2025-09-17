#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Express server with CLI endpoints for both Node.js and Deno
 *
 * This file runs an Express server that works in both environments.
 * It provides CLI endpoints for the React CLI and integrates with the A2A server.
 */

import express from "express";
import { loadAppConfig } from "./utils.js";
import { listModels } from "./api/modelsApi.js";
import { listContexts } from "./api/contextsApi.js";
import { handleListAgents, handleAgentRequest } from "./api/agentsApi.js";
import { listApiKeys } from "./api/settings/apiKeysApi.js";
import { listMcpServers } from "./api/settings/mcpServersApi.js";
import { listModelProviders } from "./api/settings/modelProvidersApi.js";
import { listTraces } from "./api/tracesApi.js";
import { listTools } from "./api/toolsApi.js";
import { TimestepAIAgentExecutor } from "./core/agentExecutor.js";
import { Task } from "@a2a-js/sdk";
import { TaskStore } from "@a2a-js/sdk/server";

// MCP Server imports
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { randomUUID } from "node:crypto";
import { exec } from "node:child_process";
import { promises as fs } from "node:fs";
import { promisify } from "node:util";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// Get app config
const appConfig = loadAppConfig();

// MCP Server constants and helpers
const NWS_API_BASE = "https://api.weather.gov";
const USER_AGENT = "weather-app/1.0";
const execAsync = promisify(exec);

// Helper function for making NWS API requests
async function makeNWSRequest<T>(url: string): Promise<T | null> {
  const headers = {
    "User-Agent": USER_AGENT,
    Accept: "application/geo+json",
  } as Record<string, string>;

  try {
    const response = await fetch(url, { headers });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return (await response.json()) as T;
  } catch (error) {
    console.error("Error making NWS request:", error);
    return null;
  }
}

// Custom task store with detailed logging
class LoggingTaskStore implements TaskStore {
  private store: Map<string, Task> = new Map();

  load(taskId: string): Promise<Task | undefined> {
    console.log(`📋 TaskStore.load(${taskId})`);
    const entry = this.store.get(taskId);
    if (entry) {
      console.log(`📋 TaskStore.load(${taskId}) -> FOUND:`, {
        id: entry.id,
        contextId: entry.contextId,
        kind: entry.kind,
        status: entry.status
      });
      // Return copies to prevent external mutation
      return Promise.resolve({...entry});
    } else {
      console.log(`📋 TaskStore.load(${taskId}) -> NOT FOUND`);
      console.log(`📋 TaskStore current keys:`, Array.from(this.store.keys()));
      return Promise.resolve(undefined);
    }
  }

  save(task: Task): Promise<void> {
    console.log(`📋 TaskStore.save(${task.id})`, {
      id: task.id,
      contextId: task.contextId,
      kind: task.kind,
      status: task.status
    });
    // Store copies to prevent internal mutation if caller reuses objects
    this.store.set(task.id, {...task});
    console.log(`📋 TaskStore.save(${task.id}) -> SAVED`);
    console.log(`📋 TaskStore current keys after save:`, Array.from(this.store.keys()));
    return Promise.resolve();
  }
}

// Create Express app for CLI endpoints and A2A server
const app = express();

// A2A server components
const agentExecutor = new TimestepAIAgentExecutor();
const sharedTaskStore = new LoggingTaskStore();

// MCP server components
const mcpServer = new Server(
  {
    name: "StatefulServer",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
      prompts: {},
    },
  }
);

// Map to store MCP transports by session ID
const mcpTransports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// MCP helper functions and types
interface PandocOptions {
  markdownContent?: string;
  markdownFile?: string;
  outputPath?: string;
  template?: string;
  variables?: Record<string, string>;
  additionalArgs?: string[];
}

interface AlertFeature {
  properties: {
    event?: string;
    areaDesc?: string;
    severity?: string;
    description?: string;
    instruction?: string;
  };
}

interface ForecastPeriod {
  name?: string;
  temperature?: number;
  temperatureUnit?: string;
  windSpeed?: string;
  windDirection?: string;
  shortForecast?: string;
  detailedForecast?: string;
}

interface AlertsResponse {
  features: AlertFeature[];
}

interface PointsResponse {
  properties: {
    forecast?: string;
  };
}

interface ForecastResponse {
  properties: {
    periods: ForecastPeriod[];
  };
}

async function markdownToPdf({
  markdownContent,
  markdownFile,
  outputPath = 'output.pdf',
  template,
  variables,
  additionalArgs = []
}: PandocOptions): Promise<boolean> {
  try {
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
    } else {
      throw new Error('Either markdownContent or markdownFile must be provided');
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
      '--variable', 'geometry:margin=1in', // Reasonable margins
      '--variable', 'fontsize=11pt' // Good readable size
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
    return true;

  } catch (error: any) {
    console.error(`❌ Error: ${error.message}`);
    if (error.stderr) {
      console.error(`Pandoc stderr: ${error.stderr}`);
    }
    return false;
  }
}

function formatAlert(feature: AlertFeature): string {
  const props = feature.properties;
  return [
    `Event: ${props.event || "Unknown"}`,
    `Area: ${props.areaDesc || "Unknown"}`,
    `Severity: ${props.severity || "Unknown"}`,
    `Description: ${props.description || "No description available"}`,
    `Instructions: ${props.instruction || "No specific instructions provided"}`,
    "---",
  ].join("\n");
}

// MCP setup functions
function setupMCPToolHandlers() {
  // List available tools
  mcpServer.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
      tools: [
        {
          name: "get-alerts",
          description: "Get weather alerts for a US state",
          inputSchema: {
            type: "object",
            properties: {
              state: {
                type: "string",
                description: "Two-letter state code (e.g. CA, NY)",
                minLength: 2,
                maxLength: 2,
              },
            },
            required: ["state"],
          },
        } as Tool,
        {
          name: "get-forecast",
          description: "Get NWS forecast for latitude/longitude (US only)",
          inputSchema: {
            type: "object",
            properties: {
              latitude: {
                type: "number",
                description: "Latitude of the location",
                minimum: -90,
                maximum: 90,
              },
              longitude: {
                type: "number",
                description: "Longitude of the location",
                minimum: -180,
                maximum: 180,
              },
            },
            required: ["latitude", "longitude"],
          },
        } as Tool,
        {
          name: "markdownToPdf",
          description: "Convert markdown content to PDF using pandoc",
          inputSchema: {
            type: "object",
            properties: {
              markdownContent: {
                type: "string",
                description: "Markdown content to convert to PDF",
              },
              markdownFile: {
                type: "string",
                description: "Path to markdown file to convert (alternative to markdownContent)",
              },
              outputPath: {
                type: "string",
                description: "Output path for the PDF file (default: output.pdf)",
              },
              template: {
                type: "string",
                description: "Pandoc template to use for PDF generation",
              },
              variables: {
                type: "object",
                description: "Variables to pass to pandoc template",
                additionalProperties: {
                  type: "string",
                },
              },
              additionalArgs: {
                type: "array",
                items: {
                  type: "string",
                },
                description: "Additional arguments to pass to pandoc",
              },
            },
          },
        } as Tool,
        {
          name: "think",
          description: "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log.",
          inputSchema: {
            type: "object",
            properties: {
              thought: {
                type: "string",
                description: "A thought to think about.",
              },
            },
            required: ["thought"],
          },
        } as Tool,
      ],
    };
  });

  // Handle tool calls
  mcpServer.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "get-alerts") {
      const stateArg = (args?.["state"] as string | undefined) || "";
      const state = stateArg.toUpperCase();
      if (!/^[A-Z]{2}$/.test(state)) {
        return {
          content: [
            { type: "text", text: "Invalid state code. Use two letters, e.g., CA or NY." },
          ],
        };
      }

      const alertsUrl = `${NWS_API_BASE}/alerts/active/area/${state}`;
      const alertsData = await makeNWSRequest<AlertsResponse>(alertsUrl);

      if (!alertsData) {
        return {
          content: [
            { type: "text", text: "Failed to retrieve alerts data" },
          ],
        };
      }

      const features = alertsData.features || [];
      if (features.length === 0) {
        return {
          content: [
            { type: "text", text: `No active alerts for ${state}` },
          ],
        };
      }

      const formattedAlerts = features.map(formatAlert);
      const alertsText = `Active alerts for ${state}:\n\n${formattedAlerts.join("\n")}`;
      return { content: [{ type: "text", text: alertsText }] };
    }

    if (name === "get-forecast") {
      const latitude = Number(args?.["latitude"]);
      const longitude = Number(args?.["longitude"]);

      if (
        Number.isNaN(latitude) ||
        Number.isNaN(longitude) ||
        latitude < -90 ||
        latitude > 90 ||
        longitude < -180 ||
        longitude > 180
      ) {
        return {
          content: [
            { type: "text", text: "Invalid coordinates. Provide latitude [-90,90] and longitude [-180,180]." },
          ],
        };
      }

      const pointsUrl = `${NWS_API_BASE}/points/${latitude.toFixed(4)},${longitude.toFixed(4)}`;
      const pointsData = await makeNWSRequest<PointsResponse>(pointsUrl);

      if (!pointsData) {
        return {
          content: [
            { type: "text", text: `Failed to retrieve grid point data for coordinates: ${latitude}, ${longitude}. This location may not be supported by the NWS API (only US locations are supported).` },
          ],
        };
      }

      const forecastUrl = pointsData.properties?.forecast;
      if (!forecastUrl) {
        return { content: [{ type: "text", text: "Failed to get forecast URL from grid point data" }] };
      }

      const forecastData = await makeNWSRequest<ForecastResponse>(forecastUrl);
      if (!forecastData) {
        return { content: [{ type: "text", text: "Failed to retrieve forecast data" }] };
      }

      const periods = forecastData.properties?.periods || [];
      if (periods.length === 0) {
        return { content: [{ type: "text", text: "No forecast periods available" }] };
      }

      const formattedForecast = periods.slice(0, 5).map((period: ForecastPeriod) =>
        [
          `${period.name || "Unknown"}:`,
          `Temperature: ${period.temperature ?? "Unknown"}°${period.temperatureUnit || "F"}`,
          `Wind: ${period.windSpeed || "Unknown"} ${period.windDirection || ""}`,
          `Forecast: ${period.detailedForecast || period.shortForecast || "No forecast available"}`,
          "---",
        ].join("\n")
      );

      const forecastText = `Forecast for ${latitude}, ${longitude}:\n\n${formattedForecast.join("\n")}`;
      return { content: [{ type: "text", text: forecastText }] };
    }

    if (name === "markdownToPdf") {
      const markdownContent = args?.["markdownContent"] as string | undefined;
      const markdownFile = args?.["markdownFile"] as string | undefined;
      const outputPath = (args?.["outputPath"] as string | undefined) || 'output.pdf';
      const template = args?.["template"] as string | undefined;
      const variables = args?.["variables"] as Record<string, string> | undefined;
      const additionalArgs = (args?.["additionalArgs"] as string[] | undefined) || [];

      if (!markdownContent && !markdownFile) {
        return {
          content: [
            { type: "text", text: "Either markdownContent or markdownFile must be provided" },
          ],
        };
      }

      try {
        const success = await markdownToPdf({
          markdownContent,
          markdownFile,
          outputPath,
          template,
          variables,
          additionalArgs,
        });

        if (success) {
          return {
            content: [
              { type: "text", text: `PDF generated successfully: ${outputPath}` },
            ],
          };
        } else {
          return {
            content: [
              { type: "text", text: "Failed to generate PDF. Check server logs for details." },
            ],
          };
        }
      } catch (error: any) {
        return {
          content: [
            { type: "text", text: `Error generating PDF: ${error.message}` },
          ],
        };
      }
    }

    if (name === "think") {
      const thought = args?.["thought"] as string | undefined;

      if (!thought || typeof thought !== 'string') {
        return {
          content: [
            { type: "text", text: "A thought string is required" },
          ],
        };
      }

      // Log the thought (this is the main functionality - append to log)
      console.log(`💭 Think tool: ${thought}`);

      // Return confirmation that the thought was processed
      return {
        content: [
          { type: "text", text: `Thought recorded: ${thought}` },
        ],
      };
    }

    throw new Error(`Unknown tool: ${name}`);
  });
}

function setupMCPResourceHandlers() {
  // List available resources
  mcpServer.setRequestHandler(ListResourcesRequestSchema, async () => {
    return {
      resources: [
        {
          uri: "greeting://{name}",
          name: "Dynamic Greeting Resource",
          description: "Get a personalized greeting",
          mimeType: "text/plain",
        },
      ],
    };
  });

  // Handle resource reads
  mcpServer.setRequestHandler(ReadResourceRequestSchema, async (request) => {
    const { uri } = request.params;

    if (uri.startsWith("greeting://")) {
      // Extract name from URI like "greeting://John"
      const name = uri.replace("greeting://", "");

      return {
        contents: [
          {
            uri,
            mimeType: "text/plain",
            text: `Hello, ${name}!`,
          },
        ],
      };
    }

    throw new Error(`Unknown resource: ${uri}`);
  });
}

function setupMCPPromptHandlers() {
  // List available prompts
  mcpServer.setRequestHandler(ListPromptsRequestSchema, async () => {
    return {
      prompts: [
        {
          name: "greet_user",
          description: "Generate a greeting prompt",
          arguments: [
            {
              name: "name",
              description: "Name of the person to greet",
              required: true,
            },
            {
              name: "style",
              description: "Style of greeting (friendly, formal, casual)",
              required: false,
            },
          ],
        },
      ],
    };
  });

  // Handle prompt requests
  mcpServer.setRequestHandler(GetPromptRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "greet_user") {
      const userName = args?.["name"] as string;
      const style = (args?.["style"] as string) || "friendly";

      if (!userName) {
        throw new Error("Name parameter is required");
      }

      const styles: Record<string, string> = {
        friendly: "Please write a warm, friendly greeting",
        formal: "Please write a formal, professional greeting",
        casual: "Please write a casual, relaxed greeting",
      };

      const styleText = styles[style] || styles["friendly"];

      return {
        messages: [
          {
            role: "user",
            content: {
              type: "text",
              text: `${styleText} for someone named ${userName}.`,
            },
          },
        ],
      };
    }

    throw new Error(`Unknown prompt: ${name}`);
  });
}

// Add CORS middleware
app.use((_req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Mcp-Session-Id");
  res.header("Access-Control-Expose-Headers", "Mcp-Session-Id");

  // Handle OPTIONS requests in middleware
  if (_req.method === 'OPTIONS') {
    res.sendStatus(200);
    return;
  }

  next();
});

// Setup MCP handlers
setupMCPToolHandlers();
setupMCPResourceHandlers();
setupMCPPromptHandlers();

// MCP Routes
// MCP POST endpoint for specific server
app.post('/mcp_servers/:serverId', async (req, res) => {
  const { serverId } = req.params;

  // For now, only support the built-in MCP server
  if (serverId !== '00000000-0000-0000-0000-000000000000') {
    res.status(404).json({
      jsonrpc: '2.0',
      error: {
        code: -32601,
        message: `MCP server ${serverId} not found or not supported`,
      },
      id: null,
    });
    return;
  }

  const sessionId = req.headers['mcp-session-id'] as string | undefined;

  try {
    let transport: StreamableHTTPServerTransport;
    if (sessionId && mcpTransports[sessionId]) {
      // Reuse existing transport
      transport = mcpTransports[sessionId];
    } else {
      // Create new transport
      transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: () => randomUUID(),
        onsessioninitialized: (sessionId) => {
          console.log(`Session initialized with ID: ${sessionId}`);
          mcpTransports[sessionId] = transport;
        }
      });

      // Set up onclose handler to clean up transport when closed
      transport.onclose = () => {
        const sid = transport.sessionId;
        if (sid && mcpTransports[sid]) {
          console.log(`Transport closed for session ${sid}, removing from transports map`);
          delete mcpTransports[sid];
        }
      };

      // Connect the transport to the MCP server
      await mcpServer.connect(transport);
    }

    // Handle the request
    await transport.handleRequest(req, res, req.body);
  } catch (error) {
    console.error('Error handling MCP request:', error);
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: '2.0',
        error: {
          code: -32603,
          message: 'Internal server error',
        },
        id: null,
      });
    }
  }
});

// Handle GET requests for SSE streams
app.get('/mcp_servers/:serverId', async (req, res) => {
  const { serverId } = req.params;

  // For now, only support the built-in MCP server
  if (serverId !== '00000000-0000-0000-0000-000000000000') {
    res.status(404).send('MCP server not found or not supported');
    return;
  }

  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !mcpTransports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }

  const transport = mcpTransports[sessionId];
  await transport.handleRequest(req, res);
});

// Handle DELETE requests for session termination
app.delete('/mcp_servers/:serverId', async (req, res) => {
  const { serverId } = req.params;

  // For now, only support the built-in MCP server
  if (serverId !== '00000000-0000-0000-0000-000000000000') {
    res.status(404).send('MCP server not found or not supported');
    return;
  }

  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !mcpTransports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }

  console.log(`Received session termination request for session ${sessionId}`);

  try {
    const transport = mcpTransports[sessionId];
    await transport.handleRequest(req, res);
  } catch (error) {
    console.error('Error handling session termination:', error);
    if (!res.headersSent) {
      res.status(500).send('Error processing session termination');
    }
  }
});

// Chats endpoint
app.get("/chats", async (_req, res) => {
  try {
    const contextsResponse = await listContexts();
    res.json(contextsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch contexts"
    });
  }
});

// Models endpoint
app.get("/models", async (_req, res) => {
  try {
    const modelsResponse = await listModels();
    res.json(modelsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch models"
    });
  }
});

// Tools endpoint
app.get("/tools", async (_req, res) => {
  try {
    const toolsResponse = await listTools();
    res.json(toolsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch tools"
    });
  }
});

// Traces endpoint
app.get("/traces", async (_req, res) => {
  try {
    const tracesResponse = await listTraces();
    res.json(tracesResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch traces"
    });
  }
});

// API Keys endpoint
app.get("/settings/api-keys", async (_req, res) => {
  try {
    const apiKeysResponse = await listApiKeys();
    res.json(apiKeysResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch API keys"
    });
  }
});

// MCP Servers endpoint
app.get("/settings/mcp-servers", async (_req, res) => {
  try {
    const mcpServersResponse = await listMcpServers();
    res.json(mcpServersResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch MCP servers"
    });
  }
});

// Model Providers endpoint
app.get("/settings/model-providers", async (_req, res) => {
  try {
    const modelProvidersResponse = await listModelProviders();
    res.json(modelProvidersResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch model providers"
    });
  }
});

// A2A Server Routes
// Add debugging middleware
app.use((req, _res, next) => {
  console.log(`🔍 Request received: ${req.method} ${req.path}`);
  next();
});

// Test route first
app.get('/test-agent', (_req, res) => {
  console.log(`🔍 Test route called`);
  res.json({ message: 'Test route working' });
});

// Dynamic agent route handler - use middleware to catch all paths under /agents/:agentId
app.use('/agents/:agentId', async (req, res, next) => {
  console.log(`🔍 A2A route handler called for: ${req.method} ${req.path} (originalUrl: ${req.originalUrl})`);
  await handleAgentRequest(req, res, next, sharedTaskStore, agentExecutor, appConfig.appPort!);
});

// Agents list endpoint - must come after dynamic routes to avoid conflicts
app.get("/agents", handleListAgents);

// Start the unified server
app.listen(appConfig.appPort, () => {
  console.log(`🌐 Unified server running on http://localhost:${appConfig.appPort}`);
  console.log(`📚 CLI endpoints available at http://localhost:${appConfig.appPort}/`);
  console.log(`🤖 A2A agents available at http://localhost:${appConfig.appPort}/agents/{agentId}/`);
  console.log(`🔌 MCP server available at http://localhost:${appConfig.appPort}/mcp_servers/00000000-0000-0000-0000-000000000000`);
  console.log(`📚 Dynamic agent routing enabled - agents loaded on-demand`);
});