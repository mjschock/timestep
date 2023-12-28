import logging
from typing import Annotated

import requests
from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from web.app.services.accounts import Account

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

security = HTTPBearer()

accounts_router = APIRouter(tags=["accounts"])


@accounts_router.on_event("startup")
async def startup():
    print("=== (print) Starting up accounts router ===")
    # logger.logger.info('=== (fastapi logger) Starting up accounts router ===')
    # logging.getLogger('uvicorn').info('=== (uvicorn logger) Starting up accounts router ===')  # noqa: E501
    logging.getLogger("root").info("=== (root logger) Starting up accounts router ===")
    logging.getLogger().info("=== (default logger) Starting up accounts router ===")
    logging.getLogger(__name__).info(
        "=== (__name__ logger) Starting up accounts router ==="
    )  # noqa: E501

    # accounts_router.state.accounts_service: AccountsService = await init_accounts_service()  # noqa: E501


# @accounts_router.post("")
# async def create_account(
#     credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
# ):
#     logger.debug("=== create_account ===")

#     # return {"scheme": credentials.scheme, "credentials": credentials.credentials}

#     response = requests.get(
#         "http://nhost-hasura-auth:4000/mfa/totp/generate",
#         headers={
#             "Authorization": f"Bearer {credentials.credentials}",
#         },
#     )

#     return response.json()


@accounts_router.put("/{account_id}")
async def update_account(
    account_id: str,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    account: Account,
):
    logger.debug("=== update_account ===")
    logger.debug(f"account_id: {account_id}")
    logger.debug(f"account: {account}")

    if account.totp_code:
        if account.activate_mfa_type == "totp":
            response = requests.post(
                "http://nhost-hasura-auth:4000/user/mfa",
                # auth=Auth,
                json={
                    "code": account.totp_code,
                    "activeMfaType": account.activate_mfa_type,
                },
                headers={
                    "Authorization": f"Bearer {credentials.credentials}",
                },
            )

        else:
            response = requests.post(
                "http://nhost-hasura-auth:4000/signin/mfa/totp",
                json={
                    # "code": user.totp_code,
                    "otp": account.totp_code,
                    "ticket": account.mfa.ticket,
                },
                headers={
                    "Authorization": f"Bearer {credentials.credentials}",
                },
            )

    # return response.json()
    return Response(
        content=response.content,
        status_code=response.status_code,
    )


@accounts_router.delete("/{account_id}")
async def delete_account(account_id: str):
    logger.debug("=== delete_account ===")
    logger.debug(f"account_id: {account_id}")

    return {
        "account_id": account_id,
    }
