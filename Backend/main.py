# main.py
import os
from fastapi import FastAPI

from api.routes_chat import router
from agents.agent import build_agent
from config import DEFAULT_MODEL


app = FastAPI()

# global state container
app.state.agent = None
app.state.model_key = DEFAULT_MODEL


@app.on_event("startup")
def startup():
    app.state.agent = build_agent(app.state.model_key)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": app.state.model_key
    }


app.include_router(router)