from fastapi import FastAPI
from app.api.movies import router as movie_router
from app.api.report import (router as report_router)

app = FastAPI()

app.include_router(movie_router)
app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "OK"}