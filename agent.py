from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from tools_manager import ToolsManager
from skills_manager import SkillsManager

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def build_agent():
    tools_manager = ToolsManager()
    skills_manager = SkillsManager()
    
    tools = tools_manager.get_all_tools()
    skills_text = skills_manager.get_all_skills()

    llm = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        model="google/gemma-4-e4b",
        temperature=0.7,
        max_tokens=2048,
        streaming=True
    )

    if tools:
        llm_with_tools = llm.bind_tools(tools)
    else:
        llm_with_tools = llm

    def chatbot(state: State):
        messages = state["messages"]
        
        if not any(isinstance(m, SystemMessage) for m in messages):
            base_sys_msg = "Senin adın Aristoteles. Zeki, hafif felsefi ama bir o kadar da pratik ve modern bir yapay zeka asistanısın. Kullanıcının sorularını Türkçe yanıtlıyorsun.\n\n"
            sys_msg_content = base_sys_msg + "Aşağıda kullanabileceğin yetenekler ve talimatlar verilmiştir:\n" + skills_text
            sys_msg = SystemMessage(content=sys_msg_content)
            messages = [sys_msg] + messages
            
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    
    if tools:
        tool_node = ToolNode(tools=tools)
        graph_builder.add_node("tools", tool_node)
        
        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_conditional_edges("chatbot", tools_condition)
        graph_builder.add_edge("tools", "chatbot")
    else:
        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_edge("chatbot", END)

    app = graph_builder.compile()
    
    return app
