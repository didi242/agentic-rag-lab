from fastapi import FastAPI
from api.routes_chat import router

app = FastAPI()

app.include_router(router)