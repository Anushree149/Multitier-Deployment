# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
