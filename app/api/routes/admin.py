from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import KYC
from app.utils.auth import admin_required

router = APIRouter()

@router.get("/kyc/pending")
def pending_kyc(current_user=Depends(admin_required), db: Session = Depends(get_db)):
    pending = db.query(KYC).filter(KYC.status == "pending").all()
    return pending
