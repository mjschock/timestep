import {
  ActionBarPrimitive,
  BranchPickerPrimitive,
  ComposerPrimitive,
  MessagePrimitive,
  ThreadPrimitive,
} from "@assistant-ui/react";
import type { FC } from "react";
import React, { useState, useEffect } from "react";
import {
  ArrowDownIcon,
  CheckIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  CopyIcon,
  PencilIcon,
  RefreshCwIcon,
  SendHorizontalIcon,
  SquareIcon,
  LoaderIcon,
  CircleIcon,
} from "lucide-react";
import { cn } from "@/lib/utils";

import { Button } from "@/components/ui/button";
import { MarkdownText } from "@/components/assistant-ui/markdown-text";
import { TooltipIconButton } from "@/components/assistant-ui/tooltip-icon-button";
import { Icon } from "@/components/ui/icon";

// Global state to store agent progress steps
let progressSteps: string[] = [];

// Function to add a progress step (callable from frontend event listeners)
function addProgressStep(step: string) {
  progressSteps.push(step);
  // Fire a custom event that can be listened to
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('agent-progress', { detail: step }));
  }
}

// Listen for progress messages from the server
if (typeof window !== 'undefined') {
  // Add a global event listener for SSE messages (works with EventSource)
  window.addEventListener('message', (event) => {
    try {
      const data = event.data;
      if (data && typeof data === 'string' && data.startsWith('data: ')) {
        try {
          const jsonStr = data.substring(6); // Remove 'data: ' prefix
          const jsonData = JSON.parse(jsonStr);
          if (jsonData.type === 2) { // Progress message
            addProgressStep(jsonData.content);
          }
        } catch (error) {
          console.error('Error parsing JSON message:', error);
        }
      }
    } catch (error) {
      console.error('Error processing message:', error);
    }
  });
}

export const Thread: FC = () => {
  return (
    <ThreadPrimitive.Root
      className="bg-background box-border flex h-full flex-col overflow-hidden"
      style={{
        ["--thread-max-width" as string]: "42rem",
      }}
    >
      <ThreadPrimitive.Viewport className="flex h-full flex-col items-center overflow-y-scroll scroll-smooth bg-inherit px-4 pt-8">
        <ThreadWelcome />

        <ThreadPrimitive.Messages
          components={{
            UserMessage: UserMessage,
            EditComposer: EditComposer,
            AssistantMessage: AssistantMessage,
          }}
        />

        <ThreadPrimitive.If empty={false}>
          <div className="min-h-8 flex-grow" />
        </ThreadPrimitive.If>

        <div className="sticky bottom-0 mt-3 flex w-full max-w-[var(--thread-max-width)] flex-col items-center justify-end rounded-t-lg bg-inherit pb-4">
          <ThreadScrollToBottom />
          <Composer />
        </div>
      </ThreadPrimitive.Viewport>
    </ThreadPrimitive.Root>
  );
};

const ThreadScrollToBottom: FC = () => {
  return (
    <ThreadPrimitive.ScrollToBottom asChild>
      <TooltipIconButton
        tooltip="Scroll to bottom"
        variant="outline"
        className="absolute -top-8 rounded-full disabled:invisible cursor-pointer"
      >
        <Icon icon={ArrowDownIcon} />
      </TooltipIconButton>
    </ThreadPrimitive.ScrollToBottom>
  );
};

const ThreadWelcome: FC = () => {
  return (
    <ThreadPrimitive.Empty>
      <div className="flex w-full max-w-[var(--thread-max-width)] flex-grow flex-col">
        <div className="flex w-full flex-grow flex-col items-center justify-center">
          <p className="mt-4 font-medium">How can I help you today?</p>
        </div>
        <ThreadWelcomeSuggestions />
      </div>
    </ThreadPrimitive.Empty>
  );
};

const ThreadWelcomeSuggestions: FC = () => {
  return (
    <div className="mt-3 flex w-full items-stretch justify-center gap-4">
      <ThreadPrimitive.Suggestion
        className="hover:bg-muted/80 flex max-w-sm grow basis-0 flex-col items-center justify-center rounded-lg border p-3 transition-colors ease-in cursor-pointer"
        prompt="What is the weather in Oakland, California?"
        method="replace"
        autoSend
      >
        <span className="line-clamp-2 text-ellipsis text-sm font-semibold">
          What is the weather in Oakland, California?
        </span>
      </ThreadPrimitive.Suggestion>
      <ThreadPrimitive.Suggestion
        className="hover:bg-muted/80 flex max-w-sm grow basis-0 flex-col items-center justify-center rounded-lg border p-3 transition-colors ease-in cursor-pointer"
        prompt="What is assistant-ui?"
        method="replace"
        autoSend
      >
        <span className="line-clamp-2 text-ellipsis text-sm font-semibold">
          What is assistant-ui?
        </span>
      </ThreadPrimitive.Suggestion>
    </div>
  );
};

