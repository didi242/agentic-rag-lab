FROM python:3.11-slim

# System dependencies (wichtig für some langchain deps)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencies zuerst (cache-friendly)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# App Code
COPY . .

# Env (optional fallback)
ENV PYTHONUNBUFFERED=1

CMD ["python", "backend/main.py"]