from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_DIR = Path(__file__).parent

app = FastAPI()
app.mount("/assets", StaticFiles(directory=BASE_DIR/"assets"), name="assets")

templates = Jinja2Templates(directory='templates')


def template_response(html: str, request: Request, **kwargs):
    context = {"request": request}
    context.update(kwargs)
    return templates.TemplateResponse(html, context)

# @app.get('/favicon.ico', include_in_schema=False)
# async def favicon():
#     return FileResponse(favicon_path)

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    pages = {
        'Links': '/links',
        'Projetos': '/projetos',
        'Sobre': '/sobre'
    }
    return template_response(
        'home.html', 
        request=request, 
        pages=pages, 
        title='Home'
    )


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='192.168.1.10', reload=True)