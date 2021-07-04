from fastapi import FastAPI

from src.routes.lists import one

app = FastAPI(
    title='EEL7053 equations'
)

app.include_router(one.router, tags=['List 1'])