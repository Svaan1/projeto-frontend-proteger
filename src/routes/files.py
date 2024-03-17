from fastapi import APIRouter, Depends, UploadFile

from src.db import get_session
from src.db.actions import create_upload
from src.security import manager
from src.exceptions import FileAlreadyExists

from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/files")

@router.get("/")
def get_user_files(active_user=Depends(manager), db=Depends(get_session)):
    """
    Returns list of files from the upload table belonging to the user
    """
    pass

@router.post("/")
def upload_file(file: UploadFile, active_user=Depends(manager), db=Depends(get_session)):
    """
    Uploads raw file (.xlsx) to storage and turns it into organized database tables 
    """
    try:
        upload = create_upload(active_user, file.filename, db)
    except IntegrityError:
        raise FileAlreadyExists
    
    db.commit()
    pass