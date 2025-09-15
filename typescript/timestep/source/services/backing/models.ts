/**
 * Custom model implementations for A2A agent library.
 */
// @ts-nocheck

import { Ollama } from "ollama";
import {
  Model,
  Usage,
  withGenerationSpan,
  resetCurrentSpan,
  createGenerationSpan,
  setCurrentSpan,
} from '@openai/agents-core';
import type {
  ModelRequest,
  ModelResponse,
  ResponseStreamEvent,
  SerializedOutputType,
} from '@openai/agents-core';
import type { Stream } from 'openai/streaming';
import { protocol } from '@openai/agents-core';
import { Span, GenerationSpanData } from '@openai/agents-core';

// Note: TypeScript SDK has different interfaces than Python, so we need to adapt
// This implementation maintains the same logic as Python but uses TypeScript SDK patterns

export class OllamaModel implements Model {
  #client: Ollama;
  #model: string;

  constructor(client: Ollama, model: string) {
    this.#client = client;
    this.#model = model;
  }

  private _convertOllamaToOpenai(ollamaResponse: any): any {
    // Convert Ollama response format to OpenAI ChatCompletion format.

    // Extract message from Ollama response
    const ollamaMessage = ollamaResponse['message'];

    // Create OpenAI-style message
    const message: any = {
      role: ollamaMessage['role'],
      content: ollamaMessage['content']
    };

    // Handle tool calls if present
    if (ollamaMessage['tool_calls'] && ollamaMessage['tool_calls'].length > 0) {
      // Convert Ollama tool calls to OpenAI format
      message.tool_calls = ollamaMessage['tool_calls'].map((toolCall: any, index: number) => {
        // Generate a more unique ID that matches OpenAI's format
        const id = `call_${Math.random().toString(36).substr(2, 9)}_${Date.now()}_${index}`;
        
        return {
          id: id,
          type: 'function',
          function: {
            name: toolCall.function.name,
            arguments: JSON.stringify(toolCall.function.arguments)
          }
        };
      });
    }

    // Create choice
    const choice = {
      finish_reason: message.tool_calls ? "tool_calls" : "stop",
      index: 0,
      message: message
    };

    // Extract token usage from Ollama response
    // Ollama provides eval_count (completion tokens) and prompt_eval_count (prompt tokens)
    const evalCount = ollamaResponse['eval_count'] || 0;
    const promptEvalCount = ollamaResponse['prompt_eval_count'] || 0;
    const totalTokens = evalCount + promptEvalCount;

    // Create usage info with actual token counts from Ollama
    const usage = {
      completion_tokens: evalCount,
      prompt_tokens: promptEvalCount,
      total_tokens: totalTokens
    };

    // Create ChatCompletion response
    const result = {
      id: `ollama-${Math.floor(Date.now() / 1000)}`,
      choices: [choice],
      created: Math.floor(Date.now() / 1000),
      model: this.#model,
      object: "chat.completion",
      usage: usage
    };

    return result;
  }

  // Convert a handoff (agent) into a function tool callable by the model
  private convertHandoffTool(handoff: any) {
    return {
      type: 'function',
      function: {
        name: handoff.toolName,
        description: handoff.toolDescription || '',
        parameters: handoff.inputJsonSchema,
      },
    };
  }

