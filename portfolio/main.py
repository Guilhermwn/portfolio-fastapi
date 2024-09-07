from fastapi import FastAPI

from .utils import render
from .views.home import homepage

from pathlib import Path
BASE_DIR = Path(__file__).parent

from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/assets", StaticFiles(directory=BASE_DIR/"assets"), name="assets")

from fastapi.responses import HTMLResponse
@app.get('/', response_class=HTMLResponse)
async def home(): 
    return render(homepage())
