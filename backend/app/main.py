from fastapi import FastAPI
from app.api.recommend import router
from app.api.sentiment import router as sentiment_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.movies import router as movie_router
from app.api.report import (
    router as report_router
)


app = FastAPI(
    title="AI Movie Recommendation API",
    version="1.0"
)
app.include_router(movie_router)
app.include_router(
    report_router
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(
    sentiment_router
)

@app.get("/")
def home():
    return {
        "message": "Movie Recommendation API Running"
    }