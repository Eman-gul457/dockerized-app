# 1) Small Python base
FROM python:3.12-slim

# 2) Friendlier Python runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Workdir
WORKDIR /app

# 4) Non-root user
RUN adduser --disabled-password --gecos '' appuser

# 5) Copy deps first
COPY requirements.txt .

# 6) Install deps + curl (for HEALTHCHECK)
RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# 7) Copy app code
COPY app ./app

# 8) Ports & env
ENV APP_PORT=5000
EXPOSE 5000

# 9) Healthcheck
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:${APP_PORT}/healthz || exit 1

# 10) Drop privileges
USER appuser

# 11) Run with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.app:app"]
