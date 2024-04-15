from src.db import get_session
from src.db.actions import create_user, get_user_by_name
from src.models.user import UserCreate, UserResponse
from src.exceptions import InvalidPermissions, InvalidUserName
from src.security import manager
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/user")


@router.get("/")
def read_user(active_user=Depends(manager)) -> UserResponse:
    return active_user