const Composer: FC = () => {
  return (
    <ComposerPrimitive.Root className="focus-within:border-ring/20 flex w-full flex-wrap items-end rounded-lg border bg-inherit px-2.5 shadow-sm transition-colors ease-in">
      <ComposerPrimitive.Input
        rows={1}
        autoFocus
        placeholder="Write a message..."
        className="placeholder:text-muted-foreground max-h-40 flex-grow resize-none border-none bg-transparent px-2 py-4 text-sm outline-none focus:ring-0 disabled:cursor-not-allowed"
      />
      <div className="composer-send" style={{ cursor: 'pointer !important' }}>
        <ComposerAction />
      </div>
    </ComposerPrimitive.Root>
  );
};

const ComposerAction: FC = () => {
  return (
    <>
      <ThreadPrimitive.If running={false}>
        <ComposerPrimitive.Send asChild>
          <TooltipIconButton
            tooltip="Send"
            variant="default"
            className="my-2.5 size-8 p-2 transition-opacity ease-in cursor-pointer"
            style={{ cursor: 'pointer !important' }}
          >
            <Icon icon={SendHorizontalIcon} style={{ cursor: 'pointer !important' }} />
          </TooltipIconButton>
        </ComposerPrimitive.Send>
      </ThreadPrimitive.If>
      <ThreadPrimitive.If running>
        <ComposerPrimitive.Cancel asChild>
          <TooltipIconButton
            tooltip="Cancel"
            variant="default"
            className="my-2.5 size-8 p-2 transition-opacity ease-in cursor-pointer"
          >
            <Icon icon={SquareIcon} />
          </TooltipIconButton>
        </ComposerPrimitive.Cancel>
      </ThreadPrimitive.If>
    </>
  );
};

const UserMessage: FC = () => {
  return (
    <MessagePrimitive.Root className="grid auto-rows-auto grid-cols-[minmax(72px,1fr)_auto] gap-y-2 [&:where(>*)]:col-start-2 w-full max-w-[var(--thread-max-width)] py-4">
      <UserActionBar />

      <div className="bg-muted text-foreground max-w-[calc(var(--thread-max-width)*0.8)] break-words rounded-3xl px-5 py-2.5 col-start-2 row-start-2">
        <MessagePrimitive.Content />
      </div>

      <BranchPicker className="col-span-full col-start-1 row-start-3 -mr-1 justify-end" />
    </MessagePrimitive.Root>
  );
};

const UserActionBar: FC = () => {
  return (
    <ActionBarPrimitive.Root
      hideWhenRunning
      autohide="not-last"
      className="flex flex-col items-end col-start-1 row-start-2 mr-3 mt-2.5"
    >
      <ActionBarPrimitive.Edit asChild>
        <TooltipIconButton tooltip="Edit">
          <Icon icon={PencilIcon} />
        </TooltipIconButton>
      </ActionBarPrimitive.Edit>
    </ActionBarPrimitive.Root>
  );
};

const EditComposer: FC = () => {
  return (
    <ComposerPrimitive.Root className="bg-muted my-4 flex w-full max-w-[var(--thread-max-width)] flex-col gap-2 rounded-xl">
      <ComposerPrimitive.Input className="text-foreground flex h-8 w-full resize-none bg-transparent p-4 pb-0 outline-none" />

      <div className="mx-3 mb-3 flex items-center justify-center gap-2 self-end">
        <ComposerPrimitive.Cancel asChild>
          <Button variant="ghost" className="cursor-pointer">Cancel</Button>
        </ComposerPrimitive.Cancel>
        <ComposerPrimitive.Send asChild>
          <Button className="cursor-pointer">Send</Button>
        </ComposerPrimitive.Send>
      </div>
    </ComposerPrimitive.Root>
  );
};

