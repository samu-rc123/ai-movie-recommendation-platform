from fastapi import APIRouter

from app.services.recommender import (
    recommend_with_scores
)

router = APIRouter()

@router.get("/recommend/{movie_name}")
def get_recommendations(
    movie_name: str
):

    recommendations = recommend_with_scores(
        movie_name
    )

    return {
        "movie": movie_name,
        "recommendations": recommendations
    }