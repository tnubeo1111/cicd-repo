# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Set environment variables để không tạo file pyc và không buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cài đặt các package cần thiết để build (ví dụ build-essential, libpq-dev cho psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy file requirements để tận dụng cache Docker khi cài package
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code (nếu code thay đổi không quá thường xuyên, có thể copy sau khi cài dependencies để cache tốt hơn)
COPY . /app

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cài runtime dependencies cần thiết cho app chạy (vd: libpq-dev nếu dùng PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy các package python đã cài từ build stage sang
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy gunicorn executable
COPY --from=builder /usr/local/bin /usr/local/bin


# Copy source code app
COPY --from=builder /app /app

# Expose port mà Django app lắng nghe (mặc định là 8000)
EXPOSE 8000

CMD ["gunicorn", "hello_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
