from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.auth import router as auth_router
from src.routes.user import router as user_router
from src.routes.files import router as files_router
from src.db import create_tables

create_tables()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: configure right allow_origins, leaving it as * for now

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(files_router)

@app.get("/")
async def root():
    return {"Hello": "World"}