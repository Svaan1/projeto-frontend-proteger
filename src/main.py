from fastapi import FastAPI

from src.routes.auth import router as auth_router
from src.routes.user import router as user_router
from src.routes.files import router as files_router
from src.db import create_tables

create_tables()  # Create the tables in the database if they don't exist
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(files_router)
