from fastapi import APIRouter

from app.services.recommender import (
    recommend_with_scores
)
from app.services.hybrid import (
    hybrid_recommend
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
@router.get("/hybrid-test")
def hybrid_test():

    return hybrid_recommend(
        user_id=1,
        movie_name="Avatar"
    )