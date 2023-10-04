from fastapi import FastAPI
from routes.routers import router

app = FastAPI()

app.include_router(router)

