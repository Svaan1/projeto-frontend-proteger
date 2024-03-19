from pydantic import BaseModel
from typing import List
from datetime import datetime

class UploadBase(BaseModel):
    id: int
    filename: str
    date: datetime

class UploadResponse(UploadBase):

    class Config:
        orm_mode = True
        exclude = ('user_id')
