from app.schemas.kyc_schema import KYCUpload, KYCStatus  # <- absolute import

# Simulate ORM objects
class KYCUploadORM:
    def __init__(self, document_type, document_url):
        self.document_type = document_type
        self.document_url = document_url

class KYCStatusORM:
    def __init__(self, status, verified_by=None):
        self.status = status
        self.verified_by = verified_by

# Create fake ORM instances
fake_upload = KYCUploadORM("passport", "https://example.com/passport.pdf")
fake_status = KYCStatusORM("verified", "AdminUser")

# Convert ORM objects to Pydantic models
upload_schema = KYCUpload.from_orm(fake_upload)
status_schema = KYCStatus.from_orm(fake_status)

print(upload_schema)
print(status_schema)
print("✅ KYCUpload and KYCStatus schemas work correctly with ORM")
