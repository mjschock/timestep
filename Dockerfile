# FROM python:3-alpine
FROM ros:jazzy-ros-base-noble

# WORKDIR /app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["python", "main.py"]

CMD ["tail", "-f", "/dev/null"]
