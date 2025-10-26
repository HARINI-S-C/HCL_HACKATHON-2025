from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    kyc_status: str

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 ORM support
