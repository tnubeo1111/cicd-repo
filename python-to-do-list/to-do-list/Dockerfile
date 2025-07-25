FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Turn off .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev 

# Copy requirements file
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Expose port mà Django dùng (mặc định 8000)
EXPOSE 8000

# Lệnh chạy server Django với IP 0.0.0.0 để container có thể expose ra ngoài
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]