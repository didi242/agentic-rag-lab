import os

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemma4:e2b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")