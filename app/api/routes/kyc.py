from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import KYC, User
from app.utils.auth import get_current_user, admin_required

router = APIRouter()

@router.post("/upload")
def upload_kyc(file: UploadFile = File(...), current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    kyc = KYC(user_id=current_user.id, document_path=file.filename)
    db.add(kyc)
    db.commit()
    db.refresh(kyc)
    return {"msg": "KYC uploaded"}

@router.get("/status")
def kyc_status(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    kyc = db.query(KYC).filter(KYC.user_id == current_user.id).first()
    if not kyc:
        return {"status": "No KYC uploaded"}
    return {"status": kyc.status}

@router.patch("/verify/{user_id}")
def verify_kyc(user_id: int, approved: bool, current_user=Depends(admin_required), db: Session = Depends(get_db)):
    kyc = db.query(KYC).filter(KYC.user_id == user_id).first()
    if not kyc:
        raise HTTPException(status_code=404, detail="KYC not found")
    kyc.status = "approved" if approved else "rejected"
    db.commit()
    return {"msg": f"KYC {'approved' if approved else 'rejected'}"}
