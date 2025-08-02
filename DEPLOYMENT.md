# Deployment Guide

## Quick Start

### Option 1: Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Docker

```bash
# Build and run with Docker
docker build -t timestep-oai-app .
docker run -p 8000:8000 timestep-oai-app
```

### Option 3: Docker Compose

```bash
# Start with docker-compose
docker-compose up -d

# Stop services
docker-compose down
```

## Production Deployment

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

The application uses the following environment variables:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

### 3. Running in Production

#### Using Gunicorn (Recommended)

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### Using Docker in Production

```bash
# Build production image
docker build -t timestep-oai-app:latest .

# Run with proper resource limits
docker run -d \
  --name timestep-oai-app \
  -p 8000:8000 \
  --memory=2g \
  --cpus=2 \
  timestep-oai-app:latest
```

### 4. Reverse Proxy Setup (Nginx)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 5. SSL/HTTPS Setup

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com
```

## Monitoring and Health Checks

### Health Check Endpoint

The application provides a health check endpoint at `/health`:

```bash
curl http://localhost:8000/health
```

### Docker Health Check

The Docker image includes a health check that runs every 30 seconds.

### Logging

For production, consider adding structured logging:

```python
import logging
from fastapi import FastAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI()
```

## Security Considerations

### 1. API Key Management

- Store API keys securely (use environment variables or secrets management)
- Rotate keys regularly
- Use different keys for different environments

### 2. Rate Limiting

Consider implementing rate limiting:

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

### 3. CORS Configuration

Configure CORS for production:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Scaling

### Horizontal Scaling

1. **Load Balancer**: Use a load balancer (HAProxy, Nginx) to distribute traffic
2. **Multiple Instances**: Run multiple instances of the application
3. **Database**: Use a shared database for persistent storage

### Vertical Scaling

1. **Resource Limits**: Adjust Docker resource limits
2. **Worker Processes**: Increase Gunicorn workers
3. **Memory**: Allocate more memory for large models

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   # Kill process
   kill -9 <PID>
   ```

2. **Memory Issues**
   ```bash
   # Check memory usage
   docker stats timestep-oai-app
   ```

3. **Connection Issues**
   ```bash
   # Test connectivity
   curl -v http://localhost:8000/health
   ```

### Logs

```bash
# View application logs
docker logs timestep-oai-app

# Follow logs
docker logs -f timestep-oai-app
```

## Performance Optimization

### 1. Caching

Implement caching for model responses:

```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8")
    FastAPICache.init(RedisBackend(redis), prefix="timestep-cache")
```

### 2. Database Optimization

- Use connection pooling
- Implement proper indexing
- Consider read replicas for high read loads

### 3. Model Optimization

- Use model quantization
- Implement model caching
- Consider model serving optimization

## Backup and Recovery

### 1. Database Backups

```bash
# PostgreSQL backup
pg_dump timestep_oai > backup.sql

# Restore
psql timestep_oai < backup.sql
```

### 2. Configuration Backups

```bash
# Backup configuration
cp .env .env.backup
cp docker-compose.yml docker-compose.yml.backup
```

### 3. Application Backups

```bash
# Backup application
tar -czf timestep-oai-backup.tar.gz .
```

## Support

For deployment issues:

1. Check the logs: `docker logs timestep-oai-app`
2. Verify configuration: `curl http://localhost:8000/health`
3. Test connectivity: `curl http://localhost:8000/`
4. Check resource usage: `docker stats timestep-oai-app`