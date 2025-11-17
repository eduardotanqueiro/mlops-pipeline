# Dockerfile for containerized pipeline (preprocess+training+eval) environment
FROM python:3.12-slim

# Install system deps
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Currently, DVC is for local only use
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["dvc", "repro"]
