from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('index.jinja', context)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='192.168.1.10')