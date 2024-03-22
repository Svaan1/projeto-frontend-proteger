from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.routes.auth import router as auth_router
from src.routes.user import router as user_router
from src.db import create_tables

create_tables()  # Create the tables in the database if they don't exist
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Redirect to the home page
    return RedirectResponse(url="/home")

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    # Render the home.html template
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    # Redirect to the home page
    return RedirectResponse(url="/home")

@app.get("/upload.html", response_class=HTMLResponse)
async def upload(request: Request):
    # Render the upload.html template
    return templates.TemplateResponse("upload.html", {"request": request})

app.include_router(auth_router)
app.include_router(user_router)

# @app.get ("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#   return templates.TemplateResponse(
#       request=request, name="item.html", context={"id": id}
#   )