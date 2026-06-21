from fastapi import APIRouter

from app.schemas.sentiment import (
    ReviewRequest,
    ReviewsRequest
)

from app.services.sentiment import (
    analyze_sentiment,
    aggregate_sentiment
)

router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment Analysis"]
)
@router.post("/")
def analyze_review(
    request: ReviewRequest
):

    result = analyze_sentiment(
        request.review
    )

    return result

@router.post("/aggregate")
def aggregate_reviews(
    request: ReviewsRequest
):

    score = aggregate_sentiment(
        request.reviews
    )

    return {
        "aggregate_sentiment": score
    }