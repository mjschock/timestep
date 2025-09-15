#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";
import { randomUUID } from "node:crypto";
import { exec } from "node:child_process";
import { promises as fs } from "node:fs";
import { promisify } from "node:util";
import process from "node:process";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// NWS (National Weather Service) API configuration
const NWS_API_BASE = "https://api.weather.gov";
const USER_AGENT = "weather-app/1.0";

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

const execAsync = promisify(exec);

interface PandocOptions {
  markdownContent?: string;
  markdownFile?: string;
  outputPath?: string;
  template?: string;
  variables?: Record<string, string>;
  additionalArgs?: string[];
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
    const { stdout, stderr } = await execAsync(cmd.join(' '));

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

interface AlertFeature {
  properties: {
    event?: string;
    areaDesc?: string;
    severity?: string;
    description?: string;
    instruction?: string;
  };
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

class StatefulMCPServer {
  private server: Server;
  private app: express.Application;
  private port: number;

  constructor(port: number = 8000) {
    this.port = port;
    this.app = express();
    
    this.server = new Server(
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

    this.setupExpress();
    this.setupToolHandlers();
    this.setupResourceHandlers();
    this.setupPromptHandlers();
  }

  private setupExpress() {
    this.app.use(express.json());
    
    // Simple CORS setup
    this.app.use((req, res, next) => {
      res.header('Access-Control-Allow-Origin', '*');
      res.header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
      res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Mcp-Session-Id');
      res.header('Access-Control-Expose-Headers', 'Mcp-Session-Id');
      
      if (req.method === 'OPTIONS') {
        res.sendStatus(200);
      } else {
        next();
      }
    });

    // Map to store transports by session ID
    const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

    // MCP POST endpoint
    this.app.post('/mcp', async (req, res) => {
      const sessionId = req.headers['mcp-session-id'] as string | undefined;
      
      try {
        let transport: StreamableHTTPServerTransport;
        if (sessionId && transports[sessionId]) {
          // Reuse existing transport
          transport = transports[sessionId];
        } else {
          // Create new transport
          transport = new StreamableHTTPServerTransport({
            sessionIdGenerator: () => randomUUID(),
            onsessioninitialized: (sessionId) => {
              console.log(`Session initialized with ID: ${sessionId}`);
              transports[sessionId] = transport;
            }
          });

          // Set up onclose handler to clean up transport when closed
          transport.onclose = () => {
            const sid = transport.sessionId;
            if (sid && transports[sid]) {
              console.log(`Transport closed for session ${sid}, removing from transports map`);
              delete transports[sid];
            }
          };

          // Connect the transport to the MCP server
          await this.server.connect(transport);
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
    this.app.get('/mcp', async (req, res) => {
      const sessionId = req.headers['mcp-session-id'] as string | undefined;
      if (!sessionId || !transports[sessionId]) {
        res.status(400).send('Invalid or missing session ID');
        return;
      }

      const transport = transports[sessionId];
      await transport.handleRequest(req, res);
    });

    // Handle DELETE requests for session termination
    this.app.delete('/mcp', async (req, res) => {
      const sessionId = req.headers['mcp-session-id'] as string | undefined;
      if (!sessionId || !transports[sessionId]) {
        res.status(400).send('Invalid or missing session ID');
        return;
      }

      console.log(`Received session termination request for session ${sessionId}`);

      try {
        const transport = transports[sessionId];
        await transport.handleRequest(req, res);
      } catch (error) {
        console.error('Error handling session termination:', error);
        if (!res.headersSent) {
          res.status(500).send('Error processing session termination');
        }
      }
    });
  }

  private setupToolHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
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
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      if (name === "get-alerts") {
        const stateArg = (args?.state as string | undefined) || "";
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
        const latitude = Number(args?.latitude);
        const longitude = Number(args?.longitude);

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
        const markdownContent = args?.markdownContent as string | undefined;
        const markdownFile = args?.markdownFile as string | undefined;
        const outputPath = (args?.outputPath as string | undefined) || 'output.pdf';
        const template = args?.template as string | undefined;
        const variables = args?.variables as Record<string, string> | undefined;
        const additionalArgs = (args?.additionalArgs as string[] | undefined) || [];

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
        const thought = args?.thought as string | undefined;
        
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

  private setupResourceHandlers() {
    // List available resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
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
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
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

  private setupPromptHandlers() {
    // List available prompts
    this.server.setRequestHandler(ListPromptsRequestSchema, async () => {
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
    this.server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      if (name === "greet_user") {
        const userName = args?.name as string;
        const style = (args?.style as string) || "friendly";

        if (!userName) {
          throw new Error("Name parameter is required");
        }

        const styles: Record<string, string> = {
          friendly: "Please write a warm, friendly greeting",
          formal: "Please write a formal, professional greeting",
          casual: "Please write a casual, relaxed greeting",
        };

        const styleText = styles[style] || styles.friendly;

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

  async run() {
    return new Promise<void>((resolve, reject) => {
      this.app.listen(this.port, (error?: Error) => {
        if (error) {
          console.error('Failed to start server:', error);
          reject(error);
        } else {
          console.log(`StatefulServer running on port ${this.port}`);
          resolve();
        }
      });
    });
  }
}

// Start the server if this file is run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  const server = new StatefulMCPServer();
  server.run().catch((error) => {
    console.error("Server error:", error);
    process.exit(1);
  });

  // Handle server shutdown
  process.on('SIGINT', async () => {
    console.log('Shutting down server...');
    process.exit(0);
  });
}

export { StatefulMCPServer };
