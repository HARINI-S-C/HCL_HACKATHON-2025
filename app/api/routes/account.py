from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.account_schema import AccountCreate, AccountResponse
from app.db.models import Account, User
from app.db.session import get_db
import random

router = APIRouter()

@router.post("/create", response_model=AccountResponse)
def create_account(request: AccountCreate, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    acc_no = "SB" + str(random.randint(10000000, 99999999))
    account = Account(user_id=user.id, account_type=request.account_type, account_number=acc_no)
    
    db.add(account)
    db.commit()
    db.refresh(account)
    
    return account
