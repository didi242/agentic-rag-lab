from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver

from pydantic import BaseModel, Field

from typing import Union

from prompts.system_prompt import SYSTEM_PROMPT

from tools.tools import get_person

from dataclasses import dataclass

@dataclass
class Context:
    user_id: str

class PersonInfo(BaseModel):
    name: str = Field(description = "Person's name")
    age: int = Field(description = "Person's age")
    occupation: str = Field(description = "Person's occupation")
    location: str = Field(description = "Person's location")
    languages: list = Field(description = "Person's languages")

class PersonEvent(BaseModel):
    event: str = Field(description = "Person's events")

class AgentReponse(BaseModel):
    person: PersonInfo | None = None
    events: list[PersonEvent] = []
    summary: str | None = None


model = init_chat_model(
    "ollama:qwen2.5:7b",
    base_url="http://ollama:11434"
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[
        get_person
    ],
    context_schema=Context,
    response_format=ToolStrategy(AgentReponse),
    checkpointer=checkpointer
)