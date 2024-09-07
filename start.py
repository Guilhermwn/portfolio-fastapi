import uvicorn
from portfolio.main import app

if __name__ == '__main__':
    uvicorn.run(app='portfolio.main:app', reload=True)
    # uvicorn.run('main:app', host='192.168.1.10', reload=True)