const AssistantMessage: FC = () => {
  // Local state to store the progress steps for this message
  const [steps, setSteps] = useState<string[]>([]);
  const [messageType, setMessageType] = useState<number>(0);
  const [messageContent, setMessageContent] = useState<string>("");
  
  // Listen for progress updates
  useEffect(() => {
    // Reset steps when component mounts
    setSteps([...progressSteps]);
    
    // Listen for agent-progress events
    const handleProgress = (event: CustomEvent) => {
      setSteps(prev => [...prev, event.detail]);
    };
    
    // Listen for message events
    const handleMessage = (event: MessageEvent) => {
      try {
        if (event.data && typeof event.data === 'string' && event.data.startsWith('data: ')) {
          const jsonStr = event.data.substring(6); // Remove 'data: ' prefix
          const jsonData = JSON.parse(jsonStr);
          setMessageType(jsonData.type);
          setMessageContent(jsonData.content);
        }
      } catch (error) {
        console.error('Error processing message:', error);
      }
    };
    
    // Add event listeners
    window.addEventListener('agent-progress', handleProgress as EventListener);
    window.addEventListener('message', handleMessage);
    
    // Cleanup
    return () => {
      window.removeEventListener('agent-progress', handleProgress as EventListener);
      window.removeEventListener('message', handleMessage);
      
      // Reset global steps when component unmounts
      progressSteps = [];
    };
  }, []);
  
  return (
    <MessagePrimitive.Root className="grid grid-cols-[auto_auto_1fr] grid-rows-[auto_1fr] relative w-full max-w-[var(--thread-max-width)] py-4">
      <div className="text-foreground max-w-[calc(var(--thread-max-width)*0.8)] break-words leading-7 col-span-2 col-start-2 row-start-1 my-1.5">
        <ThreadPrimitive.If running>
          <div className="flex items-center mb-2">
            <LoaderIcon className="mr-2 h-4 w-4 animate-spin" />
            <span className="text-sm font-medium">
              {messageType === 1 ? "Processing your request..." : messageContent}
            </span>
          </div>
          <div className="mt-2 mb-4 text-xs border rounded-md p-3 bg-muted/30 text-muted-foreground">
            {steps.length > 0 ? (
              <div className="space-y-1.5 max-h-48 overflow-y-auto">
                {steps.map((step, idx) => (
                  <div key={idx} className="flex items-start mb-1.5">
                    <CircleIcon className="h-2 w-2 mr-2 mt-1 fill-primary stroke-primary" />
                    <p className="flex-1">{step}</p>
                  </div>
                ))}
                <div className="flex items-center mt-2 animate-pulse">
                  <span className="bg-primary/20 rounded-full h-1.5 w-1.5 mr-1"></span>
                  <span className="bg-primary/30 rounded-full h-1.5 w-1.5 mr-1"></span>
                  <span className="bg-primary/40 rounded-full h-1.5 w-1.5"></span>
                </div>
              </div>
            ) : (
              <div className="space-y-1.5">
                <p className="italic">The AI is working on your request. This might take a moment for complex tasks.</p>
                
                <div className="flex items-center mt-2 animate-pulse">
                  <span className="bg-primary/20 rounded-full h-1.5 w-1.5 mr-1"></span>
                  <span className="bg-primary/30 rounded-full h-1.5 w-1.5 mr-1"></span>
                  <span className="bg-primary/40 rounded-full h-1.5 w-1.5"></span>
                </div>
              </div>
            )}
          </div>
        </ThreadPrimitive.If>
        <MessagePrimitive.Content components={{ Text: MarkdownText }} />
      </div>

      <AssistantActionBar />

      <BranchPicker className="col-start-2 row-start-2 -ml-2 mr-2" />
    </MessagePrimitive.Root>
  );
};

const AssistantActionBar: FC = () => {
  return (
    <ActionBarPrimitive.Root
      hideWhenRunning
      autohide="not-last"
      autohideFloat="single-branch"
      className="text-muted-foreground flex gap-1 col-start-3 row-start-2 -ml-1 data-[floating]:bg-background data-[floating]:absolute data-[floating]:rounded-md data-[floating]:border data-[floating]:p-1 data-[floating]:shadow-sm"
    >
      <ActionBarPrimitive.Copy asChild>
        <TooltipIconButton tooltip="Copy">
          <MessagePrimitive.If copied>
            <Icon icon={CheckIcon} />
          </MessagePrimitive.If>
          <MessagePrimitive.If copied={false}>
            <Icon icon={CopyIcon} />
          </MessagePrimitive.If>
        </TooltipIconButton>
      </ActionBarPrimitive.Copy>
      <ActionBarPrimitive.Reload asChild>
        <TooltipIconButton tooltip="Refresh">
          <Icon icon={RefreshCwIcon} />
        </TooltipIconButton>
      </ActionBarPrimitive.Reload>
    </ActionBarPrimitive.Root>
  );
};

const BranchPicker: FC<BranchPickerPrimitive.Root.Props> = ({
  className,
  ...rest
}) => {
  return (
    <BranchPickerPrimitive.Root
      hideWhenSingleBranch
      className={cn(
        "text-muted-foreground inline-flex items-center text-xs",
        className
      )}
      {...rest}
    >
      <BranchPickerPrimitive.Previous asChild>
        <TooltipIconButton tooltip="Previous">
          <Icon icon={ChevronLeftIcon} />
        </TooltipIconButton>
      </BranchPickerPrimitive.Previous>
      <span className="font-medium">
        <BranchPickerPrimitive.Number /> / <BranchPickerPrimitive.Count />
      </span>
      <BranchPickerPrimitive.Next asChild>
        <TooltipIconButton tooltip="Next">
          <Icon icon={ChevronRightIcon} />
        </TooltipIconButton>
      </BranchPickerPrimitive.Next>
    </BranchPickerPrimitive.Root>
  );
};
