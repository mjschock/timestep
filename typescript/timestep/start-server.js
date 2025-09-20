#!/usr/bin/env node
import {spawn} from 'child_process';
import {fileURLToPath} from 'url';
import {dirname, join} from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('🚀 Starting Timestep Agents Server...');

// Check if Deno is available
const denoCheck = spawn('deno', ['--version'], {stdio: 'pipe'});

denoCheck.on('error', error => {
	console.error('❌ Deno is not installed or not in PATH');
	console.error('Please install Deno from https://deno.land/');
	process.exit(1);
});

denoCheck.on('close', code => {
	if (code === 0) {
		// Deno is available, start the server
		const serverPath = join(__dirname, 'server.ts');
		const server = spawn('deno', ['run', '--allow-net', serverPath], {
			stdio: 'inherit',
		});

		server.on('error', error => {
			console.error('❌ Failed to start server:', error.message);
			process.exit(1);
		});

		server.on('close', code => {
			console.log(`Server process exited with code ${code}`);
		});

		// Handle graceful shutdown
		process.on('SIGINT', () => {
			console.log('\n🛑 Shutting down server...');
			server.kill('SIGINT');
			process.exit(0);
		});
	} else {
		console.error('❌ Deno is not installed or not in PATH');
		console.error('Please install Deno from https://deno.land/');
		process.exit(1);
	}
});
