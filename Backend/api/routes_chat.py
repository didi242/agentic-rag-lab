from fastapi import APIRouter, Request
from pydantic import BaseModel

from services.chat_service import chat_with_agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: str = "1"

@router.post("/chat")
def chat(req: ChatRequest, request: Request):
    agent = request.app.state.agent
    result = chat_with_agent(agent=agent, message=req.message, user_id=req.user_id)

    return result