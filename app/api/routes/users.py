from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.utils.auth import get_current_user, admin_required

router = APIRouter()

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/all")
def get_all_users(current_user=Depends(admin_required), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
