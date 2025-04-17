FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies first
COPY pyproject.toml .
RUN pip install --no-cache-dir --upgrade pip

# Copy the entire project
COPY . .

# Now install the package in development mode
RUN pip install --no-cache-dir -e .

# Run the application
CMD ["python", "main.py"]

# Expose port
EXPOSE 8000 