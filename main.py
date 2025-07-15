from dotenv import load_dotenv
load_dotenv()
import os
from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from create_image import create_image
from edit_image import edit_image
from search_images import search_images
from blog_post import blog_post
from linkedin_post import linkedin_post
from faceless_video import faceless_video
from get_news import get_news
from content_strategist import content_strategist

tool_map = {tool.__name__: tool for tool in [
    create_image, edit_image, search_images, blog_post,
    linkedin_post, faceless_video, get_news, content_strategist
]}
tools = list(tool_map.values())

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

def should_continue(state):
    last_message = state['messages'][-1]
    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return "end"
    return "continue"

def call_tool(state):
    last_message = state['messages'][-1]
    tool_invocations = []
    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]
        tool_to_call = tool_map.get(tool_name)

        if tool_to_call:
            try:
                print(f"Executing Tool: {tool_name} with args: {tool_call['args']}")
                tool_args = tool_call["args"]
                response = tool_to_call(**tool_args)
                tool_invocations.append(ToolMessage(content=str(response), tool_call_id=tool_call['id']))
            except Exception as e:
                error_msg = f"ERROR executing {tool_name}: {e}"
                print(error_msg)
                tool_invocations.append(ToolMessage(content=error_msg, tool_call_id=tool_call['id']))
        else:
            tool_invocations.append(ToolMessage(content=f"Tool '{tool_name}' not found.", tool_call_id=tool_call['id']))

    return {"messages": tool_invocations}

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_with_tools = llm.bind_tools(tools)

def agent(state):
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


workflow = StateGraph(AgentState)
workflow.add_node("agent", agent)
workflow.add_node("action", call_tool)
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {"continue": "action", "end": END}
)
workflow.add_edge("action", END)

app = workflow.compile()

if __name__ == "__main__":
    prompts = [
        "Develop a comprehensive content strategy about the impact of AI in gambling apps.",
        "Summarize the latest news regarding Artificial Intelligence.",
        "Write a detailed blog post on the how AI can replace humans.",
        "Draft a LinkedIn post about the rise of AI in Virtual Gaming.",
        "Create a photorealistic image of a Two Dogs Sleeping On The Red Bed",
        "Search for high-quality images of the Virat Kholi",
        "Produce a short, informative faceless video explaining the history of ancient India",
        "Take the image from this path'generated_images/a_cat_sitting_on_a_couch.png' and add a small, red bow tie to the cat."
    ]

    for user_prompt in prompts:
        print(f"\n\nInvoking Agent with prompt: '{user_prompt}'")
        
        initial_state = {
            "messages": [HumanMessage(content=user_prompt)]
        }

        try:
            result = app.invoke(initial_state)

            print("\nFinal State")
            for message in result['messages']:
                print(f"Type: {type(message).__name__}, Content: {message.content}")
                if isinstance(message, AIMessage) and message.tool_calls:
                    print(f"Tool Calls: {message.tool_calls}")
            print("Agent execution finished.")

        except Exception as e:
            print(f"\nERROR during invocation for prompt: '{user_prompt}'")
            print(f"Error: {e}")
            print("Moving to next prompt.")
