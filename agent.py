from tools import simple_search_tool
from memory import ShortTermMemory
import re

memory = ShortTermMemory(size=3)

def is_factual(question: str):
    keywords = ["what", "when", "where", "who", "how many", "define", "capital", "value"]
    return any(question.lower().startswith(kw) for kw in keywords)

def agent_response(user_msg: str):
    memory.add({"user": user_msg})

    if is_factual(user_msg):
        result = simple_search_tool(user_msg)
        
        if result != "No factual answer found in database.":
            response = f"Factual Answer: {result}"
        else:
            response = "I tried searching but couldn't find the answer in my small database."
    
    else:
        response = f"I understand. You said: '{user_msg}'. Tell me more!"

    memory.add({"assistant": response})
    return {
        "response": response,
        "memory": memory.get_context()
    }
