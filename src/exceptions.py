from fastapi import HTTPException


UsernameAlreadyTaken = HTTPException(
    status_code=400,
    detail="A user with this name or email already exists."
)

InvalidUserName = HTTPException(
    status_code=400,
    detail="No user with this name exists."
)


InvalidPermissions = HTTPException(
    status_code=401,
    detail="You do not have permission for this action."
)


FileAlreadyExists = HTTPException(
    status_code=409,
    detail="File with given name already exists."
)

MissingFile = HTTPException(
    status_code=400,
    detail="Required file is missing."
)

InvalidFileType = HTTPException(
    status_code=400,
    detail="Invalid file type, only .xlsx files are allowed."
)

FileSizeExceeded = HTTPException(
    status_code=413,
    detail="File size exceeds the maximum allowed size (5 MB)."
)