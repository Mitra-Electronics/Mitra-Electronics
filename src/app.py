from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from src.blog.router import router as brouter

BASE_DIR = Path(__file__).parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR/"static"), name="static")
app.mount("/", brouter)


@app.get("/")
async def status():
    return {"status": 200}
