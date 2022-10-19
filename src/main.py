import uvicorn
from fastapi import FastAPI

from handlers import base


app = FastAPI(
    title='Test task to the company "Digital Solutions Studio"',
    version='1.0',
)
app.include_router(base.router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
