from fastapi import APIRouter
import pandas as pd
from pathlib import Path
from huggingface_hub import hf_hub_download
import joblib


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

REPO_ID = "Samrc2255/movie-recommendation-models"
movies_path = hf_hub_download(
    repo_id=REPO_ID,
    filename="movies.pkl"
)

movies = joblib.load(movies_path)

@router.get("/movies/search/{query}")
def search_movies(query: str):

    results = movies[
        movies["title"].str.contains(
            query,
            case=False,
            na=False
        )
    ]["title"].head(10)

    return results.tolist()