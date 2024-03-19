from fastapi import APIRouter, Depends, UploadFile

from src.db import get_session
from src.db.actions import *
from src.security import manager
from src.exceptions import FileAlreadyExists, MissingFile, InvalidFileType, InvalidPermissions, FileSizeExceeded
from src.scripts.sheets import transform_file_data

from src.models.file import UploadResponse

from sqlalchemy.exc import IntegrityError

import shutil
from pathlib import Path

UPLOADS_DIRECTORY = "./src/static/uploads/"

router = APIRouter(prefix="/files")

@router.get("/", response_model=list[UploadResponse])
def get_user_files(active_user=Depends(manager), db=Depends(get_session)) -> list[UploadResponse]:
    """
    Returns list of files from the upload table belonging to the user
    """
    return get_uploads_from_user(active_user, db)


@router.post("/", status_code=201)
async def upload_file(file: UploadFile | None = None, active_user=Depends(manager), db=Depends(get_session)) -> None:
    """
    Uploads raw file (.xlsx) to storage and turns it into organized database tables 
    """
    if file is None:
        raise MissingFile
    
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise InvalidFileType

    if file.size > 5000000:
        raise FileSizeExceeded
    
    try:
        upload = create_upload(active_user, file.filename, db)
    except IntegrityError:
        raise FileAlreadyExists
        
    forms, residents = transform_file_data(file.file)

    create_forms_and_residents_from_list(upload, forms, residents, db)

    file.file.seek(0)

    shutil.os.makedirs(UPLOADS_DIRECTORY, exist_ok=True)
    with open(UPLOADS_DIRECTORY + file.filename, "wb") as f:
        shutil.copyfileobj(file.file, f)

    db.commit()
    return
    
@router.delete("/{upload_id}", status_code=204)
def delete_file(upload_id: int, active_user=Depends(manager), db=Depends(get_session)) -> None:
    upload = get_upload_by_id(upload_id, db)

    if not upload:
        return

    if upload.user_id != active_user.id:
        raise InvalidPermissions
    
    delete_upload_by_id(upload_id, db)

    file_path = Path(UPLOADS_DIRECTORY + upload.filename)

    if file_path.exists():
        file_path.unlink()

    db.commit()
    return

