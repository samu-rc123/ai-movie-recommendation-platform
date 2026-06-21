from app.services.recommender import (
    recommend_with_scores
)

from app.services.collaborative import model

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

        final_score = (
            0.6 * svd_score
            +
            0.4 * movie["content_score"]
        )

        hybrid_results.append(
            {
                "title":
                    movie["title"],

                "content_score":
                    round(
                        movie["content_score"],
                        3
                    ),

                "svd_score":
                    round(
                        float(svd_score),
                        3
                    ),

                "final_score":
                    round(
                        float(final_score),
                        3
                    )
            }
        )

    hybrid_results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return hybrid_results[:top_n]