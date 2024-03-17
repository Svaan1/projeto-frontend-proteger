from typing import Optional

from src.db import SessionLocal
from src.db.models import User, Upload
from src.security import hash_password, manager
from sqlalchemy.orm import Session

from datetime import date

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


def create_user(name: str, password: str, age: int, email: str, db: Session) -> User:
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
    user = User(username=name, password=hashed_pw, age=age, email=email)
    db.add(user)
    db.commit()
    return user

def create_upload(user: User, filename: str, db: Session) -> Upload:
    """
    Creates and commits a new upload object to the database
    Args:
        user: the owner of the file
        filename: The name of the created file
        db: The active db session

    Returns:
        The newly created upload.
    """
    upload = Upload(filename=filename, date=date.today(), user=user)
    db.add(upload)
    db.commit()
    return upload