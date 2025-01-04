# FROM ros:jazzy-ros-base-noble
FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# ENV BACKEND_URL=http://backend-service:8000
ENV BACKEND_URL=http://backend.default.svc.cluster.local:8080

CMD ["python", "main.py"]