  async #fetchResponse(
    request: ModelRequest,
    span: Span<GenerationSpanData> | undefined,
    stream: true,
  ): Promise<Stream<any>>;
  async #fetchResponse(
    request: ModelRequest,
    span: Span<GenerationSpanData> | undefined,
    stream: false,
  ): Promise<any>;
  async #fetchResponse(
    request: ModelRequest,
    span: Span<GenerationSpanData> | undefined,
    stream: boolean,
  ): Promise<Stream<any> | any> {
    // Convert input to messages - matching Python Converter.items_to_messages logic
    let convertedMessages: any[] = [];
    
    if (typeof request.input === 'string') {
      convertedMessages = [{ role: 'user', content: request.input }];
    } else {
      convertedMessages = request.input.map((item: any) => {
        // Handle different types of input items
        if (item.role === 'tool') {
          // Tool role message - use as is
          return {
            role: 'tool',
            content: item.content || '',
            tool_call_id: item.tool_call_id || ''
          };
        } else if (item.type === 'function_call') {
          // Convert function call to assistant message with tool_calls
          
          // Parse arguments string to object for Ollama
          let parsedArguments;
          try {
            parsedArguments = JSON.parse(item.arguments);
          } catch (e) {
            parsedArguments = item.arguments;
          }
          
          return {
            role: 'assistant',
            content: '',
            tool_calls: [{
              id: item.callId,
              type: 'function',
              function: {
                name: item.name,
                arguments: parsedArguments
              }
            }]
          };
        } else if (item.type === 'function_call_result') {
          // Convert function call result to tool role message
          
          // Extract text content from output object
          let content = '';
          if (typeof item.output === 'string') {
            content = item.output;
          } else if (item.output?.text) {
            content = item.output.text;
          } else if (item.output?.content) {
            content = item.output.content;
          } else {
            content = JSON.stringify(item.output) || '';
          }
          
          return {
            role: 'tool',
            content: content,
            tool_call_id: item.callId
          };
        } else if (item.role) {
          // Standard message with role
          const msg: any = {
            role: item.role,
            content: item.content || item.text || ''
          };
          
          // Preserve tool_calls if present (for assistant messages with tool calls)
          if (item.tool_calls) {
            msg.tool_calls = item.tool_calls;
          }
          
          return msg;
        } else {
          // Fallback to user message
          return {
            role: 'user', 
            content: item.content || item.text || ''
          };
        }
      }).filter(msg => msg !== null); // Remove null items
    }

    if (request.systemInstructions) {
      convertedMessages.unshift({
        content: request.systemInstructions,
        role: "system",
      });
    }


    if (span && request.tracing === true) {
      span.spanData.input = convertedMessages;
    }

    // Convert messages to Ollama format
    const ollamaMessages = [];
    for (const msg of convertedMessages) {
      // Extract text content from various formats
      let content = '';
      if (typeof msg['content'] === 'string') {
        content = msg['content'];
      } else if (Array.isArray(msg['content'])) {
        // Handle array format with input_text objects
        for (const part of msg['content']) {
          if (part.type === 'input_text' && part.text) {
            content += part.text;
          } else if (typeof part === 'string') {
            content += part;
          } else if (part.text) {
            content += part.text;
          }
        }
      } else if (msg['content'] && typeof msg['content'] === 'object' && msg['content'].text) {
        content = msg['content'].text;
      }
      
      const ollamaMsg: any = {
        'role': msg['role'],
        'content': content
      };
      
      // Add tool_call_id for tool role messages
      if (msg['role'] === 'tool' && msg['tool_call_id']) {
        ollamaMsg['tool_call_id'] = msg['tool_call_id'];
      }
      
      // Add tool_calls for assistant messages
      if (msg['role'] === 'assistant' && msg['tool_calls']) {
        // Ensure arguments are objects, not strings for Ollama
        ollamaMsg['tool_calls'] = msg['tool_calls'].map((toolCall: any) => {
          const result = { ...toolCall };
          if (result.function && result.function.arguments) {
            // Parse arguments string to object if needed
            if (typeof result.function.arguments === 'string') {
              try {
                result.function.arguments = JSON.parse(result.function.arguments);
              } catch (error) {
                result.function.arguments = {};
              }
            }
          }
          return result;
        });
      }
      
      ollamaMessages.push(ollamaMsg);
    }

    // Convert tools from SerializedTool format to Ollama format
    const ollamaTools = (request.tools?.map(tool => {
      if (tool.type === 'function') {
        return {
          type: 'function',
          function: {
            name: tool.name,
            description: tool.description,
            parameters: tool.parameters
          }
        };
      }
      // For other tool types (computer, hosted), we'll skip them for now
      // as Ollama primarily supports function tools
      return null;
    }).filter(tool => tool !== null) as any[]) || [];

    // Also include handoffs as function tools so the model can call them
    if ((request as any).handoffs && Array.isArray((request as any).handoffs)) {
      for (const handoff of (request as any).handoffs) {
        try {
          const handoffTool = this.convertHandoffTool(handoff);
          if (handoffTool) {
            ollamaTools.push(handoffTool);
          }
        } catch (e) {
          console.warn('🔍 Failed to convert handoff to tool:', e);
        }
      }
    }

    // Use Ollama client
    const chatOptions: any = {
      model: this.#model,
      messages: ollamaMessages,
      stream: stream as any
    };

    // Only add tools if there are any
    if (ollamaTools.length > 0) {
      chatOptions.tools = ollamaTools;
    }


    const responseData = await this.#client.chat(chatOptions);

    if (stream) {
      return responseData; // Return stream directly for streaming
    }

    // Convert Ollama response to OpenAI format for compatibility
    const ret = this._convertOllamaToOpenai(responseData);

    return ret;
  }

  async getResponse(request: ModelRequest): Promise<ModelResponse> {
    const response = await withGenerationSpan(async (span) => {
      span.spanData.model = this.#model;
      span.spanData.model_config = request.modelSettings
        ? {
            temperature: request.modelSettings.temperature,
            top_p: request.modelSettings.topP,
            frequency_penalty: request.modelSettings.frequencyPenalty,
            presence_penalty: request.modelSettings.presencePenalty,
          }
        : { base_url: 'ollama_client' };
      const response = await this.#fetchResponse(request, span, false);
      if (span && request.tracing === true) {
        span.spanData.output = [response];
      }
      return response;
    });

    const output: protocol.OutputModelItem[] = [];
    if (response.choices && response.choices[0]) {
      const message = response.choices[0].message;

      if (
        message.content !== undefined &&
        message.content !== null &&
        // Azure OpenAI returns empty string instead of null for tool calls, causing parser rejection
        !(message.tool_calls && message.content === '')
      ) {
        const { content, ...rest } = message;
        output.push({
          id: response.id,
          type: 'message',
          role: 'assistant',
          content: [
            {
              type: 'output_text',
              text: content || '',
              providerData: rest,
            },
          ],
          status: 'completed',
        });
      } else if (message.refusal) {
        const { refusal, ...rest } = message;
        output.push({
          id: response.id,
          type: 'message',
          role: 'assistant',
          content: [
            {
              type: 'refusal',
              refusal: refusal || '',
              providerData: rest,
            },
          ],
          status: 'completed',
        });
      } else if (message.tool_calls) {
        for (const tool_call of message.tool_calls) {
          if (tool_call.type === 'function') {
            const { id: callId, ...remainingToolCallData } = tool_call;
            const {
              arguments: args,
              name,
              ...remainingFunctionData
            } = tool_call.function;
            output.push({
              id: response.id,
              type: 'function_call',
              arguments: args,
              name: name,
              callId: callId,
              status: 'completed',
              providerData: {
                ...remainingToolCallData,
                ...remainingFunctionData,
              },
            });
          }
        }
      }
    }
    
    function toResponseUsage(usage: any) {
      return {
        requests: 1,
        input_tokens: usage.prompt_tokens,
        output_tokens: usage.completion_tokens,
        total_tokens: usage.total_tokens,
        input_tokens_details: {
          cached_tokens: usage.prompt_tokens_details?.cached_tokens || 0,
        },
        output_tokens_details: {
          reasoning_tokens: usage.completion_tokens_details?.reasoning_tokens || 0,
        },
      };
    }

    const modelResponse: ModelResponse = {
      usage: response.usage
        ? new Usage(toResponseUsage(response.usage))
        : new Usage(),
      output,
      responseId: response.id,
      providerData: response,
    };

    return modelResponse;
  }

  async *getStreamedResponse(
    request: ModelRequest,
  ): AsyncIterable<ResponseStreamEvent> {
    const span = request.tracing ? createGenerationSpan() : undefined;
    try {
      if (span) {
        span.start();
        setCurrentSpan(span);
      }
      const stream = await this.#fetchResponse(request, span, true);

      // For Ollama streaming, we need to convert the stream format
      // This is a simplified implementation - real implementation would need
      // proper stream conversion similar to convertChatCompletionsStreamToResponses
      const response = {
        id: `ollama-${Math.floor(Date.now() / 1000)}`,
        created: Math.floor(Date.now() / 1000),
        model: this.#model,
        object: 'chat.completion',
        choices: [],
        usage: {
          prompt_tokens: 0,
          completion_tokens: 0,
          total_tokens: 0,
        },
      };

      // Yield stream events - simplified for Ollama
      for await (const chunk of stream as any) {
        if (chunk.message && chunk.message.content) {
          yield {
            type: 'output_text_delta',
            delta: chunk.message.content || '',
          } as ResponseStreamEvent;
        }
        
        if (chunk.done) {
          yield {
            type: 'response_done',
            response: {
              id: response.id,
              output: [
                {
                  type: 'message' as const,
                  role: 'assistant' as const,
                  status: 'completed' as const,
                  content: [{
                    type: 'text' as const,
                    text: response.choices[0]?.message?.content || ''
                  }]
                }
              ],
              usage: new Usage({
                requests: 1,
                input_tokens: response.usage.prompt_tokens,
                output_tokens: response.usage.completion_tokens,
                total_tokens: response.usage.total_tokens
              })
            }
          } as ResponseStreamEvent;
          break;
        }
      }

      if (span && response && request.tracing === true) {
        span.spanData.output = [response];
      }
    } catch (error) {
      if (span) {
        span.setError({
          message: 'Error streaming response',
          data: {
            error:
              request.tracing === true
                ? String(error)
                : error instanceof Error
                  ? error.name
                  : undefined,
          },
        });
      }
      throw error;
    } finally {
      if (span) {
        span.end();
        resetCurrentSpan();
      }
    }
  }
}

