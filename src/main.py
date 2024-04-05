from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.routes.auth import router as auth_router
from src.routes.user import router as user_router
from src.routes.files import router as files_router
from src.db import create_tables

create_tables()
app = FastAPI()

templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse(url="/home")

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(files_router)
