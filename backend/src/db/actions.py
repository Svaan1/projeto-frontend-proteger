from typing import Optional

from src.db import SessionLocal
from src.db.models import User, Upload, Form, Resident
from src.security import hash_password, manager
from sqlalchemy.orm import Session

from datetime import datetime

def get_user_by_name(name: str, db: Session) -> Optional[User]:
    """
    Queries the database for a user with the given name

    Args:
        name: The name of the user
        db: The currently active database session

    Returns:
        The user object or none
    """
    user = db.query(User).where(User.username == name).first()
    return user


@manager.user_loader()
def get_user(name: str):
    with SessionLocal() as db:
        return get_user_by_name(name, db)


def create_user(name: str, password: str, email: str, db: Session) -> User:
    """
    Creates and commits a new user object to the database

    Args:
        name: The name of the user
        password: The plaintext password
        db: The active db session

    Returns:
        The newly created user.
    """
    hashed_pw = hash_password(password)
    user = User(username=name, password=hashed_pw, email=email)
    db.add(user)
    db.commit()
    return user

def create_upload(user: User, filename: str, db: Session) -> Upload:
    """
    Creates and commits a new upload object to the database

    Args:
        user: The owner of the file
        filename: The name of the created file
        db: The active db session

    Returns:
        The newly created upload.
    """
    upload = Upload(filename=filename, datetime=datetime.now(), user=user)
    db.add(upload)
    db.flush()
    return upload

def create_forms_and_residents_from_list(upload: Upload, form_list: list, resident_list: list, db: Session) -> None:
    """
    Creates and commits new form and resident objects to the database based on input lists.

    Args:
        upload: Upload object 
        form_list: List of dictionaries containing form data
        resident_list: List of lists, each containing dictionaries representing resident data corresponding to forms
        db: The active db session.

    Returns:
        None
    """
    for index, form in enumerate(form_list):
        new_form = Form(**form, upload=upload)
        db.add(new_form)

        for resident in resident_list[index]:
            new_resident = Resident(form=new_form, **resident)
            db.add(new_resident)
        
    db.flush()

def get_uploads_from_user(user: User, db: Session) -> list[Upload]:
    """
    Retrieves all uploads associated with a specific user from the database.
    
    Args:
        user: User object representing the owner of the uploads.
        db: The active db session

    Returns:
        A list of Upload objects belonging to the specified user
    """
    uploads = db.query(Upload).where(Upload.user_id == user.id).all()
    return uploads

def get_upload_by_id(upload_id: int, db: Session) -> Upload:
    """
    
    Retrieves an upload from the database based on its ID.
    Args:
        upload_id: The file id
        db: The active db session.

    Returns:
        The Upload object with the specified ID, or None if not found.
    """
    upload = db.query(Upload).where(Upload.id == upload_id).first()
    return upload

def delete_upload_by_id(upload_id: int, db: Session) -> None:
    """
    Deletes an upload from the database based on its ID.
    Args:
        upload_id: The ID of the upload to be deleted.
        db: The active db session.

    Returns:
        None
    """
    upload = get_upload_by_id(upload_id, db)
    db.delete(upload)
    db.flush()