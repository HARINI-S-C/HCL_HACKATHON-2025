from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_type: str

class AccountResponse(BaseModel):
    id: int
    user_id: int
    account_number: str
    account_type: str
    balance: int

    class Config:
        orm_mode = True
