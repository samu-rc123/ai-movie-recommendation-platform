from fastapi import FastAPI
from app.api.recommend import router

app = FastAPI(
    title="AI Movie Recommendation API",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Movie Recommendation API Running"
    }