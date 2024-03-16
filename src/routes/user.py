from src.db import get_session
from src.db.actions import create_user, get_user_by_name
from src.models.user import UserCreate, UserResponse
from src.exceptions import InvalidPermissions, InvalidUserName
from src.security import manager
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/user")


@router.get("/{username}")
def read_user(
    username, active_user=Depends(manager), db=Depends(get_session)
) -> UserResponse:
    """
    Shows information about the user
    """
    user = get_user_by_name(username, db)

    if user is None:
        raise InvalidUserName

    if user.username != active_user.username:
        raise InvalidPermissions

    return UserResponse.model_validate(user)
