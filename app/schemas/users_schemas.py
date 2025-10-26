from pydantic import BaseModel, EmailStr

# For creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# For login
class UserLogin(BaseModel):
    username: str
    password: str

# For output (what is returned to client)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # For Pydantic V2 (was orm_mode in V1)
