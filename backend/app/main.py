from fastapi import FastAPI
from app.api.movies import router as movie_router

app = FastAPI()

app.include_router(movie_router)

@app.get("/")
def home():
    return {"message": "OK"}