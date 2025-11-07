# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --no-deps -r requirements.txt && pip install --no-cache-dir --ignore-installed -r requirements.txt

# Copy .env.example as a template (if it doesn't exist, create it first)
RUN touch .env.example
COPY .env.example .
RUN cp .env.example .env

# Copy all project files
COPY . .

# Expose port (optional, e.g., for FastAPI or Streamlit)
EXPOSE 8000

# Default command (runs demo.py, change as needed)
CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8000", "demo.py"]
