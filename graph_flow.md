# MediaWeaver: Intelligent Content Automation Workflow

This document provides a comprehensive overview of the sophisticated graph-based workflow defined in `main.py`. The system, powered by LangGraph, leverages a powerful Large Language Model (LLM) to function as an intelligent agent, capable of understanding natural language prompts, selecting the appropriate tool, and executing complex content generation tasks.

---

## 1. Core Architecture: The Agentic Workflow

At its heart, the system is not a simple, linear script but a dynamic, stateful graph. This architecture allows for flexible and intelligent decision-making, moving beyond rigid, predefined flows.

-   **`agent` (The Brain)**: This is the central node of the graph and the primary entry point. It is powered by Google's `gemini-1.5-flash` model, which has been bound to a suite of custom tools. When it receives a user's prompt (e.g., "write a blog post about AI"), it analyzes the request, determines the user's intent, and decides which tool is best suited for the job (e.g., `blog_post`). It then constructs a precise `tool_call` with the necessary arguments.

-   **`action` (The Hands)**: This node is the workhorse of the graph. It receives the `tool_call` from the `agent` and acts as a router, executing the specified tool function (e.g., `blog_post()`, `create_image()`, etc.) with the arguments provided by the agent.

## 2. State Management (`AgentState`)

The graph's memory and context are managed by the `AgentState` class. This is a critical component that allows the graph to track the conversation's history. It contains:

-   `messages`: A continuously updated sequence of messages. This includes the initial `HumanMessage` (the user's prompt), the `AIMessage` from the agent (containing the tool call), and the `ToolMessage` (containing the result from the tool execution). This message history provides the full context for each run.

## 3. The Execution Flow: A Step-by-Step Journey

The graph follows an intelligent, conditional flow that enables it to handle a wide range of tasks seamlessly.

1.  **Initiation -> `agent` Node**:
    -   The process begins when `main.py` invokes the graph with an initial state. This state contains a `HumanMessage` with a natural language prompt from the user (e.g., "Create a short video about the history of the internet").
    -   The `agent` node receives this message. The powerful `gemini-1.5-flash` model analyzes the text, understands the user's goal, and generates an `AIMessage` containing a `tool_call` directed at the most appropriate tool (in this case, `faceless_video`).

2.  **Conditional Routing (`should_continue`)**:
    -   After the `agent` node runs, the graph consults the `should_continue` function. This function inspects the last message in the state.
    -   If the message is an `AIMessage` that contains a `tool_call`, it signals that there is work to be done. The graph then transitions to the **`action`** node.
    -   If the message does not contain a tool call (e.g., if the agent were to respond with a simple text message), the graph transitions to the **`END`** state, concluding the run.

3.  **Execution -> `action` Node**:
    -   The `action` node receives the `tool_call` and executes the corresponding Python function.
    -   The tool performs its specialized task:
        -   **Content Generation**: Writes a detailed blog post, a professional LinkedIn update, or a video script.
        -   **Image Manipulation**: Creates a new image from a prompt or edits an existing one.
        -   **Data Retrieval**: Fetches news articles or searches for images.
    -   Upon completion, the tool saves its output to the appropriate `generated_*` directory and logs the activity to a centralized Google Sheet for tracking.
    -   The result of the tool's execution (e.g., "Success: Blog post created...") is then packaged into a `ToolMessage`.

4.  **Conclusion -> `END`**:
    -   After the `action` node finishes, the graph follows a direct edge to the `END` state. The workflow is designed to execute a single, complete tool action per invocation, ensuring a clean and predictable conclusion.

This agent-driven architecture makes the MediaWeaver system exceptionally powerful and flexible. It can interpret a wide variety of user requests and intelligently route them to the correct tool, creating a seamless and automated content creation pipeline.
