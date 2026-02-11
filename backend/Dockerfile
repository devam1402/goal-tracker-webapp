# -------------------------------
# 1. Build stage
# -------------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

# System deps (only what we need)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install deps separately (cache friendly)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -------------------------------
# 2. Runtime stage
# -------------------------------
FROM python:3.11-slim

# Security: non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy only app code
COPY app app

# Change ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Production server
CMD ["gunicorn", "app.main:app", \
     "-k", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "4", \
     "--threads", "2"]
