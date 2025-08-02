from fastapi import FastAPI, Request, Header, HTTPException, Response
from fastapi.responses import JSONResponse
import httpx
from typing import Optional
import json

# App configuration
APP_NAME = "Timestep-OAI-Compatible-App"
APP_VERSION = "1.0.0"
USER_AGENT = f"{APP_NAME}/{APP_VERSION}"

# Import your existing API routers (no changes needed to these files!)
from APIs.fine_tuning import router as fine_tuning_router
from APIs.files import router as files_router
from APIs.chat import router as chat_router
from APIs.models import router as models_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Universal OpenAI-compatible fine-tuning and inference application"
)

# Mount your existing local APIs unchanged under /local/v1
app.include_router(fine_tuning_router, prefix="/local/v1", tags=["local-fine-tuning"])
app.include_router(files_router, prefix="/local/v1", tags=["local-files"])
app.include_router(chat_router, prefix="/local/v1", tags=["local-chat"])
app.include_router(models_router, prefix="/local/v1", tags=["local-models"])

# External provider configurations
EXTERNAL_PROVIDERS = {
    "openai": "https://api.openai.com/v1",
    "anyscale": "https://api.endpoints.anyscale.com/v1",
    "together": "https://api.together.xyz/v1",
    "anthropic": "https://api.anthropic.com/v1",
}

@app.get("/")
async def root():
    """API information and usage guide"""
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "description": "Universal OpenAI-compatible proxy supporting multiple AI providers",
        "usage": {
            "local": {
                "description": "Local SmolVLM2 and other models",
                "base_url": "/local/v1",
                "example": "OpenAI(api_key='anything', base_url='https://your-domain.com/local/v1')",
                "requires_auth": False
            },
            "external_providers": {
                provider: {
                    "description": f"{provider.title()} API proxy",
                    "base_url": f"/{provider}/v1",
                    "example": f"OpenAI(api_key='your-{provider}-key', base_url='https://your-domain.com/{provider}/v1')",
                    "requires_auth": True
                }
                for provider in EXTERNAL_PROVIDERS.keys()
            }
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": APP_NAME,
        "version": APP_VERSION,
        "providers": {
            "local": "available",
            **{provider: "proxy" for provider in EXTERNAL_PROVIDERS.keys()}
        }
    }

@app.api_route("/{provider}/v1/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def external_provider_proxy(
    provider: str,
    path: str,
    request: Request,
    authorization: Optional[str] = Header(None)
):
    """Proxy requests to external providers"""
   
    # Local provider is handled by mounted routers above
    if provider == "local":
        raise HTTPException(
            status_code=404,
            detail=f"Local routes are handled directly. Try: /local/v1/{path}"
        )
   
    # Check if provider exists
    if provider not in EXTERNAL_PROVIDERS:
        available_providers = list(EXTERNAL_PROVIDERS.keys()) + ["local"]
        raise HTTPException(
            status_code=404,
            detail=f"Unknown provider '{provider}'. Available: {available_providers}"
        )
   
    # Extract API key
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail=f"Authorization header required for {provider} provider"
        )
   
    api_key = authorization.replace("Bearer ", "")
    base_url = EXTERNAL_PROVIDERS[provider]
   
    # Proxy the request
    return await proxy_request_to_provider(base_url, path, request, api_key)

async def proxy_request_to_provider(
    base_url: str,
    path: str,
    request: Request,
    api_key: str
):
    """Generic proxy implementation for external providers"""
   
    method = request.method
    url = f"{base_url}/{path}"
   
    # Prepare headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": USER_AGENT
    }
   
    # Handle different request types
    content_type = request.headers.get("content-type", "")
   
    async with httpx.AsyncClient(timeout=300.0) as client:
        try:
            if "multipart/form-data" in content_type:
                # File uploads
                form = await request.form()
                files = {}
                data = {}
               
                for key, value in form.items():
                    if hasattr(value, 'read'):  # File object
                        files[key] = (value.filename, value.file, value.content_type)
                    else:
                        data[key] = value
               
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    files=files,
                    data=data
                )
           
            elif method in ["POST", "PUT", "PATCH"]:
                # JSON requests
                body = await request.body()
                if body:
                    headers["Content-Type"] = "application/json"
               
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    content=body
                )
           
            else:
                # GET, DELETE requests
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=dict(request.query_params)
                )
           
            # Return response (preserve headers except encoding ones)
            response_headers = {
                k: v for k, v in response.headers.items()
                if k.lower() not in ['content-encoding', 'transfer-encoding']
            }
           
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=response_headers
            )
           
        except httpx.TimeoutException:
            raise HTTPException(status_code=504, detail=f"Request to {base_url} timed out")
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"Failed to connect to {base_url}: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Proxy error: {str(e)}")

# Optional: Add provider management endpoints
@app.get("/providers")
async def list_providers():
    """List all available providers"""
    return {
        "providers": {
            "local": {
                "type": "local",
                "description": "Local models (SmolVLM2, etc.)",
                "base_url": "/local/v1",
                "requires_auth": False,
                "status": "available"
            },
            **{
                name: {
                    "type": "external",
                    "description": f"{name.title()} API proxy",
                    "base_url": f"/{name}/v1",
                    "requires_auth": True,
                    "status": "proxy"
                }
                for name in EXTERNAL_PROVIDERS.keys()
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)