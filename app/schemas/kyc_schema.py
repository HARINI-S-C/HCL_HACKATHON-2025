# from pydantic import BaseModel, ConfigDict

# class KYCUpload(BaseModel):
#     document_type: str
#     document_url: str

#     model_config = ConfigDict(from_attributes=True)  # For ORM support

# class KYCStatus(BaseModel):
#     status: str
#     verified_by: str | None = None

#     model_config = ConfigDict(from_attributes=True)



from pydantic import BaseModel, ConfigDict

class KYCUpload(BaseModel):
    document_type: str
    document_url: str

    model_config = ConfigDict(from_attributes=True)

class KYCStatus(BaseModel):
    status: str
    verified_by: str | None = None

    model_config = ConfigDict(from_attributes=True)
