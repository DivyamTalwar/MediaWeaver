# Graph Flow Explanation

This document explains the final, reliable flow of the LangGraph graph defined in `main.py`. The workflow is designed to be deterministic and robust, ensuring the correct tool is executed every time.

## 1. Graph Structure

The graph consists of two primary nodes and a clear, linear flow from start to finish.

-   **`agent` (Dispatcher Node)**: This is the entry point of the graph. It is not a traditional LLM-based agent but a deterministic **dispatcher**. Its sole responsibility is to parse a structured JSON request from the input message and create a specific tool call.
-   **`action` (Tool Execution Node)**: This node receives the tool call from the `agent` node and executes the corresponding tool function with the provided arguments.

## 2. State Management

The graph's state is managed by the `AgentState` class, which holds:

-   `messages`: A sequence of messages that tracks the conversation and tool interactions.
-   `chat_id`: A unique identifier for the session, passed to the tools if needed.

## 3. Execution Flow

The graph follows a simple, reliable, two-step process:

1.  **Entry Point -> `agent` Node**:
    -   The execution begins when `main.py` invokes the graph. The initial state contains a `HumanMessage` with a content payload structured as a JSON string (e.g., `{"tool_name": "blog_post", "args": {"topic": "..."}}`).
    -   The `agent` node (`agent_dispatcher` function) parses this JSON string.
    -   It constructs an `AIMessage` containing a precise `tool_call` for the specified tool and arguments.

2.  **`agent` Node -> `action` Node**:
    -   The `should_continue` conditional edge checks the output of the `agent` node. Since the message now contains a tool call, the graph transitions to the `action` node.
    -   The `action` node (`call_tool` function) executes the requested tool.
    -   The tool performs its task: generating content, saving it locally to the `langgraph/generated_*` directory, and logging the action to the designated Google Sheet.

3.  **`action` Node -> `END`**:
    -   After the tool execution is complete, the graph follows a direct edge to the `END` state.
    -   The execution finishes cleanly. There is no loop back to the agent, as the workflow is designed to perform one specific tool call per run.

This dispatcher-based architecture ensures that the system is predictable and robust, guaranteeing that the correct tool is always called with the correct parameters.