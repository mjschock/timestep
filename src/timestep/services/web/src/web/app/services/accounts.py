from pydantic import BaseModel, Field


class Mfa(BaseModel):
    enabled: bool = Field(None)
    ticket: str = Field(None)
    type: str = Field(None)


class Account(BaseModel):
    activate_mfa_type: str = Field("", alias="activateMfaType")
    mfa: Mfa = Field(None)
    totp_code: str = Field("", alias="totpCode")


class AccountsService:
    def __init__(self):
        pass

    async def create_account(self, account: Account):
        pass


async def init_accounts_service():
    return AccountsService()
