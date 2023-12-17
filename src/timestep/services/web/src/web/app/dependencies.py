from typing import Annotated

from fastapi import Depends, Header, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# from .services.agents import AgentsService, init_agents_service

security = HTTPBearer()


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


# credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    # current_user = await get_user(credentials.credentials)
    # return current_user
    print("credentials", credentials)
    return credentials
