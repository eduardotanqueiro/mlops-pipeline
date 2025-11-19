# Dockerfile
FROM python:3.12-slim AS builder

WORKDIR /api

COPY requirements_api.txt .
RUN pip install --user --no-cache-dir -r requirements_api.txt
    
COPY ./api .

# Runtime stage
FROM python:3.12-slim

WORKDIR /
COPY --from=builder /root/.local /root/.local
COPY ./api ./api

COPY ./api/ckpt/model.pkl ./api/models/model.pkl

ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]