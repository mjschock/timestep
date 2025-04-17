"use client";

import { AssistantRuntimeProvider } from "@assistant-ui/react";
import { useChatRuntime } from "@assistant-ui/react-ai-sdk";
import { Thread } from "@/components/assistant-ui/thread";
import { ThreadList } from "@/components/assistant-ui/thread-list";
import { useEffect, useState } from "react";

export const Assistant = () => {
  const runtime = useChatRuntime({
    api: "/api/chat"
  });
  
  const [isClient, setIsClient] = useState(false);
  
  // Only render the UI after client-side hydration is complete
  useEffect(() => {
    setIsClient(true);
  }, []);
  
  if (!isClient) {
    return <div className="grid h-dvh grid-cols-[200px_1fr]"></div>; // Empty placeholder
  }

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <div className="grid h-dvh grid-cols-[200px_1fr] gap-x-2 px-4 py-4">
        <ThreadList />
        <Thread />
      </div>
    </AssistantRuntimeProvider>
  );
};
