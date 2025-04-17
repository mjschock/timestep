export const runtime = "edge";
export const maxDuration = 300; // 5 minutes timeout for long-running agent tasks

export async function POST(req: Request) {
  try {
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";
    
    // Add timeout and retry logic
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 second timeout
    
    try {
      const response = await fetch(`${backendUrl}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(await req.json()),
        signal: controller.signal,
      });
      
      clearTimeout(timeoutId);

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Backend error:", errorText);
        return new Response(
          JSON.stringify({
            type: 3,
            content: `Backend error (${response.status}): ${errorText}`,
          }),
          { status: 500 }
        );
      }

      // Create a transform stream to process the backend's response
      const transformStream = new TransformStream({
        async transform(chunk, controller) {
          const text = new TextDecoder().decode(chunk);
          console.log("Frontend received chunk:", text);

          // Split the text into lines and process each line
          const lines = text.split("\n");
          for (const line of lines) {
            if (line.trim()) {
              try {
                // Parse the line to extract type and content
                const match = line.match(/^data: (.*)$/);
                if (match) {
                  const jsonStr = match[1];
                  try {
                    // Try to parse the JSON
                    const jsonChunk = JSON.parse(jsonStr);
                    console.log("Frontend parsed JSON chunk:", jsonChunk);

                    // Format as type:content for the assistant-stream library
                    const formattedChunk = `${jsonChunk.type}:${jsonChunk.content}`;
                    console.log("Frontend formatted chunk:", formattedChunk);

                    // Add the data: prefix and double newlines
                    const finalChunk = `data: ${formattedChunk}\n\n`;
                    console.log("Frontend sending chunk:", finalChunk);
                    controller.enqueue(new TextEncoder().encode(finalChunk));
                  } catch (e) {
                    console.error("Error parsing JSON:", e);
                    // If JSON parsing fails, send the raw line
                    controller.enqueue(new TextEncoder().encode(line + "\n"));
                  }
                } else {
                  // If the line doesn't match the expected format, pass it through as is
                  console.log("Frontend sending raw chunk:", line);
                  controller.enqueue(new TextEncoder().encode(line + "\n"));
                }
              } catch (e) {
                console.error("Error processing chunk:", e);
                // If there's an error processing the chunk, pass it through as is
                controller.enqueue(new TextEncoder().encode(line + "\n"));
              }
            }
          }
        },
      });

      // Return the transformed stream
      return new Response(response.body?.pipeThrough(transformStream), {
        headers: {
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          Connection: "keep-alive",
        },
      });
    } catch (error) {
      clearTimeout(timeoutId);
      if (error instanceof Error) {
        if (error.name === 'AbortError') {
          return new Response(
            JSON.stringify({
              type: 3,
              content: "Request timed out. Please try again.",
            }),
            { status: 500 }
          );
        }
        if (error.message.includes('Failed to fetch')) {
          return new Response(
            JSON.stringify({
              type: 3,
              content: "Unable to connect to the backend server. Please check if the server is running.",
            }),
            { status: 500 }
          );
        }
      }
      throw error; // Re-throw other errors to be caught by the outer try-catch
    }
  } catch (error) {
    console.error("Error in chat API route:", error);
    return new Response(
      JSON.stringify({
        type: 3,
        content: `An error occurred: ${
          error instanceof Error ? error.message : "Unknown error"
        }`,
      }),
      { status: 500 }
    );
  }
}
