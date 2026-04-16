FROM python:3.12-slim

WORKDIR /app

# System dependencies (important for pandas, sklearn)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install torch separately (CPU version)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy project files
COPY . .

# Make script executable
RUN chmod +x start.sh

# Expose ports
EXPOSE 8000 8501

# Start services
CMD ["/app/start.sh"]