FROM ros:jazzy-ros-base-noble

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8550

ENV BACKEND_URL=http://backend-service:8000

CMD ["python", "main.py"]
