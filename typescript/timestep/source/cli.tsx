#!/usr/bin/env node
import React from 'react';
import {render} from 'ink';
import meow from 'meow';
import App from './app.js';

const cli = meow(
	`
	Usage
	  $ timestep [command]

	Commands
	  server     Start the agents server
	  list-agents  List all agents from the server
	  list-chats   List all chats from the server
	  list-models  List all models from the server
	  list-tools   List all tools from the server
	  list-traces  List all traces from the server
	  --name     Your name (for greeting)

	Examples
	  $ timestep --name=Jane
	  Hello, Jane
	  
	  $ timestep server
	  Start the agents server
	  
	  $ timestep list-agents
	  List all agents from the server
	  
	  $ timestep list-chats
	  List all chats from the server
	  
	  $ timestep list-models
	  List all models from the server
	  
	  $ timestep list-tools
	  List all tools from the server
	  
	  $ timestep list-traces
	  List all traces from the server
`,
	{
		importMeta: import.meta,
		flags: {
			name: {
				type: 'string',
			},
		},
	},
);

const command = cli.input[0];

render(<App name={cli.flags.name} command={command} />);
