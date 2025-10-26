from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.db.models import User
from app.schemas.users_schemas import UserOut  # Pydantic schema for User
from app.utils.auth import get_current_user, admin_required

router = APIRouter()

# -------------------------------
# Get current logged-in user
# -------------------------------

@router.get("/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/all", response_model=list[UserOut])
def get_all_users(current_user=Depends(admin_required), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users