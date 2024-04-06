from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

from src.db.actions import create_user, get_user_by_name
from src.models.user import UserCreate
from src.db import get_session
from src.db.actions import get_user_by_name
from src.models.token import Token
from src.security import verify_password, manager
from src.exceptions import UsernameAlreadyTaken
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/auth"
)


@router.post("/register", response_model=Token, status_code=201)
def register(user: UserCreate, db=Depends(get_session)) -> Token:
    """
    Registers a new user
    """
    try:
        user = create_user(user.username, user.password,
                           user.age, user.email, db)
        token = manager.create_access_token(data={'sub': user.username})
        return Token(access_token=token, token_type='Bearer')
    except IntegrityError:
        raise UsernameAlreadyTaken


@router.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)) -> Token:
    """
    Logs in the user provided by form_data.username and form_data.password
    """
    user = get_user_by_name(form_data.username, db)
    if user is None:
        raise InvalidCredentialsException

    if not verify_password(form_data.password, user.password):
        raise InvalidCredentialsException

    token = manager.create_access_token(data={'sub': user.username})
    return Token(access_token=token, token_type='Bearer')
