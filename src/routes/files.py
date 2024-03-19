from fastapi import APIRouter, Depends, UploadFile

from src.db import get_session
from src.db.actions import create_upload, create_forms_and_residents_from_list, get_uploads_from_user
from src.security import manager
from src.exceptions import FileAlreadyExists, MissingFile, InvalidFileType
from src.scripts.sheets import transform_file_data

from src.models.file import UploadResponse

from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/files")

@router.get("/", response_model=list[UploadResponse])
def get_user_files(active_user=Depends(manager), db=Depends(get_session)) -> list[UploadResponse]:
    """
    Returns list of files from the upload table belonging to the user
    """
    return get_uploads_from_user(active_user, db)


@router.post("/", status_code=201)
def upload_file(file: UploadFile | None = None, active_user=Depends(manager), db=Depends(get_session)) -> None:
    """
    Uploads raw file (.xlsx) to storage and turns it into organized database tables 
    """
    if file is None:
        raise MissingFile
    
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise InvalidFileType

    try:
        upload = create_upload(active_user, file.filename, db)
    except IntegrityError:
        raise FileAlreadyExists
        
    forms, residents = transform_file_data(file.file)

    create_forms_and_residents_from_list(upload, forms, residents, db)

    db.commit()
    

