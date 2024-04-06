from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    username: str
    age: int
    email: str
    password: str


class UserResponse(UserCreate):

    model_config = ConfigDict(from_attributes=True)
