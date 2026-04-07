FROM python:3.12-slim

WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies with timeout fix
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy all project files
COPY . .

# Make startup script executable
RUN chmod +x start.sh

# Expose ports
EXPOSE 8000 8501

# Run both API + UI
CMD ["./start.sh"]