#!/usr/bin/env -S deno run --allow-read --allow-net
/**
 * Example Syntax Checker
 *
 * This script checks the syntax of our Supabase Edge Function examples
 * using our local build instead of the published NPM package.
 */

import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Function to replace npm imports with local imports
function replaceImportsWithLocal(content: string): string {
  return content.replace(
    /from 'npm:@timestep-ai\/timestep@[^']*'/g,
    "from '../src/index.ts'"
  );
}

async function checkExample(filename: string) {
  console.log(`🔍 Checking ${filename}...`);

  const examplePath = join(__dirname, filename);
  const originalContent = readFileSync(examplePath, 'utf-8');

  // Replace npm imports with local imports
  const modifiedContent = replaceImportsWithLocal(originalContent);

  // Write temporary file with local imports
  const tempFilename = filename.replace('.ts', '.local.ts');
  const tempPath = join(__dirname, tempFilename);

  try {
    await Deno.writeTextFile(tempPath, modifiedContent);

    // Run Deno check on the modified file with sloppy imports
    const cmd = new Deno.Command("deno", {
      args: ["check", "--sloppy-imports", tempPath],
      stdout: "piped",
      stderr: "piped",
    });

    const result = await cmd.output();

    if (result.code === 0) {
      console.log(`✅ ${filename} - Syntax OK`);
    } else {
      console.log(`❌ ${filename} - Syntax errors found:`);
      console.log(new TextDecoder().decode(result.stderr));
    }

    // Clean up temporary file
    await Deno.remove(tempPath);

    return result.code === 0;

  } catch (error) {
    console.error(`Error checking ${filename}:`, error);
    // Clean up temporary file if it exists
    try {
      await Deno.remove(tempPath);
    } catch {
      // Ignore cleanup errors
    }
    return false;
  }
}

// Check all examples
const examples = [
  'supabase-edge-function-built-in-repositories.ts',
  'supabase-edge-function-custom-repositories.ts'
];

console.log('🚀 Checking Supabase Edge Function examples syntax...\n');

let allPass = true;
for (const example of examples) {
  const passed = await checkExample(example);
  allPass = allPass && passed;
  console.log('');
}

if (allPass) {
  console.log('🎉 All examples passed syntax checks!');
  Deno.exit(0);
} else {
  console.log('💥 Some examples have syntax errors!');
  Deno.exit(1);
}