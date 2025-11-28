from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent_response

app = FastAPI(title="AI Question-Answer Helper")

class Message(BaseModel):
    user_message: str

@app.post("/chat")
def chat(message: Message):
    return agent_response(message.user_message)
