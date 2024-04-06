from pydantic import BaseModel
from datetime import datetime

class UploadBase(BaseModel):
    id: int
    filename: str
    datetime: datetime

class UploadResponse(UploadBase):

    class Config:
        from_attributes = True
        exclude = ('user_id')
