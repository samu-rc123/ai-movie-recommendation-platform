from fastapi import APIRouter

from app.services.recommender import (
    recommend_with_scores
)
from app.services.hybrid import (
    hybrid_recommend
)
from app.services.sentiment import (
    analyze_sentiment
)

from app.schemas.recommend import (
    RecommendationRequest
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
@router.post("/recommend-with-review")
def recommend_with_review(
    request: RecommendationRequest
):

    review_sentiment = analyze_sentiment(
        request.review
    )

    recommendations = hybrid_recommend(
        request.user_id,
        request.movie
    )

    if review_sentiment["label"] == "POSITIVE":
        multiplier = 1.05
    else:
        multiplier = 0.95

    for movie in recommendations:

        movie["adjusted_score"] = round(
            movie["final_score"] * multiplier,
            3
        )

    recommendations.sort(
        key=lambda x: x["adjusted_score"],
        reverse=True
    )

    return {
        "review_sentiment": review_sentiment,
        "recommendations": recommendations
    }