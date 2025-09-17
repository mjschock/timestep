/**
 * Example Supabase Edge Function using @timestep-ai/timestep
 *
 * This demonstrates how to use the pre-built Deno Express app in a Supabase Edge Function.
 * Place this file in your Supabase project at: supabase/functions/timestep-server/index.ts
 *
 * To set up this function:
 * 1. deno add npm:@timestep-ai/timestep
 * 2. Copy this code to supabase/functions/timestep-server/index.ts
 * 3. Deploy with: supabase functions deploy timestep-server
 */

import "https://deno.land/x/xhr@0.1.0/mod.ts";
import { denoApp } from 'npm:@timestep-ai/timestep@latest';

// Configure the port from environment or default
const port = parseInt(Deno.env.get("PORT") || "3000");

console.log("🦕 Starting Timestep Server in Supabase Edge Function");
console.log(`🌐 Server will run on port ${port}`);

// Add Supabase-specific middleware to the pre-built Express app
denoApp.use((req, res, next) => {
  // Add any Supabase-specific headers or processing
  res.header("X-Runtime", "Supabase-Edge-Function");
  res.header("X-Deployment-ID", Deno.env.get("DENO_DEPLOYMENT_ID") || "local");
  next();
});

// Add a Supabase-specific health check endpoint
denoApp.get('/supabase-health', (req, res) => {
  res.json({
    status: 'healthy',
    runtime: 'Supabase Edge Function',
    timestamp: new Date().toISOString(),
    denoVersion: Deno.version.deno,
    deploymentId: Deno.env.get("DENO_DEPLOYMENT_ID") || "local",
    region: Deno.env.get("DENO_REGION") || "unknown"
  });
});

// Use the pre-built Express app directly with Deno.serve
// The denoApp already includes all the Timestep endpoints:
// - GET /agents - List agents
// - GET /models - List models
// - GET /tools - List tools
// - GET /traces - List traces
// - GET /chats - List chats
// - GET /settings/* - Settings endpoints
// - /agents/{agentId}/* - Dynamic agent A2A endpoints
// - GET /health - Standard health check
Deno.serve({ port }, denoApp);

console.log("🚀 Timestep Server running in Supabase Edge Function");
console.log("📚 All Timestep endpoints are available:");
console.log("  - GET /health - Standard health check");
console.log("  - GET /supabase-health - Supabase-specific health check");
console.log("  - GET /agents - List agents");
console.log("  - GET /models - List models");
console.log("  - GET /tools - List tools");
console.log("  - GET /traces - List traces");
console.log("  - GET /chats - List chats");
console.log("  - GET /settings/* - Settings endpoints");
console.log("  - /agents/{agentId}/* - Dynamic agent A2A endpoints");