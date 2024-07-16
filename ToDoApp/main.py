from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from starlette.staticfiles import StaticFiles
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Get the directory of the current file (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the static folder
static_dir = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
