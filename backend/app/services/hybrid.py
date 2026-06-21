from app.services.recommender import (recommend_with_scores
)
from data.movie_reviews import movie_reviews
from app.services.sentiment import (
    aggregate_sentiment
)
from app.services.collaborative import model
from pathlib import Path
import json
from app.services.explain import (generate_explanation)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(
    BASE_DIR / "data/movie_sentiments.json",
    "r",
    encoding="utf-8"
) as f:
    sentiments = json.load(f)


def hybrid_recommend(
    user_id,
    movie_name,
    top_n=5
):

    candidates = recommend_with_scores(
        movie_name,
        top_n=20
    )

    hybrid_results = []

    for movie in candidates:

        movie_id = movie["movie_id"]

        svd_score = model.predict(
            user_id,
            movie_id
        ).est
        reviews = movie_reviews.get(
        movie["title"],
        ["Average movie"]
        )
        sentiment_score = aggregate_sentiment(
        reviews
        )
        normalizes_svd = svd_score / 5.0

        final_score = (
            0.5 * normalizes_svd
            +
            0.3 * float(movie["content_score"])
            +
            0.2 * sentiment_score
        )

        hybrid_results.append(
            {
        "title": movie["title"],

        "content_score":
            round(float(movie["content_score"]), 3),

        "svd_score":
            round(float(svd_score), 3),

        "sentiment_score":
            round(float(sentiment_score), 3),

        "final_score":
            round(float(final_score), 3),
        "explaination":
            generate_explanation(
                movie_name,
                float(movie["content_score"]),
                float(svd_score),
                float(sentiment_score)
            )
    }
        )

    hybrid_results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return hybrid_results[:top_n]

