from fastapi import APIRouter
from pydantic import BaseModel

from services.chat_service import chat_with_agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: str = "1"

@router.post("/chat")
def chat(req: ChatRequest):
    result = chat_with_agent(req.message, req.user_id)

    return result