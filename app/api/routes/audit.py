from fastapi import APIRouter, Depends
from app.utils.auth import admin_required

router = APIRouter()

@router.get("/logs")
def audit_logs(current_user=Depends(admin_required)):
    # Just a dummy response
    return [{"user": "testuser", "kyc_status": "approved"}]
