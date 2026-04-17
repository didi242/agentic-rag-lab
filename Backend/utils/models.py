from langchain.chat_models import init_chat_model

OLLAMA_BASE_URL = "http://ollama:11434"


MODEL_REGISTRY = {
    "fast": "qwen2.5:7b",
    "balanced": "mistral:7b",
    "smart": "gemma2:9b",
    "gemma4:e4b": "gemma4:e4b",
    "gemma4:e2b": "gemma4:e2b"
}

def get_model(model_key: str = "gemma4:e2b"):
    if model_key not in MODEL_REGISTRY:
        raise ValueError(f"Unknown model key: {model_key}")

    return init_chat_model(
        f"ollama:{MODEL_REGISTRY[model_key]}",
        base_url=OLLAMA_BASE_URL
    )