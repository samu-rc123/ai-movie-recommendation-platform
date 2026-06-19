from fastapi import APIRouter
from app.services.recommender import recommend

router = APIRouter()


@router.get("/recommend/{movie_name}")
def get_recommendations(movie_name: str):
    recommendations = recommend(movie_name)

    if not recommendations:
        return {
            "error": "Movie not found"
        }

    return {
        "movie": movie_name,
        "recommendations": recommendations
    }