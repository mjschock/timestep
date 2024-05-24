from typing import Any, Dict, List, Optional

from llama_index.callbacks.base_handler import BaseCallbackHandler
from llama_index.callbacks.schema import CBEventType


class StreamingCallbackHandler(BaseCallbackHandler):
    """Base callback handler that can be used to track event starts and ends."""

    def __init__(self) -> None:
        """Initialize the base callback handler."""
        super().__init__([], [])
        self._queue = []
        self._counter = 0

    def on_event_start(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        parent_id: str = "",
        **kwargs: Any,
    ) -> str:
        """Run when an event starts and return id of event."""
        if event_type == CBEventType.FUNCTION_CALL:
            arguments_str = payload["function_call"]
            tool_str = payload["tool"].name
            print_str = (
                "\n\n\n\n\n=== Calling Function ===\n\n\n\n"
                f"Calling function: {tool_str} with args: {arguments_str}\n\n"
            )
            # Add this to queue
            self._queue.append(print_str)

    def on_event_end(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        **kwargs: Any,
    ) -> None:
        """Run when an event ends."""
        if event_type == CBEventType.FUNCTION_CALL:
            response = payload["function_call_response"]
            # Add this to queue
            print_str = f"\n\nGot output: {response}\n" "========================\n\n"
            self._queue.append(print_str)

    def reset(self) -> None:
        """Reset the callback handler."""
        self._queue = []
        self._counter = 0

    @property
    def queue(self) -> List[str]:
        """Get the queue of events."""
        return self._queue

    @property
    def counter(self) -> int:
        """Get the counter."""
        return self._counter

    def start_trace(self, trace_id: Optional[str] = None) -> None:
        """Run when an overall trace is launched."""
        pass

    def end_trace(
        self,
        trace_id: Optional[str] = None,
        trace_map: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        """Run when an overall trace is exited."""
        pass
