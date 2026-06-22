from fastapi import APIRouter
import pandas as pd
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

movies = pd.read_csv(
    BASE_DIR / "data/processed/final_movies.csv"
)

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