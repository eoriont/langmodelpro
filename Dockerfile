# Dockerfile
FROM python:3.9-slim
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app
COPY . .

EXPOSE 8000
